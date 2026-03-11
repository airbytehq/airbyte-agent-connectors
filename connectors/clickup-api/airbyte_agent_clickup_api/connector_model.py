"""
Connector model for clickup-api.

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

ClickupApiConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('311a7a27-3fb5-4f7e-8265-5e4afe258b66'),
    name='clickup-api',
    version='0.1.2',
    base_url='https://api.clickup.com',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'Authorization', 'in': 'header'},
        user_config_spec=AirbyteAuthConfig(
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
            },
        ),
        EntityDefinition(
            name='teams',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.teams',
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
            },
        ),
        EntityDefinition(
            name='spaces',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.spaces',
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
            },
        ),
        EntityDefinition(
            name='folders',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.folders',
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
            },
        ),
        EntityDefinition(
            name='lists',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.lists',
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
            },
        ),
        EntityDefinition(
            name='tasks',
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
                                },
                            },
                            'last_page': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page of results',
                            },
                        },
                    },
                    record_extractor='$.tasks',
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
                        'statuses[]': {'type': 'array', 'required': False},
                        'assignees[]': {'type': 'array', 'required': False},
                        'tags[]': {'type': 'array', 'required': False},
                        'priority': {'type': 'integer', 'required': False},
                        'due_date_gt': {'type': 'integer', 'required': False},
                        'due_date_lt': {'type': 'integer', 'required': False},
                        'date_created_gt': {'type': 'integer', 'required': False},
                        'date_created_lt': {'type': 'integer', 'required': False},
                        'date_updated_gt': {'type': 'integer', 'required': False},
                        'date_updated_lt': {'type': 'integer', 'required': False},
                        'custom_fields': {'type': 'array', 'required': False},
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
                                },
                            },
                            'last_page': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page of results',
                            },
                        },
                    },
                    record_extractor='$.tasks',
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
            },
        ),
        EntityDefinition(
            name='comments',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.comments',
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
            },
        ),
        EntityDefinition(
            name='goals',
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
            },
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
            },
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
                                },
                            },
                            'last_page': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page of results',
                            },
                        },
                    },
                    record_extractor='$.tasks',
                    untested=True,
                ),
            },
        ),
        EntityDefinition(
            name='time_tracking',
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
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
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
            },
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
                                },
                            },
                        },
                    },
                    record_extractor='$.members',
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
            },
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
                                },
                            },
                            'next_cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for pagination to the next page of results',
                            },
                        },
                    },
                    record_extractor='$.docs',
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
            },
        ),
    ],
)