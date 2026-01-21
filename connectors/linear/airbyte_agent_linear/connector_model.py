"""
Connector model for linear.

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
from ._vendored.connector_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

LinearConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('1c5d8316-ed42-4473-8fbc-2626f03f070c'),
    name='linear',
    version='0.1.4',
    base_url='https://api.linear.app',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'Authorization', 'in': 'header'},
        user_config_spec=AirbyteAuthConfig(
            title='Linear API Key Authentication',
            description='Authenticate using your Linear API key',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Linear API key from Settings > API > Personal API keys',
                    airbyte_secret=True,
                ),
            },
            auth_mapping={'api_key': '${api_key}'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='issues',
            actions=[
                Action.LIST,
                Action.GET,
                Action.CREATE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:listIssues',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a paginated list of issues via GraphQL with pagination support',
                    query_params=['first', 'after'],
                    query_params_schema={
                        'first': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for issues list',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'issues': {
                                        'type': 'object',
                                        'properties': {
                                            'nodes': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Linear issue object',
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'Unique issue identifier'},
                                                        'title': {'type': 'string', 'description': 'Issue title'},
                                                        'description': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Issue description',
                                                        },
                                                        'state': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'name': {'type': 'string'},
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Issue state',
                                                        },
                                                        'priority': {
                                                            'oneOf': [
                                                                {'type': 'number'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Issue priority (0-4)',
                                                        },
                                                        'assignee': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'name': {'type': 'string'},
                                                                        'email': {'type': 'string'},
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Assigned user',
                                                        },
                                                        'createdAt': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Creation timestamp',
                                                        },
                                                        'updatedAt': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Last update timestamp',
                                                        },
                                                    },
                                                    'required': ['id', 'title'],
                                                    'x-airbyte-entity-name': 'issues',
                                                },
                                            },
                                            'pageInfo': {
                                                'type': 'object',
                                                'description': 'Pagination information',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean', 'description': 'Whether there are more items available'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Cursor to fetch next page',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($first: Int, $after: String) { issues(first: $first, after: $after) { nodes { id title description state { name } priority assignee { name email } createdAt updatedAt } pageInfo { hasNextPage endCursor } } }',
                        'variables': {'first': '{{ first }}', 'after': '{{ after }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:getIssue',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Get a single issue by ID via GraphQL',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for single issue',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'issue': {
                                        'type': 'object',
                                        'description': 'Linear issue object',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'Unique issue identifier'},
                                            'title': {'type': 'string', 'description': 'Issue title'},
                                            'description': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Issue description',
                                            },
                                            'state': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Issue state',
                                            },
                                            'priority': {
                                                'oneOf': [
                                                    {'type': 'number'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Issue priority (0-4)',
                                            },
                                            'assignee': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'email': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Assigned user',
                                            },
                                            'createdAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updatedAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                        },
                                        'required': ['id', 'title'],
                                        'x-airbyte-entity-name': 'issues',
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($id: String!) { issue(id: $id) { id title description state { name } priority assignee { name email } createdAt updatedAt } }',
                        'variables': {'id': '{{ id }}'},
                    },
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/graphql:createIssue',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.CREATE,
                    description='Create a new issue via GraphQL mutation',
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for issue creation',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'issueCreate': {
                                        'type': 'object',
                                        'description': 'Issue mutation result',
                                        'properties': {
                                            'success': {'type': 'boolean', 'description': 'Whether the mutation was successful'},
                                            'issue': {
                                                'type': 'object',
                                                'description': 'Issue object with state ID included',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Unique issue identifier'},
                                                    'title': {'type': 'string', 'description': 'Issue title'},
                                                    'description': {
                                                        'oneOf': [
                                                            {'type': 'string'},
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue description',
                                                    },
                                                    'state': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {'type': 'string'},
                                                                    'name': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue state with ID',
                                                    },
                                                    'priority': {
                                                        'oneOf': [
                                                            {'type': 'number'},
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue priority (0-4)',
                                                    },
                                                    'assignee': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'name': {'type': 'string'},
                                                                    'email': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Assigned user',
                                                    },
                                                    'createdAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Creation timestamp',
                                                    },
                                                    'updatedAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Last update timestamp',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'mutation($teamId: String!, $title: String!, $description: String, $stateId: String, $priority: Int) { issueCreate(input: { teamId: $teamId, title: $title, description: $description, stateId: $stateId, priority: $priority }) { success issue { id title description state { id name } priority assignee { name email } createdAt updatedAt } } }',
                        'variables': {
                            'teamId': '{{ teamId }}',
                            'title': '{{ title }}',
                            'description': '{{ description }}',
                            'stateId': '{{ stateId }}',
                            'priority': '{{ priority }}',
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/graphql:updateIssue',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.UPDATE,
                    description='Update an existing issue via GraphQL mutation. All fields except id are optional for partial updates.',
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for issue update',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'issueUpdate': {
                                        'type': 'object',
                                        'description': 'Issue mutation result',
                                        'properties': {
                                            'success': {'type': 'boolean', 'description': 'Whether the mutation was successful'},
                                            'issue': {
                                                'type': 'object',
                                                'description': 'Issue object with state ID included',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Unique issue identifier'},
                                                    'title': {'type': 'string', 'description': 'Issue title'},
                                                    'description': {
                                                        'oneOf': [
                                                            {'type': 'string'},
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue description',
                                                    },
                                                    'state': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {'type': 'string'},
                                                                    'name': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue state with ID',
                                                    },
                                                    'priority': {
                                                        'oneOf': [
                                                            {'type': 'number'},
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue priority (0-4)',
                                                    },
                                                    'assignee': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'name': {'type': 'string'},
                                                                    'email': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Assigned user',
                                                    },
                                                    'createdAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Creation timestamp',
                                                    },
                                                    'updatedAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Last update timestamp',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'mutation($id: String!, $title: String, $description: String, $stateId: String, $priority: Int) { issueUpdate(id: $id, input: { title: $title, description: $description, stateId: $stateId, priority: $priority }) { success issue { id title description state { id name } priority assignee { name email } createdAt updatedAt } } }',
                        'variables': {
                            'id': '{{ id }}',
                            'title': '{{ title }}',
                            'description': '{{ description }}',
                            'stateId': '{{ stateId }}',
                            'priority': '{{ priority }}',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Linear issue object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique issue identifier'},
                    'title': {'type': 'string', 'description': 'Issue title'},
                    'description': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'Issue description',
                    },
                    'state': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Issue state',
                    },
                    'priority': {
                        'oneOf': [
                            {'type': 'number'},
                            {'type': 'null'},
                        ],
                        'description': 'Issue priority (0-4)',
                    },
                    'assignee': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'email': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Assigned user',
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                },
                'required': ['id', 'title'],
                'x-airbyte-entity-name': 'issues',
            },
        ),
        EntityDefinition(
            name='projects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:listProjects',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a paginated list of projects via GraphQL with pagination support',
                    query_params=['first', 'after'],
                    query_params_schema={
                        'first': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for projects list',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'projects': {
                                        'type': 'object',
                                        'properties': {
                                            'nodes': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Linear project object',
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'Unique project identifier'},
                                                        'name': {'type': 'string', 'description': 'Project name'},
                                                        'description': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Project description',
                                                        },
                                                        'state': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Project state (planned, started, paused, completed, canceled)',
                                                        },
                                                        'startDate': {
                                                            'oneOf': [
                                                                {'type': 'string', 'format': 'date'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Project start date',
                                                        },
                                                        'targetDate': {
                                                            'oneOf': [
                                                                {'type': 'string', 'format': 'date'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Project target date',
                                                        },
                                                        'lead': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'name': {'type': 'string'},
                                                                        'email': {'type': 'string'},
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Project lead',
                                                        },
                                                        'createdAt': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Creation timestamp',
                                                        },
                                                        'updatedAt': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Last update timestamp',
                                                        },
                                                    },
                                                    'required': ['id', 'name'],
                                                    'x-airbyte-entity-name': 'projects',
                                                },
                                            },
                                            'pageInfo': {
                                                'type': 'object',
                                                'description': 'Pagination information',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean', 'description': 'Whether there are more items available'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Cursor to fetch next page',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($first: Int, $after: String) { projects(first: $first, after: $after) { nodes { id name description state startDate targetDate lead { name email } createdAt updatedAt } pageInfo { hasNextPage endCursor } } }',
                        'variables': {'first': '{{ first }}', 'after': '{{ after }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:getProject',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Get a single project by ID via GraphQL',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for single project',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'project': {
                                        'type': 'object',
                                        'description': 'Linear project object',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'Unique project identifier'},
                                            'name': {'type': 'string', 'description': 'Project name'},
                                            'description': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Project description',
                                            },
                                            'state': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Project state (planned, started, paused, completed, canceled)',
                                            },
                                            'startDate': {
                                                'oneOf': [
                                                    {'type': 'string', 'format': 'date'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Project start date',
                                            },
                                            'targetDate': {
                                                'oneOf': [
                                                    {'type': 'string', 'format': 'date'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Project target date',
                                            },
                                            'lead': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'email': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Project lead',
                                            },
                                            'createdAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updatedAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                        },
                                        'required': ['id', 'name'],
                                        'x-airbyte-entity-name': 'projects',
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($id: String!) { project(id: $id) { id name description state startDate targetDate lead { name email } createdAt updatedAt } }',
                        'variables': {'id': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Linear project object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique project identifier'},
                    'name': {'type': 'string', 'description': 'Project name'},
                    'description': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'Project description',
                    },
                    'state': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'Project state (planned, started, paused, completed, canceled)',
                    },
                    'startDate': {
                        'oneOf': [
                            {'type': 'string', 'format': 'date'},
                            {'type': 'null'},
                        ],
                        'description': 'Project start date',
                    },
                    'targetDate': {
                        'oneOf': [
                            {'type': 'string', 'format': 'date'},
                            {'type': 'null'},
                        ],
                        'description': 'Project target date',
                    },
                    'lead': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'email': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Project lead',
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                },
                'required': ['id', 'name'],
                'x-airbyte-entity-name': 'projects',
            },
        ),
        EntityDefinition(
            name='teams',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:listTeams',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of teams via GraphQL with pagination support',
                    query_params=['first', 'after'],
                    query_params_schema={
                        'first': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for teams list',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'teams': {
                                        'type': 'object',
                                        'properties': {
                                            'nodes': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Linear team object',
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'Unique team identifier'},
                                                        'name': {'type': 'string', 'description': 'Team name'},
                                                        'key': {'type': 'string', 'description': 'Team key (short identifier)'},
                                                        'description': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Team description',
                                                        },
                                                        'timezone': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Team timezone',
                                                        },
                                                        'createdAt': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Creation timestamp',
                                                        },
                                                        'updatedAt': {
                                                            'type': 'string',
                                                            'format': 'date-time',
                                                            'description': 'Last update timestamp',
                                                        },
                                                    },
                                                    'required': ['id', 'name', 'key'],
                                                    'x-airbyte-entity-name': 'teams',
                                                },
                                            },
                                            'pageInfo': {
                                                'type': 'object',
                                                'description': 'Pagination information',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean', 'description': 'Whether there are more items available'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Cursor to fetch next page',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($first: Int, $after: String) { teams(first: $first, after: $after) { nodes { id name key description timezone createdAt updatedAt } pageInfo { hasNextPage endCursor } } }',
                        'variables': {'first': '{{ first }}', 'after': '{{ after }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:getTeam',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Get a single team by ID via GraphQL',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for single team',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'team': {
                                        'type': 'object',
                                        'description': 'Linear team object',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'Unique team identifier'},
                                            'name': {'type': 'string', 'description': 'Team name'},
                                            'key': {'type': 'string', 'description': 'Team key (short identifier)'},
                                            'description': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Team description',
                                            },
                                            'timezone': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Team timezone',
                                            },
                                            'createdAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updatedAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                        },
                                        'required': ['id', 'name', 'key'],
                                        'x-airbyte-entity-name': 'teams',
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($id: String!) { team(id: $id) { id name key description timezone createdAt updatedAt } }',
                        'variables': {'id': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Linear team object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique team identifier'},
                    'name': {'type': 'string', 'description': 'Team name'},
                    'key': {'type': 'string', 'description': 'Team key (short identifier)'},
                    'description': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'Team description',
                    },
                    'timezone': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'Team timezone',
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                },
                'required': ['id', 'name', 'key'],
                'x-airbyte-entity-name': 'teams',
            },
        ),
        EntityDefinition(
            name='comments',
            actions=[
                Action.LIST,
                Action.GET,
                Action.CREATE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:listComments',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a paginated list of comments for an issue via GraphQL',
                    query_params=['issueId', 'first', 'after'],
                    query_params_schema={
                        'issueId': {'type': 'string', 'required': True},
                        'first': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for comments list',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'issue': {
                                        'type': 'object',
                                        'properties': {
                                            'comments': {
                                                'type': 'object',
                                                'properties': {
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'description': 'Linear comment object',
                                                            'properties': {
                                                                'id': {'type': 'string', 'description': 'Unique comment identifier'},
                                                                'body': {'type': 'string', 'description': 'Comment content in markdown'},
                                                                'user': {
                                                                    'oneOf': [
                                                                        {
                                                                            'type': 'object',
                                                                            'properties': {
                                                                                'id': {'type': 'string'},
                                                                                'name': {'type': 'string'},
                                                                                'email': {'type': 'string'},
                                                                            },
                                                                        },
                                                                        {'type': 'null'},
                                                                    ],
                                                                    'description': 'User who created the comment',
                                                                },
                                                                'issue': {
                                                                    'oneOf': [
                                                                        {
                                                                            'type': 'object',
                                                                            'properties': {
                                                                                'id': {'type': 'string'},
                                                                                'title': {'type': 'string'},
                                                                            },
                                                                        },
                                                                        {'type': 'null'},
                                                                    ],
                                                                    'description': 'Issue the comment belongs to',
                                                                },
                                                                'createdAt': {
                                                                    'type': 'string',
                                                                    'format': 'date-time',
                                                                    'description': 'Creation timestamp',
                                                                },
                                                                'updatedAt': {
                                                                    'type': 'string',
                                                                    'format': 'date-time',
                                                                    'description': 'Last update timestamp',
                                                                },
                                                            },
                                                            'required': ['id', 'body'],
                                                            'x-airbyte-entity-name': 'comments',
                                                        },
                                                    },
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'description': 'Pagination information',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean', 'description': 'Whether there are more items available'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                                'description': 'Cursor to fetch next page',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($issueId: String!, $first: Int, $after: String) { issue(id: $issueId) { comments(first: $first, after: $after) { nodes { id body user { id name email } createdAt updatedAt } pageInfo { hasNextPage endCursor } } } }',
                        'variables': {
                            'issueId': '{{ issueId }}',
                            'first': '{{ first }}',
                            'after': '{{ after }}',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:getComment',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Get a single comment by ID via GraphQL',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for single comment',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'comment': {
                                        'type': 'object',
                                        'description': 'Linear comment object',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'Unique comment identifier'},
                                            'body': {'type': 'string', 'description': 'Comment content in markdown'},
                                            'user': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'email': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'User who created the comment',
                                            },
                                            'issue': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {'type': 'string'},
                                                            'title': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Issue the comment belongs to',
                                            },
                                            'createdAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Creation timestamp',
                                            },
                                            'updatedAt': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'Last update timestamp',
                                            },
                                        },
                                        'required': ['id', 'body'],
                                        'x-airbyte-entity-name': 'comments',
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($id: String!) { comment(id: $id) { id body user { id name email } issue { id title } createdAt updatedAt } }',
                        'variables': {'id': '{{ id }}'},
                    },
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/graphql:createComment',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.CREATE,
                    description='Create a new comment on an issue via GraphQL mutation',
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for comment creation',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'commentCreate': {
                                        'type': 'object',
                                        'description': 'Comment mutation result',
                                        'properties': {
                                            'success': {'type': 'boolean', 'description': 'Whether the mutation was successful'},
                                            'comment': {
                                                'type': 'object',
                                                'description': 'Linear comment object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Unique comment identifier'},
                                                    'body': {'type': 'string', 'description': 'Comment content in markdown'},
                                                    'user': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {'type': 'string'},
                                                                    'name': {'type': 'string'},
                                                                    'email': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'User who created the comment',
                                                    },
                                                    'issue': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {'type': 'string'},
                                                                    'title': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue the comment belongs to',
                                                    },
                                                    'createdAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Creation timestamp',
                                                    },
                                                    'updatedAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Last update timestamp',
                                                    },
                                                },
                                                'required': ['id', 'body'],
                                                'x-airbyte-entity-name': 'comments',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'mutation($issueId: String!, $body: String!) { commentCreate(input: { issueId: $issueId, body: $body }) { success comment { id body user { id name email } createdAt updatedAt } } }',
                        'variables': {'issueId': '{{ issueId }}', 'body': '{{ body }}'},
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/graphql:updateComment',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.UPDATE,
                    description='Update an existing comment via GraphQL mutation',
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for comment update',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'commentUpdate': {
                                        'type': 'object',
                                        'description': 'Comment mutation result',
                                        'properties': {
                                            'success': {'type': 'boolean', 'description': 'Whether the mutation was successful'},
                                            'comment': {
                                                'type': 'object',
                                                'description': 'Linear comment object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Unique comment identifier'},
                                                    'body': {'type': 'string', 'description': 'Comment content in markdown'},
                                                    'user': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {'type': 'string'},
                                                                    'name': {'type': 'string'},
                                                                    'email': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'User who created the comment',
                                                    },
                                                    'issue': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {'type': 'string'},
                                                                    'title': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Issue the comment belongs to',
                                                    },
                                                    'createdAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Creation timestamp',
                                                    },
                                                    'updatedAt': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Last update timestamp',
                                                    },
                                                },
                                                'required': ['id', 'body'],
                                                'x-airbyte-entity-name': 'comments',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'mutation($id: String!, $body: String!) { commentUpdate(id: $id, input: { body: $body }) { success comment { id body user { id name email } createdAt updatedAt } } }',
                        'variables': {'id': '{{ id }}', 'body': '{{ body }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Linear comment object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique comment identifier'},
                    'body': {'type': 'string', 'description': 'Comment content in markdown'},
                    'user': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'email': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'User who created the comment',
                    },
                    'issue': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string'},
                                    'title': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Issue the comment belongs to',
                    },
                    'createdAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                },
                'required': ['id', 'body'],
                'x-airbyte-entity-name': 'comments',
            },
        ),
    ],
)