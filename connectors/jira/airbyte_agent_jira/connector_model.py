"""
Connector model for jira.

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

JiraConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('68e63de2-bb83-4c7e-93fa-a8a9051e3993'),
    name='jira',
    version='1.0.3',
    base_url='https://{subdomain}.atlassian.net',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
            type='object',
            required=['username', 'password'],
            properties={
                'username': AuthConfigFieldSpec(
                    title='Username',
                    description='Authentication username',
                ),
                'password': AuthConfigFieldSpec(
                    title='Password',
                    description='Authentication password',
                ),
            },
            auth_mapping={'username': '${username}', 'password': '${password}'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='issues',
            actions=[Action.SEARCH, Action.GET],
            endpoints={
                Action.SEARCH: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/search/jql',
                    action=Action.SEARCH,
                    description='Retrieve issues based on JQL query with pagination support',
                    query_params=[
                        'jql',
                        'nextPageToken',
                        'maxResults',
                        'fields',
                        'expand',
                        'properties',
                        'fieldsByKeys',
                        'failFast',
                    ],
                    query_params_schema={
                        'jql': {'type': 'string', 'required': False},
                        'nextPageToken': {'type': 'string', 'required': False},
                        'maxResults': {'type': 'integer', 'required': False},
                        'fields': {'type': 'string', 'required': False},
                        'expand': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'fieldsByKeys': {'type': 'boolean', 'required': False},
                        'failFast': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of issues from JQL search',
                        'properties': {
                            'issues': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Jira issue object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique issue identifier'},
                                        'key': {'type': 'string', 'description': 'Issue key (e.g., PROJ-123)'},
                                        'self': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of the issue',
                                        },
                                        'expand': {
                                            'type': ['string', 'null'],
                                            'description': 'Expand options that include additional issue details',
                                        },
                                        'fields': {
                                            'type': 'object',
                                            'description': "Issue fields (actual fields depend on 'fields' parameter in request)",
                                            'properties': {
                                                'summary': {'type': 'string', 'description': 'Issue summary/title'},
                                                'issuetype': {
                                                    'type': 'object',
                                                    'description': 'Issue type information',
                                                    'properties': {
                                                        'self': {'type': 'string', 'format': 'uri'},
                                                        'id': {'type': 'string'},
                                                        'description': {'type': 'string'},
                                                        'iconUrl': {'type': 'string', 'format': 'uri'},
                                                        'name': {'type': 'string'},
                                                        'subtask': {'type': 'boolean'},
                                                        'avatarId': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'hierarchyLevel': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                    },
                                                },
                                                'created': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Issue creation timestamp',
                                                },
                                                'updated': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Issue last update timestamp',
                                                },
                                                'project': {
                                                    'type': 'object',
                                                    'description': 'Project information',
                                                    'properties': {
                                                        'self': {'type': 'string', 'format': 'uri'},
                                                        'id': {'type': 'string'},
                                                        'key': {'type': 'string'},
                                                        'name': {'type': 'string'},
                                                        'projectTypeKey': {'type': 'string'},
                                                        'simplified': {'type': 'boolean'},
                                                        'avatarUrls': {
                                                            'type': 'object',
                                                            'description': 'URLs for user avatars in different sizes',
                                                            'properties': {
                                                                '16x16': {'type': 'string', 'format': 'uri'},
                                                                '24x24': {'type': 'string', 'format': 'uri'},
                                                                '32x32': {'type': 'string', 'format': 'uri'},
                                                                '48x48': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                        'projectCategory': {
                                                            'type': ['object', 'null'],
                                                            'properties': {
                                                                'self': {'type': 'string', 'format': 'uri'},
                                                                'id': {'type': 'string'},
                                                                'name': {'type': 'string'},
                                                                'description': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'reporter': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Issue reporter user information',
                                                    'properties': {
                                                        'self': {'type': 'string', 'format': 'uri'},
                                                        'accountId': {'type': 'string'},
                                                        'emailAddress': {'type': 'string', 'format': 'email'},
                                                        'avatarUrls': {
                                                            'type': 'object',
                                                            'description': 'URLs for user avatars in different sizes',
                                                            'properties': {
                                                                '16x16': {'type': 'string', 'format': 'uri'},
                                                                '24x24': {'type': 'string', 'format': 'uri'},
                                                                '32x32': {'type': 'string', 'format': 'uri'},
                                                                '48x48': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                        'displayName': {'type': 'string'},
                                                        'active': {'type': 'boolean'},
                                                        'timeZone': {'type': 'string'},
                                                        'accountType': {'type': 'string'},
                                                    },
                                                },
                                                'assignee': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Issue assignee user information (null if unassigned)',
                                                    'properties': {
                                                        'self': {'type': 'string', 'format': 'uri'},
                                                        'accountId': {'type': 'string'},
                                                        'emailAddress': {'type': 'string', 'format': 'email'},
                                                        'avatarUrls': {
                                                            'type': 'object',
                                                            'description': 'URLs for user avatars in different sizes',
                                                            'properties': {
                                                                '16x16': {'type': 'string', 'format': 'uri'},
                                                                '24x24': {'type': 'string', 'format': 'uri'},
                                                                '32x32': {'type': 'string', 'format': 'uri'},
                                                                '48x48': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                        'displayName': {'type': 'string'},
                                                        'active': {'type': 'boolean'},
                                                        'timeZone': {'type': 'string'},
                                                        'accountType': {'type': 'string'},
                                                    },
                                                },
                                                'priority': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Issue priority information',
                                                    'properties': {
                                                        'self': {'type': 'string', 'format': 'uri'},
                                                        'iconUrl': {'type': 'string', 'format': 'uri'},
                                                        'name': {'type': 'string'},
                                                        'id': {'type': 'string'},
                                                    },
                                                },
                                                'status': {
                                                    'type': 'object',
                                                    'description': 'Issue status information',
                                                    'properties': {
                                                        'self': {'type': 'string', 'format': 'uri'},
                                                        'description': {'type': 'string'},
                                                        'iconUrl': {'type': 'string', 'format': 'uri'},
                                                        'name': {'type': 'string'},
                                                        'id': {'type': 'string'},
                                                        'statusCategory': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'self': {'type': 'string', 'format': 'uri'},
                                                                'id': {'type': 'integer'},
                                                                'key': {'type': 'string'},
                                                                'colorName': {'type': 'string'},
                                                                'name': {'type': 'string'},
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'issues',
                                },
                                'description': 'Array of issue objects',
                            },
                            'total': {'type': 'integer', 'description': 'Total number of issues matching query'},
                            'maxResults': {
                                'type': ['integer', 'null'],
                                'description': 'Maximum number of results per page',
                            },
                            'startAt': {
                                'type': ['integer', 'null'],
                                'description': 'Index of first item returned',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'Token for fetching the next page',
                            },
                            'isLast': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this is the last page',
                            },
                        },
                    },
                    record_extractor='$.issues',
                    meta_extractor={
                        'nextPageToken': '$.nextPageToken',
                        'isLast': '$.isLast',
                        'total': '$.total',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/issue/{issueIdOrKey}',
                    action=Action.GET,
                    description='Retrieve a single issue by its ID or key',
                    query_params=[
                        'fields',
                        'expand',
                        'properties',
                        'fieldsByKeys',
                        'updateHistory',
                        'failFast',
                    ],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                        'expand': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                        'fieldsByKeys': {'type': 'boolean', 'required': False},
                        'updateHistory': {'type': 'boolean', 'required': False},
                        'failFast': {'type': 'boolean', 'required': False},
                    },
                    path_params=['issueIdOrKey'],
                    path_params_schema={
                        'issueIdOrKey': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Jira issue object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique issue identifier'},
                            'key': {'type': 'string', 'description': 'Issue key (e.g., PROJ-123)'},
                            'self': {
                                'type': 'string',
                                'format': 'uri',
                                'description': 'URL of the issue',
                            },
                            'expand': {
                                'type': ['string', 'null'],
                                'description': 'Expand options that include additional issue details',
                            },
                            'fields': {
                                'type': 'object',
                                'description': "Issue fields (actual fields depend on 'fields' parameter in request)",
                                'properties': {
                                    'summary': {'type': 'string', 'description': 'Issue summary/title'},
                                    'issuetype': {
                                        'type': 'object',
                                        'description': 'Issue type information',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'id': {'type': 'string'},
                                            'description': {'type': 'string'},
                                            'iconUrl': {'type': 'string', 'format': 'uri'},
                                            'name': {'type': 'string'},
                                            'subtask': {'type': 'boolean'},
                                            'avatarId': {
                                                'type': ['integer', 'null'],
                                            },
                                            'hierarchyLevel': {
                                                'type': ['integer', 'null'],
                                            },
                                        },
                                    },
                                    'created': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Issue creation timestamp',
                                    },
                                    'updated': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Issue last update timestamp',
                                    },
                                    'project': {
                                        'type': 'object',
                                        'description': 'Project information',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'id': {'type': 'string'},
                                            'key': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'projectTypeKey': {'type': 'string'},
                                            'simplified': {'type': 'boolean'},
                                            'avatarUrls': {
                                                'type': 'object',
                                                'description': 'URLs for user avatars in different sizes',
                                                'properties': {
                                                    '16x16': {'type': 'string', 'format': 'uri'},
                                                    '24x24': {'type': 'string', 'format': 'uri'},
                                                    '32x32': {'type': 'string', 'format': 'uri'},
                                                    '48x48': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                            'projectCategory': {
                                                'type': ['object', 'null'],
                                                'properties': {
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                    'id': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                    'reporter': {
                                        'type': ['object', 'null'],
                                        'description': 'Issue reporter user information',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'accountId': {'type': 'string'},
                                            'emailAddress': {'type': 'string', 'format': 'email'},
                                            'avatarUrls': {
                                                'type': 'object',
                                                'description': 'URLs for user avatars in different sizes',
                                                'properties': {
                                                    '16x16': {'type': 'string', 'format': 'uri'},
                                                    '24x24': {'type': 'string', 'format': 'uri'},
                                                    '32x32': {'type': 'string', 'format': 'uri'},
                                                    '48x48': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                            'displayName': {'type': 'string'},
                                            'active': {'type': 'boolean'},
                                            'timeZone': {'type': 'string'},
                                            'accountType': {'type': 'string'},
                                        },
                                    },
                                    'assignee': {
                                        'type': ['object', 'null'],
                                        'description': 'Issue assignee user information (null if unassigned)',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'accountId': {'type': 'string'},
                                            'emailAddress': {'type': 'string', 'format': 'email'},
                                            'avatarUrls': {
                                                'type': 'object',
                                                'description': 'URLs for user avatars in different sizes',
                                                'properties': {
                                                    '16x16': {'type': 'string', 'format': 'uri'},
                                                    '24x24': {'type': 'string', 'format': 'uri'},
                                                    '32x32': {'type': 'string', 'format': 'uri'},
                                                    '48x48': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                            'displayName': {'type': 'string'},
                                            'active': {'type': 'boolean'},
                                            'timeZone': {'type': 'string'},
                                            'accountType': {'type': 'string'},
                                        },
                                    },
                                    'priority': {
                                        'type': ['object', 'null'],
                                        'description': 'Issue priority information',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'iconUrl': {'type': 'string', 'format': 'uri'},
                                            'name': {'type': 'string'},
                                            'id': {'type': 'string'},
                                        },
                                    },
                                    'status': {
                                        'type': 'object',
                                        'description': 'Issue status information',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'description': {'type': 'string'},
                                            'iconUrl': {'type': 'string', 'format': 'uri'},
                                            'name': {'type': 'string'},
                                            'id': {'type': 'string'},
                                            'statusCategory': {
                                                'type': 'object',
                                                'properties': {
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                    'id': {'type': 'integer'},
                                                    'key': {'type': 'string'},
                                                    'colorName': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'issues',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Jira issue object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique issue identifier'},
                    'key': {'type': 'string', 'description': 'Issue key (e.g., PROJ-123)'},
                    'self': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of the issue',
                    },
                    'expand': {
                        'type': ['string', 'null'],
                        'description': 'Expand options that include additional issue details',
                    },
                    'fields': {
                        'type': 'object',
                        'description': "Issue fields (actual fields depend on 'fields' parameter in request)",
                        'properties': {
                            'summary': {'type': 'string', 'description': 'Issue summary/title'},
                            'issuetype': {
                                'type': 'object',
                                'description': 'Issue type information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'id': {'type': 'string'},
                                    'description': {'type': 'string'},
                                    'iconUrl': {'type': 'string', 'format': 'uri'},
                                    'name': {'type': 'string'},
                                    'subtask': {'type': 'boolean'},
                                    'avatarId': {
                                        'type': ['integer', 'null'],
                                    },
                                    'hierarchyLevel': {
                                        'type': ['integer', 'null'],
                                    },
                                },
                            },
                            'created': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Issue creation timestamp',
                            },
                            'updated': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Issue last update timestamp',
                            },
                            'project': {
                                'type': 'object',
                                'description': 'Project information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'id': {'type': 'string'},
                                    'key': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'projectTypeKey': {'type': 'string'},
                                    'simplified': {'type': 'boolean'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                    'projectCategory': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'id': {'type': 'string'},
                                            'name': {'type': 'string'},
                                            'description': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                            'reporter': {
                                'type': ['object', 'null'],
                                'description': 'Issue reporter user information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'emailAddress': {'type': 'string', 'format': 'email'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                    'timeZone': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                },
                            },
                            'assignee': {
                                'type': ['object', 'null'],
                                'description': 'Issue assignee user information (null if unassigned)',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'emailAddress': {'type': 'string', 'format': 'email'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                    'timeZone': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                },
                            },
                            'priority': {
                                'type': ['object', 'null'],
                                'description': 'Issue priority information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'iconUrl': {'type': 'string', 'format': 'uri'},
                                    'name': {'type': 'string'},
                                    'id': {'type': 'string'},
                                },
                            },
                            'status': {
                                'type': 'object',
                                'description': 'Issue status information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'description': {'type': 'string'},
                                    'iconUrl': {'type': 'string', 'format': 'uri'},
                                    'name': {'type': 'string'},
                                    'id': {'type': 'string'},
                                    'statusCategory': {
                                        'type': 'object',
                                        'properties': {
                                            'self': {'type': 'string', 'format': 'uri'},
                                            'id': {'type': 'integer'},
                                            'key': {'type': 'string'},
                                            'colorName': {'type': 'string'},
                                            'name': {'type': 'string'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'issues',
            },
        ),
        EntityDefinition(
            name='projects',
            actions=[Action.SEARCH, Action.GET],
            endpoints={
                Action.SEARCH: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/project/search',
                    action=Action.SEARCH,
                    description='Search and filter projects with advanced query parameters',
                    query_params=[
                        'startAt',
                        'maxResults',
                        'orderBy',
                        'id',
                        'keys',
                        'query',
                        'typeKey',
                        'categoryId',
                        'action',
                        'expand',
                        'status',
                    ],
                    query_params_schema={
                        'startAt': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'maxResults': {'type': 'integer', 'required': False},
                        'orderBy': {
                            'type': 'string',
                            'required': False,
                            'default': 'key',
                        },
                        'id': {'type': 'array', 'required': False},
                        'keys': {'type': 'array', 'required': False},
                        'query': {'type': 'string', 'required': False},
                        'typeKey': {'type': 'string', 'required': False},
                        'categoryId': {'type': 'integer', 'required': False},
                        'action': {
                            'type': 'string',
                            'required': False,
                            'default': 'view',
                        },
                        'expand': {'type': 'string', 'required': False},
                        'status': {'type': 'array', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of projects from search results',
                        'properties': {
                            'self': {
                                'type': 'string',
                                'format': 'uri',
                                'description': 'URL of the current page',
                            },
                            'nextPage': {
                                'type': ['string', 'null'],
                                'format': 'uri',
                                'description': 'URL of the next page (if exists)',
                            },
                            'maxResults': {'type': 'integer', 'description': 'Maximum number of results per page'},
                            'startAt': {'type': 'integer', 'description': 'Index of first item returned'},
                            'total': {'type': 'integer', 'description': 'Total number of projects matching query'},
                            'isLast': {'type': 'boolean', 'description': 'Whether this is the last page'},
                            'values': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Jira project object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique project identifier'},
                                        'key': {'type': 'string', 'description': 'Project key (e.g., PROJ)'},
                                        'name': {'type': 'string', 'description': 'Project name'},
                                        'self': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of the project',
                                        },
                                        'expand': {
                                            'type': ['string', 'null'],
                                            'description': 'Expand options that were applied',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Project description (available with expand=description)',
                                        },
                                        'lead': {
                                            'type': ['object', 'null'],
                                            'description': 'Project lead user (available with expand=lead)',
                                            'properties': {
                                                'self': {'type': 'string', 'format': 'uri'},
                                                'accountId': {'type': 'string'},
                                                'accountType': {'type': 'string'},
                                                'avatarUrls': {
                                                    'type': 'object',
                                                    'description': 'URLs for user avatars in different sizes',
                                                    'properties': {
                                                        '16x16': {'type': 'string', 'format': 'uri'},
                                                        '24x24': {'type': 'string', 'format': 'uri'},
                                                        '32x32': {'type': 'string', 'format': 'uri'},
                                                        '48x48': {'type': 'string', 'format': 'uri'},
                                                    },
                                                },
                                                'displayName': {'type': 'string'},
                                                'active': {'type': 'boolean'},
                                            },
                                        },
                                        'avatarUrls': {
                                            'type': 'object',
                                            'description': 'URLs for project avatars in different sizes',
                                            'properties': {
                                                '16x16': {'type': 'string', 'format': 'uri'},
                                                '24x24': {'type': 'string', 'format': 'uri'},
                                                '32x32': {'type': 'string', 'format': 'uri'},
                                                '48x48': {'type': 'string', 'format': 'uri'},
                                            },
                                        },
                                        'projectTypeKey': {'type': 'string', 'description': 'Type of the project (e.g., software, service_desk, business)'},
                                        'simplified': {'type': 'boolean', 'description': 'Whether the project uses simplified workflow'},
                                        'style': {'type': 'string', 'description': 'Project style'},
                                        'isPrivate': {'type': 'boolean', 'description': 'Whether the project is private'},
                                        'properties': {
                                            'type': 'object',
                                            'description': 'Custom properties for the project',
                                            'additionalProperties': True,
                                        },
                                        'projectCategory': {
                                            'type': ['object', 'null'],
                                            'description': 'Project category information',
                                            'properties': {
                                                'self': {'type': 'string', 'format': 'uri'},
                                                'id': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'description': {'type': 'string'},
                                            },
                                        },
                                        'entityId': {
                                            'type': ['string', 'null'],
                                            'description': 'Entity ID',
                                        },
                                        'uuid': {
                                            'type': ['string', 'null'],
                                            'description': 'UUID of the project',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'URL for the project (available with expand=url)',
                                        },
                                        'assigneeType': {
                                            'type': ['string', 'null'],
                                            'description': 'Default assignee type for the project',
                                        },
                                        'components': {
                                            'type': ['array', 'null'],
                                            'description': 'Project components',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                    'id': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                    'isAssigneeTypeValid': {'type': 'boolean'},
                                                },
                                            },
                                        },
                                        'issueTypes': {
                                            'type': ['array', 'null'],
                                            'description': 'Issue types available in the project (available with expand=issueTypes)',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                    'id': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                    'iconUrl': {'type': 'string', 'format': 'uri'},
                                                    'name': {'type': 'string'},
                                                    'subtask': {'type': 'boolean'},
                                                    'avatarId': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'hierarchyLevel': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'versions': {
                                            'type': ['array', 'null'],
                                            'description': 'Project versions',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                    'id': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                    'archived': {'type': 'boolean'},
                                                    'released': {'type': 'boolean'},
                                                    'startDate': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date',
                                                    },
                                                    'releaseDate': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date',
                                                    },
                                                    'overdue': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'userStartDate': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'userReleaseDate': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'projectId': {'type': 'integer'},
                                                },
                                            },
                                        },
                                        'roles': {
                                            'type': ['object', 'null'],
                                            'description': 'Project roles and their URLs',
                                            'additionalProperties': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                    'x-airbyte-entity-name': 'projects',
                                },
                                'description': 'Array of project objects',
                            },
                        },
                    },
                    record_extractor='$.values',
                    meta_extractor={'nextPage': '$.nextPage', 'total': '$.total'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/project/{projectIdOrKey}',
                    action=Action.GET,
                    description='Retrieve a single project by its ID or key',
                    query_params=['expand', 'properties'],
                    query_params_schema={
                        'expand': {'type': 'string', 'required': False},
                        'properties': {'type': 'string', 'required': False},
                    },
                    path_params=['projectIdOrKey'],
                    path_params_schema={
                        'projectIdOrKey': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Jira project object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique project identifier'},
                            'key': {'type': 'string', 'description': 'Project key (e.g., PROJ)'},
                            'name': {'type': 'string', 'description': 'Project name'},
                            'self': {
                                'type': 'string',
                                'format': 'uri',
                                'description': 'URL of the project',
                            },
                            'expand': {
                                'type': ['string', 'null'],
                                'description': 'Expand options that were applied',
                            },
                            'description': {
                                'type': ['string', 'null'],
                                'description': 'Project description (available with expand=description)',
                            },
                            'lead': {
                                'type': ['object', 'null'],
                                'description': 'Project lead user (available with expand=lead)',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                },
                            },
                            'avatarUrls': {
                                'type': 'object',
                                'description': 'URLs for project avatars in different sizes',
                                'properties': {
                                    '16x16': {'type': 'string', 'format': 'uri'},
                                    '24x24': {'type': 'string', 'format': 'uri'},
                                    '32x32': {'type': 'string', 'format': 'uri'},
                                    '48x48': {'type': 'string', 'format': 'uri'},
                                },
                            },
                            'projectTypeKey': {'type': 'string', 'description': 'Type of the project (e.g., software, service_desk, business)'},
                            'simplified': {'type': 'boolean', 'description': 'Whether the project uses simplified workflow'},
                            'style': {'type': 'string', 'description': 'Project style'},
                            'isPrivate': {'type': 'boolean', 'description': 'Whether the project is private'},
                            'properties': {
                                'type': 'object',
                                'description': 'Custom properties for the project',
                                'additionalProperties': True,
                            },
                            'projectCategory': {
                                'type': ['object', 'null'],
                                'description': 'Project category information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'id': {'type': 'string'},
                                    'name': {'type': 'string'},
                                    'description': {'type': 'string'},
                                },
                            },
                            'entityId': {
                                'type': ['string', 'null'],
                                'description': 'Entity ID',
                            },
                            'uuid': {
                                'type': ['string', 'null'],
                                'description': 'UUID of the project',
                            },
                            'url': {
                                'type': ['string', 'null'],
                                'description': 'URL for the project (available with expand=url)',
                            },
                            'assigneeType': {
                                'type': ['string', 'null'],
                                'description': 'Default assignee type for the project',
                            },
                            'components': {
                                'type': ['array', 'null'],
                                'description': 'Project components',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'self': {'type': 'string', 'format': 'uri'},
                                        'id': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'description': {'type': 'string'},
                                        'isAssigneeTypeValid': {'type': 'boolean'},
                                    },
                                },
                            },
                            'issueTypes': {
                                'type': ['array', 'null'],
                                'description': 'Issue types available in the project (available with expand=issueTypes)',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'self': {'type': 'string', 'format': 'uri'},
                                        'id': {'type': 'string'},
                                        'description': {'type': 'string'},
                                        'iconUrl': {'type': 'string', 'format': 'uri'},
                                        'name': {'type': 'string'},
                                        'subtask': {'type': 'boolean'},
                                        'avatarId': {
                                            'type': ['integer', 'null'],
                                        },
                                        'hierarchyLevel': {
                                            'type': ['integer', 'null'],
                                        },
                                    },
                                },
                            },
                            'versions': {
                                'type': ['array', 'null'],
                                'description': 'Project versions',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'self': {'type': 'string', 'format': 'uri'},
                                        'id': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'description': {'type': 'string'},
                                        'archived': {'type': 'boolean'},
                                        'released': {'type': 'boolean'},
                                        'startDate': {
                                            'type': ['string', 'null'],
                                            'format': 'date',
                                        },
                                        'releaseDate': {
                                            'type': ['string', 'null'],
                                            'format': 'date',
                                        },
                                        'overdue': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'userStartDate': {
                                            'type': ['string', 'null'],
                                        },
                                        'userReleaseDate': {
                                            'type': ['string', 'null'],
                                        },
                                        'projectId': {'type': 'integer'},
                                    },
                                },
                            },
                            'roles': {
                                'type': ['object', 'null'],
                                'description': 'Project roles and their URLs',
                                'additionalProperties': {'type': 'string', 'format': 'uri'},
                            },
                        },
                        'x-airbyte-entity-name': 'projects',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Jira project object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique project identifier'},
                    'key': {'type': 'string', 'description': 'Project key (e.g., PROJ)'},
                    'name': {'type': 'string', 'description': 'Project name'},
                    'self': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of the project',
                    },
                    'expand': {
                        'type': ['string', 'null'],
                        'description': 'Expand options that were applied',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Project description (available with expand=description)',
                    },
                    'lead': {
                        'type': ['object', 'null'],
                        'description': 'Project lead user (available with expand=lead)',
                        'properties': {
                            'self': {'type': 'string', 'format': 'uri'},
                            'accountId': {'type': 'string'},
                            'accountType': {'type': 'string'},
                            'avatarUrls': {
                                'type': 'object',
                                'description': 'URLs for user avatars in different sizes',
                                'properties': {
                                    '16x16': {'type': 'string', 'format': 'uri'},
                                    '24x24': {'type': 'string', 'format': 'uri'},
                                    '32x32': {'type': 'string', 'format': 'uri'},
                                    '48x48': {'type': 'string', 'format': 'uri'},
                                },
                            },
                            'displayName': {'type': 'string'},
                            'active': {'type': 'boolean'},
                        },
                    },
                    'avatarUrls': {
                        'type': 'object',
                        'description': 'URLs for project avatars in different sizes',
                        'properties': {
                            '16x16': {'type': 'string', 'format': 'uri'},
                            '24x24': {'type': 'string', 'format': 'uri'},
                            '32x32': {'type': 'string', 'format': 'uri'},
                            '48x48': {'type': 'string', 'format': 'uri'},
                        },
                    },
                    'projectTypeKey': {'type': 'string', 'description': 'Type of the project (e.g., software, service_desk, business)'},
                    'simplified': {'type': 'boolean', 'description': 'Whether the project uses simplified workflow'},
                    'style': {'type': 'string', 'description': 'Project style'},
                    'isPrivate': {'type': 'boolean', 'description': 'Whether the project is private'},
                    'properties': {
                        'type': 'object',
                        'description': 'Custom properties for the project',
                        'additionalProperties': True,
                    },
                    'projectCategory': {
                        'type': ['object', 'null'],
                        'description': 'Project category information',
                        'properties': {
                            'self': {'type': 'string', 'format': 'uri'},
                            'id': {'type': 'string'},
                            'name': {'type': 'string'},
                            'description': {'type': 'string'},
                        },
                    },
                    'entityId': {
                        'type': ['string', 'null'],
                        'description': 'Entity ID',
                    },
                    'uuid': {
                        'type': ['string', 'null'],
                        'description': 'UUID of the project',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'URL for the project (available with expand=url)',
                    },
                    'assigneeType': {
                        'type': ['string', 'null'],
                        'description': 'Default assignee type for the project',
                    },
                    'components': {
                        'type': ['array', 'null'],
                        'description': 'Project components',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'self': {'type': 'string', 'format': 'uri'},
                                'id': {'type': 'string'},
                                'name': {'type': 'string'},
                                'description': {'type': 'string'},
                                'isAssigneeTypeValid': {'type': 'boolean'},
                            },
                        },
                    },
                    'issueTypes': {
                        'type': ['array', 'null'],
                        'description': 'Issue types available in the project (available with expand=issueTypes)',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'self': {'type': 'string', 'format': 'uri'},
                                'id': {'type': 'string'},
                                'description': {'type': 'string'},
                                'iconUrl': {'type': 'string', 'format': 'uri'},
                                'name': {'type': 'string'},
                                'subtask': {'type': 'boolean'},
                                'avatarId': {
                                    'type': ['integer', 'null'],
                                },
                                'hierarchyLevel': {
                                    'type': ['integer', 'null'],
                                },
                            },
                        },
                    },
                    'versions': {
                        'type': ['array', 'null'],
                        'description': 'Project versions',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'self': {'type': 'string', 'format': 'uri'},
                                'id': {'type': 'string'},
                                'name': {'type': 'string'},
                                'description': {'type': 'string'},
                                'archived': {'type': 'boolean'},
                                'released': {'type': 'boolean'},
                                'startDate': {
                                    'type': ['string', 'null'],
                                    'format': 'date',
                                },
                                'releaseDate': {
                                    'type': ['string', 'null'],
                                    'format': 'date',
                                },
                                'overdue': {
                                    'type': ['boolean', 'null'],
                                },
                                'userStartDate': {
                                    'type': ['string', 'null'],
                                },
                                'userReleaseDate': {
                                    'type': ['string', 'null'],
                                },
                                'projectId': {'type': 'integer'},
                            },
                        },
                    },
                    'roles': {
                        'type': ['object', 'null'],
                        'description': 'Project roles and their URLs',
                        'additionalProperties': {'type': 'string', 'format': 'uri'},
                    },
                },
                'x-airbyte-entity-name': 'projects',
            },
        ),
        EntityDefinition(
            name='users',
            actions=[Action.GET, Action.LIST, Action.SEARCH],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/user',
                    action=Action.GET,
                    description='Retrieve a single user by their account ID',
                    query_params=['accountId', 'expand'],
                    query_params_schema={
                        'accountId': {'type': 'string', 'required': True},
                        'expand': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Jira user object',
                        'properties': {
                            'self': {
                                'type': 'string',
                                'format': 'uri',
                                'description': 'URL of the user',
                            },
                            'accountId': {'type': 'string', 'description': 'Unique account identifier'},
                            'accountType': {'type': 'string', 'description': 'Type of account (atlassian, app, etc.)'},
                            'emailAddress': {
                                'type': ['string', 'null'],
                                'format': 'email',
                                'description': 'Email address of the user',
                            },
                            'avatarUrls': {
                                'type': 'object',
                                'description': 'URLs for user avatars in different sizes',
                                'properties': {
                                    '16x16': {'type': 'string', 'format': 'uri'},
                                    '24x24': {'type': 'string', 'format': 'uri'},
                                    '32x32': {'type': 'string', 'format': 'uri'},
                                    '48x48': {'type': 'string', 'format': 'uri'},
                                },
                            },
                            'displayName': {'type': 'string', 'description': 'Display name of the user'},
                            'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                            'timeZone': {
                                'type': ['string', 'null'],
                                'description': 'Time zone of the user',
                            },
                            'locale': {
                                'type': ['string', 'null'],
                                'description': 'Locale of the user',
                            },
                            'expand': {
                                'type': ['string', 'null'],
                                'description': 'Expand options that were applied',
                            },
                            'groups': {
                                'type': ['object', 'null'],
                                'description': 'User groups (available with expand=groups)',
                                'properties': {
                                    'size': {'type': 'integer', 'description': 'Number of groups'},
                                    'items': {
                                        'type': 'array',
                                        'description': 'Array of group objects',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'name': {'type': 'string'},
                                                'groupId': {'type': 'string'},
                                                'self': {'type': 'string', 'format': 'uri'},
                                            },
                                        },
                                    },
                                },
                            },
                            'applicationRoles': {
                                'type': ['object', 'null'],
                                'description': 'User application roles (available with expand=applicationRoles)',
                                'properties': {
                                    'size': {'type': 'integer', 'description': 'Number of application roles'},
                                    'items': {
                                        'type': 'array',
                                        'description': 'Array of application role objects',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'key': {'type': 'string'},
                                                'name': {'type': 'string'},
                                                'groups': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                },
                                                'groupDetails': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'groupId': {'type': 'string'},
                                                            'self': {'type': 'string', 'format': 'uri'},
                                                        },
                                                    },
                                                },
                                                'defaultGroups': {
                                                    'type': 'array',
                                                    'items': {'type': 'string'},
                                                },
                                                'defaultGroupsDetails': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'groupId': {'type': 'string'},
                                                            'self': {'type': 'string', 'format': 'uri'},
                                                        },
                                                    },
                                                },
                                                'selectedByDefault': {'type': 'boolean'},
                                                'defined': {'type': 'boolean'},
                                                'numberOfSeats': {'type': 'integer'},
                                                'remainingSeats': {'type': 'integer'},
                                                'userCount': {'type': 'integer'},
                                                'userCountDescription': {'type': 'string'},
                                                'hasUnlimitedSeats': {'type': 'boolean'},
                                                'platform': {'type': 'boolean'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'users',
                    },
                ),
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/users',
                    action=Action.LIST,
                    description='Returns a paginated list of users',
                    query_params=['startAt', 'maxResults'],
                    query_params_schema={
                        'startAt': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Jira user object',
                            'properties': {
                                'self': {
                                    'type': 'string',
                                    'format': 'uri',
                                    'description': 'URL of the user',
                                },
                                'accountId': {'type': 'string', 'description': 'Unique account identifier'},
                                'accountType': {'type': 'string', 'description': 'Type of account (atlassian, app, etc.)'},
                                'emailAddress': {
                                    'type': ['string', 'null'],
                                    'format': 'email',
                                    'description': 'Email address of the user',
                                },
                                'avatarUrls': {
                                    'type': 'object',
                                    'description': 'URLs for user avatars in different sizes',
                                    'properties': {
                                        '16x16': {'type': 'string', 'format': 'uri'},
                                        '24x24': {'type': 'string', 'format': 'uri'},
                                        '32x32': {'type': 'string', 'format': 'uri'},
                                        '48x48': {'type': 'string', 'format': 'uri'},
                                    },
                                },
                                'displayName': {'type': 'string', 'description': 'Display name of the user'},
                                'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                                'timeZone': {
                                    'type': ['string', 'null'],
                                    'description': 'Time zone of the user',
                                },
                                'locale': {
                                    'type': ['string', 'null'],
                                    'description': 'Locale of the user',
                                },
                                'expand': {
                                    'type': ['string', 'null'],
                                    'description': 'Expand options that were applied',
                                },
                                'groups': {
                                    'type': ['object', 'null'],
                                    'description': 'User groups (available with expand=groups)',
                                    'properties': {
                                        'size': {'type': 'integer', 'description': 'Number of groups'},
                                        'items': {
                                            'type': 'array',
                                            'description': 'Array of group objects',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'groupId': {'type': 'string'},
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                        },
                                    },
                                },
                                'applicationRoles': {
                                    'type': ['object', 'null'],
                                    'description': 'User application roles (available with expand=applicationRoles)',
                                    'properties': {
                                        'size': {'type': 'integer', 'description': 'Number of application roles'},
                                        'items': {
                                            'type': 'array',
                                            'description': 'Array of application role objects',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'key': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'groups': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'groupDetails': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'name': {'type': 'string'},
                                                                'groupId': {'type': 'string'},
                                                                'self': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                    },
                                                    'defaultGroups': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'defaultGroupsDetails': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'name': {'type': 'string'},
                                                                'groupId': {'type': 'string'},
                                                                'self': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                    },
                                                    'selectedByDefault': {'type': 'boolean'},
                                                    'defined': {'type': 'boolean'},
                                                    'numberOfSeats': {'type': 'integer'},
                                                    'remainingSeats': {'type': 'integer'},
                                                    'userCount': {'type': 'integer'},
                                                    'userCountDescription': {'type': 'string'},
                                                    'hasUnlimitedSeats': {'type': 'boolean'},
                                                    'platform': {'type': 'boolean'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'users',
                        },
                    },
                ),
                Action.SEARCH: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/user/search',
                    action=Action.SEARCH,
                    description='Search for users using a query string',
                    query_params=[
                        'query',
                        'startAt',
                        'maxResults',
                        'accountId',
                        'property',
                    ],
                    query_params_schema={
                        'query': {'type': 'string', 'required': False},
                        'startAt': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'accountId': {'type': 'string', 'required': False},
                        'property': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Jira user object',
                            'properties': {
                                'self': {
                                    'type': 'string',
                                    'format': 'uri',
                                    'description': 'URL of the user',
                                },
                                'accountId': {'type': 'string', 'description': 'Unique account identifier'},
                                'accountType': {'type': 'string', 'description': 'Type of account (atlassian, app, etc.)'},
                                'emailAddress': {
                                    'type': ['string', 'null'],
                                    'format': 'email',
                                    'description': 'Email address of the user',
                                },
                                'avatarUrls': {
                                    'type': 'object',
                                    'description': 'URLs for user avatars in different sizes',
                                    'properties': {
                                        '16x16': {'type': 'string', 'format': 'uri'},
                                        '24x24': {'type': 'string', 'format': 'uri'},
                                        '32x32': {'type': 'string', 'format': 'uri'},
                                        '48x48': {'type': 'string', 'format': 'uri'},
                                    },
                                },
                                'displayName': {'type': 'string', 'description': 'Display name of the user'},
                                'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                                'timeZone': {
                                    'type': ['string', 'null'],
                                    'description': 'Time zone of the user',
                                },
                                'locale': {
                                    'type': ['string', 'null'],
                                    'description': 'Locale of the user',
                                },
                                'expand': {
                                    'type': ['string', 'null'],
                                    'description': 'Expand options that were applied',
                                },
                                'groups': {
                                    'type': ['object', 'null'],
                                    'description': 'User groups (available with expand=groups)',
                                    'properties': {
                                        'size': {'type': 'integer', 'description': 'Number of groups'},
                                        'items': {
                                            'type': 'array',
                                            'description': 'Array of group objects',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'groupId': {'type': 'string'},
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                        },
                                    },
                                },
                                'applicationRoles': {
                                    'type': ['object', 'null'],
                                    'description': 'User application roles (available with expand=applicationRoles)',
                                    'properties': {
                                        'size': {'type': 'integer', 'description': 'Number of application roles'},
                                        'items': {
                                            'type': 'array',
                                            'description': 'Array of application role objects',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'key': {'type': 'string'},
                                                    'name': {'type': 'string'},
                                                    'groups': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'groupDetails': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'name': {'type': 'string'},
                                                                'groupId': {'type': 'string'},
                                                                'self': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                    },
                                                    'defaultGroups': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'defaultGroupsDetails': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'name': {'type': 'string'},
                                                                'groupId': {'type': 'string'},
                                                                'self': {'type': 'string', 'format': 'uri'},
                                                            },
                                                        },
                                                    },
                                                    'selectedByDefault': {'type': 'boolean'},
                                                    'defined': {'type': 'boolean'},
                                                    'numberOfSeats': {'type': 'integer'},
                                                    'remainingSeats': {'type': 'integer'},
                                                    'userCount': {'type': 'integer'},
                                                    'userCountDescription': {'type': 'string'},
                                                    'hasUnlimitedSeats': {'type': 'boolean'},
                                                    'platform': {'type': 'boolean'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'users',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Jira user object',
                'properties': {
                    'self': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of the user',
                    },
                    'accountId': {'type': 'string', 'description': 'Unique account identifier'},
                    'accountType': {'type': 'string', 'description': 'Type of account (atlassian, app, etc.)'},
                    'emailAddress': {
                        'type': ['string', 'null'],
                        'format': 'email',
                        'description': 'Email address of the user',
                    },
                    'avatarUrls': {
                        'type': 'object',
                        'description': 'URLs for user avatars in different sizes',
                        'properties': {
                            '16x16': {'type': 'string', 'format': 'uri'},
                            '24x24': {'type': 'string', 'format': 'uri'},
                            '32x32': {'type': 'string', 'format': 'uri'},
                            '48x48': {'type': 'string', 'format': 'uri'},
                        },
                    },
                    'displayName': {'type': 'string', 'description': 'Display name of the user'},
                    'active': {'type': 'boolean', 'description': 'Whether the user is active'},
                    'timeZone': {
                        'type': ['string', 'null'],
                        'description': 'Time zone of the user',
                    },
                    'locale': {
                        'type': ['string', 'null'],
                        'description': 'Locale of the user',
                    },
                    'expand': {
                        'type': ['string', 'null'],
                        'description': 'Expand options that were applied',
                    },
                    'groups': {
                        'type': ['object', 'null'],
                        'description': 'User groups (available with expand=groups)',
                        'properties': {
                            'size': {'type': 'integer', 'description': 'Number of groups'},
                            'items': {
                                'type': 'array',
                                'description': 'Array of group objects',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                        'groupId': {'type': 'string'},
                                        'self': {'type': 'string', 'format': 'uri'},
                                    },
                                },
                            },
                        },
                    },
                    'applicationRoles': {
                        'type': ['object', 'null'],
                        'description': 'User application roles (available with expand=applicationRoles)',
                        'properties': {
                            'size': {'type': 'integer', 'description': 'Number of application roles'},
                            'items': {
                                'type': 'array',
                                'description': 'Array of application role objects',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'key': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'groups': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                        },
                                        'groupDetails': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'groupId': {'type': 'string'},
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                        },
                                        'defaultGroups': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                        },
                                        'defaultGroupsDetails': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'groupId': {'type': 'string'},
                                                    'self': {'type': 'string', 'format': 'uri'},
                                                },
                                            },
                                        },
                                        'selectedByDefault': {'type': 'boolean'},
                                        'defined': {'type': 'boolean'},
                                        'numberOfSeats': {'type': 'integer'},
                                        'remainingSeats': {'type': 'integer'},
                                        'userCount': {'type': 'integer'},
                                        'userCountDescription': {'type': 'string'},
                                        'hasUnlimitedSeats': {'type': 'boolean'},
                                        'platform': {'type': 'boolean'},
                                    },
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'users',
            },
        ),
        EntityDefinition(
            name='issue_fields',
            actions=[Action.LIST, Action.SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/field',
                    action=Action.LIST,
                    description='Returns a list of all custom and system fields',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Jira issue field object (custom or system field)',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Field ID (e.g., customfield_10000 or summary)'},
                                'key': {
                                    'type': ['string', 'null'],
                                    'description': 'Field key (e.g., summary, customfield_10000)',
                                },
                                'name': {'type': 'string', 'description': 'Field name (e.g., Summary, Story Points)'},
                                'custom': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether this is a custom field',
                                },
                                'orderable': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the field can be used for ordering',
                                },
                                'navigable': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the field is navigable',
                                },
                                'searchable': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the field is searchable',
                                },
                                'clauseNames': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'string'},
                                    'description': 'JQL clause names for this field',
                                },
                                'schema': {
                                    'type': ['object', 'null'],
                                    'description': 'Schema information for the field',
                                    'properties': {
                                        'type': {'type': 'string', 'description': 'Field type (e.g., string, number, array)'},
                                        'system': {
                                            'type': ['string', 'null'],
                                            'description': 'System field identifier',
                                        },
                                        'items': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of items in array fields',
                                        },
                                        'custom': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom field type identifier',
                                        },
                                        'customId': {
                                            'type': ['integer', 'null'],
                                            'description': 'Custom field ID',
                                        },
                                        'configuration': {
                                            'type': ['object', 'null'],
                                            'description': 'Field configuration',
                                            'additionalProperties': True,
                                        },
                                    },
                                },
                                'untranslatedName': {
                                    'type': ['string', 'null'],
                                    'description': 'Untranslated field name',
                                },
                                'typeDisplayName': {
                                    'type': ['string', 'null'],
                                    'description': 'Display name of the field type',
                                },
                                'description': {
                                    'type': ['string', 'null'],
                                    'description': 'Description of the field',
                                },
                                'searcherKey': {
                                    'type': ['string', 'null'],
                                    'description': 'Searcher key for the field (available with expand=searcherKey)',
                                },
                                'screensCount': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of screens where this field is used (available with expand=screensCount)',
                                },
                                'contextsCount': {
                                    'type': ['integer', 'null'],
                                    'description': 'Number of contexts where this field is used (available with expand=contextsCount)',
                                },
                                'isLocked': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the field is locked (available with expand=isLocked)',
                                },
                                'lastUsed': {
                                    'type': ['string', 'null'],
                                    'description': 'Date when the field was last used (available with expand=lastUsed)',
                                },
                            },
                            'x-airbyte-entity-name': 'issue_fields',
                        },
                    },
                ),
                Action.SEARCH: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/field/search',
                    action=Action.SEARCH,
                    description='Search and filter issue fields with query parameters',
                    query_params=[
                        'startAt',
                        'maxResults',
                        'type',
                        'id',
                        'query',
                        'orderBy',
                        'expand',
                    ],
                    query_params_schema={
                        'startAt': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'type': {'type': 'array', 'required': False},
                        'id': {'type': 'array', 'required': False},
                        'query': {'type': 'string', 'required': False},
                        'orderBy': {'type': 'string', 'required': False},
                        'expand': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated search results for issue fields',
                        'properties': {
                            'maxResults': {'type': 'integer', 'description': 'Maximum number of results per page'},
                            'startAt': {'type': 'integer', 'description': 'Index of first item returned'},
                            'total': {'type': 'integer', 'description': 'Total number of fields matching query'},
                            'isLast': {'type': 'boolean', 'description': 'Whether this is the last page'},
                            'values': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Jira issue field object (custom or system field)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Field ID (e.g., customfield_10000 or summary)'},
                                        'key': {
                                            'type': ['string', 'null'],
                                            'description': 'Field key (e.g., summary, customfield_10000)',
                                        },
                                        'name': {'type': 'string', 'description': 'Field name (e.g., Summary, Story Points)'},
                                        'custom': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is a custom field',
                                        },
                                        'orderable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the field can be used for ordering',
                                        },
                                        'navigable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the field is navigable',
                                        },
                                        'searchable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the field is searchable',
                                        },
                                        'clauseNames': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'JQL clause names for this field',
                                        },
                                        'schema': {
                                            'type': ['object', 'null'],
                                            'description': 'Schema information for the field',
                                            'properties': {
                                                'type': {'type': 'string', 'description': 'Field type (e.g., string, number, array)'},
                                                'system': {
                                                    'type': ['string', 'null'],
                                                    'description': 'System field identifier',
                                                },
                                                'items': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Type of items in array fields',
                                                },
                                                'custom': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Custom field type identifier',
                                                },
                                                'customId': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Custom field ID',
                                                },
                                                'configuration': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Field configuration',
                                                    'additionalProperties': True,
                                                },
                                            },
                                        },
                                        'untranslatedName': {
                                            'type': ['string', 'null'],
                                            'description': 'Untranslated field name',
                                        },
                                        'typeDisplayName': {
                                            'type': ['string', 'null'],
                                            'description': 'Display name of the field type',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Description of the field',
                                        },
                                        'searcherKey': {
                                            'type': ['string', 'null'],
                                            'description': 'Searcher key for the field (available with expand=searcherKey)',
                                        },
                                        'screensCount': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of screens where this field is used (available with expand=screensCount)',
                                        },
                                        'contextsCount': {
                                            'type': ['integer', 'null'],
                                            'description': 'Number of contexts where this field is used (available with expand=contextsCount)',
                                        },
                                        'isLocked': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the field is locked (available with expand=isLocked)',
                                        },
                                        'lastUsed': {
                                            'type': ['string', 'null'],
                                            'description': 'Date when the field was last used (available with expand=lastUsed)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'issue_fields',
                                },
                                'description': 'Array of field objects',
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Jira issue field object (custom or system field)',
                'properties': {
                    'id': {'type': 'string', 'description': 'Field ID (e.g., customfield_10000 or summary)'},
                    'key': {
                        'type': ['string', 'null'],
                        'description': 'Field key (e.g., summary, customfield_10000)',
                    },
                    'name': {'type': 'string', 'description': 'Field name (e.g., Summary, Story Points)'},
                    'custom': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is a custom field',
                    },
                    'orderable': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the field can be used for ordering',
                    },
                    'navigable': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the field is navigable',
                    },
                    'searchable': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the field is searchable',
                    },
                    'clauseNames': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'JQL clause names for this field',
                    },
                    'schema': {
                        'type': ['object', 'null'],
                        'description': 'Schema information for the field',
                        'properties': {
                            'type': {'type': 'string', 'description': 'Field type (e.g., string, number, array)'},
                            'system': {
                                'type': ['string', 'null'],
                                'description': 'System field identifier',
                            },
                            'items': {
                                'type': ['string', 'null'],
                                'description': 'Type of items in array fields',
                            },
                            'custom': {
                                'type': ['string', 'null'],
                                'description': 'Custom field type identifier',
                            },
                            'customId': {
                                'type': ['integer', 'null'],
                                'description': 'Custom field ID',
                            },
                            'configuration': {
                                'type': ['object', 'null'],
                                'description': 'Field configuration',
                                'additionalProperties': True,
                            },
                        },
                    },
                    'untranslatedName': {
                        'type': ['string', 'null'],
                        'description': 'Untranslated field name',
                    },
                    'typeDisplayName': {
                        'type': ['string', 'null'],
                        'description': 'Display name of the field type',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'Description of the field',
                    },
                    'searcherKey': {
                        'type': ['string', 'null'],
                        'description': 'Searcher key for the field (available with expand=searcherKey)',
                    },
                    'screensCount': {
                        'type': ['integer', 'null'],
                        'description': 'Number of screens where this field is used (available with expand=screensCount)',
                    },
                    'contextsCount': {
                        'type': ['integer', 'null'],
                        'description': 'Number of contexts where this field is used (available with expand=contextsCount)',
                    },
                    'isLocked': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the field is locked (available with expand=isLocked)',
                    },
                    'lastUsed': {
                        'type': ['string', 'null'],
                        'description': 'Date when the field was last used (available with expand=lastUsed)',
                    },
                },
                'x-airbyte-entity-name': 'issue_fields',
            },
        ),
        EntityDefinition(
            name='issue_comments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/issue/{issueIdOrKey}/comment',
                    action=Action.LIST,
                    description='Retrieve all comments for a specific issue',
                    query_params=[
                        'startAt',
                        'maxResults',
                        'orderBy',
                        'expand',
                    ],
                    query_params_schema={
                        'startAt': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                        'orderBy': {'type': 'string', 'required': False},
                        'expand': {'type': 'string', 'required': False},
                    },
                    path_params=['issueIdOrKey'],
                    path_params_schema={
                        'issueIdOrKey': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of issue comments',
                        'properties': {
                            'startAt': {'type': 'integer', 'description': 'Index of first item returned'},
                            'maxResults': {'type': 'integer', 'description': 'Maximum number of results per page'},
                            'total': {'type': 'integer', 'description': 'Total number of comments'},
                            'comments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Jira issue comment object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique comment identifier'},
                                        'self': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of the comment',
                                        },
                                        'body': {
                                            'type': 'object',
                                            'description': 'Comment content in ADF (Atlassian Document Format)',
                                            'properties': {
                                                'type': {'type': 'string', 'description': "Document type (always 'doc')"},
                                                'version': {'type': 'integer', 'description': 'ADF version'},
                                                'content': {
                                                    'type': 'array',
                                                    'description': 'Array of content blocks',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'description': "Block type (e.g., 'paragraph')"},
                                                            'content': {
                                                                'type': 'array',
                                                                'description': 'Nested content items',
                                                                'items': {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'type': {'type': 'string', 'description': "Content type (e.g., 'text')"},
                                                                        'text': {'type': 'string', 'description': 'Text content'},
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'additionalProperties': False,
                                        },
                                        'author': {
                                            'type': 'object',
                                            'description': 'Comment author user information',
                                            'properties': {
                                                'self': {'type': 'string', 'format': 'uri'},
                                                'accountId': {'type': 'string'},
                                                'emailAddress': {'type': 'string', 'format': 'email'},
                                                'displayName': {'type': 'string'},
                                                'active': {'type': 'boolean'},
                                                'timeZone': {'type': 'string'},
                                                'accountType': {'type': 'string'},
                                                'avatarUrls': {
                                                    'type': 'object',
                                                    'description': 'URLs for user avatars in different sizes',
                                                    'properties': {
                                                        '16x16': {'type': 'string', 'format': 'uri'},
                                                        '24x24': {'type': 'string', 'format': 'uri'},
                                                        '32x32': {'type': 'string', 'format': 'uri'},
                                                        '48x48': {'type': 'string', 'format': 'uri'},
                                                    },
                                                },
                                            },
                                        },
                                        'updateAuthor': {
                                            'type': 'object',
                                            'description': 'User who last updated the comment',
                                            'properties': {
                                                'self': {'type': 'string', 'format': 'uri'},
                                                'accountId': {'type': 'string'},
                                                'emailAddress': {'type': 'string', 'format': 'email'},
                                                'displayName': {'type': 'string'},
                                                'active': {'type': 'boolean'},
                                                'timeZone': {'type': 'string'},
                                                'accountType': {'type': 'string'},
                                                'avatarUrls': {
                                                    'type': 'object',
                                                    'description': 'URLs for user avatars in different sizes',
                                                    'properties': {
                                                        '16x16': {'type': 'string', 'format': 'uri'},
                                                        '24x24': {'type': 'string', 'format': 'uri'},
                                                        '32x32': {'type': 'string', 'format': 'uri'},
                                                        '48x48': {'type': 'string', 'format': 'uri'},
                                                    },
                                                },
                                            },
                                        },
                                        'created': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Comment creation timestamp',
                                        },
                                        'updated': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Comment last update timestamp',
                                        },
                                        'jsdPublic': {'type': 'boolean', 'description': 'Whether the comment is public in Jira Service Desk'},
                                        'visibility': {
                                            'type': ['object', 'null'],
                                            'description': 'Visibility restrictions for the comment',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'value': {'type': 'string'},
                                                'identifier': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'renderedBody': {
                                            'type': ['string', 'null'],
                                            'description': 'Rendered comment body as HTML (available with expand=renderedBody)',
                                        },
                                        'properties': {
                                            'type': ['array', 'null'],
                                            'description': 'Comment properties (available with expand=properties)',
                                            'items': {'type': 'object', 'additionalProperties': True},
                                        },
                                    },
                                    'x-airbyte-entity-name': 'issue_comments',
                                },
                                'description': 'Array of comment objects',
                            },
                        },
                    },
                    record_extractor='$.comments',
                    meta_extractor={
                        'startAt': '$.startAt',
                        'maxResults': '$.maxResults',
                        'total': '$.total',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/issue/{issueIdOrKey}/comment/{commentId}',
                    action=Action.GET,
                    description='Retrieve a single comment by its ID',
                    query_params=['expand'],
                    query_params_schema={
                        'expand': {'type': 'string', 'required': False},
                    },
                    path_params=['issueIdOrKey', 'commentId'],
                    path_params_schema={
                        'issueIdOrKey': {'type': 'string', 'required': True},
                        'commentId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Jira issue comment object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique comment identifier'},
                            'self': {
                                'type': 'string',
                                'format': 'uri',
                                'description': 'URL of the comment',
                            },
                            'body': {
                                'type': 'object',
                                'description': 'Comment content in ADF (Atlassian Document Format)',
                                'properties': {
                                    'type': {'type': 'string', 'description': "Document type (always 'doc')"},
                                    'version': {'type': 'integer', 'description': 'ADF version'},
                                    'content': {
                                        'type': 'array',
                                        'description': 'Array of content blocks',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'description': "Block type (e.g., 'paragraph')"},
                                                'content': {
                                                    'type': 'array',
                                                    'description': 'Nested content items',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'description': "Content type (e.g., 'text')"},
                                                            'text': {'type': 'string', 'description': 'Text content'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'additionalProperties': False,
                            },
                            'author': {
                                'type': 'object',
                                'description': 'Comment author user information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'emailAddress': {'type': 'string', 'format': 'email'},
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                    'timeZone': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                },
                            },
                            'updateAuthor': {
                                'type': 'object',
                                'description': 'User who last updated the comment',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'emailAddress': {'type': 'string', 'format': 'email'},
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                    'timeZone': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                },
                            },
                            'created': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Comment creation timestamp',
                            },
                            'updated': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Comment last update timestamp',
                            },
                            'jsdPublic': {'type': 'boolean', 'description': 'Whether the comment is public in Jira Service Desk'},
                            'visibility': {
                                'type': ['object', 'null'],
                                'description': 'Visibility restrictions for the comment',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'value': {'type': 'string'},
                                    'identifier': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'renderedBody': {
                                'type': ['string', 'null'],
                                'description': 'Rendered comment body as HTML (available with expand=renderedBody)',
                            },
                            'properties': {
                                'type': ['array', 'null'],
                                'description': 'Comment properties (available with expand=properties)',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                        'x-airbyte-entity-name': 'issue_comments',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Jira issue comment object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique comment identifier'},
                    'self': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of the comment',
                    },
                    'body': {
                        'type': 'object',
                        'description': 'Comment content in ADF (Atlassian Document Format)',
                        'properties': {
                            'type': {'type': 'string', 'description': "Document type (always 'doc')"},
                            'version': {'type': 'integer', 'description': 'ADF version'},
                            'content': {
                                'type': 'array',
                                'description': 'Array of content blocks',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'type': {'type': 'string', 'description': "Block type (e.g., 'paragraph')"},
                                        'content': {
                                            'type': 'array',
                                            'description': 'Nested content items',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'type': {'type': 'string', 'description': "Content type (e.g., 'text')"},
                                                    'text': {'type': 'string', 'description': 'Text content'},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'additionalProperties': False,
                    },
                    'author': {
                        'type': 'object',
                        'description': 'Comment author user information',
                        'properties': {
                            'self': {'type': 'string', 'format': 'uri'},
                            'accountId': {'type': 'string'},
                            'emailAddress': {'type': 'string', 'format': 'email'},
                            'displayName': {'type': 'string'},
                            'active': {'type': 'boolean'},
                            'timeZone': {'type': 'string'},
                            'accountType': {'type': 'string'},
                            'avatarUrls': {
                                'type': 'object',
                                'description': 'URLs for user avatars in different sizes',
                                'properties': {
                                    '16x16': {'type': 'string', 'format': 'uri'},
                                    '24x24': {'type': 'string', 'format': 'uri'},
                                    '32x32': {'type': 'string', 'format': 'uri'},
                                    '48x48': {'type': 'string', 'format': 'uri'},
                                },
                            },
                        },
                    },
                    'updateAuthor': {
                        'type': 'object',
                        'description': 'User who last updated the comment',
                        'properties': {
                            'self': {'type': 'string', 'format': 'uri'},
                            'accountId': {'type': 'string'},
                            'emailAddress': {'type': 'string', 'format': 'email'},
                            'displayName': {'type': 'string'},
                            'active': {'type': 'boolean'},
                            'timeZone': {'type': 'string'},
                            'accountType': {'type': 'string'},
                            'avatarUrls': {
                                'type': 'object',
                                'description': 'URLs for user avatars in different sizes',
                                'properties': {
                                    '16x16': {'type': 'string', 'format': 'uri'},
                                    '24x24': {'type': 'string', 'format': 'uri'},
                                    '32x32': {'type': 'string', 'format': 'uri'},
                                    '48x48': {'type': 'string', 'format': 'uri'},
                                },
                            },
                        },
                    },
                    'created': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Comment creation timestamp',
                    },
                    'updated': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Comment last update timestamp',
                    },
                    'jsdPublic': {'type': 'boolean', 'description': 'Whether the comment is public in Jira Service Desk'},
                    'visibility': {
                        'type': ['object', 'null'],
                        'description': 'Visibility restrictions for the comment',
                        'properties': {
                            'type': {'type': 'string'},
                            'value': {'type': 'string'},
                            'identifier': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'renderedBody': {
                        'type': ['string', 'null'],
                        'description': 'Rendered comment body as HTML (available with expand=renderedBody)',
                    },
                    'properties': {
                        'type': ['array', 'null'],
                        'description': 'Comment properties (available with expand=properties)',
                        'items': {'type': 'object', 'additionalProperties': True},
                    },
                },
                'x-airbyte-entity-name': 'issue_comments',
            },
        ),
        EntityDefinition(
            name='issue_worklogs',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/issue/{issueIdOrKey}/worklog',
                    action=Action.LIST,
                    description='Retrieve all worklogs for a specific issue',
                    query_params=['startAt', 'maxResults', 'expand'],
                    query_params_schema={
                        'startAt': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 1048576,
                        },
                        'expand': {'type': 'string', 'required': False},
                    },
                    path_params=['issueIdOrKey'],
                    path_params_schema={
                        'issueIdOrKey': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of issue worklogs',
                        'properties': {
                            'startAt': {'type': 'integer', 'description': 'Index of first item returned'},
                            'maxResults': {'type': 'integer', 'description': 'Maximum number of results per page'},
                            'total': {'type': 'integer', 'description': 'Total number of worklogs'},
                            'worklogs': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Jira worklog object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique worklog identifier'},
                                        'self': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of the worklog',
                                        },
                                        'author': {
                                            'type': 'object',
                                            'description': 'Worklog author user information',
                                            'properties': {
                                                'self': {'type': 'string', 'format': 'uri'},
                                                'accountId': {'type': 'string'},
                                                'emailAddress': {'type': 'string', 'format': 'email'},
                                                'displayName': {'type': 'string'},
                                                'active': {'type': 'boolean'},
                                                'timeZone': {'type': 'string'},
                                                'accountType': {'type': 'string'},
                                                'avatarUrls': {
                                                    'type': 'object',
                                                    'description': 'URLs for user avatars in different sizes',
                                                    'properties': {
                                                        '16x16': {'type': 'string', 'format': 'uri'},
                                                        '24x24': {'type': 'string', 'format': 'uri'},
                                                        '32x32': {'type': 'string', 'format': 'uri'},
                                                        '48x48': {'type': 'string', 'format': 'uri'},
                                                    },
                                                },
                                            },
                                        },
                                        'updateAuthor': {
                                            'type': 'object',
                                            'description': 'User who last updated the worklog',
                                            'properties': {
                                                'self': {'type': 'string', 'format': 'uri'},
                                                'accountId': {'type': 'string'},
                                                'emailAddress': {'type': 'string', 'format': 'email'},
                                                'displayName': {'type': 'string'},
                                                'active': {'type': 'boolean'},
                                                'timeZone': {'type': 'string'},
                                                'accountType': {'type': 'string'},
                                                'avatarUrls': {
                                                    'type': 'object',
                                                    'description': 'URLs for user avatars in different sizes',
                                                    'properties': {
                                                        '16x16': {'type': 'string', 'format': 'uri'},
                                                        '24x24': {'type': 'string', 'format': 'uri'},
                                                        '32x32': {'type': 'string', 'format': 'uri'},
                                                        '48x48': {'type': 'string', 'format': 'uri'},
                                                    },
                                                },
                                            },
                                        },
                                        'comment': {
                                            'type': 'object',
                                            'description': 'Comment associated with the worklog (ADF format)',
                                            'properties': {
                                                'type': {'type': 'string', 'description': "Document type (always 'doc')"},
                                                'version': {'type': 'integer', 'description': 'ADF version'},
                                                'content': {
                                                    'type': 'array',
                                                    'description': 'Array of content blocks',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'description': "Block type (e.g., 'paragraph')"},
                                                            'content': {
                                                                'type': 'array',
                                                                'description': 'Nested content items',
                                                                'items': {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'type': {'type': 'string', 'description': "Content type (e.g., 'text')"},
                                                                        'text': {'type': 'string', 'description': 'Text content'},
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            'additionalProperties': False,
                                        },
                                        'created': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Worklog creation timestamp',
                                        },
                                        'updated': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Worklog last update timestamp',
                                        },
                                        'started': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the work was started',
                                        },
                                        'timeSpent': {'type': 'string', 'description': 'Human-readable time spent (e.g., "3h 20m")'},
                                        'timeSpentSeconds': {'type': 'integer', 'description': 'Time spent in seconds'},
                                        'issueId': {'type': 'string', 'description': 'ID of the issue this worklog belongs to'},
                                        'visibility': {
                                            'type': ['object', 'null'],
                                            'description': 'Visibility restrictions for the worklog',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'value': {'type': 'string'},
                                                'identifier': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'properties': {
                                            'type': ['array', 'null'],
                                            'description': 'Worklog properties (available with expand=properties)',
                                            'items': {'type': 'object', 'additionalProperties': True},
                                        },
                                    },
                                    'x-airbyte-entity-name': 'worklogs',
                                },
                                'description': 'Array of worklog objects',
                            },
                        },
                    },
                    record_extractor='$.worklogs',
                    meta_extractor={
                        'startAt': '$.startAt',
                        'maxResults': '$.maxResults',
                        'total': '$.total',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}',
                    action=Action.GET,
                    description='Retrieve a single worklog by its ID',
                    query_params=['expand'],
                    query_params_schema={
                        'expand': {'type': 'string', 'required': False},
                    },
                    path_params=['issueIdOrKey', 'worklogId'],
                    path_params_schema={
                        'issueIdOrKey': {'type': 'string', 'required': True},
                        'worklogId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Jira worklog object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique worklog identifier'},
                            'self': {
                                'type': 'string',
                                'format': 'uri',
                                'description': 'URL of the worklog',
                            },
                            'author': {
                                'type': 'object',
                                'description': 'Worklog author user information',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'emailAddress': {'type': 'string', 'format': 'email'},
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                    'timeZone': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                },
                            },
                            'updateAuthor': {
                                'type': 'object',
                                'description': 'User who last updated the worklog',
                                'properties': {
                                    'self': {'type': 'string', 'format': 'uri'},
                                    'accountId': {'type': 'string'},
                                    'emailAddress': {'type': 'string', 'format': 'email'},
                                    'displayName': {'type': 'string'},
                                    'active': {'type': 'boolean'},
                                    'timeZone': {'type': 'string'},
                                    'accountType': {'type': 'string'},
                                    'avatarUrls': {
                                        'type': 'object',
                                        'description': 'URLs for user avatars in different sizes',
                                        'properties': {
                                            '16x16': {'type': 'string', 'format': 'uri'},
                                            '24x24': {'type': 'string', 'format': 'uri'},
                                            '32x32': {'type': 'string', 'format': 'uri'},
                                            '48x48': {'type': 'string', 'format': 'uri'},
                                        },
                                    },
                                },
                            },
                            'comment': {
                                'type': 'object',
                                'description': 'Comment associated with the worklog (ADF format)',
                                'properties': {
                                    'type': {'type': 'string', 'description': "Document type (always 'doc')"},
                                    'version': {'type': 'integer', 'description': 'ADF version'},
                                    'content': {
                                        'type': 'array',
                                        'description': 'Array of content blocks',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string', 'description': "Block type (e.g., 'paragraph')"},
                                                'content': {
                                                    'type': 'array',
                                                    'description': 'Nested content items',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'type': {'type': 'string', 'description': "Content type (e.g., 'text')"},
                                                            'text': {'type': 'string', 'description': 'Text content'},
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'additionalProperties': False,
                            },
                            'created': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Worklog creation timestamp',
                            },
                            'updated': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Worklog last update timestamp',
                            },
                            'started': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the work was started',
                            },
                            'timeSpent': {'type': 'string', 'description': 'Human-readable time spent (e.g., "3h 20m")'},
                            'timeSpentSeconds': {'type': 'integer', 'description': 'Time spent in seconds'},
                            'issueId': {'type': 'string', 'description': 'ID of the issue this worklog belongs to'},
                            'visibility': {
                                'type': ['object', 'null'],
                                'description': 'Visibility restrictions for the worklog',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'value': {'type': 'string'},
                                    'identifier': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'properties': {
                                'type': ['array', 'null'],
                                'description': 'Worklog properties (available with expand=properties)',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                        'x-airbyte-entity-name': 'worklogs',
                    },
                ),
            },
        ),
    ],
)