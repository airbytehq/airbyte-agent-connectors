"""
Connector model for amplitude.

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
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

AmplitudeConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('fa9f58c6-2d03-4237-aaa4-07d75e0c1396'),
    name='amplitude',
    version='1.0.3',
    base_url='https://amplitude.com/api',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AuthConfigSpec(
            title='API Key Authentication',
            type='object',
            required=['api_key', 'secret_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Amplitude project API key. Find it in Settings > Projects in your Amplitude account.\n',
                ),
                'secret_key': AuthConfigFieldSpec(
                    title='Secret Key',
                    description='Your Amplitude project secret key. Find it in Settings > Projects in your Amplitude account.\n',
                ),
            },
            auth_mapping={'username': '${api_key}', 'password': '${secret_key}'},
            replication_auth_key_mapping={'api_key': 'api_key', 'secret_key': 'secret_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='annotations',
            stream_name='annotations',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/2/annotations',
                    action=Action.LIST,
                    description='Returns all chart annotations for the project.',
                    response_schema={
                        'type': 'object',
                        'description': 'List of annotations',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A chart annotation object',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique identifier for the annotation'},
                                        'date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'The date of the annotation',
                                        },
                                        'details': {
                                            'type': ['null', 'string'],
                                            'description': 'Additional details or information about the annotation',
                                        },
                                        'label': {
                                            'type': ['null', 'string'],
                                            'description': 'The label or title of the annotation',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'annotations',
                                    'x-airbyte-stream-name': 'annotations',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Annotations marking notable events on Amplitude charts',
                                        'when_to_use': 'Looking for event annotations or chart markers in Amplitude',
                                        'trigger_phrases': ['amplitude annotation', 'chart marker', 'event annotation'],
                                        'freshness': 'live',
                                        'example_questions': ['What annotations exist in Amplitude?', 'Show recent chart annotations'],
                                        'search_strategy': 'Search by label or date range',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    no_pagination='Amplitude /2/annotations returns the full annotation collection in a single response; no pagination cursor or offset is exposed.',
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/3/annotations/{annotation_id}',
                    action=Action.GET,
                    description='Retrieves a single chart annotation by ID.',
                    path_params=['annotation_id'],
                    path_params_schema={
                        'annotation_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Single annotation response',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A chart annotation object (v3 API format)',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Unique identifier for the annotation'},
                                    'start': {
                                        'type': ['null', 'string'],
                                        'description': 'Start timestamp in ISO 8601 format',
                                    },
                                    'end': {
                                        'type': ['null', 'string'],
                                        'description': 'End timestamp in ISO 8601 format',
                                    },
                                    'label': {
                                        'type': ['null', 'string'],
                                        'description': 'The label or title of the annotation',
                                    },
                                    'details': {
                                        'type': ['null', 'string'],
                                        'description': 'Additional details about the annotation',
                                    },
                                    'category': {
                                        'type': ['null', 'object'],
                                        'description': 'The annotation category',
                                        'properties': {
                                            'id': {'type': 'integer', 'description': 'Category ID'},
                                            'category': {'type': 'string', 'description': 'Category name'},
                                        },
                                    },
                                    'chart_id': {
                                        'type': ['null', 'string'],
                                        'description': 'The chart ID this annotation is associated with',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A chart annotation object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique identifier for the annotation'},
                    'date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'The date of the annotation',
                    },
                    'details': {
                        'type': ['null', 'string'],
                        'description': 'Additional details or information about the annotation',
                    },
                    'label': {
                        'type': ['null', 'string'],
                        'description': 'The label or title of the annotation',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'annotations',
                'x-airbyte-stream-name': 'annotations',
                'x-airbyte-ai-hints': {
                    'summary': 'Annotations marking notable events on Amplitude charts',
                    'when_to_use': 'Looking for event annotations or chart markers in Amplitude',
                    'trigger_phrases': ['amplitude annotation', 'chart marker', 'event annotation'],
                    'freshness': 'live',
                    'example_questions': ['What annotations exist in Amplitude?', 'Show recent chart annotations'],
                    'search_strategy': 'Search by label or date range',
                },
            },
            ai_hints={
                'summary': 'Annotations marking notable events on Amplitude charts',
                'when_to_use': 'Looking for event annotations or chart markers in Amplitude',
                'trigger_phrases': ['amplitude annotation', 'chart marker', 'event annotation'],
                'freshness': 'live',
                'example_questions': ['What annotations exist in Amplitude?', 'Show recent chart annotations'],
                'search_strategy': 'Search by label or date range',
            },
        ),
        EntityDefinition(
            name='cohorts',
            stream_name='cohorts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/3/cohorts',
                    action=Action.LIST,
                    description='Returns all cohorts for the project.',
                    response_schema={
                        'type': 'object',
                        'description': 'List of cohorts',
                        'properties': {
                            'cohorts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A user cohort object',
                                    'properties': {
                                        'appId': {
                                            'type': ['null', 'integer'],
                                            'description': 'The unique identifier of the application',
                                        },
                                        'archived': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort is archived',
                                        },
                                        'chart_id': {
                                            'type': ['null', 'string'],
                                            'description': 'The chart ID associated with the cohort',
                                        },
                                        'createdAt': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp when the cohort was created',
                                        },
                                        'definition': {
                                            'type': ['null', 'object'],
                                            'description': 'The definition or criteria for the cohort',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'A description of the cohort',
                                        },
                                        'edit_id': {
                                            'type': ['null', 'string'],
                                            'description': 'The edit ID for version control',
                                        },
                                        'finished': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort computation has finished',
                                        },
                                        'hidden': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort is hidden from view',
                                        },
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier for the cohort',
                                        },
                                        'is_official_content': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort is official content',
                                        },
                                        'is_predictive': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort is predictive',
                                        },
                                        'lastComputed': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp of the last computation',
                                        },
                                        'lastMod': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp of the last modification',
                                        },
                                        'last_viewed': {
                                            'type': ['null', 'integer'],
                                            'description': 'Timestamp when the cohort was last viewed',
                                        },
                                        'location_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Location identifier',
                                        },
                                        'metadata': {
                                            'type': ['null', 'array'],
                                            'description': 'Additional metadata',
                                            'items': {'type': 'string'},
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'The name of the cohort',
                                        },
                                        'owners': {
                                            'type': ['null', 'array'],
                                            'description': 'The owners of the cohort',
                                            'items': {'type': 'string'},
                                        },
                                        'popularity': {
                                            'type': ['null', 'integer'],
                                            'description': 'Popularity score of the cohort',
                                        },
                                        'published': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort is published',
                                        },
                                        'shortcut_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Shortcut identifiers',
                                            'items': {'type': 'string'},
                                        },
                                        'size': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of users in the cohort',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'The type of cohort',
                                        },
                                        'view_count': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of views',
                                        },
                                        'viewers': {
                                            'type': ['null', 'array'],
                                            'description': 'Users who have viewed the cohort',
                                            'items': {'type': 'string'},
                                        },
                                        'include_data_app_types': {
                                            'type': ['null', 'array'],
                                            'description': 'Data app types to include',
                                            'items': {'type': 'string'},
                                        },
                                        'per_app_metadata': {
                                            'type': ['null', 'object'],
                                            'description': 'Per-application metadata',
                                        },
                                        'cohort_definition_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of cohort definition',
                                        },
                                        'cohort_output_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Output type for the cohort',
                                        },
                                        'is_generated_content': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the cohort is generated content',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'cohorts',
                                    'x-airbyte-stream-name': 'cohorts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'User cohorts defined in Amplitude for behavioral segmentation',
                                        'when_to_use': 'Questions about user segments or behavioral cohorts',
                                        'trigger_phrases': ['amplitude cohort', 'user segment', 'behavioral group'],
                                        'freshness': 'live',
                                        'example_questions': ['List all Amplitude cohorts', 'What user cohorts are defined?'],
                                        'search_strategy': 'Search by name to find specific cohorts',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.cohorts',
                    no_pagination='Amplitude /3/cohorts returns all cohorts for the project in a single response; no pagination cursor is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/3/cohorts/{cohort_id}',
                    action=Action.GET,
                    description='Retrieves a single cohort by ID.',
                    path_params=['cohort_id'],
                    path_params_schema={
                        'cohort_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Single cohort response wrapper',
                        'properties': {
                            'cohort': {
                                'type': 'object',
                                'description': 'A user cohort object',
                                'properties': {
                                    'appId': {
                                        'type': ['null', 'integer'],
                                        'description': 'The unique identifier of the application',
                                    },
                                    'archived': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort is archived',
                                    },
                                    'chart_id': {
                                        'type': ['null', 'string'],
                                        'description': 'The chart ID associated with the cohort',
                                    },
                                    'createdAt': {
                                        'type': ['null', 'integer'],
                                        'description': 'Timestamp when the cohort was created',
                                    },
                                    'definition': {
                                        'type': ['null', 'object'],
                                        'description': 'The definition or criteria for the cohort',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'A description of the cohort',
                                    },
                                    'edit_id': {
                                        'type': ['null', 'string'],
                                        'description': 'The edit ID for version control',
                                    },
                                    'finished': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort computation has finished',
                                    },
                                    'hidden': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort is hidden from view',
                                    },
                                    'id': {
                                        'type': ['null', 'string'],
                                        'description': 'Unique identifier for the cohort',
                                    },
                                    'is_official_content': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort is official content',
                                    },
                                    'is_predictive': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort is predictive',
                                    },
                                    'lastComputed': {
                                        'type': ['null', 'integer'],
                                        'description': 'Timestamp of the last computation',
                                    },
                                    'lastMod': {
                                        'type': ['null', 'integer'],
                                        'description': 'Timestamp of the last modification',
                                    },
                                    'last_viewed': {
                                        'type': ['null', 'integer'],
                                        'description': 'Timestamp when the cohort was last viewed',
                                    },
                                    'location_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Location identifier',
                                    },
                                    'metadata': {
                                        'type': ['null', 'array'],
                                        'description': 'Additional metadata',
                                        'items': {'type': 'string'},
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'The name of the cohort',
                                    },
                                    'owners': {
                                        'type': ['null', 'array'],
                                        'description': 'The owners of the cohort',
                                        'items': {'type': 'string'},
                                    },
                                    'popularity': {
                                        'type': ['null', 'integer'],
                                        'description': 'Popularity score of the cohort',
                                    },
                                    'published': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort is published',
                                    },
                                    'shortcut_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Shortcut identifiers',
                                        'items': {'type': 'string'},
                                    },
                                    'size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of users in the cohort',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'The type of cohort',
                                    },
                                    'view_count': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of views',
                                    },
                                    'viewers': {
                                        'type': ['null', 'array'],
                                        'description': 'Users who have viewed the cohort',
                                        'items': {'type': 'string'},
                                    },
                                    'include_data_app_types': {
                                        'type': ['null', 'array'],
                                        'description': 'Data app types to include',
                                        'items': {'type': 'string'},
                                    },
                                    'per_app_metadata': {
                                        'type': ['null', 'object'],
                                        'description': 'Per-application metadata',
                                    },
                                    'cohort_definition_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Type of cohort definition',
                                    },
                                    'cohort_output_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Output type for the cohort',
                                    },
                                    'is_generated_content': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the cohort is generated content',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'cohorts',
                                'x-airbyte-stream-name': 'cohorts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'User cohorts defined in Amplitude for behavioral segmentation',
                                    'when_to_use': 'Questions about user segments or behavioral cohorts',
                                    'trigger_phrases': ['amplitude cohort', 'user segment', 'behavioral group'],
                                    'freshness': 'live',
                                    'example_questions': ['List all Amplitude cohorts', 'What user cohorts are defined?'],
                                    'search_strategy': 'Search by name to find specific cohorts',
                                },
                            },
                        },
                    },
                    record_extractor='$.cohort',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A user cohort object',
                'properties': {
                    'appId': {
                        'type': ['null', 'integer'],
                        'description': 'The unique identifier of the application',
                    },
                    'archived': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort is archived',
                    },
                    'chart_id': {
                        'type': ['null', 'string'],
                        'description': 'The chart ID associated with the cohort',
                    },
                    'createdAt': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp when the cohort was created',
                    },
                    'definition': {
                        'type': ['null', 'object'],
                        'description': 'The definition or criteria for the cohort',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'A description of the cohort',
                    },
                    'edit_id': {
                        'type': ['null', 'string'],
                        'description': 'The edit ID for version control',
                    },
                    'finished': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort computation has finished',
                    },
                    'hidden': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort is hidden from view',
                    },
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier for the cohort',
                    },
                    'is_official_content': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort is official content',
                    },
                    'is_predictive': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort is predictive',
                    },
                    'lastComputed': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp of the last computation',
                    },
                    'lastMod': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp of the last modification',
                    },
                    'last_viewed': {
                        'type': ['null', 'integer'],
                        'description': 'Timestamp when the cohort was last viewed',
                    },
                    'location_id': {
                        'type': ['null', 'string'],
                        'description': 'Location identifier',
                    },
                    'metadata': {
                        'type': ['null', 'array'],
                        'description': 'Additional metadata',
                        'items': {'type': 'string'},
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the cohort',
                    },
                    'owners': {
                        'type': ['null', 'array'],
                        'description': 'The owners of the cohort',
                        'items': {'type': 'string'},
                    },
                    'popularity': {
                        'type': ['null', 'integer'],
                        'description': 'Popularity score of the cohort',
                    },
                    'published': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort is published',
                    },
                    'shortcut_ids': {
                        'type': ['null', 'array'],
                        'description': 'Shortcut identifiers',
                        'items': {'type': 'string'},
                    },
                    'size': {
                        'type': ['null', 'integer'],
                        'description': 'Number of users in the cohort',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'The type of cohort',
                    },
                    'view_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of views',
                    },
                    'viewers': {
                        'type': ['null', 'array'],
                        'description': 'Users who have viewed the cohort',
                        'items': {'type': 'string'},
                    },
                    'include_data_app_types': {
                        'type': ['null', 'array'],
                        'description': 'Data app types to include',
                        'items': {'type': 'string'},
                    },
                    'per_app_metadata': {
                        'type': ['null', 'object'],
                        'description': 'Per-application metadata',
                    },
                    'cohort_definition_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of cohort definition',
                    },
                    'cohort_output_type': {
                        'type': ['null', 'string'],
                        'description': 'Output type for the cohort',
                    },
                    'is_generated_content': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the cohort is generated content',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'cohorts',
                'x-airbyte-stream-name': 'cohorts',
                'x-airbyte-ai-hints': {
                    'summary': 'User cohorts defined in Amplitude for behavioral segmentation',
                    'when_to_use': 'Questions about user segments or behavioral cohorts',
                    'trigger_phrases': ['amplitude cohort', 'user segment', 'behavioral group'],
                    'freshness': 'live',
                    'example_questions': ['List all Amplitude cohorts', 'What user cohorts are defined?'],
                    'search_strategy': 'Search by name to find specific cohorts',
                },
            },
            ai_hints={
                'summary': 'User cohorts defined in Amplitude for behavioral segmentation',
                'when_to_use': 'Questions about user segments or behavioral cohorts',
                'trigger_phrases': ['amplitude cohort', 'user segment', 'behavioral group'],
                'freshness': 'live',
                'example_questions': ['List all Amplitude cohorts', 'What user cohorts are defined?'],
                'search_strategy': 'Search by name to find specific cohorts',
            },
        ),
        EntityDefinition(
            name='events_list',
            stream_name='events_list',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/2/events/list',
                    action=Action.LIST,
                    description="Returns the list of event types with the current week's totals, unique users, and percentage of DAU.\n",
                    response_schema={
                        'type': 'object',
                        'description': 'List of event types',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An event type definition with weekly totals',
                                    'properties': {
                                        'autohidden': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is auto-hidden',
                                        },
                                        'clusters_hidden': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is hidden from clusters',
                                        },
                                        'deleted': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is deleted',
                                        },
                                        'display': {
                                            'type': ['null', 'string'],
                                            'description': 'Display name of the event',
                                        },
                                        'flow_hidden': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is hidden from Pathfinder',
                                        },
                                        'hidden': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is hidden',
                                        },
                                        'id': {'type': 'number', 'description': 'Unique identifier for the event type'},
                                        'in_waitroom': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is in the waitroom',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the event type',
                                        },
                                        'non_active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is marked as inactive',
                                        },
                                        'timeline_hidden': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event is hidden from the timeline',
                                        },
                                        'totals': {
                                            'type': ['null', 'number'],
                                            'description': 'Total number of times the event occurred this week',
                                        },
                                        'totals_delta': {
                                            'type': ['null', 'number'],
                                            'description': 'Change in totals from the previous period',
                                        },
                                        'value': {
                                            'type': ['null', 'string'],
                                            'description': 'Raw event name in the data',
                                        },
                                        'waitroom_approved': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the event has been approved from the waitroom',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'events_list',
                                    'x-airbyte-stream-name': 'events_list',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Event types tracked in Amplitude analytics',
                                        'when_to_use': 'Looking up which events are tracked or event definitions',
                                        'trigger_phrases': [
                                            'amplitude event',
                                            'tracked events',
                                            'event type',
                                            'event definition',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What events are tracked in Amplitude?', 'List all event types'],
                                        'search_strategy': 'Search by event name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    no_pagination='Amplitude /api/2/taxonomy/event returns the full event taxonomy for the project in a single response; no pagination cursor is exposed.',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An event type definition with weekly totals',
                'properties': {
                    'autohidden': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is auto-hidden',
                    },
                    'clusters_hidden': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is hidden from clusters',
                    },
                    'deleted': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is deleted',
                    },
                    'display': {
                        'type': ['null', 'string'],
                        'description': 'Display name of the event',
                    },
                    'flow_hidden': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is hidden from Pathfinder',
                    },
                    'hidden': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is hidden',
                    },
                    'id': {'type': 'number', 'description': 'Unique identifier for the event type'},
                    'in_waitroom': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is in the waitroom',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the event type',
                    },
                    'non_active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is marked as inactive',
                    },
                    'timeline_hidden': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event is hidden from the timeline',
                    },
                    'totals': {
                        'type': ['null', 'number'],
                        'description': 'Total number of times the event occurred this week',
                    },
                    'totals_delta': {
                        'type': ['null', 'number'],
                        'description': 'Change in totals from the previous period',
                    },
                    'value': {
                        'type': ['null', 'string'],
                        'description': 'Raw event name in the data',
                    },
                    'waitroom_approved': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the event has been approved from the waitroom',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'events_list',
                'x-airbyte-stream-name': 'events_list',
                'x-airbyte-ai-hints': {
                    'summary': 'Event types tracked in Amplitude analytics',
                    'when_to_use': 'Looking up which events are tracked or event definitions',
                    'trigger_phrases': [
                        'amplitude event',
                        'tracked events',
                        'event type',
                        'event definition',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What events are tracked in Amplitude?', 'List all event types'],
                    'search_strategy': 'Search by event name',
                },
            },
            ai_hints={
                'summary': 'Event types tracked in Amplitude analytics',
                'when_to_use': 'Looking up which events are tracked or event definitions',
                'trigger_phrases': [
                    'amplitude event',
                    'tracked events',
                    'event type',
                    'event definition',
                ],
                'freshness': 'live',
                'example_questions': ['What events are tracked in Amplitude?', 'List all event types'],
                'search_strategy': 'Search by event name',
            },
        ),
        EntityDefinition(
            name='active_users',
            stream_name='active_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/2/users',
                    action=Action.LIST,
                    description='Returns the number of active or new users for each day in the specified date range.\n',
                    query_params=[
                        'start',
                        'end',
                        'm',
                        'i',
                        'g',
                    ],
                    query_params_schema={
                        'start': {
                            'type': 'string',
                            'required': True,
                            'default': "{{ (now_utc() - duration('P365D')).strftime('%Y%m%d') }}",
                        },
                        'end': {
                            'type': 'string',
                            'required': True,
                            'default': "{{ now_utc().strftime('%Y%m%d') }}",
                        },
                        'm': {
                            'type': 'string',
                            'required': False,
                            'default': 'active',
                            'enum': ['active', 'new'],
                        },
                        'i': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                            'enum': [1, 7, 30],
                        },
                        'g': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Active users response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Active or new user count data',
                                'properties': {
                                    'series': {
                                        'type': ['null', 'array'],
                                        'description': 'An array with one element for each group, where each element is an array of metric values per date in xValues.\n',
                                        'items': {
                                            'type': 'array',
                                            'items': {'type': 'number'},
                                        },
                                    },
                                    'seriesCollapsed': {
                                        'type': ['null', 'array'],
                                        'description': 'Collapsed series values',
                                        'items': {
                                            'type': 'array',
                                            'items': {'type': 'number'},
                                        },
                                    },
                                    'seriesLabels': {
                                        'type': ['null', 'array'],
                                        'description': 'Labels for each series group',
                                        'items': {
                                            'type': ['string', 'integer'],
                                        },
                                    },
                                    'seriesMeta': {
                                        'type': ['null', 'array'],
                                        'description': 'Metadata for each segment',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'segmentIndex': {'type': 'integer'},
                                            },
                                        },
                                    },
                                    'xValues': {
                                        'type': ['null', 'array'],
                                        'description': 'Array of dates in YYYY-MM-DD format',
                                        'items': {'type': 'string'},
                                    },
                                },
                                'x-airbyte-entity-name': 'active_users',
                                'x-airbyte-stream-name': 'active_users',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Active user counts and trends from Amplitude',
                                    'when_to_use': 'Questions about daily/weekly/monthly active user metrics',
                                    'trigger_phrases': [
                                        'active users',
                                        'DAU',
                                        'MAU',
                                        'user activity',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['How many active users last month?', 'Show active user trends'],
                                    'search_strategy': 'Filter by date range for time-series data',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    no_pagination='Amplitude /2/users returns a bounded daily active-users aggregation scoped to the requested start/end date range; no pagination cursor is exposed.',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Active or new user count data',
                'properties': {
                    'series': {
                        'type': ['null', 'array'],
                        'description': 'An array with one element for each group, where each element is an array of metric values per date in xValues.\n',
                        'items': {
                            'type': 'array',
                            'items': {'type': 'number'},
                        },
                    },
                    'seriesCollapsed': {
                        'type': ['null', 'array'],
                        'description': 'Collapsed series values',
                        'items': {
                            'type': 'array',
                            'items': {'type': 'number'},
                        },
                    },
                    'seriesLabels': {
                        'type': ['null', 'array'],
                        'description': 'Labels for each series group',
                        'items': {
                            'type': ['string', 'integer'],
                        },
                    },
                    'seriesMeta': {
                        'type': ['null', 'array'],
                        'description': 'Metadata for each segment',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'segmentIndex': {'type': 'integer'},
                            },
                        },
                    },
                    'xValues': {
                        'type': ['null', 'array'],
                        'description': 'Array of dates in YYYY-MM-DD format',
                        'items': {'type': 'string'},
                    },
                },
                'x-airbyte-entity-name': 'active_users',
                'x-airbyte-stream-name': 'active_users',
                'x-airbyte-ai-hints': {
                    'summary': 'Active user counts and trends from Amplitude',
                    'when_to_use': 'Questions about daily/weekly/monthly active user metrics',
                    'trigger_phrases': [
                        'active users',
                        'DAU',
                        'MAU',
                        'user activity',
                    ],
                    'freshness': 'live',
                    'example_questions': ['How many active users last month?', 'Show active user trends'],
                    'search_strategy': 'Filter by date range for time-series data',
                },
            },
            ai_hints={
                'summary': 'Active user counts and trends from Amplitude',
                'when_to_use': 'Questions about daily/weekly/monthly active user metrics',
                'trigger_phrases': [
                    'active users',
                    'DAU',
                    'MAU',
                    'user activity',
                ],
                'freshness': 'live',
                'example_questions': ['How many active users last month?', 'Show active user trends'],
                'search_strategy': 'Filter by date range for time-series data',
            },
        ),
        EntityDefinition(
            name='average_session_length',
            stream_name='average_session_length',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/2/sessions/average',
                    action=Action.LIST,
                    description='Returns the average session length (in seconds) for each day in the specified date range.\n',
                    query_params=['start', 'end'],
                    query_params_schema={
                        'start': {
                            'type': 'string',
                            'required': True,
                            'default': "{{ (now_utc() - duration('P365D')).strftime('%Y%m%d') }}",
                        },
                        'end': {
                            'type': 'string',
                            'required': True,
                            'default': "{{ now_utc().strftime('%Y%m%d') }}",
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Average session length response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Average session length data',
                                'properties': {
                                    'series': {
                                        'type': ['null', 'array'],
                                        'description': 'An array with one element which is an array of average session lengths (in seconds) for each day.\n',
                                        'items': {
                                            'type': 'array',
                                            'items': {'type': 'number'},
                                        },
                                    },
                                    'seriesCollapsed': {
                                        'type': ['null', 'array'],
                                        'description': 'Collapsed series values',
                                        'items': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'setId': {'type': 'string'},
                                                    'value': {'type': 'number'},
                                                },
                                            },
                                        },
                                    },
                                    'seriesMeta': {
                                        'type': ['null', 'array'],
                                        'description': 'Labels for each segment',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'segmentIndex': {'type': 'integer'},
                                                'sessionIndex': {'type': 'integer'},
                                            },
                                        },
                                    },
                                    'xValues': {
                                        'type': ['null', 'array'],
                                        'description': 'Array of dates in YYYY-MM-DD format',
                                        'items': {'type': 'string'},
                                    },
                                },
                                'x-airbyte-entity-name': 'average_session_length',
                                'x-airbyte-stream-name': 'average_session_length',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Average session duration metrics from Amplitude',
                                    'when_to_use': 'Questions about user engagement or session duration',
                                    'trigger_phrases': ['session length', 'session duration', 'engagement time'],
                                    'freshness': 'live',
                                    'example_questions': ['What is the average session length?', 'Show session duration trends'],
                                    'search_strategy': 'Filter by date range for time-series data',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    no_pagination='Amplitude /2/sessions/average returns a bounded daily aggregation scoped to the requested start/end date range; no pagination cursor is exposed.',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Average session length data',
                'properties': {
                    'series': {
                        'type': ['null', 'array'],
                        'description': 'An array with one element which is an array of average session lengths (in seconds) for each day.\n',
                        'items': {
                            'type': 'array',
                            'items': {'type': 'number'},
                        },
                    },
                    'seriesCollapsed': {
                        'type': ['null', 'array'],
                        'description': 'Collapsed series values',
                        'items': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'setId': {'type': 'string'},
                                    'value': {'type': 'number'},
                                },
                            },
                        },
                    },
                    'seriesMeta': {
                        'type': ['null', 'array'],
                        'description': 'Labels for each segment',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'segmentIndex': {'type': 'integer'},
                                'sessionIndex': {'type': 'integer'},
                            },
                        },
                    },
                    'xValues': {
                        'type': ['null', 'array'],
                        'description': 'Array of dates in YYYY-MM-DD format',
                        'items': {'type': 'string'},
                    },
                },
                'x-airbyte-entity-name': 'average_session_length',
                'x-airbyte-stream-name': 'average_session_length',
                'x-airbyte-ai-hints': {
                    'summary': 'Average session duration metrics from Amplitude',
                    'when_to_use': 'Questions about user engagement or session duration',
                    'trigger_phrases': ['session length', 'session duration', 'engagement time'],
                    'freshness': 'live',
                    'example_questions': ['What is the average session length?', 'Show session duration trends'],
                    'search_strategy': 'Filter by date range for time-series data',
                },
            },
            ai_hints={
                'summary': 'Average session duration metrics from Amplitude',
                'when_to_use': 'Questions about user engagement or session duration',
                'trigger_phrases': ['session length', 'session duration', 'engagement time'],
                'freshness': 'live',
                'example_questions': ['What is the average session length?', 'Show session duration trends'],
                'search_strategy': 'Filter by date range for time-series data',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='annotations',
                x_airbyte_name='annotations',
                fields=[
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date when the annotation was made',
                    ),
                    CacheFieldConfig(
                        name='details',
                        type=['null', 'string'],
                        description='Additional details or information related to the annotation',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='The unique identifier for the annotation',
                    ),
                    CacheFieldConfig(
                        name='label',
                        type=['null', 'string'],
                        description='The label assigned to the annotation',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='cohorts',
                suggested=True,
                x_airbyte_name='cohorts',
                fields=[
                    CacheFieldConfig(
                        name='appId',
                        type=['null', 'integer'],
                        description='The unique identifier of the application',
                    ),
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Indicates if the cohort data is archived',
                    ),
                    CacheFieldConfig(
                        name='chart_id',
                        type=['null', 'string'],
                        description='The identifier of the chart associated with the cohort',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'integer'],
                        description='The timestamp when the cohort was created',
                    ),
                    CacheFieldConfig(
                        name='definition',
                        type=['null', 'object'],
                        description='The specific definition or criteria for the cohort',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='A brief explanation or summary of the cohort',
                    ),
                    CacheFieldConfig(
                        name='edit_id',
                        type=['null', 'string'],
                        description='The ID for editing purposes or version control',
                    ),
                    CacheFieldConfig(
                        name='finished',
                        type=['null', 'boolean'],
                        description='Indicates if the cohort data has been finalized',
                    ),
                    CacheFieldConfig(
                        name='hidden',
                        type=['null', 'boolean'],
                        description='Flag to determine if the cohort is hidden from view',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier for the cohort',
                    ),
                    CacheFieldConfig(
                        name='is_official_content',
                        type=['null', 'boolean'],
                        description='Indicates if the cohort data is official content',
                    ),
                    CacheFieldConfig(
                        name='is_predictive',
                        type=['null', 'boolean'],
                        description='Flag to indicate if the cohort is predictive',
                    ),
                    CacheFieldConfig(
                        name='lastComputed',
                        type=['null', 'integer'],
                        description='Timestamp of the last computation of cohort data',
                    ),
                    CacheFieldConfig(
                        name='lastMod',
                        type=['null', 'integer'],
                        description='Timestamp of the last modification made to the cohort',
                    ),
                    CacheFieldConfig(
                        name='last_viewed',
                        type=['null', 'integer'],
                        description='Timestamp when the cohort was last viewed',
                    ),
                    CacheFieldConfig(
                        name='location_id',
                        type=['null', 'string'],
                        description='Identifier of the location associated with the cohort',
                    ),
                    CacheFieldConfig(
                        name='metadata',
                        type=['null', 'array'],
                        description='Additional information or data related to the cohort',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='The name or title of the cohort',
                    ),
                    CacheFieldConfig(
                        name='owners',
                        type=['null', 'array'],
                        description='The owners or administrators of the cohort',
                    ),
                    CacheFieldConfig(
                        name='popularity',
                        type=['null', 'integer'],
                        description='Popularity rank or score of the cohort',
                    ),
                    CacheFieldConfig(
                        name='published',
                        type=['null', 'boolean'],
                        description='Status indicating if the cohort data is published',
                    ),
                    CacheFieldConfig(
                        name='shortcut_ids',
                        type=['null', 'array'],
                        description='Identifiers of any shortcuts associated with the cohort',
                    ),
                    CacheFieldConfig(
                        name='size',
                        type=['null', 'integer'],
                        description='Size or scale of the cohort data',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='The type or category of the cohort',
                    ),
                    CacheFieldConfig(
                        name='view_count',
                        type=['null', 'integer'],
                        description='The total count of views on the cohort data',
                    ),
                    CacheFieldConfig(
                        name='viewers',
                        type=['null', 'array'],
                        description='Users or viewers who have access to the cohort data',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='events_list',
                suggested=True,
                x_airbyte_name='events_list',
                fields=[
                    CacheFieldConfig(
                        name='autohidden',
                        type=['null', 'boolean'],
                        description='Whether the event is auto-hidden',
                    ),
                    CacheFieldConfig(
                        name='clusters_hidden',
                        type=['null', 'boolean'],
                        description='Whether the event is hidden from clusters',
                    ),
                    CacheFieldConfig(
                        name='deleted',
                        type=['null', 'boolean'],
                        description='Whether the event is deleted',
                    ),
                    CacheFieldConfig(
                        name='display',
                        type=['null', 'string'],
                        description='Display name of the event',
                    ),
                    CacheFieldConfig(
                        name='flow_hidden',
                        type=['null', 'boolean'],
                        description='Whether the event is hidden from Pathfinder',
                    ),
                    CacheFieldConfig(
                        name='hidden',
                        type=['null', 'boolean'],
                        description='Whether the event is hidden',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'number'],
                        description='Unique identifier for the event type',
                    ),
                    CacheFieldConfig(
                        name='in_waitroom',
                        type=['null', 'boolean'],
                        description='Whether the event is in the waitroom',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the event type',
                    ),
                    CacheFieldConfig(
                        name='non_active',
                        type=['null', 'boolean'],
                        description='Whether the event is marked as inactive',
                    ),
                    CacheFieldConfig(
                        name='timeline_hidden',
                        type=['null', 'boolean', 'number'],
                        description='Whether the event is hidden from the timeline',
                    ),
                    CacheFieldConfig(
                        name='totals',
                        type=['null', 'number'],
                        description='Total number of times the event occurred this week',
                    ),
                    CacheFieldConfig(
                        name='totals_delta',
                        type=['null', 'number'],
                        description='Change in totals from the previous period',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Raw event name in the data',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='active_users',
                suggested=True,
                x_airbyte_name='active_users',
                fields=[
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date for which the active user data is reported',
                    ),
                    CacheFieldConfig(
                        name='statistics',
                        type=['null', 'object'],
                        description='The statistics related to the active users for the given date',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='average_session_length',
                suggested=True,
                x_airbyte_name='average_session_length',
                fields=[
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='The date on which the session occurred',
                    ),
                    CacheFieldConfig(
                        name='length',
                        type=['null', 'number'],
                        description='The duration of the session in seconds',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
    search_field_paths={
        'annotations': [
            'date',
            'details',
            'id',
            'label',
        ],
        'cohorts': [
            'appId',
            'archived',
            'chart_id',
            'createdAt',
            'definition',
            'description',
            'edit_id',
            'finished',
            'hidden',
            'id',
            'is_official_content',
            'is_predictive',
            'lastComputed',
            'lastMod',
            'last_viewed',
            'location_id',
            'metadata',
            'metadata[]',
            'name',
            'owners',
            'owners[]',
            'popularity',
            'published',
            'shortcut_ids',
            'shortcut_ids[]',
            'size',
            'type',
            'view_count',
            'viewers',
            'viewers[]',
        ],
        'events_list': [
            'autohidden',
            'clusters_hidden',
            'deleted',
            'display',
            'flow_hidden',
            'hidden',
            'id',
            'in_waitroom',
            'name',
            'non_active',
            'timeline_hidden',
            'totals',
            'totals_delta',
            'value',
        ],
        'active_users': ['date', 'statistics'],
        'average_session_length': ['date', 'length'],
    },
    example_questions=ExampleQuestions(
        direct=['List all chart annotations in Amplitude', 'Show me all cohorts', 'List all event types'],
        context_store_search=['Which cohorts have more than 1000 users?', 'What are the most popular event types by total count?', 'Show me annotations created in the last month'],
        search=['Which cohorts have more than 1000 users?', 'What are the most popular event types by total count?', 'Show me annotations created in the last month'],
        unsupported=['Create a new annotation', 'Delete a cohort', 'Export raw event data'],
    ),
)