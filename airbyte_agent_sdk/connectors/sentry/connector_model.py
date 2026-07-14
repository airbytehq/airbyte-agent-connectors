"""
Connector model for sentry.

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
    ScopingParamConfig,
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

SentryConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('cdaf146a-9b75-49fd-9dd2-9d64a0bb4781'),
    name='sentry',
    version='1.0.5',
    base_url='https://{hostname}/api/0',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
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
                    path='/organizations/{organization_slug}/projects/',
                    action=Action.LIST,
                    description='Return a list of projects the authenticated user has access to within the given organization. Requires the token to have the `org:read` scope. Note: unlike the deprecated `/projects/` endpoint, this only returns projects belonging to the configured organization and omits the `avatar`, `color`, `isInternal`, `isPublic`, `organization`, and `status` fields (use the project_detail action to retrieve those).',
                    query_params=['cursor'],
                    query_params_schema={
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
                                    'description': 'Organization this project belongs to. Not returned by the organization-scoped list endpoint; available via project_detail.',
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
                                'team': {
                                    'type': ['object', 'null'],
                                    'description': 'Primary team that owns this project.',
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
                                    'description': 'Teams that have access to this project.',
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
                                },
                                'environments': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'Environments configured for this project.',
                                },
                                'platforms': {
                                    'type': ['array', 'null'],
                                    'items': {
                                        'type': ['string', 'null'],
                                    },
                                    'description': 'Platforms detected for this project.',
                                },
                                'hasUserReports': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the project has user reports.',
                                },
                                'latestRelease': {
                                    'type': ['object', 'null'],
                                    'description': 'The most recent release for this project.',
                                    'properties': {
                                        'version': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'latestDeploys': {
                                    'type': ['object', 'null'],
                                    'description': 'The most recent deploys for this project, keyed by environment.',
                                },
                            },
                            'x-airbyte-entity-name': 'projects',
                            'x-airbyte-stream-name': 'projects',
                            'x-airbyte-ai-hints': {
                                'summary': 'Sentry projects tracking errors for specific applications',
                                'when_to_use': 'Questions about available projects or project configuration',
                                'trigger_phrases': ['sentry project', 'error tracking project'],
                                'freshness': 'live',
                                'example_questions': ['What projects are in Sentry?'],
                                'search_strategy': 'Search by name or slug',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Detailed Sentry project configuration and stats',
                            'when_to_use': 'Looking up detailed project settings or statistics',
                            'trigger_phrases': ['project detail', 'project settings', 'project stats'],
                            'freshness': 'live',
                            'example_questions': ['Show details for a Sentry project'],
                            'search_strategy': 'Retrieve by project slug',
                        },
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
                        'description': 'Organization this project belongs to. Not returned by the organization-scoped list endpoint; available via project_detail.',
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
                    'team': {
                        'type': ['object', 'null'],
                        'description': 'Primary team that owns this project.',
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
                        'description': 'Teams that have access to this project.',
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
                    },
                    'environments': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Environments configured for this project.',
                    },
                    'platforms': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': ['string', 'null'],
                        },
                        'description': 'Platforms detected for this project.',
                    },
                    'hasUserReports': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the project has user reports.',
                    },
                    'latestRelease': {
                        'type': ['object', 'null'],
                        'description': 'The most recent release for this project.',
                        'properties': {
                            'version': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'latestDeploys': {
                        'type': ['object', 'null'],
                        'description': 'The most recent deploys for this project, keyed by environment.',
                    },
                },
                'x-airbyte-entity-name': 'projects',
                'x-airbyte-stream-name': 'projects',
                'x-airbyte-ai-hints': {
                    'summary': 'Sentry projects tracking errors for specific applications',
                    'when_to_use': 'Questions about available projects or project configuration',
                    'trigger_phrases': ['sentry project', 'error tracking project'],
                    'freshness': 'live',
                    'example_questions': ['What projects are in Sentry?'],
                    'search_strategy': 'Search by name or slug',
                },
            },
            ai_hints={
                'summary': 'Sentry projects tracking errors for specific applications',
                'when_to_use': 'Questions about available projects or project configuration',
                'trigger_phrases': ['sentry project', 'error tracking project'],
                'freshness': 'live',
                'example_questions': ['What projects are in Sentry?'],
                'search_strategy': 'Search by name or slug',
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Sentry issues (error groups) with frequency and status',
                                'when_to_use': 'Questions about errors, crashes, or bug frequency',
                                'trigger_phrases': [
                                    'sentry issue',
                                    'error',
                                    'crash',
                                    'bug frequency',
                                ],
                                'freshness': 'live',
                                'example_questions': ['What are the top Sentry issues?', 'Show unresolved errors'],
                                'search_strategy': 'Search by title or filter by project, status, or frequency',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Sentry issues (error groups) with frequency and status',
                            'when_to_use': 'Questions about errors, crashes, or bug frequency',
                            'trigger_phrases': [
                                'sentry issue',
                                'error',
                                'crash',
                                'bug frequency',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What are the top Sentry issues?', 'Show unresolved errors'],
                            'search_strategy': 'Search by title or filter by project, status, or frequency',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Sentry issues (error groups) with frequency and status',
                    'when_to_use': 'Questions about errors, crashes, or bug frequency',
                    'trigger_phrases': [
                        'sentry issue',
                        'error',
                        'crash',
                        'bug frequency',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What are the top Sentry issues?', 'Show unresolved errors'],
                    'search_strategy': 'Search by title or filter by project, status, or frequency',
                },
            },
            ai_hints={
                'summary': 'Sentry issues (error groups) with frequency and status',
                'when_to_use': 'Questions about errors, crashes, or bug frequency',
                'trigger_phrases': [
                    'sentry issue',
                    'error',
                    'crash',
                    'bug frequency',
                ],
                'freshness': 'live',
                'example_questions': ['What are the top Sentry issues?', 'Show unresolved errors'],
                'search_strategy': 'Search by title or filter by project, status, or frequency',
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Individual error events with stack traces and context',
                                'when_to_use': 'Investigating specific error occurrences or stack traces',
                                'trigger_phrases': ['error event', 'stack trace', 'crash event'],
                                'freshness': 'live',
                                'example_questions': ['Show the latest error events'],
                                'search_strategy': 'Filter by issue or project',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Individual error events with stack traces and context',
                            'when_to_use': 'Investigating specific error occurrences or stack traces',
                            'trigger_phrases': ['error event', 'stack trace', 'crash event'],
                            'freshness': 'live',
                            'example_questions': ['Show the latest error events'],
                            'search_strategy': 'Filter by issue or project',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Individual error events with stack traces and context',
                    'when_to_use': 'Investigating specific error occurrences or stack traces',
                    'trigger_phrases': ['error event', 'stack trace', 'crash event'],
                    'freshness': 'live',
                    'example_questions': ['Show the latest error events'],
                    'search_strategy': 'Filter by issue or project',
                },
            },
            ai_hints={
                'summary': 'Individual error events with stack traces and context',
                'when_to_use': 'Investigating specific error occurrences or stack traces',
                'trigger_phrases': ['error event', 'stack trace', 'crash event'],
                'freshness': 'live',
                'example_questions': ['Show the latest error events'],
                'search_strategy': 'Filter by issue or project',
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
                            'x-airbyte-ai-hints': {
                                'summary': 'Software releases tracked in Sentry with deployment and error data',
                                'when_to_use': 'Questions about release health, deploy tracking, or regression detection',
                                'trigger_phrases': [
                                    'sentry release',
                                    'release health',
                                    'deploy',
                                    'regression',
                                ],
                                'freshness': 'live',
                                'example_questions': ['What is the latest release?', 'Did the new release introduce errors?'],
                                'search_strategy': 'Filter by project or search by version',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Software releases tracked in Sentry with deployment and error data',
                            'when_to_use': 'Questions about release health, deploy tracking, or regression detection',
                            'trigger_phrases': [
                                'sentry release',
                                'release health',
                                'deploy',
                                'regression',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What is the latest release?', 'Did the new release introduce errors?'],
                            'search_strategy': 'Filter by project or search by version',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Software releases tracked in Sentry with deployment and error data',
                    'when_to_use': 'Questions about release health, deploy tracking, or regression detection',
                    'trigger_phrases': [
                        'sentry release',
                        'release health',
                        'deploy',
                        'regression',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What is the latest release?', 'Did the new release introduce errors?'],
                    'search_strategy': 'Filter by project or search by version',
                },
            },
            ai_hints={
                'summary': 'Software releases tracked in Sentry with deployment and error data',
                'when_to_use': 'Questions about release health, deploy tracking, or regression detection',
                'trigger_phrases': [
                    'sentry release',
                    'release health',
                    'deploy',
                    'regression',
                ],
                'freshness': 'live',
                'example_questions': ['What is the latest release?', 'Did the new release introduce errors?'],
                'search_strategy': 'Filter by project or search by version',
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
                        'x-airbyte-ai-hints': {
                            'summary': 'Detailed Sentry project configuration and stats',
                            'when_to_use': 'Looking up detailed project settings or statistics',
                            'trigger_phrases': ['project detail', 'project settings', 'project stats'],
                            'freshness': 'live',
                            'example_questions': ['Show details for a Sentry project'],
                            'search_strategy': 'Retrieve by project slug',
                        },
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
                'x-airbyte-ai-hints': {
                    'summary': 'Detailed Sentry project configuration and stats',
                    'when_to_use': 'Looking up detailed project settings or statistics',
                    'trigger_phrases': ['project detail', 'project settings', 'project stats'],
                    'freshness': 'live',
                    'example_questions': ['Show details for a Sentry project'],
                    'search_strategy': 'Retrieve by project slug',
                },
            },
            ai_hints={
                'summary': 'Detailed Sentry project configuration and stats',
                'when_to_use': 'Looking up detailed project settings or statistics',
                'trigger_phrases': ['project detail', 'project settings', 'project stats'],
                'freshness': 'live',
                'example_questions': ['Show details for a Sentry project'],
                'search_strategy': 'Retrieve by project slug',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='project_detail',
                    target_entity='projects',
                    foreign_key='project_slug',
                    target_key='slug',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='events',
                suggested=True,
                x_airbyte_name='events',
                fields=[
                    CacheFieldConfig(
                        name='_meta',
                        type=['null', 'object'],
                        description='Meta information for data scrubbing.',
                    ),
                    CacheFieldConfig(
                        name='context',
                        type=['null', 'object'],
                        description='Additional context data.',
                    ),
                    CacheFieldConfig(
                        name='contexts',
                        type=['null', 'object'],
                        description='Structured context information.',
                    ),
                    CacheFieldConfig(
                        name='crashFile',
                        type=['null', 'string'],
                        description='Crash file reference.',
                    ),
                    CacheFieldConfig(
                        name='culprit',
                        type=['null', 'string'],
                        description='The culprit (source) of the event.',
                    ),
                    CacheFieldConfig(
                        name='dateCreated',
                        type=['string', 'null'],
                        description='When the event was created.',
                    ),
                    CacheFieldConfig(
                        name='dateReceived',
                        type=['null', 'string'],
                        description='When the event was received by Sentry.',
                    ),
                    CacheFieldConfig(
                        name='dist',
                        type=['null', 'string'],
                        description='Distribution information.',
                    ),
                    CacheFieldConfig(
                        name='entries',
                        type=['null', 'array'],
                        description='Event entries (exception, breadcrumbs, request, etc.).',
                    ),
                    CacheFieldConfig(
                        name='errors',
                        type=['null', 'array'],
                        description='Processing errors.',
                    ),
                    CacheFieldConfig(
                        name='event.type',
                        type=['string', 'null'],
                        description='The type of the event.',
                    ),
                    CacheFieldConfig(
                        name='eventID',
                        type=['string', 'null'],
                        description='Event ID as reported by the client.',
                    ),
                    CacheFieldConfig(
                        name='fingerprints',
                        type=['null', 'array'],
                        description='Fingerprints used for grouping.',
                    ),
                    CacheFieldConfig(
                        name='groupID',
                        type=['string', 'null'],
                        description='ID of the issue group this event belongs to.',
                    ),
                    CacheFieldConfig(
                        name='groupingConfig',
                        type=['null', 'object'],
                        description='Grouping configuration.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'enhancements': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['string', 'null'],
                        description='Unique event identifier.',
                    ),
                    CacheFieldConfig(
                        name='location',
                        type=['null', 'string'],
                        description='Location in source code.',
                    ),
                    CacheFieldConfig(
                        name='message',
                        type=['string', 'null'],
                        description='Event message.',
                    ),
                    CacheFieldConfig(
                        name='metadata',
                        type=['null', 'object'],
                        description='Event metadata.',
                        properties={
                            'title': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'in_app_frame_mix': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='occurrence',
                        type=['null', 'string'],
                        description='Occurrence information for the event.',
                    ),
                    CacheFieldConfig(
                        name='packages',
                        type=['null', 'object'],
                        description='Package information.',
                    ),
                    CacheFieldConfig(
                        name='platform',
                        type=['string', 'null'],
                        description='Platform the event was generated on.',
                    ),
                    CacheFieldConfig(
                        name='projectID',
                        type=['null', 'string'],
                        description='Project ID this event belongs to.',
                    ),
                    CacheFieldConfig(
                        name='sdk',
                        type=['null', 'string'],
                        description='SDK information.',
                    ),
                    CacheFieldConfig(
                        name='size',
                        type=['null', 'integer'],
                        description='Event payload size in bytes.',
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['array', 'null'],
                        description='Tags associated with the event.',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['string', 'null'],
                        description='Event title.',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Event type.',
                    ),
                    CacheFieldConfig(
                        name='user',
                        type=['null', 'object'],
                        description='User associated with the event.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'email': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'username': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'ip_address': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='issues',
                suggested=True,
                x_airbyte_name='issues',
                fields=[
                    CacheFieldConfig(
                        name='annotations',
                        type=['array', 'null'],
                        description='Annotations on the issue.',
                    ),
                    CacheFieldConfig(
                        name='assignedTo',
                        type=['null', 'object'],
                        description='User or team assigned to this issue.',
                    ),
                    CacheFieldConfig(
                        name='count',
                        type=['string', 'null'],
                        description='Number of events for this issue.',
                    ),
                    CacheFieldConfig(
                        name='culprit',
                        type=['string', 'null'],
                        description='The culprit (source) of the issue.',
                    ),
                    CacheFieldConfig(
                        name='firstSeen',
                        type=['string', 'null'],
                        description='When the issue was first seen.',
                    ),
                    CacheFieldConfig(
                        name='hasSeen',
                        type=['boolean', 'null'],
                        description='Whether the authenticated user has seen the issue.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['string', 'null'],
                        description='Unique issue identifier.',
                    ),
                    CacheFieldConfig(
                        name='isBookmarked',
                        type=['boolean', 'null'],
                        description='Whether the issue is bookmarked.',
                    ),
                    CacheFieldConfig(
                        name='isPublic',
                        type=['boolean', 'null'],
                        description='Whether the issue is public.',
                    ),
                    CacheFieldConfig(
                        name='isSubscribed',
                        type=['boolean', 'null'],
                        description='Whether the user is subscribed to the issue.',
                    ),
                    CacheFieldConfig(
                        name='isUnhandled',
                        type=['null', 'boolean'],
                        description='Whether the issue is from an unhandled error.',
                    ),
                    CacheFieldConfig(
                        name='issueCategory',
                        type=['null', 'string'],
                        description='The category classification of the issue.',
                    ),
                    CacheFieldConfig(
                        name='issueType',
                        type=['null', 'string'],
                        description='The type classification of the issue.',
                    ),
                    CacheFieldConfig(
                        name='lastSeen',
                        type=['string', 'null'],
                        description='When the issue was last seen.',
                    ),
                    CacheFieldConfig(
                        name='level',
                        type=['string', 'null'],
                        description='Issue severity level.',
                    ),
                    CacheFieldConfig(
                        name='logger',
                        type=['null', 'string'],
                        description='Logger that generated the issue.',
                    ),
                    CacheFieldConfig(
                        name='metadata',
                        type=['object', 'null'],
                        description='Issue metadata.',
                    ),
                    CacheFieldConfig(
                        name='numComments',
                        type=['integer', 'null'],
                        description='Number of comments on the issue.',
                    ),
                    CacheFieldConfig(
                        name='permalink',
                        type=['string', 'null'],
                        description='Permalink to the issue in the Sentry UI.',
                    ),
                    CacheFieldConfig(
                        name='platform',
                        type=['null', 'string'],
                        description='Platform for this issue.',
                    ),
                    CacheFieldConfig(
                        name='project',
                        type=['object', 'null'],
                        description='Project this issue belongs to.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'name': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'slug': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='shareId',
                        type=['null', 'string'],
                        description='Share ID if the issue is shared.',
                    ),
                    CacheFieldConfig(
                        name='shortId',
                        type=['string', 'null'],
                        description='Short human-readable identifier.',
                    ),
                    CacheFieldConfig(
                        name='stats',
                        type=['object', 'null'],
                        description='Issue event statistics.',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['string', 'null'],
                        description='Issue status (resolved, unresolved, ignored).',
                    ),
                    CacheFieldConfig(
                        name='statusDetails',
                        type=['object', 'null'],
                        description='Status detail information.',
                    ),
                    CacheFieldConfig(
                        name='subscriptionDetails',
                        type=['null', 'object'],
                        description='Subscription details.',
                    ),
                    CacheFieldConfig(
                        name='substatus',
                        type=['null', 'string'],
                        description='Issue substatus.',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['string', 'null'],
                        description='Issue title.',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['string', 'null'],
                        description='Issue type.',
                    ),
                    CacheFieldConfig(
                        name='userCount',
                        type=['integer', 'null'],
                        description='Number of users affected.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='projects',
                suggested=True,
                x_airbyte_name='projects',
                fields=[
                    CacheFieldConfig(
                        name='access',
                        type=['null', 'array'],
                        description='List of access permissions for the authenticated user.',
                    ),
                    CacheFieldConfig(
                        name='avatar',
                        type=['object', 'null'],
                        description='Project avatar information.',
                        properties={
                            'avatarUrl': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'avatarType': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'avatarUuid': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='color',
                        type=['string', 'null'],
                        description='Project color code.',
                    ),
                    CacheFieldConfig(
                        name='dateCreated',
                        type=['string', 'null'],
                        description='Date the project was created.',
                    ),
                    CacheFieldConfig(
                        name='features',
                        type=['array', 'null'],
                        description='List of enabled features.',
                    ),
                    CacheFieldConfig(
                        name='firstEvent',
                        type=['null', 'string'],
                        description='Timestamp of the first event.',
                    ),
                    CacheFieldConfig(
                        name='firstTransactionEvent',
                        type=['null', 'boolean'],
                        description='Whether a transaction event has been received.',
                    ),
                    CacheFieldConfig(
                        name='hasAccess',
                        type=['boolean', 'null'],
                        description='Whether the user has access to this project.',
                    ),
                    CacheFieldConfig(
                        name='hasCustomMetrics',
                        type=['null', 'boolean'],
                        description='Whether the project has custom metrics.',
                    ),
                    CacheFieldConfig(
                        name='hasFeedbacks',
                        type=['null', 'boolean'],
                        description='Whether the project has user feedback.',
                    ),
                    CacheFieldConfig(
                        name='hasMinifiedStackTrace',
                        type=['null', 'boolean'],
                        description='Whether the project has minified stack traces.',
                    ),
                    CacheFieldConfig(
                        name='hasMonitors',
                        type=['null', 'boolean'],
                        description='Whether the project has cron monitors.',
                    ),
                    CacheFieldConfig(
                        name='hasNewFeedbacks',
                        type=['null', 'boolean'],
                        description='Whether the project has new user feedback.',
                    ),
                    CacheFieldConfig(
                        name='hasProfiles',
                        type=['null', 'boolean'],
                        description='Whether the project has profiling data.',
                    ),
                    CacheFieldConfig(
                        name='hasReplays',
                        type=['null', 'boolean'],
                        description='Whether the project has session replays.',
                    ),
                    CacheFieldConfig(
                        name='hasSessions',
                        type=['null', 'boolean'],
                        description='Whether the project has session data.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['string', 'null'],
                        description='Unique project identifier.',
                    ),
                    CacheFieldConfig(
                        name='isBookmarked',
                        type=['boolean', 'null'],
                        description='Whether the project is bookmarked.',
                    ),
                    CacheFieldConfig(
                        name='isInternal',
                        type=['boolean', 'null'],
                        description='Whether the project is internal.',
                    ),
                    CacheFieldConfig(
                        name='isMember',
                        type=['boolean', 'null'],
                        description='Whether the authenticated user is a member.',
                    ),
                    CacheFieldConfig(
                        name='isPublic',
                        type=['boolean', 'null'],
                        description='Whether the project is public.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['string', 'null'],
                        description='Human-readable project name.',
                    ),
                    CacheFieldConfig(
                        name='organization',
                        type=['object', 'null'],
                        description='Organization this project belongs to.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'name': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'slug': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='platform',
                        type=['null', 'string'],
                        description='The platform for this project.',
                    ),
                    CacheFieldConfig(
                        name='slug',
                        type=['string', 'null'],
                        description='URL-friendly project identifier.',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['string', 'null'],
                        description='Project status.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='releases',
                suggested=True,
                x_airbyte_name='releases',
                fields=[
                    CacheFieldConfig(
                        name='authors',
                        type=['null', 'array'],
                        description='Authors of commits in this release.',
                    ),
                    CacheFieldConfig(
                        name='commitCount',
                        type=['null', 'integer'],
                        description='Number of commits in this release.',
                    ),
                    CacheFieldConfig(
                        name='currentProjectMeta',
                        type=['null', 'object'],
                        description='Metadata for the current project context.',
                    ),
                    CacheFieldConfig(
                        name='data',
                        type=['null', 'object'],
                        description='Additional release data.',
                    ),
                    CacheFieldConfig(
                        name='dateCreated',
                        type=['null', 'string'],
                        description='When the release was created.',
                    ),
                    CacheFieldConfig(
                        name='dateReleased',
                        type=['null', 'string'],
                        description='When the release was deployed.',
                    ),
                    CacheFieldConfig(
                        name='deployCount',
                        type=['null', 'integer'],
                        description='Number of deploys for this release.',
                    ),
                    CacheFieldConfig(
                        name='firstEvent',
                        type=['null', 'string'],
                        description='Timestamp of the first event in this release.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique release identifier.',
                    ),
                    CacheFieldConfig(
                        name='lastCommit',
                        type=['null', 'object'],
                        description='Last commit in this release.',
                    ),
                    CacheFieldConfig(
                        name='lastDeploy',
                        type=['null', 'object'],
                        description='Last deploy of this release.',
                    ),
                    CacheFieldConfig(
                        name='lastEvent',
                        type=['null', 'string'],
                        description='Timestamp of the last event in this release.',
                    ),
                    CacheFieldConfig(
                        name='newGroups',
                        type=['null', 'integer'],
                        description='Number of new issue groups in this release.',
                    ),
                    CacheFieldConfig(
                        name='owner',
                        type=['null', 'string'],
                        description='Owner of the release.',
                    ),
                    CacheFieldConfig(
                        name='projects',
                        type=['null', 'array'],
                        description='Projects associated with this release.',
                    ),
                    CacheFieldConfig(
                        name='ref',
                        type=['null', 'string'],
                        description='Git reference (commit SHA, tag, etc.).',
                    ),
                    CacheFieldConfig(
                        name='shortVersion',
                        type=['null', 'string'],
                        description='Short version string.',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Release status.',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['null', 'string'],
                        description='URL associated with the release.',
                    ),
                    CacheFieldConfig(
                        name='userAgent',
                        type=['null', 'string'],
                        description='User agent that created the release.',
                    ),
                    CacheFieldConfig(
                        name='version',
                        type=['null', 'string'],
                        description='Release version string.',
                    ),
                    CacheFieldConfig(
                        name='versionInfo',
                        type=['null', 'object'],
                        description='Parsed version information.',
                        properties={
                            'version': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'pre': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'raw': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'major': CacheFieldProperty(
                                        type=['null', 'integer'],
                                    ),
                                    'minor': CacheFieldProperty(
                                        type=['null', 'integer'],
                                    ),
                                    'patch': CacheFieldProperty(
                                        type=['null', 'integer'],
                                    ),
                                    'buildCode': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'components': CacheFieldProperty(
                                        type=['null', 'integer'],
                                    ),
                                },
                            ),
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'package': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'buildHash': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
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
        context_store_search=[
            'What are the most common unresolved issues?',
            'Which projects have the most events?',
            'Show me issues that were first seen this week',
            'Find releases created in the last month',
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