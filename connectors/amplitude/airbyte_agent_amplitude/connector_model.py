"""
Connector model for amplitude.

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

AmplitudeConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('fa9f58c6-2d03-4237-aaa4-07d75e0c1396'),
    name='amplitude',
    version='1.0.1',
    base_url='https://amplitude.com/api',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
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
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.cohorts',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
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
                        'start': {'type': 'string', 'required': True},
                        'end': {'type': 'string', 'required': True},
                        'm': {
                            'type': 'string',
                            'required': False,
                            'default': 'active',
                        },
                        'i': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
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
                            },
                        },
                    },
                    record_extractor='$.data',
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
                        'start': {'type': 'string', 'required': True},
                        'end': {'type': 'string', 'required': True},
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
                            },
                        },
                    },
                    record_extractor='$.data',
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
            },
        ),
    ],
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
        'events': [
            '$insert_id',
            'adid',
            'amplitude_attribution_ids',
            'amplitude_event_type',
            'amplitude_id',
            'app',
            'city',
            'client_event_time',
            'client_upload_time',
            'country',
            'data',
            'data_type',
            'device_brand',
            'device_carrier',
            'device_family',
            'device_id',
            'device_manufacturer',
            'device_model',
            'device_type',
            'dma',
            'event_id',
            'event_properties',
            'event_time',
            'event_type',
            'global_user_properties',
            'group_properties',
            'groups',
            'idfa',
            'ip_address',
            'is_attribution_event',
            'language',
            'library',
            'location_lat',
            'location_lng',
            'os_name',
            'os_version',
            'partner_id',
            'paying',
            'plan',
            'plan.branch',
            'plan.source',
            'plan.version',
            'platform',
            'processed_time',
            'region',
            'sample_rate',
            'server_received_time',
            'server_upload_time',
            'session_id',
            'source_id',
            'start_version',
            'user_creation_time',
            'user_id',
            'user_properties',
            'uuid',
            'version_name',
        ],
        'average_session_length': ['date', 'length'],
    },
)