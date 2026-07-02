"""
Connector model for linear.

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
    CacheConfig,
    CacheEntityConfig,
    CacheFieldConfig,
    EnrichmentConfig,
    EnrichmentMatch,
    EnrichmentProjection,
    EntityRelationshipConfig,
    SemanticEmbedding,
    SemanticMetadataField,
    SemanticSample,
    SemanticSampling,
    SemanticSearchConfig,
    SemanticWindowing,
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

LinearConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('1c5d8316-ed42-4473-8fbc-2626f03f070c'),
    name='linear',
    version='0.1.19',
    base_url='https://api.linear.app',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='linearOAuth',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://api.linear.app/oauth/token',
                    'auth_style': 'body',
                    'body_format': 'form',
                },
                user_config_spec=AuthConfigSpec(
                    title='OAuth2',
                    type='object',
                    required=['client_id', 'client_secret', 'refresh_token'],
                    properties={
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='Your Linear OAuth2 application client ID',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='Your Linear OAuth2 application client secret',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='Your Linear OAuth2 refresh token',
                        ),
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='Your Linear OAuth2 access token (optional if refresh_token is provided)',
                        ),
                    },
                    auth_mapping={
                        'client_id': '${client_id}',
                        'client_secret': '${client_secret}',
                        'refresh_token': '${refresh_token}',
                        'access_token': '${access_token}',
                    },
                    replication_auth_key_mapping={
                        'credentials.client_id': 'client_id',
                        'credentials.client_secret': 'client_secret',
                        'credentials.refresh_token': 'refresh_token',
                    },
                    replication_auth_key_constants={'credentials.auth_type': 'OAuth2.0'},
                ),
                untested=True,
            ),
            AuthOption(
                scheme_name='apiKeyAuth',
                type=AuthType.API_KEY,
                config={'header': 'Authorization', 'in': 'header'},
                user_config_spec=AuthConfigSpec(
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
                    replication_auth_key_mapping={'credentials.api_key': 'api_key'},
                    replication_auth_key_constants={'credentials.auth_type': 'API Key'},
                ),
            ),
        ],
    ),
    entities=[
        EntityDefinition(
            name='issues',
            stream_name='issues',
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
                            'minimum': 1,
                            'maximum': 250,
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
                                                                        'id': {'type': 'string', 'description': 'Workflow state UUID for status update operations'},
                                                                        'name': {'type': 'string'},
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Issue workflow state with ID for status transitions',
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
                                                                        'id': {'type': 'string', 'description': 'Unique user identifier (UUID) for assignment operations'},
                                                                        'name': {'type': 'string'},
                                                                        'email': {'type': 'string'},
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Assigned user with ID for reassignment workflows',
                                                        },
                                                        'team': {
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
                                                            'description': 'Team the issue belongs to',
                                                        },
                                                        'project': {
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
                                                            'description': 'Project the issue belongs to',
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
                                                    'x-airbyte-stream-name': 'issues',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Engineering issues, bugs, feature requests, and feedback intake items',
                                                        'when_to_use': 'Engineering, bug, or roadmap questions about tracked issues',
                                                        'trigger_phrases': [
                                                            'is there a ticket',
                                                            'known bug',
                                                            'feature request',
                                                            'Linear issue',
                                                            'engineering status',
                                                        ],
                                                        'freshness': 'live',
                                                        'example_questions': ['Is there a ticket for the OAuth issue?', "What's the status of the API rate limiting feature?", 'Show me high-priority bugs assigned to the team'],
                                                        'search_strategy': 'Search across both title and description for best results (use OR filter)',
                                                    },
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
                        'query': 'query($first: Int, $after: String) { issues(first: $first, after: $after) { nodes { id title description state { id name } priority assignee { id name email } team { id name } project { id name } createdAt updatedAt } pageInfo { hasNextPage endCursor } } }',
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
                                                            'id': {'type': 'string', 'description': 'Workflow state UUID for status update operations'},
                                                            'name': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Issue workflow state with ID for status transitions',
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
                                                            'id': {'type': 'string', 'description': 'Unique user identifier (UUID) for assignment operations'},
                                                            'name': {'type': 'string'},
                                                            'email': {'type': 'string'},
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'Assigned user with ID for reassignment workflows',
                                            },
                                            'team': {
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
                                                'description': 'Team the issue belongs to',
                                            },
                                            'project': {
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
                                                'description': 'Project the issue belongs to',
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
                                        'x-airbyte-stream-name': 'issues',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Engineering issues, bugs, feature requests, and feedback intake items',
                                            'when_to_use': 'Engineering, bug, or roadmap questions about tracked issues',
                                            'trigger_phrases': [
                                                'is there a ticket',
                                                'known bug',
                                                'feature request',
                                                'Linear issue',
                                                'engineering status',
                                            ],
                                            'freshness': 'live',
                                            'example_questions': ['Is there a ticket for the OAuth issue?', "What's the status of the API rate limiting feature?", 'Show me high-priority bugs assigned to the team'],
                                            'search_strategy': 'Search across both title and description for best results (use OR filter)',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query($id: String!) { issue(id: $id) { id title description state { id name } priority assignee { id name email } team { id name } project { id name } createdAt updatedAt } }',
                        'variables': {'id': '{{ id }}'},
                    },
                    record_extractor='$.data.issue',
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
                                                    'project': {
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
                                                        'description': 'Project the issue belongs to',
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
                        'query': 'mutation($teamId: String!, $title: String!, $description: String, $stateId: String, $priority: Int, $projectId: String) { issueCreate(input: { teamId: $teamId, title: $title, description: $description, stateId: $stateId, priority: $priority, projectId: $projectId }) { success issue { id title description state { id name } priority assignee { id name email } project { id name } createdAt updatedAt } } }',
                        'variables': {
                            'teamId': '{{ teamId }}',
                            'title': '{{ title }}',
                            'description': '{{ description }}',
                            'stateId': '{{ stateId }}',
                            'priority': '{{ priority }}',
                            'projectId': '{{ projectId }}',
                        },
                    },
                    record_extractor='$.data.issueCreate',
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
                                                    'project': {
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
                                                        'description': 'Project the issue belongs to',
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
                        'query': 'mutation($id: String!, $title: String, $description: String, $stateId: String, $priority: Int, $assigneeId: String, $projectId: String) { issueUpdate(id: $id, input: { title: $title, description: $description, stateId: $stateId, priority: $priority, assigneeId: $assigneeId, projectId: $projectId }) { success issue { id title description state { id name } priority assignee { id name email } project { id name } createdAt updatedAt } } }',
                        'variables': {
                            'id': '{{ id }}',
                            'title': '{{ title }}',
                            'description': '{{ description }}',
                            'stateId': '{{ stateId }}',
                            'priority': '{{ priority }}',
                            'assigneeId': '{{ assigneeId }}',
                            'projectId': '{{ projectId }}',
                        },
                        'nullable_variables': ['assigneeId', 'projectId'],
                    },
                    record_extractor='$.data.issueUpdate',
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
                                    'id': {'type': 'string', 'description': 'Workflow state UUID for status update operations'},
                                    'name': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Issue workflow state with ID for status transitions',
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
                                    'id': {'type': 'string', 'description': 'Unique user identifier (UUID) for assignment operations'},
                                    'name': {'type': 'string'},
                                    'email': {'type': 'string'},
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Assigned user with ID for reassignment workflows',
                    },
                    'team': {
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
                        'description': 'Team the issue belongs to',
                    },
                    'project': {
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
                        'description': 'Project the issue belongs to',
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
                'x-airbyte-stream-name': 'issues',
                'x-airbyte-ai-hints': {
                    'summary': 'Engineering issues, bugs, feature requests, and feedback intake items',
                    'when_to_use': 'Engineering, bug, or roadmap questions about tracked issues',
                    'trigger_phrases': [
                        'is there a ticket',
                        'known bug',
                        'feature request',
                        'Linear issue',
                        'engineering status',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Is there a ticket for the OAuth issue?', "What's the status of the API rate limiting feature?", 'Show me high-priority bugs assigned to the team'],
                    'search_strategy': 'Search across both title and description for best results (use OR filter)',
                },
            },
            ai_hints={
                'summary': 'Engineering issues, bugs, feature requests, and feedback intake items',
                'when_to_use': 'Engineering, bug, or roadmap questions about tracked issues',
                'trigger_phrases': [
                    'is there a ticket',
                    'known bug',
                    'feature request',
                    'Linear issue',
                    'engineering status',
                ],
                'freshness': 'live',
                'example_questions': ['Is there a ticket for the OAuth issue?', "What's the status of the API rate limiting feature?", 'Show me high-priority bugs assigned to the team'],
                'search_strategy': 'Search across both title and description for best results (use OR filter)',
            },
        ),
        EntityDefinition(
            name='projects',
            stream_name='projects',
            actions=[
                Action.LIST,
                Action.GET,
                Action.CREATE,
                Action.UPDATE,
            ],
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
                            'minimum': 1,
                            'maximum': 250,
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
                                                    'x-airbyte-stream-name': 'projects',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Linear projects grouping issues by initiative or milestone',
                                                        'when_to_use': 'Questions about project progress, milestones, or initiative status',
                                                        'trigger_phrases': [
                                                            'linear project',
                                                            'project status',
                                                            'milestone',
                                                            'initiative',
                                                        ],
                                                        'freshness': 'live',
                                                        'example_questions': ['What Linear projects are in progress?', 'Show project status'],
                                                        'search_strategy': 'Search by name',
                                                    },
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
                                        'x-airbyte-stream-name': 'projects',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Linear projects grouping issues by initiative or milestone',
                                            'when_to_use': 'Questions about project progress, milestones, or initiative status',
                                            'trigger_phrases': [
                                                'linear project',
                                                'project status',
                                                'milestone',
                                                'initiative',
                                            ],
                                            'freshness': 'live',
                                            'example_questions': ['What Linear projects are in progress?', 'Show project status'],
                                            'search_strategy': 'Search by name',
                                        },
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
                    record_extractor='$.data.project',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/graphql:createProject',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.CREATE,
                    description='Create a new project via GraphQL mutation',
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'createProject',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for project creation',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'projectCreate': {
                                        'type': 'object',
                                        'description': 'Project mutation result',
                                        'properties': {
                                            'success': {'type': 'boolean', 'description': 'Whether the mutation was successful'},
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
                                                'x-airbyte-stream-name': 'projects',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Linear projects grouping issues by initiative or milestone',
                                                    'when_to_use': 'Questions about project progress, milestones, or initiative status',
                                                    'trigger_phrases': [
                                                        'linear project',
                                                        'project status',
                                                        'milestone',
                                                        'initiative',
                                                    ],
                                                    'freshness': 'live',
                                                    'example_questions': ['What Linear projects are in progress?', 'Show project status'],
                                                    'search_strategy': 'Search by name',
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
                        'query': 'mutation($name: String!, $teamIds: [String!]!, $description: String, $state: String, $startDate: TimelessDate, $targetDate: TimelessDate, $leadId: String) { projectCreate(input: { name: $name, teamIds: $teamIds, description: $description, state: $state, startDate: $startDate, targetDate: $targetDate, leadId: $leadId }) { success project { id name description state startDate targetDate lead { name email } createdAt updatedAt } } }',
                        'variables': {
                            'name': '{{ name }}',
                            'teamIds': '{{ teamIds }}',
                            'description': '{{ description }}',
                            'state': '{{ state }}',
                            'startDate': '{{ startDate }}',
                            'targetDate': '{{ targetDate }}',
                            'leadId': '{{ leadId }}',
                        },
                    },
                    record_extractor='$.data.projectCreate',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/graphql:updateProject',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.UPDATE,
                    description='Update an existing project via GraphQL mutation. All fields except id are optional for partial updates.\nUse this to rename projects, change descriptions, update dates, or change the project state.\n',
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'updateProject',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for project update',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'projectUpdate': {
                                        'type': 'object',
                                        'description': 'Project mutation result',
                                        'properties': {
                                            'success': {'type': 'boolean', 'description': 'Whether the mutation was successful'},
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
                                                'x-airbyte-stream-name': 'projects',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Linear projects grouping issues by initiative or milestone',
                                                    'when_to_use': 'Questions about project progress, milestones, or initiative status',
                                                    'trigger_phrases': [
                                                        'linear project',
                                                        'project status',
                                                        'milestone',
                                                        'initiative',
                                                    ],
                                                    'freshness': 'live',
                                                    'example_questions': ['What Linear projects are in progress?', 'Show project status'],
                                                    'search_strategy': 'Search by name',
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
                        'query': 'mutation($id: String!, $name: String, $description: String, $state: String, $startDate: TimelessDate, $targetDate: TimelessDate, $leadId: String) { projectUpdate(id: $id, input: { name: $name, description: $description, state: $state, startDate: $startDate, targetDate: $targetDate, leadId: $leadId }) { success project { id name description state startDate targetDate lead { name email } createdAt updatedAt } } }',
                        'variables': {
                            'id': '{{ id }}',
                            'name': '{{ name }}',
                            'description': '{{ description }}',
                            'state': '{{ state }}',
                            'startDate': '{{ startDate }}',
                            'targetDate': '{{ targetDate }}',
                            'leadId': '{{ leadId }}',
                        },
                        'nullable_variables': ['leadId', 'startDate', 'targetDate'],
                    },
                    record_extractor='$.data.projectUpdate',
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
                'x-airbyte-stream-name': 'projects',
                'x-airbyte-ai-hints': {
                    'summary': 'Linear projects grouping issues by initiative or milestone',
                    'when_to_use': 'Questions about project progress, milestones, or initiative status',
                    'trigger_phrases': [
                        'linear project',
                        'project status',
                        'milestone',
                        'initiative',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What Linear projects are in progress?', 'Show project status'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Linear projects grouping issues by initiative or milestone',
                'when_to_use': 'Questions about project progress, milestones, or initiative status',
                'trigger_phrases': [
                    'linear project',
                    'project status',
                    'milestone',
                    'initiative',
                ],
                'freshness': 'live',
                'example_questions': ['What Linear projects are in progress?', 'Show project status'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='teams',
            stream_name='teams',
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
                            'minimum': 1,
                            'maximum': 250,
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
                                                    'x-airbyte-stream-name': 'teams',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Linear teams with workflow configuration and membership',
                                                        'when_to_use': 'Questions about team structure or workflow settings',
                                                        'trigger_phrases': ['linear team', 'which team', 'team members'],
                                                        'freshness': 'live',
                                                        'example_questions': ['What teams are in Linear?'],
                                                        'search_strategy': 'Search by name or key',
                                                    },
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
                                        'x-airbyte-stream-name': 'teams',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Linear teams with workflow configuration and membership',
                                            'when_to_use': 'Questions about team structure or workflow settings',
                                            'trigger_phrases': ['linear team', 'which team', 'team members'],
                                            'freshness': 'live',
                                            'example_questions': ['What teams are in Linear?'],
                                            'search_strategy': 'Search by name or key',
                                        },
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
                    record_extractor='$.data.team',
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
                'x-airbyte-stream-name': 'teams',
                'x-airbyte-ai-hints': {
                    'summary': 'Linear teams with workflow configuration and membership',
                    'when_to_use': 'Questions about team structure or workflow settings',
                    'trigger_phrases': ['linear team', 'which team', 'team members'],
                    'freshness': 'live',
                    'example_questions': ['What teams are in Linear?'],
                    'search_strategy': 'Search by name or key',
                },
            },
            ai_hints={
                'summary': 'Linear teams with workflow configuration and membership',
                'when_to_use': 'Questions about team structure or workflow settings',
                'trigger_phrases': ['linear team', 'which team', 'team members'],
                'freshness': 'live',
                'example_questions': ['What teams are in Linear?'],
                'search_strategy': 'Search by name or key',
            },
        ),
        EntityDefinition(
            name='workflow_states',
            stream_name='workflow_states',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:listWorkflowStates',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns workflow states for a team via GraphQL, including name and UUID for status transitions',
                    query_params=['first', 'after'],
                    query_params_schema={
                        'first': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 250,
                        },
                        'after': {'type': 'string', 'required': False},
                    },
                    header_params=['x-apollo-operation-name'],
                    header_params_schema={
                        'x-apollo-operation-name': {
                            'type': 'string',
                            'required': True,
                            'default': 'listWorkflowStates',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'GraphQL response for workflow states list',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'workflowStates': {
                                        'type': 'object',
                                        'properties': {
                                            'nodes': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'description': "Linear workflow state object representing a status in a team's workflow",
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'Unique workflow state identifier (UUID) used for issue status transitions'},
                                                        'name': {'type': 'string', 'description': 'Workflow state name (e.g., Backlog, In Progress, Done)'},
                                                        'type': {'type': 'string', 'description': 'State type category (triage, backlog, unstarted, started, completed, cancelled)'},
                                                        'position': {
                                                            'oneOf': [
                                                                {'type': 'number'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'Display position order',
                                                        },
                                                        'color': {
                                                            'oneOf': [
                                                                {'type': 'string'},
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'State color hex code',
                                                        },
                                                        'team': {
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
                                                            'description': 'Team this workflow state belongs to',
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
                                                    'required': ['id', 'name', 'type'],
                                                    'x-airbyte-entity-name': 'workflow_states',
                                                    'x-airbyte-stream-name': 'workflow_states',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Workflow states (statuses) configured for Linear teams',
                                                        'when_to_use': 'Questions about issue statuses or workflow configuration',
                                                        'trigger_phrases': ['workflow state', 'issue status', 'status definition'],
                                                        'freshness': 'static',
                                                        'example_questions': ['What statuses are available for issues?'],
                                                        'search_strategy': 'Filter by team',
                                                    },
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
                        'query': 'query($first: Int, $after: String) { workflowStates(first: $first, after: $after) { nodes { id name type position color team { id name } createdAt updatedAt } pageInfo { hasNextPage endCursor } } }',
                        'variables': {'first': '{{ first }}', 'after': '{{ after }}'},
                    },
                    record_extractor='$.data.workflowStates.nodes',
                    meta_extractor={'hasNextPage': '$.data.workflowStates.pageInfo.hasNextPage', 'endCursor': '$.data.workflowStates.pageInfo.endCursor'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': "Linear workflow state object representing a status in a team's workflow",
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique workflow state identifier (UUID) used for issue status transitions'},
                    'name': {'type': 'string', 'description': 'Workflow state name (e.g., Backlog, In Progress, Done)'},
                    'type': {'type': 'string', 'description': 'State type category (triage, backlog, unstarted, started, completed, cancelled)'},
                    'position': {
                        'oneOf': [
                            {'type': 'number'},
                            {'type': 'null'},
                        ],
                        'description': 'Display position order',
                    },
                    'color': {
                        'oneOf': [
                            {'type': 'string'},
                            {'type': 'null'},
                        ],
                        'description': 'State color hex code',
                    },
                    'team': {
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
                        'description': 'Team this workflow state belongs to',
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
                'required': ['id', 'name', 'type'],
                'x-airbyte-entity-name': 'workflow_states',
                'x-airbyte-stream-name': 'workflow_states',
                'x-airbyte-ai-hints': {
                    'summary': 'Workflow states (statuses) configured for Linear teams',
                    'when_to_use': 'Questions about issue statuses or workflow configuration',
                    'trigger_phrases': ['workflow state', 'issue status', 'status definition'],
                    'freshness': 'static',
                    'example_questions': ['What statuses are available for issues?'],
                    'search_strategy': 'Filter by team',
                },
            },
            ai_hints={
                'summary': 'Workflow states (statuses) configured for Linear teams',
                'when_to_use': 'Questions about issue statuses or workflow configuration',
                'trigger_phrases': ['workflow state', 'issue status', 'status definition'],
                'freshness': 'static',
                'example_questions': ['What statuses are available for issues?'],
                'search_strategy': 'Filter by team',
            },
        ),
        EntityDefinition(
            name='users',
            stream_name='users',
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
                            'minimum': 1,
                            'maximum': 250,
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
                                                    'x-airbyte-stream-name': 'users',
                                                    'x-airbyte-ai-hints': {
                                                        'summary': 'Linear users with display name, email, and role',
                                                        'when_to_use': 'Looking up team members in Linear',
                                                        'trigger_phrases': ['linear user', 'who is', 'team member'],
                                                        'freshness': 'live',
                                                        'example_questions': ['Find a user in Linear'],
                                                        'search_strategy': 'Search by name or email',
                                                    },
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
                    record_extractor='$.data.users.nodes',
                    meta_extractor={'hasNextPage': '$.data.users.pageInfo.hasNextPage', 'endCursor': '$.data.users.pageInfo.endCursor'},
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
                                        'x-airbyte-stream-name': 'users',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Linear users with display name, email, and role',
                                            'when_to_use': 'Looking up team members in Linear',
                                            'trigger_phrases': ['linear user', 'who is', 'team member'],
                                            'freshness': 'live',
                                            'example_questions': ['Find a user in Linear'],
                                            'search_strategy': 'Search by name or email',
                                        },
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
                    record_extractor='$.data.user',
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
                'x-airbyte-stream-name': 'users',
                'x-airbyte-ai-hints': {
                    'summary': 'Linear users with display name, email, and role',
                    'when_to_use': 'Looking up team members in Linear',
                    'trigger_phrases': ['linear user', 'who is', 'team member'],
                    'freshness': 'live',
                    'example_questions': ['Find a user in Linear'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Linear users with display name, email, and role',
                'when_to_use': 'Looking up team members in Linear',
                'trigger_phrases': ['linear user', 'who is', 'team member'],
                'freshness': 'live',
                'example_questions': ['Find a user in Linear'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='comments',
            stream_name='comments',
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
                            'minimum': 1,
                            'maximum': 250,
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
                                                            'x-airbyte-stream-name': 'comments',
                                                            'x-airbyte-ai-hints': {
                                                                'summary': 'Comments on Linear issues',
                                                                'when_to_use': 'Looking for discussion or updates on specific issues',
                                                                'trigger_phrases': ['linear comment', 'issue comment', 'issue discussion'],
                                                                'freshness': 'live',
                                                                'example_questions': ['What comments are on this issue?'],
                                                                'search_strategy': 'Filter by issue',
                                                            },
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
                    record_extractor='$.data.issue.comments.nodes',
                    meta_extractor={'hasNextPage': '$.data.issue.comments.pageInfo.hasNextPage', 'endCursor': '$.data.issue.comments.pageInfo.endCursor'},
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
                                        'x-airbyte-stream-name': 'comments',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Comments on Linear issues',
                                            'when_to_use': 'Looking for discussion or updates on specific issues',
                                            'trigger_phrases': ['linear comment', 'issue comment', 'issue discussion'],
                                            'freshness': 'live',
                                            'example_questions': ['What comments are on this issue?'],
                                            'search_strategy': 'Filter by issue',
                                        },
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
                    record_extractor='$.data.comment',
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
                                                'x-airbyte-stream-name': 'comments',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Comments on Linear issues',
                                                    'when_to_use': 'Looking for discussion or updates on specific issues',
                                                    'trigger_phrases': ['linear comment', 'issue comment', 'issue discussion'],
                                                    'freshness': 'live',
                                                    'example_questions': ['What comments are on this issue?'],
                                                    'search_strategy': 'Filter by issue',
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
                        'query': 'mutation($issueId: String!, $body: String!) { commentCreate(input: { issueId: $issueId, body: $body }) { success comment { id body user { id name email } createdAt updatedAt } } }',
                        'variables': {'issueId': '{{ issueId }}', 'body': '{{ body }}'},
                    },
                    record_extractor='$.data.commentCreate',
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
                                                'x-airbyte-stream-name': 'comments',
                                                'x-airbyte-ai-hints': {
                                                    'summary': 'Comments on Linear issues',
                                                    'when_to_use': 'Looking for discussion or updates on specific issues',
                                                    'trigger_phrases': ['linear comment', 'issue comment', 'issue discussion'],
                                                    'freshness': 'live',
                                                    'example_questions': ['What comments are on this issue?'],
                                                    'search_strategy': 'Filter by issue',
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
                        'query': 'mutation($id: String!, $body: String!) { commentUpdate(id: $id, input: { body: $body }) { success comment { id body user { id name email } createdAt updatedAt } } }',
                        'variables': {'id': '{{ id }}', 'body': '{{ body }}'},
                    },
                    record_extractor='$.data.commentUpdate',
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
                'x-airbyte-stream-name': 'comments',
                'x-airbyte-ai-hints': {
                    'summary': 'Comments on Linear issues',
                    'when_to_use': 'Looking for discussion or updates on specific issues',
                    'trigger_phrases': ['linear comment', 'issue comment', 'issue discussion'],
                    'freshness': 'live',
                    'example_questions': ['What comments are on this issue?'],
                    'search_strategy': 'Filter by issue',
                },
            },
            ai_hints={
                'summary': 'Comments on Linear issues',
                'when_to_use': 'Looking for discussion or updates on specific issues',
                'trigger_phrases': ['linear comment', 'issue comment', 'issue discussion'],
                'freshness': 'live',
                'example_questions': ['What comments are on this issue?'],
                'search_strategy': 'Filter by issue',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='comments',
                    target_entity='issues',
                    foreign_key='issueId',
                    cardinality='many_to_one',
                ),
            ],
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='comments',
                suggested=True,
                x_airbyte_name='comments',
                fields=[
                    CacheFieldConfig(
                        name='body',
                        type=['string', 'null'],
                        description='',
                        x_airbyte_semantic_search=SemanticSearchConfig(
                            content_type='markdown',
                            samples=[
                                SemanticSample(
                                    name='comment_paragraph',
                                    windowed=True,
                                    sampling=SemanticSampling(
                                        sample_type='regex',
                                        unit_label='comment_paragraph',
                                        split_pattern='\\n\\s*\\n',
                                    ),
                                ),
                            ],
                            windowing=SemanticWindowing(
                                context_max_chars=2048,
                            ),
                            embedding=SemanticEmbedding(
                                model='text-embedding-3-small',
                            ),
                            metadata=[
                                SemanticMetadataField(
                                    name='id',
                                    path='/id',
                                ),
                                SemanticMetadataField(
                                    name='url',
                                    path='/url',
                                ),
                                SemanticMetadataField(
                                    name='issueId',
                                    path='/issueId',
                                ),
                                SemanticMetadataField(
                                    name='userId',
                                    path='/userId',
                                ),
                                SemanticMetadataField(
                                    name='createdAt',
                                    path='/createdAt',
                                ),
                            ],
                        ),
                    ),
                    CacheFieldConfig(
                        name='bodyData',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='editedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issue',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issueId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='parentCommentId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='resolvingCommentId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='resolvingUserId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='user',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='userId',
                        type=['string', 'null'],
                        description='',
                    ),
                ],
                x_airbyte_enrichment=[
                    EnrichmentConfig(
                        target='users',
                        match=[
                            EnrichmentMatch(
                                local='userId',
                                foreign='id',
                            ),
                        ],
                        project=[
                            EnrichmentProjection(
                                name='authorName',
                                from_='displayName',
                            ),
                        ],
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='issues',
                suggested=True,
                x_airbyte_name='issues',
                fields=[
                    CacheFieldConfig(
                        name='addedToCycleAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='addedToProjectAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='addedToTeamAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='assignee',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='assigneeId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='attachmentIds',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='attachments',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='branchName',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='canceledAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='completedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='creator',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='creatorId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='customerTicketCount',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycle',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['string', 'null'],
                        description='',
                        x_airbyte_semantic_search=SemanticSearchConfig(
                            content_type='markdown',
                            samples=[
                                SemanticSample(
                                    name='issue_description_paragraph',
                                    windowed=True,
                                    sampling=SemanticSampling(
                                        sample_type='regex',
                                        unit_label='issue_description_paragraph',
                                        split_pattern='\\n\\s*\\n',
                                    ),
                                ),
                            ],
                            windowing=SemanticWindowing(
                                context_max_chars=2048,
                            ),
                            embedding=SemanticEmbedding(
                                model='text-embedding-3-small',
                            ),
                            metadata=[
                                SemanticMetadataField(
                                    name='id',
                                    path='/id',
                                ),
                                SemanticMetadataField(
                                    name='url',
                                    path='/url',
                                ),
                                SemanticMetadataField(
                                    name='identifier',
                                    path='/identifier',
                                ),
                                SemanticMetadataField(
                                    name='title',
                                    path='/title',
                                ),
                                SemanticMetadataField(
                                    name='creatorId',
                                    path='/creatorId',
                                ),
                                SemanticMetadataField(
                                    name='assigneeId',
                                    path='/assigneeId',
                                ),
                                SemanticMetadataField(
                                    name='createdAt',
                                    path='/createdAt',
                                ),
                            ],
                        ),
                    ),
                    CacheFieldConfig(
                        name='descriptionState',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='dueDate',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='estimate',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='identifier',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='integrationSourceType',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='labelIds',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='labels',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='milestoneId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='number',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='parent',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='parentId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='previousIdentifiers',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='priority',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='priorityLabel',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='prioritySortOrder',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='project',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='projectId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='projectMilestone',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='reactionData',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='relationIds',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='relations',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='slaType',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='sortOrder',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='sourceCommentId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='startedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='state',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='stateId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='subIssueSortOrder',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='subscriberIds',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='subscribers',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='team',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='teamId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['string', 'null'],
                        description='',
                    ),
                ],
                x_airbyte_enrichment=[
                    EnrichmentConfig(
                        target='users',
                        match=[
                            EnrichmentMatch(
                                local='creatorId',
                                foreign='id',
                            ),
                        ],
                        project=[
                            EnrichmentProjection(
                                name='creatorName',
                                from_='displayName',
                            ),
                        ],
                    ),
                    EnrichmentConfig(
                        target='users',
                        match=[
                            EnrichmentMatch(
                                local='assigneeId',
                                foreign='id',
                            ),
                        ],
                        project=[
                            EnrichmentProjection(
                                name='assigneeName',
                                from_='displayName',
                            ),
                        ],
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='projects',
                suggested=True,
                x_airbyte_name='projects',
                fields=[
                    CacheFieldConfig(
                        name='canceledAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='color',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='completedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='completedIssueCountHistory',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='completedScopeHistory',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='content',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='contentState',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='convertedFromIssue',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='convertedFromIssueId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='creator',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='creatorId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='health',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='healthUpdatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='icon',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='inProgressScopeHistory',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issueCountHistory',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='lead',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='leadId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='priority',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='prioritySortOrder',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='progress',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='scope',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='scopeHistory',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='slugId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='sortOrder',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='startDate',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='startedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='statusId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='targetDate',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='teamIds',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='teams',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updateRemindersDay',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updateRemindersHour',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['string', 'null'],
                        description='',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='teams',
                suggested=True,
                x_airbyte_name='teams',
                fields=[
                    CacheFieldConfig(
                        name='activeCycle',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='activeCycleId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='autoArchivePeriod',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='autoClosePeriod',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='autoCloseStateId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='color',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleCalenderUrl',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleCooldownTime',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleDuration',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleIssueAutoAssignCompleted',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleIssueAutoAssignStarted',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleLockToActive',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cycleStartDay',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='cyclesEnabled',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='defaultIssueEstimate',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='defaultIssueState',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='defaultIssueStateId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='groupIssueHistory',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='icon',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='inviteHash',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issueCount',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issueEstimationAllowZero',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issueEstimationExtended',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='issueEstimationType',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='key',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='markedAsDuplicateWorkflowState',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='markedAsDuplicateWorkflowStateId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='parentTeamId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='private',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='requirePriorityToLeaveTriage',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='scimManaged',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='setIssueSortOrderOnStateChange',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='timezone',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='triageEnabled',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='triageIssueStateId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='upcomingCycleCount',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='users',
                suggested=True,
                x_airbyte_name='users',
                fields=[
                    CacheFieldConfig(
                        name='active',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='admin',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='avatarBackgroundColor',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='avatarUrl',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdIssueCount',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='displayName',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='guest',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='initials',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='inviteHash',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='isMe',
                        type=['boolean', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='lastSeen',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='teamIds',
                        type=['array', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='teams',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='timezone',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['string', 'null'],
                        description='',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='workflow_states',
                x_airbyte_name='workflow_states',
                fields=[
                    CacheFieldConfig(
                        name='color',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='description',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='inheritedFromId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['number', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='team',
                        type=['object', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='teamId',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['string', 'null'],
                        description='',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['string', 'null'],
                        description='',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
    search_field_paths={
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
    semantic_search_fields={
        'comments': {
            'body': SemanticSearchConfig(
                content_type='markdown',
                samples=[
                    SemanticSample(
                        name='comment_paragraph',
                        windowed=True,
                        sampling=SemanticSampling(
                            sample_type='regex',
                            unit_label='comment_paragraph',
                            split_pattern='\\n\\s*\\n',
                        ),
                    ),
                ],
                windowing=SemanticWindowing(
                    context_max_chars=2048,
                ),
                embedding=SemanticEmbedding(
                    model='text-embedding-3-small',
                ),
                metadata=[
                    SemanticMetadataField(
                        name='id',
                        path='/id',
                    ),
                    SemanticMetadataField(
                        name='url',
                        path='/url',
                    ),
                    SemanticMetadataField(
                        name='issueId',
                        path='/issueId',
                    ),
                    SemanticMetadataField(
                        name='userId',
                        path='/userId',
                    ),
                    SemanticMetadataField(
                        name='createdAt',
                        path='/createdAt',
                    ),
                ],
            ),
        },
        'issues': {
            'description': SemanticSearchConfig(
                content_type='markdown',
                samples=[
                    SemanticSample(
                        name='issue_description_paragraph',
                        windowed=True,
                        sampling=SemanticSampling(
                            sample_type='regex',
                            unit_label='issue_description_paragraph',
                            split_pattern='\\n\\s*\\n',
                        ),
                    ),
                ],
                windowing=SemanticWindowing(
                    context_max_chars=2048,
                ),
                embedding=SemanticEmbedding(
                    model='text-embedding-3-small',
                ),
                metadata=[
                    SemanticMetadataField(
                        name='id',
                        path='/id',
                    ),
                    SemanticMetadataField(
                        name='url',
                        path='/url',
                    ),
                    SemanticMetadataField(
                        name='identifier',
                        path='/identifier',
                    ),
                    SemanticMetadataField(
                        name='title',
                        path='/title',
                    ),
                    SemanticMetadataField(
                        name='creatorId',
                        path='/creatorId',
                    ),
                    SemanticMetadataField(
                        name='assigneeId',
                        path='/assigneeId',
                    ),
                    SemanticMetadataField(
                        name='createdAt',
                        path='/createdAt',
                    ),
                ],
            ),
        },
    },
    enrichment_configs={
        'comments': [
            EnrichmentConfig(
                target='users',
                match=[
                    EnrichmentMatch(
                        local='userId',
                        foreign='id',
                    ),
                ],
                project=[
                    EnrichmentProjection(
                        name='authorName',
                        from_='displayName',
                    ),
                ],
            ),
        ],
        'issues': [
            EnrichmentConfig(
                target='users',
                match=[
                    EnrichmentMatch(
                        local='creatorId',
                        foreign='id',
                    ),
                ],
                project=[
                    EnrichmentProjection(
                        name='creatorName',
                        from_='displayName',
                    ),
                ],
            ),
            EnrichmentConfig(
                target='users',
                match=[
                    EnrichmentMatch(
                        local='assigneeId',
                        foreign='id',
                    ),
                ],
                project=[
                    EnrichmentProjection(
                        name='assigneeName',
                        from_='displayName',
                    ),
                ],
            ),
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'Show me the open issues assigned to my team this week',
            "List out all projects I'm currently involved in",
            'List all users in my Linear workspace',
            'Who is assigned to the most recently updated issue?',
            "Create a new issue titled 'Fix login bug'",
            'Update the priority of a recent issue to urgent',
            "Change the title of a recent issue to 'Updated feature request'",
            "Add a comment to a recent issue saying 'This is ready for review'",
            "Update my most recent comment to say 'Revised feedback after testing'",
            'Create a high priority issue about API performance',
            'Assign a recent issue to a teammate',
            'Unassign the current assignee from a recent issue',
            'Reassign a recent issue from one teammate to another',
            "Create a new issue in the 'Backend Improvements' project",
            'Add a recent issue to a specific project',
            'Move an issue to a different project',
            "Create a new project called 'Q3 Platform Migration'",
            "Update the description of the 'Backend Improvements' project",
            'Change the target date of a project to next month',
            'Mark a project as started',
            "Set a project lead for the 'API Redesign' project",
        ],
        context_store_search=[
            'Analyze the workload distribution across my development team',
            'What are the top priority issues in our current sprint?',
            'Identify the most active projects in our organization right now',
            'Summarize the recent issues for {team_member} in the last two weeks',
            'Compare the issue complexity across different teams',
            'Which projects have the most unresolved issues?',
            "Give me an overview of my team's current project backlog",
        ],
        search=[
            'Analyze the workload distribution across my development team',
            'What are the top priority issues in our current sprint?',
            'Identify the most active projects in our organization right now',
            'Summarize the recent issues for {team_member} in the last two weeks',
            'Compare the issue complexity across different teams',
            'Which projects have the most unresolved issues?',
            "Give me an overview of my team's current project backlog",
        ],
        unsupported=[
            'Delete an outdated project from our workspace',
            'Schedule a sprint planning meeting',
            'Delete this issue',
            'Remove a comment from an issue',
        ],
    ),
)