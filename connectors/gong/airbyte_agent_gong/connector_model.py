"""
Connector model for gong.

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

GongConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('32382e40-3b49-4b99-9c5c-4076501914e7'),
    name='gong',
    version='0.1.14',
    base_url='https://api.gong.io',
    auth=AuthConfig(
        options=[
            AuthOption(
                scheme_name='oauth2',
                type=AuthType.OAUTH2,
                config={
                    'header': 'Authorization',
                    'prefix': 'Bearer',
                    'refresh_url': 'https://app.gong.io/oauth2/generate-customer-token',
                    'auth_style': 'basic',
                    'body_format': 'form',
                },
                user_config_spec=AirbyteAuthConfig(
                    title='OAuth 2.0 Authentication',
                    type='object',
                    required=['refresh_token', 'client_id', 'client_secret'],
                    properties={
                        'access_token': AuthConfigFieldSpec(
                            title='Access Token',
                            description='Your Gong OAuth2 Access Token.',
                        ),
                        'refresh_token': AuthConfigFieldSpec(
                            title='Refresh Token',
                            description='Your Gong OAuth2 Refresh Token. Note: Gong uses single-use refresh tokens.',
                        ),
                        'client_id': AuthConfigFieldSpec(
                            title='Client ID',
                            description='Your Gong OAuth App Client ID.',
                        ),
                        'client_secret': AuthConfigFieldSpec(
                            title='Client Secret',
                            description='Your Gong OAuth App Client Secret.',
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
                    replication_auth_key_constants={'credentials.auth_type': 'OAuth2.0'},
                ),
                untested=True,
            ),
            AuthOption(
                scheme_name='basicAuth',
                type=AuthType.BASIC,
                user_config_spec=AirbyteAuthConfig(
                    title='Access Key Authentication',
                    type='object',
                    required=['access_key', 'access_key_secret'],
                    properties={
                        'access_key': AuthConfigFieldSpec(
                            title='Access Key',
                            description='Your Gong API Access Key',
                        ),
                        'access_key_secret': AuthConfigFieldSpec(
                            title='Access Key Secret',
                            description='Your Gong API Access Key Secret',
                        ),
                    },
                    auth_mapping={'username': '${access_key}', 'password': '${access_key_secret}'},
                    replication_auth_key_mapping={'credentials.access_key': 'access_key', 'credentials.access_key_secret': 'access_key_secret'},
                    replication_auth_key_constants={'credentials.auth_type': 'APIKey'},
                ),
            ),
        ],
    ),
    entities=[
        EntityDefinition(
            name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/users',
                    action=Action.LIST,
                    description='Returns a list of all users in the Gong account',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of users',
                        'properties': {
                            'users': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'User object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique user identifier'},
                                        'emailAddress': {'type': 'string', 'description': 'User email address'},
                                        'created': {'type': 'string', 'description': 'User creation timestamp'},
                                        'active': {'type': 'boolean', 'description': 'Whether user is active'},
                                        'emailAliases': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Email aliases for the user',
                                        },
                                        'trustedEmailAddress': {
                                            'type': ['string', 'null'],
                                            'description': 'Trusted email address',
                                        },
                                        'firstName': {'type': 'string', 'description': 'User first name'},
                                        'lastName': {'type': 'string', 'description': 'User last name'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Job title',
                                        },
                                        'phoneNumber': {
                                            'type': ['string', 'null'],
                                            'description': 'Phone number',
                                        },
                                        'extension': {
                                            'type': ['string', 'null'],
                                            'description': 'Phone extension',
                                        },
                                        'personalMeetingUrls': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Personal meeting URLs',
                                        },
                                        'settings': {
                                            'type': 'object',
                                            'description': 'User settings',
                                            'properties': {
                                                'webConferencesRecorded': {'type': 'boolean'},
                                                'preventWebConferenceRecording': {'type': 'boolean'},
                                                'telephonyCallsImported': {'type': 'boolean'},
                                                'emailsImported': {'type': 'boolean'},
                                                'preventEmailImport': {'type': 'boolean'},
                                                'nonRecordedMeetingsImported': {'type': 'boolean'},
                                                'gongConnectEnabled': {'type': 'boolean'},
                                            },
                                        },
                                        'managerId': {
                                            'type': ['string', 'null'],
                                            'description': 'Manager user ID',
                                        },
                                        'meetingConsentPageUrl': {
                                            'type': ['string', 'null'],
                                            'description': 'Meeting consent page URL',
                                        },
                                        'spokenLanguages': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'language': {'type': 'string'},
                                                    'primary': {'type': 'boolean'},
                                                },
                                            },
                                            'description': 'Spoken languages',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'users',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.users',
                    meta_extractor={'pagination': '$.records'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/users/{id}',
                    action=Action.GET,
                    description='Get a single user by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing single user',
                        'properties': {
                            'user': {
                                'type': 'object',
                                'description': 'User object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                                    'emailAddress': {'type': 'string', 'description': 'User email address'},
                                    'created': {'type': 'string', 'description': 'User creation timestamp'},
                                    'active': {'type': 'boolean', 'description': 'Whether user is active'},
                                    'emailAliases': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'Email aliases for the user',
                                    },
                                    'trustedEmailAddress': {
                                        'type': ['string', 'null'],
                                        'description': 'Trusted email address',
                                    },
                                    'firstName': {'type': 'string', 'description': 'User first name'},
                                    'lastName': {'type': 'string', 'description': 'User last name'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'Job title',
                                    },
                                    'phoneNumber': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone number',
                                    },
                                    'extension': {
                                        'type': ['string', 'null'],
                                        'description': 'Phone extension',
                                    },
                                    'personalMeetingUrls': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'Personal meeting URLs',
                                    },
                                    'settings': {
                                        'type': 'object',
                                        'description': 'User settings',
                                        'properties': {
                                            'webConferencesRecorded': {'type': 'boolean'},
                                            'preventWebConferenceRecording': {'type': 'boolean'},
                                            'telephonyCallsImported': {'type': 'boolean'},
                                            'emailsImported': {'type': 'boolean'},
                                            'preventEmailImport': {'type': 'boolean'},
                                            'nonRecordedMeetingsImported': {'type': 'boolean'},
                                            'gongConnectEnabled': {'type': 'boolean'},
                                        },
                                    },
                                    'managerId': {
                                        'type': ['string', 'null'],
                                        'description': 'Manager user ID',
                                    },
                                    'meetingConsentPageUrl': {
                                        'type': ['string', 'null'],
                                        'description': 'Meeting consent page URL',
                                    },
                                    'spokenLanguages': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'language': {'type': 'string'},
                                                'primary': {'type': 'boolean'},
                                            },
                                        },
                                        'description': 'Spoken languages',
                                    },
                                },
                                'x-airbyte-entity-name': 'users',
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.user',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'User object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                    'emailAddress': {'type': 'string', 'description': 'User email address'},
                    'created': {'type': 'string', 'description': 'User creation timestamp'},
                    'active': {'type': 'boolean', 'description': 'Whether user is active'},
                    'emailAliases': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Email aliases for the user',
                    },
                    'trustedEmailAddress': {
                        'type': ['string', 'null'],
                        'description': 'Trusted email address',
                    },
                    'firstName': {'type': 'string', 'description': 'User first name'},
                    'lastName': {'type': 'string', 'description': 'User last name'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Job title',
                    },
                    'phoneNumber': {
                        'type': ['string', 'null'],
                        'description': 'Phone number',
                    },
                    'extension': {
                        'type': ['string', 'null'],
                        'description': 'Phone extension',
                    },
                    'personalMeetingUrls': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Personal meeting URLs',
                    },
                    'settings': {
                        'type': 'object',
                        'description': 'User settings',
                        'properties': {
                            'webConferencesRecorded': {'type': 'boolean'},
                            'preventWebConferenceRecording': {'type': 'boolean'},
                            'telephonyCallsImported': {'type': 'boolean'},
                            'emailsImported': {'type': 'boolean'},
                            'preventEmailImport': {'type': 'boolean'},
                            'nonRecordedMeetingsImported': {'type': 'boolean'},
                            'gongConnectEnabled': {'type': 'boolean'},
                        },
                    },
                    'managerId': {
                        'type': ['string', 'null'],
                        'description': 'Manager user ID',
                    },
                    'meetingConsentPageUrl': {
                        'type': ['string', 'null'],
                        'description': 'Meeting consent page URL',
                    },
                    'spokenLanguages': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'language': {'type': 'string'},
                                'primary': {'type': 'boolean'},
                            },
                        },
                        'description': 'Spoken languages',
                    },
                },
                'x-airbyte-entity-name': 'users',
            },
        ),
        EntityDefinition(
            name='calls',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/calls',
                    action=Action.LIST,
                    description='Retrieve calls data by date range',
                    query_params=['fromDateTime', 'toDateTime', 'cursor'],
                    query_params_schema={
                        'fromDateTime': {'type': 'string', 'required': False},
                        'toDateTime': {'type': 'string', 'required': False},
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of calls',
                        'properties': {
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Call object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique call identifier'},
                                        'url': {'type': 'string', 'description': 'URL to call in Gong'},
                                        'title': {'type': 'string', 'description': 'Call title'},
                                        'scheduled': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Scheduled time',
                                        },
                                        'started': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Call start time',
                                        },
                                        'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                                        'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                                        'direction': {'type': 'string', 'description': 'Call direction (inbound/outbound)'},
                                        'system': {'type': 'string', 'description': 'System type'},
                                        'scope': {'type': 'string', 'description': 'Call scope'},
                                        'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                                        'language': {'type': 'string', 'description': 'Call language'},
                                        'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                                        'sdrDisposition': {
                                            'type': ['string', 'null'],
                                            'description': 'SDR disposition',
                                        },
                                        'clientUniqueId': {
                                            'type': ['string', 'null'],
                                            'description': 'Client unique identifier',
                                        },
                                        'customData': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom data',
                                        },
                                        'purpose': {
                                            'type': ['string', 'null'],
                                            'description': 'Call purpose',
                                        },
                                        'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                                        'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                                        'calendarEventId': {
                                            'type': ['string', 'null'],
                                            'description': 'Calendar event ID',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'calls',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.calls',
                    meta_extractor={'pagination': '$.records'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v2/calls/{id}',
                    action=Action.GET,
                    description='Get specific call data by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing single call',
                        'properties': {
                            'call': {
                                'type': 'object',
                                'description': 'Call object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique call identifier'},
                                    'url': {'type': 'string', 'description': 'URL to call in Gong'},
                                    'title': {'type': 'string', 'description': 'Call title'},
                                    'scheduled': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Scheduled time',
                                    },
                                    'started': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Call start time',
                                    },
                                    'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                                    'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                                    'direction': {'type': 'string', 'description': 'Call direction (inbound/outbound)'},
                                    'system': {'type': 'string', 'description': 'System type'},
                                    'scope': {'type': 'string', 'description': 'Call scope'},
                                    'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                                    'language': {'type': 'string', 'description': 'Call language'},
                                    'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                                    'sdrDisposition': {
                                        'type': ['string', 'null'],
                                        'description': 'SDR disposition',
                                    },
                                    'clientUniqueId': {
                                        'type': ['string', 'null'],
                                        'description': 'Client unique identifier',
                                    },
                                    'customData': {
                                        'type': ['string', 'null'],
                                        'description': 'Custom data',
                                    },
                                    'purpose': {
                                        'type': ['string', 'null'],
                                        'description': 'Call purpose',
                                    },
                                    'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                                    'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                                    'calendarEventId': {
                                        'type': ['string', 'null'],
                                        'description': 'Calendar event ID',
                                    },
                                },
                                'x-airbyte-entity-name': 'calls',
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.call',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Call object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique call identifier'},
                    'url': {'type': 'string', 'description': 'URL to call in Gong'},
                    'title': {'type': 'string', 'description': 'Call title'},
                    'scheduled': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Scheduled time',
                    },
                    'started': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Call start time',
                    },
                    'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                    'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                    'direction': {'type': 'string', 'description': 'Call direction (inbound/outbound)'},
                    'system': {'type': 'string', 'description': 'System type'},
                    'scope': {'type': 'string', 'description': 'Call scope'},
                    'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                    'language': {'type': 'string', 'description': 'Call language'},
                    'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                    'sdrDisposition': {
                        'type': ['string', 'null'],
                        'description': 'SDR disposition',
                    },
                    'clientUniqueId': {
                        'type': ['string', 'null'],
                        'description': 'Client unique identifier',
                    },
                    'customData': {
                        'type': ['string', 'null'],
                        'description': 'Custom data',
                    },
                    'purpose': {
                        'type': ['string', 'null'],
                        'description': 'Call purpose',
                    },
                    'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                    'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                    'calendarEventId': {
                        'type': ['string', 'null'],
                        'description': 'Calendar event ID',
                    },
                },
                'x-airbyte-entity-name': 'calls',
            },
        ),
        EntityDefinition(
            name='calls_extensive',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/calls/extensive',
                    action=Action.LIST,
                    description='Retrieve detailed call data including participants, interaction stats, and content',
                    body_fields=['filter', 'contentSelector', 'cursor'],
                    request_schema={
                        'type': 'object',
                        'required': ['filter'],
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'fromDateTime': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Start date in ISO 8601 format',
                                    },
                                    'toDateTime': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'End date in ISO 8601 format',
                                    },
                                    'callIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of specific call IDs to retrieve',
                                    },
                                    'workspaceId': {'type': 'string', 'description': 'Filter by workspace ID'},
                                },
                            },
                            'contentSelector': {
                                'type': 'object',
                                'description': 'Select which content to include in the response',
                                'properties': {
                                    'context': {
                                        'type': 'string',
                                        'description': 'Context level for the data',
                                        'enum': ['Extended'],
                                    },
                                    'contextTiming': {
                                        'type': 'array',
                                        'description': 'Context timing options',
                                        'items': {
                                            'type': 'string',
                                            'enum': ['Now', 'TimeOfCall'],
                                        },
                                    },
                                    'exposedFields': {
                                        'type': 'object',
                                        'description': 'Specify which fields to include in the response',
                                        'properties': {
                                            'collaboration': {
                                                'type': 'object',
                                                'properties': {
                                                    'publicComments': {'type': 'boolean', 'description': 'Include public comments'},
                                                },
                                            },
                                            'content': {
                                                'type': 'object',
                                                'properties': {
                                                    'pointsOfInterest': {'type': 'boolean', 'description': 'Include points of interest (deprecated, use highlights)'},
                                                    'structure': {'type': 'boolean', 'description': 'Include call structure'},
                                                    'topics': {'type': 'boolean', 'description': 'Include topics discussed'},
                                                    'trackers': {'type': 'boolean', 'description': 'Include trackers'},
                                                    'trackerOccurrences': {'type': 'boolean', 'description': 'Include tracker occurrences'},
                                                    'brief': {'type': 'boolean', 'description': 'Include call brief'},
                                                    'outline': {'type': 'boolean', 'description': 'Include call outline'},
                                                    'highlights': {'type': 'boolean', 'description': 'Include call highlights'},
                                                    'callOutcome': {'type': 'boolean', 'description': 'Include call outcome'},
                                                    'keyPoints': {'type': 'boolean', 'description': 'Include key points'},
                                                },
                                            },
                                            'interaction': {
                                                'type': 'object',
                                                'properties': {
                                                    'personInteractionStats': {'type': 'boolean', 'description': 'Include person interaction statistics'},
                                                    'questions': {'type': 'boolean', 'description': 'Include questions asked'},
                                                    'speakers': {'type': 'boolean', 'description': 'Include speaker information'},
                                                    'video': {'type': 'boolean', 'description': 'Include video interaction data'},
                                                },
                                            },
                                            'media': {'type': 'boolean', 'description': 'Include media URLs (audio/video)'},
                                            'parties': {'type': 'boolean', 'description': 'Include participant information'},
                                        },
                                    },
                                },
                            },
                            'cursor': {'type': 'string', 'description': 'Cursor for pagination'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing detailed call data',
                        'properties': {
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Detailed call object with extended information',
                                    'properties': {
                                        'metaData': {
                                            'type': 'object',
                                            'description': 'Call metadata',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Unique call identifier'},
                                                'url': {'type': 'string', 'description': 'URL to call in Gong'},
                                                'title': {'type': 'string', 'description': 'Call title'},
                                                'scheduled': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Scheduled time',
                                                },
                                                'started': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Call start time',
                                                },
                                                'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                                                'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                                                'direction': {'type': 'string', 'description': 'Call direction'},
                                                'system': {'type': 'string', 'description': 'System type'},
                                                'scope': {'type': 'string', 'description': 'Call scope'},
                                                'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                                                'language': {'type': 'string', 'description': 'Call language'},
                                                'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                                                'sdrDisposition': {
                                                    'type': ['string', 'null'],
                                                    'description': 'SDR disposition',
                                                },
                                                'clientUniqueId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Client unique identifier',
                                                },
                                                'customData': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Custom data',
                                                },
                                                'purpose': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Call purpose',
                                                },
                                                'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                                                'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                                                'calendarEventId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Calendar event ID',
                                                },
                                            },
                                        },
                                        'parties': {
                                            'type': 'array',
                                            'description': 'Call participants',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Party ID'},
                                                    'emailAddress': {'type': 'string', 'description': 'Email address'},
                                                    'name': {'type': 'string', 'description': 'Full name'},
                                                    'title': {'type': 'string', 'description': 'Job title'},
                                                    'userId': {'type': 'string', 'description': 'Gong user ID if internal'},
                                                    'speakerId': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Speaker ID for transcript matching',
                                                    },
                                                    'affiliation': {'type': 'string', 'description': 'Internal or External'},
                                                    'methods': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                        'description': 'Contact methods',
                                                    },
                                                    'phoneNumber': {'type': 'string', 'description': 'Phone number'},
                                                    'context': {
                                                        'type': 'array',
                                                        'description': 'CRM context data linked to this participant',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'system': {'type': 'string', 'description': 'CRM system name (e.g., Salesforce, HubSpot)'},
                                                                'objects': {
                                                                    'type': 'array',
                                                                    'description': 'CRM objects linked to this participant',
                                                                    'items': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'objectType': {'type': 'string', 'description': 'CRM object type (Account, Contact, Opportunity, Lead)'},
                                                                            'objectId': {'type': 'string', 'description': 'CRM record ID'},
                                                                            'fields': {
                                                                                'type': 'array',
                                                                                'description': 'CRM field values',
                                                                                'items': {
                                                                                    'type': 'object',
                                                                                    'properties': {
                                                                                        'name': {'type': 'string', 'description': 'Field name'},
                                                                                        'value': {
                                                                                            'type': ['string', 'number', 'null'],
                                                                                            'description': 'Field value',
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
                                        'interaction': {
                                            'type': 'object',
                                            'description': 'Interaction statistics',
                                            'properties': {
                                                'interactionStats': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string', 'description': 'Stat name'},
                                                            'value': {'type': 'number', 'description': 'Stat value'},
                                                        },
                                                    },
                                                },
                                                'questions': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'companyCount': {'type': 'integer'},
                                                        'nonCompanyCount': {'type': 'integer'},
                                                    },
                                                },
                                            },
                                        },
                                        'collaboration': {
                                            'type': 'object',
                                            'description': 'Collaboration data',
                                            'properties': {
                                                'publicComments': {
                                                    'type': 'array',
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                        'content': {
                                            'type': 'object',
                                            'description': 'Content data including topics and trackers',
                                            'properties': {
                                                'topics': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'duration': {'type': 'number'},
                                                        },
                                                    },
                                                },
                                                'trackers': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'count': {'type': 'integer'},
                                                            'type': {'type': 'string'},
                                                            'occurrences': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'pointsOfInterest': {'type': 'object'},
                                            },
                                        },
                                        'media': {
                                            'type': 'object',
                                            'description': 'Media URLs',
                                            'properties': {
                                                'audioUrl': {'type': 'string'},
                                                'videoUrl': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'calls_extensive',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.calls',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Detailed call object with extended information',
                'properties': {
                    'metaData': {
                        'type': 'object',
                        'description': 'Call metadata',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique call identifier'},
                            'url': {'type': 'string', 'description': 'URL to call in Gong'},
                            'title': {'type': 'string', 'description': 'Call title'},
                            'scheduled': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Scheduled time',
                            },
                            'started': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Call start time',
                            },
                            'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                            'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                            'direction': {'type': 'string', 'description': 'Call direction'},
                            'system': {'type': 'string', 'description': 'System type'},
                            'scope': {'type': 'string', 'description': 'Call scope'},
                            'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                            'language': {'type': 'string', 'description': 'Call language'},
                            'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                            'sdrDisposition': {
                                'type': ['string', 'null'],
                                'description': 'SDR disposition',
                            },
                            'clientUniqueId': {
                                'type': ['string', 'null'],
                                'description': 'Client unique identifier',
                            },
                            'customData': {
                                'type': ['string', 'null'],
                                'description': 'Custom data',
                            },
                            'purpose': {
                                'type': ['string', 'null'],
                                'description': 'Call purpose',
                            },
                            'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                            'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                            'calendarEventId': {
                                'type': ['string', 'null'],
                                'description': 'Calendar event ID',
                            },
                        },
                    },
                    'parties': {
                        'type': 'array',
                        'description': 'Call participants',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Party ID'},
                                'emailAddress': {'type': 'string', 'description': 'Email address'},
                                'name': {'type': 'string', 'description': 'Full name'},
                                'title': {'type': 'string', 'description': 'Job title'},
                                'userId': {'type': 'string', 'description': 'Gong user ID if internal'},
                                'speakerId': {
                                    'type': ['string', 'null'],
                                    'description': 'Speaker ID for transcript matching',
                                },
                                'affiliation': {'type': 'string', 'description': 'Internal or External'},
                                'methods': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Contact methods',
                                },
                                'phoneNumber': {'type': 'string', 'description': 'Phone number'},
                                'context': {
                                    'type': 'array',
                                    'description': 'CRM context data linked to this participant',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'system': {'type': 'string', 'description': 'CRM system name (e.g., Salesforce, HubSpot)'},
                                            'objects': {
                                                'type': 'array',
                                                'description': 'CRM objects linked to this participant',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'objectType': {'type': 'string', 'description': 'CRM object type (Account, Contact, Opportunity, Lead)'},
                                                        'objectId': {'type': 'string', 'description': 'CRM record ID'},
                                                        'fields': {
                                                            'type': 'array',
                                                            'description': 'CRM field values',
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'name': {'type': 'string', 'description': 'Field name'},
                                                                    'value': {
                                                                        'type': ['string', 'number', 'null'],
                                                                        'description': 'Field value',
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
                    'interaction': {
                        'type': 'object',
                        'description': 'Interaction statistics',
                        'properties': {
                            'interactionStats': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'Stat name'},
                                        'value': {'type': 'number', 'description': 'Stat value'},
                                    },
                                },
                            },
                            'questions': {
                                'type': 'object',
                                'properties': {
                                    'companyCount': {'type': 'integer'},
                                    'nonCompanyCount': {'type': 'integer'},
                                },
                            },
                        },
                    },
                    'collaboration': {
                        'type': 'object',
                        'description': 'Collaboration data',
                        'properties': {
                            'publicComments': {
                                'type': 'array',
                                'items': {'type': 'object'},
                            },
                        },
                    },
                    'content': {
                        'type': 'object',
                        'description': 'Content data including topics and trackers',
                        'properties': {
                            'topics': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                        'duration': {'type': 'number'},
                                    },
                                },
                            },
                            'trackers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string'},
                                        'name': {'type': 'string'},
                                        'count': {'type': 'integer'},
                                        'type': {'type': 'string'},
                                        'occurrences': {
                                            'type': 'array',
                                            'items': {'type': 'object'},
                                        },
                                    },
                                },
                            },
                            'pointsOfInterest': {'type': 'object'},
                        },
                    },
                    'media': {
                        'type': 'object',
                        'description': 'Media URLs',
                        'properties': {
                            'audioUrl': {'type': 'string'},
                            'videoUrl': {'type': 'string'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'calls_extensive',
            },
        ),
        EntityDefinition(
            name='call_audio',
            actions=[Action.DOWNLOAD],
            endpoints={
                Action.DOWNLOAD: EndpointDefinition(
                    method='POST',
                    path='/v2/calls:audio/download',
                    path_override=PathOverrideConfig(
                        path='/v2/calls/extensive',
                    ),
                    action=Action.DOWNLOAD,
                    description='Downloads the audio media file for a call. Temporarily, the request body must be configured with:\n{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}\n',
                    body_fields=['filter', 'contentSelector'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'callIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List containing the single call ID',
                                    },
                                },
                            },
                            'contentSelector': {
                                'type': 'object',
                                'properties': {
                                    'exposedFields': {
                                        'type': 'object',
                                        'properties': {
                                            'media': {
                                                'type': 'boolean',
                                                'description': 'Must be true to get media URLs',
                                                'default': True,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing detailed call data',
                        'properties': {
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Detailed call object with extended information',
                                    'properties': {
                                        'metaData': {
                                            'type': 'object',
                                            'description': 'Call metadata',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Unique call identifier'},
                                                'url': {'type': 'string', 'description': 'URL to call in Gong'},
                                                'title': {'type': 'string', 'description': 'Call title'},
                                                'scheduled': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Scheduled time',
                                                },
                                                'started': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Call start time',
                                                },
                                                'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                                                'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                                                'direction': {'type': 'string', 'description': 'Call direction'},
                                                'system': {'type': 'string', 'description': 'System type'},
                                                'scope': {'type': 'string', 'description': 'Call scope'},
                                                'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                                                'language': {'type': 'string', 'description': 'Call language'},
                                                'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                                                'sdrDisposition': {
                                                    'type': ['string', 'null'],
                                                    'description': 'SDR disposition',
                                                },
                                                'clientUniqueId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Client unique identifier',
                                                },
                                                'customData': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Custom data',
                                                },
                                                'purpose': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Call purpose',
                                                },
                                                'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                                                'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                                                'calendarEventId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Calendar event ID',
                                                },
                                            },
                                        },
                                        'parties': {
                                            'type': 'array',
                                            'description': 'Call participants',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Party ID'},
                                                    'emailAddress': {'type': 'string', 'description': 'Email address'},
                                                    'name': {'type': 'string', 'description': 'Full name'},
                                                    'title': {'type': 'string', 'description': 'Job title'},
                                                    'userId': {'type': 'string', 'description': 'Gong user ID if internal'},
                                                    'speakerId': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Speaker ID for transcript matching',
                                                    },
                                                    'affiliation': {'type': 'string', 'description': 'Internal or External'},
                                                    'methods': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                        'description': 'Contact methods',
                                                    },
                                                    'phoneNumber': {'type': 'string', 'description': 'Phone number'},
                                                    'context': {
                                                        'type': 'array',
                                                        'description': 'CRM context data linked to this participant',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'system': {'type': 'string', 'description': 'CRM system name (e.g., Salesforce, HubSpot)'},
                                                                'objects': {
                                                                    'type': 'array',
                                                                    'description': 'CRM objects linked to this participant',
                                                                    'items': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'objectType': {'type': 'string', 'description': 'CRM object type (Account, Contact, Opportunity, Lead)'},
                                                                            'objectId': {'type': 'string', 'description': 'CRM record ID'},
                                                                            'fields': {
                                                                                'type': 'array',
                                                                                'description': 'CRM field values',
                                                                                'items': {
                                                                                    'type': 'object',
                                                                                    'properties': {
                                                                                        'name': {'type': 'string', 'description': 'Field name'},
                                                                                        'value': {
                                                                                            'type': ['string', 'number', 'null'],
                                                                                            'description': 'Field value',
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
                                        'interaction': {
                                            'type': 'object',
                                            'description': 'Interaction statistics',
                                            'properties': {
                                                'interactionStats': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string', 'description': 'Stat name'},
                                                            'value': {'type': 'number', 'description': 'Stat value'},
                                                        },
                                                    },
                                                },
                                                'questions': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'companyCount': {'type': 'integer'},
                                                        'nonCompanyCount': {'type': 'integer'},
                                                    },
                                                },
                                            },
                                        },
                                        'collaboration': {
                                            'type': 'object',
                                            'description': 'Collaboration data',
                                            'properties': {
                                                'publicComments': {
                                                    'type': 'array',
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                        'content': {
                                            'type': 'object',
                                            'description': 'Content data including topics and trackers',
                                            'properties': {
                                                'topics': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'duration': {'type': 'number'},
                                                        },
                                                    },
                                                },
                                                'trackers': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'count': {'type': 'integer'},
                                                            'type': {'type': 'string'},
                                                            'occurrences': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'pointsOfInterest': {'type': 'object'},
                                            },
                                        },
                                        'media': {
                                            'type': 'object',
                                            'description': 'Media URLs',
                                            'properties': {
                                                'audioUrl': {'type': 'string'},
                                                'videoUrl': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'calls_extensive',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    file_field='calls[0].media.audioUrl',
                ),
            },
        ),
        EntityDefinition(
            name='call_video',
            actions=[Action.DOWNLOAD],
            endpoints={
                Action.DOWNLOAD: EndpointDefinition(
                    method='POST',
                    path='/v2/calls:video/download',
                    path_override=PathOverrideConfig(
                        path='/v2/calls/extensive',
                    ),
                    action=Action.DOWNLOAD,
                    description='Downloads the video media file for a call. Temporarily, the request body must be configured with:\n{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}\n',
                    body_fields=['filter', 'contentSelector'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'callIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List containing the single call ID',
                                    },
                                },
                            },
                            'contentSelector': {
                                'type': 'object',
                                'properties': {
                                    'exposedFields': {
                                        'type': 'object',
                                        'properties': {
                                            'media': {
                                                'type': 'boolean',
                                                'description': 'Must be true to get media URLs',
                                                'default': True,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing detailed call data',
                        'properties': {
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Detailed call object with extended information',
                                    'properties': {
                                        'metaData': {
                                            'type': 'object',
                                            'description': 'Call metadata',
                                            'properties': {
                                                'id': {'type': 'string', 'description': 'Unique call identifier'},
                                                'url': {'type': 'string', 'description': 'URL to call in Gong'},
                                                'title': {'type': 'string', 'description': 'Call title'},
                                                'scheduled': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Scheduled time',
                                                },
                                                'started': {
                                                    'type': 'string',
                                                    'format': 'date-time',
                                                    'description': 'Call start time',
                                                },
                                                'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                                                'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                                                'direction': {'type': 'string', 'description': 'Call direction'},
                                                'system': {'type': 'string', 'description': 'System type'},
                                                'scope': {'type': 'string', 'description': 'Call scope'},
                                                'media': {'type': 'string', 'description': 'Media type (Audio/Video)'},
                                                'language': {'type': 'string', 'description': 'Call language'},
                                                'workspaceId': {'type': 'string', 'description': 'Workspace ID'},
                                                'sdrDisposition': {
                                                    'type': ['string', 'null'],
                                                    'description': 'SDR disposition',
                                                },
                                                'clientUniqueId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Client unique identifier',
                                                },
                                                'customData': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Custom data',
                                                },
                                                'purpose': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Call purpose',
                                                },
                                                'isPrivate': {'type': 'boolean', 'description': 'Whether call is private'},
                                                'meetingUrl': {'type': 'string', 'description': 'Meeting URL'},
                                                'calendarEventId': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Calendar event ID',
                                                },
                                            },
                                        },
                                        'parties': {
                                            'type': 'array',
                                            'description': 'Call participants',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Party ID'},
                                                    'emailAddress': {'type': 'string', 'description': 'Email address'},
                                                    'name': {'type': 'string', 'description': 'Full name'},
                                                    'title': {'type': 'string', 'description': 'Job title'},
                                                    'userId': {'type': 'string', 'description': 'Gong user ID if internal'},
                                                    'speakerId': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Speaker ID for transcript matching',
                                                    },
                                                    'affiliation': {'type': 'string', 'description': 'Internal or External'},
                                                    'methods': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                        'description': 'Contact methods',
                                                    },
                                                    'phoneNumber': {'type': 'string', 'description': 'Phone number'},
                                                    'context': {
                                                        'type': 'array',
                                                        'description': 'CRM context data linked to this participant',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'system': {'type': 'string', 'description': 'CRM system name (e.g., Salesforce, HubSpot)'},
                                                                'objects': {
                                                                    'type': 'array',
                                                                    'description': 'CRM objects linked to this participant',
                                                                    'items': {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'objectType': {'type': 'string', 'description': 'CRM object type (Account, Contact, Opportunity, Lead)'},
                                                                            'objectId': {'type': 'string', 'description': 'CRM record ID'},
                                                                            'fields': {
                                                                                'type': 'array',
                                                                                'description': 'CRM field values',
                                                                                'items': {
                                                                                    'type': 'object',
                                                                                    'properties': {
                                                                                        'name': {'type': 'string', 'description': 'Field name'},
                                                                                        'value': {
                                                                                            'type': ['string', 'number', 'null'],
                                                                                            'description': 'Field value',
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
                                        'interaction': {
                                            'type': 'object',
                                            'description': 'Interaction statistics',
                                            'properties': {
                                                'interactionStats': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string', 'description': 'Stat name'},
                                                            'value': {'type': 'number', 'description': 'Stat value'},
                                                        },
                                                    },
                                                },
                                                'questions': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'companyCount': {'type': 'integer'},
                                                        'nonCompanyCount': {'type': 'integer'},
                                                    },
                                                },
                                            },
                                        },
                                        'collaboration': {
                                            'type': 'object',
                                            'description': 'Collaboration data',
                                            'properties': {
                                                'publicComments': {
                                                    'type': 'array',
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                        'content': {
                                            'type': 'object',
                                            'description': 'Content data including topics and trackers',
                                            'properties': {
                                                'topics': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'name': {'type': 'string'},
                                                            'duration': {'type': 'number'},
                                                        },
                                                    },
                                                },
                                                'trackers': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'id': {'type': 'string'},
                                                            'name': {'type': 'string'},
                                                            'count': {'type': 'integer'},
                                                            'type': {'type': 'string'},
                                                            'occurrences': {
                                                                'type': 'array',
                                                                'items': {'type': 'object'},
                                                            },
                                                        },
                                                    },
                                                },
                                                'pointsOfInterest': {'type': 'object'},
                                            },
                                        },
                                        'media': {
                                            'type': 'object',
                                            'description': 'Media URLs',
                                            'properties': {
                                                'audioUrl': {'type': 'string'},
                                                'videoUrl': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'calls_extensive',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    file_field='calls[0].media.videoUrl',
                ),
            },
        ),
        EntityDefinition(
            name='workspaces',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/workspaces',
                    action=Action.LIST,
                    description='List all company workspaces',
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of workspaces',
                        'properties': {
                            'workspaces': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Workspace object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique workspace identifier'},
                                        'workspaceId': {'type': 'string', 'description': 'Unique workspace identifier (legacy)'},
                                        'name': {'type': 'string', 'description': 'Workspace name'},
                                        'description': {'type': 'string', 'description': 'Workspace description'},
                                    },
                                    'x-airbyte-entity-name': 'workspaces',
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.workspaces',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Workspace object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique workspace identifier'},
                    'workspaceId': {'type': 'string', 'description': 'Unique workspace identifier (legacy)'},
                    'name': {'type': 'string', 'description': 'Workspace name'},
                    'description': {'type': 'string', 'description': 'Workspace description'},
                },
                'x-airbyte-entity-name': 'workspaces',
            },
        ),
        EntityDefinition(
            name='call_transcripts',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/calls/transcript',
                    action=Action.LIST,
                    description='Returns transcripts for calls in a specified date range or specific call IDs',
                    body_fields=['filter', 'cursor'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'fromDateTime': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Start date in ISO 8601 format (optional if callIds provided)',
                                    },
                                    'toDateTime': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'End date in ISO 8601 format (optional if callIds provided)',
                                    },
                                    'callIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of specific call IDs to retrieve transcripts for',
                                    },
                                },
                            },
                            'cursor': {'type': 'string', 'description': 'Cursor for pagination'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing call transcripts',
                        'properties': {
                            'callTranscripts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Call transcript object',
                                    'properties': {
                                        'callId': {'type': 'string', 'description': 'Call identifier'},
                                        'transcript': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'speakerId': {'type': 'string', 'description': 'Speaker identifier'},
                                                    'topic': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Topic',
                                                    },
                                                    'sentences': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'start': {'type': 'integer', 'description': 'Start time in seconds'},
                                                                'end': {'type': 'integer', 'description': 'End time in seconds'},
                                                                'text': {'type': 'string', 'description': 'Sentence text'},
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'call_transcripts',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                        },
                    },
                    record_extractor='$.callTranscripts',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Call transcript object',
                'properties': {
                    'callId': {'type': 'string', 'description': 'Call identifier'},
                    'transcript': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'speakerId': {'type': 'string', 'description': 'Speaker identifier'},
                                'topic': {
                                    'type': ['string', 'null'],
                                    'description': 'Topic',
                                },
                                'sentences': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'start': {'type': 'integer', 'description': 'Start time in seconds'},
                                            'end': {'type': 'integer', 'description': 'End time in seconds'},
                                            'text': {'type': 'string', 'description': 'Sentence text'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'call_transcripts',
            },
        ),
        EntityDefinition(
            name='stats_activity_aggregate',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/stats/activity/aggregate',
                    action=Action.LIST,
                    description='Provides aggregated user activity metrics across a specified period',
                    body_fields=['filter'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'fromDate': {
                                        'type': 'string',
                                        'format': 'date',
                                        'description': 'Start date (YYYY-MM-DD)',
                                    },
                                    'toDate': {
                                        'type': 'string',
                                        'format': 'date',
                                        'description': 'End date (YYYY-MM-DD)',
                                    },
                                    'userIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of user IDs to retrieve stats for',
                                    },
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing aggregated activity statistics',
                        'properties': {
                            'requestId': {'type': 'string'},
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'usersAggregateActivityStats': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'User with aggregated activity statistics',
                                    'properties': {
                                        'userId': {'type': 'string'},
                                        'userEmailAddress': {'type': 'string'},
                                        'userAggregateActivityStats': {
                                            'type': 'object',
                                            'description': 'Aggregated activity statistics for a user',
                                            'properties': {
                                                'callsAsHost': {'type': 'integer'},
                                                'callsGaveFeedback': {'type': 'integer'},
                                                'callsRequestedFeedback': {'type': 'integer'},
                                                'callsReceivedFeedback': {'type': 'integer'},
                                                'ownCallsListenedTo': {'type': 'integer'},
                                                'othersCallsListenedTo': {'type': 'integer'},
                                                'callsSharedInternally': {'type': 'integer'},
                                                'callsSharedExternally': {'type': 'integer'},
                                                'callsScorecardsFilled': {'type': 'integer'},
                                                'callsScorecardsReceived': {'type': 'integer'},
                                                'callsAttended': {'type': 'integer'},
                                                'callsCommentsGiven': {'type': 'integer'},
                                                'callsCommentsReceived': {'type': 'integer'},
                                                'callsMarkedAsFeedbackGiven': {'type': 'integer'},
                                                'callsMarkedAsFeedbackReceived': {'type': 'integer'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'stats_activity_aggregate',
                                },
                            },
                            'fromDateTime': {'type': 'string'},
                            'toDateTime': {'type': 'string'},
                            'timeZone': {'type': 'string'},
                        },
                    },
                    record_extractor='$.usersAggregateActivityStats',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'User with aggregated activity statistics',
                'properties': {
                    'userId': {'type': 'string'},
                    'userEmailAddress': {'type': 'string'},
                    'userAggregateActivityStats': {'$ref': '#/components/schemas/UserAggregateActivityStats'},
                },
                'x-airbyte-entity-name': 'stats_activity_aggregate',
            },
        ),
        EntityDefinition(
            name='stats_activity_day_by_day',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/stats/activity/day-by-day',
                    action=Action.LIST,
                    description='Delivers daily user activity metrics across a specified date range',
                    body_fields=['filter'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'fromDate': {
                                        'type': 'string',
                                        'format': 'date',
                                        'description': 'Start date (YYYY-MM-DD)',
                                    },
                                    'toDate': {
                                        'type': 'string',
                                        'format': 'date',
                                        'description': 'End date (YYYY-MM-DD)',
                                    },
                                    'userIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of user IDs to retrieve stats for',
                                    },
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing daily activity statistics',
                        'properties': {
                            'requestId': {'type': 'string'},
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'usersDetailedActivities': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'User with detailed daily activity statistics',
                                    'properties': {
                                        'userId': {'type': 'string'},
                                        'userEmailAddress': {'type': 'string'},
                                        'userDailyActivityStats': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'description': 'Daily activity statistics with call IDs',
                                                'properties': {
                                                    'callsAsHost': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsGaveFeedback': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsRequestedFeedback': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsReceivedFeedback': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'ownCallsListenedTo': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'othersCallsListenedTo': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsSharedInternally': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsSharedExternally': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsAttended': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsCommentsGiven': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsCommentsReceived': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsMarkedAsFeedbackGiven': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsMarkedAsFeedbackReceived': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsScorecardsFilled': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'callsScorecardsReceived': {
                                                        'type': 'array',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'fromDate': {'type': 'string'},
                                                    'toDate': {'type': 'string'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'stats_activity_day_by_day',
                                },
                            },
                        },
                    },
                    record_extractor='$.usersDetailedActivities',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'User with detailed daily activity statistics',
                'properties': {
                    'userId': {'type': 'string'},
                    'userEmailAddress': {'type': 'string'},
                    'userDailyActivityStats': {
                        'type': 'array',
                        'items': {'$ref': '#/components/schemas/DailyActivityStats'},
                    },
                },
                'x-airbyte-entity-name': 'stats_activity_day_by_day',
            },
        ),
        EntityDefinition(
            name='stats_interaction',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/stats/interaction',
                    action=Action.LIST,
                    description='Returns interaction stats for users based on calls that have Whisper turned on',
                    body_fields=['filter'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'fromDate': {
                                        'type': 'string',
                                        'format': 'date',
                                        'description': 'Start date (YYYY-MM-DD)',
                                    },
                                    'toDate': {
                                        'type': 'string',
                                        'format': 'date',
                                        'description': 'End date (YYYY-MM-DD)',
                                    },
                                    'userIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of user IDs to retrieve stats for',
                                    },
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing interaction statistics',
                        'properties': {
                            'requestId': {'type': 'string'},
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                            'peopleInteractionStats': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'User with interaction statistics',
                                    'properties': {
                                        'userId': {'type': 'string'},
                                        'userEmailAddress': {'type': 'string'},
                                        'personInteractionStats': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'description': 'Individual interaction statistic',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'value': {'type': 'number'},
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'stats_interaction',
                                },
                            },
                            'fromDateTime': {'type': 'string'},
                            'toDateTime': {'type': 'string'},
                            'timeZone': {'type': 'string'},
                        },
                    },
                    record_extractor='$.peopleInteractionStats',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'User with interaction statistics',
                'properties': {
                    'userId': {'type': 'string'},
                    'userEmailAddress': {'type': 'string'},
                    'personInteractionStats': {
                        'type': 'array',
                        'items': {'$ref': '#/components/schemas/PersonInteractionStat'},
                    },
                },
                'x-airbyte-entity-name': 'stats_interaction',
            },
        ),
        EntityDefinition(
            name='settings_scorecards',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/settings/scorecards',
                    action=Action.LIST,
                    description='Retrieve all scorecard configurations in the company',
                    query_params=['workspaceId'],
                    query_params_schema={
                        'workspaceId': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of scorecards',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                            'scorecards': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Scorecard configuration',
                                    'properties': {
                                        'scorecardId': {'type': 'string', 'description': 'Unique scorecard identifier'},
                                        'scorecardName': {'type': 'string', 'description': 'Name of the scorecard'},
                                        'workspaceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID (null if company-wide)',
                                        },
                                        'enabled': {'type': 'boolean', 'description': 'Whether the scorecard is enabled'},
                                        'updaterUserId': {'type': 'string', 'description': 'User ID of last updater'},
                                        'created': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'updated': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'reviewMethod': {'type': 'string', 'description': 'Review method (e.g., MANUAL, AUTOMATIC)'},
                                        'questions': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A question within a scorecard',
                                                'properties': {
                                                    'questionId': {'type': 'string', 'description': 'Unique question identifier'},
                                                    'questionRevisionId': {'type': 'string', 'description': 'Question revision identifier'},
                                                    'questionText': {'type': 'string', 'description': 'The question text'},
                                                    'questionType': {'type': 'string', 'description': 'Type of question (e.g., rating, yes/no)'},
                                                    'isRequired': {'type': 'boolean', 'description': 'Whether the question is required'},
                                                    'isOverall': {'type': 'boolean', 'description': 'Whether this is an overall rating question'},
                                                    'updaterUserId': {'type': 'string', 'description': 'User ID of last updater'},
                                                    'answerGuide': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Guide text for answering the question',
                                                    },
                                                    'minRange': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Minimum range value for range-type questions',
                                                    },
                                                    'maxRange': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Maximum range value for range-type questions',
                                                    },
                                                    'created': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Creation timestamp',
                                                    },
                                                    'updated': {
                                                        'type': 'string',
                                                        'format': 'date-time',
                                                        'description': 'Last update timestamp',
                                                    },
                                                    'answerOptions': {
                                                        'type': 'array',
                                                        'description': 'Available answer options',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'optionId': {'type': 'string'},
                                                                'optionText': {'type': 'string'},
                                                                'score': {'type': 'number'},
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'settings_scorecards',
                                },
                            },
                        },
                    },
                    record_extractor='$.scorecards',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Scorecard configuration',
                'properties': {
                    'scorecardId': {'type': 'string', 'description': 'Unique scorecard identifier'},
                    'scorecardName': {'type': 'string', 'description': 'Name of the scorecard'},
                    'workspaceId': {
                        'type': ['string', 'null'],
                        'description': 'Workspace ID (null if company-wide)',
                    },
                    'enabled': {'type': 'boolean', 'description': 'Whether the scorecard is enabled'},
                    'updaterUserId': {'type': 'string', 'description': 'User ID of last updater'},
                    'created': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'updated': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'reviewMethod': {'type': 'string', 'description': 'Review method (e.g., MANUAL, AUTOMATIC)'},
                    'questions': {
                        'type': 'array',
                        'items': {'$ref': '#/components/schemas/ScorecardQuestion'},
                    },
                },
                'x-airbyte-entity-name': 'settings_scorecards',
            },
        ),
        EntityDefinition(
            name='settings_trackers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/settings/trackers',
                    action=Action.LIST,
                    description='Retrieve all keyword tracker configurations in the company',
                    query_params=['workspaceId'],
                    query_params_schema={
                        'workspaceId': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing list of trackers',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                            'keywordTrackers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Keyword tracker configuration',
                                    'properties': {
                                        'trackerId': {'type': 'string', 'description': 'Unique tracker identifier'},
                                        'trackerName': {'type': 'string', 'description': 'Name of the tracker'},
                                        'workspaceId': {
                                            'type': ['string', 'null'],
                                            'description': 'Workspace ID (null if company-wide)',
                                        },
                                        'languageKeywords': {
                                            'type': 'array',
                                            'description': 'Keywords by language',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'language': {'type': 'string', 'description': 'Language code'},
                                                    'keywords': {
                                                        'type': 'array',
                                                        'description': 'List of keywords for this language',
                                                        'items': {'type': 'string'},
                                                    },
                                                    'includeRelatedForms': {'type': 'boolean', 'description': 'Whether to include related word forms'},
                                                },
                                            },
                                        },
                                        'affiliation': {'type': 'string', 'description': 'Who the tracker applies to (internal, external, both)'},
                                        'partOfQuestion': {'type': 'boolean', 'description': 'Whether this is part of a question'},
                                        'saidAt': {'type': 'string', 'description': 'When the keyword should be said (Anytime, etc.)'},
                                        'saidAtInterval': {
                                            'type': ['string', 'null'],
                                            'description': 'Interval for when keyword should be said',
                                        },
                                        'saidAtUnit': {
                                            'type': ['string', 'null'],
                                            'description': 'Unit for said at interval',
                                        },
                                        'saidInTopics': {
                                            'type': 'array',
                                            'description': 'Topics where the keyword should be mentioned',
                                            'items': {'type': 'string'},
                                        },
                                        'filterQuery': {'type': 'string', 'description': 'Filter query JSON string'},
                                        'created': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Creation timestamp',
                                        },
                                        'creatorUserId': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID of creator',
                                        },
                                        'updated': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                        'updaterUserId': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID of last updater',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'settings_trackers',
                                },
                            },
                        },
                    },
                    record_extractor='$.keywordTrackers',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Keyword tracker configuration',
                'properties': {
                    'trackerId': {'type': 'string', 'description': 'Unique tracker identifier'},
                    'trackerName': {'type': 'string', 'description': 'Name of the tracker'},
                    'workspaceId': {
                        'type': ['string', 'null'],
                        'description': 'Workspace ID (null if company-wide)',
                    },
                    'languageKeywords': {
                        'type': 'array',
                        'description': 'Keywords by language',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'language': {'type': 'string', 'description': 'Language code'},
                                'keywords': {
                                    'type': 'array',
                                    'description': 'List of keywords for this language',
                                    'items': {'type': 'string'},
                                },
                                'includeRelatedForms': {'type': 'boolean', 'description': 'Whether to include related word forms'},
                            },
                        },
                    },
                    'affiliation': {'type': 'string', 'description': 'Who the tracker applies to (internal, external, both)'},
                    'partOfQuestion': {'type': 'boolean', 'description': 'Whether this is part of a question'},
                    'saidAt': {'type': 'string', 'description': 'When the keyword should be said (Anytime, etc.)'},
                    'saidAtInterval': {
                        'type': ['string', 'null'],
                        'description': 'Interval for when keyword should be said',
                    },
                    'saidAtUnit': {
                        'type': ['string', 'null'],
                        'description': 'Unit for said at interval',
                    },
                    'saidInTopics': {
                        'type': 'array',
                        'description': 'Topics where the keyword should be mentioned',
                        'items': {'type': 'string'},
                    },
                    'filterQuery': {'type': 'string', 'description': 'Filter query JSON string'},
                    'created': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Creation timestamp',
                    },
                    'creatorUserId': {
                        'type': ['string', 'null'],
                        'description': 'User ID of creator',
                    },
                    'updated': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                    'updaterUserId': {
                        'type': ['string', 'null'],
                        'description': 'User ID of last updater',
                    },
                },
                'x-airbyte-entity-name': 'settings_trackers',
            },
        ),
        EntityDefinition(
            name='library_folders',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/library/folders',
                    action=Action.LIST,
                    description='Retrieve the folder structure of the call library',
                    query_params=['workspaceId'],
                    query_params_schema={
                        'workspaceId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing library folder structure',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                            'folders': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Library folder structure',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique folder identifier'},
                                        'name': {'type': 'string', 'description': 'Folder name'},
                                        'parentFolderId': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent folder ID (null for root folders)',
                                        },
                                        'createdBy': {
                                            'type': ['string', 'null'],
                                            'description': 'User ID of folder creator',
                                        },
                                        'updated': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Last update timestamp',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'library_folders',
                                },
                            },
                        },
                    },
                    record_extractor='$.folders',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Library folder structure',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique folder identifier'},
                    'name': {'type': 'string', 'description': 'Folder name'},
                    'parentFolderId': {
                        'type': ['string', 'null'],
                        'description': 'Parent folder ID (null for root folders)',
                    },
                    'createdBy': {
                        'type': ['string', 'null'],
                        'description': 'User ID of folder creator',
                    },
                    'updated': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Last update timestamp',
                    },
                },
                'x-airbyte-entity-name': 'library_folders',
            },
        ),
        EntityDefinition(
            name='library_folder_content',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/library/folder-content',
                    action=Action.LIST,
                    description='Retrieve calls in a specific library folder',
                    query_params=['folderId', 'cursor'],
                    query_params_schema={
                        'folderId': {'type': 'string', 'required': True},
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing calls in a folder',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                            'id': {'type': 'string', 'description': 'Folder ID'},
                            'name': {'type': 'string', 'description': 'Folder name'},
                            'createdBy': {
                                'type': ['string', 'null'],
                                'description': 'User ID of folder creator',
                            },
                            'updated': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Last update timestamp',
                            },
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Call within a library folder',
                                    'properties': {
                                        'callId': {'type': 'string', 'description': 'Unique call identifier'},
                                        'title': {'type': 'string', 'description': 'Call title'},
                                        'started': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Call start time',
                                        },
                                        'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                                        'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                                        'url': {'type': 'string', 'description': 'URL to call in Gong'},
                                    },
                                    'x-airbyte-entity-name': 'library_folder_content',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                        },
                    },
                    record_extractor='$.calls',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Call within a library folder',
                'properties': {
                    'callId': {'type': 'string', 'description': 'Unique call identifier'},
                    'title': {'type': 'string', 'description': 'Call title'},
                    'started': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Call start time',
                    },
                    'duration': {'type': 'integer', 'description': 'Call duration in seconds'},
                    'primaryUserId': {'type': 'string', 'description': 'Primary user ID'},
                    'url': {'type': 'string', 'description': 'URL to call in Gong'},
                },
                'x-airbyte-entity-name': 'library_folder_content',
            },
        ),
        EntityDefinition(
            name='coaching',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v2/coaching',
                    action=Action.LIST,
                    description='Retrieve coaching metrics for a manager and their direct reports',
                    query_params=[
                        'workspace-id',
                        'manager-id',
                        'from',
                        'to',
                    ],
                    query_params_schema={
                        'workspace-id': {'type': 'string', 'required': True},
                        'manager-id': {'type': 'string', 'required': True},
                        'from': {'type': 'string', 'required': True},
                        'to': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing coaching metrics',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                            'coachingData': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Coaching data for a user',
                                    'properties': {
                                        'userId': {'type': 'string', 'description': 'User identifier'},
                                        'userEmailAddress': {'type': 'string', 'description': 'User email address'},
                                        'userName': {'type': 'string', 'description': 'User name'},
                                        'isManager': {'type': 'boolean', 'description': 'Whether the user is a manager'},
                                        'coachingMetrics': {
                                            'type': 'object',
                                            'description': 'Coaching metrics for a user',
                                            'properties': {
                                                'callsListened': {'type': 'integer', 'description': 'Number of team calls listened to'},
                                                'callsAttended': {'type': 'integer', 'description': 'Number of team calls participated in'},
                                                'callsWithFeedback': {'type': 'integer', 'description': 'Number of calls with feedback given'},
                                                'callsWithComments': {'type': 'integer', 'description': 'Number of calls with comments'},
                                                'scorecardsFilled': {'type': 'integer', 'description': 'Number of scorecards filled'},
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'coaching',
                                },
                            },
                            'fromDateTime': {'type': 'string'},
                            'toDateTime': {'type': 'string'},
                        },
                    },
                    record_extractor='$.coachingData',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Coaching data for a user',
                'properties': {
                    'userId': {'type': 'string', 'description': 'User identifier'},
                    'userEmailAddress': {'type': 'string', 'description': 'User email address'},
                    'userName': {'type': 'string', 'description': 'User name'},
                    'isManager': {'type': 'boolean', 'description': 'Whether the user is a manager'},
                    'coachingMetrics': {'$ref': '#/components/schemas/CoachingMetrics'},
                },
                'x-airbyte-entity-name': 'coaching',
            },
        ),
        EntityDefinition(
            name='stats_activity_scorecards',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/v2/stats/activity/scorecards',
                    action=Action.LIST,
                    description='Retrieve answered scorecards for applicable reviewed users or scorecards for a date range',
                    body_fields=['filter', 'cursor'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filter': {
                                'type': 'object',
                                'properties': {
                                    'fromDateTime': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'Start date in ISO 8601 format',
                                    },
                                    'toDateTime': {
                                        'type': 'string',
                                        'format': 'date-time',
                                        'description': 'End date in ISO 8601 format',
                                    },
                                    'scorecardIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of scorecard IDs to filter by',
                                    },
                                    'reviewedUserIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of reviewed user IDs to filter by',
                                    },
                                    'reviewerUserIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of reviewer user IDs to filter by',
                                    },
                                    'callIds': {
                                        'type': 'array',
                                        'items': {'type': 'string'},
                                        'description': 'List of call IDs to filter by',
                                    },
                                },
                            },
                            'cursor': {'type': 'string', 'description': 'Cursor for pagination'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response containing answered scorecards',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Request identifier'},
                            'answeredScorecards': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A completed scorecard',
                                    'properties': {
                                        'answeredScorecardId': {'type': 'string', 'description': 'Unique answered scorecard identifier'},
                                        'scorecardId': {'type': 'string', 'description': 'Scorecard identifier'},
                                        'scorecardName': {'type': 'string', 'description': 'Scorecard name'},
                                        'callId': {'type': 'string', 'description': 'Call identifier'},
                                        'callStartTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the call started',
                                        },
                                        'reviewedUserId': {'type': 'string', 'description': 'User being reviewed'},
                                        'reviewerUserId': {'type': 'string', 'description': 'User who completed the review'},
                                        'reviewMethod': {'type': 'string', 'description': 'Review method (MANUAL, AUTOMATIC)'},
                                        'editorUserId': {
                                            'type': ['string', 'null'],
                                            'description': 'User who edited the scorecard',
                                        },
                                        'answeredDateTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the scorecard was completed',
                                        },
                                        'reviewTime': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the review was completed',
                                        },
                                        'visibilityType': {'type': 'string', 'description': 'Visibility type (PUBLIC, PRIVATE)'},
                                        'answers': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'description': 'An answer to a scorecard question',
                                                'properties': {
                                                    'questionId': {'type': 'string', 'description': 'Question identifier'},
                                                    'questionRevisionId': {'type': 'string', 'description': 'Question revision identifier'},
                                                    'isOverall': {'type': 'boolean', 'description': 'Whether this is an overall rating question'},
                                                    'answer': {'type': 'string', 'description': 'The answer value'},
                                                    'answerText': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Answer text (for text answers)',
                                                    },
                                                    'score': {'type': 'number', 'description': 'Score for the answer'},
                                                    'notApplicable': {'type': 'boolean', 'description': 'Whether marked as N/A'},
                                                    'selectedOptions': {
                                                        'type': ['array', 'null'],
                                                        'description': 'Selected option IDs for multi-choice questions',
                                                        'items': {'type': 'string'},
                                                    },
                                                },
                                            },
                                        },
                                        'overallScore': {'type': 'number', 'description': 'Overall scorecard score'},
                                        'visibility': {'type': 'string', 'description': 'Visibility setting (public, private)'},
                                    },
                                    'x-airbyte-entity-name': 'stats_activity_scorecards',
                                },
                            },
                            'records': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'totalRecords': {'type': 'integer', 'description': 'Total number of records'},
                                    'currentPageSize': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'currentPageNumber': {'type': 'integer', 'description': 'Current page number'},
                                    'cursor': {'type': 'string', 'description': 'Cursor for next page'},
                                },
                            },
                        },
                    },
                    record_extractor='$.answeredScorecards',
                    meta_extractor={'pagination': '$.records'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A completed scorecard',
                'properties': {
                    'answeredScorecardId': {'type': 'string', 'description': 'Unique answered scorecard identifier'},
                    'scorecardId': {'type': 'string', 'description': 'Scorecard identifier'},
                    'scorecardName': {'type': 'string', 'description': 'Scorecard name'},
                    'callId': {'type': 'string', 'description': 'Call identifier'},
                    'callStartTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the call started',
                    },
                    'reviewedUserId': {'type': 'string', 'description': 'User being reviewed'},
                    'reviewerUserId': {'type': 'string', 'description': 'User who completed the review'},
                    'reviewMethod': {'type': 'string', 'description': 'Review method (MANUAL, AUTOMATIC)'},
                    'editorUserId': {
                        'type': ['string', 'null'],
                        'description': 'User who edited the scorecard',
                    },
                    'answeredDateTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the scorecard was completed',
                    },
                    'reviewTime': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the review was completed',
                    },
                    'visibilityType': {'type': 'string', 'description': 'Visibility type (PUBLIC, PRIVATE)'},
                    'answers': {
                        'type': 'array',
                        'items': {'$ref': '#/components/schemas/AnsweredScorecardAnswer'},
                    },
                    'overallScore': {'type': 'number', 'description': 'Overall scorecard score'},
                    'visibility': {'type': 'string', 'description': 'Visibility setting (public, private)'},
                },
                'x-airbyte-entity-name': 'stats_activity_scorecards',
            },
        ),
    ],
    search_field_paths={
        'users': [
            'active',
            'created',
            'emailAddress',
            'emailAliases',
            'emailAliases[]',
            'extension',
            'firstName',
            'id',
            'lastName',
            'managerId',
            'meetingConsentPageUrl',
            'personalMeetingUrls',
            'personalMeetingUrls[]',
            'phoneNumber',
            'settings',
            'spokenLanguages',
            'spokenLanguages[]',
            'title',
            'trustedEmailAddress',
        ],
        'calls': [
            'calendarEventId',
            'clientUniqueId',
            'customData',
            'direction',
            'duration',
            'id',
            'isPrivate',
            'language',
            'media',
            'meetingUrl',
            'primaryUserId',
            'purpose',
            'scheduled',
            'scope',
            'sdrDisposition',
            'started',
            'system',
            'title',
            'url',
            'workspaceId',
        ],
        'calls_extensive': [
            'id',
            'startdatetime',
            'collaboration',
            'collaboration.brief',
            'content',
            'content.brief',
            'content.highlights',
            'content.highlights[]',
            'content.keyPoints',
            'content.keyPoints[]',
            'content.outline',
            'content.outline[]',
            'content.pointsOfInterest',
            'content.pointsOfInterest.actionItems',
            'content.pointsOfInterest.actionItems[]',
            'content.topics',
            'content.topics[]',
            'content.trackers',
            'content.trackers[]',
            'context',
            'context.objects',
            'context.objects[]',
            'context.system',
            'interaction',
            'interaction.interactionStats',
            'interaction.interactionStats[]',
            'interaction.questions',
            'interaction.questions.companyCount',
            'interaction.questions.nonCompanyCount',
            'interaction.speakers',
            'interaction.speakers[]',
            'interaction.video',
            'interaction.video[]',
            'media',
            'media.audioUrl',
            'media.videoUrl',
            'metaData',
            'metaData.calendarEventId',
            'metaData.clientUniqueId',
            'metaData.customData',
            'metaData.direction',
            'metaData.duration',
            'metaData.id',
            'metaData.isPrivate',
            'metaData.language',
            'metaData.media',
            'metaData.meetingUrl',
            'metaData.primaryUserId',
            'metaData.purpose',
            'metaData.scheduled',
            'metaData.scope',
            'metaData.sdrDisposition',
            'metaData.started',
            'metaData.system',
            'metaData.title',
            'metaData.url',
            'metaData.workspaceId',
            'parties',
            'parties[]',
        ],
        'settings_scorecards': [
            'created',
            'enabled',
            'questions',
            'questions[]',
            'scorecardId',
            'scorecardName',
            'updated',
            'updaterUserId',
            'workspaceId',
        ],
        'stats_activity_scorecards': [
            'answeredScorecardId',
            'answers',
            'answers[]',
            'callId',
            'callStartTime',
            'reviewTime',
            'reviewedUserId',
            'reviewerUserId',
            'scorecardId',
            'scorecardName',
            'visibilityType',
        ],
    },
)