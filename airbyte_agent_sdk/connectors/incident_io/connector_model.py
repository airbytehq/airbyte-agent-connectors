"""
Connector model for incident-io.

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
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

IncidentIoConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('7926da90-399e-4f9f-9833-52d8dc3fcb29'),
    name='incident-io',
    version='1.0.4',
    base_url='https://api.incident.io',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your incident.io API key. Create one at https://app.incident.io/settings/api-keys',
                ),
            },
            auth_mapping={'token': '${api_key}'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='incidents',
            stream_name='incidents',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/incidents',
                    action=Action.LIST,
                    description='List all incidents for the organisation with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incidents': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An incident tracked in incident.io',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the incident'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name/title of the incident',
                                        },
                                        'reference': {
                                            'type': ['null', 'string'],
                                            'description': 'Human-readable reference (e.g. INC-123)',
                                        },
                                        'summary': {
                                            'type': ['null', 'string'],
                                            'description': 'Detailed summary of the incident',
                                        },
                                        'mode': {
                                            'type': ['null', 'string'],
                                            'description': 'Mode of the incident: standard, retrospective, test, or tutorial',
                                        },
                                        'visibility': {
                                            'type': ['null', 'string'],
                                            'description': 'Whether the incident is public or private',
                                        },
                                        'permalink': {
                                            'type': ['null', 'string'],
                                            'description': 'Link to the incident in the dashboard',
                                        },
                                        'call_url': {
                                            'type': ['null', 'string'],
                                            'description': 'URL of the call associated with the incident',
                                        },
                                        'slack_channel_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Slack channel ID for the incident',
                                        },
                                        'slack_channel_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Slack channel name for the incident',
                                        },
                                        'slack_team_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Slack team/workspace ID',
                                        },
                                        'has_debrief': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the incident has had a debrief',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the incident was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the incident was last updated',
                                        },
                                        'creator': {
                                            'type': ['null', 'object'],
                                            'description': 'The user who created the incident',
                                            'properties': {
                                                'user': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'email': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'role': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'slack_user_id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'incident_status': {
                                            'type': ['null', 'object'],
                                            'description': 'Current status of the incident',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'category': {
                                                    'type': ['null', 'string'],
                                                },
                                                'rank': {
                                                    'type': ['null', 'number'],
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'severity': {
                                            'type': ['null', 'object'],
                                            'description': 'Severity of the incident',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'rank': {
                                                    'type': ['null', 'number'],
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'incident_type': {
                                            'type': ['null', 'object'],
                                            'description': 'Type of the incident',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'create_in_triage': {
                                                    'type': ['null', 'string'],
                                                },
                                                'is_default': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'private_incidents_only': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'incident_role_assignments': {
                                            'type': ['null', 'array'],
                                            'description': 'Role assignments for the incident',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'assignee': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'email': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'role': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'slack_user_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'role': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'description': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'instructions': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'required': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'role_type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'shortform': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'created_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'updated_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'custom_field_entries': {
                                            'type': ['null', 'array'],
                                            'description': 'Custom field values for the incident',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'custom_field': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'description': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'field_type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'options': {
                                                                'type': ['null', 'array'],
                                                            },
                                                        },
                                                    },
                                                    'values': {
                                                        'type': ['null', 'array'],
                                                    },
                                                },
                                            },
                                        },
                                        'duration_metrics': {
                                            'type': ['null', 'array'],
                                            'description': 'Duration metrics associated with the incident',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'duration_metric': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'incident_timestamp_values': {
                                            'type': ['null', 'array'],
                                            'description': 'Timestamp values for the incident',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'incident_timestamp': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'rank': {
                                                                'type': ['null', 'number'],
                                                            },
                                                        },
                                                    },
                                                    'value': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'value': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'workload_minutes_late': {
                                            'type': ['null', 'number'],
                                            'description': 'Minutes of workload classified as late',
                                        },
                                        'workload_minutes_sleeping': {
                                            'type': ['null', 'number'],
                                            'description': 'Minutes of workload classified as sleeping',
                                        },
                                        'workload_minutes_total': {
                                            'type': ['null', 'number'],
                                            'description': 'Total workload minutes',
                                        },
                                        'workload_minutes_working': {
                                            'type': ['null', 'number'],
                                            'description': 'Minutes of workload classified as working',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'incidents',
                                    'x-airbyte-stream-name': 'incidents',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Incidents tracked in incident.io with severity, status, and timeline',
                                        'when_to_use': 'Questions about incidents, outages, or post-mortems',
                                        'trigger_phrases': [
                                            'incident',
                                            'outage',
                                            'post-mortem',
                                            'what happened',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent incidents', 'What incidents are open?'],
                                        'search_strategy': 'Search by name or filter by severity, status, or date',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.incidents',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/incidents/{id}',
                    action=Action.GET,
                    description='Get a single incident by ID or numeric reference.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident': {
                                'type': 'object',
                                'description': 'An incident tracked in incident.io',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the incident'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name/title of the incident',
                                    },
                                    'reference': {
                                        'type': ['null', 'string'],
                                        'description': 'Human-readable reference (e.g. INC-123)',
                                    },
                                    'summary': {
                                        'type': ['null', 'string'],
                                        'description': 'Detailed summary of the incident',
                                    },
                                    'mode': {
                                        'type': ['null', 'string'],
                                        'description': 'Mode of the incident: standard, retrospective, test, or tutorial',
                                    },
                                    'visibility': {
                                        'type': ['null', 'string'],
                                        'description': 'Whether the incident is public or private',
                                    },
                                    'permalink': {
                                        'type': ['null', 'string'],
                                        'description': 'Link to the incident in the dashboard',
                                    },
                                    'call_url': {
                                        'type': ['null', 'string'],
                                        'description': 'URL of the call associated with the incident',
                                    },
                                    'slack_channel_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Slack channel ID for the incident',
                                    },
                                    'slack_channel_name': {
                                        'type': ['null', 'string'],
                                        'description': 'Slack channel name for the incident',
                                    },
                                    'slack_team_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Slack team/workspace ID',
                                    },
                                    'has_debrief': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the incident has had a debrief',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the incident was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the incident was last updated',
                                    },
                                    'creator': {
                                        'type': ['null', 'object'],
                                        'description': 'The user who created the incident',
                                        'properties': {
                                            'user': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'email': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'role': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'slack_user_id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'incident_status': {
                                        'type': ['null', 'object'],
                                        'description': 'Current status of the incident',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'description': {
                                                'type': ['null', 'string'],
                                            },
                                            'category': {
                                                'type': ['null', 'string'],
                                            },
                                            'rank': {
                                                'type': ['null', 'number'],
                                            },
                                            'created_at': {
                                                'type': ['null', 'string'],
                                            },
                                            'updated_at': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'severity': {
                                        'type': ['null', 'object'],
                                        'description': 'Severity of the incident',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'description': {
                                                'type': ['null', 'string'],
                                            },
                                            'rank': {
                                                'type': ['null', 'number'],
                                            },
                                            'created_at': {
                                                'type': ['null', 'string'],
                                            },
                                            'updated_at': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'incident_type': {
                                        'type': ['null', 'object'],
                                        'description': 'Type of the incident',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'description': {
                                                'type': ['null', 'string'],
                                            },
                                            'create_in_triage': {
                                                'type': ['null', 'string'],
                                            },
                                            'is_default': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'private_incidents_only': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'created_at': {
                                                'type': ['null', 'string'],
                                            },
                                            'updated_at': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'incident_role_assignments': {
                                        'type': ['null', 'array'],
                                        'description': 'Role assignments for the incident',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'assignee': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'email': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'role': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'slack_user_id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'role': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'instructions': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'required': {
                                                            'type': ['null', 'boolean'],
                                                        },
                                                        'role_type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'shortform': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'created_at': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'updated_at': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'custom_field_entries': {
                                        'type': ['null', 'array'],
                                        'description': 'Custom field values for the incident',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'custom_field': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'field_type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'options': {
                                                            'type': ['null', 'array'],
                                                        },
                                                    },
                                                },
                                                'values': {
                                                    'type': ['null', 'array'],
                                                },
                                            },
                                        },
                                    },
                                    'duration_metrics': {
                                        'type': ['null', 'array'],
                                        'description': 'Duration metrics associated with the incident',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'duration_metric': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'incident_timestamp_values': {
                                        'type': ['null', 'array'],
                                        'description': 'Timestamp values for the incident',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'incident_timestamp': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'rank': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                                'value': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'value': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'workload_minutes_late': {
                                        'type': ['null', 'number'],
                                        'description': 'Minutes of workload classified as late',
                                    },
                                    'workload_minutes_sleeping': {
                                        'type': ['null', 'number'],
                                        'description': 'Minutes of workload classified as sleeping',
                                    },
                                    'workload_minutes_total': {
                                        'type': ['null', 'number'],
                                        'description': 'Total workload minutes',
                                    },
                                    'workload_minutes_working': {
                                        'type': ['null', 'number'],
                                        'description': 'Minutes of workload classified as working',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'incidents',
                                'x-airbyte-stream-name': 'incidents',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Incidents tracked in incident.io with severity, status, and timeline',
                                    'when_to_use': 'Questions about incidents, outages, or post-mortems',
                                    'trigger_phrases': [
                                        'incident',
                                        'outage',
                                        'post-mortem',
                                        'what happened',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Show recent incidents', 'What incidents are open?'],
                                    'search_strategy': 'Search by name or filter by severity, status, or date',
                                },
                            },
                        },
                    },
                    record_extractor='$.incident',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An incident tracked in incident.io',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the incident'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name/title of the incident',
                    },
                    'reference': {
                        'type': ['null', 'string'],
                        'description': 'Human-readable reference (e.g. INC-123)',
                    },
                    'summary': {
                        'type': ['null', 'string'],
                        'description': 'Detailed summary of the incident',
                    },
                    'mode': {
                        'type': ['null', 'string'],
                        'description': 'Mode of the incident: standard, retrospective, test, or tutorial',
                    },
                    'visibility': {
                        'type': ['null', 'string'],
                        'description': 'Whether the incident is public or private',
                    },
                    'permalink': {
                        'type': ['null', 'string'],
                        'description': 'Link to the incident in the dashboard',
                    },
                    'call_url': {
                        'type': ['null', 'string'],
                        'description': 'URL of the call associated with the incident',
                    },
                    'slack_channel_id': {
                        'type': ['null', 'string'],
                        'description': 'Slack channel ID for the incident',
                    },
                    'slack_channel_name': {
                        'type': ['null', 'string'],
                        'description': 'Slack channel name for the incident',
                    },
                    'slack_team_id': {
                        'type': ['null', 'string'],
                        'description': 'Slack team/workspace ID',
                    },
                    'has_debrief': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the incident has had a debrief',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the incident was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the incident was last updated',
                    },
                    'creator': {
                        'type': ['null', 'object'],
                        'description': 'The user who created the incident',
                        'properties': {
                            'user': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                    },
                                    'role': {
                                        'type': ['null', 'string'],
                                    },
                                    'slack_user_id': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    'incident_status': {
                        'type': ['null', 'object'],
                        'description': 'Current status of the incident',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                            'category': {
                                'type': ['null', 'string'],
                            },
                            'rank': {
                                'type': ['null', 'number'],
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'severity': {
                        'type': ['null', 'object'],
                        'description': 'Severity of the incident',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                            'rank': {
                                'type': ['null', 'number'],
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'incident_type': {
                        'type': ['null', 'object'],
                        'description': 'Type of the incident',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                            'create_in_triage': {
                                'type': ['null', 'string'],
                            },
                            'is_default': {
                                'type': ['null', 'boolean'],
                            },
                            'private_incidents_only': {
                                'type': ['null', 'boolean'],
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'incident_role_assignments': {
                        'type': ['null', 'array'],
                        'description': 'Role assignments for the incident',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'assignee': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                        },
                                        'role': {
                                            'type': ['null', 'string'],
                                        },
                                        'slack_user_id': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'role': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                        },
                                        'instructions': {
                                            'type': ['null', 'string'],
                                        },
                                        'required': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'role_type': {
                                            'type': ['null', 'string'],
                                        },
                                        'shortform': {
                                            'type': ['null', 'string'],
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'custom_field_entries': {
                        'type': ['null', 'array'],
                        'description': 'Custom field values for the incident',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'custom_field': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                        },
                                        'field_type': {
                                            'type': ['null', 'string'],
                                        },
                                        'options': {
                                            'type': ['null', 'array'],
                                        },
                                    },
                                },
                                'values': {
                                    'type': ['null', 'array'],
                                },
                            },
                        },
                    },
                    'duration_metrics': {
                        'type': ['null', 'array'],
                        'description': 'Duration metrics associated with the incident',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'duration_metric': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'incident_timestamp_values': {
                        'type': ['null', 'array'],
                        'description': 'Timestamp values for the incident',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'incident_timestamp': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'rank': {
                                            'type': ['null', 'number'],
                                        },
                                    },
                                },
                                'value': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'value': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'workload_minutes_late': {
                        'type': ['null', 'number'],
                        'description': 'Minutes of workload classified as late',
                    },
                    'workload_minutes_sleeping': {
                        'type': ['null', 'number'],
                        'description': 'Minutes of workload classified as sleeping',
                    },
                    'workload_minutes_total': {
                        'type': ['null', 'number'],
                        'description': 'Total workload minutes',
                    },
                    'workload_minutes_working': {
                        'type': ['null', 'number'],
                        'description': 'Minutes of workload classified as working',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'incidents',
                'x-airbyte-stream-name': 'incidents',
                'x-airbyte-ai-hints': {
                    'summary': 'Incidents tracked in incident.io with severity, status, and timeline',
                    'when_to_use': 'Questions about incidents, outages, or post-mortems',
                    'trigger_phrases': [
                        'incident',
                        'outage',
                        'post-mortem',
                        'what happened',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show recent incidents', 'What incidents are open?'],
                    'search_strategy': 'Search by name or filter by severity, status, or date',
                },
            },
            ai_hints={
                'summary': 'Incidents tracked in incident.io with severity, status, and timeline',
                'when_to_use': 'Questions about incidents, outages, or post-mortems',
                'trigger_phrases': [
                    'incident',
                    'outage',
                    'post-mortem',
                    'what happened',
                ],
                'freshness': 'live',
                'example_questions': ['Show recent incidents', 'What incidents are open?'],
                'search_strategy': 'Search by name or filter by severity, status, or date',
            },
        ),
        EntityDefinition(
            name='alerts',
            stream_name='alerts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/alerts',
                    action=Action.LIST,
                    description='List all alerts for the account with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'alerts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An alert ingested from an alert source',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the alert'},
                                        'title': {
                                            'type': ['null', 'string'],
                                            'description': 'Title of the alert',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the alert',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Status of the alert: firing or resolved',
                                        },
                                        'alert_source_id': {
                                            'type': ['null', 'string'],
                                            'description': 'ID of the alert source that generated this alert',
                                        },
                                        'deduplication_key': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication key uniquely referencing this alert from the source',
                                        },
                                        'source_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Link to the alert in the upstream system',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the alert was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the alert was last updated',
                                        },
                                        'resolved_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the alert was resolved',
                                        },
                                        'attributes': {
                                            'type': ['null', 'array'],
                                            'description': 'Structured alert attributes',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'attribute': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'array': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                        },
                                                    },
                                                    'value': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'literal': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'label': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'catalog_entry': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'id': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'name': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'catalog_type_id': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'alerts',
                                    'x-airbyte-stream-name': 'alerts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Alerts triggered in incident.io from monitoring systems',
                                        'when_to_use': 'Questions about alerts, monitoring triggers, or alert status',
                                        'trigger_phrases': ['alert', 'monitoring alert', 'triggered alert'],
                                        'freshness': 'live',
                                        'example_questions': ['What alerts are active?', 'Show recent alerts'],
                                        'search_strategy': 'Filter by status or source',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.alerts',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/alerts/{id}',
                    action=Action.GET,
                    description='Show a single alert by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'alert': {
                                'type': 'object',
                                'description': 'An alert ingested from an alert source',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the alert'},
                                    'title': {
                                        'type': ['null', 'string'],
                                        'description': 'Title of the alert',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the alert',
                                    },
                                    'status': {
                                        'type': ['null', 'string'],
                                        'description': 'Status of the alert: firing or resolved',
                                    },
                                    'alert_source_id': {
                                        'type': ['null', 'string'],
                                        'description': 'ID of the alert source that generated this alert',
                                    },
                                    'deduplication_key': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication key uniquely referencing this alert from the source',
                                    },
                                    'source_url': {
                                        'type': ['null', 'string'],
                                        'description': 'Link to the alert in the upstream system',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the alert was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the alert was last updated',
                                    },
                                    'resolved_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the alert was resolved',
                                    },
                                    'attributes': {
                                        'type': ['null', 'array'],
                                        'description': 'Structured alert attributes',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'attribute': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'array': {
                                                            'type': ['null', 'boolean'],
                                                        },
                                                    },
                                                },
                                                'value': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'literal': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'label': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'catalog_entry': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'name': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'catalog_type_id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'alerts',
                                'x-airbyte-stream-name': 'alerts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Alerts triggered in incident.io from monitoring systems',
                                    'when_to_use': 'Questions about alerts, monitoring triggers, or alert status',
                                    'trigger_phrases': ['alert', 'monitoring alert', 'triggered alert'],
                                    'freshness': 'live',
                                    'example_questions': ['What alerts are active?', 'Show recent alerts'],
                                    'search_strategy': 'Filter by status or source',
                                },
                            },
                        },
                    },
                    record_extractor='$.alert',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An alert ingested from an alert source',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the alert'},
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Title of the alert',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the alert',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Status of the alert: firing or resolved',
                    },
                    'alert_source_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the alert source that generated this alert',
                    },
                    'deduplication_key': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication key uniquely referencing this alert from the source',
                    },
                    'source_url': {
                        'type': ['null', 'string'],
                        'description': 'Link to the alert in the upstream system',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the alert was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the alert was last updated',
                    },
                    'resolved_at': {
                        'type': ['null', 'string'],
                        'description': 'When the alert was resolved',
                    },
                    'attributes': {
                        'type': ['null', 'array'],
                        'description': 'Structured alert attributes',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'attribute': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'array': {
                                            'type': ['null', 'boolean'],
                                        },
                                    },
                                },
                                'value': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'literal': {
                                            'type': ['null', 'string'],
                                        },
                                        'label': {
                                            'type': ['null', 'string'],
                                        },
                                        'catalog_entry': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'catalog_type_id': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'alerts',
                'x-airbyte-stream-name': 'alerts',
                'x-airbyte-ai-hints': {
                    'summary': 'Alerts triggered in incident.io from monitoring systems',
                    'when_to_use': 'Questions about alerts, monitoring triggers, or alert status',
                    'trigger_phrases': ['alert', 'monitoring alert', 'triggered alert'],
                    'freshness': 'live',
                    'example_questions': ['What alerts are active?', 'Show recent alerts'],
                    'search_strategy': 'Filter by status or source',
                },
            },
            ai_hints={
                'summary': 'Alerts triggered in incident.io from monitoring systems',
                'when_to_use': 'Questions about alerts, monitoring triggers, or alert status',
                'trigger_phrases': ['alert', 'monitoring alert', 'triggered alert'],
                'freshness': 'live',
                'example_questions': ['What alerts are active?', 'Show recent alerts'],
                'search_strategy': 'Filter by status or source',
            },
        ),
        EntityDefinition(
            name='escalations',
            stream_name='escalations',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/escalations',
                    action=Action.LIST,
                    description='List all escalations for the account with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'escalations': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An escalation that pages people via escalation paths',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the escalation'},
                                        'title': {
                                            'type': ['null', 'string'],
                                            'description': 'Title of the escalation',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Status: pending, triggered, acked, resolved, expired, cancelled, snoozed',
                                        },
                                        'escalation_path_id': {
                                            'type': ['null', 'string'],
                                            'description': 'ID of the escalation path used',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the escalation was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the escalation was last updated',
                                        },
                                        'creator': {
                                            'type': ['null', 'object'],
                                            'description': 'The creator of this escalation',
                                            'properties': {
                                                'alert': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'title': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'user': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'email': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'role': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'slack_user_id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                                'workflow': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'priority': {
                                            'type': ['null', 'object'],
                                            'description': 'Priority of the escalation',
                                            'properties': {
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'events': {
                                            'type': ['null', 'array'],
                                            'description': 'History of escalation events',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'event': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'occurred_at': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'urgency': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'users': {
                                                        'type': ['null', 'array'],
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'name': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'email': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'role': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'slack_user_id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'channels': {
                                                        'type': ['null', 'array'],
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'slack_channel_id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'slack_team_id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'microsoft_teams_channel_id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'microsoft_teams_team_id': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'related_incidents': {
                                            'type': ['null', 'array'],
                                            'description': 'Incidents related to this escalation',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'reference': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'summary': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'external_id': {
                                                        'type': ['null', 'integer'],
                                                    },
                                                    'status_category': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'visibility': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'related_alerts': {
                                            'type': ['null', 'array'],
                                            'description': 'Alerts related to this escalation',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'title': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'description': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'status': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'alert_source_id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'deduplication_key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'source_url': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'created_at': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'updated_at': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'resolved_at': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'escalations',
                                    'x-airbyte-stream-name': 'escalations',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Escalation paths and on-call routing rules',
                                        'when_to_use': 'Questions about escalation policies or who is on-call',
                                        'trigger_phrases': ['escalation', 'on-call', 'escalation path'],
                                        'freshness': 'live',
                                        'example_questions': ['What are the escalation paths?'],
                                        'search_strategy': 'List escalation policies',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.escalations',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/escalations/{id}',
                    action=Action.GET,
                    description='Show a specific escalation by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'escalation': {
                                'type': 'object',
                                'description': 'An escalation that pages people via escalation paths',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the escalation'},
                                    'title': {
                                        'type': ['null', 'string'],
                                        'description': 'Title of the escalation',
                                    },
                                    'status': {
                                        'type': ['null', 'string'],
                                        'description': 'Status: pending, triggered, acked, resolved, expired, cancelled, snoozed',
                                    },
                                    'escalation_path_id': {
                                        'type': ['null', 'string'],
                                        'description': 'ID of the escalation path used',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the escalation was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the escalation was last updated',
                                    },
                                    'creator': {
                                        'type': ['null', 'object'],
                                        'description': 'The creator of this escalation',
                                        'properties': {
                                            'alert': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'title': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                            'user': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'email': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'role': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'slack_user_id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                            'workflow': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'priority': {
                                        'type': ['null', 'object'],
                                        'description': 'Priority of the escalation',
                                        'properties': {
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'events': {
                                        'type': ['null', 'array'],
                                        'description': 'History of escalation events',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'event': {
                                                    'type': ['null', 'string'],
                                                },
                                                'occurred_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'urgency': {
                                                    'type': ['null', 'string'],
                                                },
                                                'users': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'email': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'role': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'slack_user_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'channels': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'slack_channel_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'slack_team_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'microsoft_teams_channel_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'microsoft_teams_team_id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'related_incidents': {
                                        'type': ['null', 'array'],
                                        'description': 'Incidents related to this escalation',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'reference': {
                                                    'type': ['null', 'string'],
                                                },
                                                'summary': {
                                                    'type': ['null', 'string'],
                                                },
                                                'external_id': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'status_category': {
                                                    'type': ['null', 'string'],
                                                },
                                                'visibility': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                    'related_alerts': {
                                        'type': ['null', 'array'],
                                        'description': 'Alerts related to this escalation',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'title': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'status': {
                                                    'type': ['null', 'string'],
                                                },
                                                'alert_source_id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'deduplication_key': {
                                                    'type': ['null', 'string'],
                                                },
                                                'source_url': {
                                                    'type': ['null', 'string'],
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'resolved_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'escalations',
                                'x-airbyte-stream-name': 'escalations',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Escalation paths and on-call routing rules',
                                    'when_to_use': 'Questions about escalation policies or who is on-call',
                                    'trigger_phrases': ['escalation', 'on-call', 'escalation path'],
                                    'freshness': 'live',
                                    'example_questions': ['What are the escalation paths?'],
                                    'search_strategy': 'List escalation policies',
                                },
                            },
                        },
                    },
                    record_extractor='$.escalation',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An escalation that pages people via escalation paths',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the escalation'},
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Title of the escalation',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Status: pending, triggered, acked, resolved, expired, cancelled, snoozed',
                    },
                    'escalation_path_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the escalation path used',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the escalation was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the escalation was last updated',
                    },
                    'creator': {
                        'type': ['null', 'object'],
                        'description': 'The creator of this escalation',
                        'properties': {
                            'alert': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                    },
                                    'title': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'user': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                    },
                                    'role': {
                                        'type': ['null', 'string'],
                                    },
                                    'slack_user_id': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                            'workflow': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    'priority': {
                        'type': ['null', 'object'],
                        'description': 'Priority of the escalation',
                        'properties': {
                            'name': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'events': {
                        'type': ['null', 'array'],
                        'description': 'History of escalation events',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'event': {
                                    'type': ['null', 'string'],
                                },
                                'occurred_at': {
                                    'type': ['null', 'string'],
                                },
                                'urgency': {
                                    'type': ['null', 'string'],
                                },
                                'users': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'email': {
                                                'type': ['null', 'string'],
                                            },
                                            'role': {
                                                'type': ['null', 'string'],
                                            },
                                            'slack_user_id': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'channels': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'slack_channel_id': {
                                                'type': ['null', 'string'],
                                            },
                                            'slack_team_id': {
                                                'type': ['null', 'string'],
                                            },
                                            'microsoft_teams_channel_id': {
                                                'type': ['null', 'string'],
                                            },
                                            'microsoft_teams_team_id': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'related_incidents': {
                        'type': ['null', 'array'],
                        'description': 'Incidents related to this escalation',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'reference': {
                                    'type': ['null', 'string'],
                                },
                                'summary': {
                                    'type': ['null', 'string'],
                                },
                                'external_id': {
                                    'type': ['null', 'integer'],
                                },
                                'status_category': {
                                    'type': ['null', 'string'],
                                },
                                'visibility': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'related_alerts': {
                        'type': ['null', 'array'],
                        'description': 'Alerts related to this escalation',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                },
                                'status': {
                                    'type': ['null', 'string'],
                                },
                                'alert_source_id': {
                                    'type': ['null', 'string'],
                                },
                                'deduplication_key': {
                                    'type': ['null', 'string'],
                                },
                                'source_url': {
                                    'type': ['null', 'string'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                },
                                'resolved_at': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'escalations',
                'x-airbyte-stream-name': 'escalations',
                'x-airbyte-ai-hints': {
                    'summary': 'Escalation paths and on-call routing rules',
                    'when_to_use': 'Questions about escalation policies or who is on-call',
                    'trigger_phrases': ['escalation', 'on-call', 'escalation path'],
                    'freshness': 'live',
                    'example_questions': ['What are the escalation paths?'],
                    'search_strategy': 'List escalation policies',
                },
            },
            ai_hints={
                'summary': 'Escalation paths and on-call routing rules',
                'when_to_use': 'Questions about escalation policies or who is on-call',
                'trigger_phrases': ['escalation', 'on-call', 'escalation path'],
                'freshness': 'live',
                'example_questions': ['What are the escalation paths?'],
                'search_strategy': 'List escalation policies',
            },
        ),
        EntityDefinition(
            name='users',
            stream_name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/users',
                    action=Action.LIST,
                    description='List all users for the organisation with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'users': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A user in the incident.io organisation',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the user'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Full name of the user',
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address of the user',
                                        },
                                        'role': {
                                            'type': ['null', 'string'],
                                            'description': 'Deprecated role field',
                                        },
                                        'slack_user_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Slack user ID',
                                        },
                                        'base_role': {
                                            'type': ['null', 'object'],
                                            'description': 'Base role assigned to the user',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'slug': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'custom_roles': {
                                            'type': ['null', 'array'],
                                            'description': 'Custom roles assigned to the user',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'users',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Users in incident.io with roles and on-call assignments',
                                        'when_to_use': 'Looking up team members or responder details',
                                        'trigger_phrases': ['incident.io user', 'responder', 'who is on-call'],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the responders?'],
                                        'search_strategy': 'Search by name or email',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.users',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/users/{id}',
                    action=Action.GET,
                    description='Get a single user by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'user': {
                                'type': 'object',
                                'description': 'A user in the incident.io organisation',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the user'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Full name of the user',
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                        'description': 'Email address of the user',
                                    },
                                    'role': {
                                        'type': ['null', 'string'],
                                        'description': 'Deprecated role field',
                                    },
                                    'slack_user_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Slack user ID',
                                    },
                                    'base_role': {
                                        'type': ['null', 'object'],
                                        'description': 'Base role assigned to the user',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'slug': {
                                                'type': ['null', 'string'],
                                            },
                                            'description': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'custom_roles': {
                                        'type': ['null', 'array'],
                                        'description': 'Custom roles assigned to the user',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'users',
                                'x-airbyte-stream-name': 'users',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Users in incident.io with roles and on-call assignments',
                                    'when_to_use': 'Looking up team members or responder details',
                                    'trigger_phrases': ['incident.io user', 'responder', 'who is on-call'],
                                    'freshness': 'live',
                                    'example_questions': ['Who are the responders?'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                        },
                    },
                    record_extractor='$.user',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A user in the incident.io organisation',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the user'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Full name of the user',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'Email address of the user',
                    },
                    'role': {
                        'type': ['null', 'string'],
                        'description': 'Deprecated role field',
                    },
                    'slack_user_id': {
                        'type': ['null', 'string'],
                        'description': 'Slack user ID',
                    },
                    'base_role': {
                        'type': ['null', 'object'],
                        'description': 'Base role assigned to the user',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'slug': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'custom_roles': {
                        'type': ['null', 'array'],
                        'description': 'Custom roles assigned to the user',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
                'x-airbyte-ai-hints': {
                    'summary': 'Users in incident.io with roles and on-call assignments',
                    'when_to_use': 'Looking up team members or responder details',
                    'trigger_phrases': ['incident.io user', 'responder', 'who is on-call'],
                    'freshness': 'live',
                    'example_questions': ['Who are the responders?'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Users in incident.io with roles and on-call assignments',
                'when_to_use': 'Looking up team members or responder details',
                'trigger_phrases': ['incident.io user', 'responder', 'who is on-call'],
                'freshness': 'live',
                'example_questions': ['Who are the responders?'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='incident_updates',
            stream_name='incident_updates',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/incident_updates',
                    action=Action.LIST,
                    description='List all incident updates for the organisation with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_updates': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An update posted to an incident',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the incident update'},
                                        'incident_id': {
                                            'type': ['null', 'string'],
                                            'description': 'ID of the incident this update belongs to',
                                        },
                                        'message': {
                                            'type': ['null', 'string'],
                                            'description': 'Update message content',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the update was created',
                                        },
                                        'new_incident_status': {
                                            'type': ['null', 'object'],
                                            'description': 'New incident status set by this update',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'category': {
                                                    'type': ['null', 'string'],
                                                },
                                                'rank': {
                                                    'type': ['null', 'number'],
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'new_severity': {
                                            'type': ['null', 'object'],
                                            'description': 'New severity set by this update',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'rank': {
                                                    'type': ['null', 'number'],
                                                },
                                                'created_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'updated_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'updater': {
                                            'type': ['null', 'object'],
                                            'description': 'Who made this update',
                                            'properties': {
                                                'user': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'email': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'role': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'slack_user_id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'incident_updates',
                                    'x-airbyte-stream-name': 'incident_updates',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Status updates posted during incident response',
                                        'when_to_use': 'Looking for incident timeline or status update history',
                                        'trigger_phrases': ['incident update', 'status update', 'incident timeline'],
                                        'freshness': 'live',
                                        'example_questions': ['What updates were posted for an incident?'],
                                        'search_strategy': 'Filter by incident',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_updates',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An update posted to an incident',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the incident update'},
                    'incident_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the incident this update belongs to',
                    },
                    'message': {
                        'type': ['null', 'string'],
                        'description': 'Update message content',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the update was created',
                    },
                    'new_incident_status': {
                        'type': ['null', 'object'],
                        'description': 'New incident status set by this update',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                            'category': {
                                'type': ['null', 'string'],
                            },
                            'rank': {
                                'type': ['null', 'number'],
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'new_severity': {
                        'type': ['null', 'object'],
                        'description': 'New severity set by this update',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'name': {
                                'type': ['null', 'string'],
                            },
                            'description': {
                                'type': ['null', 'string'],
                            },
                            'rank': {
                                'type': ['null', 'number'],
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'updater': {
                        'type': ['null', 'object'],
                        'description': 'Who made this update',
                        'properties': {
                            'user': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                    },
                                    'role': {
                                        'type': ['null', 'string'],
                                    },
                                    'slack_user_id': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'incident_updates',
                'x-airbyte-stream-name': 'incident_updates',
                'x-airbyte-ai-hints': {
                    'summary': 'Status updates posted during incident response',
                    'when_to_use': 'Looking for incident timeline or status update history',
                    'trigger_phrases': ['incident update', 'status update', 'incident timeline'],
                    'freshness': 'live',
                    'example_questions': ['What updates were posted for an incident?'],
                    'search_strategy': 'Filter by incident',
                },
            },
            ai_hints={
                'summary': 'Status updates posted during incident response',
                'when_to_use': 'Looking for incident timeline or status update history',
                'trigger_phrases': ['incident update', 'status update', 'incident timeline'],
                'freshness': 'live',
                'example_questions': ['What updates were posted for an incident?'],
                'search_strategy': 'Filter by incident',
            },
        ),
        EntityDefinition(
            name='incident_roles',
            stream_name='incident_roles',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/incident_roles',
                    action=Action.LIST,
                    description='List all incident roles for the organisation.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_roles': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A role that can be assigned during an incident',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the incident role'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the role',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the role',
                                        },
                                        'instructions': {
                                            'type': ['null', 'string'],
                                            'description': 'Instructions for the role holder',
                                        },
                                        'shortform': {
                                            'type': ['null', 'string'],
                                            'description': 'Short form label for the role',
                                        },
                                        'role_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of role (e.g. lead, custom)',
                                        },
                                        'required': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this role must be assigned',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the role was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the role was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'incident_roles',
                                    'x-airbyte-stream-name': 'incident_roles',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Roles assigned during incident response (lead, comms, etc.)',
                                        'when_to_use': 'Questions about incident response role definitions',
                                        'trigger_phrases': ['incident role', 'response role', 'incident lead'],
                                        'freshness': 'static',
                                        'example_questions': ['What incident roles are defined?'],
                                        'search_strategy': 'List all incident roles',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_roles',
                    no_pagination='incident.io incident roles endpoint returns the full bounded configuration set; the API does not expose pagination on this endpoint.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/incident_roles/{id}',
                    action=Action.GET,
                    description='Get a single incident role by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_role': {
                                'type': 'object',
                                'description': 'A role that can be assigned during an incident',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the incident role'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the role',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the role',
                                    },
                                    'instructions': {
                                        'type': ['null', 'string'],
                                        'description': 'Instructions for the role holder',
                                    },
                                    'shortform': {
                                        'type': ['null', 'string'],
                                        'description': 'Short form label for the role',
                                    },
                                    'role_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Type of role (e.g. lead, custom)',
                                    },
                                    'required': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether this role must be assigned',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the role was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the role was last updated',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'incident_roles',
                                'x-airbyte-stream-name': 'incident_roles',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Roles assigned during incident response (lead, comms, etc.)',
                                    'when_to_use': 'Questions about incident response role definitions',
                                    'trigger_phrases': ['incident role', 'response role', 'incident lead'],
                                    'freshness': 'static',
                                    'example_questions': ['What incident roles are defined?'],
                                    'search_strategy': 'List all incident roles',
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_role',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A role that can be assigned during an incident',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the incident role'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the role',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the role',
                    },
                    'instructions': {
                        'type': ['null', 'string'],
                        'description': 'Instructions for the role holder',
                    },
                    'shortform': {
                        'type': ['null', 'string'],
                        'description': 'Short form label for the role',
                    },
                    'role_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of role (e.g. lead, custom)',
                    },
                    'required': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this role must be assigned',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the role was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the role was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'incident_roles',
                'x-airbyte-stream-name': 'incident_roles',
                'x-airbyte-ai-hints': {
                    'summary': 'Roles assigned during incident response (lead, comms, etc.)',
                    'when_to_use': 'Questions about incident response role definitions',
                    'trigger_phrases': ['incident role', 'response role', 'incident lead'],
                    'freshness': 'static',
                    'example_questions': ['What incident roles are defined?'],
                    'search_strategy': 'List all incident roles',
                },
            },
            ai_hints={
                'summary': 'Roles assigned during incident response (lead, comms, etc.)',
                'when_to_use': 'Questions about incident response role definitions',
                'trigger_phrases': ['incident role', 'response role', 'incident lead'],
                'freshness': 'static',
                'example_questions': ['What incident roles are defined?'],
                'search_strategy': 'List all incident roles',
            },
        ),
        EntityDefinition(
            name='incident_statuses',
            stream_name='incident_statuses',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/incident_statuses',
                    action=Action.LIST,
                    description='List all incident statuses for the organisation.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_statuses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A status that an incident can be in',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the status'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the status',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the status',
                                        },
                                        'category': {
                                            'type': ['null', 'string'],
                                            'description': 'Category: triage, active, post-incident, closed, etc.',
                                        },
                                        'rank': {
                                            'type': ['null', 'number'],
                                            'description': 'Rank for ordering',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the status was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the status was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'incident_statuses',
                                    'x-airbyte-stream-name': 'incident_statuses',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Incident lifecycle statuses (investigating, mitigated, resolved)',
                                        'when_to_use': 'Questions about incident status workflow or definitions',
                                        'trigger_phrases': ['incident status', 'status definition'],
                                        'freshness': 'static',
                                        'example_questions': ['What incident statuses are available?'],
                                        'search_strategy': 'List all statuses',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_statuses',
                    no_pagination='incident.io incident statuses endpoint returns the full bounded configuration set; the API does not expose pagination on this endpoint.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/incident_statuses/{id}',
                    action=Action.GET,
                    description='Get a single incident status by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_status': {
                                'type': 'object',
                                'description': 'A status that an incident can be in',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the status'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the status',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the status',
                                    },
                                    'category': {
                                        'type': ['null', 'string'],
                                        'description': 'Category: triage, active, post-incident, closed, etc.',
                                    },
                                    'rank': {
                                        'type': ['null', 'number'],
                                        'description': 'Rank for ordering',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the status was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the status was last updated',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'incident_statuses',
                                'x-airbyte-stream-name': 'incident_statuses',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Incident lifecycle statuses (investigating, mitigated, resolved)',
                                    'when_to_use': 'Questions about incident status workflow or definitions',
                                    'trigger_phrases': ['incident status', 'status definition'],
                                    'freshness': 'static',
                                    'example_questions': ['What incident statuses are available?'],
                                    'search_strategy': 'List all statuses',
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_status',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A status that an incident can be in',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the status'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the status',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the status',
                    },
                    'category': {
                        'type': ['null', 'string'],
                        'description': 'Category: triage, active, post-incident, closed, etc.',
                    },
                    'rank': {
                        'type': ['null', 'number'],
                        'description': 'Rank for ordering',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the status was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the status was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'incident_statuses',
                'x-airbyte-stream-name': 'incident_statuses',
                'x-airbyte-ai-hints': {
                    'summary': 'Incident lifecycle statuses (investigating, mitigated, resolved)',
                    'when_to_use': 'Questions about incident status workflow or definitions',
                    'trigger_phrases': ['incident status', 'status definition'],
                    'freshness': 'static',
                    'example_questions': ['What incident statuses are available?'],
                    'search_strategy': 'List all statuses',
                },
            },
            ai_hints={
                'summary': 'Incident lifecycle statuses (investigating, mitigated, resolved)',
                'when_to_use': 'Questions about incident status workflow or definitions',
                'trigger_phrases': ['incident status', 'status definition'],
                'freshness': 'static',
                'example_questions': ['What incident statuses are available?'],
                'search_strategy': 'List all statuses',
            },
        ),
        EntityDefinition(
            name='incident_timestamps',
            stream_name='incident_timestamps',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/incident_timestamps',
                    action=Action.LIST,
                    description='List all incident timestamps for the organisation.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_timestamps': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A timestamp definition for incidents',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the timestamp'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the timestamp (e.g. Reported, Resolved)',
                                        },
                                        'rank': {
                                            'type': ['null', 'number'],
                                            'description': 'Rank for ordering',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'incident_timestamps',
                                    'x-airbyte-stream-name': 'incident_timestamps',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Key timestamps during incident lifecycle (detected, resolved, etc.)',
                                        'when_to_use': 'Questions about incident timing or duration analysis',
                                        'trigger_phrases': ['incident timestamp', 'time to resolve', 'incident duration'],
                                        'freshness': 'live',
                                        'example_questions': ['How long did an incident take to resolve?'],
                                        'search_strategy': 'Filter by incident',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_timestamps',
                    no_pagination='incident.io incident timestamps endpoint returns the full bounded configuration set; the API does not expose pagination on this endpoint.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/incident_timestamps/{id}',
                    action=Action.GET,
                    description='Get a single incident timestamp by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'incident_timestamp': {
                                'type': 'object',
                                'description': 'A timestamp definition for incidents',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the timestamp'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the timestamp (e.g. Reported, Resolved)',
                                    },
                                    'rank': {
                                        'type': ['null', 'number'],
                                        'description': 'Rank for ordering',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'incident_timestamps',
                                'x-airbyte-stream-name': 'incident_timestamps',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Key timestamps during incident lifecycle (detected, resolved, etc.)',
                                    'when_to_use': 'Questions about incident timing or duration analysis',
                                    'trigger_phrases': ['incident timestamp', 'time to resolve', 'incident duration'],
                                    'freshness': 'live',
                                    'example_questions': ['How long did an incident take to resolve?'],
                                    'search_strategy': 'Filter by incident',
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_timestamp',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A timestamp definition for incidents',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the timestamp'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the timestamp (e.g. Reported, Resolved)',
                    },
                    'rank': {
                        'type': ['null', 'number'],
                        'description': 'Rank for ordering',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'incident_timestamps',
                'x-airbyte-stream-name': 'incident_timestamps',
                'x-airbyte-ai-hints': {
                    'summary': 'Key timestamps during incident lifecycle (detected, resolved, etc.)',
                    'when_to_use': 'Questions about incident timing or duration analysis',
                    'trigger_phrases': ['incident timestamp', 'time to resolve', 'incident duration'],
                    'freshness': 'live',
                    'example_questions': ['How long did an incident take to resolve?'],
                    'search_strategy': 'Filter by incident',
                },
            },
            ai_hints={
                'summary': 'Key timestamps during incident lifecycle (detected, resolved, etc.)',
                'when_to_use': 'Questions about incident timing or duration analysis',
                'trigger_phrases': ['incident timestamp', 'time to resolve', 'incident duration'],
                'freshness': 'live',
                'example_questions': ['How long did an incident take to resolve?'],
                'search_strategy': 'Filter by incident',
            },
        ),
        EntityDefinition(
            name='severities',
            stream_name='severities',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/severities',
                    action=Action.LIST,
                    description='List all severities for the organisation.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'severities': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A severity level for incidents',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the severity'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the severity (e.g. SEV1, Critical)',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the severity',
                                        },
                                        'rank': {
                                            'type': ['null', 'number'],
                                            'description': 'Rank for ordering (lower is more severe)',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the severity was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the severity was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'severities',
                                    'x-airbyte-stream-name': 'severities',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Severity level definitions for incidents',
                                        'when_to_use': 'Questions about severity classification or impact levels',
                                        'trigger_phrases': ['severity', 'severity level', 'impact level'],
                                        'freshness': 'static',
                                        'example_questions': ['What severity levels are defined?'],
                                        'search_strategy': 'List all severities',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.severities',
                    no_pagination='incident.io severities endpoint returns the full bounded configuration set; the API does not expose pagination on this endpoint.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/severities/{id}',
                    action=Action.GET,
                    description='Get a single severity by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'severity': {
                                'type': 'object',
                                'description': 'A severity level for incidents',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the severity'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the severity (e.g. SEV1, Critical)',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the severity',
                                    },
                                    'rank': {
                                        'type': ['null', 'number'],
                                        'description': 'Rank for ordering (lower is more severe)',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the severity was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the severity was last updated',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'severities',
                                'x-airbyte-stream-name': 'severities',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Severity level definitions for incidents',
                                    'when_to_use': 'Questions about severity classification or impact levels',
                                    'trigger_phrases': ['severity', 'severity level', 'impact level'],
                                    'freshness': 'static',
                                    'example_questions': ['What severity levels are defined?'],
                                    'search_strategy': 'List all severities',
                                },
                            },
                        },
                    },
                    record_extractor='$.severity',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A severity level for incidents',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the severity'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the severity (e.g. SEV1, Critical)',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the severity',
                    },
                    'rank': {
                        'type': ['null', 'number'],
                        'description': 'Rank for ordering (lower is more severe)',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the severity was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the severity was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'severities',
                'x-airbyte-stream-name': 'severities',
                'x-airbyte-ai-hints': {
                    'summary': 'Severity level definitions for incidents',
                    'when_to_use': 'Questions about severity classification or impact levels',
                    'trigger_phrases': ['severity', 'severity level', 'impact level'],
                    'freshness': 'static',
                    'example_questions': ['What severity levels are defined?'],
                    'search_strategy': 'List all severities',
                },
            },
            ai_hints={
                'summary': 'Severity level definitions for incidents',
                'when_to_use': 'Questions about severity classification or impact levels',
                'trigger_phrases': ['severity', 'severity level', 'impact level'],
                'freshness': 'static',
                'example_questions': ['What severity levels are defined?'],
                'search_strategy': 'List all severities',
            },
        ),
        EntityDefinition(
            name='custom_fields',
            stream_name='custom_fields',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/custom_fields',
                    action=Action.LIST,
                    description='List all custom fields for the organisation.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'custom_fields': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A custom field definition for incidents',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the custom field'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the custom field',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the custom field',
                                        },
                                        'field_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of field: single_select, multi_select, text, link, numeric',
                                        },
                                        'catalog_type_id': {
                                            'type': ['null', 'string'],
                                            'description': 'ID of the catalog type associated with this custom field',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the custom field was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the custom field was last updated',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'custom_fields',
                                    'x-airbyte-stream-name': 'custom_fields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom fields for capturing additional incident metadata',
                                        'when_to_use': 'Questions about custom incident data fields',
                                        'trigger_phrases': ['custom field', 'incident field'],
                                        'freshness': 'static',
                                        'example_questions': ['What custom fields are on incidents?'],
                                        'search_strategy': 'List all custom fields',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.custom_fields',
                    no_pagination='incident.io custom fields endpoint returns the full bounded configuration set; the API does not expose pagination on this endpoint.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/custom_fields/{id}',
                    action=Action.GET,
                    description='Get a single custom field by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'custom_field': {
                                'type': 'object',
                                'description': 'A custom field definition for incidents',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the custom field'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the custom field',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the custom field',
                                    },
                                    'field_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Type of field: single_select, multi_select, text, link, numeric',
                                    },
                                    'catalog_type_id': {
                                        'type': ['null', 'string'],
                                        'description': 'ID of the catalog type associated with this custom field',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the custom field was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the custom field was last updated',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'custom_fields',
                                'x-airbyte-stream-name': 'custom_fields',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Custom fields for capturing additional incident metadata',
                                    'when_to_use': 'Questions about custom incident data fields',
                                    'trigger_phrases': ['custom field', 'incident field'],
                                    'freshness': 'static',
                                    'example_questions': ['What custom fields are on incidents?'],
                                    'search_strategy': 'List all custom fields',
                                },
                            },
                        },
                    },
                    record_extractor='$.custom_field',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A custom field definition for incidents',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the custom field'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the custom field',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the custom field',
                    },
                    'field_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of field: single_select, multi_select, text, link, numeric',
                    },
                    'catalog_type_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the catalog type associated with this custom field',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the custom field was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the custom field was last updated',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'custom_fields',
                'x-airbyte-stream-name': 'custom_fields',
                'x-airbyte-ai-hints': {
                    'summary': 'Custom fields for capturing additional incident metadata',
                    'when_to_use': 'Questions about custom incident data fields',
                    'trigger_phrases': ['custom field', 'incident field'],
                    'freshness': 'static',
                    'example_questions': ['What custom fields are on incidents?'],
                    'search_strategy': 'List all custom fields',
                },
            },
            ai_hints={
                'summary': 'Custom fields for capturing additional incident metadata',
                'when_to_use': 'Questions about custom incident data fields',
                'trigger_phrases': ['custom field', 'incident field'],
                'freshness': 'static',
                'example_questions': ['What custom fields are on incidents?'],
                'search_strategy': 'List all custom fields',
            },
        ),
        EntityDefinition(
            name='catalog_types',
            stream_name='catalog_types',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/catalog_types',
                    action=Action.LIST,
                    description='List all catalog types for the organisation.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'catalog_types': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A catalog type defining a category of catalog entries',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the catalog type'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the catalog type',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the catalog type',
                                        },
                                        'type_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Programmatic type name',
                                        },
                                        'color': {
                                            'type': ['null', 'string'],
                                            'description': 'Display color',
                                        },
                                        'icon': {
                                            'type': ['null', 'string'],
                                            'description': 'Display icon',
                                        },
                                        'ranked': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether entries are ranked',
                                        },
                                        'is_editable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether entries can be edited',
                                        },
                                        'registry_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Registry type if synced from an integration',
                                        },
                                        'semantic_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Semantic type for special behavior',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the catalog type was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the catalog type was last updated',
                                        },
                                        'last_synced_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the catalog type was last synced from an integration',
                                        },
                                        'annotations': {
                                            'type': ['null', 'object'],
                                            'description': 'Annotations metadata',
                                        },
                                        'categories': {
                                            'type': ['null', 'array'],
                                            'description': 'Categories this type belongs to',
                                            'items': {'type': 'string'},
                                        },
                                        'required_integrations': {
                                            'type': ['null', 'array'],
                                            'description': 'Integrations required for this type',
                                            'items': {'type': 'string'},
                                        },
                                        'schema': {
                                            'type': ['null', 'object'],
                                            'description': 'Schema definition for the catalog type',
                                            'properties': {
                                                'version': {
                                                    'type': ['null', 'number'],
                                                },
                                                'attributes': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'array': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'mode': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'catalog_types',
                                    'x-airbyte-stream-name': 'catalog_types',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Catalog types defining service, team, and infrastructure entities',
                                        'when_to_use': 'Questions about the service catalog or entity types',
                                        'trigger_phrases': ['catalog type', 'service catalog', 'entity type'],
                                        'freshness': 'static',
                                        'example_questions': ['What catalog types are defined?'],
                                        'search_strategy': 'List all catalog types',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.catalog_types',
                    no_pagination='incident.io catalog types endpoint returns the full bounded collection; the API does not expose pagination on this endpoint.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/catalog_types/{id}',
                    action=Action.GET,
                    description='Show a single catalog type by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'catalog_type': {
                                'type': 'object',
                                'description': 'A catalog type defining a category of catalog entries',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the catalog type'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the catalog type',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the catalog type',
                                    },
                                    'type_name': {
                                        'type': ['null', 'string'],
                                        'description': 'Programmatic type name',
                                    },
                                    'color': {
                                        'type': ['null', 'string'],
                                        'description': 'Display color',
                                    },
                                    'icon': {
                                        'type': ['null', 'string'],
                                        'description': 'Display icon',
                                    },
                                    'ranked': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether entries are ranked',
                                    },
                                    'is_editable': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether entries can be edited',
                                    },
                                    'registry_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Registry type if synced from an integration',
                                    },
                                    'semantic_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Semantic type for special behavior',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the catalog type was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the catalog type was last updated',
                                    },
                                    'last_synced_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the catalog type was last synced from an integration',
                                    },
                                    'annotations': {
                                        'type': ['null', 'object'],
                                        'description': 'Annotations metadata',
                                    },
                                    'categories': {
                                        'type': ['null', 'array'],
                                        'description': 'Categories this type belongs to',
                                        'items': {'type': 'string'},
                                    },
                                    'required_integrations': {
                                        'type': ['null', 'array'],
                                        'description': 'Integrations required for this type',
                                        'items': {'type': 'string'},
                                    },
                                    'schema': {
                                        'type': ['null', 'object'],
                                        'description': 'Schema definition for the catalog type',
                                        'properties': {
                                            'version': {
                                                'type': ['null', 'number'],
                                            },
                                            'attributes': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'array': {
                                                            'type': ['null', 'boolean'],
                                                        },
                                                        'mode': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'catalog_types',
                                'x-airbyte-stream-name': 'catalog_types',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Catalog types defining service, team, and infrastructure entities',
                                    'when_to_use': 'Questions about the service catalog or entity types',
                                    'trigger_phrases': ['catalog type', 'service catalog', 'entity type'],
                                    'freshness': 'static',
                                    'example_questions': ['What catalog types are defined?'],
                                    'search_strategy': 'List all catalog types',
                                },
                            },
                        },
                    },
                    record_extractor='$.catalog_type',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A catalog type defining a category of catalog entries',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the catalog type'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the catalog type',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the catalog type',
                    },
                    'type_name': {
                        'type': ['null', 'string'],
                        'description': 'Programmatic type name',
                    },
                    'color': {
                        'type': ['null', 'string'],
                        'description': 'Display color',
                    },
                    'icon': {
                        'type': ['null', 'string'],
                        'description': 'Display icon',
                    },
                    'ranked': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether entries are ranked',
                    },
                    'is_editable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether entries can be edited',
                    },
                    'registry_type': {
                        'type': ['null', 'string'],
                        'description': 'Registry type if synced from an integration',
                    },
                    'semantic_type': {
                        'type': ['null', 'string'],
                        'description': 'Semantic type for special behavior',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the catalog type was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the catalog type was last updated',
                    },
                    'last_synced_at': {
                        'type': ['null', 'string'],
                        'description': 'When the catalog type was last synced from an integration',
                    },
                    'annotations': {
                        'type': ['null', 'object'],
                        'description': 'Annotations metadata',
                    },
                    'categories': {
                        'type': ['null', 'array'],
                        'description': 'Categories this type belongs to',
                        'items': {'type': 'string'},
                    },
                    'required_integrations': {
                        'type': ['null', 'array'],
                        'description': 'Integrations required for this type',
                        'items': {'type': 'string'},
                    },
                    'schema': {
                        'type': ['null', 'object'],
                        'description': 'Schema definition for the catalog type',
                        'properties': {
                            'version': {
                                'type': ['null', 'number'],
                            },
                            'attributes': {
                                'type': ['null', 'array'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'array': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'mode': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'catalog_types',
                'x-airbyte-stream-name': 'catalog_types',
                'x-airbyte-ai-hints': {
                    'summary': 'Catalog types defining service, team, and infrastructure entities',
                    'when_to_use': 'Questions about the service catalog or entity types',
                    'trigger_phrases': ['catalog type', 'service catalog', 'entity type'],
                    'freshness': 'static',
                    'example_questions': ['What catalog types are defined?'],
                    'search_strategy': 'List all catalog types',
                },
            },
            ai_hints={
                'summary': 'Catalog types defining service, team, and infrastructure entities',
                'when_to_use': 'Questions about the service catalog or entity types',
                'trigger_phrases': ['catalog type', 'service catalog', 'entity type'],
                'freshness': 'static',
                'example_questions': ['What catalog types are defined?'],
                'search_strategy': 'List all catalog types',
            },
        ),
        EntityDefinition(
            name='schedules',
            stream_name='schedules',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/schedules',
                    action=Action.LIST,
                    description='List all on-call schedules with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'schedules': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'An on-call schedule',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the schedule'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the schedule',
                                        },
                                        'timezone': {
                                            'type': ['null', 'string'],
                                            'description': 'Timezone for the schedule',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the schedule was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'When the schedule was last updated',
                                        },
                                        'annotations': {
                                            'type': ['null', 'object'],
                                            'description': 'Annotations metadata',
                                        },
                                        'config': {
                                            'type': ['null', 'object'],
                                            'description': 'Schedule configuration with rotations',
                                            'properties': {
                                                'rotations': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'handover_start_at': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'handovers': {
                                                                'type': ['null', 'array'],
                                                                'items': {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'interval': {
                                                                            'type': ['null', 'number'],
                                                                        },
                                                                        'interval_type': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                            'layers': {
                                                                'type': ['null', 'array'],
                                                                'items': {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'id': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                        'name': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'team_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'IDs of teams associated with this schedule',
                                            'items': {'type': 'string'},
                                        },
                                        'holidays_public_config': {
                                            'type': ['null', 'object'],
                                            'description': 'Public holiday configuration for the schedule',
                                        },
                                        'current_shifts': {
                                            'type': ['null', 'array'],
                                            'description': 'Currently active shifts',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'rotation_id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'fingerprint': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'start_at': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'end_at': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'schedules',
                                    'x-airbyte-stream-name': 'schedules',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'On-call schedules defining rotation and coverage',
                                        'when_to_use': 'Questions about on-call schedules or rotation planning',
                                        'trigger_phrases': ['on-call schedule', 'rotation', 'coverage schedule'],
                                        'freshness': 'live',
                                        'example_questions': ['What on-call schedules are set up?', 'Who is on-call?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.schedules',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/schedules/{id}',
                    action=Action.GET,
                    description='Get a single on-call schedule by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'schedule': {
                                'type': 'object',
                                'description': 'An on-call schedule',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique identifier for the schedule'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the schedule',
                                    },
                                    'timezone': {
                                        'type': ['null', 'string'],
                                        'description': 'Timezone for the schedule',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the schedule was created',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'description': 'When the schedule was last updated',
                                    },
                                    'annotations': {
                                        'type': ['null', 'object'],
                                        'description': 'Annotations metadata',
                                    },
                                    'config': {
                                        'type': ['null', 'object'],
                                        'description': 'Schedule configuration with rotations',
                                        'properties': {
                                            'rotations': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'name': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'handover_start_at': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'handovers': {
                                                            'type': ['null', 'array'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'interval': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                    'interval_type': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'layers': {
                                                            'type': ['null', 'array'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'name': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'team_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'IDs of teams associated with this schedule',
                                        'items': {'type': 'string'},
                                    },
                                    'holidays_public_config': {
                                        'type': ['null', 'object'],
                                        'description': 'Public holiday configuration for the schedule',
                                    },
                                    'current_shifts': {
                                        'type': ['null', 'array'],
                                        'description': 'Currently active shifts',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'rotation_id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'fingerprint': {
                                                    'type': ['null', 'string'],
                                                },
                                                'start_at': {
                                                    'type': ['null', 'string'],
                                                },
                                                'end_at': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'schedules',
                                'x-airbyte-stream-name': 'schedules',
                                'x-airbyte-ai-hints': {
                                    'summary': 'On-call schedules defining rotation and coverage',
                                    'when_to_use': 'Questions about on-call schedules or rotation planning',
                                    'trigger_phrases': ['on-call schedule', 'rotation', 'coverage schedule'],
                                    'freshness': 'live',
                                    'example_questions': ['What on-call schedules are set up?', 'Who is on-call?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                        },
                    },
                    record_extractor='$.schedule',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An on-call schedule',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the schedule'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the schedule',
                    },
                    'timezone': {
                        'type': ['null', 'string'],
                        'description': 'Timezone for the schedule',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'When the schedule was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'When the schedule was last updated',
                    },
                    'annotations': {
                        'type': ['null', 'object'],
                        'description': 'Annotations metadata',
                    },
                    'config': {
                        'type': ['null', 'object'],
                        'description': 'Schedule configuration with rotations',
                        'properties': {
                            'rotations': {
                                'type': ['null', 'array'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'handover_start_at': {
                                            'type': ['null', 'string'],
                                        },
                                        'handovers': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'interval': {
                                                        'type': ['null', 'number'],
                                                    },
                                                    'interval_type': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                        'layers': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'team_ids': {
                        'type': ['null', 'array'],
                        'description': 'IDs of teams associated with this schedule',
                        'items': {'type': 'string'},
                    },
                    'holidays_public_config': {
                        'type': ['null', 'object'],
                        'description': 'Public holiday configuration for the schedule',
                    },
                    'current_shifts': {
                        'type': ['null', 'array'],
                        'description': 'Currently active shifts',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'rotation_id': {
                                    'type': ['null', 'string'],
                                },
                                'fingerprint': {
                                    'type': ['null', 'string'],
                                },
                                'start_at': {
                                    'type': ['null', 'string'],
                                },
                                'end_at': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'schedules',
                'x-airbyte-stream-name': 'schedules',
                'x-airbyte-ai-hints': {
                    'summary': 'On-call schedules defining rotation and coverage',
                    'when_to_use': 'Questions about on-call schedules or rotation planning',
                    'trigger_phrases': ['on-call schedule', 'rotation', 'coverage schedule'],
                    'freshness': 'live',
                    'example_questions': ['What on-call schedules are set up?', 'Who is on-call?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'On-call schedules defining rotation and coverage',
                'when_to_use': 'Questions about on-call schedules or rotation planning',
                'trigger_phrases': ['on-call schedule', 'rotation', 'coverage schedule'],
                'freshness': 'live',
                'example_questions': ['What on-call schedules are set up?', 'Who is on-call?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='teams',
            stream_name='teams',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v3/teams',
                    action=Action.LIST,
                    description='List all teams in the organisation with cursor-based pagination.',
                    query_params=['page_size', 'after'],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'teams': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A team in incident.io',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique ID of the team'},
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the team',
                                        },
                                        'catalog_entry': {
                                            'type': ['null', 'object'],
                                            'description': 'Associated catalog entry for enrichment',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'ID of the catalog entry',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Name of the catalog entry',
                                                },
                                            },
                                        },
                                        'members': {
                                            'type': ['null', 'array'],
                                            'description': 'Members of the team',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                        'description': 'Unique identifier of the user',
                                                    },
                                                    'name': {
                                                        'type': ['null', 'string'],
                                                        'description': 'Name of the user',
                                                    },
                                                    'email': {
                                                        'type': ['null', 'string'],
                                                        'description': 'Email address of the user',
                                                    },
                                                    'slack_user_id': {
                                                        'type': ['null', 'string'],
                                                        'description': 'Slack ID of the user',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'teams',
                                    'x-airbyte-stream-name': 'teams',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Teams in incident.io with members and catalog entry associations',
                                        'when_to_use': 'Questions about teams, team members, or team associations',
                                        'trigger_phrases': [
                                            'team',
                                            'teams',
                                            'team members',
                                            'group',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What teams exist?', 'Who are the members of each team?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'pagination_meta': {
                                'type': 'object',
                                'description': 'Cursor-based pagination metadata',
                                'properties': {
                                    'after': {
                                        'type': ['null', 'string'],
                                        'description': 'Cursor to pass as the after parameter to get the next page',
                                    },
                                    'page_size': {
                                        'type': ['null', 'integer'],
                                        'description': 'Maximum number of results per page',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.teams',
                    meta_extractor={'next_cursor': '$.pagination_meta.after'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v3/teams/{id}',
                    action=Action.GET,
                    description='Get a single team by ID.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'team': {
                                'type': 'object',
                                'description': 'A team in incident.io',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique ID of the team'},
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the team',
                                    },
                                    'catalog_entry': {
                                        'type': ['null', 'object'],
                                        'description': 'Associated catalog entry for enrichment',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                                'description': 'ID of the catalog entry',
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                                'description': 'Name of the catalog entry',
                                            },
                                        },
                                    },
                                    'members': {
                                        'type': ['null', 'array'],
                                        'description': 'Members of the team',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Unique identifier of the user',
                                                },
                                                'name': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Name of the user',
                                                },
                                                'email': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Email address of the user',
                                                },
                                                'slack_user_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Slack ID of the user',
                                                },
                                            },
                                        },
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'teams',
                                'x-airbyte-stream-name': 'teams',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Teams in incident.io with members and catalog entry associations',
                                    'when_to_use': 'Questions about teams, team members, or team associations',
                                    'trigger_phrases': [
                                        'team',
                                        'teams',
                                        'team members',
                                        'group',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What teams exist?', 'Who are the members of each team?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                        },
                    },
                    record_extractor='$.team',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A team in incident.io',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique ID of the team'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the team',
                    },
                    'catalog_entry': {
                        'type': ['null', 'object'],
                        'description': 'Associated catalog entry for enrichment',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'ID of the catalog entry',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the catalog entry',
                            },
                        },
                    },
                    'members': {
                        'type': ['null', 'array'],
                        'description': 'Members of the team',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                    'description': 'Unique identifier of the user',
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the user',
                                },
                                'email': {
                                    'type': ['null', 'string'],
                                    'description': 'Email address of the user',
                                },
                                'slack_user_id': {
                                    'type': ['null', 'string'],
                                    'description': 'Slack ID of the user',
                                },
                            },
                        },
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'teams',
                'x-airbyte-stream-name': 'teams',
                'x-airbyte-ai-hints': {
                    'summary': 'Teams in incident.io with members and catalog entry associations',
                    'when_to_use': 'Questions about teams, team members, or team associations',
                    'trigger_phrases': [
                        'team',
                        'teams',
                        'team members',
                        'group',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What teams exist?', 'Who are the members of each team?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Teams in incident.io with members and catalog entry associations',
                'when_to_use': 'Questions about teams, team members, or team associations',
                'trigger_phrases': [
                    'team',
                    'teams',
                    'team members',
                    'group',
                ],
                'freshness': 'live',
                'example_questions': ['What teams exist?', 'Who are the members of each team?'],
                'search_strategy': 'Search by name',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='incidents',
                suggested=True,
                x_airbyte_name='incidents',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the incident was created',
                    ),
                    CacheFieldConfig(
                        name='creator',
                        type=['null', 'object'],
                        description='The user who created the incident',
                        properties={
                            'user': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'email': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'role': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'slack_user_id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='custom_field_entries',
                        type=['null', 'array'],
                        description='Custom field values for the incident',
                    ),
                    CacheFieldConfig(
                        name='duration_metrics',
                        type=['null', 'array'],
                        description='Duration metrics associated with the incident',
                    ),
                    CacheFieldConfig(
                        name='has_debrief',
                        type=['null', 'boolean'],
                        description='Whether the incident has had a debrief',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the incident',
                    ),
                    CacheFieldConfig(
                        name='incident_role_assignments',
                        type=['null', 'array'],
                        description='Role assignments for the incident',
                    ),
                    CacheFieldConfig(
                        name='incident_status',
                        type=['null', 'object'],
                        description='Current status of the incident',
                        properties={
                            'category': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'created_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'rank': CacheFieldProperty(
                                type=['null', 'number'],
                            ),
                            'updated_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='incident_timestamp_values',
                        type=['null', 'array'],
                        description='Timestamp values for the incident',
                    ),
                    CacheFieldConfig(
                        name='incident_type',
                        type=['null', 'object'],
                        description='Type of the incident',
                        properties={
                            'create_in_triage': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'created_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'is_default': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'private_incidents_only': CacheFieldProperty(
                                type=['null', 'boolean'],
                            ),
                            'updated_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='mode',
                        type=['null', 'string'],
                        description='Mode of the incident: standard, retrospective, test, or tutorial',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name/title of the incident',
                    ),
                    CacheFieldConfig(
                        name='permalink',
                        type=['null', 'string'],
                        description='Link to the incident in the dashboard',
                    ),
                    CacheFieldConfig(
                        name='reference',
                        type=['null', 'string'],
                        description='Human-readable reference (e.g. INC-123)',
                    ),
                    CacheFieldConfig(
                        name='severity',
                        type=['null', 'object'],
                        description='Severity of the incident',
                        properties={
                            'created_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'rank': CacheFieldProperty(
                                type=['null', 'number'],
                            ),
                            'updated_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='slack_channel_id',
                        type=['null', 'string'],
                        description='Slack channel ID for the incident',
                    ),
                    CacheFieldConfig(
                        name='slack_channel_name',
                        type=['null', 'string'],
                        description='Slack channel name for the incident',
                    ),
                    CacheFieldConfig(
                        name='slack_team_id',
                        type=['null', 'string'],
                        description='Slack team/workspace ID',
                    ),
                    CacheFieldConfig(
                        name='summary',
                        type=['null', 'string'],
                        description='Detailed summary of the incident',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the incident was last updated',
                    ),
                    CacheFieldConfig(
                        name='visibility',
                        type=['null', 'string'],
                        description='Whether the incident is public or private',
                    ),
                    CacheFieldConfig(
                        name='workload_minutes_late',
                        type=['null', 'number'],
                        description='Minutes of workload classified as late',
                    ),
                    CacheFieldConfig(
                        name='workload_minutes_sleeping',
                        type=['null', 'number'],
                        description='Minutes of workload classified as sleeping',
                    ),
                    CacheFieldConfig(
                        name='workload_minutes_total',
                        type=['null', 'number'],
                        description='Total workload minutes',
                    ),
                    CacheFieldConfig(
                        name='workload_minutes_working',
                        type=['null', 'number'],
                        description='Minutes of workload classified as working',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='alerts',
                suggested=True,
                x_airbyte_name='alerts',
                fields=[
                    CacheFieldConfig(
                        name='alert_source_id',
                        type=['null', 'string'],
                        description='ID of the alert source that generated this alert',
                    ),
                    CacheFieldConfig(
                        name='attributes',
                        type=['null', 'array'],
                        description='Structured alert attributes',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the alert was created',
                    ),
                    CacheFieldConfig(
                        name='deduplication_key',
                        type=['null', 'string'],
                        description='Deduplication key uniquely referencing this alert',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the alert',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the alert',
                    ),
                    CacheFieldConfig(
                        name='resolved_at',
                        type=['null', 'string'],
                        description='When the alert was resolved',
                    ),
                    CacheFieldConfig(
                        name='source_url',
                        type=['null', 'string'],
                        description='Link to the alert in the upstream system',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Status of the alert: firing or resolved',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Title of the alert',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the alert was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='users',
                suggested=True,
                x_airbyte_name='users',
                fields=[
                    CacheFieldConfig(
                        name='base_role',
                        type=['null', 'object'],
                        description='Base role assigned to the user',
                        properties={
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'slug': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='custom_roles',
                        type=['null', 'array'],
                        description='Custom roles assigned to the user',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Email address of the user',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the user',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Full name of the user',
                    ),
                    CacheFieldConfig(
                        name='role',
                        type=['null', 'string'],
                        description='Deprecated role field',
                    ),
                    CacheFieldConfig(
                        name='slack_user_id',
                        type=['null', 'string'],
                        description='Slack user ID',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='incident_updates',
                suggested=True,
                x_airbyte_name='incident_updates',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the update was created',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the incident update',
                    ),
                    CacheFieldConfig(
                        name='incident_id',
                        type=['null', 'string'],
                        description='ID of the incident this update belongs to',
                    ),
                    CacheFieldConfig(
                        name='message',
                        type=['null', 'string'],
                        description='Update message content',
                    ),
                    CacheFieldConfig(
                        name='new_incident_status',
                        type=['null', 'object'],
                        description='New incident status set by this update',
                        properties={
                            'category': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'created_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'rank': CacheFieldProperty(
                                type=['null', 'number'],
                            ),
                            'updated_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='new_severity',
                        type=['null', 'object'],
                        description='New severity set by this update',
                        properties={
                            'created_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'description': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'rank': CacheFieldProperty(
                                type=['null', 'number'],
                            ),
                            'updated_at': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='updater',
                        type=['null', 'object'],
                        description='Who made this update',
                        properties={
                            'user': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'email': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'role': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'slack_user_id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='incident_roles',
                suggested=True,
                x_airbyte_name='incident_roles',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the role was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the role',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the incident role',
                    ),
                    CacheFieldConfig(
                        name='instructions',
                        type=['null', 'string'],
                        description='Instructions for the role holder',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the role',
                    ),
                    CacheFieldConfig(
                        name='required',
                        type=['null', 'boolean'],
                        description='Whether this role must be assigned',
                    ),
                    CacheFieldConfig(
                        name='role_type',
                        type=['null', 'string'],
                        description='Type of role',
                    ),
                    CacheFieldConfig(
                        name='shortform',
                        type=['null', 'string'],
                        description='Short form label for the role',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the role was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='incident_statuses',
                suggested=True,
                x_airbyte_name='incident_statuses',
                fields=[
                    CacheFieldConfig(
                        name='category',
                        type=['null', 'string'],
                        description='Category: triage, active, post-incident, closed, etc.',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the status was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the status',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the status',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the status',
                    ),
                    CacheFieldConfig(
                        name='rank',
                        type=['null', 'number'],
                        description='Rank for ordering',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the status was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='incident_timestamps',
                suggested=True,
                x_airbyte_name='incident_timestamps',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the timestamp',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the timestamp',
                    ),
                    CacheFieldConfig(
                        name='rank',
                        type=['null', 'number'],
                        description='Rank for ordering',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='severities',
                suggested=True,
                x_airbyte_name='severities',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the severity was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the severity',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the severity',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the severity',
                    ),
                    CacheFieldConfig(
                        name='rank',
                        type=['null', 'number'],
                        description='Rank for ordering',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the severity was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='custom_fields',
                suggested=True,
                x_airbyte_name='custom_fields',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the custom field was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the custom field',
                    ),
                    CacheFieldConfig(
                        name='field_type',
                        type=['null', 'string'],
                        description='Type of field',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the custom field',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the custom field',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the custom field was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='catalog_types',
                x_airbyte_name='catalog_types',
                fields=[
                    CacheFieldConfig(
                        name='annotations',
                        type=['null', 'object'],
                        description='Annotations metadata',
                    ),
                    CacheFieldConfig(
                        name='categories',
                        type=['null', 'array'],
                        description='Categories this type belongs to',
                    ),
                    CacheFieldConfig(
                        name='color',
                        type=['null', 'string'],
                        description='Display color',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the catalog type was created',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the catalog type',
                    ),
                    CacheFieldConfig(
                        name='icon',
                        type=['null', 'string'],
                        description='Display icon',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the catalog type',
                    ),
                    CacheFieldConfig(
                        name='is_editable',
                        type=['null', 'boolean'],
                        description='Whether entries can be edited',
                    ),
                    CacheFieldConfig(
                        name='last_synced_at',
                        type=['null', 'string'],
                        description='When the catalog type was last synced',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the catalog type',
                    ),
                    CacheFieldConfig(
                        name='ranked',
                        type=['null', 'boolean'],
                        description='Whether entries are ranked',
                    ),
                    CacheFieldConfig(
                        name='registry_type',
                        type=['null', 'string'],
                        description='Registry type if synced from an integration',
                    ),
                    CacheFieldConfig(
                        name='required_integrations',
                        type=['null', 'array'],
                        description='Integrations required for this type',
                    ),
                    CacheFieldConfig(
                        name='schema',
                        type=['null', 'object'],
                        description='Schema definition for the catalog type',
                        properties={
                            'attributes': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                            'version': CacheFieldProperty(
                                type=['null', 'number'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='semantic_type',
                        type=['null', 'string'],
                        description='Semantic type for special behavior',
                    ),
                    CacheFieldConfig(
                        name='type_name',
                        type=['null', 'string'],
                        description='Programmatic type name',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the catalog type was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='schedules',
                suggested=True,
                x_airbyte_name='schedules',
                fields=[
                    CacheFieldConfig(
                        name='annotations',
                        type=['null', 'object'],
                        description='Annotations metadata',
                    ),
                    CacheFieldConfig(
                        name='config',
                        type=['null', 'object'],
                        description='Schedule configuration with rotations',
                        properties={
                            'rotations': CacheFieldProperty(
                                type=['null', 'array'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the schedule was created',
                    ),
                    CacheFieldConfig(
                        name='current_shifts',
                        type=['null', 'array'],
                        description='Currently active shifts',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the schedule',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the schedule',
                    ),
                    CacheFieldConfig(
                        name='timezone',
                        type=['null', 'string'],
                        description='Timezone for the schedule',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the schedule was last updated',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='escalations',
                suggested=True,
                x_airbyte_name='escalations',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='When the escalation was created',
                    ),
                    CacheFieldConfig(
                        name='creator',
                        type=['null', 'object'],
                        description='The creator of this escalation',
                        properties={
                            'alert': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'title': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'user': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'email': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'role': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'slack_user_id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'workflow': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'id': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                    'name': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='escalation_path_id',
                        type=['null', 'string'],
                        description='ID of the escalation path used',
                    ),
                    CacheFieldConfig(
                        name='events',
                        type=['null', 'array'],
                        description='History of escalation events',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the escalation',
                    ),
                    CacheFieldConfig(
                        name='priority',
                        type=['null', 'object'],
                        description='Priority of the escalation',
                        properties={
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='related_alerts',
                        type=['null', 'array'],
                        description='Alerts related to this escalation',
                    ),
                    CacheFieldConfig(
                        name='related_incidents',
                        type=['null', 'array'],
                        description='Incidents related to this escalation',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Status: pending, triggered, acked, resolved, expired, cancelled',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Title of the escalation',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='When the escalation was last updated',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
    search_field_paths={
        'incidents': [
            'created_at',
            'creator',
            'creator.user',
            'creator.user.email',
            'creator.user.id',
            'creator.user.name',
            'creator.user.role',
            'creator.user.slack_user_id',
            'custom_field_entries',
            'custom_field_entries[]',
            'duration_metrics',
            'duration_metrics[]',
            'has_debrief',
            'id',
            'incident_role_assignments',
            'incident_role_assignments[]',
            'incident_status',
            'incident_status.category',
            'incident_status.created_at',
            'incident_status.description',
            'incident_status.id',
            'incident_status.name',
            'incident_status.rank',
            'incident_status.updated_at',
            'incident_timestamp_values',
            'incident_timestamp_values[]',
            'incident_type',
            'incident_type.create_in_triage',
            'incident_type.created_at',
            'incident_type.description',
            'incident_type.id',
            'incident_type.is_default',
            'incident_type.name',
            'incident_type.private_incidents_only',
            'incident_type.updated_at',
            'mode',
            'name',
            'permalink',
            'reference',
            'severity',
            'severity.created_at',
            'severity.description',
            'severity.id',
            'severity.name',
            'severity.rank',
            'severity.updated_at',
            'slack_channel_id',
            'slack_channel_name',
            'slack_team_id',
            'summary',
            'updated_at',
            'visibility',
            'workload_minutes_late',
            'workload_minutes_sleeping',
            'workload_minutes_total',
            'workload_minutes_working',
        ],
        'alerts': [
            'alert_source_id',
            'attributes',
            'attributes[]',
            'created_at',
            'deduplication_key',
            'description',
            'id',
            'resolved_at',
            'source_url',
            'status',
            'title',
            'updated_at',
        ],
        'users': [
            'base_role',
            'base_role.description',
            'base_role.id',
            'base_role.name',
            'base_role.slug',
            'custom_roles',
            'custom_roles[]',
            'email',
            'id',
            'name',
            'role',
            'slack_user_id',
        ],
        'incident_updates': [
            'created_at',
            'id',
            'incident_id',
            'message',
            'new_incident_status',
            'new_incident_status.category',
            'new_incident_status.created_at',
            'new_incident_status.description',
            'new_incident_status.id',
            'new_incident_status.name',
            'new_incident_status.rank',
            'new_incident_status.updated_at',
            'new_severity',
            'new_severity.created_at',
            'new_severity.description',
            'new_severity.id',
            'new_severity.name',
            'new_severity.rank',
            'new_severity.updated_at',
            'updater',
            'updater.user',
            'updater.user.email',
            'updater.user.id',
            'updater.user.name',
            'updater.user.role',
            'updater.user.slack_user_id',
        ],
        'incident_roles': [
            'created_at',
            'description',
            'id',
            'instructions',
            'name',
            'required',
            'role_type',
            'shortform',
            'updated_at',
        ],
        'incident_statuses': [
            'category',
            'created_at',
            'description',
            'id',
            'name',
            'rank',
            'updated_at',
        ],
        'incident_timestamps': ['id', 'name', 'rank'],
        'severities': [
            'created_at',
            'description',
            'id',
            'name',
            'rank',
            'updated_at',
        ],
        'custom_fields': [
            'created_at',
            'description',
            'field_type',
            'id',
            'name',
            'updated_at',
        ],
        'catalog_types': [
            'annotations',
            'categories',
            'categories[]',
            'color',
            'created_at',
            'description',
            'icon',
            'id',
            'is_editable',
            'last_synced_at',
            'name',
            'ranked',
            'registry_type',
            'required_integrations',
            'required_integrations[]',
            'schema',
            'schema.attributes',
            'schema.attributes[]',
            'schema.version',
            'semantic_type',
            'type_name',
            'updated_at',
        ],
        'schedules': [
            'annotations',
            'config',
            'config.rotations',
            'config.rotations[]',
            'created_at',
            'current_shifts',
            'current_shifts[]',
            'id',
            'name',
            'timezone',
            'updated_at',
        ],
        'escalations': [
            'created_at',
            'creator',
            'creator.alert',
            'creator.alert.id',
            'creator.alert.title',
            'creator.user',
            'creator.user.email',
            'creator.user.id',
            'creator.user.name',
            'creator.user.role',
            'creator.user.slack_user_id',
            'creator.workflow',
            'creator.workflow.id',
            'creator.workflow.name',
            'escalation_path_id',
            'events',
            'events[]',
            'id',
            'priority',
            'priority.name',
            'related_alerts',
            'related_alerts[]',
            'related_incidents',
            'related_incidents[]',
            'status',
            'title',
            'updated_at',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all incidents',
            'Show all open incidents',
            'List all alerts',
            'Show all users',
            'List all escalations',
            'Show all on-call schedules',
            'List all severities',
            'Show all incident statuses',
            'List all custom fields',
            'List all teams',
        ],
        context_store_search=[
            'Which incidents were created this week?',
            'What are the most recent high-severity incidents?',
            'Who is currently on-call?',
            'How many incidents are in triage status?',
            'What incidents were updated today?',
        ],
        search=[
            'Which incidents were created this week?',
            'What are the most recent high-severity incidents?',
            'Who is currently on-call?',
            'How many incidents are in triage status?',
            'What incidents were updated today?',
        ],
        unsupported=[
            'Create a new incident',
            "Update an incident's severity",
            'Delete an alert',
            'Assign someone to an incident role',
        ],
    ),
)