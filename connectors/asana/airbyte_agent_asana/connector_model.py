"""
Connector model for asana.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from ._vendored.connector_sdk.types import (
    Action,
    AuthConfig,
    AuthOption,
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

AsanaConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('d0243522-dccf-4978-8ba0-37ed47a0bdbf'),
    name='asana',
    version='0.1.10',
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
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth 2',
                    type='object',
                    required=['refresh_token', 'client_id', 'client_secret'],
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
                ),
            ),
            AuthOption(
                scheme_name='personalAccessToken',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AirbyteAuthConfig(
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
                ),
            ),
        ],
    ),
    entities=[
        EntityDefinition(
            name='tasks',
            actions=[Action.LIST, Action.GET],
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
                    preferred_for_check=True,
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
        ),
        EntityDefinition(
            name='projects',
            actions=[Action.LIST, Action.GET],
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
                                        'type': 'object',
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
                                },
                            },
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
            actions=[Action.LIST],
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
            },
        ),
        EntityDefinition(
            name='tags',
            actions=[Action.GET],
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
        ),
        EntityDefinition(
            name='project_sections',
            actions=[Action.LIST],
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
            },
        ),
        EntityDefinition(
            name='sections',
            actions=[Action.GET],
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
)