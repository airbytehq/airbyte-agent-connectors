"""
Connector model for google-search-console.

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

GoogleSearchConsoleConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('eb4c9e00-db83-4d63-a386-39cfa91012a8'),
    name='google-search-console',
    base_url='https://www.googleapis.com/webmasters/v3',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://oauth2.googleapis.com/token',
        },
        user_config_spec=AirbyteAuthConfig(
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
                                },
                            },
                        },
                    },
                    record_extractor='$.siteEntry',
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
            },
        ),
        EntityDefinition(
            name='sitemaps',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.sitemap',
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
            },
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
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date.',
                        'properties': {
                            'startDate': {'type': 'string', 'description': 'Start date of the requested date range, in YYYY-MM-DD format.'},
                            'endDate': {'type': 'string', 'description': 'End date of the requested date range, in YYYY-MM-DD format.'},
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
                ),
            },
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
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and country.',
                        'properties': {
                            'startDate': {'type': 'string', 'description': 'Start date of the requested date range, in YYYY-MM-DD format.'},
                            'endDate': {'type': 'string', 'description': 'End date of the requested date range, in YYYY-MM-DD format.'},
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
                ),
            },
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
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and device.',
                        'properties': {
                            'startDate': {'type': 'string', 'description': 'Start date of the requested date range, in YYYY-MM-DD format.'},
                            'endDate': {'type': 'string', 'description': 'End date of the requested date range, in YYYY-MM-DD format.'},
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
                ),
            },
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
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and page.',
                        'properties': {
                            'startDate': {'type': 'string', 'description': 'Start date of the requested date range, in YYYY-MM-DD format.'},
                            'endDate': {'type': 'string', 'description': 'End date of the requested date range, in YYYY-MM-DD format.'},
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
                ),
            },
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
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by date and query.',
                        'properties': {
                            'startDate': {'type': 'string', 'description': 'Start date of the requested date range, in YYYY-MM-DD format.'},
                            'endDate': {'type': 'string', 'description': 'End date of the requested date range, in YYYY-MM-DD format.'},
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
                ),
            },
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
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for search analytics query grouped by all dimensions.',
                        'properties': {
                            'startDate': {'type': 'string', 'description': 'Start date of the requested date range, in YYYY-MM-DD format.'},
                            'endDate': {'type': 'string', 'description': 'End date of the requested date range, in YYYY-MM-DD format.'},
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
                ),
            },
        ),
    ],
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
        'search_analytics_page_report': [
            'clicks',
            'country',
            'ctr',
            'date',
            'device',
            'impressions',
            'page',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_site_report_by_page': [
            'clicks',
            'country',
            'ctr',
            'date',
            'device',
            'impressions',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_site_report_by_site': [
            'clicks',
            'country',
            'ctr',
            'date',
            'device',
            'impressions',
            'position',
            'search_type',
            'site_url',
        ],
        'search_analytics_keyword_page_report': [
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
        'search_analytics_keyword_site_report_by_page': [
            'clicks',
            'country',
            'ctr',
            'date',
            'device',
            'impressions',
            'position',
            'query',
            'search_type',
            'site_url',
        ],
        'search_analytics_keyword_site_report_by_site': [
            'clicks',
            'country',
            'ctr',
            'date',
            'device',
            'impressions',
            'position',
            'query',
            'search_type',
            'site_url',
        ],
    },
)