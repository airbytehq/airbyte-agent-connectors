"""
Connector model for asana.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from airbyte_agent_sdk.types import (
    Action,
    AuthConfig,
    AuthOption,
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

AsanaConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d0243522-dccf-4978-8ba0-37ed47a0bdbf'),
    name='asana',
    version='0.1.20',
    base_url='https://app.asana.com/api/1.0',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='oauth2',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://app.asana.com/-/oauth_token',
                    'auth_style': 'body',
                    'body_format': 'form',
                },
                user_config_spec=AuthConfigSpec(
                    title='OAuth 2',
                    type='object',
                    required=['refresh_token'],
                    properties={
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='OAuth access token for API requests',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='OAuth refresh token for automatic token renewal',
                        ),
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='Connected App Consumer Key',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='Connected App Consumer Secret',
                        ),
                    },
                    auth_mapping={
                        'access_token': '${access_token}',
                        'refresh_token': '${refresh_token}',
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                    },
                    replication_auth_key_mapping={
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                        'credentials.refresh_token': 'refresh_token',
                    },
                    replication_auth_key_constants={'credentials.option_title': 'OAuth Credentials'},
                ),
            ),
            AuthOption(
                scheme_name='personalAccessToken',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AuthConfigSpec(
                    title='Personal Access Token',
                    type='object',
                    required=['token'],
                    properties={
                        'token': AuthConfigFieldSpec(
                            title='Personal Access Token',
                            description='Your Asana Personal Access Token. Generate one at https://app.asana.com/0/my-apps',
                        ),
                    },
                    auth_mapping={'token': '${token}'},
                    replication_auth_key_mapping={'credentials.personal_access_token': 'token'},
                    replication_auth_key_constants={'credentials.option_title': 'PAT Credentials'},
                ),
            ),
        ],
    ),
    entities=[
        EntityDefinition(
            name='tasks',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tasks',
                    action=Action.LIST,
                    description='Returns a paginated list of tasks. Must include either a project OR a section OR a workspace AND assignee parameter.',
                    query_params=[
                        'limit',
                        'offset',
                        'project',
                        'workspace',
                        'section',
                        'assignee',
                        'completed_since',
                        'modified_since',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'project': {'type': 'string', 'required': False},
                        'workspace': {'type': 'string', 'required': False},
                        'section': {'type': 'string', 'required': False},
                        'assignee': {'type': 'string', 'required': False},
                        'completed_since': {'type': 'string', 'required': False},
                        'modified_since': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/tasks',
                    action=Action.CREATE,
                    description='Creates a new task. Every task is required to be created in a specific workspace,\nand this workspace cannot be changed once set. The workspace need not be set explicitly\nif you specify projects or a parent task instead.\n',
                    body_fields=['data'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new task',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['name', 'workspace'],
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the task'},
                                    'workspace': {'type': 'string', 'description': 'GID of the workspace to create the task in'},
                                    'projects': {
                                        'type': 'array',
                                        'description': 'Array of project GIDs to add the task to',
                                        'items': {'type': 'string'},
                                    },
                                    'assignee': {'type': 'string', 'description': "GID of the user to assign the task to, or 'me' for the current user"},
                                    'notes': {'type': 'string', 'description': 'Free-form textual description of the task (plain text, no formatting)'},
                                    'html_notes': {'type': 'string', 'description': 'HTML-formatted description of the task'},
                                    'due_on': {'type': 'string', 'description': 'Due date in YYYY-MM-DD format'},
                                    'due_at': {'type': 'string', 'description': 'Due date and time in ISO 8601 format (e.g., 2025-03-20T12:00:00.000Z)'},
                                    'start_on': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format'},
                                    'completed': {'type': 'boolean', 'description': 'Whether the task is completed'},
                                    'parent': {'type': 'string', 'description': 'GID of the parent task (to create a subtask)'},
                                    'tags': {
                                        'type': 'array',
                                        'description': 'Array of tag GIDs to add to the task',
                                        'items': {'type': 'string'},
                                    },
                                    'followers': {
                                        'type': 'array',
                                        'description': 'Array of user GIDs to add as followers',
                                        'items': {'type': 'string'},
                                    },
                                    'resource_subtype': {
                                        'type': 'string',
                                        'description': 'The subtype of the task: default_task, milestone, section, or approval',
                                        'enum': [
                                            'default_task',
                                            'milestone',
                                            'section',
                                            'approval',
                                        ],
                                    },
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Task response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full task object',
                                'properties': {
                                    'gid': {
                                        'type': 'string',
                                        'actual_time_minutes': {
                                            'type': ['integer', 'null'],
                                        },
                                        'assignee': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                        'assignee_status': {'type': 'string'},
                                        'assignee_section': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                        'completed': {'type': 'boolean'},
                                        'completed_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {'type': 'string'},
                                        'due_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'due_on': {
                                            'type': ['string', 'null'],
                                        },
                                        'followers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'hearted': {'type': 'boolean'},
                                        'hearts': {'type': 'array'},
                                        'liked': {'type': 'boolean'},
                                        'likes': {'type': 'array'},
                                        'memberships': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'project': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'gid': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'resource_type': {'type': 'string'},
                                                        },
                                                    },
                                                    'section': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'gid': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'resource_type': {'type': 'string'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'modified_at': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'notes': {'type': 'string'},
                                        'num_hearts': {'type': 'integer'},
                                        'num_likes': {'type': 'integer'},
                                        'parent': {
                                            'type': ['object', 'null'],
                                        },
                                        'permalink_url': {'type': 'string'},
                                        'projects': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'resource_type': {'type': 'string'},
                                        'start_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'start_on': {
                                            'type': ['string', 'null'],
                                        },
                                        'tags': {'type': 'array'},
                                        'resource_subtype': {'type': 'string'},
                                        'workspace': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/tasks/{task_gid}',
                    action=Action.GET,
                    description='Get a single task by its ID',
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Task response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full task object',
                                'properties': {
                                    'gid': {
                                        'type': 'string',
                                        'actual_time_minutes': {
                                            'type': ['integer', 'null'],
                                        },
                                        'assignee': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                        'assignee_status': {'type': 'string'},
                                        'assignee_section': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                        'completed': {'type': 'boolean'},
                                        'completed_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {'type': 'string'},
                                        'due_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'due_on': {
                                            'type': ['string', 'null'],
                                        },
                                        'followers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'hearted': {'type': 'boolean'},
                                        'hearts': {'type': 'array'},
                                        'liked': {'type': 'boolean'},
                                        'likes': {'type': 'array'},
                                        'memberships': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'project': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'gid': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'resource_type': {'type': 'string'},
                                                        },
                                                    },
                                                    'section': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'gid': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'resource_type': {'type': 'string'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'modified_at': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'notes': {'type': 'string'},
                                        'num_hearts': {'type': 'integer'},
                                        'num_likes': {'type': 'integer'},
                                        'parent': {
                                            'type': ['object', 'null'],
                                        },
                                        'permalink_url': {'type': 'string'},
                                        'projects': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'resource_type': {'type': 'string'},
                                        'start_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'start_on': {
                                            'type': ['string', 'null'],
                                        },
                                        'tags': {'type': 'array'},
                                        'resource_subtype': {'type': 'string'},
                                        'workspace': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/tasks/{task_gid}',
                    action=Action.UPDATE,
                    description='Updates an existing task. Only the fields provided in the data block will be updated;\nany unspecified fields will remain unchanged. When using this method, it is best to\nspecify only those fields you wish to change.\n',
                    body_fields=['data'],
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing task',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the task'},
                                    'assignee': {'type': 'string', 'description': "GID of the user to assign the task to, or 'me' for the current user"},
                                    'notes': {'type': 'string', 'description': 'Free-form textual description of the task (plain text, no formatting)'},
                                    'html_notes': {'type': 'string', 'description': 'HTML-formatted description of the task'},
                                    'due_on': {'type': 'string', 'description': 'Due date in YYYY-MM-DD format'},
                                    'due_at': {'type': 'string', 'description': 'Due date and time in ISO 8601 format (e.g., 2025-03-20T12:00:00.000Z)'},
                                    'start_on': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format'},
                                    'completed': {'type': 'boolean', 'description': 'Whether the task is completed'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Task response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full task object',
                                'properties': {
                                    'gid': {
                                        'type': 'string',
                                        'actual_time_minutes': {
                                            'type': ['integer', 'null'],
                                        },
                                        'assignee': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                        'assignee_status': {'type': 'string'},
                                        'assignee_section': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                        'completed': {'type': 'boolean'},
                                        'completed_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {'type': 'string'},
                                        'due_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'due_on': {
                                            'type': ['string', 'null'],
                                        },
                                        'followers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'hearted': {'type': 'boolean'},
                                        'hearts': {'type': 'array'},
                                        'liked': {'type': 'boolean'},
                                        'likes': {'type': 'array'},
                                        'memberships': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'project': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'gid': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'resource_type': {'type': 'string'},
                                                        },
                                                    },
                                                    'section': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'gid': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'resource_type': {'type': 'string'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'modified_at': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'notes': {'type': 'string'},
                                        'num_hearts': {'type': 'integer'},
                                        'num_likes': {'type': 'integer'},
                                        'parent': {
                                            'type': ['object', 'null'],
                                        },
                                        'permalink_url': {'type': 'string'},
                                        'projects': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'resource_type': {'type': 'string'},
                                        'start_at': {
                                            'type': ['string', 'null'],
                                        },
                                        'start_on': {
                                            'type': ['string', 'null'],
                                        },
                                        'tags': {'type': 'array'},
                                        'resource_subtype': {'type': 'string'},
                                        'workspace': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/tasks/{task_gid}',
                    action=Action.DELETE,
                    description='Deletes a specific, existing task. Deleted tasks go into the trash of the user\nmaking the delete request. Tasks can be recovered from the trash within 30 days;\nafterward they are completely removed from the system.\n',
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact task object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                    'name': {'type': 'string', 'description': 'Task name'},
                    'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                    'created_by': {
                        'type': 'object',
                        'description': 'User who created the task',
                        'properties': {
                            'gid': {'type': 'string'},
                            'resource_type': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'tasks',
            },
        ),
        EntityDefinition(
            name='project_tasks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_gid}/tasks',
                    action=Action.LIST,
                    description='Returns all tasks in a project',
                    query_params=['limit', 'offset', 'completed_since'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'completed_since': {'type': 'string', 'required': False},
                    },
                    path_params=['project_gid'],
                    path_params_schema={
                        'project_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='project_tasks',
                    target_entity='projects',
                    foreign_key='project_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='workspace_task_search',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces/{workspace_gid}/tasks/search',
                    action=Action.LIST,
                    description='Returns tasks that match the specified search criteria. This endpoint requires a premium Asana account.\n\nIMPORTANT: At least one search filter parameter must be provided. Valid filter parameters include: text, completed, assignee.any, projects.any, sections.any, teams.any, followers.any, created_at.after, created_at.before, modified_at.after, modified_at.before, due_on.after, due_on.before, and resource_subtype. The sort_by and sort_ascending parameters are for ordering results and do not count as search filters.\n',
                    query_params=[
                        'limit',
                        'offset',
                        'text',
                        'completed',
                        'assignee.any',
                        'projects.any',
                        'sections.any',
                        'teams.any',
                        'followers.any',
                        'created_at.after',
                        'created_at.before',
                        'modified_at.after',
                        'modified_at.before',
                        'due_on.after',
                        'due_on.before',
                        'resource_subtype',
                        'sort_by',
                        'sort_ascending',
                    ],
                    query_params_schema={
                        'limit': {'type': 'integer', 'required': False},
                        'offset': {'type': 'string', 'required': False},
                        'text': {'type': 'string', 'required': False},
                        'completed': {'type': 'boolean', 'required': False},
                        'assignee.any': {'type': 'string', 'required': False},
                        'projects.any': {'type': 'string', 'required': False},
                        'sections.any': {'type': 'string', 'required': False},
                        'teams.any': {'type': 'string', 'required': False},
                        'followers.any': {'type': 'string', 'required': False},
                        'created_at.after': {'type': 'string', 'required': False},
                        'created_at.before': {'type': 'string', 'required': False},
                        'modified_at.after': {'type': 'string', 'required': False},
                        'modified_at.before': {'type': 'string', 'required': False},
                        'due_on.after': {'type': 'string', 'required': False},
                        'due_on.before': {'type': 'string', 'required': False},
                        'resource_subtype': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_ascending': {'type': 'boolean', 'required': False},
                    },
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='workspace_task_search',
                    target_entity='workspaces',
                    foreign_key='workspace_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='projects',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects',
                    action=Action.LIST,
                    description='Returns a paginated list of projects',
                    query_params=[
                        'limit',
                        'offset',
                        'workspace',
                        'team',
                        'archived',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'workspace': {'type': 'string', 'required': False},
                        'team': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of projects containing compact project objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact project object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (project)'},
                                        'name': {'type': 'string', 'description': 'Project name'},
                                    },
                                    'x-airbyte-entity-name': 'projects',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/projects',
                    action=Action.CREATE,
                    description='Create a new project in a workspace or team. Every project is required to be\ncreated in a specific workspace or organization, and this cannot be changed once set.\n',
                    body_fields=['data'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new project',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['name', 'workspace'],
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the project'},
                                    'workspace': {'type': 'string', 'description': 'GID of the workspace to create the project in'},
                                    'team': {'type': 'string', 'description': 'GID of the team to share the project with (required for organizations)'},
                                    'notes': {'type': 'string', 'description': 'Free-form textual description of the project (plain text)'},
                                    'html_notes': {'type': 'string', 'description': 'HTML-formatted description of the project'},
                                    'color': {'type': 'string', 'description': 'Color of the project (e.g., dark-pink, dark-green, dark-blue, dark-red, dark-teal, dark-brown, dark-orange, dark-purple, dark-warm-gray, light-pink, light-green, light-blue, light-red, light-teal, light-brown, light-orange, light-purple, light-warm-gray, none)'},
                                    'default_view': {
                                        'type': 'string',
                                        'description': 'The default view of the project (list, board, calendar, timeline)',
                                        'enum': [
                                            'list',
                                            'board',
                                            'calendar',
                                            'timeline',
                                        ],
                                    },
                                    'due_on': {'type': 'string', 'description': 'Due date in YYYY-MM-DD format'},
                                    'start_on': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format'},
                                    'privacy_setting': {
                                        'type': 'string',
                                        'description': 'Privacy setting: public_to_workspace or private',
                                        'enum': ['public_to_workspace', 'private'],
                                    },
                                    'archived': {'type': 'boolean', 'description': 'Whether the project is archived'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Project response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full project object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'archived': {'type': 'boolean'},
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                    'completed': {'type': 'boolean'},
                                    'completed_at': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {'type': 'string'},
                                    'current_status': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'author': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                            'color': {'type': 'string'},
                                            'created_at': {'type': 'string'},
                                            'created_by': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                            'modified_at': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'text': {'type': 'string'},
                                            'title': {'type': 'string'},
                                        },
                                    },
                                    'current_status_update': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'resource_subtype': {'type': 'string'},
                                            'title': {'type': 'string'},
                                        },
                                    },
                                    'custom_fields': {'type': 'array'},
                                    'default_access_level': {'type': 'string'},
                                    'default_view': {'type': 'string'},
                                    'due_on': {
                                        'type': ['string', 'null'],
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                    },
                                    'followers': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'members': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'minimum_access_level_for_customization': {'type': 'string'},
                                    'minimum_access_level_for_sharing': {'type': 'string'},
                                    'modified_at': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'notes': {'type': 'string'},
                                    'owner': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'permalink_url': {'type': 'string'},
                                    'privacy_setting': {'type': 'string'},
                                    'public': {'type': 'boolean'},
                                    'resource_type': {'type': 'string'},
                                    'start_on': {
                                        'type': ['string', 'null'],
                                    },
                                    'team': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'workspace': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'icon': {
                                        'type': ['string', 'null'],
                                    },
                                    'completed_by': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_gid}',
                    action=Action.GET,
                    description='Get a single project by its ID',
                    path_params=['project_gid'],
                    path_params_schema={
                        'project_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Project response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full project object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'archived': {'type': 'boolean'},
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                    'completed': {'type': 'boolean'},
                                    'completed_at': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {'type': 'string'},
                                    'current_status': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'author': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                            'color': {'type': 'string'},
                                            'created_at': {'type': 'string'},
                                            'created_by': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                            'modified_at': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'text': {'type': 'string'},
                                            'title': {'type': 'string'},
                                        },
                                    },
                                    'current_status_update': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'resource_subtype': {'type': 'string'},
                                            'title': {'type': 'string'},
                                        },
                                    },
                                    'custom_fields': {'type': 'array'},
                                    'default_access_level': {'type': 'string'},
                                    'default_view': {'type': 'string'},
                                    'due_on': {
                                        'type': ['string', 'null'],
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                    },
                                    'followers': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'members': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'minimum_access_level_for_customization': {'type': 'string'},
                                    'minimum_access_level_for_sharing': {'type': 'string'},
                                    'modified_at': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'notes': {'type': 'string'},
                                    'owner': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'permalink_url': {'type': 'string'},
                                    'privacy_setting': {'type': 'string'},
                                    'public': {'type': 'boolean'},
                                    'resource_type': {'type': 'string'},
                                    'start_on': {
                                        'type': ['string', 'null'],
                                    },
                                    'team': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'workspace': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'icon': {
                                        'type': ['string', 'null'],
                                    },
                                    'completed_by': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/projects/{project_gid}',
                    action=Action.UPDATE,
                    description='Updates an existing project. Only the fields provided in the data block will be updated;\nany unspecified fields will remain unchanged. When using this method, it is best to\nspecify only those fields you wish to change.\n',
                    body_fields=['data'],
                    path_params=['project_gid'],
                    path_params_schema={
                        'project_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing project',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the project'},
                                    'notes': {'type': 'string', 'description': 'Free-form textual description of the project (plain text)'},
                                    'html_notes': {'type': 'string', 'description': 'HTML-formatted description of the project'},
                                    'color': {'type': 'string', 'description': 'Color of the project'},
                                    'default_view': {
                                        'type': 'string',
                                        'description': 'The default view of the project (list, board, calendar, timeline)',
                                        'enum': [
                                            'list',
                                            'board',
                                            'calendar',
                                            'timeline',
                                        ],
                                    },
                                    'due_on': {'type': 'string', 'description': 'Due date in YYYY-MM-DD format'},
                                    'start_on': {'type': 'string', 'description': 'Start date in YYYY-MM-DD format'},
                                    'archived': {'type': 'boolean', 'description': 'Whether the project is archived'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Project response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full project object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'archived': {'type': 'boolean'},
                                    'color': {
                                        'type': ['string', 'null'],
                                    },
                                    'completed': {'type': 'boolean'},
                                    'completed_at': {
                                        'type': ['string', 'null'],
                                    },
                                    'created_at': {'type': 'string'},
                                    'current_status': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'author': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                            'color': {'type': 'string'},
                                            'created_at': {'type': 'string'},
                                            'created_by': {
                                                'type': 'object',
                                                'properties': {
                                                    'gid': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'resource_type': {'type': 'string'},
                                                },
                                            },
                                            'modified_at': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'text': {'type': 'string'},
                                            'title': {'type': 'string'},
                                        },
                                    },
                                    'current_status_update': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'resource_subtype': {'type': 'string'},
                                            'title': {'type': 'string'},
                                        },
                                    },
                                    'custom_fields': {'type': 'array'},
                                    'default_access_level': {'type': 'string'},
                                    'default_view': {'type': 'string'},
                                    'due_on': {
                                        'type': ['string', 'null'],
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                    },
                                    'followers': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'members': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'minimum_access_level_for_customization': {'type': 'string'},
                                    'minimum_access_level_for_sharing': {'type': 'string'},
                                    'modified_at': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'notes': {'type': 'string'},
                                    'owner': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'permalink_url': {'type': 'string'},
                                    'privacy_setting': {'type': 'string'},
                                    'public': {'type': 'boolean'},
                                    'resource_type': {'type': 'string'},
                                    'start_on': {
                                        'type': ['string', 'null'],
                                    },
                                    'team': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'workspace': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'icon': {
                                        'type': ['string', 'null'],
                                    },
                                    'completed_by': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/projects/{project_gid}',
                    action=Action.DELETE,
                    description='Deletes a specific, existing project. Returns an empty data record.\n',
                    path_params=['project_gid'],
                    path_params_schema={
                        'project_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact project object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (project)'},
                    'name': {'type': 'string', 'description': 'Project name'},
                },
                'x-airbyte-entity-name': 'projects',
            },
        ),
        EntityDefinition(
            name='task_projects',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tasks/{task_gid}/projects',
                    action=Action.LIST,
                    description='Returns all projects a task is in',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of projects containing compact project objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact project object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (project)'},
                                        'name': {'type': 'string', 'description': 'Project name'},
                                    },
                                    'x-airbyte-entity-name': 'projects',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='task_projects',
                    target_entity='tasks',
                    foreign_key='task_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='team_projects',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/teams/{team_gid}/projects',
                    action=Action.LIST,
                    description='Returns all projects for a team',
                    query_params=['limit', 'offset', 'archived'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['team_gid'],
                    path_params_schema={
                        'team_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of projects containing compact project objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact project object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (project)'},
                                        'name': {'type': 'string', 'description': 'Project name'},
                                    },
                                    'x-airbyte-entity-name': 'projects',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='team_projects',
                    target_entity='workspace_teams',
                    foreign_key='team_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='workspace_projects',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces/{workspace_gid}/projects',
                    action=Action.LIST,
                    description='Returns all projects in a workspace',
                    query_params=['limit', 'offset', 'archived'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'archived': {'type': 'boolean', 'required': False},
                    },
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of projects containing compact project objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact project object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (project)'},
                                        'name': {'type': 'string', 'description': 'Project name'},
                                    },
                                    'x-airbyte-entity-name': 'projects',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='workspace_projects',
                    target_entity='workspaces',
                    foreign_key='workspace_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='workspaces',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces',
                    action=Action.LIST,
                    description='Returns a paginated list of workspaces',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of workspaces containing compact workspace objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact workspace object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (workspace)'},
                                        'name': {'type': 'string', 'description': 'Workspace name'},
                                    },
                                    'x-airbyte-entity-name': 'workspaces',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/workspaces/{workspace_gid}',
                    action=Action.GET,
                    description='Get a single workspace by its ID',
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Workspace response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full workspace object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'email_domains': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                    },
                                    'is_organization': {'type': 'boolean'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact workspace object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (workspace)'},
                    'name': {'type': 'string', 'description': 'Workspace name'},
                },
                'x-airbyte-entity-name': 'workspaces',
            },
        ),
        EntityDefinition(
            name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/users',
                    action=Action.LIST,
                    description='Returns a paginated list of users',
                    query_params=[
                        'limit',
                        'offset',
                        'workspace',
                        'team',
                    ],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'workspace': {'type': 'string', 'required': False},
                        'team': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of users containing compact user objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact user object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (user)'},
                                        'name': {'type': 'string', 'description': 'User name'},
                                    },
                                    'x-airbyte-entity-name': 'users',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/users/{user_gid}',
                    action=Action.GET,
                    description='Get a single user by their ID',
                    path_params=['user_gid'],
                    path_params_schema={
                        'user_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'User response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full user object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'email': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'photo': {
                                        'type': ['object', 'null'],
                                    },
                                    'resource_type': {'type': 'string'},
                                    'workspaces': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
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
                'description': 'Compact user object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (user)'},
                    'name': {'type': 'string', 'description': 'User name'},
                },
                'x-airbyte-entity-name': 'users',
            },
        ),
        EntityDefinition(
            name='workspace_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces/{workspace_gid}/users',
                    action=Action.LIST,
                    description='Returns all users in a workspace',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of users containing compact user objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact user object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (user)'},
                                        'name': {'type': 'string', 'description': 'User name'},
                                    },
                                    'x-airbyte-entity-name': 'users',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='workspace_users',
                    target_entity='workspaces',
                    foreign_key='workspace_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='team_users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/teams/{team_gid}/users',
                    action=Action.LIST,
                    description='Returns all users in a team',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['team_gid'],
                    path_params_schema={
                        'team_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of users containing compact user objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact user object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (user)'},
                                        'name': {'type': 'string', 'description': 'User name'},
                                    },
                                    'x-airbyte-entity-name': 'users',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='team_users',
                    target_entity='workspace_teams',
                    foreign_key='team_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='teams',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/teams/{team_gid}',
                    action=Action.GET,
                    description='Get a single team by its ID',
                    path_params=['team_gid'],
                    path_params_schema={
                        'team_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Team response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full team object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'permalink_url': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact team object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (team)'},
                    'name': {'type': 'string', 'description': 'Team name'},
                },
                'x-airbyte-entity-name': 'teams',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='teams',
                    target_entity='workspace_teams',
                    foreign_key='team_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='workspace_teams',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces/{workspace_gid}/teams',
                    action=Action.LIST,
                    description='Returns all teams in a workspace',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of teams containing compact team objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact team object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (team)'},
                                        'name': {'type': 'string', 'description': 'Team name'},
                                    },
                                    'x-airbyte-entity-name': 'teams',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='workspace_teams',
                    target_entity='workspaces',
                    foreign_key='workspace_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='user_teams',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/users/{user_gid}/teams',
                    action=Action.LIST,
                    description='Returns all teams a user is a member of',
                    query_params=['organization', 'limit', 'offset'],
                    query_params_schema={
                        'organization': {'type': 'string', 'required': True},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['user_gid'],
                    path_params_schema={
                        'user_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of teams containing compact team objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact team object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (team)'},
                                        'name': {'type': 'string', 'description': 'Team name'},
                                    },
                                    'x-airbyte-entity-name': 'teams',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='user_teams',
                    target_entity='users',
                    foreign_key='user_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='user_teams',
                    target_entity='workspaces',
                    foreign_key='organization',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='attachments',
            actions=[Action.LIST, Action.GET, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/attachments',
                    action=Action.LIST,
                    description='Returns a list of attachments for an object (task, project, etc.)',
                    query_params=['parent', 'limit', 'offset'],
                    query_params_schema={
                        'parent': {'type': 'string', 'required': True},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of attachments containing compact attachment objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact attachment object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (attachment)'},
                                        'name': {'type': 'string', 'description': 'The name of the attachment'},
                                        'resource_subtype': {'type': 'string', 'description': 'The type of the attachment (e.g., external, dropbox, gdrive, asana, etc.)'},
                                    },
                                    'x-airbyte-entity-name': 'attachments',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/attachments/{attachment_gid}',
                    action=Action.GET,
                    description='Get details for a single attachment by its GID',
                    path_params=['attachment_gid'],
                    path_params_schema={
                        'attachment_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Attachment response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full attachment object',
                                'properties': {
                                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                    'resource_type': {'type': 'string', 'description': 'Resource type (attachment)'},
                                    'name': {'type': 'string', 'description': 'The name of the attachment'},
                                    'resource_subtype': {'type': 'string', 'description': 'The type of the attachment (e.g., external, dropbox, gdrive, etc.)'},
                                    'created_at': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'The time at which this attachment was created',
                                    },
                                    'download_url': {
                                        'type': ['string', 'null'],
                                        'format': 'uri',
                                        'description': 'The URL where the attachment can be downloaded. May be null if the attachment is hosted externally.',
                                    },
                                    'permanent_url': {
                                        'type': ['string', 'null'],
                                        'format': 'uri',
                                        'description': 'The permanent URL of the attachment. May be null if the attachment does not support permanent URLs.',
                                    },
                                    'host': {'type': 'string', 'description': 'The service hosting the attachment (asana, dropbox, gdrive, box, etc.)'},
                                    'parent': {
                                        'type': 'object',
                                        'description': 'The parent object this attachment is attached to',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_subtype': {'type': 'string', 'description': 'The subtype of the parent resource'},
                                        },
                                    },
                                    'view_url': {
                                        'type': ['string', 'null'],
                                        'format': 'uri',
                                        'description': 'The URL where the attachment can be viewed in a browser',
                                    },
                                    'size': {
                                        'type': ['integer', 'null'],
                                        'description': 'The size of the attachment in bytes',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/attachments/{attachment_gid}:download',
                    path_override=PathOverrideConfig(
                        path='/attachments/{attachment_gid}',
                    ),
                    action=Action.DOWNLOAD,
                    description='Downloads the file content of an attachment. This operation first retrieves the attachment\nmetadata to get the download_url, then downloads the file from that URL.\n',
                    path_params=['attachment_gid'],
                    path_params_schema={
                        'attachment_gid': {'type': 'string', 'required': True},
                    },
                    file_field='data.download_url',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact attachment object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (attachment)'},
                    'name': {'type': 'string', 'description': 'The name of the attachment'},
                    'resource_subtype': {'type': 'string', 'description': 'The type of the attachment (e.g., external, dropbox, gdrive, asana, etc.)'},
                },
                'x-airbyte-entity-name': 'attachments',
            },
        ),
        EntityDefinition(
            name='workspace_tags',
            actions=[Action.LIST, Action.CREATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces/{workspace_gid}/tags',
                    action=Action.LIST,
                    description='Returns all tags in a workspace',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tags containing compact tag objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact tag object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (tag)'},
                                        'name': {'type': 'string', 'description': 'Tag name'},
                                    },
                                    'x-airbyte-entity-name': 'tags',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/workspaces/{workspace_gid}/tags',
                    action=Action.CREATE,
                    description='Creates a new tag in a workspace or organization. Every tag is required to be\ncreated in a specific workspace or organization, and this cannot be changed once set.\nReturns the full record of the newly created tag.\n',
                    body_fields=['data'],
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new tag in a workspace',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['name'],
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the tag'},
                                    'color': {'type': 'string', 'description': 'Color of the tag. Must be one of: dark-pink, dark-green, dark-blue, dark-red, dark-teal, dark-brown, dark-orange, dark-purple, dark-warm-gray, light-pink, light-green, light-blue, light-red, light-teal, light-brown, light-orange, light-purple, light-warm-gray, none, null'},
                                    'notes': {'type': 'string', 'description': 'Free-form textual description of the tag'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Tag response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full tag object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'color': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'followers': {'type': 'array'},
                                    'notes': {'type': 'string'},
                                    'permalink_url': {'type': 'string'},
                                    'workspace': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='workspace_tags',
                    target_entity='workspaces',
                    foreign_key='workspace_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='tags',
            actions=[Action.GET, Action.UPDATE, Action.DELETE],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/tags/{tag_gid}',
                    action=Action.GET,
                    description='Get a single tag by its ID',
                    path_params=['tag_gid'],
                    path_params_schema={
                        'tag_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Tag response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full tag object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'color': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'followers': {'type': 'array'},
                                    'notes': {'type': 'string'},
                                    'permalink_url': {'type': 'string'},
                                    'workspace': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/tags/{tag_gid}',
                    action=Action.UPDATE,
                    description='Updates the properties of a tag. Only the fields provided in the data block will\nbe updated; any unspecified fields will remain unchanged. Returns the complete\nupdated tag record.\n',
                    body_fields=['data'],
                    path_params=['tag_gid'],
                    path_params_schema={
                        'tag_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing tag',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the tag'},
                                    'color': {'type': 'string', 'description': 'Color of the tag'},
                                    'notes': {'type': 'string', 'description': 'Free-form textual description of the tag'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Tag response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full tag object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'color': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'followers': {'type': 'array'},
                                    'notes': {'type': 'string'},
                                    'permalink_url': {'type': 'string'},
                                    'workspace': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/tags/{tag_gid}',
                    action=Action.DELETE,
                    description='A specific, existing tag can be deleted by making a DELETE request on the URL\nfor that tag. Returns an empty data record.\n',
                    path_params=['tag_gid'],
                    path_params_schema={
                        'tag_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact tag object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (tag)'},
                    'name': {'type': 'string', 'description': 'Tag name'},
                },
                'x-airbyte-entity-name': 'tags',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tags',
                    target_entity='workspace_tags',
                    foreign_key='tag_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='tag_tasks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tags/{tag_gid}/tasks',
                    action=Action.LIST,
                    description='Returns the compact task records for all tasks with the given tag.\nTasks can have more than one tag at a time.\n',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['tag_gid'],
                    path_params_schema={
                        'tag_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tag_tasks',
                    target_entity='workspace_tags',
                    foreign_key='tag_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='project_sections',
            actions=[Action.LIST, Action.CREATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/projects/{project_gid}/sections',
                    action=Action.LIST,
                    description='Returns all sections in a project',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['project_gid'],
                    path_params_schema={
                        'project_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of sections containing compact section objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact section object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (section)'},
                                        'name': {'type': 'string', 'description': 'Section name'},
                                    },
                                    'x-airbyte-entity-name': 'sections',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/projects/{project_gid}/sections',
                    action=Action.CREATE,
                    description='Creates a new section in a project. Returns the full record of the newly created section.\n',
                    body_fields=['data'],
                    path_params=['project_gid'],
                    path_params_schema={
                        'project_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a new section in a project',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['name'],
                                'properties': {
                                    'name': {'type': 'string', 'description': 'The name of the section (this is displayed as the column header in board view)'},
                                    'insert_before': {'type': 'string', 'description': 'GID of a section in the same project before which the new section should be inserted. Cannot be provided together with insert_after.'},
                                    'insert_after': {'type': 'string', 'description': 'GID of a section in the same project after which the new section should be inserted. Cannot be provided together with insert_before.'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Section response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full section object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'project': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='project_sections',
                    target_entity='projects',
                    foreign_key='project_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='sections',
            actions=[Action.GET, Action.UPDATE, Action.DELETE],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sections/{section_gid}',
                    action=Action.GET,
                    description='Get a single section by its ID',
                    path_params=['section_gid'],
                    path_params_schema={
                        'section_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Section response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full section object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'project': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/sections/{section_gid}',
                    action=Action.UPDATE,
                    description='A specific, existing section can be updated by making a PUT request on the URL for\nthat section. Only the fields provided in the data block will be updated; any unspecified\nfields will remain unchanged. Currently only the name field can be updated.\n',
                    body_fields=['data'],
                    path_params=['section_gid'],
                    path_params_schema={
                        'section_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating an existing section',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string', 'description': 'The new name of the section'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Section response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full section object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'created_at': {'type': 'string'},
                                    'project': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/sections/{section_gid}',
                    action=Action.DELETE,
                    description='A specific, existing section can be deleted by making a DELETE request on the URL\nfor that section. Note that sections must be empty to be deleted. The last remaining\nsection in a project cannot be deleted.\n',
                    path_params=['section_gid'],
                    path_params_schema={
                        'section_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Compact section object',
                'properties': {
                    'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                    'resource_type': {'type': 'string', 'description': 'Resource type (section)'},
                    'name': {'type': 'string', 'description': 'Section name'},
                },
                'x-airbyte-entity-name': 'sections',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='sections',
                    target_entity='project_sections',
                    foreign_key='section_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='section_tasks',
            actions=[Action.LIST, Action.CREATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/sections/{section_gid}/tasks',
                    action=Action.LIST,
                    description='Returns the compact task records for all tasks within the given section.',
                    query_params=['limit', 'offset', 'completed_since'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                        'completed_since': {'type': 'string', 'required': False},
                    },
                    path_params=['section_gid'],
                    path_params_schema={
                        'section_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/sections/{section_gid}/addTask',
                    action=Action.CREATE,
                    description='Add a task to a specific, existing section. This will remove the task from other\nsections of the project. The task will be inserted at the top of the section unless\nan insert_before or insert_after parameter is declared.\n',
                    body_fields=['data'],
                    path_params=['section_gid'],
                    path_params_schema={
                        'section_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for adding a task to a section',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['task'],
                                'properties': {
                                    'task': {'type': 'string', 'description': 'The GID of the task to add to this section'},
                                    'insert_before': {'type': 'string', 'description': 'GID of a task in this section before which the added task should be inserted. Cannot be provided together with insert_after.'},
                                    'insert_after': {'type': 'string', 'description': 'GID of a task in this section after which the added task should be inserted. Cannot be provided together with insert_before.'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='section_tasks',
                    target_entity='project_sections',
                    foreign_key='section_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='task_subtasks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tasks/{task_gid}/subtasks',
                    action=Action.LIST,
                    description='Returns all subtasks of a task',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='task_subtasks',
                    target_entity='tasks',
                    foreign_key='task_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='task_dependencies',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tasks/{task_gid}/dependencies',
                    action=Action.LIST,
                    description='Returns all tasks that this task depends on',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='task_dependencies',
                    target_entity='tasks',
                    foreign_key='task_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='task_dependents',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tasks/{task_gid}/dependents',
                    action=Action.LIST,
                    description='Returns all tasks that depend on this task',
                    query_params=['limit', 'offset'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'offset': {'type': 'string', 'required': False},
                    },
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks containing compact task objects',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Compact task object',
                                    'properties': {
                                        'gid': {'type': 'string', 'description': 'Globally unique identifier'},
                                        'resource_type': {'type': 'string', 'description': 'Resource type (task)'},
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'resource_subtype': {'type': 'string', 'description': 'Task subtype'},
                                        'created_by': {
                                            'type': 'object',
                                            'description': 'User who created the task',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'next_page': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'offset': {'type': 'string'},
                                    'path': {'type': 'string'},
                                    'uri': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_page': '$.next_page'},
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='task_dependents',
                    target_entity='tasks',
                    foreign_key='task_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='task_stories',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/tasks/{task_gid}/stories',
                    action=Action.CREATE,
                    description='Adds a comment to a task. The comment will be authored by the currently\nauthenticated user, and timestamped when the server receives the request.\n',
                    body_fields=['data'],
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a comment (story) on a task',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['text'],
                                'properties': {
                                    'text': {'type': 'string', 'description': 'The plain text body of the comment'},
                                    'html_text': {'type': 'string', 'description': 'HTML-formatted body of the comment'},
                                    'is_pinned': {'type': 'boolean', 'description': 'Whether the story should be pinned on the resource'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Story response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'A story represents an activity associated with an object in Asana',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'resource_type': {'type': 'string'},
                                    'resource_subtype': {'type': 'string'},
                                    'text': {'type': 'string'},
                                    'html_text': {'type': 'string'},
                                    'is_pinned': {'type': 'boolean'},
                                    'created_at': {'type': 'string'},
                                    'created_by': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'target': {
                                        'type': 'object',
                                        'properties': {
                                            'gid': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'resource_type': {'type': 'string'},
                                        },
                                    },
                                    'type': {'type': 'string'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='task_stories',
                    target_entity='tasks',
                    foreign_key='task_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='task_tags',
            actions=[Action.CREATE, Action.DELETE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/tasks/{task_gid}/addTag',
                    action=Action.CREATE,
                    description='Adds a tag to a task. Returns an empty data block.\n',
                    body_fields=['data'],
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for adding a tag to a task',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['tag'],
                                'properties': {
                                    'tag': {'type': 'string', 'description': 'The GID of the tag to add to the task'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.DELETE: EndpointDefinition(
                    method='POST',
                    path='/tasks/{task_gid}/removeTag',
                    action=Action.DELETE,
                    description='Removes a tag from a task. Returns an empty data block.\n',
                    body_fields=['data'],
                    path_params=['task_gid'],
                    path_params_schema={
                        'task_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for removing a tag from a task',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['tag'],
                                'properties': {
                                    'tag': {'type': 'string', 'description': 'The GID of the tag to remove from the task'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Empty response returned by delete operations',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='task_tags',
                    target_entity='tasks',
                    foreign_key='task_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='workspace_memberships',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/workspaces/{workspace_gid}/addUser',
                    action=Action.CREATE,
                    description='Add a user to a workspace or organization. The user can be referenced by their\nglobally unique user ID or their email address. Returns the full user record\nfor the invited user.\n',
                    body_fields=['data'],
                    path_params=['workspace_gid'],
                    path_params_schema={
                        'workspace_gid': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for adding a user to a workspace or organization',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'required': ['user'],
                                'properties': {
                                    'user': {'type': 'string', 'description': 'A user GID or email address to add to the workspace'},
                                },
                            },
                        },
                        'required': ['data'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'User response wrapper',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'description': 'Full user object',
                                'properties': {
                                    'gid': {'type': 'string'},
                                    'email': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'photo': {
                                        'type': ['object', 'null'],
                                    },
                                    'resource_type': {'type': 'string'},
                                    'workspaces': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'gid': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'resource_type': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='workspace_memberships',
                    target_entity='workspaces',
                    foreign_key='workspace_gid',
                    target_key='gid',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    search_field_paths={
        'attachments': [
            'connected_to_app',
            'created_at',
            'download_url',
            'gid',
            'host',
            'name',
            'parent',
            'parent.created_by',
            'parent.gid',
            'parent.name',
            'parent.resource_subtype',
            'parent.resource_type',
            'permanent_url',
            'resource_subtype',
            'resource_type',
            'size',
            'view_url',
        ],
        'attachments_compact': [
            'gid',
            'name',
            'resource_subtype',
            'resource_type',
        ],
        'custom_fields': [
            'created_by',
            'created_by.gid',
            'created_by.name',
            'created_by.resource_type',
            'currency_code',
            'custom_label',
            'custom_label_position',
            'description',
            'display_value',
            'enabled',
            'enum_options',
            'enum_options[]',
            'enum_value',
            'enum_value.color',
            'enum_value.enabled',
            'enum_value.gid',
            'enum_value.name',
            'enum_value.resource_type',
            'format',
            'gid',
            'has_notifications_enabled',
            'is_global_to_workspace',
            'number_value',
            'precision',
            'resource_subtype',
            'resource_type',
            'text_value',
            'type',
        ],
        'events': [
            'action',
            'change',
            'change.action',
            'change.added_value',
            'change.field',
            'change.new_value',
            'change.removed_value',
            'created_at',
            'parent',
            'parent.gid',
            'parent.name',
            'parent.resource_type',
            'resource',
            'resource.gid',
            'resource.name',
            'resource.resource_type',
            'type',
            'user',
            'user.gid',
            'user.name',
            'user.resource_type',
        ],
        'organization_exports': [
            'created_at',
            'download_url',
            'gid',
            'organization',
            'organization.gid',
            'organization.name',
            'organization.resource_type',
            'resource_type',
            'state',
        ],
        'portfolio_items': ['gid', 'name', 'resource_type'],
        'portfolios': [
            'color',
            'created_at',
            'created_by',
            'created_by.gid',
            'created_by.name',
            'created_by.resource_type',
            'current_status_update',
            'current_status_update.gid',
            'current_status_update.resource_subtype',
            'current_status_update.resource_type',
            'current_status_update.title',
            'due_on',
            'gid',
            'members',
            'members.gid',
            'members.name',
            'members.resource_type',
            'name',
            'owner',
            'owner.gid',
            'owner.name',
            'owner.resource_type',
            'permalink_url',
            'project_templates',
            'project_templates.gid',
            'project_templates.name',
            'project_templates.resource_type',
            'public',
            'resource_type',
            'start_on',
            'workspace',
            'workspace.gid',
            'workspace.name',
            'workspace.resource_type',
        ],
        'portfolios_compact': ['gid', 'name', 'resource_type'],
        'portfolios_memberships': [
            'gid',
            'portfolio',
            'portfolio.gid',
            'portfolio.name',
            'portfolio.resource_type',
            'resource_type',
            'user',
            'user.gid',
            'user.name',
            'user.resource_type',
        ],
        'projects': [
            'archived',
            'color',
            'created_at',
            'current_status',
            'current_status.author',
            'current_status.color',
            'current_status.created_at',
            'current_status.created_by',
            'current_status.gid',
            'current_status.html_text',
            'current_status.modified_at',
            'current_status.resource_type',
            'current_status.text',
            'current_status.title',
            'custom_field_settings',
            'custom_field_settings[]',
            'custom_fields',
            'custom_fields[]',
            'default_view',
            'due_date',
            'due_on',
            'followers',
            'followers[]',
            'gid',
            'html_notes',
            'icon',
            'is_template',
            'members',
            'members[]',
            'modified_at',
            'name',
            'notes',
            'owner',
            'owner.gid',
            'owner.name',
            'owner.resource_type',
            'permalink_url',
            'public',
            'resource_type',
            'start_on',
            'team',
            'team.gid',
            'team.name',
            'team.resource_type',
            'workspace',
            'workspace.gid',
            'workspace.name',
            'workspace.resource_type',
        ],
        'sections': [
            'created_at',
            'gid',
            'name',
            'project',
            'project.gid',
            'project.name',
            'project.resource_type',
            'resource_type',
        ],
        'sections_compact': ['gid', 'name', 'resource_type'],
        'stories': [
            'created_at',
            'created_by',
            'created_by.gid',
            'created_by.name',
            'created_by.resource_type',
            'gid',
            'html_text',
            'is_editable',
            'is_edited',
            'is_pinned',
            'liked',
            'likes',
            'likes[]',
            'num_likes',
            'resource_subtype',
            'resource_type',
            'sticker_name',
            'task',
            'task.gid',
            'task.name',
            'task.resource_subtype',
            'task.resource_type',
            'text',
            'type',
        ],
        'stories_compact': [
            'created_at',
            'created_by',
            'created_by.gid',
            'created_by.name',
            'created_by.resource_type',
            'gid',
            'resource_subtype',
            'resource_type',
            'target',
            'target.gid',
            'target.name',
            'target.resource_subtype',
            'target.resource_type',
            'task',
            'task.gid',
            'task.name',
            'task.resource_subtype',
            'task.resource_type',
            'text',
            'type',
        ],
        'tags': [
            'color',
            'followers',
            'followers[]',
            'gid',
            'name',
            'permalink_url',
            'resource_type',
            'workspace',
            'workspace.gid',
            'workspace.name',
            'workspace.resource_type',
        ],
        'tasks': [
            'actual_time_minutes',
            'approval_status',
            'assignee',
            'assignee.gid',
            'assignee.name',
            'assignee.resource_type',
            'completed',
            'completed_at',
            'completed_by',
            'completed_by.gid',
            'completed_by.name',
            'completed_by.resource_type',
            'created_at',
            'custom_fields',
            'custom_fields[]',
            'dependencies',
            'dependencies[]',
            'dependents',
            'dependents[]',
            'due_at',
            'due_on',
            'external',
            'external.data',
            'external.gid',
            'followers',
            'followers[]',
            'gid',
            'hearted',
            'hearts',
            'hearts[]',
            'html_notes',
            'is_rendered_as_separator',
            'liked',
            'likes',
            'likes[]',
            'memberships',
            'memberships[]',
            'modified_at',
            'name',
            'notes',
            'num_hearts',
            'num_likes',
            'num_subtasks',
            'parent',
            'parent.gid',
            'parent.name',
            'parent.resource_type',
            'permalink_url',
            'projects',
            'projects[]',
            'resource_subtype',
            'resource_type',
            'start_on',
            'tags',
            'tags[]',
            'workspace',
            'workspace.gid',
            'workspace.name',
            'workspace.resource_type',
        ],
        'team_memberships': [
            'gid',
            'is_guest',
            'resource_type',
            'team',
            'team.gid',
            'team.name',
            'team.resource_type',
            'user',
            'user.gid',
            'user.name',
            'user.resource_type',
        ],
        'teams': [
            'description',
            'gid',
            'html_description',
            'name',
            'organization',
            'organization.gid',
            'organization.name',
            'organization.resource_type',
            'permalink_url',
            'resource_type',
        ],
        'users': [
            'email',
            'gid',
            'name',
            'photo',
            'photo.image_128x128',
            'photo.image_21x21',
            'photo.image_27x27',
            'photo.image_36x36',
            'photo.image_60x60',
            'resource_type',
            'workspaces',
            'workspaces[]',
        ],
        'workspaces': [
            'email_domains',
            'email_domains[]',
            'gid',
            'is_organization',
            'name',
            'resource_type',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'What tasks are assigned to me this week?',
            'List all projects in my workspace',
            'Show me the tasks for a recent project',
            'Who are the team members in one of my teams?',
            'Show me details of my current workspace and its users',
            "Create a new task called 'Review Q3 report' in my project",
            "Mark the task 'Submit proposal' as completed",
            'Update the due date of task X to next Friday',
            "Create a new project called 'Product Launch' in my workspace",
            "Add a comment on the task saying 'Looks good, approved!'",
            'Assign the task to me and set the due date to tomorrow',
            "Delete the project 'Old Campaign'",
            'Schedule a new team meeting as a task for next Tuesday',
            'Add a new team member to my workspace by email',
            "Delete the task 'Outdated draft'",
        ],
        context_store_search=[
            "Summarize my team's workload and task completion rates",
            'Find all tasks related to {client_name} across my workspaces',
            'Analyze the most active projects in my workspace last month',
            'Compare task completion rates between my different teams',
            'Identify overdue tasks across all my projects',
            "Create a new section called 'In Review' in my project",
            "Move a task to the 'Done' section",
            "List all tasks in the 'To do' section",
            "Rename the 'Backlog' section to 'Icebox'",
            "Delete the empty 'Old Section' from the project",
            "Create a tag called 'Urgent' in my workspace",
            "Tag this task with 'Bug'",
            "Remove the 'Low Priority' tag from this task",
            "List all tasks tagged 'Release v2'",
            "Rename the tag 'WIP' to 'In Progress'",
            "Delete the tag 'Deprecated'",
        ],
        search=[
            "Summarize my team's workload and task completion rates",
            'Find all tasks related to {client_name} across my workspaces',
            'Analyze the most active projects in my workspace last month',
            'Compare task completion rates between my different teams',
            'Identify overdue tasks across all my projects',
            "Create a new section called 'In Review' in my project",
            "Move a task to the 'Done' section",
            "List all tasks in the 'To do' section",
            "Rename the 'Backlog' section to 'Icebox'",
            "Delete the empty 'Old Section' from the project",
            "Create a tag called 'Urgent' in my workspace",
            "Tag this task with 'Bug'",
            "Remove the 'Low Priority' tag from this task",
            "List all tasks tagged 'Release v2'",
            "Rename the tag 'WIP' to 'In Progress'",
            "Delete the tag 'Deprecated'",
        ],
        unsupported=['Move this task to another project'],
    ),
)