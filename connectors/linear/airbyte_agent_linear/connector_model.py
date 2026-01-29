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
    version='0.1.8',
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'listIssues',
                        },
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
                    record_extractor='$.data.issues.nodes',
                    meta_extractor={'hasNextPage': '$.data.issues.pageInfo.hasNextPage', 'endCursor': '$.data.issues.pageInfo.endCursor'},
                    preferred_for_check=True,
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'getIssue',
                        },
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'createIssue',
                        },
                    },
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
                                                'description': 'Issue object with state ID and assignee ID included',
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
                                                                    'id': {'type': 'string'},
                                                                    'name': {'type': 'string'},
                                                                    'email': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Assigned user with ID',
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
                    description="Update an existing issue via GraphQL mutation. All fields except id are optional for partial updates.\nTo assign a user, provide assigneeId with the user's ID (get user IDs from the users list).\nOmit assigneeId to leave the current assignee unchanged.\n",
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'updateIssue',
                        },
                    },
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
                                                'description': 'Issue object with state ID and assignee ID included',
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
                                                                    'id': {'type': 'string'},
                                                                    'name': {'type': 'string'},
                                                                    'email': {'type': 'string'},
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'Assigned user with ID',
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
                        'query': 'mutation($id: String!, $title: String, $description: String, $stateId: String, $priority: Int, $assigneeId: String) { issueUpdate(id: $id, input: { title: $title, description: $description, stateId: $stateId, priority: $priority, assigneeId: $assigneeId }) { success issue { id title description state { id name } priority assignee { id name email } createdAt updatedAt } } }',
                        'variables': {
                            'id': '{{ id }}',
                            'title': '{{ title }}',
                            'description': '{{ description }}',
                            'stateId': '{{ stateId }}',
                            'priority': '{{ priority }}',
                            'assigneeId': '{{ assigneeId }}',
                        },
                        'nullable_variables': ['assigneeId'],
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'listProjects',
                        },
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
                    record_extractor='$.data.projects.nodes',
                    meta_extractor={'hasNextPage': '$.data.projects.pageInfo.hasNextPage', 'endCursor': '$.data.projects.pageInfo.endCursor'},
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'getProject',
                        },
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'listTeams',
                        },
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
                    record_extractor='$.data.teams.nodes',
                    meta_extractor={'hasNextPage': '$.data.teams.pageInfo.hasNextPage', 'endCursor': '$.data.teams.pageInfo.endCursor'},
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'getTeam',
                        },
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
            name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:listUsers',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a paginated list of users in the organization via GraphQL',
                    query_params=['first', 'after'],
                    query_params_schema={
                        'first': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'listUsers',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for users list',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'users': {
                                        'type': 'object',
                                        'properties': {
                                            'nodes': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'Linear user object',
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'Unique user identifier'},
                                                        'name': {'type': 'string', 'description': "User's full name"},
                                                        'email': {'type': 'string', 'description': "User's email address"},
                                                        'displayName': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': "User's display name",
                                                        },
                                                        'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                                                        'admin': {'type': 'boolean', 'description': 'Whether the user is an admin'},
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
                                                    'required': ['id', 'name', 'email'],
                                                    'x-airbyte-entity-name': 'users',
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
                        'query': 'query($first: Int, $after: String) { users(first: $first, after: $after) { nodes { id name email displayName active admin createdAt updatedAt } pageInfo { hasNextPage endCursor } } }',
                        'variables': {'first': '{{ first }}', 'after': '{{ after }}'},
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:getUser',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Get a single user by ID via GraphQL',
                    query_params=['id'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'getUser',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for single user',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'user': {
                                        'type': 'object',
                                        'description': 'Linear user object',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'Unique user identifier'},
                                            'name': {'type': 'string', 'description': "User's full name"},
                                            'email': {'type': 'string', 'description': "User's email address"},
                                            'displayName': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'null'},
                                                ],
                                                'description': "User's display name",
                                            },
                                            'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                                            'admin': {'type': 'boolean', 'description': 'Whether the user is an admin'},
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
                                        'required': ['id', 'name', 'email'],
                                        'x-airbyte-entity-name': 'users',
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($id: String!) { user(id: $id) { id name email displayName active admin createdAt updatedAt } }',
                        'variables': {'id': '{{ id }}'},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Linear user object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                    'name': {'type': 'string', 'description': "User's full name"},
                    'email': {'type': 'string', 'description': "User's email address"},
                    'displayName': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': "User's display name",
                    },
                    'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                    'admin': {'type': 'boolean', 'description': 'Whether the user is an admin'},
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
                'required': ['id', 'name', 'email'],
                'x-airbyte-entity-name': 'users',
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'listComments',
                        },
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'getComment',
                        },
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'createComment',
                        },
                    },
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
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'updateComment',
                        },
                    },
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
    search_field_paths={
        'attachments': [
            'createdAt',
            'creator',
            'creatorId',
            'groupBySource',
            'id',
            'issue',
            'issueId',
            'sourceType',
            'subtitle',
            'title',
            'updatedAt',
            'url',
        ],
        'comments': [
            'body',
            'bodyData',
            'createdAt',
            'editedAt',
            'id',
            'issue',
            'issueId',
            'parent',
            'parentCommentId',
            'resolvingCommentId',
            'resolvingUserId',
            'updatedAt',
            'url',
            'user',
            'userId',
        ],
        'customer_needs': [
            'attachment',
            'attachmentId',
            'commentId',
            'createdAt',
            'creatorId',
            'customer',
            'customerId',
            'id',
            'issue',
            'issueId',
            'priority',
            'project',
            'projectId',
            'updatedAt',
        ],
        'customer_statuses': [
            'color',
            'createdAt',
            'id',
            'name',
            'position',
            'updatedAt',
        ],
        'customer_tiers': [
            'color',
            'createdAt',
            'displayName',
            'id',
            'name',
            'position',
            'updatedAt',
        ],
        'customers': [
            'approximateNeedCount',
            'createdAt',
            'domains',
            'domains[]',
            'externalIds',
            'externalIds[]',
            'id',
            'logoUrl',
            'name',
            'revenue',
            'slugId',
            'status',
            'statusId',
            'tier',
            'tierId',
            'updatedAt',
        ],
        'cycles': [
            'completedAt',
            'completedIssueCountHistory',
            'completedIssueCountHistory[]',
            'completedScopeHistory',
            'completedScopeHistory[]',
            'createdAt',
            'description',
            'endsAt',
            'id',
            'inProgressScopeHistory',
            'inProgressScopeHistory[]',
            'inheritedFromId',
            'issueCountHistory',
            'issueCountHistory[]',
            'name',
            'number',
            'progress',
            'scopeHistory',
            'scopeHistory[]',
            'startsAt',
            'team',
            'teamId',
            'uncompletedIssueIdsUponClose',
            'uncompletedIssueIdsUponClose[]',
            'uncompletedIssuesUponClose',
            'updatedAt',
        ],
        'issue_labels': [
            'color',
            'createdAt',
            'creator',
            'creatorId',
            'description',
            'id',
            'inheritedFromId',
            'isGroup',
            'name',
            'parent',
            'parentLabelId',
            'team',
            'teamId',
            'updatedAt',
        ],
        'issue_relations': [
            'createdAt',
            'id',
            'issue',
            'issueId',
            'relatedIssue',
            'relatedIssueId',
            'type',
            'updatedAt',
        ],
        'issues': [
            'addedToCycleAt',
            'addedToProjectAt',
            'addedToTeamAt',
            'assignee',
            'assigneeId',
            'attachmentIds',
            'attachmentIds[]',
            'attachments',
            'branchName',
            'canceledAt',
            'completedAt',
            'createdAt',
            'creator',
            'creatorId',
            'customerTicketCount',
            'cycle',
            'cycleId',
            'description',
            'descriptionState',
            'dueDate',
            'estimate',
            'id',
            'identifier',
            'integrationSourceType',
            'labelIds',
            'labelIds[]',
            'labels',
            'milestoneId',
            'number',
            'parent',
            'parentId',
            'previousIdentifiers',
            'previousIdentifiers[]',
            'priority',
            'priorityLabel',
            'prioritySortOrder',
            'project',
            'projectId',
            'projectMilestone',
            'reactionData',
            'reactionData[]',
            'relationIds',
            'relationIds[]',
            'relations',
            'slaType',
            'sortOrder',
            'sourceCommentId',
            'startedAt',
            'state',
            'stateId',
            'subIssueSortOrder',
            'subscriberIds',
            'subscriberIds[]',
            'subscribers',
            'team',
            'teamId',
            'title',
            'updatedAt',
            'url',
        ],
        'project_milestones': [
            'createdAt',
            'description',
            'descriptionState',
            'id',
            'name',
            'progress',
            'project',
            'projectId',
            'sortOrder',
            'status',
            'targetDate',
            'updatedAt',
        ],
        'project_statuses': [
            'color',
            'createdAt',
            'id',
            'indefinite',
            'name',
            'position',
            'type',
            'updatedAt',
        ],
        'projects': [
            'canceledAt',
            'color',
            'completedAt',
            'completedIssueCountHistory',
            'completedIssueCountHistory[]',
            'completedScopeHistory',
            'completedScopeHistory[]',
            'content',
            'contentState',
            'convertedFromIssue',
            'convertedFromIssueId',
            'createdAt',
            'creator',
            'creatorId',
            'description',
            'health',
            'healthUpdatedAt',
            'icon',
            'id',
            'inProgressScopeHistory',
            'inProgressScopeHistory[]',
            'issueCountHistory',
            'issueCountHistory[]',
            'lead',
            'leadId',
            'name',
            'priority',
            'prioritySortOrder',
            'progress',
            'scope',
            'scopeHistory',
            'scopeHistory[]',
            'slugId',
            'sortOrder',
            'startDate',
            'startedAt',
            'status',
            'statusId',
            'targetDate',
            'teamIds',
            'teamIds[]',
            'teams',
            'updateRemindersDay',
            'updateRemindersHour',
            'updatedAt',
            'url',
        ],
        'teams': [
            'activeCycle',
            'activeCycleId',
            'autoArchivePeriod',
            'autoClosePeriod',
            'autoCloseStateId',
            'color',
            'createdAt',
            'cycleCalenderUrl',
            'cycleCooldownTime',
            'cycleDuration',
            'cycleIssueAutoAssignCompleted',
            'cycleIssueAutoAssignStarted',
            'cycleLockToActive',
            'cycleStartDay',
            'cyclesEnabled',
            'defaultIssueEstimate',
            'defaultIssueState',
            'defaultIssueStateId',
            'groupIssueHistory',
            'icon',
            'id',
            'inviteHash',
            'issueCount',
            'issueEstimationAllowZero',
            'issueEstimationExtended',
            'issueEstimationType',
            'key',
            'markedAsDuplicateWorkflowState',
            'markedAsDuplicateWorkflowStateId',
            'name',
            'parentTeamId',
            'private',
            'requirePriorityToLeaveTriage',
            'scimManaged',
            'setIssueSortOrderOnStateChange',
            'timezone',
            'triageEnabled',
            'triageIssueStateId',
            'upcomingCycleCount',
            'updatedAt',
        ],
        'users': [
            'active',
            'admin',
            'avatarBackgroundColor',
            'avatarUrl',
            'createdAt',
            'createdIssueCount',
            'displayName',
            'email',
            'guest',
            'id',
            'initials',
            'inviteHash',
            'isMe',
            'lastSeen',
            'name',
            'teamIds',
            'teamIds[]',
            'teams',
            'timezone',
            'updatedAt',
            'url',
        ],
        'workflow_states': [
            'color',
            'createdAt',
            'description',
            'id',
            'inheritedFromId',
            'name',
            'position',
            'team',
            'teamId',
            'type',
            'updatedAt',
        ],
    },
)