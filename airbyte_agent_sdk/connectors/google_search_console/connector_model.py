"""
Connector model for google-search-console.

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

GoogleSearchConsoleConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('eb4c9e00-db83-4d63-a386-39cfa91012a8'),
    name='google-search-console',
    version='1.0.3',
    base_url='https://www.googleapis.com/webmasters/v3',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://oauth2.googleapis.com/token',
        },
        user_config_spec=AuthConfigSpec(
            title='OAuth2 Authentication',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='The client ID of your Google Search Console developer application.',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='The client secret of your Google Search Console developer application.',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='The refresh token for obtaining new access tokens.',
                ),
            },
            auth_mapping={
                'refresh_token': '${refresh_token}',
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
            },
            replication_auth_key_mapping={
                'authorization.client_id': 'client_id',
                'authorization.client_secret': 'client_secret',
                'authorization.refresh_token': 'refresh_token',
            },
            replication_auth_key_constants={'authorization.auth_type': 'Client'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='sites',
            stream_name='sites',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/sites',
                    action=Action.LIST,
                    description="Lists the user's Search Console sites.",
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of sites.',
                        'properties': {
                            'siteEntry': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Search Console site resource.',
                                    'properties': {
                                        'siteUrl': {
                                            'type': ['null', 'string'],
                                            'description': 'The URL of the property. Examples: http://www.example.com/ (for a URL-prefix property) or sc-domain:example.com (for a Domain property).\n',
                                        },
                                        'permissionLevel': {
                                            'type': ['null', 'string'],
                                            'description': "The user's permission level for the site. Values: siteFullUser, siteOwner, siteRestrictedUser, siteUnverifiedUser.\n",
                                        },
                                    },
                                    'x-airbyte-entity-name': 'sites',
                                    'x-airbyte-stream-name': 'sites',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Verified sites in Google Search Console',
                                        'when_to_use': 'Questions about which websites are tracked in Search Console',
                                        'trigger_phrases': ['search console site', 'verified site', 'tracked website'],
                                        'freshness': 'live',
                                        'example_questions': ['What sites are in Google Search Console?'],
                                        'search_strategy': 'List all verified sites',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.siteEntry',
                    no_pagination='Google Search Console GET /sites returns all verified sites for the authenticated user in a single response; no pagination cursor, offset, or page token is exposed.',
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sites/{siteUrl}',
                    action=Action.GET,
                    description='Retrieves information about a specific site.',
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Search Console site resource.',
                        'properties': {
                            'siteUrl': {
                                'type': ['null', 'string'],
                                'description': 'The URL of the property. Examples: http://www.example.com/ (for a URL-prefix property) or sc-domain:example.com (for a Domain property).\n',
                            },
                            'permissionLevel': {
                                'type': ['null', 'string'],
                                'description': "The user's permission level for the site. Values: siteFullUser, siteOwner, siteRestrictedUser, siteUnverifiedUser.\n",
                            },
                        },
                        'x-airbyte-entity-name': 'sites',
                        'x-airbyte-stream-name': 'sites',
                        'x-airbyte-ai-hints': {
                            'summary': 'Verified sites in Google Search Console',
                            'when_to_use': 'Questions about which websites are tracked in Search Console',
                            'trigger_phrases': ['search console site', 'verified site', 'tracked website'],
                            'freshness': 'live',
                            'example_questions': ['What sites are in Google Search Console?'],
                            'search_strategy': 'List all verified sites',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Search Console site resource.',
                'properties': {
                    'siteUrl': {
                        'type': ['null', 'string'],
                        'description': 'The URL of the property. Examples: http://www.example.com/ (for a URL-prefix property) or sc-domain:example.com (for a Domain property).\n',
                    },
                    'permissionLevel': {
                        'type': ['null', 'string'],
                        'description': "The user's permission level for the site. Values: siteFullUser, siteOwner, siteRestrictedUser, siteUnverifiedUser.\n",
                    },
                },
                'x-airbyte-entity-name': 'sites',
                'x-airbyte-stream-name': 'sites',
                'x-airbyte-ai-hints': {
                    'summary': 'Verified sites in Google Search Console',
                    'when_to_use': 'Questions about which websites are tracked in Search Console',
                    'trigger_phrases': ['search console site', 'verified site', 'tracked website'],
                    'freshness': 'live',
                    'example_questions': ['What sites are in Google Search Console?'],
                    'search_strategy': 'List all verified sites',
                },
            },
            ai_hints={
                'summary': 'Verified sites in Google Search Console',
                'when_to_use': 'Questions about which websites are tracked in Search Console',
                'trigger_phrases': ['search console site', 'verified site', 'tracked website'],
                'freshness': 'live',
                'example_questions': ['What sites are in Google Search Console?'],
                'search_strategy': 'List all verified sites',
            },
        ),
        EntityDefinition(
            name='sitemaps',
            stream_name='sitemaps',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/sites/{siteUrl}/sitemaps',
                    action=Action.LIST,
                    description='Lists the sitemaps submitted for a site.',
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing a list of sitemaps.',
                        'properties': {
                            'sitemap': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A sitemap resource with details about a submitted sitemap.',
                                    'properties': {
                                        'path': {
                                            'type': ['null', 'string'],
                                            'description': 'The URL of the sitemap.',
                                        },
                                        'lastSubmitted': {
                                            'type': ['null', 'string'],
                                            'description': 'Date and time when this sitemap was last submitted (RFC 3339 format).',
                                        },
                                        'isPending': {
                                            'type': ['null', 'boolean'],
                                            'description': 'If true, the sitemap has not been processed yet.',
                                        },
                                        'isSitemapsIndex': {
                                            'type': ['null', 'boolean'],
                                            'description': 'If true, the sitemap is a collection of sitemaps.',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'The type of the sitemap. Values: atomFeed, notSitemap, patternSitemap, rssFeed, sitemap, urlList.\n',
                                        },
                                        'lastDownloaded': {
                                            'type': ['null', 'string'],
                                            'description': 'Date and time when this sitemap was last downloaded (RFC 3339 format).',
                                        },
                                        'warnings': {
                                            'type': ['null', 'string'],
                                            'description': 'Number of warnings for the sitemap.',
                                        },
                                        'errors': {
                                            'type': ['null', 'string'],
                                            'description': 'Number of errors in the sitemap.',
                                        },
                                        'contents': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'Information about a specific content type in a sitemap.',
                                                'properties': {
                                                    'type': {
                                                        'type': ['null', 'string'],
                                                        'description': 'The specific type of content in this sitemap. Values: androidApp, image, iosApp, mobile, news, pattern, video, web.\n',
                                                    },
                                                    'submitted': {
                                                        'type': ['null', 'string'],
                                                        'description': 'The number of URLs in the sitemap of this content type.',
                                                    },
                                                    'indexed': {
                                                        'type': ['null', 'string'],
                                                        'description': 'Deprecated; do not use.',
                                                    },
                                                },
                                            },
                                            'description': 'The various content types in the sitemap.',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'sitemaps',
                                    'x-airbyte-stream-name': 'sitemaps',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sitemaps submitted to Google Search Console',
                                        'when_to_use': 'Questions about sitemap status or submitted URLs',
                                        'trigger_phrases': ['sitemap', 'submitted sitemap', 'sitemap status'],
                                        'freshness': 'live',
                                        'example_questions': ['What sitemaps are submitted?', 'Show sitemap status'],
                                        'search_strategy': 'Filter by site',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.sitemap',
                    no_pagination='Google Search Console GET /sites/{siteUrl}/sitemaps returns all submitted sitemaps for the site in a single response; no pagination cursor, offset, or page token is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sites/{siteUrl}/sitemaps/{feedpath}',
                    action=Action.GET,
                    description='Retrieves information about a specific sitemap.',
                    path_params=['siteUrl', 'feedpath'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                        'feedpath': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A sitemap resource with details about a submitted sitemap.',
                        'properties': {
                            'path': {
                                'type': ['null', 'string'],
                                'description': 'The URL of the sitemap.',
                            },
                            'lastSubmitted': {
                                'type': ['null', 'string'],
                                'description': 'Date and time when this sitemap was last submitted (RFC 3339 format).',
                            },
                            'isPending': {
                                'type': ['null', 'boolean'],
                                'description': 'If true, the sitemap has not been processed yet.',
                            },
                            'isSitemapsIndex': {
                                'type': ['null', 'boolean'],
                                'description': 'If true, the sitemap is a collection of sitemaps.',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'The type of the sitemap. Values: atomFeed, notSitemap, patternSitemap, rssFeed, sitemap, urlList.\n',
                            },
                            'lastDownloaded': {
                                'type': ['null', 'string'],
                                'description': 'Date and time when this sitemap was last downloaded (RFC 3339 format).',
                            },
                            'warnings': {
                                'type': ['null', 'string'],
                                'description': 'Number of warnings for the sitemap.',
                            },
                            'errors': {
                                'type': ['null', 'string'],
                                'description': 'Number of errors in the sitemap.',
                            },
                            'contents': {
                                'type': ['null', 'array'],
                                'items': {
                                    'type': 'object',
                                    'description': 'Information about a specific content type in a sitemap.',
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'The specific type of content in this sitemap. Values: androidApp, image, iosApp, mobile, news, pattern, video, web.\n',
                                        },
                                        'submitted': {
                                            'type': ['null', 'string'],
                                            'description': 'The number of URLs in the sitemap of this content type.',
                                        },
                                        'indexed': {
                                            'type': ['null', 'string'],
                                            'description': 'Deprecated; do not use.',
                                        },
                                    },
                                },
                                'description': 'The various content types in the sitemap.',
                            },
                        },
                        'x-airbyte-entity-name': 'sitemaps',
                        'x-airbyte-stream-name': 'sitemaps',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sitemaps submitted to Google Search Console',
                            'when_to_use': 'Questions about sitemap status or submitted URLs',
                            'trigger_phrases': ['sitemap', 'submitted sitemap', 'sitemap status'],
                            'freshness': 'live',
                            'example_questions': ['What sitemaps are submitted?', 'Show sitemap status'],
                            'search_strategy': 'Filter by site',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A sitemap resource with details about a submitted sitemap.',
                'properties': {
                    'path': {
                        'type': ['null', 'string'],
                        'description': 'The URL of the sitemap.',
                    },
                    'lastSubmitted': {
                        'type': ['null', 'string'],
                        'description': 'Date and time when this sitemap was last submitted (RFC 3339 format).',
                    },
                    'isPending': {
                        'type': ['null', 'boolean'],
                        'description': 'If true, the sitemap has not been processed yet.',
                    },
                    'isSitemapsIndex': {
                        'type': ['null', 'boolean'],
                        'description': 'If true, the sitemap is a collection of sitemaps.',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'The type of the sitemap. Values: atomFeed, notSitemap, patternSitemap, rssFeed, sitemap, urlList.\n',
                    },
                    'lastDownloaded': {
                        'type': ['null', 'string'],
                        'description': 'Date and time when this sitemap was last downloaded (RFC 3339 format).',
                    },
                    'warnings': {
                        'type': ['null', 'string'],
                        'description': 'Number of warnings for the sitemap.',
                    },
                    'errors': {
                        'type': ['null', 'string'],
                        'description': 'Number of errors in the sitemap.',
                    },
                    'contents': {
                        'type': ['null', 'array'],
                        'items': {'$ref': '#/components/schemas/SitemapContent'},
                        'description': 'The various content types in the sitemap.',
                    },
                },
                'x-airbyte-entity-name': 'sitemaps',
                'x-airbyte-stream-name': 'sitemaps',
                'x-airbyte-ai-hints': {
                    'summary': 'Sitemaps submitted to Google Search Console',
                    'when_to_use': 'Questions about sitemap status or submitted URLs',
                    'trigger_phrases': ['sitemap', 'submitted sitemap', 'sitemap status'],
                    'freshness': 'live',
                    'example_questions': ['What sitemaps are submitted?', 'Show sitemap status'],
                    'search_strategy': 'Filter by site',
                },
            },
            ai_hints={
                'summary': 'Sitemaps submitted to Google Search Console',
                'when_to_use': 'Questions about sitemap status or submitted URLs',
                'trigger_phrases': ['sitemap', 'submitted sitemap', 'sitemap status'],
                'freshness': 'live',
                'example_questions': ['What sitemaps are submitted?', 'Show sitemap status'],
                'search_strategy': 'Filter by site',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='sitemaps',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='search_analytics_by_date',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sites/{siteUrl}/searchAnalytics/query:search_analytics_by_date',
                    path_override=PathOverrideConfig(
                        path='/sites/{siteUrl}/searchAnalytics/query',
                    ),
                    action=Action.LIST,
                    description='Query search analytics data grouped by date. Returns clicks, impressions, CTR, and average position for each date in the specified range.\n',
                    body_fields=[
                        'startDate',
                        'endDate',
                        'dimensions',
                        'rowLimit',
                        'startRow',
                        'type',
                        'aggregationType',
                        'dataState',
                    ],
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dimensions': ['date'],
                        'rowLimit': 1000,
                        'startRow': 0,
                        'type': 'web',
                        'aggregationType': 'auto',
                        'dataState': 'final',
                    },
                    request_body_probe_defaults={'startDate': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}", 'endDate': "{{ now_utc().strftime('%Y-%m-%d') }}"},
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date.',
                        'properties': {
                            'startDate': {
                                'type': 'string',
                                'description': 'Start date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}",
                            },
                            'endDate': {
                                'type': 'string',
                                'description': 'End date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ now_utc().strftime('%Y-%m-%d') }}",
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'default': ['date'],
                                'description': 'Dimensions to group results by.',
                            },
                            'rowLimit': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 25000,
                                'default': 1000,
                                'description': 'The maximum number of rows to return.',
                            },
                            'startRow': {
                                'type': 'integer',
                                'minimum': 0,
                                'default': 0,
                                'description': 'Zero-based index of the first row in the response.',
                            },
                            'type': {
                                'type': 'string',
                                'default': 'web',
                                'description': 'Filter results by type: web, discover, googleNews, news, image, video.\n',
                            },
                            'aggregationType': {
                                'type': 'string',
                                'default': 'auto',
                                'description': 'How data is aggregated: auto, byPage, byProperty, byNewsShowcasePanel.\n',
                            },
                            'dataState': {
                                'type': 'string',
                                'default': 'final',
                                'description': 'Data freshness: final (stable data only) or all (includes fresh data).\n',
                            },
                        },
                        'required': ['startDate', 'endDate'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing search analytics data.',
                        'properties': {
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A row of search analytics data.',
                                    'properties': {
                                        'keys': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'A list of dimension values for this row, in the order specified in the dimensions field of the request.\n',
                                        },
                                        'clicks': {
                                            'type': ['null', 'number'],
                                            'description': 'Click count for the row.',
                                        },
                                        'impressions': {
                                            'type': ['null', 'number'],
                                            'description': 'Impression count for the row.',
                                        },
                                        'ctr': {
                                            'type': ['null', 'number'],
                                            'description': 'Click Through Rate (CTR) for the row. Values range from 0 to 1.0.',
                                        },
                                        'position': {
                                            'type': ['null', 'number'],
                                            'description': 'Average position in search results.',
                                        },
                                    },
                                },
                                'description': 'List of rows grouped by the key values.',
                            },
                            'responseAggregationType': {
                                'type': ['null', 'string'],
                                'description': 'How the results were aggregated (auto, byPage, byProperty).',
                            },
                        },
                    },
                    record_extractor='$.rows',
                    meta_extractor={'response_aggregation_type': '$.responseAggregationType'},
                    no_pagination='Google Search Console searchAnalytics/query uses request-body offset pagination (startRow + rowLimit); the response exposes no next-page cursor, offset, or has-more flag, so continuation is driven entirely by the caller.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='search_analytics_by_date',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='search_analytics_by_country',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sites/{siteUrl}/searchAnalytics/query:search_analytics_by_country',
                    path_override=PathOverrideConfig(
                        path='/sites/{siteUrl}/searchAnalytics/query',
                    ),
                    action=Action.LIST,
                    description='Query search analytics data grouped by date and country. Returns clicks, impressions, CTR, and average position for each country.\n',
                    body_fields=[
                        'startDate',
                        'endDate',
                        'dimensions',
                        'rowLimit',
                        'startRow',
                        'type',
                        'aggregationType',
                        'dataState',
                    ],
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dimensions': ['date', 'country'],
                        'rowLimit': 1000,
                        'startRow': 0,
                        'type': 'web',
                        'aggregationType': 'auto',
                        'dataState': 'final',
                    },
                    request_body_probe_defaults={'startDate': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}", 'endDate': "{{ now_utc().strftime('%Y-%m-%d') }}"},
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and country.',
                        'properties': {
                            'startDate': {
                                'type': 'string',
                                'description': 'Start date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}",
                            },
                            'endDate': {
                                'type': 'string',
                                'description': 'End date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ now_utc().strftime('%Y-%m-%d') }}",
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'default': ['date', 'country'],
                                'description': 'Dimensions to group results by.',
                            },
                            'rowLimit': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 25000,
                                'default': 1000,
                                'description': 'The maximum number of rows to return.',
                            },
                            'startRow': {
                                'type': 'integer',
                                'minimum': 0,
                                'default': 0,
                                'description': 'Zero-based index of the first row in the response.',
                            },
                            'type': {
                                'type': 'string',
                                'default': 'web',
                                'description': 'Filter results by type: web, discover, googleNews, news, image, video.\n',
                            },
                            'aggregationType': {
                                'type': 'string',
                                'default': 'auto',
                                'description': 'How data is aggregated: auto, byPage, byProperty.\n',
                            },
                            'dataState': {
                                'type': 'string',
                                'default': 'final',
                                'description': 'Data freshness: final (stable data only) or all (includes fresh data).\n',
                            },
                        },
                        'required': ['startDate', 'endDate'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing search analytics data.',
                        'properties': {
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A row of search analytics data.',
                                    'properties': {
                                        'keys': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'A list of dimension values for this row, in the order specified in the dimensions field of the request.\n',
                                        },
                                        'clicks': {
                                            'type': ['null', 'number'],
                                            'description': 'Click count for the row.',
                                        },
                                        'impressions': {
                                            'type': ['null', 'number'],
                                            'description': 'Impression count for the row.',
                                        },
                                        'ctr': {
                                            'type': ['null', 'number'],
                                            'description': 'Click Through Rate (CTR) for the row. Values range from 0 to 1.0.',
                                        },
                                        'position': {
                                            'type': ['null', 'number'],
                                            'description': 'Average position in search results.',
                                        },
                                    },
                                },
                                'description': 'List of rows grouped by the key values.',
                            },
                            'responseAggregationType': {
                                'type': ['null', 'string'],
                                'description': 'How the results were aggregated (auto, byPage, byProperty).',
                            },
                        },
                    },
                    record_extractor='$.rows',
                    meta_extractor={'response_aggregation_type': '$.responseAggregationType'},
                    no_pagination='Google Search Console searchAnalytics/query uses request-body offset pagination (startRow + rowLimit); the response exposes no next-page cursor, offset, or has-more flag, so continuation is driven entirely by the caller.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='search_analytics_by_country',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='search_analytics_by_device',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sites/{siteUrl}/searchAnalytics/query:search_analytics_by_device',
                    path_override=PathOverrideConfig(
                        path='/sites/{siteUrl}/searchAnalytics/query',
                    ),
                    action=Action.LIST,
                    description='Query search analytics data grouped by date and device. Returns clicks, impressions, CTR, and average position for each device type.\n',
                    body_fields=[
                        'startDate',
                        'endDate',
                        'dimensions',
                        'rowLimit',
                        'startRow',
                        'type',
                        'aggregationType',
                        'dataState',
                    ],
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dimensions': ['date', 'device'],
                        'rowLimit': 1000,
                        'startRow': 0,
                        'type': 'web',
                        'aggregationType': 'auto',
                        'dataState': 'final',
                    },
                    request_body_probe_defaults={'startDate': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}", 'endDate': "{{ now_utc().strftime('%Y-%m-%d') }}"},
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and device.',
                        'properties': {
                            'startDate': {
                                'type': 'string',
                                'description': 'Start date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}",
                            },
                            'endDate': {
                                'type': 'string',
                                'description': 'End date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ now_utc().strftime('%Y-%m-%d') }}",
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'default': ['date', 'device'],
                                'description': 'Dimensions to group results by.',
                            },
                            'rowLimit': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 25000,
                                'default': 1000,
                                'description': 'The maximum number of rows to return.',
                            },
                            'startRow': {
                                'type': 'integer',
                                'minimum': 0,
                                'default': 0,
                                'description': 'Zero-based index of the first row in the response.',
                            },
                            'type': {
                                'type': 'string',
                                'default': 'web',
                                'description': 'Filter results by type: web, discover, googleNews, news, image, video.\n',
                            },
                            'aggregationType': {
                                'type': 'string',
                                'default': 'auto',
                                'description': 'How data is aggregated: auto, byPage, byProperty.\n',
                            },
                            'dataState': {
                                'type': 'string',
                                'default': 'final',
                                'description': 'Data freshness: final (stable data only) or all (includes fresh data).\n',
                            },
                        },
                        'required': ['startDate', 'endDate'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing search analytics data.',
                        'properties': {
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A row of search analytics data.',
                                    'properties': {
                                        'keys': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'A list of dimension values for this row, in the order specified in the dimensions field of the request.\n',
                                        },
                                        'clicks': {
                                            'type': ['null', 'number'],
                                            'description': 'Click count for the row.',
                                        },
                                        'impressions': {
                                            'type': ['null', 'number'],
                                            'description': 'Impression count for the row.',
                                        },
                                        'ctr': {
                                            'type': ['null', 'number'],
                                            'description': 'Click Through Rate (CTR) for the row. Values range from 0 to 1.0.',
                                        },
                                        'position': {
                                            'type': ['null', 'number'],
                                            'description': 'Average position in search results.',
                                        },
                                    },
                                },
                                'description': 'List of rows grouped by the key values.',
                            },
                            'responseAggregationType': {
                                'type': ['null', 'string'],
                                'description': 'How the results were aggregated (auto, byPage, byProperty).',
                            },
                        },
                    },
                    record_extractor='$.rows',
                    meta_extractor={'response_aggregation_type': '$.responseAggregationType'},
                    no_pagination='Google Search Console searchAnalytics/query uses request-body offset pagination (startRow + rowLimit); the response exposes no next-page cursor, offset, or has-more flag, so continuation is driven entirely by the caller.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='search_analytics_by_device',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='search_analytics_by_page',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sites/{siteUrl}/searchAnalytics/query:search_analytics_by_page',
                    path_override=PathOverrideConfig(
                        path='/sites/{siteUrl}/searchAnalytics/query',
                    ),
                    action=Action.LIST,
                    description='Query search analytics data grouped by date and page. Returns clicks, impressions, CTR, and average position for each page URL.\n',
                    body_fields=[
                        'startDate',
                        'endDate',
                        'dimensions',
                        'rowLimit',
                        'startRow',
                        'type',
                        'aggregationType',
                        'dataState',
                    ],
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dimensions': ['date', 'page'],
                        'rowLimit': 1000,
                        'startRow': 0,
                        'type': 'web',
                        'aggregationType': 'auto',
                        'dataState': 'final',
                    },
                    request_body_probe_defaults={'startDate': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}", 'endDate': "{{ now_utc().strftime('%Y-%m-%d') }}"},
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and page.',
                        'properties': {
                            'startDate': {
                                'type': 'string',
                                'description': 'Start date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}",
                            },
                            'endDate': {
                                'type': 'string',
                                'description': 'End date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ now_utc().strftime('%Y-%m-%d') }}",
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'default': ['date', 'page'],
                                'description': 'Dimensions to group results by.',
                            },
                            'rowLimit': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 25000,
                                'default': 1000,
                                'description': 'The maximum number of rows to return.',
                            },
                            'startRow': {
                                'type': 'integer',
                                'minimum': 0,
                                'default': 0,
                                'description': 'Zero-based index of the first row in the response.',
                            },
                            'type': {
                                'type': 'string',
                                'default': 'web',
                                'description': 'Filter results by type: web, discover, googleNews, news, image, video.\n',
                            },
                            'aggregationType': {
                                'type': 'string',
                                'default': 'auto',
                                'description': 'How data is aggregated: auto, byPage, byProperty.\n',
                            },
                            'dataState': {
                                'type': 'string',
                                'default': 'final',
                                'description': 'Data freshness: final (stable data only) or all (includes fresh data).\n',
                            },
                        },
                        'required': ['startDate', 'endDate'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing search analytics data.',
                        'properties': {
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A row of search analytics data.',
                                    'properties': {
                                        'keys': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'A list of dimension values for this row, in the order specified in the dimensions field of the request.\n',
                                        },
                                        'clicks': {
                                            'type': ['null', 'number'],
                                            'description': 'Click count for the row.',
                                        },
                                        'impressions': {
                                            'type': ['null', 'number'],
                                            'description': 'Impression count for the row.',
                                        },
                                        'ctr': {
                                            'type': ['null', 'number'],
                                            'description': 'Click Through Rate (CTR) for the row. Values range from 0 to 1.0.',
                                        },
                                        'position': {
                                            'type': ['null', 'number'],
                                            'description': 'Average position in search results.',
                                        },
                                    },
                                },
                                'description': 'List of rows grouped by the key values.',
                            },
                            'responseAggregationType': {
                                'type': ['null', 'string'],
                                'description': 'How the results were aggregated (auto, byPage, byProperty).',
                            },
                        },
                    },
                    record_extractor='$.rows',
                    meta_extractor={'response_aggregation_type': '$.responseAggregationType'},
                    no_pagination='Google Search Console searchAnalytics/query uses request-body offset pagination (startRow + rowLimit); the response exposes no next-page cursor, offset, or has-more flag, so continuation is driven entirely by the caller.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='search_analytics_by_page',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='search_analytics_by_query',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sites/{siteUrl}/searchAnalytics/query:search_analytics_by_query',
                    path_override=PathOverrideConfig(
                        path='/sites/{siteUrl}/searchAnalytics/query',
                    ),
                    action=Action.LIST,
                    description='Query search analytics data grouped by date and query. Returns clicks, impressions, CTR, and average position for each search query.\n',
                    body_fields=[
                        'startDate',
                        'endDate',
                        'dimensions',
                        'rowLimit',
                        'startRow',
                        'type',
                        'aggregationType',
                        'dataState',
                    ],
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dimensions': ['date', 'query'],
                        'rowLimit': 1000,
                        'startRow': 0,
                        'type': 'web',
                        'aggregationType': 'auto',
                        'dataState': 'final',
                    },
                    request_body_probe_defaults={'startDate': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}", 'endDate': "{{ now_utc().strftime('%Y-%m-%d') }}"},
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and query.',
                        'properties': {
                            'startDate': {
                                'type': 'string',
                                'description': 'Start date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}",
                            },
                            'endDate': {
                                'type': 'string',
                                'description': 'End date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ now_utc().strftime('%Y-%m-%d') }}",
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'default': ['date', 'query'],
                                'description': 'Dimensions to group results by.',
                            },
                            'rowLimit': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 25000,
                                'default': 1000,
                                'description': 'The maximum number of rows to return.',
                            },
                            'startRow': {
                                'type': 'integer',
                                'minimum': 0,
                                'default': 0,
                                'description': 'Zero-based index of the first row in the response.',
                            },
                            'type': {
                                'type': 'string',
                                'default': 'web',
                                'description': 'Filter results by type: web, discover, googleNews, news, image, video.\n',
                            },
                            'aggregationType': {
                                'type': 'string',
                                'default': 'auto',
                                'description': 'How data is aggregated: auto, byPage, byProperty.\n',
                            },
                            'dataState': {
                                'type': 'string',
                                'default': 'final',
                                'description': 'Data freshness: final (stable data only) or all (includes fresh data).\n',
                            },
                        },
                        'required': ['startDate', 'endDate'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing search analytics data.',
                        'properties': {
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A row of search analytics data.',
                                    'properties': {
                                        'keys': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'A list of dimension values for this row, in the order specified in the dimensions field of the request.\n',
                                        },
                                        'clicks': {
                                            'type': ['null', 'number'],
                                            'description': 'Click count for the row.',
                                        },
                                        'impressions': {
                                            'type': ['null', 'number'],
                                            'description': 'Impression count for the row.',
                                        },
                                        'ctr': {
                                            'type': ['null', 'number'],
                                            'description': 'Click Through Rate (CTR) for the row. Values range from 0 to 1.0.',
                                        },
                                        'position': {
                                            'type': ['null', 'number'],
                                            'description': 'Average position in search results.',
                                        },
                                    },
                                },
                                'description': 'List of rows grouped by the key values.',
                            },
                            'responseAggregationType': {
                                'type': ['null', 'string'],
                                'description': 'How the results were aggregated (auto, byPage, byProperty).',
                            },
                        },
                    },
                    record_extractor='$.rows',
                    meta_extractor={'response_aggregation_type': '$.responseAggregationType'},
                    no_pagination='Google Search Console searchAnalytics/query uses request-body offset pagination (startRow + rowLimit); the response exposes no next-page cursor, offset, or has-more flag, so continuation is driven entirely by the caller.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='search_analytics_by_query',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='search_analytics_all_fields',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/sites/{siteUrl}/searchAnalytics/query:search_analytics_all_fields',
                    path_override=PathOverrideConfig(
                        path='/sites/{siteUrl}/searchAnalytics/query',
                    ),
                    action=Action.LIST,
                    description='Query search analytics data grouped by all dimensions (date, country, device, page, query). Returns the most granular breakdown of search data.\n',
                    body_fields=[
                        'startDate',
                        'endDate',
                        'dimensions',
                        'rowLimit',
                        'startRow',
                        'type',
                        'aggregationType',
                        'dataState',
                    ],
                    path_params=['siteUrl'],
                    path_params_schema={
                        'siteUrl': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dimensions': [
                            'date',
                            'country',
                            'device',
                            'page',
                            'query',
                        ],
                        'rowLimit': 1000,
                        'startRow': 0,
                        'type': 'web',
                        'aggregationType': 'auto',
                        'dataState': 'final',
                    },
                    request_body_probe_defaults={'startDate': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}", 'endDate': "{{ now_utc().strftime('%Y-%m-%d') }}"},
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by all dimensions.',
                        'properties': {
                            'startDate': {
                                'type': 'string',
                                'description': 'Start date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ (now_utc() - duration('P7D')).strftime('%Y-%m-%d') }}",
                            },
                            'endDate': {
                                'type': 'string',
                                'description': 'End date of the requested date range, in YYYY-MM-DD format.',
                                'x-airbyte-probe-default': "{{ now_utc().strftime('%Y-%m-%d') }}",
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'default': [
                                    'date',
                                    'country',
                                    'device',
                                    'page',
                                    'query',
                                ],
                                'description': 'Dimensions to group results by.',
                            },
                            'rowLimit': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 25000,
                                'default': 1000,
                                'description': 'The maximum number of rows to return.',
                            },
                            'startRow': {
                                'type': 'integer',
                                'minimum': 0,
                                'default': 0,
                                'description': 'Zero-based index of the first row in the response.',
                            },
                            'type': {
                                'type': 'string',
                                'default': 'web',
                                'description': 'Filter results by type: web, discover, googleNews, news, image, video.\n',
                            },
                            'aggregationType': {
                                'type': 'string',
                                'default': 'auto',
                                'description': 'How data is aggregated: auto, byPage, byProperty.\n',
                            },
                            'dataState': {
                                'type': 'string',
                                'default': 'final',
                                'description': 'Data freshness: final (stable data only) or all (includes fresh data).\n',
                            },
                        },
                        'required': ['startDate', 'endDate'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing search analytics data.',
                        'properties': {
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A row of search analytics data.',
                                    'properties': {
                                        'keys': {
                                            'type': ['null', 'array'],
                                            'items': {'type': 'string'},
                                            'description': 'A list of dimension values for this row, in the order specified in the dimensions field of the request.\n',
                                        },
                                        'clicks': {
                                            'type': ['null', 'number'],
                                            'description': 'Click count for the row.',
                                        },
                                        'impressions': {
                                            'type': ['null', 'number'],
                                            'description': 'Impression count for the row.',
                                        },
                                        'ctr': {
                                            'type': ['null', 'number'],
                                            'description': 'Click Through Rate (CTR) for the row. Values range from 0 to 1.0.',
                                        },
                                        'position': {
                                            'type': ['null', 'number'],
                                            'description': 'Average position in search results.',
                                        },
                                    },
                                },
                                'description': 'List of rows grouped by the key values.',
                            },
                            'responseAggregationType': {
                                'type': ['null', 'string'],
                                'description': 'How the results were aggregated (auto, byPage, byProperty).',
                            },
                        },
                    },
                    record_extractor='$.rows',
                    meta_extractor={'response_aggregation_type': '$.responseAggregationType'},
                    no_pagination='Google Search Console searchAnalytics/query uses request-body offset pagination (startRow + rowLimit); the response exposes no next-page cursor, offset, or has-more flag, so continuation is driven entirely by the caller.',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='search_analytics_all_fields',
                    target_entity='sites',
                    foreign_key='siteUrl',
                    target_key='siteUrl',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='sites',
                suggested=True,
                x_airbyte_name='sites',
                fields=[
                    CacheFieldConfig(
                        name='permissionLevel',
                        type=['null', 'string'],
                        description="The user's permission level for the site (owner, full, restricted, etc.)",
                    ),
                    CacheFieldConfig(
                        name='siteUrl',
                        type=['null', 'string'],
                        description='The URL of the site data being fetched',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='sitemaps',
                x_airbyte_name='sitemaps',
                fields=[
                    CacheFieldConfig(
                        name='contents',
                        type=['null', 'array'],
                        description='Data related to the sitemap contents',
                    ),
                    CacheFieldConfig(
                        name='errors',
                        type=['null', 'string'],
                        description='Errors encountered while processing the sitemaps',
                    ),
                    CacheFieldConfig(
                        name='isPending',
                        type=['null', 'boolean'],
                        description='Flag indicating if the sitemap is pending for processing',
                    ),
                    CacheFieldConfig(
                        name='isSitemapsIndex',
                        type=['null', 'boolean'],
                        description='Flag indicating if the data represents a sitemap index',
                    ),
                    CacheFieldConfig(
                        name='lastDownloaded',
                        type=['null', 'string'],
                        description='Timestamp when the sitemap was last downloaded',
                    ),
                    CacheFieldConfig(
                        name='lastSubmitted',
                        type=['null', 'string'],
                        description='Timestamp when the sitemap was last submitted',
                    ),
                    CacheFieldConfig(
                        name='path',
                        type=['null', 'string'],
                        description='Path to the sitemap file',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Type of the sitemap',
                    ),
                    CacheFieldConfig(
                        name='warnings',
                        type=['null', 'string'],
                        description='Warnings encountered while processing the sitemaps',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_analytics_all_fields',
                suggested=True,
                x_airbyte_name='search_analytics_all_fields',
                fields=[
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'integer'],
                        description='The number of times users clicked on the search result for a specific query',
                    ),
                    CacheFieldConfig(
                        name='country',
                        type=['null', 'string'],
                        description='The country from which the search query originated',
                    ),
                    CacheFieldConfig(
                        name='ctr',
                        type=['null', 'number'],
                        description='Click-through rate, calculated as clicks divided by impressions',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date when the search query occurred',
                    ),
                    CacheFieldConfig(
                        name='device',
                        type=['null', 'string'],
                        description='The type of device used by the user (e.g., desktop, mobile)',
                    ),
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'integer'],
                        description='The number of times a search result appeared in response to a query',
                    ),
                    CacheFieldConfig(
                        name='page',
                        type=['null', 'string'],
                        description='The page URL that appeared in the search results',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'number'],
                        description='The average position of the search result on the search engine results page',
                    ),
                    CacheFieldConfig(
                        name='query',
                        type=['null', 'string'],
                        description='The search query entered by the user',
                    ),
                    CacheFieldConfig(
                        name='search_type',
                        type=['null', 'string'],
                        description='The type of search (e.g., web, image, video) that triggered the search result',
                    ),
                    CacheFieldConfig(
                        name='site_url',
                        type=['null', 'string'],
                        description='The URL of the site from which the data originates',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_analytics_by_country',
                suggested=True,
                x_airbyte_name='search_analytics_by_country',
                fields=[
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'integer'],
                        description='The number of times users clicked on the search result for a specific country',
                    ),
                    CacheFieldConfig(
                        name='country',
                        type=['null', 'string'],
                        description='The country for which the search analytics data is being reported',
                    ),
                    CacheFieldConfig(
                        name='ctr',
                        type=['null', 'number'],
                        description='The click-through rate for a specific country',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date for which the search analytics data is being reported',
                    ),
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'integer'],
                        description='The total number of times a search result was shown for a specific country',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'number'],
                        description="The average position at which the site's search result appeared for a specific country",
                    ),
                    CacheFieldConfig(
                        name='search_type',
                        type=['null', 'string'],
                        description='The type of search for which the data is being reported',
                    ),
                    CacheFieldConfig(
                        name='site_url',
                        type=['null', 'string'],
                        description='The URL of the site for which the search analytics data is being reported',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_analytics_by_date',
                suggested=True,
                x_airbyte_name='search_analytics_by_date',
                fields=[
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'integer'],
                        description='The total number of clicks on the specific date',
                    ),
                    CacheFieldConfig(
                        name='ctr',
                        type=['null', 'number'],
                        description='The click-through rate for the specific date',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date for which the search analytics data is being reported',
                    ),
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'integer'],
                        description='The number of impressions on the specific date',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'number'],
                        description='The average position in search results for the specific date',
                    ),
                    CacheFieldConfig(
                        name='search_type',
                        type=['null', 'string'],
                        description='The type of search query that generated the data',
                    ),
                    CacheFieldConfig(
                        name='site_url',
                        type=['null', 'string'],
                        description='The URL of the site for which the search analytics data is being reported',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_analytics_by_device',
                suggested=True,
                x_airbyte_name='search_analytics_by_device',
                fields=[
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'integer'],
                        description='The total number of clicks by device type',
                    ),
                    CacheFieldConfig(
                        name='ctr',
                        type=['null', 'number'],
                        description='Click-through rate by device type',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date for which the search analytics data is provided',
                    ),
                    CacheFieldConfig(
                        name='device',
                        type=['null', 'string'],
                        description='The type of device used by the user (e.g., desktop, mobile)',
                    ),
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'integer'],
                        description='The total number of impressions by device type',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'number'],
                        description='The average position in search results by device type',
                    ),
                    CacheFieldConfig(
                        name='search_type',
                        type=['null', 'string'],
                        description='The type of search performed',
                    ),
                    CacheFieldConfig(
                        name='site_url',
                        type=['null', 'string'],
                        description='The URL of the site for which search analytics data is being provided',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_analytics_by_page',
                suggested=True,
                x_airbyte_name='search_analytics_by_page',
                fields=[
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'integer'],
                        description='The number of clicks for a specific page',
                    ),
                    CacheFieldConfig(
                        name='ctr',
                        type=['null', 'number'],
                        description='Click-through rate for the page',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date for which the search analytics data is reported',
                    ),
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'integer'],
                        description='The number of impressions for the page',
                    ),
                    CacheFieldConfig(
                        name='page',
                        type=['null', 'string'],
                        description='The URL of the specific page being analyzed',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'number'],
                        description='The average position at which the page appeared in search results',
                    ),
                    CacheFieldConfig(
                        name='search_type',
                        type=['null', 'string'],
                        description='The type of search query that led to the page being displayed',
                    ),
                    CacheFieldConfig(
                        name='site_url',
                        type=['null', 'string'],
                        description='The URL of the site for which the search analytics data is being reported',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='search_analytics_by_query',
                suggested=True,
                x_airbyte_name='search_analytics_by_query',
                fields=[
                    CacheFieldConfig(
                        name='clicks',
                        type=['null', 'integer'],
                        description='The number of clicks for the specific query',
                    ),
                    CacheFieldConfig(
                        name='ctr',
                        type=['null', 'number'],
                        description='The click-through rate for the specific query',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date for which the search analytics data is recorded',
                    ),
                    CacheFieldConfig(
                        name='impressions',
                        type=['null', 'integer'],
                        description='The number of impressions for the specific query',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'number'],
                        description='The average position for the specific query',
                    ),
                    CacheFieldConfig(
                        name='query',
                        type=['null', 'string'],
                        description='The search query for which the data is recorded',
                    ),
                    CacheFieldConfig(
                        name='search_type',
                        type=['null', 'string'],
                        description='The type of search result for the specific query',
                    ),
                    CacheFieldConfig(
                        name='site_url',
                        type=['null', 'string'],
                        description='The URL of the site for which the search analytics data is captured',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'sites': ['permissionLevel', 'siteUrl'],
        'sitemaps': [
            'contents',
            'contents[]',
            'errors',
            'isPending',
            'isSitemapsIndex',
            'lastDownloaded',
            'lastSubmitted',
            'path',
            'type',
            'warnings',
        ],
        'search_analytics_all_fields': [
            'clicks',
            'country',
            'ctr',
            'date',
            'device',
            'impressions',
            'page',
            'position',
            'query',
            'search_type',
            'site_url',
        ],
        'search_analytics_by_country': [
            'clicks',
            'country',
            'ctr',
            'date',
            'impressions',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_by_date': [
            'clicks',
            'ctr',
            'date',
            'impressions',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_by_device': [
            'clicks',
            'ctr',
            'date',
            'device',
            'impressions',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_by_page': [
            'clicks',
            'ctr',
            'date',
            'impressions',
            'page',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_by_query': [
            'clicks',
            'ctr',
            'date',
            'impressions',
            'position',
            'query',
            'search_type',
            'site_url',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all my verified sites in Search Console',
            'Show me the sitemaps for my website',
            'Get search analytics by date for the last 7 days',
            'Show search performance broken down by country',
            'What devices are people using to find my site?',
            'Which pages get the most clicks?',
            'What queries bring the most traffic to my site?',
        ],
        context_store_search=[
            'Which country has the highest CTR for my site?',
            'What are my top 10 search queries by impressions?',
            'Compare mobile vs desktop click-through rates',
            'Which pages have the worst average position?',
            'Show me search performance trends over the last month',
        ],
        search=[
            'Which country has the highest CTR for my site?',
            'What are my top 10 search queries by impressions?',
            'Compare mobile vs desktop click-through rates',
            'Which pages have the worst average position?',
            'Show me search performance trends over the last month',
        ],
        unsupported=[
            'Submit a new sitemap',
            'Add a new site to Search Console',
            'Remove a site from Search Console',
            "Inspect a URL's index status",
            'Request indexing for a page',
        ],
    ),
)