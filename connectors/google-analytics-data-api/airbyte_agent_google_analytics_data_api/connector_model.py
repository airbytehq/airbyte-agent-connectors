"""
Connector model for google-analytics-data-api.

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

GoogleAnalyticsDataApiConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('3cc2eafd-84aa-4dca-93af-322d9dfeec1a'),
    name='google-analytics-data-api',
    version='1.0.2',
    base_url='https://analyticsdata.googleapis.com/v1beta',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://oauth2.googleapis.com/token',
        },
        user_config_spec=AirbyteAuthConfig(
            title='OAuth 2.0 Authentication',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='OAuth 2.0 Client ID from Google Cloud Console',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='OAuth 2.0 Client Secret from Google Cloud Console',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='OAuth 2.0 Refresh Token for obtaining new access tokens',
                ),
            },
            auth_mapping={
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
                'refresh_token': '${refresh_token}',
            },
            replication_auth_key_mapping={
                'credentials.client_id': 'client_id',
                'credentials.client_secret': 'client_secret',
                'credentials.refresh_token': 'refresh_token',
            },
            replication_auth_key_constants={'credentials.auth_type': 'Client'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='website_overview',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:website_overview',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns website overview metrics including total users, new users, sessions, bounce rate, page views, and average session duration by date.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                        ],
                        'metrics': [
                            {'name': 'totalUsers'},
                            {'name': 'newUsers'},
                            {'name': 'sessions'},
                            {'name': 'sessionsPerUser'},
                            {'name': 'averageSessionDuration'},
                            {'name': 'screenPageViews'},
                            {'name': 'screenPageViewsPerSession'},
                            {'name': 'bounceRate'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for website overview report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'totalUsers'},
                                    {'name': 'newUsers'},
                                    {'name': 'sessions'},
                                    {'name': 'sessionsPerUser'},
                                    {'name': 'averageSessionDuration'},
                                    {'name': 'screenPageViews'},
                                    {'name': 'screenPageViewsPerSession'},
                                    {'name': 'bounceRate'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                    preferred_for_check=True,
                ),
            },
        ),
        EntityDefinition(
            name='daily_active_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:daily_active_users',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns daily active user counts (1-day active users) by date.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                        ],
                        'metrics': [
                            {'name': 'active1DayUsers'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for daily active users report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'active1DayUsers'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
        EntityDefinition(
            name='weekly_active_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:weekly_active_users',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns weekly active user counts (7-day active users) by date.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                        ],
                        'metrics': [
                            {'name': 'active7DayUsers'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for weekly active users report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'active7DayUsers'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
        EntityDefinition(
            name='four_weekly_active_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:four_weekly_active_users',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns 28-day active user counts by date.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                        ],
                        'metrics': [
                            {'name': 'active28DayUsers'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for four-weekly active users report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'active28DayUsers'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
        EntityDefinition(
            name='traffic_sources',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:traffic_sources',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns traffic source metrics broken down by session source, session medium, and date, including users, sessions, bounce rate, and page views.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                            {'name': 'sessionSource'},
                            {'name': 'sessionMedium'},
                        ],
                        'metrics': [
                            {'name': 'totalUsers'},
                            {'name': 'newUsers'},
                            {'name': 'sessions'},
                            {'name': 'sessionsPerUser'},
                            {'name': 'averageSessionDuration'},
                            {'name': 'screenPageViews'},
                            {'name': 'screenPageViewsPerSession'},
                            {'name': 'bounceRate'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for traffic sources report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                    {'name': 'sessionSource'},
                                    {'name': 'sessionMedium'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'totalUsers'},
                                    {'name': 'newUsers'},
                                    {'name': 'sessions'},
                                    {'name': 'sessionsPerUser'},
                                    {'name': 'averageSessionDuration'},
                                    {'name': 'screenPageViews'},
                                    {'name': 'screenPageViewsPerSession'},
                                    {'name': 'bounceRate'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
        EntityDefinition(
            name='pages',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:pages',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns page-level metrics including page views and bounce rate, broken down by host name, page path, and date.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                            {'name': 'hostName'},
                            {'name': 'pagePathPlusQueryString'},
                        ],
                        'metrics': [
                            {'name': 'screenPageViews'},
                            {'name': 'bounceRate'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for pages report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                    {'name': 'hostName'},
                                    {'name': 'pagePathPlusQueryString'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'screenPageViews'},
                                    {'name': 'bounceRate'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
        EntityDefinition(
            name='devices',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:devices',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns device-related metrics broken down by device category, operating system, browser, and date, including users, sessions, and page views.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'date'},
                            {'name': 'deviceCategory'},
                            {'name': 'operatingSystem'},
                            {'name': 'browser'},
                        ],
                        'metrics': [
                            {'name': 'totalUsers'},
                            {'name': 'newUsers'},
                            {'name': 'sessions'},
                            {'name': 'sessionsPerUser'},
                            {'name': 'averageSessionDuration'},
                            {'name': 'screenPageViews'},
                            {'name': 'screenPageViewsPerSession'},
                            {'name': 'bounceRate'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for devices report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'date'},
                                    {'name': 'deviceCategory'},
                                    {'name': 'operatingSystem'},
                                    {'name': 'browser'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'totalUsers'},
                                    {'name': 'newUsers'},
                                    {'name': 'sessions'},
                                    {'name': 'sessionsPerUser'},
                                    {'name': 'averageSessionDuration'},
                                    {'name': 'screenPageViews'},
                                    {'name': 'screenPageViewsPerSession'},
                                    {'name': 'bounceRate'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
        EntityDefinition(
            name='locations',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/properties/{property_id}:runReport:locations',
                    path_override=PathOverrideConfig(
                        path='/properties/{property_id}:runReport',
                    ),
                    action=Action.LIST,
                    description='Returns geographic metrics broken down by region, country, city, and date, including users, sessions, bounce rate, and page views.',
                    body_fields=[
                        'dateRanges',
                        'dimensions',
                        'metrics',
                        'keepEmptyRows',
                        'returnPropertyQuota',
                        'limit',
                    ],
                    path_params=['property_id'],
                    path_params_schema={
                        'property_id': {'type': 'string', 'required': True},
                    },
                    request_body_defaults={
                        'dateRanges': [
                            {'startDate': '30daysAgo', 'endDate': 'today'},
                        ],
                        'dimensions': [
                            {'name': 'region'},
                            {'name': 'country'},
                            {'name': 'city'},
                            {'name': 'date'},
                        ],
                        'metrics': [
                            {'name': 'totalUsers'},
                            {'name': 'newUsers'},
                            {'name': 'sessions'},
                            {'name': 'sessionsPerUser'},
                            {'name': 'averageSessionDuration'},
                            {'name': 'screenPageViews'},
                            {'name': 'screenPageViewsPerSession'},
                            {'name': 'bounceRate'},
                        ],
                        'keepEmptyRows': False,
                        'returnPropertyQuota': True,
                        'limit': 100000,
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Request body for locations report',
                        'properties': {
                            'dateRanges': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'startDate': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)'},
                                        'endDate': {'type': 'string', 'description': 'End date in YYYY-MM-DD format or relative (e.g., today)'},
                                    },
                                },
                                'default': [
                                    {'startDate': '30daysAgo', 'endDate': 'today'},
                                ],
                            },
                            'dimensions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'region'},
                                    {'name': 'country'},
                                    {'name': 'city'},
                                    {'name': 'date'},
                                ],
                            },
                            'metrics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                    },
                                },
                                'default': [
                                    {'name': 'totalUsers'},
                                    {'name': 'newUsers'},
                                    {'name': 'sessions'},
                                    {'name': 'sessionsPerUser'},
                                    {'name': 'averageSessionDuration'},
                                    {'name': 'screenPageViews'},
                                    {'name': 'screenPageViewsPerSession'},
                                    {'name': 'bounceRate'},
                                ],
                            },
                            'keepEmptyRows': {'type': 'boolean', 'default': False},
                            'returnPropertyQuota': {'type': 'boolean', 'default': True},
                            'limit': {'type': 'integer', 'default': 100000},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the runReport endpoint',
                        'properties': {
                            'dimensionHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The dimension name'},
                                    },
                                },
                                'description': 'Column headers for dimensions',
                            },
                            'metricHeaders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'The metric name'},
                                        'type': {'type': 'string', 'description': 'The metric data type'},
                                    },
                                },
                                'description': 'Column headers for metrics',
                            },
                            'rows': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'dimensionValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The dimension value'},
                                                },
                                            },
                                            'description': 'Dimension values for this row',
                                        },
                                        'metricValues': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {'type': 'string', 'description': 'The metric value'},
                                                },
                                            },
                                            'description': 'Metric values for this row',
                                        },
                                    },
                                },
                                'description': 'Report data rows',
                            },
                            'rowCount': {'type': 'integer', 'description': 'Total number of rows in the query result'},
                            'metadata': {
                                'type': 'object',
                                'properties': {
                                    'currencyCode': {'type': 'string', 'description': 'The currency code used in this report'},
                                    'timeZone': {'type': 'string', 'description': "The property's current timezone"},
                                },
                            },
                            'propertyQuota': {
                                'type': 'object',
                                'description': 'Quota status for this Analytics property',
                                'properties': {
                                    'tokensPerDay': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'concurrentRequests': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'serverErrorsPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'potentiallyThresholdedRequestsPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                    'tokensPerProjectPerHour': {
                                        'type': 'object',
                                        'properties': {
                                            'consumed': {'type': 'integer'},
                                            'remaining': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                            'kind': {'type': 'string', 'description': 'Resource type identifier'},
                        },
                    },
                    record_extractor='$.rows',
                ),
            },
        ),
    ],
    search_field_paths={
        'website_overview': [
            'averageSessionDuration',
            'bounceRate',
            'date',
            'endDate',
            'newUsers',
            'property_id',
            'screenPageViews',
            'screenPageViewsPerSession',
            'sessions',
            'sessionsPerUser',
            'startDate',
            'totalUsers',
        ],
        'daily_active_users': [
            'active1DayUsers',
            'date',
            'endDate',
            'property_id',
            'startDate',
        ],
        'weekly_active_users': [
            'active7DayUsers',
            'date',
            'endDate',
            'property_id',
            'startDate',
        ],
        'four_weekly_active_users': [
            'active28DayUsers',
            'date',
            'endDate',
            'property_id',
            'startDate',
        ],
        'traffic_sources': [
            'averageSessionDuration',
            'bounceRate',
            'date',
            'endDate',
            'newUsers',
            'property_id',
            'screenPageViews',
            'screenPageViewsPerSession',
            'sessionMedium',
            'sessionSource',
            'sessions',
            'sessionsPerUser',
            'startDate',
            'totalUsers',
        ],
        'pages': [
            'bounceRate',
            'date',
            'endDate',
            'hostName',
            'pagePathPlusQueryString',
            'property_id',
            'screenPageViews',
            'startDate',
        ],
        'devices': [
            'averageSessionDuration',
            'bounceRate',
            'browser',
            'date',
            'deviceCategory',
            'endDate',
            'newUsers',
            'operatingSystem',
            'property_id',
            'screenPageViews',
            'screenPageViewsPerSession',
            'sessions',
            'sessionsPerUser',
            'startDate',
            'totalUsers',
        ],
        'locations': [
            'averageSessionDuration',
            'bounceRate',
            'city',
            'country',
            'date',
            'endDate',
            'newUsers',
            'property_id',
            'region',
            'screenPageViews',
            'screenPageViewsPerSession',
            'sessions',
            'sessionsPerUser',
            'startDate',
            'totalUsers',
        ],
    },
)