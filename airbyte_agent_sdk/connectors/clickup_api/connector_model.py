"""
Connector model for clickup-api.

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
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

ClickupApiConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('311a7a27-3fb5-4f7e-8265-5e4afe258b66'),
    name='clickup-api',
    version='0.1.5',
    base_url='https://api.clickup.com',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'Authorization', 'in': 'header'},
        user_config_spec=AuthConfigSpec(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your ClickUp personal API token',
                ),
            },
            auth_mapping={'api_key': '${api_key}'},
            replication_auth_key_mapping={'api_token': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='user',
            stream_name='user',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/user',
                    action=Action.GET,
                    description="View the details of the authenticated user's ClickUp account",
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'user': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'User ID'},
                                    'username': {'type': 'string', 'description': 'Username'},
                                    'email': {'type': 'string', 'description': 'Email address'},
                                    'color': {
                                        'type': ['string', 'null'],
                                        'description': 'User avatar color',
                                    },
                                    'profilePicture': {
                                        'type': ['string', 'null'],
                                        'description': 'Profile picture URL',
                                    },
                                    'initials': {
                                        'type': ['string', 'null'],
                                        'description': 'User initials',
                                    },
                                    'week_start_day': {
                                        'type': ['integer', 'null'],
                                        'description': 'Week start day preference',
                                    },
                                    'global_font_support': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Global font support enabled',
                                    },
                                    'timezone': {
                                        'type': ['string', 'null'],
                                        'description': 'User timezone',
                                    },
                                },
                                'x-airbyte-entity-name': 'user',
                                'x-airbyte-stream-name': 'user',
                                'x-airbyte-ai-hints': {
                                    'summary': 'ClickUp user profile and workspace access details',
                                    'when_to_use': 'Looking up the current user or workspace membership',
                                    'trigger_phrases': ['clickup user', 'my profile', 'who am I'],
                                    'freshness': 'live',
                                    'example_questions': ['Who is the current ClickUp user?'],
                                    'search_strategy': 'Retrieve the authenticated user profile',
                                },
                            },
                        },
                    },
                    record_extractor='$.user',
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'User ID'},
                    'username': {'type': 'string', 'description': 'Username'},
                    'email': {'type': 'string', 'description': 'Email address'},
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'User avatar color',
                    },
                    'profilePicture': {
                        'type': ['string', 'null'],
                        'description': 'Profile picture URL',
                    },
                    'initials': {
                        'type': ['string', 'null'],
                        'description': 'User initials',
                    },
                    'week_start_day': {
                        'type': ['integer', 'null'],
                        'description': 'Week start day preference',
                    },
                    'global_font_support': {
                        'type': ['boolean', 'null'],
                        'description': 'Global font support enabled',
                    },
                    'timezone': {
                        'type': ['string', 'null'],
                        'description': 'User timezone',
                    },
                },
                'x-airbyte-entity-name': 'user',
                'x-airbyte-stream-name': 'user',
                'x-airbyte-ai-hints': {
                    'summary': 'ClickUp user profile and workspace access details',
                    'when_to_use': 'Looking up the current user or workspace membership',
                    'trigger_phrases': ['clickup user', 'my profile', 'who am I'],
                    'freshness': 'live',
                    'example_questions': ['Who is the current ClickUp user?'],
                    'search_strategy': 'Retrieve the authenticated user profile',
                },
            },
            ai_hints={
                'summary': 'ClickUp user profile and workspace access details',
                'when_to_use': 'Looking up the current user or workspace membership',
                'trigger_phrases': ['clickup user', 'my profile', 'who am I'],
                'freshness': 'live',
                'example_questions': ['Who is the current ClickUp user?'],
                'search_strategy': 'Retrieve the authenticated user profile',
            },
        ),
        EntityDefinition(
            name='teams',
            stream_name='team',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team',
                    action=Action.LIST,
                    description='Get the workspaces (teams) available to the authenticated user',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'teams': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Workspace ID'},
                                        'name': {'type': 'string', 'description': 'Workspace name'},
                                        'color': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace color',
                                        },
                                        'avatar': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace avatar URL',
                                        },
                                        'members': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'user': {
                                                        'type': 'object',
                                                        'description': 'Member user details',
                                                        'properties': {
                                                            'id': {'type': 'integer', 'description': 'User ID'},
                                                            'username': {'type': 'string', 'description': 'Username'},
                                                            'email': {'type': 'string', 'description': 'Email address'},
                                                            'color': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Avatar color',
                                                            },
                                                            'profilePicture': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Profile picture URL',
                                                            },
                                                            'initials': {
                                                                'type': ['string', 'null'],
                                                                'description': 'User initials',
                                                            },
                                                            'role': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'User role ID',
                                                            },
                                                            'role_subtype': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'User role subtype',
                                                            },
                                                            'role_key': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Role key name',
                                                            },
                                                            'custom_role': {
                                                                'type': ['object', 'null'],
                                                                'description': 'Custom role details',
                                                            },
                                                            'last_active': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Last active timestamp (Unix ms)',
                                                            },
                                                            'date_joined': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Date joined (Unix ms)',
                                                            },
                                                            'date_invited': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Date invited (Unix ms)',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'description': 'List of workspace members',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'teams',
                                    'x-airbyte-stream-name': 'team',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp workspaces (called teams in the API)',
                                        'when_to_use': 'Questions about available workspaces or organizational boundaries',
                                        'trigger_phrases': ['clickup workspace', 'clickup team', 'which workspace'],
                                        'freshness': 'live',
                                        'example_questions': ['What ClickUp workspaces do I have?'],
                                        'search_strategy': 'List all available workspaces',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.teams',
                    no_pagination='ClickUp GET /api/v2/team returns all workspaces accessible to the authenticated user in a single response; no pagination cursor or offset is exposed.',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Workspace ID'},
                    'name': {'type': 'string', 'description': 'Workspace name'},
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'Workspace color',
                    },
                    'avatar': {
                        'type': ['string', 'null'],
                        'description': 'Workspace avatar URL',
                    },
                    'members': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'user': {
                                    'type': 'object',
                                    'description': 'Member user details',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'User ID'},
                                        'username': {'type': 'string', 'description': 'Username'},
                                        'email': {'type': 'string', 'description': 'Email address'},
                                        'color': {
                                            'type': ['string', 'null'],
                                            'description': 'Avatar color',
                                        },
                                        'profilePicture': {
                                            'type': ['string', 'null'],
                                            'description': 'Profile picture URL',
                                        },
                                        'initials': {
                                            'type': ['string', 'null'],
                                            'description': 'User initials',
                                        },
                                        'role': {
                                            'type': ['integer', 'null'],
                                            'description': 'User role ID',
                                        },
                                        'role_subtype': {
                                            'type': ['integer', 'null'],
                                            'description': 'User role subtype',
                                        },
                                        'role_key': {
                                            'type': ['string', 'null'],
                                            'description': 'Role key name',
                                        },
                                        'custom_role': {
                                            'type': ['object', 'null'],
                                            'description': 'Custom role details',
                                        },
                                        'last_active': {
                                            'type': ['string', 'null'],
                                            'description': 'Last active timestamp (Unix ms)',
                                        },
                                        'date_joined': {
                                            'type': ['string', 'null'],
                                            'description': 'Date joined (Unix ms)',
                                        },
                                        'date_invited': {
                                            'type': ['string', 'null'],
                                            'description': 'Date invited (Unix ms)',
                                        },
                                    },
                                },
                            },
                        },
                        'description': 'List of workspace members',
                    },
                },
                'x-airbyte-entity-name': 'teams',
                'x-airbyte-stream-name': 'team',
                'x-airbyte-ai-hints': {
                    'summary': 'ClickUp workspaces (called teams in the API)',
                    'when_to_use': 'Questions about available workspaces or organizational boundaries',
                    'trigger_phrases': ['clickup workspace', 'clickup team', 'which workspace'],
                    'freshness': 'live',
                    'example_questions': ['What ClickUp workspaces do I have?'],
                    'search_strategy': 'List all available workspaces',
                },
            },
            ai_hints={
                'summary': 'ClickUp workspaces (called teams in the API)',
                'when_to_use': 'Questions about available workspaces or organizational boundaries',
                'trigger_phrases': ['clickup workspace', 'clickup team', 'which workspace'],
                'freshness': 'live',
                'example_questions': ['What ClickUp workspaces do I have?'],
                'search_strategy': 'List all available workspaces',
            },
        ),
        EntityDefinition(
            name='spaces',
            stream_name='space',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team/{team_id}/space',
                    action=Action.LIST,
                    description='Get the spaces available in a workspace',
                    path_params=['team_id'],
                    path_params_schema={
                        'team_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'spaces': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Space ID'},
                                        'name': {'type': 'string', 'description': 'Space name'},
                                        'private': {'type': 'boolean', 'description': 'Whether the space is private'},
                                        'color': {
                                            'type': ['string', 'null'],
                                            'description': 'Space color',
                                        },
                                        'avatar': {
                                            'type': ['string', 'null'],
                                            'description': 'Space avatar URL',
                                        },
                                        'admin_can_manage': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether admins can manage',
                                        },
                                        'statuses': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Status ID'},
                                                    'status': {'type': 'string', 'description': 'Status name'},
                                                    'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                    'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                                    'color': {'type': 'string', 'description': 'Status color hex code'},
                                                },
                                            },
                                            'description': 'Space statuses',
                                        },
                                        'multiple_assignees': {'type': 'boolean', 'description': 'Multiple assignees enabled'},
                                        'features': {
                                            'type': 'object',
                                            'description': 'Feature flags for the space',
                                            'properties': {
                                                'due_dates': {
                                                    'type': 'object',
                                                    'description': 'Due dates feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether due dates are enabled'},
                                                        'start_date': {'type': 'boolean', 'description': 'Whether start dates are enabled'},
                                                        'remap_due_dates': {'type': 'boolean', 'description': 'Whether due dates are remapped'},
                                                        'remap_closed_due_date': {'type': 'boolean', 'description': 'Whether closed due dates are remapped'},
                                                    },
                                                },
                                                'sprints': {
                                                    'type': 'object',
                                                    'description': 'Sprints feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether sprints are enabled'},
                                                    },
                                                },
                                                'time_tracking': {
                                                    'type': 'object',
                                                    'description': 'Time tracking feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether time tracking is enabled'},
                                                        'harvest': {'type': 'boolean', 'description': 'Whether Harvest integration is enabled'},
                                                        'rollup': {'type': 'boolean', 'description': 'Whether time rollup is enabled'},
                                                        'default_to_billable': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Default billable setting',
                                                        },
                                                    },
                                                },
                                                'points': {
                                                    'type': 'object',
                                                    'description': 'Points feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether points are enabled'},
                                                    },
                                                },
                                                'custom_items': {
                                                    'type': 'object',
                                                    'description': 'Custom items feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether custom items are enabled'},
                                                    },
                                                },
                                                'priorities': {
                                                    'type': 'object',
                                                    'description': 'Priorities feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether priorities are enabled'},
                                                        'priorities': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'color': {'type': 'string', 'description': 'Priority color hex code'},
                                                                    'id': {'type': 'string', 'description': 'Priority ID'},
                                                                    'orderindex': {'type': 'string', 'description': 'Priority order index'},
                                                                    'priority': {'type': 'string', 'description': 'Priority name'},
                                                                },
                                                            },
                                                            'description': 'Priority levels',
                                                        },
                                                    },
                                                },
                                                'tags': {
                                                    'type': 'object',
                                                    'description': 'Tags feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether tags are enabled'},
                                                    },
                                                },
                                                'time_estimates': {
                                                    'type': 'object',
                                                    'description': 'Time estimates feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether time estimates are enabled'},
                                                        'rollup': {'type': 'boolean', 'description': 'Whether time estimate rollup is enabled'},
                                                        'per_assignee': {'type': 'boolean', 'description': 'Whether per-assignee estimates are enabled'},
                                                    },
                                                },
                                                'check_unresolved': {
                                                    'type': 'object',
                                                    'description': 'Check unresolved feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether check unresolved is enabled'},
                                                        'subtasks': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Check unresolved subtasks',
                                                        },
                                                        'checklists': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Check unresolved checklists',
                                                        },
                                                        'comments': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Check unresolved comments',
                                                        },
                                                    },
                                                },
                                                'milestones': {
                                                    'type': 'object',
                                                    'description': 'Milestones feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether milestones are enabled'},
                                                    },
                                                },
                                                'custom_fields': {
                                                    'type': 'object',
                                                    'description': 'Custom fields feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether custom fields are enabled'},
                                                    },
                                                },
                                                'remap_dependencies': {
                                                    'type': 'object',
                                                    'description': 'Remap dependencies feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether remap dependencies is enabled'},
                                                    },
                                                },
                                                'dependency_warning': {
                                                    'type': 'object',
                                                    'description': 'Dependency warning feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether dependency warnings are enabled'},
                                                    },
                                                },
                                                'status_pies': {
                                                    'type': 'object',
                                                    'description': 'Status pies feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether status pies are enabled'},
                                                    },
                                                },
                                                'multiple_assignees': {
                                                    'type': 'object',
                                                    'description': 'Multiple assignees feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether multiple assignees are enabled'},
                                                    },
                                                },
                                                'emails': {
                                                    'type': 'object',
                                                    'description': 'Emails feature settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether emails are enabled'},
                                                    },
                                                },
                                                'scheduler_enabled': {'type': 'boolean', 'description': 'Whether scheduler is enabled'},
                                                'dependency_type_enabled': {'type': 'boolean', 'description': 'Whether dependency types are enabled'},
                                                'dependency_enforcement': {
                                                    'type': 'object',
                                                    'description': 'Dependency enforcement settings',
                                                    'properties': {
                                                        'enforcement_enabled': {'type': 'boolean', 'description': 'Whether enforcement is enabled'},
                                                        'enforcement_mode': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Enforcement mode',
                                                        },
                                                    },
                                                },
                                                'reschedule_closed_dependencies': {
                                                    'type': 'object',
                                                    'description': 'Reschedule closed dependencies settings',
                                                    'properties': {
                                                        'enabled': {'type': 'boolean', 'description': 'Whether rescheduling closed dependencies is enabled'},
                                                    },
                                                },
                                            },
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the space is archived'},
                                    },
                                    'x-airbyte-entity-name': 'spaces',
                                    'x-airbyte-stream-name': 'space',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp spaces organizing projects within a workspace',
                                        'when_to_use': 'Questions about project spaces or organizational structure',
                                        'trigger_phrases': ['clickup space', 'project space'],
                                        'freshness': 'live',
                                        'example_questions': ['What spaces are in my ClickUp workspace?'],
                                        'search_strategy': 'Search by name within a workspace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.spaces',
                    no_pagination='ClickUp GET /api/v2/team/{team_id}/space returns all spaces in the workspace in a single response; no pagination cursor or offset is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/space/{space_id}',
                    action=Action.GET,
                    description='Get a single space by ID',
                    path_params=['space_id'],
                    path_params_schema={
                        'space_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Space ID'},
                            'name': {'type': 'string', 'description': 'Space name'},
                            'private': {'type': 'boolean', 'description': 'Whether the space is private'},
                            'color': {
                                'type': ['string', 'null'],
                                'description': 'Space color',
                            },
                            'avatar': {
                                'type': ['string', 'null'],
                                'description': 'Space avatar URL',
                            },
                            'admin_can_manage': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether admins can manage',
                            },
                            'statuses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Status ID'},
                                        'status': {'type': 'string', 'description': 'Status name'},
                                        'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                        'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                        'color': {'type': 'string', 'description': 'Status color hex code'},
                                    },
                                },
                                'description': 'Space statuses',
                            },
                            'multiple_assignees': {'type': 'boolean', 'description': 'Multiple assignees enabled'},
                            'features': {
                                'type': 'object',
                                'description': 'Feature flags for the space',
                                'properties': {
                                    'due_dates': {
                                        'type': 'object',
                                        'description': 'Due dates feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether due dates are enabled'},
                                            'start_date': {'type': 'boolean', 'description': 'Whether start dates are enabled'},
                                            'remap_due_dates': {'type': 'boolean', 'description': 'Whether due dates are remapped'},
                                            'remap_closed_due_date': {'type': 'boolean', 'description': 'Whether closed due dates are remapped'},
                                        },
                                    },
                                    'sprints': {
                                        'type': 'object',
                                        'description': 'Sprints feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether sprints are enabled'},
                                        },
                                    },
                                    'time_tracking': {
                                        'type': 'object',
                                        'description': 'Time tracking feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether time tracking is enabled'},
                                            'harvest': {'type': 'boolean', 'description': 'Whether Harvest integration is enabled'},
                                            'rollup': {'type': 'boolean', 'description': 'Whether time rollup is enabled'},
                                            'default_to_billable': {
                                                'type': ['integer', 'null'],
                                                'description': 'Default billable setting',
                                            },
                                        },
                                    },
                                    'points': {
                                        'type': 'object',
                                        'description': 'Points feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether points are enabled'},
                                        },
                                    },
                                    'custom_items': {
                                        'type': 'object',
                                        'description': 'Custom items feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether custom items are enabled'},
                                        },
                                    },
                                    'priorities': {
                                        'type': 'object',
                                        'description': 'Priorities feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether priorities are enabled'},
                                            'priorities': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'color': {'type': 'string', 'description': 'Priority color hex code'},
                                                        'id': {'type': 'string', 'description': 'Priority ID'},
                                                        'orderindex': {'type': 'string', 'description': 'Priority order index'},
                                                        'priority': {'type': 'string', 'description': 'Priority name'},
                                                    },
                                                },
                                                'description': 'Priority levels',
                                            },
                                        },
                                    },
                                    'tags': {
                                        'type': 'object',
                                        'description': 'Tags feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether tags are enabled'},
                                        },
                                    },
                                    'time_estimates': {
                                        'type': 'object',
                                        'description': 'Time estimates feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether time estimates are enabled'},
                                            'rollup': {'type': 'boolean', 'description': 'Whether time estimate rollup is enabled'},
                                            'per_assignee': {'type': 'boolean', 'description': 'Whether per-assignee estimates are enabled'},
                                        },
                                    },
                                    'check_unresolved': {
                                        'type': 'object',
                                        'description': 'Check unresolved feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether check unresolved is enabled'},
                                            'subtasks': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Check unresolved subtasks',
                                            },
                                            'checklists': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Check unresolved checklists',
                                            },
                                            'comments': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Check unresolved comments',
                                            },
                                        },
                                    },
                                    'milestones': {
                                        'type': 'object',
                                        'description': 'Milestones feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether milestones are enabled'},
                                        },
                                    },
                                    'custom_fields': {
                                        'type': 'object',
                                        'description': 'Custom fields feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether custom fields are enabled'},
                                        },
                                    },
                                    'remap_dependencies': {
                                        'type': 'object',
                                        'description': 'Remap dependencies feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether remap dependencies is enabled'},
                                        },
                                    },
                                    'dependency_warning': {
                                        'type': 'object',
                                        'description': 'Dependency warning feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether dependency warnings are enabled'},
                                        },
                                    },
                                    'status_pies': {
                                        'type': 'object',
                                        'description': 'Status pies feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether status pies are enabled'},
                                        },
                                    },
                                    'multiple_assignees': {
                                        'type': 'object',
                                        'description': 'Multiple assignees feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether multiple assignees are enabled'},
                                        },
                                    },
                                    'emails': {
                                        'type': 'object',
                                        'description': 'Emails feature settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether emails are enabled'},
                                        },
                                    },
                                    'scheduler_enabled': {'type': 'boolean', 'description': 'Whether scheduler is enabled'},
                                    'dependency_type_enabled': {'type': 'boolean', 'description': 'Whether dependency types are enabled'},
                                    'dependency_enforcement': {
                                        'type': 'object',
                                        'description': 'Dependency enforcement settings',
                                        'properties': {
                                            'enforcement_enabled': {'type': 'boolean', 'description': 'Whether enforcement is enabled'},
                                            'enforcement_mode': {
                                                'type': ['integer', 'null'],
                                                'description': 'Enforcement mode',
                                            },
                                        },
                                    },
                                    'reschedule_closed_dependencies': {
                                        'type': 'object',
                                        'description': 'Reschedule closed dependencies settings',
                                        'properties': {
                                            'enabled': {'type': 'boolean', 'description': 'Whether rescheduling closed dependencies is enabled'},
                                        },
                                    },
                                },
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the space is archived'},
                        },
                        'x-airbyte-entity-name': 'spaces',
                        'x-airbyte-stream-name': 'space',
                        'x-airbyte-ai-hints': {
                            'summary': 'ClickUp spaces organizing projects within a workspace',
                            'when_to_use': 'Questions about project spaces or organizational structure',
                            'trigger_phrases': ['clickup space', 'project space'],
                            'freshness': 'live',
                            'example_questions': ['What spaces are in my ClickUp workspace?'],
                            'search_strategy': 'Search by name within a workspace',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Space ID'},
                    'name': {'type': 'string', 'description': 'Space name'},
                    'private': {'type': 'boolean', 'description': 'Whether the space is private'},
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'Space color',
                    },
                    'avatar': {
                        'type': ['string', 'null'],
                        'description': 'Space avatar URL',
                    },
                    'admin_can_manage': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether admins can manage',
                    },
                    'statuses': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Status ID'},
                                'status': {'type': 'string', 'description': 'Status name'},
                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                'color': {'type': 'string', 'description': 'Status color hex code'},
                            },
                        },
                        'description': 'Space statuses',
                    },
                    'multiple_assignees': {'type': 'boolean', 'description': 'Multiple assignees enabled'},
                    'features': {
                        'type': 'object',
                        'description': 'Feature flags for the space',
                        'properties': {
                            'due_dates': {
                                'type': 'object',
                                'description': 'Due dates feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether due dates are enabled'},
                                    'start_date': {'type': 'boolean', 'description': 'Whether start dates are enabled'},
                                    'remap_due_dates': {'type': 'boolean', 'description': 'Whether due dates are remapped'},
                                    'remap_closed_due_date': {'type': 'boolean', 'description': 'Whether closed due dates are remapped'},
                                },
                            },
                            'sprints': {
                                'type': 'object',
                                'description': 'Sprints feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether sprints are enabled'},
                                },
                            },
                            'time_tracking': {
                                'type': 'object',
                                'description': 'Time tracking feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether time tracking is enabled'},
                                    'harvest': {'type': 'boolean', 'description': 'Whether Harvest integration is enabled'},
                                    'rollup': {'type': 'boolean', 'description': 'Whether time rollup is enabled'},
                                    'default_to_billable': {
                                        'type': ['integer', 'null'],
                                        'description': 'Default billable setting',
                                    },
                                },
                            },
                            'points': {
                                'type': 'object',
                                'description': 'Points feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether points are enabled'},
                                },
                            },
                            'custom_items': {
                                'type': 'object',
                                'description': 'Custom items feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether custom items are enabled'},
                                },
                            },
                            'priorities': {
                                'type': 'object',
                                'description': 'Priorities feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether priorities are enabled'},
                                    'priorities': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'color': {'type': 'string', 'description': 'Priority color hex code'},
                                                'id': {'type': 'string', 'description': 'Priority ID'},
                                                'orderindex': {'type': 'string', 'description': 'Priority order index'},
                                                'priority': {'type': 'string', 'description': 'Priority name'},
                                            },
                                        },
                                        'description': 'Priority levels',
                                    },
                                },
                            },
                            'tags': {
                                'type': 'object',
                                'description': 'Tags feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether tags are enabled'},
                                },
                            },
                            'time_estimates': {
                                'type': 'object',
                                'description': 'Time estimates feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether time estimates are enabled'},
                                    'rollup': {'type': 'boolean', 'description': 'Whether time estimate rollup is enabled'},
                                    'per_assignee': {'type': 'boolean', 'description': 'Whether per-assignee estimates are enabled'},
                                },
                            },
                            'check_unresolved': {
                                'type': 'object',
                                'description': 'Check unresolved feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether check unresolved is enabled'},
                                    'subtasks': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Check unresolved subtasks',
                                    },
                                    'checklists': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Check unresolved checklists',
                                    },
                                    'comments': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Check unresolved comments',
                                    },
                                },
                            },
                            'milestones': {
                                'type': 'object',
                                'description': 'Milestones feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether milestones are enabled'},
                                },
                            },
                            'custom_fields': {
                                'type': 'object',
                                'description': 'Custom fields feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether custom fields are enabled'},
                                },
                            },
                            'remap_dependencies': {
                                'type': 'object',
                                'description': 'Remap dependencies feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether remap dependencies is enabled'},
                                },
                            },
                            'dependency_warning': {
                                'type': 'object',
                                'description': 'Dependency warning feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether dependency warnings are enabled'},
                                },
                            },
                            'status_pies': {
                                'type': 'object',
                                'description': 'Status pies feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether status pies are enabled'},
                                },
                            },
                            'multiple_assignees': {
                                'type': 'object',
                                'description': 'Multiple assignees feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether multiple assignees are enabled'},
                                },
                            },
                            'emails': {
                                'type': 'object',
                                'description': 'Emails feature settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether emails are enabled'},
                                },
                            },
                            'scheduler_enabled': {'type': 'boolean', 'description': 'Whether scheduler is enabled'},
                            'dependency_type_enabled': {'type': 'boolean', 'description': 'Whether dependency types are enabled'},
                            'dependency_enforcement': {
                                'type': 'object',
                                'description': 'Dependency enforcement settings',
                                'properties': {
                                    'enforcement_enabled': {'type': 'boolean', 'description': 'Whether enforcement is enabled'},
                                    'enforcement_mode': {
                                        'type': ['integer', 'null'],
                                        'description': 'Enforcement mode',
                                    },
                                },
                            },
                            'reschedule_closed_dependencies': {
                                'type': 'object',
                                'description': 'Reschedule closed dependencies settings',
                                'properties': {
                                    'enabled': {'type': 'boolean', 'description': 'Whether rescheduling closed dependencies is enabled'},
                                },
                            },
                        },
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the space is archived'},
                },
                'x-airbyte-entity-name': 'spaces',
                'x-airbyte-stream-name': 'space',
                'x-airbyte-ai-hints': {
                    'summary': 'ClickUp spaces organizing projects within a workspace',
                    'when_to_use': 'Questions about project spaces or organizational structure',
                    'trigger_phrases': ['clickup space', 'project space'],
                    'freshness': 'live',
                    'example_questions': ['What spaces are in my ClickUp workspace?'],
                    'search_strategy': 'Search by name within a workspace',
                },
            },
            ai_hints={
                'summary': 'ClickUp spaces organizing projects within a workspace',
                'when_to_use': 'Questions about project spaces or organizational structure',
                'trigger_phrases': ['clickup space', 'project space'],
                'freshness': 'live',
                'example_questions': ['What spaces are in my ClickUp workspace?'],
                'search_strategy': 'Search by name within a workspace',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='spaces',
                    target_entity='teams',
                    foreign_key='team_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='folders',
            stream_name='folder',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/space/{space_id}/folder',
                    action=Action.LIST,
                    description='Get the folders in a space',
                    path_params=['space_id'],
                    path_params_schema={
                        'space_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'folders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Folder ID'},
                                        'name': {'type': 'string', 'description': 'Folder name'},
                                        'orderindex': {
                                            'type': ['integer', 'null'],
                                            'description': 'Sort order index',
                                        },
                                        'override_statuses': {'type': 'boolean', 'description': 'Whether folder overrides space statuses'},
                                        'hidden': {'type': 'boolean', 'description': 'Whether the folder is hidden'},
                                        'space': {
                                            'type': 'object',
                                            'description': 'Parent space reference',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Space ID'},
                                                'name': {'type': 'string', 'description': 'Space name'},
                                                'access': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether user has access',
                                                },
                                            },
                                        },
                                        'task_count': {
                                            'type': ['string', 'null'],
                                            'description': 'Number of tasks in the folder',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the folder is archived'},
                                        'statuses': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Status ID'},
                                                    'status': {'type': 'string', 'description': 'Status name'},
                                                    'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                    'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                                    'color': {'type': 'string', 'description': 'Status color hex code'},
                                                },
                                            },
                                            'description': 'Folder statuses',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the folder is deleted',
                                        },
                                        'lists': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'List ID'},
                                                    'name': {'type': 'string', 'description': 'List name'},
                                                    'orderindex': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Sort order index',
                                                    },
                                                    'content': {
                                                        'type': ['string', 'null'],
                                                        'description': 'List description',
                                                    },
                                                    'status': {
                                                        'type': ['object', 'null'],
                                                        'description': 'List status',
                                                    },
                                                    'priority': {
                                                        'type': ['object', 'null'],
                                                        'description': 'List priority',
                                                    },
                                                    'assignee': {
                                                        'type': ['object', 'null'],
                                                        'description': 'List assignee',
                                                    },
                                                    'task_count': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Number of tasks',
                                                    },
                                                    'due_date': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Due date (Unix ms)',
                                                    },
                                                    'start_date': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Start date (Unix ms)',
                                                    },
                                                    'space': {
                                                        'type': ['object', 'null'],
                                                        'description': 'Parent space reference',
                                                    },
                                                    'archived': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the list is archived',
                                                    },
                                                    'override_statuses': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether list overrides statuses',
                                                    },
                                                    'statuses': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'id': {'type': 'string', 'description': 'Status ID'},
                                                                'status': {'type': 'string', 'description': 'Status name'},
                                                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                                                'color': {'type': 'string', 'description': 'Status color hex code'},
                                                                'status_group': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'Status group identifier',
                                                                },
                                                            },
                                                        },
                                                        'description': 'List statuses',
                                                    },
                                                    'permission_level': {
                                                        'type': ['string', 'null'],
                                                        'description': 'User permission level',
                                                    },
                                                },
                                            },
                                            'description': 'Lists in the folder',
                                        },
                                        'permission_level': {
                                            'type': ['string', 'null'],
                                            'description': 'User permission level',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'folders',
                                    'x-airbyte-stream-name': 'folder',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Folders organizing lists within ClickUp spaces',
                                        'when_to_use': 'Questions about folder structure or project groupings',
                                        'trigger_phrases': ['clickup folder', 'project folder'],
                                        'freshness': 'live',
                                        'example_questions': ['What folders are in this space?'],
                                        'search_strategy': 'Filter by space',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.folders',
                    no_pagination='ClickUp GET /api/v2/space/{space_id}/folder returns all folders in the space in a single response; no pagination cursor or offset is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/folder/{folder_id}',
                    action=Action.GET,
                    description='Get a single folder by ID',
                    path_params=['folder_id'],
                    path_params_schema={
                        'folder_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Folder ID'},
                            'name': {'type': 'string', 'description': 'Folder name'},
                            'orderindex': {
                                'type': ['integer', 'null'],
                                'description': 'Sort order index',
                            },
                            'override_statuses': {'type': 'boolean', 'description': 'Whether folder overrides space statuses'},
                            'hidden': {'type': 'boolean', 'description': 'Whether the folder is hidden'},
                            'space': {
                                'type': 'object',
                                'description': 'Parent space reference',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Space ID'},
                                    'name': {'type': 'string', 'description': 'Space name'},
                                    'access': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether user has access',
                                    },
                                },
                            },
                            'task_count': {
                                'type': ['string', 'null'],
                                'description': 'Number of tasks in the folder',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the folder is archived'},
                            'statuses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Status ID'},
                                        'status': {'type': 'string', 'description': 'Status name'},
                                        'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                        'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                        'color': {'type': 'string', 'description': 'Status color hex code'},
                                    },
                                },
                                'description': 'Folder statuses',
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the folder is deleted',
                            },
                            'lists': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'List ID'},
                                        'name': {'type': 'string', 'description': 'List name'},
                                        'orderindex': {
                                            'type': ['integer', 'null'],
                                            'description': 'Sort order index',
                                        },
                                        'content': {
                                            'type': ['string', 'null'],
                                            'description': 'List description',
                                        },
                                        'status': {
                                            'type': ['object', 'null'],
                                            'description': 'List status',
                                        },
                                        'priority': {
                                            'type': ['object', 'null'],
                                            'description': 'List priority',
                                        },
                                        'assignee': {
                                            'type': ['object', 'null'],
                                            'description': 'List assignee',
                                        },
                                        'task_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of tasks',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Due date (Unix ms)',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Start date (Unix ms)',
                                        },
                                        'space': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent space reference',
                                        },
                                        'archived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the list is archived',
                                        },
                                        'override_statuses': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether list overrides statuses',
                                        },
                                        'statuses': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Status ID'},
                                                    'status': {'type': 'string', 'description': 'Status name'},
                                                    'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                    'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                                    'color': {'type': 'string', 'description': 'Status color hex code'},
                                                    'status_group': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Status group identifier',
                                                    },
                                                },
                                            },
                                            'description': 'List statuses',
                                        },
                                        'permission_level': {
                                            'type': ['string', 'null'],
                                            'description': 'User permission level',
                                        },
                                    },
                                },
                                'description': 'Lists in the folder',
                            },
                            'permission_level': {
                                'type': ['string', 'null'],
                                'description': 'User permission level',
                            },
                        },
                        'x-airbyte-entity-name': 'folders',
                        'x-airbyte-stream-name': 'folder',
                        'x-airbyte-ai-hints': {
                            'summary': 'Folders organizing lists within ClickUp spaces',
                            'when_to_use': 'Questions about folder structure or project groupings',
                            'trigger_phrases': ['clickup folder', 'project folder'],
                            'freshness': 'live',
                            'example_questions': ['What folders are in this space?'],
                            'search_strategy': 'Filter by space',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Folder ID'},
                    'name': {'type': 'string', 'description': 'Folder name'},
                    'orderindex': {
                        'type': ['integer', 'null'],
                        'description': 'Sort order index',
                    },
                    'override_statuses': {'type': 'boolean', 'description': 'Whether folder overrides space statuses'},
                    'hidden': {'type': 'boolean', 'description': 'Whether the folder is hidden'},
                    'space': {
                        'type': 'object',
                        'description': 'Parent space reference',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Space ID'},
                            'name': {'type': 'string', 'description': 'Space name'},
                            'access': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether user has access',
                            },
                        },
                    },
                    'task_count': {
                        'type': ['string', 'null'],
                        'description': 'Number of tasks in the folder',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the folder is archived'},
                    'statuses': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Status ID'},
                                'status': {'type': 'string', 'description': 'Status name'},
                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                'color': {'type': 'string', 'description': 'Status color hex code'},
                            },
                        },
                        'description': 'Folder statuses',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the folder is deleted',
                    },
                    'lists': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'description': 'List ID'},
                                'name': {'type': 'string', 'description': 'List name'},
                                'orderindex': {
                                    'type': ['integer', 'null'],
                                    'description': 'Sort order index',
                                },
                                'content': {
                                    'type': ['string', 'null'],
                                    'description': 'List description',
                                },
                                'status': {
                                    'type': ['object', 'null'],
                                    'description': 'List status',
                                },
                                'priority': {
                                    'type': ['object', 'null'],
                                    'description': 'List priority',
                                },
                                'assignee': {
                                    'type': ['object', 'null'],
                                    'description': 'List assignee',
                                },
                                'task_count': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of tasks',
                                },
                                'due_date': {
                                    'type': ['string', 'null'],
                                    'description': 'Due date (Unix ms)',
                                },
                                'start_date': {
                                    'type': ['string', 'null'],
                                    'description': 'Start date (Unix ms)',
                                },
                                'space': {
                                    'type': ['object', 'null'],
                                    'description': 'Parent space reference',
                                },
                                'archived': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the list is archived',
                                },
                                'override_statuses': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether list overrides statuses',
                                },
                                'statuses': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'Status ID'},
                                            'status': {'type': 'string', 'description': 'Status name'},
                                            'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                            'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                            'color': {'type': 'string', 'description': 'Status color hex code'},
                                            'status_group': {
                                                'type': ['string', 'null'],
                                                'description': 'Status group identifier',
                                            },
                                        },
                                    },
                                    'description': 'List statuses',
                                },
                                'permission_level': {
                                    'type': ['string', 'null'],
                                    'description': 'User permission level',
                                },
                            },
                        },
                        'description': 'Lists in the folder',
                    },
                    'permission_level': {
                        'type': ['string', 'null'],
                        'description': 'User permission level',
                    },
                },
                'x-airbyte-entity-name': 'folders',
                'x-airbyte-stream-name': 'folder',
                'x-airbyte-ai-hints': {
                    'summary': 'Folders organizing lists within ClickUp spaces',
                    'when_to_use': 'Questions about folder structure or project groupings',
                    'trigger_phrases': ['clickup folder', 'project folder'],
                    'freshness': 'live',
                    'example_questions': ['What folders are in this space?'],
                    'search_strategy': 'Filter by space',
                },
            },
            ai_hints={
                'summary': 'Folders organizing lists within ClickUp spaces',
                'when_to_use': 'Questions about folder structure or project groupings',
                'trigger_phrases': ['clickup folder', 'project folder'],
                'freshness': 'live',
                'example_questions': ['What folders are in this space?'],
                'search_strategy': 'Filter by space',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='folders',
                    target_entity='spaces',
                    foreign_key='space_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='lists',
            stream_name='list',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/folder/{folder_id}/list',
                    action=Action.LIST,
                    description='Get the lists in a folder',
                    path_params=['folder_id'],
                    path_params_schema={
                        'folder_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'lists': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'List ID'},
                                        'name': {'type': 'string', 'description': 'List name'},
                                        'orderindex': {
                                            'type': ['integer', 'null'],
                                            'description': 'Sort order index',
                                        },
                                        'status': {
                                            'type': ['object', 'null'],
                                            'description': 'List status',
                                        },
                                        'priority': {
                                            'type': ['object', 'null'],
                                            'description': 'List priority',
                                        },
                                        'assignee': {
                                            'type': ['object', 'null'],
                                            'description': 'List assignee',
                                        },
                                        'task_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of tasks',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Due date (Unix ms)',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Start date (Unix ms)',
                                        },
                                        'folder': {
                                            'type': 'object',
                                            'description': 'Parent folder reference',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Folder ID'},
                                                'name': {'type': 'string', 'description': 'Folder name'},
                                                'hidden': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether the folder is hidden',
                                                },
                                                'access': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether user has access',
                                                },
                                            },
                                        },
                                        'space': {
                                            'type': 'object',
                                            'description': 'Parent space reference',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Space ID'},
                                                'name': {'type': 'string', 'description': 'Space name'},
                                                'access': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether user has access',
                                                },
                                            },
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the list is archived'},
                                        'override_statuses': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether list overrides folder/space statuses',
                                        },
                                        'content': {
                                            'type': ['string', 'null'],
                                            'description': 'List description',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the list is deleted',
                                        },
                                        'inbound_address': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address for inbound task creation',
                                        },
                                        'statuses': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Status ID'},
                                                    'status': {'type': 'string', 'description': 'Status name'},
                                                    'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                    'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                                    'color': {'type': 'string', 'description': 'Status color hex code'},
                                                    'status_group': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Status group identifier',
                                                    },
                                                },
                                            },
                                            'description': 'List statuses',
                                        },
                                        'permission_level': {
                                            'type': ['string', 'null'],
                                            'description': 'User permission level',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'lists',
                                    'x-airbyte-stream-name': 'list',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp lists containing tasks',
                                        'when_to_use': 'Questions about task lists or containers for work items',
                                        'trigger_phrases': ['clickup list', 'task list'],
                                        'freshness': 'live',
                                        'example_questions': ['What lists are available?'],
                                        'search_strategy': 'Filter by space or folder',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.lists',
                    no_pagination='ClickUp GET /api/v2/folder/{folder_id}/list returns all lists in the folder in a single response; no pagination cursor or offset is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/list/{list_id}',
                    action=Action.GET,
                    description='Get a single list by ID',
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'List ID'},
                            'name': {'type': 'string', 'description': 'List name'},
                            'orderindex': {
                                'type': ['integer', 'null'],
                                'description': 'Sort order index',
                            },
                            'status': {
                                'type': ['object', 'null'],
                                'description': 'List status',
                            },
                            'priority': {
                                'type': ['object', 'null'],
                                'description': 'List priority',
                            },
                            'assignee': {
                                'type': ['object', 'null'],
                                'description': 'List assignee',
                            },
                            'task_count': {
                                'type': ['integer', 'null'],
                                'description': 'Number of tasks',
                            },
                            'due_date': {
                                'type': ['string', 'null'],
                                'description': 'Due date (Unix ms)',
                            },
                            'start_date': {
                                'type': ['string', 'null'],
                                'description': 'Start date (Unix ms)',
                            },
                            'folder': {
                                'type': 'object',
                                'description': 'Parent folder reference',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Folder ID'},
                                    'name': {'type': 'string', 'description': 'Folder name'},
                                    'hidden': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the folder is hidden',
                                    },
                                    'access': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether user has access',
                                    },
                                },
                            },
                            'space': {
                                'type': 'object',
                                'description': 'Parent space reference',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Space ID'},
                                    'name': {'type': 'string', 'description': 'Space name'},
                                    'access': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether user has access',
                                    },
                                },
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the list is archived'},
                            'override_statuses': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether list overrides folder/space statuses',
                            },
                            'content': {
                                'type': ['string', 'null'],
                                'description': 'List description',
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the list is deleted',
                            },
                            'inbound_address': {
                                'type': ['string', 'null'],
                                'description': 'Email address for inbound task creation',
                            },
                            'statuses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Status ID'},
                                        'status': {'type': 'string', 'description': 'Status name'},
                                        'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                        'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                        'color': {'type': 'string', 'description': 'Status color hex code'},
                                        'status_group': {
                                            'type': ['string', 'null'],
                                            'description': 'Status group identifier',
                                        },
                                    },
                                },
                                'description': 'List statuses',
                            },
                            'permission_level': {
                                'type': ['string', 'null'],
                                'description': 'User permission level',
                            },
                        },
                        'x-airbyte-entity-name': 'lists',
                        'x-airbyte-stream-name': 'list',
                        'x-airbyte-ai-hints': {
                            'summary': 'ClickUp lists containing tasks',
                            'when_to_use': 'Questions about task lists or containers for work items',
                            'trigger_phrases': ['clickup list', 'task list'],
                            'freshness': 'live',
                            'example_questions': ['What lists are available?'],
                            'search_strategy': 'Filter by space or folder',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'List ID'},
                    'name': {'type': 'string', 'description': 'List name'},
                    'orderindex': {
                        'type': ['integer', 'null'],
                        'description': 'Sort order index',
                    },
                    'status': {
                        'type': ['object', 'null'],
                        'description': 'List status',
                    },
                    'priority': {
                        'type': ['object', 'null'],
                        'description': 'List priority',
                    },
                    'assignee': {
                        'type': ['object', 'null'],
                        'description': 'List assignee',
                    },
                    'task_count': {
                        'type': ['integer', 'null'],
                        'description': 'Number of tasks',
                    },
                    'due_date': {
                        'type': ['string', 'null'],
                        'description': 'Due date (Unix ms)',
                    },
                    'start_date': {
                        'type': ['string', 'null'],
                        'description': 'Start date (Unix ms)',
                    },
                    'folder': {
                        'type': 'object',
                        'description': 'Parent folder reference',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Folder ID'},
                            'name': {'type': 'string', 'description': 'Folder name'},
                            'hidden': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the folder is hidden',
                            },
                            'access': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether user has access',
                            },
                        },
                    },
                    'space': {
                        'type': 'object',
                        'description': 'Parent space reference',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Space ID'},
                            'name': {'type': 'string', 'description': 'Space name'},
                            'access': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether user has access',
                            },
                        },
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the list is archived'},
                    'override_statuses': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether list overrides folder/space statuses',
                    },
                    'content': {
                        'type': ['string', 'null'],
                        'description': 'List description',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the list is deleted',
                    },
                    'inbound_address': {
                        'type': ['string', 'null'],
                        'description': 'Email address for inbound task creation',
                    },
                    'statuses': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Status ID'},
                                'status': {'type': 'string', 'description': 'Status name'},
                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                'color': {'type': 'string', 'description': 'Status color hex code'},
                                'status_group': {
                                    'type': ['string', 'null'],
                                    'description': 'Status group identifier',
                                },
                            },
                        },
                        'description': 'List statuses',
                    },
                    'permission_level': {
                        'type': ['string', 'null'],
                        'description': 'User permission level',
                    },
                },
                'x-airbyte-entity-name': 'lists',
                'x-airbyte-stream-name': 'list',
                'x-airbyte-ai-hints': {
                    'summary': 'ClickUp lists containing tasks',
                    'when_to_use': 'Questions about task lists or containers for work items',
                    'trigger_phrases': ['clickup list', 'task list'],
                    'freshness': 'live',
                    'example_questions': ['What lists are available?'],
                    'search_strategy': 'Filter by space or folder',
                },
            },
            ai_hints={
                'summary': 'ClickUp lists containing tasks',
                'when_to_use': 'Questions about task lists or containers for work items',
                'trigger_phrases': ['clickup list', 'task list'],
                'freshness': 'live',
                'example_questions': ['What lists are available?'],
                'search_strategy': 'Filter by space or folder',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='lists',
                    target_entity='folders',
                    foreign_key='folder_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='tasks',
            stream_name='task',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/list/{list_id}/task',
                    action=Action.LIST,
                    description='Get the tasks in a list',
                    query_params=['page'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'tasks': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Task ID'},
                                        'custom_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom task ID',
                                        },
                                        'custom_item_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Custom item type identifier',
                                        },
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'text_content': {
                                            'type': ['string', 'null'],
                                            'description': 'Plain text content',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Task description',
                                        },
                                        'status': {
                                            'type': 'object',
                                            'description': 'Task status',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Status ID'},
                                                'status': {'type': 'string', 'description': 'Status name'},
                                                'color': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Status color hex code',
                                                },
                                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                            },
                                        },
                                        'orderindex': {
                                            'type': ['string', 'null'],
                                            'description': 'Sort order',
                                        },
                                        'date_created': {
                                            'type': ['string', 'null'],
                                            'description': 'Created date (Unix ms)',
                                        },
                                        'date_updated': {
                                            'type': ['string', 'null'],
                                            'description': 'Updated date (Unix ms)',
                                        },
                                        'date_closed': {
                                            'type': ['string', 'null'],
                                            'description': 'Closed date (Unix ms)',
                                        },
                                        'date_done': {
                                            'type': ['string', 'null'],
                                            'description': 'Done date (Unix ms)',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                                        'creator': {
                                            'type': 'object',
                                            'description': 'Task creator',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Creator user ID'},
                                                'username': {'type': 'string', 'description': 'Creator username'},
                                                'color': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Creator avatar color',
                                                },
                                                'email': {'type': 'string', 'description': 'Creator email'},
                                                'profilePicture': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Creator profile picture URL',
                                                },
                                            },
                                        },
                                        'assignees': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Assigned users',
                                        },
                                        'group_assignees': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Group assignees',
                                        },
                                        'watchers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Watcher user ID'},
                                                    'username': {'type': 'string', 'description': 'Watcher username'},
                                                    'color': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher avatar color',
                                                    },
                                                    'initials': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher initials',
                                                    },
                                                    'email': {'type': 'string', 'description': 'Watcher email'},
                                                    'profilePicture': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher profile picture URL',
                                                    },
                                                },
                                            },
                                            'description': 'Task watchers',
                                        },
                                        'checklists': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task checklists',
                                        },
                                        'tags': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task tags',
                                        },
                                        'parent': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent task ID',
                                        },
                                        'priority': {
                                            'type': ['object', 'null'],
                                            'description': 'Task priority',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Due date (Unix ms)',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Start date (Unix ms)',
                                        },
                                        'points': {
                                            'type': ['number', 'null'],
                                            'description': 'Sprint points',
                                        },
                                        'time_estimate': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time estimate (ms)',
                                        },
                                        'time_spent': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time spent (ms)',
                                        },
                                        'custom_fields': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Custom fields',
                                        },
                                        'dependencies': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task dependencies',
                                        },
                                        'linked_tasks': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Linked tasks',
                                        },
                                        'team_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID',
                                        },
                                        'url': {'type': 'string', 'description': 'Task URL'},
                                        'list': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent list reference',
                                        },
                                        'project': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent project reference',
                                        },
                                        'folder': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent folder reference',
                                        },
                                        'space': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent space reference',
                                        },
                                        'top_level_parent': {
                                            'type': ['string', 'null'],
                                            'description': 'Top-level parent task ID',
                                        },
                                        'locations': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task locations',
                                        },
                                        'sharing': {
                                            'type': ['object', 'null'],
                                            'description': 'Task sharing settings',
                                        },
                                        'permission_level': {
                                            'type': ['string', 'null'],
                                            'description': 'User permission level for this task',
                                        },
                                        'attachments': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task attachments',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                    'x-airbyte-stream-name': 'task',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp tasks with assignees, due dates, statuses, and priorities',
                                        'when_to_use': 'Questions about task assignments, status, or deadlines',
                                        'trigger_phrases': [
                                            'clickup task',
                                            'assigned task',
                                            'task status',
                                            'due date',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What tasks are assigned to me?', 'Show overdue tasks in ClickUp'],
                                        'search_strategy': 'Search by name or filter by assignee, status, or list',
                                    },
                                },
                            },
                            'last_page': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page of results',
                            },
                        },
                    },
                    record_extractor='$.tasks',
                    meta_extractor={'last_page': '$.last_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/task/{task_id}',
                    action=Action.GET,
                    description='Get a single task by ID',
                    query_params=['custom_task_ids', 'include_subtasks'],
                    query_params_schema={
                        'custom_task_ids': {'type': 'boolean', 'required': False},
                        'include_subtasks': {'type': 'boolean', 'required': False},
                    },
                    path_params=['task_id'],
                    path_params_schema={
                        'task_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Task ID'},
                            'custom_id': {
                                'type': ['string', 'null'],
                                'description': 'Custom task ID',
                            },
                            'custom_item_id': {
                                'type': ['integer', 'null'],
                                'description': 'Custom item type identifier',
                            },
                            'name': {'type': 'string', 'description': 'Task name'},
                            'text_content': {
                                'type': ['string', 'null'],
                                'description': 'Plain text content',
                            },
                            'description': {
                                'type': ['string', 'null'],
                                'description': 'Task description',
                            },
                            'status': {
                                'type': 'object',
                                'description': 'Task status',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Status ID'},
                                    'status': {'type': 'string', 'description': 'Status name'},
                                    'color': {
                                        'type': ['string', 'null'],
                                        'description': 'Status color hex code',
                                    },
                                    'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                    'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                },
                            },
                            'orderindex': {
                                'type': ['string', 'null'],
                                'description': 'Sort order',
                            },
                            'date_created': {
                                'type': ['string', 'null'],
                                'description': 'Created date (Unix ms)',
                            },
                            'date_updated': {
                                'type': ['string', 'null'],
                                'description': 'Updated date (Unix ms)',
                            },
                            'date_closed': {
                                'type': ['string', 'null'],
                                'description': 'Closed date (Unix ms)',
                            },
                            'date_done': {
                                'type': ['string', 'null'],
                                'description': 'Done date (Unix ms)',
                            },
                            'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                            'creator': {
                                'type': 'object',
                                'description': 'Task creator',
                                'properties': {
                                    'id': {'type': 'integer', 'description': 'Creator user ID'},
                                    'username': {'type': 'string', 'description': 'Creator username'},
                                    'color': {
                                        'type': ['string', 'null'],
                                        'description': 'Creator avatar color',
                                    },
                                    'email': {'type': 'string', 'description': 'Creator email'},
                                    'profilePicture': {
                                        'type': ['string', 'null'],
                                        'description': 'Creator profile picture URL',
                                    },
                                },
                            },
                            'assignees': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Assigned users',
                            },
                            'group_assignees': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Group assignees',
                            },
                            'watchers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Watcher user ID'},
                                        'username': {'type': 'string', 'description': 'Watcher username'},
                                        'color': {
                                            'type': ['string', 'null'],
                                            'description': 'Watcher avatar color',
                                        },
                                        'initials': {
                                            'type': ['string', 'null'],
                                            'description': 'Watcher initials',
                                        },
                                        'email': {'type': 'string', 'description': 'Watcher email'},
                                        'profilePicture': {
                                            'type': ['string', 'null'],
                                            'description': 'Watcher profile picture URL',
                                        },
                                    },
                                },
                                'description': 'Task watchers',
                            },
                            'checklists': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Task checklists',
                            },
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Task tags',
                            },
                            'parent': {
                                'type': ['string', 'null'],
                                'description': 'Parent task ID',
                            },
                            'priority': {
                                'type': ['object', 'null'],
                                'description': 'Task priority',
                            },
                            'due_date': {
                                'type': ['string', 'null'],
                                'description': 'Due date (Unix ms)',
                            },
                            'start_date': {
                                'type': ['string', 'null'],
                                'description': 'Start date (Unix ms)',
                            },
                            'points': {
                                'type': ['number', 'null'],
                                'description': 'Sprint points',
                            },
                            'time_estimate': {
                                'type': ['integer', 'null'],
                                'description': 'Time estimate (ms)',
                            },
                            'time_spent': {
                                'type': ['integer', 'null'],
                                'description': 'Time spent (ms)',
                            },
                            'custom_fields': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Custom fields',
                            },
                            'dependencies': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Task dependencies',
                            },
                            'linked_tasks': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Linked tasks',
                            },
                            'team_id': {
                                'type': ['string', 'null'],
                                'description': 'Workspace ID',
                            },
                            'url': {'type': 'string', 'description': 'Task URL'},
                            'list': {
                                'type': ['object', 'null'],
                                'description': 'Parent list reference',
                            },
                            'project': {
                                'type': ['object', 'null'],
                                'description': 'Parent project reference',
                            },
                            'folder': {
                                'type': ['object', 'null'],
                                'description': 'Parent folder reference',
                            },
                            'space': {
                                'type': ['object', 'null'],
                                'description': 'Parent space reference',
                            },
                            'top_level_parent': {
                                'type': ['string', 'null'],
                                'description': 'Top-level parent task ID',
                            },
                            'locations': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Task locations',
                            },
                            'sharing': {
                                'type': ['object', 'null'],
                                'description': 'Task sharing settings',
                            },
                            'permission_level': {
                                'type': ['string', 'null'],
                                'description': 'User permission level for this task',
                            },
                            'attachments': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Task attachments',
                            },
                        },
                        'x-airbyte-entity-name': 'tasks',
                        'x-airbyte-stream-name': 'task',
                        'x-airbyte-ai-hints': {
                            'summary': 'ClickUp tasks with assignees, due dates, statuses, and priorities',
                            'when_to_use': 'Questions about task assignments, status, or deadlines',
                            'trigger_phrases': [
                                'clickup task',
                                'assigned task',
                                'task status',
                                'due date',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What tasks are assigned to me?', 'Show overdue tasks in ClickUp'],
                            'search_strategy': 'Search by name or filter by assignee, status, or list',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team/{team_id}/task',
                    action=Action.API_SEARCH,
                    description='View the tasks that meet specific criteria from a workspace. Supports free-text search\nand structured filters including status, assignee, tags, priority, and date ranges.\nResponses are limited to 100 tasks per page.\n',
                    query_params=[
                        'search',
                        'statuses[]',
                        'assignees[]',
                        'tags[]',
                        'priority',
                        'due_date_gt',
                        'due_date_lt',
                        'date_created_gt',
                        'date_created_lt',
                        'date_updated_gt',
                        'date_updated_lt',
                        'custom_fields',
                        'include_closed',
                        'page',
                    ],
                    query_params_schema={
                        'search': {'type': 'string', 'required': False},
                        'statuses[]': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                        },
                        'assignees[]': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                        },
                        'tags[]': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'string'},
                        },
                        'priority': {'type': 'integer', 'required': False},
                        'due_date_gt': {'type': 'integer', 'required': False},
                        'due_date_lt': {'type': 'integer', 'required': False},
                        'date_created_gt': {'type': 'integer', 'required': False},
                        'date_created_lt': {'type': 'integer', 'required': False},
                        'date_updated_gt': {'type': 'integer', 'required': False},
                        'date_updated_lt': {'type': 'integer', 'required': False},
                        'custom_fields': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'object'},
                        },
                        'include_closed': {'type': 'boolean', 'required': False},
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['team_id'],
                    path_params_schema={
                        'team_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'tasks': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Task ID'},
                                        'custom_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom task ID',
                                        },
                                        'custom_item_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Custom item type identifier',
                                        },
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'text_content': {
                                            'type': ['string', 'null'],
                                            'description': 'Plain text content',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Task description',
                                        },
                                        'status': {
                                            'type': 'object',
                                            'description': 'Task status',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Status ID'},
                                                'status': {'type': 'string', 'description': 'Status name'},
                                                'color': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Status color hex code',
                                                },
                                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                            },
                                        },
                                        'orderindex': {
                                            'type': ['string', 'null'],
                                            'description': 'Sort order',
                                        },
                                        'date_created': {
                                            'type': ['string', 'null'],
                                            'description': 'Created date (Unix ms)',
                                        },
                                        'date_updated': {
                                            'type': ['string', 'null'],
                                            'description': 'Updated date (Unix ms)',
                                        },
                                        'date_closed': {
                                            'type': ['string', 'null'],
                                            'description': 'Closed date (Unix ms)',
                                        },
                                        'date_done': {
                                            'type': ['string', 'null'],
                                            'description': 'Done date (Unix ms)',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                                        'creator': {
                                            'type': 'object',
                                            'description': 'Task creator',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Creator user ID'},
                                                'username': {'type': 'string', 'description': 'Creator username'},
                                                'color': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Creator avatar color',
                                                },
                                                'email': {'type': 'string', 'description': 'Creator email'},
                                                'profilePicture': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Creator profile picture URL',
                                                },
                                            },
                                        },
                                        'assignees': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Assigned users',
                                        },
                                        'group_assignees': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Group assignees',
                                        },
                                        'watchers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Watcher user ID'},
                                                    'username': {'type': 'string', 'description': 'Watcher username'},
                                                    'color': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher avatar color',
                                                    },
                                                    'initials': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher initials',
                                                    },
                                                    'email': {'type': 'string', 'description': 'Watcher email'},
                                                    'profilePicture': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher profile picture URL',
                                                    },
                                                },
                                            },
                                            'description': 'Task watchers',
                                        },
                                        'checklists': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task checklists',
                                        },
                                        'tags': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task tags',
                                        },
                                        'parent': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent task ID',
                                        },
                                        'priority': {
                                            'type': ['object', 'null'],
                                            'description': 'Task priority',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Due date (Unix ms)',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Start date (Unix ms)',
                                        },
                                        'points': {
                                            'type': ['number', 'null'],
                                            'description': 'Sprint points',
                                        },
                                        'time_estimate': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time estimate (ms)',
                                        },
                                        'time_spent': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time spent (ms)',
                                        },
                                        'custom_fields': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Custom fields',
                                        },
                                        'dependencies': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task dependencies',
                                        },
                                        'linked_tasks': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Linked tasks',
                                        },
                                        'team_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID',
                                        },
                                        'url': {'type': 'string', 'description': 'Task URL'},
                                        'list': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent list reference',
                                        },
                                        'project': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent project reference',
                                        },
                                        'folder': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent folder reference',
                                        },
                                        'space': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent space reference',
                                        },
                                        'top_level_parent': {
                                            'type': ['string', 'null'],
                                            'description': 'Top-level parent task ID',
                                        },
                                        'locations': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task locations',
                                        },
                                        'sharing': {
                                            'type': ['object', 'null'],
                                            'description': 'Task sharing settings',
                                        },
                                        'permission_level': {
                                            'type': ['string', 'null'],
                                            'description': 'User permission level for this task',
                                        },
                                        'attachments': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task attachments',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                    'x-airbyte-stream-name': 'task',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp tasks with assignees, due dates, statuses, and priorities',
                                        'when_to_use': 'Questions about task assignments, status, or deadlines',
                                        'trigger_phrases': [
                                            'clickup task',
                                            'assigned task',
                                            'task status',
                                            'due date',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What tasks are assigned to me?', 'Show overdue tasks in ClickUp'],
                                        'search_strategy': 'Search by name or filter by assignee, status, or list',
                                    },
                                },
                            },
                            'last_page': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page of results',
                            },
                        },
                    },
                    record_extractor='$.tasks',
                    meta_extractor={'last_page': '$.last_page'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Task ID'},
                    'custom_id': {
                        'type': ['string', 'null'],
                        'description': 'Custom task ID',
                    },
                    'custom_item_id': {
                        'type': ['integer', 'null'],
                        'description': 'Custom item type identifier',
                    },
                    'name': {'type': 'string', 'description': 'Task name'},
                    'text_content': {
                        'type': ['string', 'null'],
                        'description': 'Plain text content',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Task description',
                    },
                    'status': {
                        'type': 'object',
                        'description': 'Task status',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Status ID'},
                            'status': {'type': 'string', 'description': 'Status name'},
                            'color': {
                                'type': ['string', 'null'],
                                'description': 'Status color hex code',
                            },
                            'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                            'orderindex': {'type': 'integer', 'description': 'Status order index'},
                        },
                    },
                    'orderindex': {
                        'type': ['string', 'null'],
                        'description': 'Sort order',
                    },
                    'date_created': {
                        'type': ['string', 'null'],
                        'description': 'Created date (Unix ms)',
                    },
                    'date_updated': {
                        'type': ['string', 'null'],
                        'description': 'Updated date (Unix ms)',
                    },
                    'date_closed': {
                        'type': ['string', 'null'],
                        'description': 'Closed date (Unix ms)',
                    },
                    'date_done': {
                        'type': ['string', 'null'],
                        'description': 'Done date (Unix ms)',
                    },
                    'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                    'creator': {
                        'type': 'object',
                        'description': 'Task creator',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Creator user ID'},
                            'username': {'type': 'string', 'description': 'Creator username'},
                            'color': {
                                'type': ['string', 'null'],
                                'description': 'Creator avatar color',
                            },
                            'email': {'type': 'string', 'description': 'Creator email'},
                            'profilePicture': {
                                'type': ['string', 'null'],
                                'description': 'Creator profile picture URL',
                            },
                        },
                    },
                    'assignees': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Assigned users',
                    },
                    'group_assignees': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Group assignees',
                    },
                    'watchers': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Watcher user ID'},
                                'username': {'type': 'string', 'description': 'Watcher username'},
                                'color': {
                                    'type': ['string', 'null'],
                                    'description': 'Watcher avatar color',
                                },
                                'initials': {
                                    'type': ['string', 'null'],
                                    'description': 'Watcher initials',
                                },
                                'email': {'type': 'string', 'description': 'Watcher email'},
                                'profilePicture': {
                                    'type': ['string', 'null'],
                                    'description': 'Watcher profile picture URL',
                                },
                            },
                        },
                        'description': 'Task watchers',
                    },
                    'checklists': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Task checklists',
                    },
                    'tags': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Task tags',
                    },
                    'parent': {
                        'type': ['string', 'null'],
                        'description': 'Parent task ID',
                    },
                    'priority': {
                        'type': ['object', 'null'],
                        'description': 'Task priority',
                    },
                    'due_date': {
                        'type': ['string', 'null'],
                        'description': 'Due date (Unix ms)',
                    },
                    'start_date': {
                        'type': ['string', 'null'],
                        'description': 'Start date (Unix ms)',
                    },
                    'points': {
                        'type': ['number', 'null'],
                        'description': 'Sprint points',
                    },
                    'time_estimate': {
                        'type': ['integer', 'null'],
                        'description': 'Time estimate (ms)',
                    },
                    'time_spent': {
                        'type': ['integer', 'null'],
                        'description': 'Time spent (ms)',
                    },
                    'custom_fields': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Custom fields',
                    },
                    'dependencies': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Task dependencies',
                    },
                    'linked_tasks': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Linked tasks',
                    },
                    'team_id': {
                        'type': ['string', 'null'],
                        'description': 'Workspace ID',
                    },
                    'url': {'type': 'string', 'description': 'Task URL'},
                    'list': {
                        'type': ['object', 'null'],
                        'description': 'Parent list reference',
                    },
                    'project': {
                        'type': ['object', 'null'],
                        'description': 'Parent project reference',
                    },
                    'folder': {
                        'type': ['object', 'null'],
                        'description': 'Parent folder reference',
                    },
                    'space': {
                        'type': ['object', 'null'],
                        'description': 'Parent space reference',
                    },
                    'top_level_parent': {
                        'type': ['string', 'null'],
                        'description': 'Top-level parent task ID',
                    },
                    'locations': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Task locations',
                    },
                    'sharing': {
                        'type': ['object', 'null'],
                        'description': 'Task sharing settings',
                    },
                    'permission_level': {
                        'type': ['string', 'null'],
                        'description': 'User permission level for this task',
                    },
                    'attachments': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Task attachments',
                    },
                },
                'x-airbyte-entity-name': 'tasks',
                'x-airbyte-stream-name': 'task',
                'x-airbyte-ai-hints': {
                    'summary': 'ClickUp tasks with assignees, due dates, statuses, and priorities',
                    'when_to_use': 'Questions about task assignments, status, or deadlines',
                    'trigger_phrases': [
                        'clickup task',
                        'assigned task',
                        'task status',
                        'due date',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What tasks are assigned to me?', 'Show overdue tasks in ClickUp'],
                    'search_strategy': 'Search by name or filter by assignee, status, or list',
                },
            },
            ai_hints={
                'summary': 'ClickUp tasks with assignees, due dates, statuses, and priorities',
                'when_to_use': 'Questions about task assignments, status, or deadlines',
                'trigger_phrases': [
                    'clickup task',
                    'assigned task',
                    'task status',
                    'due date',
                ],
                'freshness': 'live',
                'example_questions': ['What tasks are assigned to me?', 'Show overdue tasks in ClickUp'],
                'search_strategy': 'Search by name or filter by assignee, status, or list',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='lists',
                    foreign_key='list_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='comments',
            stream_name='list_comments',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/task/{task_id}/comment',
                    action=Action.LIST,
                    description='Get the comments on a task',
                    path_params=['task_id'],
                    path_params_schema={
                        'task_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'comments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Comment ID'},
                                        'comment': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Comment content blocks',
                                        },
                                        'comment_text': {'type': 'string', 'description': 'Plain text comment'},
                                        'user': {'type': 'object', 'description': 'Comment author'},
                                        'resolved': {'type': 'boolean', 'description': 'Whether the comment is resolved'},
                                        'assignee': {
                                            'type': ['object', 'null'],
                                            'description': 'Assigned user',
                                        },
                                        'assigned_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who assigned',
                                        },
                                        'reactions': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Comment reactions',
                                        },
                                        'date': {'type': 'string', 'description': 'Comment date (Unix ms)'},
                                    },
                                    'x-airbyte-entity-name': 'comments',
                                    'x-airbyte-stream-name': 'list_comments',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Comments on ClickUp tasks',
                                        'when_to_use': 'Looking for discussion or notes on specific tasks',
                                        'trigger_phrases': ['clickup comment', 'task comment', 'task discussion'],
                                        'freshness': 'live',
                                        'example_questions': ['What comments are on this task?'],
                                        'search_strategy': 'Filter by task',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.comments',
                    no_pagination='ClickUp GET /api/v2/task/{task_id}/comment returns all comments on the task in a single response; cursor-based pagination is only available on alternate start/start_id query params not modelled here.',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/api/v2/task/{task_id}/comment',
                    action=Action.CREATE,
                    description='Create a comment on a task',
                    body_fields=['comment_text', 'assignee', 'notify_all'],
                    path_params=['task_id'],
                    path_params_schema={
                        'task_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'comment_text': {'type': 'string', 'description': 'The comment text'},
                            'assignee': {'type': 'integer', 'description': 'User ID to assign'},
                            'notify_all': {'type': 'boolean', 'description': 'Notify all assignees and watchers'},
                        },
                        'required': ['comment_text'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'New comment ID'},
                            'hist_id': {'type': 'string', 'description': 'History ID'},
                            'date': {'type': 'integer', 'description': 'Comment date (Unix ms)'},
                            'version': {
                                'type': ['object', 'null'],
                                'description': 'Version metadata for the comment operation',
                            },
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/comment/{comment_id}/reply',
                    action=Action.GET,
                    description='Get threaded replies on a comment',
                    path_params=['comment_id'],
                    path_params_schema={
                        'comment_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'comments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Comment ID'},
                                        'comment': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Comment content blocks',
                                        },
                                        'comment_text': {'type': 'string', 'description': 'Plain text comment'},
                                        'user': {'type': 'object', 'description': 'Comment author'},
                                        'resolved': {'type': 'boolean', 'description': 'Whether the comment is resolved'},
                                        'assignee': {
                                            'type': ['object', 'null'],
                                            'description': 'Assigned user',
                                        },
                                        'assigned_by': {
                                            'type': ['object', 'null'],
                                            'description': 'User who assigned',
                                        },
                                        'reactions': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Comment reactions',
                                        },
                                        'date': {'type': 'string', 'description': 'Comment date (Unix ms)'},
                                    },
                                    'x-airbyte-entity-name': 'comments',
                                    'x-airbyte-stream-name': 'list_comments',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Comments on ClickUp tasks',
                                        'when_to_use': 'Looking for discussion or notes on specific tasks',
                                        'trigger_phrases': ['clickup comment', 'task comment', 'task discussion'],
                                        'freshness': 'live',
                                        'example_questions': ['What comments are on this task?'],
                                        'search_strategy': 'Filter by task',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.comments',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/api/v2/comment/{comment_id}',
                    action=Action.UPDATE,
                    description='Update an existing comment',
                    body_fields=['comment_text', 'assignee', 'resolved'],
                    path_params=['comment_id'],
                    path_params_schema={
                        'comment_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'comment_text': {'type': 'string', 'description': 'Updated comment text'},
                            'assignee': {'type': 'integer', 'description': 'User ID to assign'},
                            'resolved': {'type': 'boolean', 'description': 'Whether the comment is resolved'},
                        },
                    },
                    response_schema={'type': 'object'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Comment ID'},
                    'comment': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Comment content blocks',
                    },
                    'comment_text': {'type': 'string', 'description': 'Plain text comment'},
                    'user': {'type': 'object', 'description': 'Comment author'},
                    'resolved': {'type': 'boolean', 'description': 'Whether the comment is resolved'},
                    'assignee': {
                        'type': ['object', 'null'],
                        'description': 'Assigned user',
                    },
                    'assigned_by': {
                        'type': ['object', 'null'],
                        'description': 'User who assigned',
                    },
                    'reactions': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Comment reactions',
                    },
                    'date': {'type': 'string', 'description': 'Comment date (Unix ms)'},
                },
                'x-airbyte-entity-name': 'comments',
                'x-airbyte-stream-name': 'list_comments',
                'x-airbyte-ai-hints': {
                    'summary': 'Comments on ClickUp tasks',
                    'when_to_use': 'Looking for discussion or notes on specific tasks',
                    'trigger_phrases': ['clickup comment', 'task comment', 'task discussion'],
                    'freshness': 'live',
                    'example_questions': ['What comments are on this task?'],
                    'search_strategy': 'Filter by task',
                },
            },
            ai_hints={
                'summary': 'Comments on ClickUp tasks',
                'when_to_use': 'Looking for discussion or notes on specific tasks',
                'trigger_phrases': ['clickup comment', 'task comment', 'task discussion'],
                'freshness': 'live',
                'example_questions': ['What comments are on this task?'],
                'search_strategy': 'Filter by task',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='comments',
                    target_entity='tasks',
                    foreign_key='task_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='goals',
            stream_name='team_goals',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team/{team_id}/goal',
                    action=Action.LIST,
                    description='Get the goals in a workspace',
                    path_params=['team_id'],
                    path_params_schema={
                        'team_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'goals': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Goal ID'},
                                        'pretty_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Human-readable goal ID',
                                        },
                                        'name': {'type': 'string', 'description': 'Goal name'},
                                        'team_id': {'type': 'string', 'description': 'Workspace ID'},
                                        'creator': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creator user ID',
                                        },
                                        'owner': {
                                            'type': ['object', 'null'],
                                            'description': 'Goal owner',
                                        },
                                        'color': {'type': 'string', 'description': 'Goal color'},
                                        'date_created': {
                                            'type': ['string', 'null'],
                                            'description': 'Created date (Unix ms)',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Start date (Unix ms)',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Due date (Unix ms)',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Goal description',
                                        },
                                        'private': {'type': 'boolean', 'description': 'Whether the goal is private'},
                                        'archived': {'type': 'boolean', 'description': 'Whether the goal is archived'},
                                        'multiple_owners': {'type': 'boolean', 'description': 'Multiple owners allowed'},
                                        'members': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Goal members',
                                        },
                                        'key_results': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Key results',
                                        },
                                        'percent_completed': {
                                            'type': ['integer', 'null'],
                                            'description': 'Completion percentage',
                                        },
                                        'history': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Goal history',
                                        },
                                        'pretty_url': {
                                            'type': ['string', 'null'],
                                            'description': 'Goal URL',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'goals',
                                    'x-airbyte-stream-name': 'team_goals',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Goals and targets tracked in ClickUp',
                                        'when_to_use': 'Questions about team goals, OKRs, or targets',
                                        'trigger_phrases': [
                                            'clickup goal',
                                            'target',
                                            'OKR',
                                            'objective',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What goals are set in ClickUp?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'folders': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Goal folders',
                            },
                        },
                    },
                    record_extractor='$.goals',
                    no_pagination='ClickUp GET /api/v2/team/{team_id}/goal returns all goals in the workspace in a single response; no pagination cursor or offset is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/goal/{goal_id}',
                    action=Action.GET,
                    description='Get a single goal by ID',
                    path_params=['goal_id'],
                    path_params_schema={
                        'goal_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'goal': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Goal ID'},
                                    'pretty_id': {
                                        'type': ['string', 'null'],
                                        'description': 'Human-readable goal ID',
                                    },
                                    'name': {'type': 'string', 'description': 'Goal name'},
                                    'team_id': {'type': 'string', 'description': 'Workspace ID'},
                                    'creator': {
                                        'type': ['integer', 'null'],
                                        'description': 'Creator user ID',
                                    },
                                    'owner': {
                                        'type': ['object', 'null'],
                                        'description': 'Goal owner',
                                    },
                                    'color': {'type': 'string', 'description': 'Goal color'},
                                    'date_created': {
                                        'type': ['string', 'null'],
                                        'description': 'Created date (Unix ms)',
                                    },
                                    'start_date': {
                                        'type': ['string', 'null'],
                                        'description': 'Start date (Unix ms)',
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                        'description': 'Due date (Unix ms)',
                                    },
                                    'description': {
                                        'type': ['string', 'null'],
                                        'description': 'Goal description',
                                    },
                                    'private': {'type': 'boolean', 'description': 'Whether the goal is private'},
                                    'archived': {'type': 'boolean', 'description': 'Whether the goal is archived'},
                                    'multiple_owners': {'type': 'boolean', 'description': 'Multiple owners allowed'},
                                    'members': {
                                        'type': 'array',
                                        'items': {'type': 'object'},
                                        'description': 'Goal members',
                                    },
                                    'key_results': {
                                        'type': 'array',
                                        'items': {'type': 'object'},
                                        'description': 'Key results',
                                    },
                                    'percent_completed': {
                                        'type': ['integer', 'null'],
                                        'description': 'Completion percentage',
                                    },
                                    'history': {
                                        'type': 'array',
                                        'items': {'type': 'object'},
                                        'description': 'Goal history',
                                    },
                                    'pretty_url': {
                                        'type': ['string', 'null'],
                                        'description': 'Goal URL',
                                    },
                                },
                                'x-airbyte-entity-name': 'goals',
                                'x-airbyte-stream-name': 'team_goals',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Goals and targets tracked in ClickUp',
                                    'when_to_use': 'Questions about team goals, OKRs, or targets',
                                    'trigger_phrases': [
                                        'clickup goal',
                                        'target',
                                        'OKR',
                                        'objective',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What goals are set in ClickUp?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                        },
                    },
                    record_extractor='$.goal',
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Goal ID'},
                    'pretty_id': {
                        'type': ['string', 'null'],
                        'description': 'Human-readable goal ID',
                    },
                    'name': {'type': 'string', 'description': 'Goal name'},
                    'team_id': {'type': 'string', 'description': 'Workspace ID'},
                    'creator': {
                        'type': ['integer', 'null'],
                        'description': 'Creator user ID',
                    },
                    'owner': {
                        'type': ['object', 'null'],
                        'description': 'Goal owner',
                    },
                    'color': {'type': 'string', 'description': 'Goal color'},
                    'date_created': {
                        'type': ['string', 'null'],
                        'description': 'Created date (Unix ms)',
                    },
                    'start_date': {
                        'type': ['string', 'null'],
                        'description': 'Start date (Unix ms)',
                    },
                    'due_date': {
                        'type': ['string', 'null'],
                        'description': 'Due date (Unix ms)',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Goal description',
                    },
                    'private': {'type': 'boolean', 'description': 'Whether the goal is private'},
                    'archived': {'type': 'boolean', 'description': 'Whether the goal is archived'},
                    'multiple_owners': {'type': 'boolean', 'description': 'Multiple owners allowed'},
                    'members': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Goal members',
                    },
                    'key_results': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Key results',
                    },
                    'percent_completed': {
                        'type': ['integer', 'null'],
                        'description': 'Completion percentage',
                    },
                    'history': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Goal history',
                    },
                    'pretty_url': {
                        'type': ['string', 'null'],
                        'description': 'Goal URL',
                    },
                },
                'x-airbyte-entity-name': 'goals',
                'x-airbyte-stream-name': 'team_goals',
                'x-airbyte-ai-hints': {
                    'summary': 'Goals and targets tracked in ClickUp',
                    'when_to_use': 'Questions about team goals, OKRs, or targets',
                    'trigger_phrases': [
                        'clickup goal',
                        'target',
                        'OKR',
                        'objective',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What goals are set in ClickUp?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Goals and targets tracked in ClickUp',
                'when_to_use': 'Questions about team goals, OKRs, or targets',
                'trigger_phrases': [
                    'clickup goal',
                    'target',
                    'OKR',
                    'objective',
                ],
                'freshness': 'live',
                'example_questions': ['What goals are set in ClickUp?'],
                'search_strategy': 'Search by name',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='goals',
                    target_entity='teams',
                    foreign_key='team_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='views',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team/{team_id}/view',
                    action=Action.LIST,
                    description='Get the workspace-level (Everything level) views',
                    path_params=['team_id'],
                    path_params_schema={
                        'team_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'views': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'View ID'},
                                        'name': {'type': 'string', 'description': 'View name'},
                                        'type': {'type': 'string', 'description': 'View type (list, board, calendar, gantt, etc.)'},
                                        'parent': {
                                            'type': 'object',
                                            'description': 'Parent reference',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'integer'],
                                                    'description': 'Parent entity ID',
                                                },
                                                'type': {
                                                    'type': ['string', 'integer'],
                                                    'description': 'Parent entity type',
                                                },
                                            },
                                        },
                                        'grouping': {'type': 'object', 'description': 'Grouping settings'},
                                        'divide': {'type': 'object', 'description': 'Division settings'},
                                        'sorting': {'type': 'object', 'description': 'Sorting settings'},
                                        'filters': {'type': 'object', 'description': 'Filter settings'},
                                        'columns': {'type': 'object', 'description': 'Column settings'},
                                        'team_sidebar': {'type': 'object', 'description': 'Team sidebar settings'},
                                        'settings': {'type': 'object', 'description': 'View settings'},
                                        'date_created': {
                                            'type': ['string', 'null'],
                                            'description': 'Created date (Unix ms)',
                                        },
                                        'creator': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creator user ID',
                                        },
                                        'visibility': {
                                            'type': ['string', 'null'],
                                            'description': 'View visibility',
                                        },
                                        'protected': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the view is protected',
                                        },
                                        'protected_note': {
                                            'type': ['string', 'null'],
                                            'description': 'Note associated with protection',
                                        },
                                        'protected_by': {
                                            'type': ['integer', 'null'],
                                            'description': 'User ID who protected the view',
                                        },
                                        'date_protected': {
                                            'type': ['string', 'null'],
                                            'description': 'Date the view was protected (Unix ms or null)',
                                        },
                                        'orderindex': {'type': 'integer', 'description': 'View order index'},
                                        'public': {'type': 'boolean', 'description': 'Whether the view is public'},
                                    },
                                    'x-airbyte-entity-name': 'views',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Saved views for filtering and displaying ClickUp data',
                                        'when_to_use': 'Questions about saved views or display configurations',
                                        'trigger_phrases': ['clickup view', 'saved view', 'board view'],
                                        'freshness': 'live',
                                        'example_questions': ['What views are saved in ClickUp?'],
                                        'search_strategy': 'Filter by space or list',
                                    },
                                },
                            },
                            'required_views': {
                                'type': ['object', 'null'],
                                'description': 'Required views configuration by type',
                            },
                            'default_view': {
                                'type': ['object', 'null'],
                                'description': 'Default view configuration',
                            },
                        },
                    },
                    record_extractor='$.views',
                    no_pagination='ClickUp GET /api/v2/team/{team_id}/view returns all workspace-level views in a single response; no pagination cursor or offset is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/view/{view_id}',
                    action=Action.GET,
                    description='Get a single view by ID',
                    path_params=['view_id'],
                    path_params_schema={
                        'view_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'view': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'View ID'},
                                    'name': {'type': 'string', 'description': 'View name'},
                                    'type': {'type': 'string', 'description': 'View type (list, board, calendar, gantt, etc.)'},
                                    'parent': {
                                        'type': 'object',
                                        'description': 'Parent reference',
                                        'properties': {
                                            'id': {
                                                'type': ['string', 'integer'],
                                                'description': 'Parent entity ID',
                                            },
                                            'type': {
                                                'type': ['string', 'integer'],
                                                'description': 'Parent entity type',
                                            },
                                        },
                                    },
                                    'grouping': {'type': 'object', 'description': 'Grouping settings'},
                                    'divide': {'type': 'object', 'description': 'Division settings'},
                                    'sorting': {'type': 'object', 'description': 'Sorting settings'},
                                    'filters': {'type': 'object', 'description': 'Filter settings'},
                                    'columns': {'type': 'object', 'description': 'Column settings'},
                                    'team_sidebar': {'type': 'object', 'description': 'Team sidebar settings'},
                                    'settings': {'type': 'object', 'description': 'View settings'},
                                    'date_created': {
                                        'type': ['string', 'null'],
                                        'description': 'Created date (Unix ms)',
                                    },
                                    'creator': {
                                        'type': ['integer', 'null'],
                                        'description': 'Creator user ID',
                                    },
                                    'visibility': {
                                        'type': ['string', 'null'],
                                        'description': 'View visibility',
                                    },
                                    'protected': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the view is protected',
                                    },
                                    'protected_note': {
                                        'type': ['string', 'null'],
                                        'description': 'Note associated with protection',
                                    },
                                    'protected_by': {
                                        'type': ['integer', 'null'],
                                        'description': 'User ID who protected the view',
                                    },
                                    'date_protected': {
                                        'type': ['string', 'null'],
                                        'description': 'Date the view was protected (Unix ms or null)',
                                    },
                                    'orderindex': {'type': 'integer', 'description': 'View order index'},
                                    'public': {'type': 'boolean', 'description': 'Whether the view is public'},
                                },
                                'x-airbyte-entity-name': 'views',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Saved views for filtering and displaying ClickUp data',
                                    'when_to_use': 'Questions about saved views or display configurations',
                                    'trigger_phrases': ['clickup view', 'saved view', 'board view'],
                                    'freshness': 'live',
                                    'example_questions': ['What views are saved in ClickUp?'],
                                    'search_strategy': 'Filter by space or list',
                                },
                            },
                        },
                    },
                    record_extractor='$.view',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'View ID'},
                    'name': {'type': 'string', 'description': 'View name'},
                    'type': {'type': 'string', 'description': 'View type (list, board, calendar, gantt, etc.)'},
                    'parent': {
                        'type': 'object',
                        'description': 'Parent reference',
                        'properties': {
                            'id': {
                                'type': ['string', 'integer'],
                                'description': 'Parent entity ID',
                            },
                            'type': {
                                'type': ['string', 'integer'],
                                'description': 'Parent entity type',
                            },
                        },
                    },
                    'grouping': {'type': 'object', 'description': 'Grouping settings'},
                    'divide': {'type': 'object', 'description': 'Division settings'},
                    'sorting': {'type': 'object', 'description': 'Sorting settings'},
                    'filters': {'type': 'object', 'description': 'Filter settings'},
                    'columns': {'type': 'object', 'description': 'Column settings'},
                    'team_sidebar': {'type': 'object', 'description': 'Team sidebar settings'},
                    'settings': {'type': 'object', 'description': 'View settings'},
                    'date_created': {
                        'type': ['string', 'null'],
                        'description': 'Created date (Unix ms)',
                    },
                    'creator': {
                        'type': ['integer', 'null'],
                        'description': 'Creator user ID',
                    },
                    'visibility': {
                        'type': ['string', 'null'],
                        'description': 'View visibility',
                    },
                    'protected': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the view is protected',
                    },
                    'protected_note': {
                        'type': ['string', 'null'],
                        'description': 'Note associated with protection',
                    },
                    'protected_by': {
                        'type': ['integer', 'null'],
                        'description': 'User ID who protected the view',
                    },
                    'date_protected': {
                        'type': ['string', 'null'],
                        'description': 'Date the view was protected (Unix ms or null)',
                    },
                    'orderindex': {'type': 'integer', 'description': 'View order index'},
                    'public': {'type': 'boolean', 'description': 'Whether the view is public'},
                },
                'x-airbyte-entity-name': 'views',
                'x-airbyte-ai-hints': {
                    'summary': 'Saved views for filtering and displaying ClickUp data',
                    'when_to_use': 'Questions about saved views or display configurations',
                    'trigger_phrases': ['clickup view', 'saved view', 'board view'],
                    'freshness': 'live',
                    'example_questions': ['What views are saved in ClickUp?'],
                    'search_strategy': 'Filter by space or list',
                },
            },
            ai_hints={
                'summary': 'Saved views for filtering and displaying ClickUp data',
                'when_to_use': 'Questions about saved views or display configurations',
                'trigger_phrases': ['clickup view', 'saved view', 'board view'],
                'freshness': 'live',
                'example_questions': ['What views are saved in ClickUp?'],
                'search_strategy': 'Filter by space or list',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='views',
                    target_entity='teams',
                    foreign_key='team_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='view_tasks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/view/{view_id}/task',
                    action=Action.LIST,
                    description="Get tasks matching a view's pre-configured filters — useful as a secondary search mechanism",
                    query_params=['page'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['view_id'],
                    path_params_schema={
                        'view_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'tasks': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Task ID'},
                                        'custom_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom task ID',
                                        },
                                        'custom_item_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Custom item type identifier',
                                        },
                                        'name': {'type': 'string', 'description': 'Task name'},
                                        'text_content': {
                                            'type': ['string', 'null'],
                                            'description': 'Plain text content',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Task description',
                                        },
                                        'status': {
                                            'type': 'object',
                                            'description': 'Task status',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Status ID'},
                                                'status': {'type': 'string', 'description': 'Status name'},
                                                'color': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Status color hex code',
                                                },
                                                'type': {'type': 'string', 'description': 'Status type (open, custom, closed)'},
                                                'orderindex': {'type': 'integer', 'description': 'Status order index'},
                                            },
                                        },
                                        'orderindex': {
                                            'type': ['string', 'null'],
                                            'description': 'Sort order',
                                        },
                                        'date_created': {
                                            'type': ['string', 'null'],
                                            'description': 'Created date (Unix ms)',
                                        },
                                        'date_updated': {
                                            'type': ['string', 'null'],
                                            'description': 'Updated date (Unix ms)',
                                        },
                                        'date_closed': {
                                            'type': ['string', 'null'],
                                            'description': 'Closed date (Unix ms)',
                                        },
                                        'date_done': {
                                            'type': ['string', 'null'],
                                            'description': 'Done date (Unix ms)',
                                        },
                                        'archived': {'type': 'boolean', 'description': 'Whether the task is archived'},
                                        'creator': {
                                            'type': 'object',
                                            'description': 'Task creator',
                                            'properties': {
                                                'id': {'type': 'integer', 'description': 'Creator user ID'},
                                                'username': {'type': 'string', 'description': 'Creator username'},
                                                'color': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Creator avatar color',
                                                },
                                                'email': {'type': 'string', 'description': 'Creator email'},
                                                'profilePicture': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Creator profile picture URL',
                                                },
                                            },
                                        },
                                        'assignees': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Assigned users',
                                        },
                                        'group_assignees': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Group assignees',
                                        },
                                        'watchers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'integer', 'description': 'Watcher user ID'},
                                                    'username': {'type': 'string', 'description': 'Watcher username'},
                                                    'color': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher avatar color',
                                                    },
                                                    'initials': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher initials',
                                                    },
                                                    'email': {'type': 'string', 'description': 'Watcher email'},
                                                    'profilePicture': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Watcher profile picture URL',
                                                    },
                                                },
                                            },
                                            'description': 'Task watchers',
                                        },
                                        'checklists': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task checklists',
                                        },
                                        'tags': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task tags',
                                        },
                                        'parent': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent task ID',
                                        },
                                        'priority': {
                                            'type': ['object', 'null'],
                                            'description': 'Task priority',
                                        },
                                        'due_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Due date (Unix ms)',
                                        },
                                        'start_date': {
                                            'type': ['string', 'null'],
                                            'description': 'Start date (Unix ms)',
                                        },
                                        'points': {
                                            'type': ['number', 'null'],
                                            'description': 'Sprint points',
                                        },
                                        'time_estimate': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time estimate (ms)',
                                        },
                                        'time_spent': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time spent (ms)',
                                        },
                                        'custom_fields': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Custom fields',
                                        },
                                        'dependencies': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task dependencies',
                                        },
                                        'linked_tasks': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Linked tasks',
                                        },
                                        'team_id': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID',
                                        },
                                        'url': {'type': 'string', 'description': 'Task URL'},
                                        'list': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent list reference',
                                        },
                                        'project': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent project reference',
                                        },
                                        'folder': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent folder reference',
                                        },
                                        'space': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent space reference',
                                        },
                                        'top_level_parent': {
                                            'type': ['string', 'null'],
                                            'description': 'Top-level parent task ID',
                                        },
                                        'locations': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task locations',
                                        },
                                        'sharing': {
                                            'type': ['object', 'null'],
                                            'description': 'Task sharing settings',
                                        },
                                        'permission_level': {
                                            'type': ['string', 'null'],
                                            'description': 'User permission level for this task',
                                        },
                                        'attachments': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Task attachments',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tasks',
                                    'x-airbyte-stream-name': 'task',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp tasks with assignees, due dates, statuses, and priorities',
                                        'when_to_use': 'Questions about task assignments, status, or deadlines',
                                        'trigger_phrases': [
                                            'clickup task',
                                            'assigned task',
                                            'task status',
                                            'due date',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What tasks are assigned to me?', 'Show overdue tasks in ClickUp'],
                                        'search_strategy': 'Search by name or filter by assignee, status, or list',
                                    },
                                },
                            },
                            'last_page': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page of results',
                            },
                        },
                    },
                    record_extractor='$.tasks',
                    meta_extractor={'last_page': '$.last_page'},
                    untested=True,
                ),
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='view_tasks',
                    target_entity='views',
                    foreign_key='view_id',
                    cardinality='many_to_one',
                    parent_record_filter={
                        'type': [
                            'list',
                            'board',
                            'calendar',
                            'gantt',
                        ],
                    },
                ),
            ],
        ),
        EntityDefinition(
            name='time_tracking',
            stream_name='time_tracking',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team/{team_id}/time_entries',
                    action=Action.LIST,
                    description='Get time entries within a date range for a workspace',
                    query_params=['start_date', 'end_date', 'assignee'],
                    query_params_schema={
                        'start_date': {'type': 'integer', 'required': False},
                        'end_date': {'type': 'integer', 'required': False},
                        'assignee': {'type': 'string', 'required': False},
                    },
                    path_params=['team_id'],
                    path_params_schema={
                        'team_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Time entry ID'},
                                        'task': {
                                            'type': ['object', 'null'],
                                            'description': 'Associated task',
                                        },
                                        'wid': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID',
                                        },
                                        'user': {'type': 'object', 'description': 'User who tracked time'},
                                        'billable': {'type': 'boolean', 'description': 'Whether the entry is billable'},
                                        'start': {'type': 'string', 'description': 'Start time (Unix ms)'},
                                        'end': {
                                            'type': ['string', 'null'],
                                            'description': 'End time (Unix ms)',
                                        },
                                        'duration': {'type': 'string', 'description': 'Duration in milliseconds'},
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Time entry description',
                                        },
                                        'tags': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                            'description': 'Time entry tags',
                                        },
                                        'at': {
                                            'type': ['string', 'null'],
                                            'description': 'Last updated (Unix ms)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'time_tracking',
                                    'x-airbyte-stream-name': 'time_tracking',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Time tracking entries on ClickUp tasks',
                                        'when_to_use': 'Questions about logged hours or time tracking data',
                                        'trigger_phrases': [
                                            'time tracking',
                                            'hours logged',
                                            'time entry',
                                            'time spent',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['How much time was logged on a task?', 'Show time entries for this week'],
                                        'search_strategy': 'Filter by task or assignee',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    no_pagination='ClickUp GET /api/v2/team/{team_id}/time_entries returns a bounded set of time entries scoped to the requested start_date/end_date window; no pagination cursor or offset is exposed.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/team/{team_id}/time_entries/{time_entry_id}',
                    action=Action.GET,
                    description='Get a single time entry by ID',
                    path_params=['team_id', 'time_entry_id'],
                    path_params_schema={
                        'team_id': {'type': 'string', 'required': True},
                        'time_entry_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Time entry ID'},
                                    'task': {
                                        'type': ['object', 'null'],
                                        'description': 'Associated task',
                                    },
                                    'wid': {
                                        'type': ['string', 'null'],
                                        'description': 'Workspace ID',
                                    },
                                    'user': {'type': 'object', 'description': 'User who tracked time'},
                                    'billable': {'type': 'boolean', 'description': 'Whether the entry is billable'},
                                    'start': {'type': 'string', 'description': 'Start time (Unix ms)'},
                                    'end': {
                                        'type': ['string', 'null'],
                                        'description': 'End time (Unix ms)',
                                    },
                                    'duration': {'type': 'string', 'description': 'Duration in milliseconds'},
                                    'description': {
                                        'type': ['string', 'null'],
                                        'description': 'Time entry description',
                                    },
                                    'tags': {
                                        'type': 'array',
                                        'items': {'type': 'object'},
                                        'description': 'Time entry tags',
                                    },
                                    'at': {
                                        'type': ['string', 'null'],
                                        'description': 'Last updated (Unix ms)',
                                    },
                                },
                                'x-airbyte-entity-name': 'time_tracking',
                                'x-airbyte-stream-name': 'time_tracking',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Time tracking entries on ClickUp tasks',
                                    'when_to_use': 'Questions about logged hours or time tracking data',
                                    'trigger_phrases': [
                                        'time tracking',
                                        'hours logged',
                                        'time entry',
                                        'time spent',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['How much time was logged on a task?', 'Show time entries for this week'],
                                    'search_strategy': 'Filter by task or assignee',
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Time entry ID'},
                    'task': {
                        'type': ['object', 'null'],
                        'description': 'Associated task',
                    },
                    'wid': {
                        'type': ['string', 'null'],
                        'description': 'Workspace ID',
                    },
                    'user': {'type': 'object', 'description': 'User who tracked time'},
                    'billable': {'type': 'boolean', 'description': 'Whether the entry is billable'},
                    'start': {'type': 'string', 'description': 'Start time (Unix ms)'},
                    'end': {
                        'type': ['string', 'null'],
                        'description': 'End time (Unix ms)',
                    },
                    'duration': {'type': 'string', 'description': 'Duration in milliseconds'},
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Time entry description',
                    },
                    'tags': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Time entry tags',
                    },
                    'at': {
                        'type': ['string', 'null'],
                        'description': 'Last updated (Unix ms)',
                    },
                },
                'x-airbyte-entity-name': 'time_tracking',
                'x-airbyte-stream-name': 'time_tracking',
                'x-airbyte-ai-hints': {
                    'summary': 'Time tracking entries on ClickUp tasks',
                    'when_to_use': 'Questions about logged hours or time tracking data',
                    'trigger_phrases': [
                        'time tracking',
                        'hours logged',
                        'time entry',
                        'time spent',
                    ],
                    'freshness': 'live',
                    'example_questions': ['How much time was logged on a task?', 'Show time entries for this week'],
                    'search_strategy': 'Filter by task or assignee',
                },
            },
            ai_hints={
                'summary': 'Time tracking entries on ClickUp tasks',
                'when_to_use': 'Questions about logged hours or time tracking data',
                'trigger_phrases': [
                    'time tracking',
                    'hours logged',
                    'time entry',
                    'time spent',
                ],
                'freshness': 'live',
                'example_questions': ['How much time was logged on a task?', 'Show time entries for this week'],
                'search_strategy': 'Filter by task or assignee',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='time_tracking',
                    target_entity='teams',
                    foreign_key='team_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='members',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v2/task/{task_id}/member',
                    action=Action.LIST,
                    description='Get the members assigned to a task',
                    path_params=['task_id'],
                    path_params_schema={
                        'task_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'members': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Member user ID'},
                                        'username': {'type': 'string', 'description': 'Username'},
                                        'email': {'type': 'string', 'description': 'Email address'},
                                        'color': {
                                            'type': ['string', 'null'],
                                            'description': 'Avatar color',
                                        },
                                        'profilePicture': {
                                            'type': ['string', 'null'],
                                            'description': 'Profile picture URL',
                                        },
                                        'initials': {
                                            'type': ['string', 'null'],
                                            'description': 'User initials',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'members',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Workspace or list members in ClickUp',
                                        'when_to_use': 'Questions about team membership or access',
                                        'trigger_phrases': ['clickup member', 'workspace member', 'who has access'],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the members of this workspace?'],
                                        'search_strategy': 'Filter by list or workspace',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.members',
                    no_pagination='ClickUp GET /api/v2/task/{task_id}/member returns all members assigned to the task in a single response; no pagination cursor or offset is exposed.',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Member user ID'},
                    'username': {'type': 'string', 'description': 'Username'},
                    'email': {'type': 'string', 'description': 'Email address'},
                    'color': {
                        'type': ['string', 'null'],
                        'description': 'Avatar color',
                    },
                    'profilePicture': {
                        'type': ['string', 'null'],
                        'description': 'Profile picture URL',
                    },
                    'initials': {
                        'type': ['string', 'null'],
                        'description': 'User initials',
                    },
                },
                'x-airbyte-entity-name': 'members',
                'x-airbyte-ai-hints': {
                    'summary': 'Workspace or list members in ClickUp',
                    'when_to_use': 'Questions about team membership or access',
                    'trigger_phrases': ['clickup member', 'workspace member', 'who has access'],
                    'freshness': 'live',
                    'example_questions': ['Who are the members of this workspace?'],
                    'search_strategy': 'Filter by list or workspace',
                },
            },
            ai_hints={
                'summary': 'Workspace or list members in ClickUp',
                'when_to_use': 'Questions about team membership or access',
                'trigger_phrases': ['clickup member', 'workspace member', 'who has access'],
                'freshness': 'live',
                'example_questions': ['Who are the members of this workspace?'],
                'search_strategy': 'Filter by list or workspace',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='members',
                    target_entity='tasks',
                    foreign_key='task_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='docs',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api/v3/workspaces/{workspace_id}/docs',
                    action=Action.LIST,
                    description='Search for docs in a workspace',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    path_params=['workspace_id'],
                    path_params_schema={
                        'workspace_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'docs': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Doc ID'},
                                        'name': {'type': 'string', 'description': 'Doc name'},
                                        'type': {
                                            'type': ['integer', 'null'],
                                            'description': 'Doc type',
                                        },
                                        'parent': {
                                            'type': ['object', 'null'],
                                            'description': 'Parent reference',
                                        },
                                        'creator': {
                                            'type': ['integer', 'null'],
                                            'description': 'Creator user ID',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the doc is deleted',
                                        },
                                        'public': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the doc is public',
                                        },
                                        'date_created': {
                                            'type': ['integer', 'null'],
                                            'description': 'Created date (Unix ms)',
                                        },
                                        'date_updated': {
                                            'type': ['integer', 'null'],
                                            'description': 'Last updated date (Unix ms)',
                                        },
                                        'workspace_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Workspace ID',
                                        },
                                        'content': {
                                            'type': ['string', 'null'],
                                            'description': 'Doc content',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'docs',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'ClickUp Docs — documents and wiki pages',
                                        'when_to_use': 'Questions about documentation or wiki content in ClickUp',
                                        'trigger_phrases': ['clickup doc', 'document', 'wiki page'],
                                        'freshness': 'live',
                                        'example_questions': ['Find a document in ClickUp', 'What docs are in this space?'],
                                        'search_strategy': 'Search by name or content',
                                    },
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for pagination to the next page of results',
                            },
                        },
                    },
                    record_extractor='$.docs',
                    meta_extractor={'next_cursor': '$.next_cursor'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v3/workspaces/{workspace_id}/docs/{doc_id}',
                    action=Action.GET,
                    description='Fetch a single doc by ID',
                    path_params=['workspace_id', 'doc_id'],
                    path_params_schema={
                        'workspace_id': {'type': 'string', 'required': True},
                        'doc_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Doc ID'},
                            'name': {'type': 'string', 'description': 'Doc name'},
                            'type': {
                                'type': ['integer', 'null'],
                                'description': 'Doc type',
                            },
                            'parent': {
                                'type': ['object', 'null'],
                                'description': 'Parent reference',
                            },
                            'creator': {
                                'type': ['integer', 'null'],
                                'description': 'Creator user ID',
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the doc is deleted',
                            },
                            'public': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the doc is public',
                            },
                            'date_created': {
                                'type': ['integer', 'null'],
                                'description': 'Created date (Unix ms)',
                            },
                            'date_updated': {
                                'type': ['integer', 'null'],
                                'description': 'Last updated date (Unix ms)',
                            },
                            'workspace_id': {
                                'type': ['integer', 'null'],
                                'description': 'Workspace ID',
                            },
                            'content': {
                                'type': ['string', 'null'],
                                'description': 'Doc content',
                            },
                        },
                        'x-airbyte-entity-name': 'docs',
                        'x-airbyte-ai-hints': {
                            'summary': 'ClickUp Docs — documents and wiki pages',
                            'when_to_use': 'Questions about documentation or wiki content in ClickUp',
                            'trigger_phrases': ['clickup doc', 'document', 'wiki page'],
                            'freshness': 'live',
                            'example_questions': ['Find a document in ClickUp', 'What docs are in this space?'],
                            'search_strategy': 'Search by name or content',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Doc ID'},
                    'name': {'type': 'string', 'description': 'Doc name'},
                    'type': {
                        'type': ['integer', 'null'],
                        'description': 'Doc type',
                    },
                    'parent': {
                        'type': ['object', 'null'],
                        'description': 'Parent reference',
                    },
                    'creator': {
                        'type': ['integer', 'null'],
                        'description': 'Creator user ID',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the doc is deleted',
                    },
                    'public': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the doc is public',
                    },
                    'date_created': {
                        'type': ['integer', 'null'],
                        'description': 'Created date (Unix ms)',
                    },
                    'date_updated': {
                        'type': ['integer', 'null'],
                        'description': 'Last updated date (Unix ms)',
                    },
                    'workspace_id': {
                        'type': ['integer', 'null'],
                        'description': 'Workspace ID',
                    },
                    'content': {
                        'type': ['string', 'null'],
                        'description': 'Doc content',
                    },
                },
                'x-airbyte-entity-name': 'docs',
                'x-airbyte-ai-hints': {
                    'summary': 'ClickUp Docs — documents and wiki pages',
                    'when_to_use': 'Questions about documentation or wiki content in ClickUp',
                    'trigger_phrases': ['clickup doc', 'document', 'wiki page'],
                    'freshness': 'live',
                    'example_questions': ['Find a document in ClickUp', 'What docs are in this space?'],
                    'search_strategy': 'Search by name or content',
                },
            },
            ai_hints={
                'summary': 'ClickUp Docs — documents and wiki pages',
                'when_to_use': 'Questions about documentation or wiki content in ClickUp',
                'trigger_phrases': ['clickup doc', 'document', 'wiki page'],
                'freshness': 'live',
                'example_questions': ['Find a document in ClickUp', 'What docs are in this space?'],
                'search_strategy': 'Search by name or content',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='docs',
                    target_entity='teams',
                    foreign_key='workspace_id',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='user',
                suggested=True,
                x_airbyte_name='user',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique identifier for the user',
                    ),
                    CacheFieldConfig(
                        name='username',
                        type=['null', 'string'],
                        description='Display name of the user',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='teams',
                suggested=True,
                x_airbyte_name='team',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the team (workspace)',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the team',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='spaces',
                suggested=True,
                x_airbyte_name='space',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the space',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the space',
                    ),
                    CacheFieldConfig(
                        name='private',
                        type=['null', 'boolean'],
                        description='Whether the space is private',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='folders',
                suggested=True,
                x_airbyte_name='folder',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the folder',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the folder',
                    ),
                    CacheFieldConfig(
                        name='hidden',
                        type=['null', 'boolean'],
                        description='Whether the folder is hidden from the sidebar',
                    ),
                    CacheFieldConfig(
                        name='task_count',
                        type=['null', 'string'],
                        description='Number of tasks contained in the folder',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='lists',
                suggested=True,
                x_airbyte_name='list',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the list',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the list',
                    ),
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Whether the list has been archived',
                    ),
                    CacheFieldConfig(
                        name='due_date',
                        type=['null', 'string'],
                        description='Due date for the list, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='start_date',
                        type=['null', 'string'],
                        description='Start date for the list, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='priority',
                        type=['null', 'string'],
                        description='Priority assigned to the list',
                    ),
                    CacheFieldConfig(
                        name='task_count',
                        type=['null', 'integer'],
                        description='Number of tasks contained in the list',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='tasks',
                suggested=True,
                x_airbyte_name='task',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the task',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the task',
                    ),
                    CacheFieldConfig(
                        name='date_created',
                        type=['null', 'string'],
                        description='Creation timestamp of the task, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='date_updated',
                        type=['null', 'string'],
                        description='Last update timestamp of the task, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='date_closed',
                        type=['null', 'string'],
                        description='Timestamp when the task was closed, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='due_date',
                        type=['null', 'string'],
                        description='Due date for the task, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='start_date',
                        type=['null', 'string'],
                        description='Start date for the task, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['null', 'string'],
                        description='ID of the parent task, if this task is a subtask',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['null', 'string'],
                        description='Permalink URL to view the task in ClickUp',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='comments',
                suggested=True,
                x_airbyte_name='list_comments',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the comment',
                    ),
                    CacheFieldConfig(
                        name='comment_text',
                        type=['null', 'string'],
                        description='Plain-text content of the comment',
                    ),
                    CacheFieldConfig(
                        name='date',
                        type=['null', 'string'],
                        description='Timestamp when the comment was posted, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='reply_count',
                        type=['null', 'number'],
                        description='Number of replies on the comment',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='goals',
                suggested=True,
                x_airbyte_name='team_goals',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the goal',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the goal',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['null', 'string'],
                        description='Description of the goal',
                    ),
                    CacheFieldConfig(
                        name='archived',
                        type=['null', 'boolean'],
                        description='Whether the goal has been archived',
                    ),
                    CacheFieldConfig(
                        name='pinned',
                        type=['null', 'boolean'],
                        description='Whether the goal is pinned to the top of the list',
                    ),
                    CacheFieldConfig(
                        name='private',
                        type=['null', 'boolean'],
                        description='Whether the goal is private to its owners',
                    ),
                    CacheFieldConfig(
                        name='date_created',
                        type=['null', 'string'],
                        description='Creation timestamp of the goal, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='due_date',
                        type=['null', 'string'],
                        description='Due date for the goal, in ClickUp timestamp format',
                    ),
                    CacheFieldConfig(
                        name='percent_completed',
                        type=['null', 'number'],
                        description='Completion percentage of the goal, between 0 and 100',
                    ),
                    CacheFieldConfig(
                        name='team_id',
                        type=['null', 'string'],
                        description='Identifier of the team that owns the goal',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='time_tracking',
                suggested=True,
                x_airbyte_name='time_tracking',
                fields=[
                    CacheFieldConfig(
                        name='time',
                        type=['number', 'null'],
                        description='Total tracked time in milliseconds',
                    ),
                    CacheFieldConfig(
                        name='user',
                        type=['object', 'null'],
                        description='User who tracked the time',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'user': ['id', 'username'],
        'teams': ['id', 'name'],
        'spaces': ['id', 'name', 'private'],
        'folders': [
            'id',
            'name',
            'hidden',
            'task_count',
        ],
        'lists': [
            'id',
            'name',
            'archived',
            'due_date',
            'start_date',
            'priority',
            'task_count',
        ],
        'tasks': [
            'id',
            'name',
            'date_created',
            'date_updated',
            'date_closed',
            'due_date',
            'start_date',
            'parent',
            'url',
        ],
        'comments': [
            'id',
            'comment_text',
            'date',
            'reply_count',
        ],
        'goals': [
            'id',
            'name',
            'description',
            'archived',
            'pinned',
            'private',
            'date_created',
            'due_date',
            'percent_completed',
            'team_id',
        ],
        'time_tracking': ['time', 'user'],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all workspaces I have access to',
            'Show me the spaces in my workspace',
            'List the folders in a space',
            'Show me the lists in a folder',
            'Get the tasks in a list',
            'Get details for a specific task',
            "Search for tasks containing 'bug' across my workspace",
            'Find all urgent priority tasks in my workspace',
            'Show me tasks assigned to a specific user',
            'List comments on a task',
            'Get threaded replies on a comment',
            'Create a comment on a task',
            'Update a comment to mark it resolved',
            'List all goals in my workspace',
            'Get details for a specific goal',
            'Show me all workspace-level views',
            'Get tasks matching a saved view',
            'List time entries for my workspace this week',
            'Get details for a specific time entry',
            'Show me the members assigned to a task',
            'List all docs in my workspace',
            'Get details for a specific doc',
        ],
        context_store_search=[
            'What tasks are overdue in my workspace?',
            'Which tasks were updated in the last 24 hours?',
            'Show me all high-priority tasks across all projects',
            'How much time has been tracked this week?',
            'What are the most commented tasks?',
        ],
        search=[
            'What tasks are overdue in my workspace?',
            'Which tasks were updated in the last 24 hours?',
            'Show me all high-priority tasks across all projects',
            'How much time has been tracked this week?',
            'What are the most commented tasks?',
        ],
        unsupported=['Delete a task', 'Delete a comment', 'Delete a goal'],
    ),
)