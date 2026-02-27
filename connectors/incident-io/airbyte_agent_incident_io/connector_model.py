"""
Connector model for incident-io.

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

IncidentIoConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('7926da90-399e-4f9f-9833-52d8dc3fcb29'),
    name='incident-io',
    version='1.0.1',
    base_url='https://api.incident.io',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
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
                    meta_extractor={'pagination': '$.pagination_meta'},
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
                    meta_extractor={'pagination': '$.pagination_meta'},
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
                    meta_extractor={'pagination': '$.pagination_meta'},
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
                    meta_extractor={'pagination': '$.pagination_meta'},
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
                    meta_extractor={'pagination': '$.pagination_meta'},
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
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_roles',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_statuses',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.incident_timestamps',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.severities',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.custom_fields',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.catalog_types',
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
                    meta_extractor={'pagination': '$.pagination_meta'},
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
            },
        ),
    ],
    search_field_paths={
        'incidents': [
            'call_url',
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
            'catalog_type_id',
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
            'holidays_public_config',
            'id',
            'name',
            'team_ids',
            'team_ids[]',
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
)