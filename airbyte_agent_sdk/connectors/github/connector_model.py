"""
Connector model for github.

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
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from airbyte_agent_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

GithubConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('ef69ef6e-aa7f-4af1-a01d-ef775033524e'),
    name='github',
    version='0.1.18',
    base_url='https://api.github.com',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='githubOAuth',
                type=AuthType.OAUTH2,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AuthConfigSpec(
                    title='OAuth 2',
                    type='object',
                    required=['access_token'],
                    properties={
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='OAuth 2.0 access token',
                        ),
                    },
                    auth_mapping={'access_token': '${access_token}'},
                    replication_auth_key_mapping={'credentials.access_token': 'access_token'},
                    replication_auth_key_constants={'credentials.option_title': 'OAuth Credentials'},
                ),
            ),
            AuthOption(
                scheme_name='githubPAT',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AuthConfigSpec(
                    title='Personal Access Token',
                    type='object',
                    required=['token'],
                    properties={
                        'token': AuthConfigFieldSpec(
                            title='Personal Access Token',
                            description='GitHub personal access token (fine-grained or classic)',
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
            name='repositories',
            actions=[Action.GET, Action.LIST, Action.API_SEARCH],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:repositories:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific GitHub repository using GraphQL',
                    query_params=['owner', 'repo', 'fields'],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {'type': 'object', 'description': 'Repository object with selected fields'},
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetRepository($owner: String!, $name: String!) {\n  repository(owner: $owner, name: $name) {\n    {{ fields }}\n  }\n}\n',
                        'variables': {'owner': '{{ owner }}', 'name': '{{ repo }}'},
                        'default_fields': 'id name nameWithOwner description url createdAt updatedAt pushedAt forkCount stargazerCount isPrivate isFork isArchived isTemplate hasIssuesEnabled hasWikiEnabled primaryLanguage { name } licenseInfo { name spdxId } owner { login avatarUrl } defaultBranchRef { name } repositoryTopics(first: 10) { nodes { topic { name } } }',
                    },
                    record_extractor='$.data.repository',
                ),
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:repositories:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of repositories for the specified user using GraphQL',
                    query_params=[
                        'username',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'username': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'user': {
                                        'type': 'object',
                                        'properties': {
                                            'repositories': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'description': 'Array of repository results',
                                                        'items': {'type': 'object', 'description': 'Repository object with selected fields'},
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
                        'query': 'query ListRepositories($login: String!, $first: Int!, $after: String) {\n  user(login: $login) {\n    repositories(first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'login': '{{ username }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id name nameWithOwner description url createdAt updatedAt pushedAt forkCount stargazerCount isPrivate isFork isArchived isTemplate hasIssuesEnabled hasWikiEnabled primaryLanguage { name } licenseInfo { name spdxId } owner { login avatarUrl } defaultBranchRef { name } repositoryTopics(first: 10) { nodes { topic { name } } }',
                    },
                    record_extractor='$.data.user.repositories.nodes',
                    preferred_for_check=True,
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/graphql:repositories',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for GitHub repositories using GitHub\'s powerful search syntax.\nExamples: "language:python stars:>1000", "topic:machine-learning", "org:facebook is:public"\n',
                    query_params=[
                        'query',
                        'limit',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'query': {'type': 'string', 'required': True},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'repositoryCount': {'type': 'integer', 'description': 'Total number of repositories matching the query'},
                                            'pageInfo': {
                                                'type': 'object',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            'nodes': {
                                                'type': 'array',
                                                'description': 'Array of repository results',
                                                'items': {'type': 'object', 'description': 'Repository object with selected fields'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query SearchRepositories($searchQuery: String!, $first: Int!, $after: String) {\n  search(query: $searchQuery, type: REPOSITORY, first: $first, after: $after) {\n    repositoryCount\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n    nodes {\n      ... on Repository {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'searchQuery': '{{ query }}',
                            'first': '{{ limit }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id name nameWithOwner description url createdAt updatedAt pushedAt forkCount stargazerCount isPrivate isFork isArchived isTemplate hasIssuesEnabled hasWikiEnabled primaryLanguage { name } licenseInfo { name spdxId } owner { login avatarUrl } defaultBranchRef { name } repositoryTopics(first: 10) { nodes { topic { name } } }',
                    },
                    record_extractor='$.data.search.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='org_repositories',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:org_repositories:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of repositories for the specified organization using GraphQL',
                    query_params=[
                        'org',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'repositories': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListOrgRepositories($login: String!, $first: Int!, $after: String) {\n  organization(login: $login) {\n    repositories(first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'login': '{{ org }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id name nameWithOwner description url createdAt updatedAt pushedAt forkCount stargazerCount isPrivate isFork isArchived isTemplate hasIssuesEnabled hasWikiEnabled primaryLanguage { name } licenseInfo { name spdxId } owner { login avatarUrl } defaultBranchRef { name } repositoryTopics(first: 10) { nodes { topic { name } } }',
                    },
                    record_extractor='$.data.organization.repositories.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='branches',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:branches:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of branches for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'refs': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListBranches($owner: String!, $name: String!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    refs(refPrefix: "refs/heads/", first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'name prefix target { ... on Commit { oid commitUrl message author { name email date } } } associatedPullRequests(first: 1) { totalCount }',
                    },
                    record_extractor='$.data.repository.refs.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:branches:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific branch using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'branch',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'branch': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'ref': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetBranch($owner: String!, $name: String!, $branch: String!) {\n  repository(owner: $owner, name: $name) {\n    ref(qualifiedName: $branch) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'branch': 'refs/heads/{{ branch }}',
                        },
                        'default_fields': 'name prefix target { ... on Commit { oid commitUrl message author { name email date } } } associatedPullRequests(first: 1) { totalCount }',
                    },
                    record_extractor='$.data.repository.ref',
                ),
            },
        ),
        EntityDefinition(
            name='commits',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:commits:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of commits for the default branch using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'per_page',
                        'after',
                        'path',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'path': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'defaultBranchRef': {
                                                'type': 'object',
                                                'properties': {
                                                    'target': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'history': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'pageInfo': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'hasNextPage': {'type': 'boolean'},
                                                                            'endCursor': {
                                                                                'type': ['string', 'null'],
                                                                            },
                                                                        },
                                                                    },
                                                                    'nodes': {
                                                                        'type': 'array',
                                                                        'items': {'type': 'object'},
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
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query ListCommits($owner: String!, $name: String!, $first: Int!, $after: String, $path: String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n          history(first: $first, after: $after, path: $path) {\n            pageInfo {\n              hasNextPage\n              endCursor\n            }\n            nodes {\n              {{ fields }}\n            }\n          }\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                            'path': '{{ path }}',
                        },
                        'default_fields': 'oid message messageHeadline committedDate author { name email } additions deletions changedFiles parents(first: 5) { nodes { oid } }',
                    },
                    record_extractor='$.data.repository.defaultBranchRef.target.history.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:commits:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific commit by SHA using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'sha',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'sha': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'object': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetCommit($owner: String!, $name: String!, $oid: GitObjectID!) {\n  repository(owner: $owner, name: $name) {\n    object(oid: $oid) {\n      ... on Commit {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'oid': '{{ sha }}',
                        },
                        'default_fields': 'oid message messageHeadline committedDate author { name email } additions deletions changedFiles parents(first: 5) { nodes { oid } }',
                    },
                    record_extractor='$.data.repository.object',
                ),
            },
        ),
        EntityDefinition(
            name='releases',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:releases:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of releases for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'releases': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListReleases($owner: String!, $name: String!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    releases(first: $first, after: $after, orderBy: {field: CREATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId name tagName description publishedAt createdAt isPrerelease isDraft author { login avatarUrl } releaseAssets(first: 10) { nodes { name downloadUrl size } }',
                    },
                    record_extractor='$.data.repository.releases.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:releases:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific release by tag name using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'tag',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'tag': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'release': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetRelease($owner: String!, $name: String!, $tagName: String!) {\n  repository(owner: $owner, name: $name) {\n    release(tagName: $tagName) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'tagName': '{{ tag }}',
                        },
                        'default_fields': 'id databaseId name tagName description publishedAt createdAt isPrerelease isDraft author { login avatarUrl } releaseAssets(first: 10) { nodes { name downloadUrl size } }',
                    },
                    record_extractor='$.data.repository.release',
                ),
            },
        ),
        EntityDefinition(
            name='issues',
            actions=[
                Action.LIST,
                Action.GET,
                Action.API_SEARCH,
                Action.CREATE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:issues:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of issues for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'states',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'states': {'type': 'array', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'issues': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListIssues($owner: String!, $name: String!, $first: Int!, $after: String, $states: [IssueState!]) {\n  repository(owner: $owner, name: $name) {\n    issues(first: $first, after: $after, states: $states, orderBy: {field: CREATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                            'states': '{{ states }}',
                        },
                        'default_fields': 'id databaseId number title body state stateReason createdAt updatedAt closedAt author { login avatarUrl } assignees(first: 10) { nodes { login } } labels(first: 10) { nodes { name color } } milestone { title number } url locked comments { totalCount }',
                    },
                    record_extractor='$.data.repository.issues.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:issues:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific issue using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'issue': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetIssue($owner: String!, $name: String!, $number: Int!) {\n  repository(owner: $owner, name: $name) {\n    issue(number: $number) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                        },
                        'default_fields': 'id databaseId number title body bodyHTML state stateReason createdAt updatedAt closedAt author { login avatarUrl } assignees(first: 10) { nodes { login } } labels(first: 10) { nodes { name color } } milestone { title number } url locked comments { totalCount }',
                    },
                    record_extractor='$.data.repository.issue',
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/graphql:issues:search',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.API_SEARCH,
                    description="Search for issues using GitHub's search syntax",
                    query_params=[
                        'query',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'query': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'issueCount': {'type': 'integer'},
                                            'pageInfo': {
                                                'type': 'object',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            'nodes': {
                                                'type': 'array',
                                                'items': {'type': 'object'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query SearchIssues($searchQuery: String!, $first: Int!, $after: String) {\n  search(query: $searchQuery, type: ISSUE, first: $first, after: $after) {\n    issueCount\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n    nodes {\n      ... on Issue {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'searchQuery': '{{ query }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId number title body state stateReason createdAt updatedAt closedAt author { login avatarUrl } assignees(first: 10) { nodes { login } } labels(first: 10) { nodes { name color } } milestone { title number } url locked comments { totalCount }',
                    },
                    record_extractor='$.data.search.nodes',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/repos/{owner}/{repo}/issues',
                    action=Action.CREATE,
                    description='Creates a new issue in the specified repository.\nAny user with pull access to a repository can create an issue.\nLabels and assignees are silently dropped if the authenticated user does not have push access.\n',
                    body_fields=[
                        'title',
                        'body',
                        'labels',
                        'assignees',
                        'milestone',
                    ],
                    path_params=['owner', 'repo'],
                    path_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the issue'},
                            'body': {'type': 'string', 'description': 'The contents of the issue (supports Markdown)'},
                            'labels': {
                                'type': 'array',
                                'description': 'Labels to associate with this issue (requires push access)',
                                'items': {'type': 'string'},
                            },
                            'assignees': {
                                'type': 'array',
                                'description': 'Logins for users to assign to this issue (requires push access)',
                                'items': {'type': 'string'},
                            },
                            'milestone': {
                                'type': ['integer', 'null'],
                                'description': 'The number of the milestone to associate this issue with (requires push access)',
                            },
                        },
                        'required': ['title'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique identifier of the issue'},
                            'node_id': {'type': 'string', 'description': 'GraphQL node ID'},
                            'url': {'type': 'string', 'description': 'API URL for this issue'},
                            'repository_url': {'type': 'string', 'description': 'API URL for the repository'},
                            'labels_url': {'type': 'string', 'description': 'URL template for labels'},
                            'comments_url': {'type': 'string', 'description': 'API URL for comments'},
                            'events_url': {'type': 'string', 'description': 'API URL for events'},
                            'html_url': {'type': 'string', 'description': 'Web URL for this issue'},
                            'number': {'type': 'integer', 'description': 'Issue number'},
                            'state': {'type': 'string', 'description': 'State of the issue (open or closed)'},
                            'state_reason': {
                                'type': ['string', 'null'],
                                'description': 'Reason for the current state',
                            },
                            'title': {'type': 'string', 'description': 'Title of the issue'},
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'Body content of the issue',
                            },
                            'user': {
                                'type': ['object', 'null'],
                                'description': 'The user who created the issue',
                                'properties': {
                                    'login': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'node_id': {'type': 'string'},
                                    'avatar_url': {'type': 'string'},
                                    'url': {'type': 'string'},
                                    'html_url': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'site_admin': {'type': 'boolean'},
                                },
                            },
                            'labels': {
                                'type': 'array',
                                'description': 'Labels associated with this issue',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'integer'},
                                        'node_id': {'type': 'string'},
                                        'url': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'color': {'type': 'string'},
                                        'default': {'type': 'boolean'},
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                            },
                            'assignees': {
                                'type': 'array',
                                'description': 'Users assigned to this issue',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'login': {'type': 'string'},
                                        'id': {'type': 'integer'},
                                        'node_id': {'type': 'string'},
                                        'avatar_url': {'type': 'string'},
                                        'url': {'type': 'string'},
                                        'html_url': {'type': 'string'},
                                        'type': {'type': 'string'},
                                        'site_admin': {'type': 'boolean'},
                                    },
                                },
                            },
                            'milestone': {
                                'type': ['object', 'null'],
                                'description': 'Milestone associated with this issue',
                            },
                            'locked': {'type': 'boolean', 'description': 'Whether the issue is locked'},
                            'comments': {'type': 'integer', 'description': 'Number of comments'},
                            'closed_at': {
                                'type': ['string', 'null'],
                                'description': 'When the issue was closed',
                            },
                            'created_at': {'type': 'string', 'description': 'When the issue was created'},
                            'updated_at': {'type': 'string', 'description': 'When the issue was last updated'},
                            'author_association': {'type': 'string', 'description': 'How the author is associated with the repository'},
                            'active_lock_reason': {
                                'type': ['string', 'null'],
                                'description': 'The reason the issue is locked',
                            },
                            'closed_by': {
                                'type': ['object', 'null'],
                                'description': 'The user who closed the issue',
                            },
                            'timeline_url': {'type': 'string', 'description': 'API URL for the issue timeline'},
                            'performed_via_github_app': {
                                'type': ['object', 'null'],
                                'description': 'GitHub App that performed the action',
                            },
                            'assignee': {
                                'type': ['object', 'null'],
                                'description': 'Primary user assigned to this issue',
                                'properties': {
                                    'login': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'node_id': {'type': 'string'},
                                    'avatar_url': {'type': 'string'},
                                    'url': {'type': 'string'},
                                    'html_url': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'site_admin': {'type': 'boolean'},
                                },
                            },
                            'reactions': {
                                'type': 'object',
                                'description': 'Reaction counts',
                                'properties': {
                                    'url': {'type': 'string'},
                                    'total_count': {'type': 'integer'},
                                    '+1': {'type': 'integer'},
                                    '-1': {'type': 'integer'},
                                    'laugh': {'type': 'integer'},
                                    'hooray': {'type': 'integer'},
                                    'confused': {'type': 'integer'},
                                    'heart': {'type': 'integer'},
                                    'rocket': {'type': 'integer'},
                                    'eyes': {'type': 'integer'},
                                },
                            },
                            'sub_issues_summary': {
                                'type': 'object',
                                'description': 'Summary of sub-issues',
                                'properties': {
                                    'total': {'type': 'integer'},
                                    'completed': {'type': 'integer'},
                                    'percent_completed': {'type': 'integer'},
                                },
                            },
                            'type': {
                                'type': ['object', 'null'],
                                'description': 'Issue type',
                            },
                            'pinned_comment': {
                                'type': ['object', 'null'],
                                'description': 'Pinned comment on the issue',
                            },
                            'issue_field_values': {
                                'type': 'array',
                                'description': 'Custom field values for the issue',
                                'items': {'type': 'object'},
                            },
                            'issue_dependencies_summary': {
                                'type': 'object',
                                'description': 'Summary of issue dependencies',
                                'properties': {
                                    'blocked_by': {'type': 'integer'},
                                    'blocking': {'type': 'integer'},
                                    'total_blocked_by': {'type': 'integer'},
                                    'total_blocking': {'type': 'integer'},
                                },
                            },
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/repos/{owner}/{repo}/issues/{issue_number}',
                    action=Action.UPDATE,
                    description='Updates an existing issue in the specified repository.\nUse this to close/reopen issues, change title/body, add/remove labels, assign users, or set milestones.\nAny user with push access can update an issue.\n',
                    body_fields=[
                        'title',
                        'body',
                        'state',
                        'state_reason',
                        'labels',
                        'assignees',
                        'milestone',
                    ],
                    path_params=['owner', 'repo', 'issue_number'],
                    path_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'issue_number': {'type': 'integer', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the issue'},
                            'body': {'type': 'string', 'description': 'The contents of the issue (supports Markdown)'},
                            'state': {
                                'type': 'string',
                                'enum': ['open', 'closed'],
                                'description': 'State of the issue: open or closed',
                            },
                            'state_reason': {
                                'type': ['string', 'null'],
                                'enum': [
                                    'completed',
                                    'not_planned',
                                    'reopened',
                                    None,
                                ],
                                'description': 'Reason for the state change: completed, not_planned, reopened, or null',
                            },
                            'labels': {
                                'type': 'array',
                                'description': 'Labels to set on this issue (replaces all existing labels; requires push access)',
                                'items': {'type': 'string'},
                            },
                            'assignees': {
                                'type': 'array',
                                'description': 'Logins for users to assign to this issue (replaces all existing assignees; requires push access)',
                                'items': {'type': 'string'},
                            },
                            'milestone': {
                                'type': ['integer', 'null'],
                                'description': 'The number of the milestone to associate this issue with, or null to remove the milestone (requires push access)',
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique identifier of the issue'},
                            'node_id': {'type': 'string', 'description': 'GraphQL node ID'},
                            'url': {'type': 'string', 'description': 'API URL for this issue'},
                            'repository_url': {'type': 'string', 'description': 'API URL for the repository'},
                            'labels_url': {'type': 'string', 'description': 'URL template for labels'},
                            'comments_url': {'type': 'string', 'description': 'API URL for comments'},
                            'events_url': {'type': 'string', 'description': 'API URL for events'},
                            'html_url': {'type': 'string', 'description': 'Web URL for this issue'},
                            'number': {'type': 'integer', 'description': 'Issue number'},
                            'state': {'type': 'string', 'description': 'State of the issue (open or closed)'},
                            'state_reason': {
                                'type': ['string', 'null'],
                                'description': 'Reason for the current state',
                            },
                            'title': {'type': 'string', 'description': 'Title of the issue'},
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'Body content of the issue',
                            },
                            'user': {
                                'type': ['object', 'null'],
                                'description': 'The user who created the issue',
                                'properties': {
                                    'login': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'node_id': {'type': 'string'},
                                    'avatar_url': {'type': 'string'},
                                    'url': {'type': 'string'},
                                    'html_url': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'site_admin': {'type': 'boolean'},
                                },
                            },
                            'labels': {
                                'type': 'array',
                                'description': 'Labels associated with this issue',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'integer'},
                                        'node_id': {'type': 'string'},
                                        'url': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'color': {'type': 'string'},
                                        'default': {'type': 'boolean'},
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                            },
                            'assignees': {
                                'type': 'array',
                                'description': 'Users assigned to this issue',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'login': {'type': 'string'},
                                        'id': {'type': 'integer'},
                                        'node_id': {'type': 'string'},
                                        'avatar_url': {'type': 'string'},
                                        'url': {'type': 'string'},
                                        'html_url': {'type': 'string'},
                                        'type': {'type': 'string'},
                                        'site_admin': {'type': 'boolean'},
                                    },
                                },
                            },
                            'milestone': {
                                'type': ['object', 'null'],
                                'description': 'Milestone associated with this issue',
                            },
                            'locked': {'type': 'boolean', 'description': 'Whether the issue is locked'},
                            'comments': {'type': 'integer', 'description': 'Number of comments'},
                            'closed_at': {
                                'type': ['string', 'null'],
                                'description': 'When the issue was closed',
                            },
                            'created_at': {'type': 'string', 'description': 'When the issue was created'},
                            'updated_at': {'type': 'string', 'description': 'When the issue was last updated'},
                            'author_association': {'type': 'string', 'description': 'How the author is associated with the repository'},
                            'active_lock_reason': {
                                'type': ['string', 'null'],
                                'description': 'The reason the issue is locked',
                            },
                            'closed_by': {
                                'type': ['object', 'null'],
                                'description': 'The user who closed the issue',
                            },
                            'timeline_url': {'type': 'string', 'description': 'API URL for the issue timeline'},
                            'performed_via_github_app': {
                                'type': ['object', 'null'],
                                'description': 'GitHub App that performed the action',
                            },
                            'assignee': {
                                'type': ['object', 'null'],
                                'description': 'Primary user assigned to this issue',
                                'properties': {
                                    'login': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'node_id': {'type': 'string'},
                                    'avatar_url': {'type': 'string'},
                                    'url': {'type': 'string'},
                                    'html_url': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'site_admin': {'type': 'boolean'},
                                },
                            },
                            'reactions': {
                                'type': 'object',
                                'description': 'Reaction counts',
                                'properties': {
                                    'url': {'type': 'string'},
                                    'total_count': {'type': 'integer'},
                                    '+1': {'type': 'integer'},
                                    '-1': {'type': 'integer'},
                                    'laugh': {'type': 'integer'},
                                    'hooray': {'type': 'integer'},
                                    'confused': {'type': 'integer'},
                                    'heart': {'type': 'integer'},
                                    'rocket': {'type': 'integer'},
                                    'eyes': {'type': 'integer'},
                                },
                            },
                            'sub_issues_summary': {
                                'type': 'object',
                                'description': 'Summary of sub-issues',
                                'properties': {
                                    'total': {'type': 'integer'},
                                    'completed': {'type': 'integer'},
                                    'percent_completed': {'type': 'integer'},
                                },
                            },
                            'type': {
                                'type': ['object', 'null'],
                                'description': 'Issue type',
                            },
                            'pinned_comment': {
                                'type': ['object', 'null'],
                                'description': 'Pinned comment on the issue',
                            },
                            'issue_field_values': {
                                'type': 'array',
                                'description': 'Custom field values for the issue',
                                'items': {'type': 'object'},
                            },
                            'issue_dependencies_summary': {
                                'type': 'object',
                                'description': 'Summary of issue dependencies',
                                'properties': {
                                    'blocked_by': {'type': 'integer'},
                                    'blocking': {'type': 'integer'},
                                    'total_blocked_by': {'type': 'integer'},
                                    'total_blocking': {'type': 'integer'},
                                },
                            },
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='comments',
            actions=[Action.CREATE, Action.LIST, Action.GET],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/repos/{owner}/{repo}/issues/{issue_number}/comments',
                    action=Action.CREATE,
                    description='Creates a comment on the specified issue.\nThis endpoint works for both issues and pull requests, since pull requests are issues.\nAny user with read access can create a comment.\n',
                    body_fields=['body'],
                    path_params=['owner', 'repo', 'issue_number'],
                    path_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'issue_number': {'type': 'integer', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'body': {'type': 'string', 'description': 'The contents of the comment (supports Markdown)'},
                        },
                        'required': ['body'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique identifier of the comment'},
                            'node_id': {'type': 'string', 'description': 'GraphQL node ID'},
                            'url': {'type': 'string', 'description': 'API URL for this comment'},
                            'html_url': {'type': 'string', 'description': 'Web URL for this comment'},
                            'body': {'type': 'string', 'description': 'Body content of the comment'},
                            'user': {
                                'type': ['object', 'null'],
                                'description': 'The user who created the comment',
                                'properties': {
                                    'login': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'node_id': {'type': 'string'},
                                    'avatar_url': {'type': 'string'},
                                    'url': {'type': 'string'},
                                    'html_url': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'site_admin': {'type': 'boolean'},
                                },
                            },
                            'created_at': {'type': 'string', 'description': 'When the comment was created'},
                            'updated_at': {'type': 'string', 'description': 'When the comment was last updated'},
                            'issue_url': {'type': 'string', 'description': 'API URL for the parent issue'},
                            'author_association': {'type': 'string', 'description': 'How the author is associated with the repository'},
                            'performed_via_github_app': {
                                'type': ['object', 'null'],
                                'description': 'GitHub App that performed the action',
                            },
                            'reactions': {
                                'type': 'object',
                                'description': 'Reaction counts',
                                'properties': {
                                    'url': {'type': 'string'},
                                    'total_count': {'type': 'integer'},
                                    '+1': {'type': 'integer'},
                                    '-1': {'type': 'integer'},
                                    'laugh': {'type': 'integer'},
                                    'hooray': {'type': 'integer'},
                                    'confused': {'type': 'integer'},
                                    'heart': {'type': 'integer'},
                                    'rocket': {'type': 'integer'},
                                    'eyes': {'type': 'integer'},
                                },
                            },
                        },
                    },
                ),
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:comments:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of comments for the specified issue using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'issue': {
                                                'type': 'object',
                                                'properties': {
                                                    'comments': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'pageInfo': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'hasNextPage': {'type': 'boolean'},
                                                                    'endCursor': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'nodes': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
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
                        'query': 'query ListComments($owner: String!, $name: String!, $number: Int!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    issue(number: $number) {\n      comments(first: $first, after: $after) {\n        pageInfo {\n          hasNextPage\n          endCursor\n        }\n        nodes {\n          {{ fields }}\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId body bodyHTML createdAt updatedAt author { login avatarUrl } url isMinimized minimizedReason',
                    },
                    record_extractor='$.data.repository.issue.comments.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:comments:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description="Gets information about a specific issue comment by its GraphQL node ID.\n\nNote: This endpoint requires a GraphQL node ID (e.g., 'IC_kwDOBZtLds6YWTMj'),\nnot a numeric database ID. You can obtain node IDs from the Comments_List response,\nwhere each comment includes both 'id' (node ID) and 'databaseId' (numeric ID).\n",
                    query_params=['id', 'fields'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'node': {'type': 'object'},
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetComment($id: ID!) {\n  node(id: $id) {\n    ... on IssueComment {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {'id': '{{ id }}'},
                        'default_fields': 'id databaseId body bodyHTML createdAt updatedAt author { login avatarUrl } url isMinimized minimizedReason',
                    },
                    record_extractor='$.data.node',
                ),
            },
        ),
        EntityDefinition(
            name='pull_requests',
            actions=[
                Action.CREATE,
                Action.LIST,
                Action.GET,
                Action.API_SEARCH,
            ],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/repos/{owner}/{repo}/pulls',
                    action=Action.CREATE,
                    description='Creates a new pull request in the specified repository.\nTo open or update a pull request in a public repository, you must have write access to the head or the source branch.\n',
                    body_fields=[
                        'title',
                        'head',
                        'base',
                        'body',
                        'draft',
                        'maintainer_can_modify',
                    ],
                    path_params=['owner', 'repo'],
                    path_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the new pull request'},
                            'head': {'type': 'string', 'description': 'The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace head with a user like this: username:branch'},
                            'base': {'type': 'string', 'description': 'The name of the branch you want the changes pulled into (e.g. main)'},
                            'body': {'type': 'string', 'description': 'The contents of the pull request (supports Markdown)'},
                            'draft': {'type': 'boolean', 'description': 'Indicates whether the pull request is a draft'},
                            'maintainer_can_modify': {'type': 'boolean', 'description': 'Indicates whether maintainers can modify the pull request'},
                        },
                        'required': ['title', 'head', 'base'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique identifier of the pull request'},
                            'node_id': {'type': 'string', 'description': 'GraphQL node ID'},
                            'url': {'type': 'string', 'description': 'API URL for this pull request'},
                            'html_url': {'type': 'string', 'description': 'Web URL for this pull request'},
                            'diff_url': {'type': 'string', 'description': 'URL for the diff'},
                            'patch_url': {'type': 'string', 'description': 'URL for the patch'},
                            'number': {'type': 'integer', 'description': 'Pull request number'},
                            'state': {'type': 'string', 'description': 'State of the pull request (open or closed)'},
                            'locked': {'type': 'boolean', 'description': 'Whether the pull request is locked'},
                            'title': {'type': 'string', 'description': 'Title of the pull request'},
                            'body': {
                                'type': ['string', 'null'],
                                'description': 'Body content of the pull request',
                            },
                            'user': {
                                'type': ['object', 'null'],
                                'description': 'The user who created the pull request',
                                'properties': {
                                    'login': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'node_id': {'type': 'string'},
                                    'avatar_url': {'type': 'string'},
                                    'url': {'type': 'string'},
                                    'html_url': {'type': 'string'},
                                    'type': {'type': 'string'},
                                    'site_admin': {'type': 'boolean'},
                                },
                            },
                            'created_at': {'type': 'string', 'description': 'When the pull request was created'},
                            'updated_at': {'type': 'string', 'description': 'When the pull request was last updated'},
                            'closed_at': {
                                'type': ['string', 'null'],
                                'description': 'When the pull request was closed',
                            },
                            'merged_at': {
                                'type': ['string', 'null'],
                                'description': 'When the pull request was merged',
                            },
                            'merge_commit_sha': {
                                'type': ['string', 'null'],
                                'description': 'SHA of the merge commit',
                            },
                            'draft': {'type': 'boolean', 'description': 'Whether this is a draft pull request'},
                            'head': {
                                'type': 'object',
                                'description': 'The head branch',
                                'properties': {
                                    'label': {'type': 'string'},
                                    'ref': {'type': 'string'},
                                    'sha': {'type': 'string'},
                                },
                            },
                            'base': {
                                'type': 'object',
                                'description': 'The base branch',
                                'properties': {
                                    'label': {'type': 'string'},
                                    'ref': {'type': 'string'},
                                    'sha': {'type': 'string'},
                                },
                            },
                            'author_association': {'type': 'string', 'description': 'How the author is associated with the repository'},
                            'labels': {
                                'type': 'array',
                                'description': 'Labels associated with this pull request',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'integer'},
                                        'node_id': {'type': 'string'},
                                        'url': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'color': {'type': 'string'},
                                        'default': {'type': 'boolean'},
                                        'description': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                            },
                            'milestone': {
                                'type': ['object', 'null'],
                                'description': 'Milestone associated with this pull request',
                            },
                            'assignees': {
                                'type': 'array',
                                'description': 'Users assigned to this pull request',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'login': {'type': 'string'},
                                        'id': {'type': 'integer'},
                                        'node_id': {'type': 'string'},
                                        'avatar_url': {'type': 'string'},
                                        'url': {'type': 'string'},
                                        'html_url': {'type': 'string'},
                                        'type': {'type': 'string'},
                                        'site_admin': {'type': 'boolean'},
                                    },
                                },
                            },
                            'requested_reviewers': {
                                'type': 'array',
                                'description': 'Users requested to review this pull request',
                                'items': {'type': 'object'},
                            },
                            'comments': {'type': 'integer', 'description': 'Number of comments'},
                            'review_comments': {'type': 'integer', 'description': 'Number of review comments'},
                            'commits': {'type': 'integer', 'description': 'Number of commits'},
                            'additions': {'type': 'integer', 'description': 'Number of additions'},
                            'deletions': {'type': 'integer', 'description': 'Number of deletions'},
                            'changed_files': {'type': 'integer', 'description': 'Number of changed files'},
                        },
                    },
                ),
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:pull_requests:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of pull requests for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'states',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'states': {'type': 'array', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'pullRequests': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListPullRequests($owner: String!, $name: String!, $first: Int!, $after: String, $states: [PullRequestState!]) {\n  repository(owner: $owner, name: $name) {\n    pullRequests(first: $first, after: $after, states: $states, orderBy: {field: CREATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                            'states': '{{ states }}',
                        },
                        'default_fields': 'id databaseId number title body state isDraft createdAt updatedAt closedAt mergedAt author { login avatarUrl } baseRefName headRefName mergeable merged mergedBy { login } additions deletions changedFiles commits { totalCount } comments { totalCount } reviews { totalCount } reviewRequests { totalCount } assignees(first: 10) { nodes { login } } labels(first: 10) { nodes { name color } } url',
                    },
                    record_extractor='$.data.repository.pullRequests.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:pull_requests:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific pull request using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'pullRequest': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetPullRequest($owner: String!, $name: String!, $number: Int!) {\n  repository(owner: $owner, name: $name) {\n    pullRequest(number: $number) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                        },
                        'default_fields': 'id databaseId number title body bodyHTML state isDraft createdAt updatedAt closedAt mergedAt author { login avatarUrl } baseRefName headRefName mergeable merged mergedBy { login } additions deletions changedFiles commits { totalCount } comments { totalCount } reviews { totalCount } reviewRequests { totalCount } assignees(first: 10) { nodes { login } } labels(first: 10) { nodes { name color } } url',
                    },
                    record_extractor='$.data.repository.pullRequest',
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/graphql:pull_requests:search',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.API_SEARCH,
                    description="Search for pull requests using GitHub's search syntax",
                    query_params=[
                        'query',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'query': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'issueCount': {'type': 'integer'},
                                            'pageInfo': {
                                                'type': 'object',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            'nodes': {
                                                'type': 'array',
                                                'items': {'type': 'object'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query SearchPullRequests($searchQuery: String!, $first: Int!, $after: String) {\n  search(query: $searchQuery, type: ISSUE, first: $first, after: $after) {\n    issueCount\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n    nodes {\n      ... on PullRequest {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'searchQuery': '{{ query }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId number title body state isDraft createdAt updatedAt closedAt mergedAt author { login avatarUrl } baseRefName headRefName mergeable merged mergedBy { login } additions deletions changedFiles commits { totalCount } comments { totalCount } reviews { totalCount } reviewRequests { totalCount } assignees(first: 10) { nodes { login } } labels(first: 10) { nodes { name color } } url',
                    },
                    record_extractor='$.data.search.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='reviews',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:reviews:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of reviews for the specified pull request using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'pullRequest': {
                                                'type': 'object',
                                                'properties': {
                                                    'reviews': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'pageInfo': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'hasNextPage': {'type': 'boolean'},
                                                                    'endCursor': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'nodes': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
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
                        'query': 'query ListReviews($owner: String!, $name: String!, $number: Int!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    pullRequest(number: $number) {\n      reviews(first: $first, after: $after) {\n        pageInfo {\n          hasNextPage\n          endCursor\n        }\n        nodes {\n          {{ fields }}\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId state body submittedAt author { login avatarUrl } comments { totalCount }',
                    },
                    record_extractor='$.data.repository.pullRequest.reviews.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='pr_comments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:pr_comments:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of comments for the specified pull request using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'pullRequest': {
                                                'type': 'object',
                                                'properties': {
                                                    'comments': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'pageInfo': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'hasNextPage': {'type': 'boolean'},
                                                                    'endCursor': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'nodes': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
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
                        'query': 'query ListPRComments($owner: String!, $name: String!, $number: Int!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    pullRequest(number: $number) {\n      comments(first: $first, after: $after) {\n        pageInfo {\n          hasNextPage\n          endCursor\n        }\n        nodes {\n          {{ fields }}\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId body bodyHTML createdAt updatedAt author { login avatarUrl } url isMinimized minimizedReason',
                    },
                    record_extractor='$.data.repository.pullRequest.comments.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:pr_comments:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description="Gets information about a specific pull request comment by its GraphQL node ID.\n\nNote: This endpoint requires a GraphQL node ID (e.g., 'IC_kwDOBZtLds6YWTMj'),\nnot a numeric database ID. You can obtain node IDs from the PRComments_List response,\nwhere each comment includes both 'id' (node ID) and 'databaseId' (numeric ID).\n",
                    query_params=['id', 'fields'],
                    query_params_schema={
                        'id': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'node': {'type': 'object'},
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetPRComment($id: ID!) {\n  node(id: $id) {\n    ... on IssueComment {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {'id': '{{ id }}'},
                        'default_fields': 'id databaseId body bodyHTML createdAt updatedAt author { login avatarUrl } url isMinimized minimizedReason',
                    },
                    record_extractor='$.data.node',
                ),
            },
        ),
        EntityDefinition(
            name='labels',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:labels:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of labels for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'labels': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListLabels($owner: String!, $name: String!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    labels(first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id name color description createdAt url issues { totalCount } pullRequests { totalCount }',
                    },
                    record_extractor='$.data.repository.labels.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:labels:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific label by name using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'name',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'name': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'label': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetLabel($owner: String!, $repoName: String!, $labelName: String!) {\n  repository(owner: $owner, name: $repoName) {\n    label(name: $labelName) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'repoName': '{{ repo }}',
                            'labelName': '{{ name }}',
                        },
                        'default_fields': 'id name color description createdAt url issues { totalCount } pullRequests { totalCount }',
                    },
                    record_extractor='$.data.repository.label',
                ),
            },
        ),
        EntityDefinition(
            name='milestones',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:milestones:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of milestones for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'states',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'states': {'type': 'array', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'milestones': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListMilestones($owner: String!, $name: String!, $first: Int!, $after: String, $states: [MilestoneState!]) {\n  repository(owner: $owner, name: $name) {\n    milestones(first: $first, after: $after, states: $states, orderBy: {field: CREATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                            'states': '{{ states }}',
                        },
                        'default_fields': 'id number title description state dueOn closedAt createdAt updatedAt progressPercentage issues { totalCount } pullRequests { totalCount }',
                    },
                    record_extractor='$.data.repository.milestones.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:milestones:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific milestone by number using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'milestone': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetMilestone($owner: String!, $name: String!, $number: Int!) {\n  repository(owner: $owner, name: $name) {\n    milestone(number: $number) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                        },
                        'default_fields': 'id number title description state dueOn closedAt createdAt updatedAt progressPercentage issues { totalCount } pullRequests { totalCount }',
                    },
                    record_extractor='$.data.repository.milestone',
                ),
            },
        ),
        EntityDefinition(
            name='organizations',
            actions=[Action.GET, Action.LIST],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:organizations:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific organization using GraphQL',
                    query_params=['org', 'fields'],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {'type': 'object'},
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetOrganization($login: String!) {\n  organization(login: $login) {\n    {{ fields }}\n  }\n}\n',
                        'variables': {'login': '{{ org }}'},
                        'default_fields': 'id databaseId login name description email websiteUrl url avatarUrl createdAt updatedAt location isVerified repositories { totalCount } membersWithRole { totalCount } teams { totalCount }',
                    },
                    record_extractor='$.data.organization',
                ),
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:organizations:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of organizations the user belongs to using GraphQL',
                    query_params=[
                        'username',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'username': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'user': {
                                        'type': 'object',
                                        'properties': {
                                            'organizations': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListOrganizations($login: String!, $first: Int!, $after: String) {\n  user(login: $login) {\n    organizations(first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'login': '{{ username }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId login name description email websiteUrl url avatarUrl createdAt updatedAt location isVerified repositories { totalCount } membersWithRole { totalCount } teams { totalCount }',
                    },
                    record_extractor='$.data.user.organizations.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='users',
            actions=[Action.GET, Action.LIST, Action.API_SEARCH],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:users:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific user using GraphQL',
                    query_params=['username', 'fields'],
                    query_params_schema={
                        'username': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'user': {'type': 'object'},
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetUser($login: String!) {\n  user(login: $login) {\n    {{ fields }}\n  }\n}\n',
                        'variables': {'login': '{{ username }}'},
                        'default_fields': 'id databaseId login name email bio company location websiteUrl twitterUsername url avatarUrl createdAt updatedAt isHireable followers { totalCount } following { totalCount } repositories { totalCount } starredRepositories { totalCount } organizations { totalCount }',
                    },
                    record_extractor='$.data.user',
                ),
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:users:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of members for the specified organization using GraphQL',
                    query_params=[
                        'org',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'membersWithRole': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListUsers($login: String!, $first: Int!, $after: String) {\n  organization(login: $login) {\n    membersWithRole(first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'login': '{{ org }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId login name email bio company location websiteUrl twitterUsername url avatarUrl createdAt updatedAt isHireable followers { totalCount } following { totalCount } repositories { totalCount } starredRepositories { totalCount } organizations { totalCount }',
                    },
                    record_extractor='$.data.organization.membersWithRole.nodes',
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/graphql:users:search',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for GitHub users using search syntax',
                    query_params=[
                        'query',
                        'limit',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'query': {'type': 'string', 'required': True},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'userCount': {'type': 'integer'},
                                            'pageInfo': {
                                                'type': 'object',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            'nodes': {
                                                'type': 'array',
                                                'items': {'type': 'object'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query SearchUsers($searchQuery: String!, $first: Int!, $after: String) {\n  search(query: $searchQuery, type: USER, first: $first, after: $after) {\n    userCount\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n    nodes {\n      ... on User {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'searchQuery': '{{ query }}',
                            'first': '{{ limit }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId login name email bio company location websiteUrl twitterUsername url avatarUrl createdAt updatedAt isHireable followers { totalCount } following { totalCount } repositories { totalCount } starredRepositories { totalCount } organizations { totalCount }',
                    },
                    record_extractor='$.data.search.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='teams',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:teams:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of teams for the specified organization using GraphQL',
                    query_params=[
                        'org',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'teams': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListTeams($login: String!, $first: Int!, $after: String) {\n  organization(login: $login) {\n    teams(first: $first, after: $after) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'login': '{{ org }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId slug name description privacy url avatarUrl createdAt updatedAt parentTeam { slug name } members { totalCount } repositories { totalCount }',
                    },
                    record_extractor='$.data.organization.teams.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:teams:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific team using GraphQL',
                    query_params=['org', 'team_slug', 'fields'],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'team_slug': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'team': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetTeam($login: String!, $slug: String!) {\n  organization(login: $login) {\n    team(slug: $slug) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {'login': '{{ org }}', 'slug': '{{ team_slug }}'},
                        'default_fields': 'id databaseId slug name description privacy url avatarUrl createdAt updatedAt parentTeam { slug name } members { totalCount } repositories { totalCount }',
                    },
                    record_extractor='$.data.organization.team',
                ),
            },
        ),
        EntityDefinition(
            name='tags',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:tags:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of tags for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'refs': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListTags($owner: String!, $name: String!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    refs(refPrefix: "refs/tags/", first: $first, after: $after, orderBy: {field: TAG_COMMIT_DATE, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'name prefix target { oid ... on Commit { commitUrl message } ... on Tag { tagger { name email date } message } }',
                    },
                    record_extractor='$.data.repository.refs.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:tags:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific tag by name using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'tag',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'tag': {'type': 'string', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'ref': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetTag($owner: String!, $name: String!, $tag: String!) {\n  repository(owner: $owner, name: $name) {\n    ref(qualifiedName: $tag) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'tag': 'refs/tags/{{ tag }}',
                        },
                        'default_fields': 'name prefix target { oid ... on Commit { commitUrl message } ... on Tag { tagger { name email date } message } }',
                    },
                    record_extractor='$.data.repository.ref',
                ),
            },
        ),
        EntityDefinition(
            name='stargazers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:stargazers:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of users who have starred the repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'stargazers': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {'type': 'string'},
                                                        },
                                                    },
                                                    'edges': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListStargazers($owner: String!, $name: String!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    stargazers(first: $first, after: $after, orderBy: {field: STARRED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      edges {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'starredAt node { id login name avatarUrl url }',
                    },
                    record_extractor='$.data.repository.stargazers.edges',
                ),
            },
        ),
        EntityDefinition(
            name='viewer',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:viewer:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description="Gets information about the currently authenticated user.\nThis is useful when you don't know the username but need to access\nthe current user's profile, permissions, or associated resources.\n",
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'viewer': {'type': 'object', 'description': 'The authenticated user object with selected fields'},
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetViewer {\n  viewer {\n    {{ fields }}\n  }\n}\n',
                        'default_fields': 'id login name email bio company location websiteUrl avatarUrl url createdAt updatedAt isEmployee isDeveloperProgramMember isHireable isSiteAdmin viewerCanFollow viewerIsFollowing followers { totalCount } following { totalCount } repositories { totalCount } starredRepositories { totalCount } watching { totalCount }',
                    },
                    record_extractor='$.data.viewer',
                ),
            },
        ),
        EntityDefinition(
            name='viewer_repositories',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:viewer_repositories:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of repositories owned by the authenticated user.\nUnlike Repositories_List which requires a username, this endpoint\nautomatically lists repositories for the current authenticated user.\n',
                    query_params=['per_page', 'after', 'fields'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'viewer': {
                                        'type': 'object',
                                        'properties': {
                                            'repositories': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListViewerRepositories($first: Int!, $after: String) {\n  viewer {\n    repositories(first: $first, after: $after, ownerAffiliations: [OWNER], orderBy: {field: UPDATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {'first': '{{ per_page }}', 'after': '{{ after }}'},
                        'default_fields': 'id name nameWithOwner description url createdAt updatedAt pushedAt forkCount stargazerCount isPrivate isFork isArchived isTemplate hasIssuesEnabled hasWikiEnabled primaryLanguage { name } licenseInfo { name spdxId } owner { login avatarUrl } defaultBranchRef { name } repositoryTopics(first: 10) { nodes { topic { name } } }',
                    },
                    record_extractor='$.data.viewer.repositories.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='projects',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:projects:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of GitHub Projects V2 for the specified organization.\nProjects V2 are the new project boards that replaced classic projects.\n',
                    query_params=[
                        'org',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'projectsV2': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListProjects($org: String!, $first: Int!, $after: String) {\n  organization(login: $org) {\n    projectsV2(first: $first, after: $after, orderBy: {field: UPDATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'org': '{{ org }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id number title shortDescription url closed public createdAt updatedAt creator { login }',
                    },
                    record_extractor='$.data.organization.projectsV2.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:projects:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific GitHub Project V2 by number',
                    query_params=['org', 'project_number', 'fields'],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'project_number': {'type': 'integer', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'projectV2': {'type': 'object', 'description': 'Project object with selected fields'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetProject($org: String!, $number: Int!) {\n  organization(login: $org) {\n    projectV2(number: $number) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {'org': '{{ org }}', 'number': '{{ project_number }}'},
                        'default_fields': 'id number title shortDescription readme url closed public createdAt updatedAt creator { login } fields(first: 20) { nodes { ... on ProjectV2SingleSelectField { id name options { id name color description } } ... on ProjectV2Field { id name dataType } } }',
                    },
                    record_extractor='$.data.organization.projectV2',
                ),
            },
        ),
        EntityDefinition(
            name='project_items',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:project_items:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of items (issues, pull requests, draft issues) in a GitHub Project V2.\nEach item includes its field values like Status, Priority, etc.\n',
                    query_params=[
                        'org',
                        'project_number',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'org': {'type': 'string', 'required': True},
                        'project_number': {'type': 'integer', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'organization': {
                                        'type': 'object',
                                        'properties': {
                                            'projectV2': {
                                                'type': 'object',
                                                'properties': {
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'pageInfo': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'hasNextPage': {'type': 'boolean'},
                                                                    'endCursor': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'nodes': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
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
                        'query': 'query ListProjectItems($org: String!, $number: Int!, $first: Int!, $after: String) {\n  organization(login: $org) {\n    projectV2(number: $number) {\n      items(first: $first, after: $after) {\n        pageInfo {\n          hasNextPage\n          endCursor\n        }\n        nodes {\n          {{ fields }}\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'org': '{{ org }}',
                            'number': '{{ project_number }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id\ntype\ncreatedAt\nupdatedAt\nisArchived\ncontent {\n  ... on Issue {\n    id\n    title\n    number\n    state\n    url\n    createdAt\n    updatedAt\n    author { login }\n    assignees(first: 5) { nodes { login } }\n    labels(first: 10) { nodes { name color } }\n    repository { nameWithOwner }\n  }\n  ... on PullRequest {\n    id\n    title\n    number\n    state\n    url\n    createdAt\n    updatedAt\n    author { login }\n    assignees(first: 5) { nodes { login } }\n    labels(first: 10) { nodes { name color } }\n    repository { nameWithOwner }\n  }\n  ... on DraftIssue {\n    id\n    title\n    body\n    createdAt\n    updatedAt\n    creator { login }\n  }\n}\nfieldValues(first: 20) {\n  nodes {\n    ... on ProjectV2ItemFieldSingleSelectValue {\n      name\n      field { ... on ProjectV2SingleSelectField { name } }\n    }\n    ... on ProjectV2ItemFieldTextValue {\n      text\n      field { ... on ProjectV2Field { name } }\n    }\n    ... on ProjectV2ItemFieldDateValue {\n      date\n      field { ... on ProjectV2Field { name } }\n    }\n    ... on ProjectV2ItemFieldNumberValue {\n      number\n      field { ... on ProjectV2Field { name } }\n    }\n    ... on ProjectV2ItemFieldIterationValue {\n      title\n      startDate\n      duration\n      field { ... on ProjectV2IterationField { name } }\n    }\n    ... on ProjectV2ItemFieldLabelValue {\n      labels(first: 10) { nodes { name color } }\n      field { ... on ProjectV2Field { name } }\n    }\n    ... on ProjectV2ItemFieldUserValue {\n      users(first: 5) { nodes { login } }\n      field { ... on ProjectV2Field { name } }\n    }\n    ... on ProjectV2ItemFieldRepositoryValue {\n      repository { nameWithOwner }\n      field { ... on ProjectV2Field { name } }\n    }\n    ... on ProjectV2ItemFieldMilestoneValue {\n      milestone { title number }\n      field { ... on ProjectV2Field { name } }\n    }\n  }\n}\n',
                    },
                    record_extractor='$.data.organization.projectV2.items.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='discussions',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:discussions:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of discussions for the specified repository using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'states',
                        'answered',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'states': {'type': 'array', 'required': False},
                        'answered': {'type': 'boolean', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'discussions': {
                                                'type': 'object',
                                                'properties': {
                                                    'pageInfo': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'hasNextPage': {'type': 'boolean'},
                                                            'endCursor': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                    'nodes': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListDiscussions($owner: String!, $name: String!, $first: Int!, $after: String, $states: [DiscussionState!], $answered: Boolean) {\n  repository(owner: $owner, name: $name) {\n    discussions(first: $first, after: $after, states: $states, answered: $answered, orderBy: {field: CREATED_AT, direction: DESC}) {\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n      nodes {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                            'states': '{{ states }}',
                            'answered': '{{ answered }}',
                        },
                        'default_fields': 'id databaseId number title body bodyHTML createdAt updatedAt closedAt closed locked activeLockReason stateReason upvoteCount url isAnswered answerChosenAt author { login avatarUrl } category { id name slug emoji isAnswerable } answerChosenBy { login } answer { id body author { login } createdAt } labels(first: 10) { nodes { name color } } comments { totalCount }',
                    },
                    record_extractor='$.data.repository.discussions.nodes',
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:discussions:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Gets information about a specific discussion by number using GraphQL',
                    query_params=[
                        'owner',
                        'repo',
                        'number',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'number': {'type': 'integer', 'required': True},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'discussion': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetDiscussion($owner: String!, $name: String!, $number: Int!) {\n  repository(owner: $owner, name: $name) {\n    discussion(number: $number) {\n      {{ fields }}\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'number': '{{ number }}',
                        },
                        'default_fields': 'id databaseId number title body bodyHTML createdAt updatedAt closedAt closed locked activeLockReason stateReason upvoteCount url isAnswered answerChosenAt author { login avatarUrl } category { id name slug emoji isAnswerable } answerChosenBy { login } answer { id body author { login } createdAt } labels(first: 10) { nodes { name color } } comments { totalCount }',
                    },
                    record_extractor='$.data.repository.discussion',
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='POST',
                    path='/graphql:discussions:search',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.API_SEARCH,
                    description="Search for discussions using GitHub's search syntax",
                    query_params=[
                        'query',
                        'per_page',
                        'after',
                        'fields',
                    ],
                    query_params_schema={
                        'query': {'type': 'string', 'required': True},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 30,
                        },
                        'after': {'type': 'string', 'required': False},
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'discussionCount': {'type': 'integer'},
                                            'pageInfo': {
                                                'type': 'object',
                                                'properties': {
                                                    'hasNextPage': {'type': 'boolean'},
                                                    'endCursor': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            'nodes': {
                                                'type': 'array',
                                                'items': {'type': 'object'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query SearchDiscussions($searchQuery: String!, $first: Int!, $after: String) {\n  search(query: $searchQuery, type: DISCUSSION, first: $first, after: $after) {\n    discussionCount\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n    nodes {\n      ... on Discussion {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'searchQuery': '{{ query }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
                        },
                        'default_fields': 'id databaseId number title body createdAt updatedAt closedAt closed locked stateReason upvoteCount url isAnswered answerChosenAt author { login avatarUrl } category { id name slug emoji isAnswerable } answerChosenBy { login } answer { id body author { login } createdAt } labels(first: 10) { nodes { name color } } comments { totalCount }',
                    },
                    record_extractor='$.data.search.nodes',
                ),
            },
        ),
        EntityDefinition(
            name='file_content',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/graphql:file_content:get',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.GET,
                    description='Returns the text content of a file at a specific path and git ref (branch, tag, or commit SHA).\nOnly works for text files. Binary files will have text as null and isBinary as true.\n',
                    query_params=[
                        'owner',
                        'repo',
                        'path',
                        'ref',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'path': {'type': 'string', 'required': True},
                        'ref': {
                            'type': 'string',
                            'required': False,
                            'default': 'HEAD',
                        },
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'object': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    graphql_body={
                        'type': 'graphql',
                        'query': 'query GetFileContent($owner: String!, $name: String!, $expression: String!) {\n  repository(owner: $owner, name: $name) {\n    object(expression: $expression) {\n      ... on Blob {\n        {{ fields }}\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'expression': '{{ ref }}:{{ path }}',
                        },
                        'default_fields': 'text byteSize isBinary isTruncated oid abbreviatedOid',
                    },
                    record_extractor='$.data.repository.object',
                ),
            },
        ),
        EntityDefinition(
            name='directory_content',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/graphql:directory_content:list',
                    path_override=PathOverrideConfig(
                        path='/graphql',
                    ),
                    action=Action.LIST,
                    description='Returns a list of files and subdirectories at a specific path in the repository.\nEach entry includes the name, type (blob for files, tree for directories), and object ID.\nUse this to explore repository structure before reading specific files.\n',
                    query_params=[
                        'owner',
                        'repo',
                        'path',
                        'ref',
                        'fields',
                    ],
                    query_params_schema={
                        'owner': {'type': 'string', 'required': True},
                        'repo': {'type': 'string', 'required': True},
                        'path': {'type': 'string', 'required': True},
                        'ref': {
                            'type': 'string',
                            'required': False,
                            'default': 'HEAD',
                        },
                        'fields': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'repository': {
                                        'type': 'object',
                                        'properties': {
                                            'object': {
                                                'type': 'object',
                                                'properties': {
                                                    'entries': {
                                                        'type': 'array',
                                                        'items': {'type': 'object'},
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
                        'query': 'query ListDirectoryContent($owner: String!, $name: String!, $expression: String!) {\n  repository(owner: $owner, name: $name) {\n    object(expression: $expression) {\n      ... on Tree {\n        entries {\n          {{ fields }}\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'expression': '{{ ref }}:{{ path }}',
                        },
                        'default_fields': 'name type oid path',
                    },
                    record_extractor='$.data.repository.object.entries',
                ),
            },
        ),
    ],
    search_field_paths={},
    example_questions=ExampleQuestions(
        direct=[
            'Show me all open issues in my repositories this month',
            "List the top 5 repositories I've starred recently",
            'Analyze the commit trends in my main project over the last quarter',
            'Find all pull requests created in the past two weeks',
            'Search for repositories related to machine learning in my organizations',
            'Compare the number of contributors across my different team projects',
            'Identify the most active branches in my main repository',
            'Get details about the most recent releases in my organization',
            'List all milestones for our current development sprint',
            'Show me insights about pull request review patterns in our team',
            'List all unanswered discussions in a repository',
            'Show me recent discussions in the General category',
            "Create a new issue titled 'Fix login bug' in my repository",
            "Create an issue with labels 'bug' and 'urgent' in owner/repo",
            'File a new bug report issue in our project repository',
            'Create an issue and assign it to a team member',
            'Open a new feature request issue in the repository',
            'Close issue #42 in owner/repo as completed',
            'Reopen issue #15 in our repository',
            "Add the 'bug' and 'urgent' labels to issue #10",
            'Assign user @johndoe to issue #25 in owner/repo',
            "Update the title of issue #30 to 'New title'",
            "Add a comment to issue #5 saying 'This has been fixed in the latest release'",
            'Post a comment on pull request #100 with a status update',
            'Create a pull request from feature-branch to main in owner/repo',
            "Open a draft PR titled 'Add new feature' from my-branch to main",
        ],
        unsupported=[
            'Delete an old branch from the repository',
            'Schedule a team review for this code',
            'Merge a pull request',
            'Delete an issue or comment',
        ],
    ),
)