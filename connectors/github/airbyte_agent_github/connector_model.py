"""
Connector model for github.

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

GithubConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('ef69ef6e-aa7f-4af1-a01d-ef775033524e'),
    name='github',
    version='0.1.9',
    base_url='https://api.github.com',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='githubOAuth',
                type=AuthType.OAUTH2,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AirbyteAuthConfig(
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
                ),
            ),
            AuthOption(
                scheme_name='githubPAT',
                type=AuthType.BEARER,
                config={'header': 'Authorization', 'prefix': 'Bearer'},
                user_config_spec=AirbyteAuthConfig(
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
                        'query': 'query ListCommits($owner: String!, $name: String!, $first: Int!, $after: String) {\n  repository(owner: $owner, name: $name) {\n    defaultBranchRef {\n      target {\n        ... on Commit {\n          history(first: $first, after: $after) {\n            pageInfo {\n              hasNextPage\n              endCursor\n            }\n            nodes {\n              {{ fields }}\n            }\n          }\n        }\n      }\n    }\n  }\n}\n',
                        'variables': {
                            'owner': '{{ owner }}',
                            'name': '{{ repo }}',
                            'first': '{{ per_page }}',
                            'after': '{{ after }}',
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
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
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
            },
        ),
        EntityDefinition(
            name='pull_requests',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
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
            name='comments',
            actions=[Action.LIST, Action.GET],
            endpoints={
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
    ],
)