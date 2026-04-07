"""
Connector model for sentry.

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
from ._vendored.connector_sdk.schema.extensions import (
    EntityRelationshipConfig,
    ScopingParamConfig,
)
from ._vendored.connector_sdk.schema.base import (
    ExampleQuestions,
)
from ._vendored.connector_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

SentryConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('cdaf146a-9b75-49fd-9dd2-9d64a0bb4781'),
    name='sentry',
    version='1.0.3',
    base_url='https://{hostname}/api/0',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='Authentication Token',
            type='object',
            required=['auth_token'],
            properties={
                'auth_token': AuthConfigFieldSpec(
                    title='Authentication Token',
                    description='Sentry authentication token. Log into Sentry and create one at Settings > Account > API > Auth Tokens.',
                ),
            },
            auth_mapping={'token': '${auth_token}'},
            replication_auth_key_mapping={'auth_token': 'auth_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='projects',
            stream_name='projects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/',
                    action=Action.LIST,
                    description='Return a list of projects available to the authenticated user.',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Sentry project (summary view from list endpoint).',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                    'description': 'Unique project identifier.',
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                    'description': 'Human-readable project name.',
                                },
                                'slug': {
                                    'type': ['string', 'null'],
                                    'description': 'URL-friendly project identifier.',
                                },
                                'status': {
                                    'type': ['string', 'null'],
                                    'description': 'Project status.',
                                },
                                'platform': {
                                    'type': ['string', 'null'],
                                    'description': 'The platform for this project.',
                                },
                                'dateCreated': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'Date the project was created.',
                                },
                                'isBookmarked': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project is bookmarked.',
                                },
                                'isMember': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the authenticated user is a member.',
                                },
                                'hasAccess': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the user has access to this project.',
                                },
                                'isPublic': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project is public.',
                                },
                                'isInternal': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project is internal.',
                                },
                                'color': {
                                    'type': ['string', 'null'],
                                    'description': 'Project color code.',
                                },
                                'features': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'List of enabled features.',
                                },
                                'firstEvent': {
                                    'type': ['string', 'null'],
                                    'description': 'Timestamp of the first event.',
                                },
                                'firstTransactionEvent': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether a transaction event has been received.',
                                },
                                'access': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'List of access permissions for the authenticated user.',
                                },
                                'hasMinifiedStackTrace': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has minified stack traces.',
                                },
                                'hasMonitors': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has cron monitors.',
                                },
                                'hasProfiles': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has profiling data.',
                                },
                                'hasReplays': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has session replays.',
                                },
                                'hasFeedbacks': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has user feedback.',
                                },
                                'hasFlags': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has feature flags.',
                                },
                                'hasNewFeedbacks': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has new user feedback.',
                                },
                                'hasSessions': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has session data.',
                                },
                                'hasInsightsHttp': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has HTTP insights.',
                                },
                                'hasInsightsDb': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has database insights.',
                                },
                                'hasInsightsAssets': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has asset insights.',
                                },
                                'hasInsightsAppStart': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has app start insights.',
                                },
                                'hasInsightsScreenLoad': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has screen load insights.',
                                },
                                'hasInsightsVitals': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has web vitals insights.',
                                },
                                'hasInsightsCaches': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has cache insights.',
                                },
                                'hasInsightsQueues': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has queue insights.',
                                },
                                'hasInsightsAgentMonitoring': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has agent monitoring insights.',
                                },
                                'hasInsightsMCP': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has MCP insights.',
                                },
                                'hasLogs': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has log data.',
                                },
                                'hasTraceMetrics': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has trace metrics.',
                                },
                                'avatar': {
                                    'type': ['object', 'null'],
                                    'description': 'Project avatar information.',
                                    'properties': {
                                        'avatarType': {
                                            'type': ['string', 'null'],
                                        },
                                        'avatarUuid': {
                                            'type': ['string', 'null'],
                                        },
                                        'avatarUrl': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'organization': {
                                    'type': ['object', 'null'],
                                    'description': 'Organization this project belongs to.',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'projects',
                            'x-airbyte-stream-name': 'projects',
                        },
                    },
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{organization_slug}/{project_slug}/',
                    action=Action.GET,
                    description='Return details on an individual project.',
                    path_params=['organization_slug', 'project_slug'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'project_slug': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Detailed project information.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'Unique project identifier.',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Human-readable project name.',
                            },
                            'slug': {
                                'type': ['string', 'null'],
                                'description': 'URL-friendly project identifier.',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Project status.',
                            },
                            'platform': {
                                'type': ['string', 'null'],
                                'description': 'The platform for this project.',
                            },
                            'dateCreated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Date the project was created.',
                            },
                            'isBookmarked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project is bookmarked.',
                            },
                            'isMember': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the authenticated user is a member.',
                            },
                            'hasAccess': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user has access.',
                            },
                            'isPublic': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project is public.',
                            },
                            'isInternal': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project is internal.',
                            },
                            'color': {
                                'type': ['string', 'null'],
                                'description': 'Project color code.',
                            },
                            'features': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'List of enabled features.',
                            },
                            'firstEvent': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp of the first event.',
                            },
                            'firstTransactionEvent': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether a transaction event has been received.',
                            },
                            'access': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'List of access permissions for the authenticated user.',
                            },
                            'hasMinifiedStackTrace': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has minified stack traces.',
                            },
                            'hasMonitors': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has cron monitors.',
                            },
                            'hasProfiles': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has profiling data.',
                            },
                            'hasReplays': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has session replays.',
                            },
                            'hasFeedbacks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has user feedback.',
                            },
                            'hasFlags': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has feature flags.',
                            },
                            'hasNewFeedbacks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has new user feedback.',
                            },
                            'hasSessions': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has session data.',
                            },
                            'hasInsightsHttp': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has HTTP insights.',
                            },
                            'hasInsightsDb': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has database insights.',
                            },
                            'hasInsightsAssets': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has asset insights.',
                            },
                            'hasInsightsAppStart': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has app start insights.',
                            },
                            'hasInsightsScreenLoad': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has screen load insights.',
                            },
                            'hasInsightsVitals': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has web vitals insights.',
                            },
                            'hasInsightsCaches': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has cache insights.',
                            },
                            'hasInsightsQueues': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has queue insights.',
                            },
                            'hasInsightsAgentMonitoring': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has agent monitoring insights.',
                            },
                            'hasInsightsMCP': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has MCP insights.',
                            },
                            'hasLogs': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has log data.',
                            },
                            'hasTraceMetrics': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has trace metrics.',
                            },
                            'team': {
                                'type': ['object', 'null'],
                                'description': 'Primary team for this project.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'teams': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['object', 'null'],
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'Teams assigned to this project.',
                            },
                            'avatar': {
                                'type': ['object', 'null'],
                                'description': 'Project avatar information.',
                                'properties': {
                                    'avatarType': {
                                        'type': ['string', 'null'],
                                    },
                                    'avatarUuid': {
                                        'type': ['string', 'null'],
                                    },
                                    'avatarUrl': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'organization': {
                                'type': ['object', 'null'],
                                'description': 'Organization this project belongs to.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'latestRelease': {
                                'type': ['object', 'null'],
                                'description': 'Latest release for this project.',
                            },
                            'options': {
                                'type': ['object', 'null'],
                                'description': 'Project configuration options.',
                            },
                            'digestsMinDelay': {
                                'type': ['integer', 'null'],
                                'description': 'Minimum digest delay in seconds.',
                            },
                            'digestsMaxDelay': {
                                'type': ['integer', 'null'],
                                'description': 'Maximum digest delay in seconds.',
                            },
                            'resolveAge': {
                                'type': ['integer', 'null'],
                                'description': 'Hours before an issue is auto-resolved.',
                            },
                            'dataScrubber': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether data scrubbing is enabled.',
                            },
                            'safeFields': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Fields that are safe from data scrubbing.',
                            },
                            'sensitiveFields': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Fields that contain sensitive data.',
                            },
                            'verifySSL': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether SSL verification is enabled.',
                            },
                            'scrubIPAddresses': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether IP address scrubbing is enabled.',
                            },
                            'scrapeJavaScript': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether JavaScript scraping is enabled.',
                            },
                            'allowedDomains': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Domains allowed to send events.',
                            },
                            'processingIssues': {
                                'type': ['integer', 'null'],
                                'description': 'Number of processing issues.',
                            },
                            'securityToken': {
                                'type': ['string', 'null'],
                                'description': 'Security token for the project.',
                            },
                            'subjectPrefix': {
                                'type': ['string', 'null'],
                                'description': 'Subject prefix for notification emails.',
                            },
                            'dataScrubberDefaults': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether default data scrubbers are enabled.',
                            },
                            'storeCrashReports': {
                                'type': ['boolean', 'integer', 'null'],
                                'description': 'Number of crash reports to store, or null/false if disabled.',
                            },
                            'subjectTemplate': {
                                'type': ['string', 'null'],
                                'description': 'Template for notification email subjects.',
                            },
                            'securityTokenHeader': {
                                'type': ['string', 'null'],
                                'description': 'Custom security token header name.',
                            },
                            'groupingConfig': {
                                'type': ['string', 'null'],
                                'description': 'Grouping configuration identifier.',
                            },
                            'groupingEnhancements': {
                                'type': ['string', 'null'],
                                'description': 'Custom grouping enhancements.',
                            },
                            'derivedGroupingEnhancements': {
                                'type': ['string', 'null'],
                                'description': 'Derived grouping enhancements.',
                            },
                            'secondaryGroupingExpiry': {
                                'type': ['integer', 'null'],
                                'description': 'Expiry timestamp for secondary grouping.',
                            },
                            'secondaryGroupingConfig': {
                                'type': ['string', 'null'],
                                'description': 'Secondary grouping configuration.',
                            },
                            'fingerprintingRules': {
                                'type': ['string', 'null'],
                                'description': 'Custom fingerprinting rules.',
                            },
                            'plugins': {
                                'type': ['array', 'null'],
                                'description': 'Installed plugins.',
                            },
                            'platforms': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Platforms detected in this project.',
                            },
                            'defaultEnvironment': {
                                'type': ['string', 'null'],
                                'description': 'Default environment for the project.',
                            },
                            'relayPiiConfig': {
                                'type': ['string', 'null'],
                                'description': 'Relay PII configuration.',
                            },
                            'builtinSymbolSources': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Built-in symbol sources.',
                            },
                            'dynamicSamplingBiases': {
                                'type': ['array', 'null'],
                                'description': 'Dynamic sampling biases configuration.',
                            },
                            'symbolSources': {
                                'type': ['string', 'null'],
                                'description': 'Custom symbol sources configuration.',
                            },
                            'isDynamicallySampled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether dynamic sampling is active.',
                            },
                            'autofixAutomationTuning': {
                                'type': ['string', 'null'],
                                'description': 'Autofix automation tuning setting.',
                            },
                            'seerScannerAutomation': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether Seer scanner automation is enabled.',
                            },
                            'highlightTags': {
                                'type': ['array', 'null'],
                                'description': 'Highlighted tags configuration.',
                            },
                            'highlightContext': {
                                'type': ['object', 'null'],
                                'description': 'Highlighted context configuration.',
                            },
                            'highlightPreset': {
                                'type': ['object', 'null'],
                                'description': 'Highlight preset configuration.',
                            },
                            'debugFilesRole': {
                                'type': ['string', 'null'],
                                'description': 'Debug files role configuration.',
                            },
                        },
                        'x-airbyte-entity-name': 'project_detail',
                        'x-airbyte-stream-name': 'project_detail',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Sentry project (summary view from list endpoint).',
                'properties': {
                    'id': {
                        'type': ['string', 'null'],
                        'description': 'Unique project identifier.',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Human-readable project name.',
                    },
                    'slug': {
                        'type': ['string', 'null'],
                        'description': 'URL-friendly project identifier.',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Project status.',
                    },
                    'platform': {
                        'type': ['string', 'null'],
                        'description': 'The platform for this project.',
                    },
                    'dateCreated': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Date the project was created.',
                    },
                    'isBookmarked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project is bookmarked.',
                    },
                    'isMember': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the authenticated user is a member.',
                    },
                    'hasAccess': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user has access to this project.',
                    },
                    'isPublic': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project is public.',
                    },
                    'isInternal': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project is internal.',
                    },
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'Project color code.',
                    },
                    'features': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'List of enabled features.',
                    },
                    'firstEvent': {
                        'type': ['string', 'null'],
                        'description': 'Timestamp of the first event.',
                    },
                    'firstTransactionEvent': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether a transaction event has been received.',
                    },
                    'access': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'List of access permissions for the authenticated user.',
                    },
                    'hasMinifiedStackTrace': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has minified stack traces.',
                    },
                    'hasMonitors': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has cron monitors.',
                    },
                    'hasProfiles': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has profiling data.',
                    },
                    'hasReplays': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has session replays.',
                    },
                    'hasFeedbacks': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has user feedback.',
                    },
                    'hasFlags': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has feature flags.',
                    },
                    'hasNewFeedbacks': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has new user feedback.',
                    },
                    'hasSessions': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has session data.',
                    },
                    'hasInsightsHttp': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has HTTP insights.',
                    },
                    'hasInsightsDb': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has database insights.',
                    },
                    'hasInsightsAssets': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has asset insights.',
                    },
                    'hasInsightsAppStart': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has app start insights.',
                    },
                    'hasInsightsScreenLoad': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has screen load insights.',
                    },
                    'hasInsightsVitals': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has web vitals insights.',
                    },
                    'hasInsightsCaches': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has cache insights.',
                    },
                    'hasInsightsQueues': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has queue insights.',
                    },
                    'hasInsightsAgentMonitoring': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has agent monitoring insights.',
                    },
                    'hasInsightsMCP': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has MCP insights.',
                    },
                    'hasLogs': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has log data.',
                    },
                    'hasTraceMetrics': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has trace metrics.',
                    },
                    'avatar': {
                        'type': ['object', 'null'],
                        'description': 'Project avatar information.',
                        'properties': {
                            'avatarType': {
                                'type': ['string', 'null'],
                            },
                            'avatarUuid': {
                                'type': ['string', 'null'],
                            },
                            'avatarUrl': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'organization': {
                        'type': ['object', 'null'],
                        'description': 'Organization this project belongs to.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'slug': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'projects',
                'x-airbyte-stream-name': 'projects',
            },
        ),
        EntityDefinition(
            name='issues',
            stream_name='issues',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{organization_slug}/{project_slug}/issues/',
                    action=Action.LIST,
                    description='Return a list of issues (groups) bound to a project. A default query of is:unresolved is applied. To return results with other statuses send a new query value (i.e. ?query= for all results).',
                    query_params=['query', 'statsPeriod', 'cursor'],
                    query_params_schema={
                        'query': {'type': 'string', 'required': False},
                        'statsPeriod': {'type': 'string', 'required': False},
                        'cursor': {'type': 'string', 'required': False},
                    },
                    path_params=['organization_slug', 'project_slug'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'project_slug': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Sentry issue (group of similar events).',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                    'description': 'Unique issue identifier.',
                                },
                                'title': {
                                    'type': ['string', 'null'],
                                    'description': 'Issue title.',
                                },
                                'shortId': {
                                    'type': ['string', 'null'],
                                    'description': 'Short human-readable identifier.',
                                },
                                'culprit': {
                                    'type': ['string', 'null'],
                                    'description': 'The culprit (source) of the issue.',
                                },
                                'level': {
                                    'type': ['string', 'null'],
                                    'description': 'Issue severity level.',
                                },
                                'status': {
                                    'type': ['string', 'null'],
                                    'description': 'Issue status (resolved, unresolved, ignored).',
                                },
                                'type': {
                                    'type': ['string', 'null'],
                                    'description': 'Issue type.',
                                },
                                'count': {
                                    'type': ['string', 'null'],
                                    'description': 'Number of events for this issue.',
                                },
                                'userCount': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of users affected.',
                                },
                                'firstSeen': {
                                    'type': ['string', 'null'],
                                    'description': 'When the issue was first seen.',
                                },
                                'lastSeen': {
                                    'type': ['string', 'null'],
                                    'description': 'When the issue was last seen.',
                                },
                                'hasSeen': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the authenticated user has seen the issue.',
                                },
                                'isBookmarked': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the issue is bookmarked.',
                                },
                                'isPublic': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the issue is public.',
                                },
                                'isSubscribed': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the user is subscribed to the issue.',
                                },
                                'logger': {
                                    'type': ['string', 'null'],
                                    'description': 'Logger that generated the issue.',
                                },
                                'permalink': {
                                    'type': ['string', 'null'],
                                    'description': 'Permalink to the issue in the Sentry UI.',
                                },
                                'platform': {
                                    'type': ['string', 'null'],
                                    'description': 'Platform for this issue.',
                                },
                                'shareId': {
                                    'type': ['string', 'null'],
                                    'description': 'Share ID if the issue is shared.',
                                },
                                'numComments': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of comments on the issue.',
                                },
                                'issueType': {
                                    'type': ['string', 'null'],
                                    'description': 'The type classification of the issue.',
                                },
                                'issueCategory': {
                                    'type': ['string', 'null'],
                                    'description': 'The category classification of the issue.',
                                },
                                'isUnhandled': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the issue is from an unhandled error.',
                                },
                                'substatus': {
                                    'type': ['string', 'null'],
                                    'description': 'Issue substatus.',
                                },
                                'metadata': {
                                    'type': ['object', 'null'],
                                    'description': 'Issue metadata.',
                                    'properties': {
                                        'title': {
                                            'type': ['string', 'null'],
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': ['string', 'null'],
                                        },
                                        'filename': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'project': {
                                    'type': ['object', 'null'],
                                    'description': 'Project this issue belongs to.',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'stats': {
                                    'type': ['object', 'null'],
                                    'description': 'Issue event statistics.',
                                },
                                'statusDetails': {
                                    'type': ['object', 'null'],
                                    'description': 'Status detail information.',
                                },
                                'assignedTo': {
                                    'type': ['object', 'null'],
                                    'description': 'User or team assigned to this issue.',
                                },
                                'annotations': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'Annotations on the issue.',
                                },
                                'subscriptionDetails': {
                                    'type': ['object', 'null'],
                                    'description': 'Subscription details.',
                                },
                            },
                            'x-airbyte-entity-name': 'issues',
                            'x-airbyte-stream-name': 'issues',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/organizations/{organization_slug}/issues/{issue_id}/',
                    action=Action.GET,
                    description='Return details on an individual issue. This returns the basic stats for the issue (title, last seen, first seen), some overall numbers (number of comments, user reports) as well as the summarized event data.',
                    path_params=['organization_slug', 'issue_id'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'issue_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Sentry issue (group of similar events).',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'Unique issue identifier.',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'Issue title.',
                            },
                            'shortId': {
                                'type': ['string', 'null'],
                                'description': 'Short human-readable identifier.',
                            },
                            'culprit': {
                                'type': ['string', 'null'],
                                'description': 'The culprit (source) of the issue.',
                            },
                            'level': {
                                'type': ['string', 'null'],
                                'description': 'Issue severity level.',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Issue status (resolved, unresolved, ignored).',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Issue type.',
                            },
                            'count': {
                                'type': ['string', 'null'],
                                'description': 'Number of events for this issue.',
                            },
                            'userCount': {
                                'type': ['integer', 'null'],
                                'description': 'Number of users affected.',
                            },
                            'firstSeen': {
                                'type': ['string', 'null'],
                                'description': 'When the issue was first seen.',
                            },
                            'lastSeen': {
                                'type': ['string', 'null'],
                                'description': 'When the issue was last seen.',
                            },
                            'hasSeen': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the authenticated user has seen the issue.',
                            },
                            'isBookmarked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the issue is bookmarked.',
                            },
                            'isPublic': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the issue is public.',
                            },
                            'isSubscribed': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user is subscribed to the issue.',
                            },
                            'logger': {
                                'type': ['string', 'null'],
                                'description': 'Logger that generated the issue.',
                            },
                            'permalink': {
                                'type': ['string', 'null'],
                                'description': 'Permalink to the issue in the Sentry UI.',
                            },
                            'platform': {
                                'type': ['string', 'null'],
                                'description': 'Platform for this issue.',
                            },
                            'shareId': {
                                'type': ['string', 'null'],
                                'description': 'Share ID if the issue is shared.',
                            },
                            'numComments': {
                                'type': ['integer', 'null'],
                                'description': 'Number of comments on the issue.',
                            },
                            'issueType': {
                                'type': ['string', 'null'],
                                'description': 'The type classification of the issue.',
                            },
                            'issueCategory': {
                                'type': ['string', 'null'],
                                'description': 'The category classification of the issue.',
                            },
                            'isUnhandled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the issue is from an unhandled error.',
                            },
                            'substatus': {
                                'type': ['string', 'null'],
                                'description': 'Issue substatus.',
                            },
                            'metadata': {
                                'type': ['object', 'null'],
                                'description': 'Issue metadata.',
                                'properties': {
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                    },
                                    'filename': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'project': {
                                'type': ['object', 'null'],
                                'description': 'Project this issue belongs to.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'stats': {
                                'type': ['object', 'null'],
                                'description': 'Issue event statistics.',
                            },
                            'statusDetails': {
                                'type': ['object', 'null'],
                                'description': 'Status detail information.',
                            },
                            'assignedTo': {
                                'type': ['object', 'null'],
                                'description': 'User or team assigned to this issue.',
                            },
                            'annotations': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Annotations on the issue.',
                            },
                            'subscriptionDetails': {
                                'type': ['object', 'null'],
                                'description': 'Subscription details.',
                            },
                        },
                        'x-airbyte-entity-name': 'issues',
                        'x-airbyte-stream-name': 'issues',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Sentry issue (group of similar events).',
                'properties': {
                    'id': {
                        'type': ['string', 'null'],
                        'description': 'Unique issue identifier.',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Issue title.',
                    },
                    'shortId': {
                        'type': ['string', 'null'],
                        'description': 'Short human-readable identifier.',
                    },
                    'culprit': {
                        'type': ['string', 'null'],
                        'description': 'The culprit (source) of the issue.',
                    },
                    'level': {
                        'type': ['string', 'null'],
                        'description': 'Issue severity level.',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Issue status (resolved, unresolved, ignored).',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Issue type.',
                    },
                    'count': {
                        'type': ['string', 'null'],
                        'description': 'Number of events for this issue.',
                    },
                    'userCount': {
                        'type': ['integer', 'null'],
                        'description': 'Number of users affected.',
                    },
                    'firstSeen': {
                        'type': ['string', 'null'],
                        'description': 'When the issue was first seen.',
                    },
                    'lastSeen': {
                        'type': ['string', 'null'],
                        'description': 'When the issue was last seen.',
                    },
                    'hasSeen': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the authenticated user has seen the issue.',
                    },
                    'isBookmarked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the issue is bookmarked.',
                    },
                    'isPublic': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the issue is public.',
                    },
                    'isSubscribed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is subscribed to the issue.',
                    },
                    'logger': {
                        'type': ['string', 'null'],
                        'description': 'Logger that generated the issue.',
                    },
                    'permalink': {
                        'type': ['string', 'null'],
                        'description': 'Permalink to the issue in the Sentry UI.',
                    },
                    'platform': {
                        'type': ['string', 'null'],
                        'description': 'Platform for this issue.',
                    },
                    'shareId': {
                        'type': ['string', 'null'],
                        'description': 'Share ID if the issue is shared.',
                    },
                    'numComments': {
                        'type': ['integer', 'null'],
                        'description': 'Number of comments on the issue.',
                    },
                    'issueType': {
                        'type': ['string', 'null'],
                        'description': 'The type classification of the issue.',
                    },
                    'issueCategory': {
                        'type': ['string', 'null'],
                        'description': 'The category classification of the issue.',
                    },
                    'isUnhandled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the issue is from an unhandled error.',
                    },
                    'substatus': {
                        'type': ['string', 'null'],
                        'description': 'Issue substatus.',
                    },
                    'metadata': {
                        'type': ['object', 'null'],
                        'description': 'Issue metadata.',
                        'properties': {
                            'title': {
                                'type': ['string', 'null'],
                            },
                            'type': {
                                'type': ['string', 'null'],
                            },
                            'value': {
                                'type': ['string', 'null'],
                            },
                            'filename': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'project': {
                        'type': ['object', 'null'],
                        'description': 'Project this issue belongs to.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'slug': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'stats': {
                        'type': ['object', 'null'],
                        'description': 'Issue event statistics.',
                    },
                    'statusDetails': {
                        'type': ['object', 'null'],
                        'description': 'Status detail information.',
                    },
                    'assignedTo': {
                        'type': ['object', 'null'],
                        'description': 'User or team assigned to this issue.',
                    },
                    'annotations': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Annotations on the issue.',
                    },
                    'subscriptionDetails': {
                        'type': ['object', 'null'],
                        'description': 'Subscription details.',
                    },
                },
                'x-airbyte-entity-name': 'issues',
                'x-airbyte-stream-name': 'issues',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='issues',
                    target_entity='projects',
                    foreign_key='project_slug',
                    target_key='slug',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='events',
            stream_name='events',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{organization_slug}/{project_slug}/events/',
                    action=Action.LIST,
                    description='Return a list of events bound to a project.',
                    query_params=['full', 'cursor'],
                    query_params_schema={
                        'full': {
                            'type': 'string',
                            'required': False,
                            'default': 'true',
                        },
                        'cursor': {'type': 'string', 'required': False},
                    },
                    path_params=['organization_slug', 'project_slug'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'project_slug': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Sentry event (individual error occurrence).',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                    'description': 'Unique event identifier.',
                                },
                                'eventID': {
                                    'type': ['string', 'null'],
                                    'description': 'Event ID as reported by the client.',
                                },
                                'groupID': {
                                    'type': ['string', 'null'],
                                    'description': 'ID of the issue group this event belongs to.',
                                },
                                'title': {
                                    'type': ['string', 'null'],
                                    'description': 'Event title.',
                                },
                                'message': {
                                    'type': ['string', 'null'],
                                    'description': 'Event message.',
                                },
                                'type': {
                                    'type': ['string', 'null'],
                                    'description': 'Event type.',
                                },
                                'platform': {
                                    'type': ['string', 'null'],
                                    'description': 'Platform the event was generated on.',
                                },
                                'dateCreated': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the event was created.',
                                },
                                'dateReceived': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the event was received by Sentry.',
                                },
                                'culprit': {
                                    'type': ['string', 'null'],
                                    'description': 'The culprit (source) of the event.',
                                },
                                'location': {
                                    'type': ['string', 'null'],
                                    'description': 'Location in source code.',
                                },
                                'crashFile': {
                                    'type': ['string', 'null'],
                                    'description': 'Crash file reference.',
                                },
                                'projectID': {
                                    'type': ['string', 'null'],
                                    'description': 'Project ID this event belongs to.',
                                },
                                'sdk': {
                                    'type': ['string', 'null'],
                                    'description': 'SDK information.',
                                },
                                'dist': {
                                    'type': ['string', 'null'],
                                    'description': 'Distribution information.',
                                },
                                'size': {
                                    'type': ['integer', 'null'],
                                    'description': 'Event payload size in bytes.',
                                },
                                'event.type': {
                                    'type': ['string', 'null'],
                                    'description': 'The type of the event.',
                                },
                                'tags': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'key': {
                                                'type': ['string', 'null'],
                                            },
                                            'value': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                    'description': 'Tags associated with the event.',
                                },
                                'user': {
                                    'type': ['object', 'null'],
                                    'description': 'User associated with the event.',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                        },
                                        'username': {
                                            'type': ['string', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'ip_address': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'metadata': {
                                    'type': ['object', 'null'],
                                    'description': 'Event metadata.',
                                    'properties': {
                                        'title': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'context': {
                                    'type': ['object', 'null'],
                                    'description': 'Additional context data.',
                                },
                                'contexts': {
                                    'type': ['object', 'null'],
                                    'description': 'Structured context information.',
                                },
                                'entries': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['object', 'null'],
                                    },
                                    'description': 'Event entries (exception, breadcrumbs, request, etc.).',
                                },
                                'errors': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'Processing errors.',
                                },
                                'fingerprints': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'Fingerprints used for grouping.',
                                },
                                'packages': {
                                    'type': ['object', 'null'],
                                    'description': 'Package information.',
                                },
                                'groupingConfig': {
                                    'type': ['object', 'null'],
                                    'description': 'Grouping configuration.',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'enhancements': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                '_meta': {
                                    'type': ['object', 'null'],
                                    'description': 'Meta information for data scrubbing.',
                                },
                            },
                            'x-airbyte-entity-name': 'events',
                            'x-airbyte-stream-name': 'events',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{organization_slug}/{project_slug}/events/{event_id}/',
                    action=Action.GET,
                    description='Return details on an individual event.',
                    path_params=['organization_slug', 'project_slug', 'event_id'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'project_slug': {'type': 'string', 'required': True},
                        'event_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Sentry event (individual error occurrence).',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'Unique event identifier.',
                            },
                            'eventID': {
                                'type': ['string', 'null'],
                                'description': 'Event ID as reported by the client.',
                            },
                            'groupID': {
                                'type': ['string', 'null'],
                                'description': 'ID of the issue group this event belongs to.',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'Event title.',
                            },
                            'message': {
                                'type': ['string', 'null'],
                                'description': 'Event message.',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Event type.',
                            },
                            'platform': {
                                'type': ['string', 'null'],
                                'description': 'Platform the event was generated on.',
                            },
                            'dateCreated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the event was created.',
                            },
                            'dateReceived': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the event was received by Sentry.',
                            },
                            'culprit': {
                                'type': ['string', 'null'],
                                'description': 'The culprit (source) of the event.',
                            },
                            'location': {
                                'type': ['string', 'null'],
                                'description': 'Location in source code.',
                            },
                            'crashFile': {
                                'type': ['string', 'null'],
                                'description': 'Crash file reference.',
                            },
                            'projectID': {
                                'type': ['string', 'null'],
                                'description': 'Project ID this event belongs to.',
                            },
                            'sdk': {
                                'type': ['string', 'null'],
                                'description': 'SDK information.',
                            },
                            'dist': {
                                'type': ['string', 'null'],
                                'description': 'Distribution information.',
                            },
                            'size': {
                                'type': ['integer', 'null'],
                                'description': 'Event payload size in bytes.',
                            },
                            'event.type': {
                                'type': ['string', 'null'],
                                'description': 'The type of the event.',
                            },
                            'tags': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['object', 'null'],
                                    'properties': {
                                        'key': {
                                            'type': ['string', 'null'],
                                        },
                                        'value': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'Tags associated with the event.',
                            },
                            'user': {
                                'type': ['object', 'null'],
                                'description': 'User associated with the event.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'username': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'ip_address': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'metadata': {
                                'type': ['object', 'null'],
                                'description': 'Event metadata.',
                                'properties': {
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'context': {
                                'type': ['object', 'null'],
                                'description': 'Additional context data.',
                            },
                            'contexts': {
                                'type': ['object', 'null'],
                                'description': 'Structured context information.',
                            },
                            'entries': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['object', 'null'],
                                },
                                'description': 'Event entries (exception, breadcrumbs, request, etc.).',
                            },
                            'errors': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Processing errors.',
                            },
                            'fingerprints': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Fingerprints used for grouping.',
                            },
                            'packages': {
                                'type': ['object', 'null'],
                                'description': 'Package information.',
                            },
                            'groupingConfig': {
                                'type': ['object', 'null'],
                                'description': 'Grouping configuration.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'enhancements': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            '_meta': {
                                'type': ['object', 'null'],
                                'description': 'Meta information for data scrubbing.',
                            },
                        },
                        'x-airbyte-entity-name': 'events',
                        'x-airbyte-stream-name': 'events',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Sentry event (individual error occurrence).',
                'properties': {
                    'id': {
                        'type': ['string', 'null'],
                        'description': 'Unique event identifier.',
                    },
                    'eventID': {
                        'type': ['string', 'null'],
                        'description': 'Event ID as reported by the client.',
                    },
                    'groupID': {
                        'type': ['string', 'null'],
                        'description': 'ID of the issue group this event belongs to.',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Event title.',
                    },
                    'message': {
                        'type': ['string', 'null'],
                        'description': 'Event message.',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Event type.',
                    },
                    'platform': {
                        'type': ['string', 'null'],
                        'description': 'Platform the event was generated on.',
                    },
                    'dateCreated': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the event was created.',
                    },
                    'dateReceived': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the event was received by Sentry.',
                    },
                    'culprit': {
                        'type': ['string', 'null'],
                        'description': 'The culprit (source) of the event.',
                    },
                    'location': {
                        'type': ['string', 'null'],
                        'description': 'Location in source code.',
                    },
                    'crashFile': {
                        'type': ['string', 'null'],
                        'description': 'Crash file reference.',
                    },
                    'projectID': {
                        'type': ['string', 'null'],
                        'description': 'Project ID this event belongs to.',
                    },
                    'sdk': {
                        'type': ['string', 'null'],
                        'description': 'SDK information.',
                    },
                    'dist': {
                        'type': ['string', 'null'],
                        'description': 'Distribution information.',
                    },
                    'size': {
                        'type': ['integer', 'null'],
                        'description': 'Event payload size in bytes.',
                    },
                    'event.type': {
                        'type': ['string', 'null'],
                        'description': 'The type of the event.',
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['object', 'null'],
                            'properties': {
                                'key': {
                                    'type': ['string', 'null'],
                                },
                                'value': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                        'description': 'Tags associated with the event.',
                    },
                    'user': {
                        'type': ['object', 'null'],
                        'description': 'User associated with the event.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'email': {
                                'type': ['string', 'null'],
                            },
                            'username': {
                                'type': ['string', 'null'],
                            },
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'ip_address': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'metadata': {
                        'type': ['object', 'null'],
                        'description': 'Event metadata.',
                        'properties': {
                            'title': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'context': {
                        'type': ['object', 'null'],
                        'description': 'Additional context data.',
                    },
                    'contexts': {
                        'type': ['object', 'null'],
                        'description': 'Structured context information.',
                    },
                    'entries': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['object', 'null'],
                        },
                        'description': 'Event entries (exception, breadcrumbs, request, etc.).',
                    },
                    'errors': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Processing errors.',
                    },
                    'fingerprints': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Fingerprints used for grouping.',
                    },
                    'packages': {
                        'type': ['object', 'null'],
                        'description': 'Package information.',
                    },
                    'groupingConfig': {
                        'type': ['object', 'null'],
                        'description': 'Grouping configuration.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'enhancements': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    '_meta': {
                        'type': ['object', 'null'],
                        'description': 'Meta information for data scrubbing.',
                    },
                },
                'x-airbyte-entity-name': 'events',
                'x-airbyte-stream-name': 'events',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='events',
                    target_entity='projects',
                    foreign_key='project_slug',
                    target_key='slug',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='releases',
            stream_name='releases',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/organizations/{organization_slug}/releases/',
                    action=Action.LIST,
                    description='Return a list of releases for a given organization.',
                    query_params=['query', 'cursor'],
                    query_params_schema={
                        'query': {'type': 'string', 'required': False},
                        'cursor': {'type': 'string', 'required': False},
                    },
                    path_params=['organization_slug'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Sentry release.',
                            'properties': {
                                'id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Unique release identifier.',
                                },
                                'version': {
                                    'type': ['string', 'null'],
                                    'description': 'Release version string.',
                                },
                                'shortVersion': {
                                    'type': ['string', 'null'],
                                    'description': 'Short version string.',
                                },
                                'ref': {
                                    'type': ['string', 'null'],
                                    'description': 'Git reference (commit SHA, tag, etc.).',
                                },
                                'url': {
                                    'type': ['string', 'null'],
                                    'description': 'URL associated with the release.',
                                },
                                'status': {
                                    'type': ['string', 'null'],
                                    'description': 'Release status.',
                                },
                                'dateCreated': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the release was created.',
                                },
                                'dateReleased': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the release was deployed.',
                                },
                                'owner': {
                                    'type': ['string', 'null'],
                                    'description': 'Owner of the release.',
                                },
                                'newGroups': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of new issue groups in this release.',
                                },
                                'commitCount': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of commits in this release.',
                                },
                                'deployCount': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of deploys for this release.',
                                },
                                'firstEvent': {
                                    'type': ['string', 'null'],
                                    'description': 'Timestamp of the first event in this release.',
                                },
                                'lastEvent': {
                                    'type': ['string', 'null'],
                                    'description': 'Timestamp of the last event in this release.',
                                },
                                'lastCommit': {
                                    'type': ['object', 'null'],
                                    'description': 'Last commit in this release.',
                                },
                                'lastDeploy': {
                                    'type': ['object', 'null'],
                                    'description': 'Last deploy of this release.',
                                },
                                'data': {
                                    'type': ['object', 'null'],
                                    'description': 'Additional release data.',
                                },
                                'userAgent': {
                                    'type': ['string', 'null'],
                                    'description': 'User agent that created the release.',
                                },
                                'authors': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                            },
                                            'email': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                    'description': 'Authors of commits in this release.',
                                },
                                'projects': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'id': {
                                                'type': ['integer', 'null'],
                                            },
                                            'name': {
                                                'type': ['string', 'null'],
                                            },
                                            'slug': {
                                                'type': ['string', 'null'],
                                            },
                                            'platform': {
                                                'type': ['string', 'null'],
                                            },
                                            'newGroups': {
                                                'type': ['integer', 'null'],
                                            },
                                            'hasHealthData': {
                                                'type': ['boolean', 'null'],
                                            },
                                        },
                                    },
                                    'description': 'Projects associated with this release.',
                                },
                                'versionInfo': {
                                    'type': ['object', 'null'],
                                    'description': 'Parsed version information.',
                                    'properties': {
                                        'version': {
                                            'type': ['object', 'null'],
                                            'properties': {
                                                'raw': {
                                                    'type': ['string', 'null'],
                                                },
                                                'major': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'minor': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'patch': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'pre': {
                                                    'type': ['string', 'null'],
                                                },
                                                'buildCode': {
                                                    'type': ['string', 'null'],
                                                },
                                                'components': {
                                                    'type': ['integer', 'null'],
                                                },
                                            },
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                        'package': {
                                            'type': ['string', 'null'],
                                        },
                                        'buildHash': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'currentProjectMeta': {
                                    'type': ['object', 'null'],
                                    'description': 'Metadata for the current project context.',
                                },
                            },
                            'x-airbyte-entity-name': 'releases',
                            'x-airbyte-stream-name': 'releases',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/organizations/{organization_slug}/releases/{version}/',
                    action=Action.GET,
                    description='Return a release for a given organization.',
                    path_params=['organization_slug', 'version'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'version': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Sentry release.',
                        'properties': {
                            'id': {
                                'type': ['integer', 'null'],
                                'description': 'Unique release identifier.',
                            },
                            'version': {
                                'type': ['string', 'null'],
                                'description': 'Release version string.',
                            },
                            'shortVersion': {
                                'type': ['string', 'null'],
                                'description': 'Short version string.',
                            },
                            'ref': {
                                'type': ['string', 'null'],
                                'description': 'Git reference (commit SHA, tag, etc.).',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL associated with the release.',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Release status.',
                            },
                            'dateCreated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the release was created.',
                            },
                            'dateReleased': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the release was deployed.',
                            },
                            'owner': {
                                'type': ['string', 'null'],
                                'description': 'Owner of the release.',
                            },
                            'newGroups': {
                                'type': ['integer', 'null'],
                                'description': 'Number of new issue groups in this release.',
                            },
                            'commitCount': {
                                'type': ['integer', 'null'],
                                'description': 'Number of commits in this release.',
                            },
                            'deployCount': {
                                'type': ['integer', 'null'],
                                'description': 'Number of deploys for this release.',
                            },
                            'firstEvent': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp of the first event in this release.',
                            },
                            'lastEvent': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp of the last event in this release.',
                            },
                            'lastCommit': {
                                'type': ['object', 'null'],
                                'description': 'Last commit in this release.',
                            },
                            'lastDeploy': {
                                'type': ['object', 'null'],
                                'description': 'Last deploy of this release.',
                            },
                            'data': {
                                'type': ['object', 'null'],
                                'description': 'Additional release data.',
                            },
                            'userAgent': {
                                'type': ['string', 'null'],
                                'description': 'User agent that created the release.',
                            },
                            'authors': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['object', 'null'],
                                    'properties': {
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'Authors of commits in this release.',
                            },
                            'projects': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['object', 'null'],
                                    'properties': {
                                        'id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                        },
                                        'platform': {
                                            'type': ['string', 'null'],
                                        },
                                        'newGroups': {
                                            'type': ['integer', 'null'],
                                        },
                                        'hasHealthData': {
                                            'type': ['boolean', 'null'],
                                        },
                                    },
                                },
                                'description': 'Projects associated with this release.',
                            },
                            'versionInfo': {
                                'type': ['object', 'null'],
                                'description': 'Parsed version information.',
                                'properties': {
                                    'version': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'raw': {
                                                'type': ['string', 'null'],
                                            },
                                            'major': {
                                                'type': ['integer', 'null'],
                                            },
                                            'minor': {
                                                'type': ['integer', 'null'],
                                            },
                                            'patch': {
                                                'type': ['integer', 'null'],
                                            },
                                            'pre': {
                                                'type': ['string', 'null'],
                                            },
                                            'buildCode': {
                                                'type': ['string', 'null'],
                                            },
                                            'components': {
                                                'type': ['integer', 'null'],
                                            },
                                        },
                                    },
                                    'description': {
                                        'type': ['string', 'null'],
                                    },
                                    'package': {
                                        'type': ['string', 'null'],
                                    },
                                    'buildHash': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'currentProjectMeta': {
                                'type': ['object', 'null'],
                                'description': 'Metadata for the current project context.',
                            },
                        },
                        'x-airbyte-entity-name': 'releases',
                        'x-airbyte-stream-name': 'releases',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Sentry release.',
                'properties': {
                    'id': {
                        'type': ['integer', 'null'],
                        'description': 'Unique release identifier.',
                    },
                    'version': {
                        'type': ['string', 'null'],
                        'description': 'Release version string.',
                    },
                    'shortVersion': {
                        'type': ['string', 'null'],
                        'description': 'Short version string.',
                    },
                    'ref': {
                        'type': ['string', 'null'],
                        'description': 'Git reference (commit SHA, tag, etc.).',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL associated with the release.',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Release status.',
                    },
                    'dateCreated': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the release was created.',
                    },
                    'dateReleased': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the release was deployed.',
                    },
                    'owner': {
                        'type': ['string', 'null'],
                        'description': 'Owner of the release.',
                    },
                    'newGroups': {
                        'type': ['integer', 'null'],
                        'description': 'Number of new issue groups in this release.',
                    },
                    'commitCount': {
                        'type': ['integer', 'null'],
                        'description': 'Number of commits in this release.',
                    },
                    'deployCount': {
                        'type': ['integer', 'null'],
                        'description': 'Number of deploys for this release.',
                    },
                    'firstEvent': {
                        'type': ['string', 'null'],
                        'description': 'Timestamp of the first event in this release.',
                    },
                    'lastEvent': {
                        'type': ['string', 'null'],
                        'description': 'Timestamp of the last event in this release.',
                    },
                    'lastCommit': {
                        'type': ['object', 'null'],
                        'description': 'Last commit in this release.',
                    },
                    'lastDeploy': {
                        'type': ['object', 'null'],
                        'description': 'Last deploy of this release.',
                    },
                    'data': {
                        'type': ['object', 'null'],
                        'description': 'Additional release data.',
                    },
                    'userAgent': {
                        'type': ['string', 'null'],
                        'description': 'User agent that created the release.',
                    },
                    'authors': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['object', 'null'],
                            'properties': {
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'email': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                        'description': 'Authors of commits in this release.',
                    },
                    'projects': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['object', 'null'],
                            'properties': {
                                'id': {
                                    'type': ['integer', 'null'],
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'slug': {
                                    'type': ['string', 'null'],
                                },
                                'platform': {
                                    'type': ['string', 'null'],
                                },
                                'newGroups': {
                                    'type': ['integer', 'null'],
                                },
                                'hasHealthData': {
                                    'type': ['boolean', 'null'],
                                },
                            },
                        },
                        'description': 'Projects associated with this release.',
                    },
                    'versionInfo': {
                        'type': ['object', 'null'],
                        'description': 'Parsed version information.',
                        'properties': {
                            'version': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'raw': {
                                        'type': ['string', 'null'],
                                    },
                                    'major': {
                                        'type': ['integer', 'null'],
                                    },
                                    'minor': {
                                        'type': ['integer', 'null'],
                                    },
                                    'patch': {
                                        'type': ['integer', 'null'],
                                    },
                                    'pre': {
                                        'type': ['string', 'null'],
                                    },
                                    'buildCode': {
                                        'type': ['string', 'null'],
                                    },
                                    'components': {
                                        'type': ['integer', 'null'],
                                    },
                                },
                            },
                            'description': {
                                'type': ['string', 'null'],
                            },
                            'package': {
                                'type': ['string', 'null'],
                            },
                            'buildHash': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'currentProjectMeta': {
                        'type': ['object', 'null'],
                        'description': 'Metadata for the current project context.',
                    },
                },
                'x-airbyte-entity-name': 'releases',
                'x-airbyte-stream-name': 'releases',
            },
        ),
        EntityDefinition(
            name='project_detail',
            stream_name='project_detail',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{organization_slug}/{project_slug}/detail/',
                    path_override=PathOverrideConfig(
                        path='/projects/{organization_slug}/{project_slug}/',
                    ),
                    action=Action.GET,
                    description='Return detailed information about a specific project.',
                    path_params=['organization_slug', 'project_slug'],
                    path_params_schema={
                        'organization_slug': {'type': 'string', 'required': True},
                        'project_slug': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Detailed project information.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                                'description': 'Unique project identifier.',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'Human-readable project name.',
                            },
                            'slug': {
                                'type': ['string', 'null'],
                                'description': 'URL-friendly project identifier.',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Project status.',
                            },
                            'platform': {
                                'type': ['string', 'null'],
                                'description': 'The platform for this project.',
                            },
                            'dateCreated': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Date the project was created.',
                            },
                            'isBookmarked': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project is bookmarked.',
                            },
                            'isMember': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the authenticated user is a member.',
                            },
                            'hasAccess': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user has access.',
                            },
                            'isPublic': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project is public.',
                            },
                            'isInternal': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project is internal.',
                            },
                            'color': {
                                'type': ['string', 'null'],
                                'description': 'Project color code.',
                            },
                            'features': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'List of enabled features.',
                            },
                            'firstEvent': {
                                'type': ['string', 'null'],
                                'description': 'Timestamp of the first event.',
                            },
                            'firstTransactionEvent': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether a transaction event has been received.',
                            },
                            'access': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'List of access permissions for the authenticated user.',
                            },
                            'hasMinifiedStackTrace': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has minified stack traces.',
                            },
                            'hasMonitors': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has cron monitors.',
                            },
                            'hasProfiles': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has profiling data.',
                            },
                            'hasReplays': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has session replays.',
                            },
                            'hasFeedbacks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has user feedback.',
                            },
                            'hasFlags': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has feature flags.',
                            },
                            'hasNewFeedbacks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has new user feedback.',
                            },
                            'hasSessions': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has session data.',
                            },
                            'hasInsightsHttp': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has HTTP insights.',
                            },
                            'hasInsightsDb': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has database insights.',
                            },
                            'hasInsightsAssets': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has asset insights.',
                            },
                            'hasInsightsAppStart': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has app start insights.',
                            },
                            'hasInsightsScreenLoad': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has screen load insights.',
                            },
                            'hasInsightsVitals': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has web vitals insights.',
                            },
                            'hasInsightsCaches': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has cache insights.',
                            },
                            'hasInsightsQueues': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has queue insights.',
                            },
                            'hasInsightsAgentMonitoring': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has agent monitoring insights.',
                            },
                            'hasInsightsMCP': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has MCP insights.',
                            },
                            'hasLogs': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has log data.',
                            },
                            'hasTraceMetrics': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the project has trace metrics.',
                            },
                            'team': {
                                'type': ['object', 'null'],
                                'description': 'Primary team for this project.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'teams': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['object', 'null'],
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'Teams assigned to this project.',
                            },
                            'avatar': {
                                'type': ['object', 'null'],
                                'description': 'Project avatar information.',
                                'properties': {
                                    'avatarType': {
                                        'type': ['string', 'null'],
                                    },
                                    'avatarUuid': {
                                        'type': ['string', 'null'],
                                    },
                                    'avatarUrl': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'organization': {
                                'type': ['object', 'null'],
                                'description': 'Organization this project belongs to.',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'latestRelease': {
                                'type': ['object', 'null'],
                                'description': 'Latest release for this project.',
                            },
                            'options': {
                                'type': ['object', 'null'],
                                'description': 'Project configuration options.',
                            },
                            'digestsMinDelay': {
                                'type': ['integer', 'null'],
                                'description': 'Minimum digest delay in seconds.',
                            },
                            'digestsMaxDelay': {
                                'type': ['integer', 'null'],
                                'description': 'Maximum digest delay in seconds.',
                            },
                            'resolveAge': {
                                'type': ['integer', 'null'],
                                'description': 'Hours before an issue is auto-resolved.',
                            },
                            'dataScrubber': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether data scrubbing is enabled.',
                            },
                            'safeFields': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Fields that are safe from data scrubbing.',
                            },
                            'sensitiveFields': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Fields that contain sensitive data.',
                            },
                            'verifySSL': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether SSL verification is enabled.',
                            },
                            'scrubIPAddresses': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether IP address scrubbing is enabled.',
                            },
                            'scrapeJavaScript': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether JavaScript scraping is enabled.',
                            },
                            'allowedDomains': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Domains allowed to send events.',
                            },
                            'processingIssues': {
                                'type': ['integer', 'null'],
                                'description': 'Number of processing issues.',
                            },
                            'securityToken': {
                                'type': ['string', 'null'],
                                'description': 'Security token for the project.',
                            },
                            'subjectPrefix': {
                                'type': ['string', 'null'],
                                'description': 'Subject prefix for notification emails.',
                            },
                            'dataScrubberDefaults': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether default data scrubbers are enabled.',
                            },
                            'storeCrashReports': {
                                'type': ['boolean', 'integer', 'null'],
                                'description': 'Number of crash reports to store, or null/false if disabled.',
                            },
                            'subjectTemplate': {
                                'type': ['string', 'null'],
                                'description': 'Template for notification email subjects.',
                            },
                            'securityTokenHeader': {
                                'type': ['string', 'null'],
                                'description': 'Custom security token header name.',
                            },
                            'groupingConfig': {
                                'type': ['string', 'null'],
                                'description': 'Grouping configuration identifier.',
                            },
                            'groupingEnhancements': {
                                'type': ['string', 'null'],
                                'description': 'Custom grouping enhancements.',
                            },
                            'derivedGroupingEnhancements': {
                                'type': ['string', 'null'],
                                'description': 'Derived grouping enhancements.',
                            },
                            'secondaryGroupingExpiry': {
                                'type': ['integer', 'null'],
                                'description': 'Expiry timestamp for secondary grouping.',
                            },
                            'secondaryGroupingConfig': {
                                'type': ['string', 'null'],
                                'description': 'Secondary grouping configuration.',
                            },
                            'fingerprintingRules': {
                                'type': ['string', 'null'],
                                'description': 'Custom fingerprinting rules.',
                            },
                            'plugins': {
                                'type': ['array', 'null'],
                                'description': 'Installed plugins.',
                            },
                            'platforms': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Platforms detected in this project.',
                            },
                            'defaultEnvironment': {
                                'type': ['string', 'null'],
                                'description': 'Default environment for the project.',
                            },
                            'relayPiiConfig': {
                                'type': ['string', 'null'],
                                'description': 'Relay PII configuration.',
                            },
                            'builtinSymbolSources': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': ['string', 'null'],
                                },
                                'description': 'Built-in symbol sources.',
                            },
                            'dynamicSamplingBiases': {
                                'type': ['array', 'null'],
                                'description': 'Dynamic sampling biases configuration.',
                            },
                            'symbolSources': {
                                'type': ['string', 'null'],
                                'description': 'Custom symbol sources configuration.',
                            },
                            'isDynamicallySampled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether dynamic sampling is active.',
                            },
                            'autofixAutomationTuning': {
                                'type': ['string', 'null'],
                                'description': 'Autofix automation tuning setting.',
                            },
                            'seerScannerAutomation': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether Seer scanner automation is enabled.',
                            },
                            'highlightTags': {
                                'type': ['array', 'null'],
                                'description': 'Highlighted tags configuration.',
                            },
                            'highlightContext': {
                                'type': ['object', 'null'],
                                'description': 'Highlighted context configuration.',
                            },
                            'highlightPreset': {
                                'type': ['object', 'null'],
                                'description': 'Highlight preset configuration.',
                            },
                            'debugFilesRole': {
                                'type': ['string', 'null'],
                                'description': 'Debug files role configuration.',
                            },
                        },
                        'x-airbyte-entity-name': 'project_detail',
                        'x-airbyte-stream-name': 'project_detail',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Detailed project information.',
                'properties': {
                    'id': {
                        'type': ['string', 'null'],
                        'description': 'Unique project identifier.',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Human-readable project name.',
                    },
                    'slug': {
                        'type': ['string', 'null'],
                        'description': 'URL-friendly project identifier.',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Project status.',
                    },
                    'platform': {
                        'type': ['string', 'null'],
                        'description': 'The platform for this project.',
                    },
                    'dateCreated': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Date the project was created.',
                    },
                    'isBookmarked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project is bookmarked.',
                    },
                    'isMember': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the authenticated user is a member.',
                    },
                    'hasAccess': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user has access.',
                    },
                    'isPublic': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project is public.',
                    },
                    'isInternal': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project is internal.',
                    },
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'Project color code.',
                    },
                    'features': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'List of enabled features.',
                    },
                    'firstEvent': {
                        'type': ['string', 'null'],
                        'description': 'Timestamp of the first event.',
                    },
                    'firstTransactionEvent': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether a transaction event has been received.',
                    },
                    'access': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'List of access permissions for the authenticated user.',
                    },
                    'hasMinifiedStackTrace': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has minified stack traces.',
                    },
                    'hasMonitors': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has cron monitors.',
                    },
                    'hasProfiles': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has profiling data.',
                    },
                    'hasReplays': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has session replays.',
                    },
                    'hasFeedbacks': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has user feedback.',
                    },
                    'hasFlags': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has feature flags.',
                    },
                    'hasNewFeedbacks': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has new user feedback.',
                    },
                    'hasSessions': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has session data.',
                    },
                    'hasInsightsHttp': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has HTTP insights.',
                    },
                    'hasInsightsDb': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has database insights.',
                    },
                    'hasInsightsAssets': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has asset insights.',
                    },
                    'hasInsightsAppStart': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has app start insights.',
                    },
                    'hasInsightsScreenLoad': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has screen load insights.',
                    },
                    'hasInsightsVitals': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has web vitals insights.',
                    },
                    'hasInsightsCaches': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has cache insights.',
                    },
                    'hasInsightsQueues': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has queue insights.',
                    },
                    'hasInsightsAgentMonitoring': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has agent monitoring insights.',
                    },
                    'hasInsightsMCP': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has MCP insights.',
                    },
                    'hasLogs': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has log data.',
                    },
                    'hasTraceMetrics': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has trace metrics.',
                    },
                    'team': {
                        'type': ['object', 'null'],
                        'description': 'Primary team for this project.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'slug': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'teams': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['object', 'null'],
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'slug': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                        'description': 'Teams assigned to this project.',
                    },
                    'avatar': {
                        'type': ['object', 'null'],
                        'description': 'Project avatar information.',
                        'properties': {
                            'avatarType': {
                                'type': ['string', 'null'],
                            },
                            'avatarUuid': {
                                'type': ['string', 'null'],
                            },
                            'avatarUrl': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'organization': {
                        'type': ['object', 'null'],
                        'description': 'Organization this project belongs to.',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'slug': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'latestRelease': {
                        'type': ['object', 'null'],
                        'description': 'Latest release for this project.',
                    },
                    'options': {
                        'type': ['object', 'null'],
                        'description': 'Project configuration options.',
                    },
                    'digestsMinDelay': {
                        'type': ['integer', 'null'],
                        'description': 'Minimum digest delay in seconds.',
                    },
                    'digestsMaxDelay': {
                        'type': ['integer', 'null'],
                        'description': 'Maximum digest delay in seconds.',
                    },
                    'resolveAge': {
                        'type': ['integer', 'null'],
                        'description': 'Hours before an issue is auto-resolved.',
                    },
                    'dataScrubber': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether data scrubbing is enabled.',
                    },
                    'safeFields': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Fields that are safe from data scrubbing.',
                    },
                    'sensitiveFields': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Fields that contain sensitive data.',
                    },
                    'verifySSL': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether SSL verification is enabled.',
                    },
                    'scrubIPAddresses': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether IP address scrubbing is enabled.',
                    },
                    'scrapeJavaScript': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether JavaScript scraping is enabled.',
                    },
                    'allowedDomains': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Domains allowed to send events.',
                    },
                    'processingIssues': {
                        'type': ['integer', 'null'],
                        'description': 'Number of processing issues.',
                    },
                    'securityToken': {
                        'type': ['string', 'null'],
                        'description': 'Security token for the project.',
                    },
                    'subjectPrefix': {
                        'type': ['string', 'null'],
                        'description': 'Subject prefix for notification emails.',
                    },
                    'dataScrubberDefaults': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether default data scrubbers are enabled.',
                    },
                    'storeCrashReports': {
                        'type': ['boolean', 'integer', 'null'],
                        'description': 'Number of crash reports to store, or null/false if disabled.',
                    },
                    'subjectTemplate': {
                        'type': ['string', 'null'],
                        'description': 'Template for notification email subjects.',
                    },
                    'securityTokenHeader': {
                        'type': ['string', 'null'],
                        'description': 'Custom security token header name.',
                    },
                    'groupingConfig': {
                        'type': ['string', 'null'],
                        'description': 'Grouping configuration identifier.',
                    },
                    'groupingEnhancements': {
                        'type': ['string', 'null'],
                        'description': 'Custom grouping enhancements.',
                    },
                    'derivedGroupingEnhancements': {
                        'type': ['string', 'null'],
                        'description': 'Derived grouping enhancements.',
                    },
                    'secondaryGroupingExpiry': {
                        'type': ['integer', 'null'],
                        'description': 'Expiry timestamp for secondary grouping.',
                    },
                    'secondaryGroupingConfig': {
                        'type': ['string', 'null'],
                        'description': 'Secondary grouping configuration.',
                    },
                    'fingerprintingRules': {
                        'type': ['string', 'null'],
                        'description': 'Custom fingerprinting rules.',
                    },
                    'plugins': {
                        'type': ['array', 'null'],
                        'description': 'Installed plugins.',
                    },
                    'platforms': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Platforms detected in this project.',
                    },
                    'defaultEnvironment': {
                        'type': ['string', 'null'],
                        'description': 'Default environment for the project.',
                    },
                    'relayPiiConfig': {
                        'type': ['string', 'null'],
                        'description': 'Relay PII configuration.',
                    },
                    'builtinSymbolSources': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Built-in symbol sources.',
                    },
                    'dynamicSamplingBiases': {
                        'type': ['array', 'null'],
                        'description': 'Dynamic sampling biases configuration.',
                    },
                    'symbolSources': {
                        'type': ['string', 'null'],
                        'description': 'Custom symbol sources configuration.',
                    },
                    'isDynamicallySampled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether dynamic sampling is active.',
                    },
                    'autofixAutomationTuning': {
                        'type': ['string', 'null'],
                        'description': 'Autofix automation tuning setting.',
                    },
                    'seerScannerAutomation': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether Seer scanner automation is enabled.',
                    },
                    'highlightTags': {
                        'type': ['array', 'null'],
                        'description': 'Highlighted tags configuration.',
                    },
                    'highlightContext': {
                        'type': ['object', 'null'],
                        'description': 'Highlighted context configuration.',
                    },
                    'highlightPreset': {
                        'type': ['object', 'null'],
                        'description': 'Highlight preset configuration.',
                    },
                    'debugFilesRole': {
                        'type': ['string', 'null'],
                        'description': 'Debug files role configuration.',
                    },
                },
                'x-airbyte-entity-name': 'project_detail',
                'x-airbyte-stream-name': 'project_detail',
            },
        ),
    ],
    search_field_paths={
        'events': [
            '_meta',
            'context',
            'contexts',
            'crashFile',
            'culprit',
            'dateCreated',
            'dateReceived',
            'dist',
            'entries',
            'entries[]',
            'errors',
            'errors[]',
            'event.type',
            'eventID',
            'fingerprints',
            'fingerprints[]',
            'groupID',
            'groupingConfig',
            'groupingConfig.id',
            'groupingConfig.enhancements',
            'id',
            'location',
            'message',
            'metadata',
            'metadata.title',
            'metadata.in_app_frame_mix',
            'occurrence',
            'packages',
            'platform',
            'projectID',
            'sdk',
            'size',
            'tags',
            'tags[]',
            'title',
            'type',
            'user',
            'user.id',
            'user.email',
            'user.username',
            'user.name',
            'user.ip_address',
        ],
        'issues': [
            'annotations',
            'annotations[]',
            'assignedTo',
            'count',
            'culprit',
            'firstSeen',
            'hasSeen',
            'id',
            'isBookmarked',
            'isPublic',
            'isSubscribed',
            'isUnhandled',
            'issueCategory',
            'issueType',
            'lastSeen',
            'level',
            'logger',
            'metadata',
            'numComments',
            'permalink',
            'platform',
            'project',
            'project.id',
            'project.name',
            'project.slug',
            'shareId',
            'shortId',
            'stats',
            'status',
            'statusDetails',
            'subscriptionDetails',
            'substatus',
            'title',
            'type',
            'userCount',
        ],
        'projects': [
            'access',
            'access[]',
            'avatar',
            'avatar.avatarUrl',
            'avatar.avatarType',
            'avatar.avatarUuid',
            'color',
            'dateCreated',
            'features',
            'features[]',
            'firstEvent',
            'firstTransactionEvent',
            'hasAccess',
            'hasCustomMetrics',
            'hasFeedbacks',
            'hasMinifiedStackTrace',
            'hasMonitors',
            'hasNewFeedbacks',
            'hasProfiles',
            'hasReplays',
            'hasSessions',
            'id',
            'isBookmarked',
            'isInternal',
            'isMember',
            'isPublic',
            'name',
            'organization',
            'organization.id',
            'organization.name',
            'organization.slug',
            'platform',
            'slug',
            'status',
        ],
        'releases': [
            'authors',
            'authors[]',
            'commitCount',
            'currentProjectMeta',
            'data',
            'dateCreated',
            'dateReleased',
            'deployCount',
            'firstEvent',
            'id',
            'lastCommit',
            'lastDeploy',
            'lastEvent',
            'newGroups',
            'owner',
            'projects',
            'projects[]',
            'ref',
            'shortVersion',
            'status',
            'url',
            'userAgent',
            'version',
            'versionInfo',
            'versionInfo.version',
            'versionInfo.version.pre',
            'versionInfo.version.raw',
            'versionInfo.version.major',
            'versionInfo.version.minor',
            'versionInfo.version.patch',
            'versionInfo.version.buildCode',
            'versionInfo.version.components',
            'versionInfo.description',
            'versionInfo.package',
            'versionInfo.buildHash',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all projects in my Sentry organization',
            'Show me the issues for a specific project',
            'List recent events from a project',
            'Show me all releases for my organization',
            'Get the details of a specific project',
        ],
        search=[
            'What are the most common unresolved issues?',
            'Which projects have the most events?',
            'Show me issues that were first seen this week',
            'Find releases created in the last month',
        ],
        unsupported=[
            'Create a new project in Sentry',
            'Delete an issue',
            'Update a release',
            'Resolve all issues in a project',
        ],
    ),
    scoping=[
        ScopingParamConfig(
            param='organization_slug',
            config_key='organization',
        ),
    ],
    server_variable_defaults={'hostname': 'sentry.io'},
)