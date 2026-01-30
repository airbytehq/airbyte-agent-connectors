"""
Connector model for google-drive.

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

GoogleDriveConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('9f8dda77-1048-4368-815b-269bf54ee9b8'),
    name='google-drive',
    version='0.1.3',
    base_url='https://www.googleapis.com',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://oauth2.googleapis.com/token',
        },
        user_config_spec=AirbyteAuthConfig(
            title='OAuth 2.0 Authentication',
            type='object',
            required=['refresh_token', 'client_id', 'client_secret'],
            properties={
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Your Google OAuth2 Access Token (optional, will be obtained via refresh)',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='Your Google OAuth2 Refresh Token',
                ),
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='Your Google OAuth2 Client ID',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='Your Google OAuth2 Client Secret',
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
    entities=[
        EntityDefinition(
            name='files',
            actions=[Action.LIST, Action.GET, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files',
                    action=Action.LIST,
                    description="Lists the user's files. Returns a paginated list of files.",
                    query_params=[
                        'pageSize',
                        'pageToken',
                        'q',
                        'orderBy',
                        'fields',
                        'spaces',
                        'corpora',
                        'driveId',
                        'includeItemsFromAllDrives',
                        'supportsAllDrives',
                    ],
                    query_params_schema={
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'q': {'type': 'string', 'required': False},
                        'orderBy': {'type': 'string', 'required': False},
                        'fields': {'type': 'string', 'required': False},
                        'spaces': {'type': 'string', 'required': False},
                        'corpora': {'type': 'string', 'required': False},
                        'driveId': {'type': 'string', 'required': False},
                        'includeItemsFromAllDrives': {'type': 'boolean', 'required': False},
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of files',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of files',
                            },
                            'incompleteSearch': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the search process was incomplete',
                            },
                            'files': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'The metadata for a file',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of the file'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the file',
                                        },
                                        'mimeType': {
                                            'type': ['string', 'null'],
                                            'description': 'The MIME type of the file',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'A short description of the file',
                                        },
                                        'starred': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user has starred the file',
                                        },
                                        'trashed': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file has been trashed',
                                        },
                                        'explicitlyTrashed': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file has been explicitly trashed',
                                        },
                                        'parents': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'The IDs of the parent folders',
                                        },
                                        'properties': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {'type': 'string'},
                                            'description': 'A collection of arbitrary key-value pairs',
                                        },
                                        'appProperties': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {'type': 'string'},
                                            'description': 'A collection of arbitrary key-value pairs private to the app',
                                        },
                                        'spaces': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'The list of spaces which contain the file',
                                        },
                                        'version': {
                                            'type': ['string', 'null'],
                                            'description': 'A monotonically increasing version number for the file',
                                        },
                                        'webContentLink': {
                                            'type': ['string', 'null'],
                                            'description': 'A link for downloading the content of the file',
                                        },
                                        'webViewLink': {
                                            'type': ['string', 'null'],
                                            'description': 'A link for opening the file in a relevant Google editor or viewer',
                                        },
                                        'iconLink': {
                                            'type': ['string', 'null'],
                                            'description': "A static, unauthenticated link to the file's icon",
                                        },
                                        'hasThumbnail': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this file has a thumbnail',
                                        },
                                        'thumbnailLink': {
                                            'type': ['string', 'null'],
                                            'description': "A short-lived link to the file's thumbnail",
                                        },
                                        'thumbnailVersion': {
                                            'type': ['string', 'null'],
                                            'description': 'The thumbnail version for use in thumbnail cache invalidation',
                                        },
                                        'viewedByMe': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file has been viewed by this user',
                                        },
                                        'viewedByMeTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the file was viewed by the user',
                                        },
                                        'createdTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which the file was created',
                                        },
                                        'modifiedTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the file was modified by anyone',
                                        },
                                        'modifiedByMeTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the file was modified by the user',
                                        },
                                        'modifiedByMe': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file has been modified by this user',
                                        },
                                        'sharedWithMeTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which the file was shared with the user',
                                        },
                                        'sharingUser': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The user who shared the file with the requesting user',
                                        },
                                        'owners': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'Information about a Drive user',
                                                'properties': {
                                                    'kind': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Identifies what kind of resource this is',
                                                    },
                                                    'displayName': {
                                                        'type': ['string', 'null'],
                                                        'description': 'A plain text displayable name for this user',
                                                    },
                                                    'photoLink': {
                                                        'type': ['string', 'null'],
                                                        'description': "A link to the user's profile photo",
                                                    },
                                                    'me': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether this user is the requesting user',
                                                    },
                                                    'permissionId': {
                                                        'type': ['string', 'null'],
                                                        'description': "The user's ID as visible in Permission resources",
                                                    },
                                                    'emailAddress': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email address of the user',
                                                    },
                                                },
                                            },
                                            'description': 'The owner of this file',
                                        },
                                        'driveId': {
                                            'type': ['string', 'null'],
                                            'description': 'ID of the shared drive the file resides in',
                                        },
                                        'lastModifyingUser': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The last user to modify the file',
                                        },
                                        'shared': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file has been shared',
                                        },
                                        'ownedByMe': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user owns the file',
                                        },
                                        'capabilities': {
                                            'type': ['object', 'null'],
                                            'description': 'Capabilities the current user has on this file',
                                            'properties': {
                                                'canEdit': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canComment': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canShare': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canCopy': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canDownload': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canDelete': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canRename': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canTrash': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canReadRevisions': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canAddChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canListChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canRemoveChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'viewersCanCopyContent': {
                                            'type': ['boolean', 'null'],
                                            'description': "Whether users with only reader or commenter permission can copy the file's content",
                                        },
                                        'copyRequiresWriterPermission': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the options to copy, print, or download this file should be disabled',
                                        },
                                        'writersCanShare': {
                                            'type': ['boolean', 'null'],
                                            'description': "Whether users with only writer permission can modify the file's permissions",
                                        },
                                        'permissionIds': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'List of permission IDs for users with access to this file',
                                        },
                                        'folderColorRgb': {
                                            'type': ['string', 'null'],
                                            'description': 'The color for a folder as an RGB hex string',
                                        },
                                        'originalFilename': {
                                            'type': ['string', 'null'],
                                            'description': 'The original filename of the uploaded content',
                                        },
                                        'fullFileExtension': {
                                            'type': ['string', 'null'],
                                            'description': 'The full file extension extracted from the name field',
                                        },
                                        'fileExtension': {
                                            'type': ['string', 'null'],
                                            'description': 'The final component of fullFileExtension',
                                        },
                                        'md5Checksum': {
                                            'type': ['string', 'null'],
                                            'description': 'The MD5 checksum for the content of the file',
                                        },
                                        'sha1Checksum': {
                                            'type': ['string', 'null'],
                                            'description': 'The SHA1 checksum for the content of the file',
                                        },
                                        'sha256Checksum': {
                                            'type': ['string', 'null'],
                                            'description': 'The SHA256 checksum for the content of the file',
                                        },
                                        'size': {
                                            'type': ['string', 'null'],
                                            'description': 'Size in bytes of blobs and first party editor files',
                                        },
                                        'quotaBytesUsed': {
                                            'type': ['string', 'null'],
                                            'description': 'The number of storage quota bytes used by the file',
                                        },
                                        'headRevisionId': {
                                            'type': ['string', 'null'],
                                            'description': "The ID of the file's head revision",
                                        },
                                        'isAppAuthorized': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file was created or opened by the requesting app',
                                        },
                                        'exportLinks': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {'type': 'string'},
                                            'description': 'Links for exporting Docs Editors files to specific formats',
                                        },
                                        'shortcutDetails': {
                                            'type': ['object', 'null'],
                                            'description': 'Shortcut file details',
                                            'properties': {
                                                'targetId': {
                                                    'type': ['string', 'null'],
                                                },
                                                'targetMimeType': {
                                                    'type': ['string', 'null'],
                                                },
                                                'targetResourceKey': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'contentRestrictions': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'readOnly': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'reason': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'restrictingUser': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'description': 'Information about a Drive user',
                                                                'properties': {
                                                                    'kind': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Identifies what kind of resource this is',
                                                                    },
                                                                    'displayName': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'A plain text displayable name for this user',
                                                                    },
                                                                    'photoLink': {
                                                                        'type': ['string', 'null'],
                                                                        'description': "A link to the user's profile photo",
                                                                    },
                                                                    'me': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this user is the requesting user',
                                                                    },
                                                                    'permissionId': {
                                                                        'type': ['string', 'null'],
                                                                        'description': "The user's ID as visible in Permission resources",
                                                                    },
                                                                    'emailAddress': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The email address of the user',
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'restrictionTime': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            'description': 'Restrictions for accessing the content of the file',
                                        },
                                        'resourceKey': {
                                            'type': ['string', 'null'],
                                            'description': 'A key needed to access the item via a shared link',
                                        },
                                        'linkShareMetadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Contains details about the link URLs',
                                            'properties': {
                                                'securityUpdateEligible': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'securityUpdateEnabled': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'labelInfo': {
                                            'type': ['object', 'null'],
                                            'description': 'An overview of the labels on the file',
                                            'properties': {
                                                'labels': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'object'},
                                                },
                                            },
                                        },
                                        'trashedTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time that the item was trashed',
                                        },
                                        'trashingUser': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The user who trashed the file',
                                        },
                                        'imageMediaMetadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional metadata about image media',
                                            'properties': {
                                                'width': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'height': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'rotation': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'time': {
                                                    'type': ['string', 'null'],
                                                },
                                                'cameraMake': {
                                                    'type': ['string', 'null'],
                                                },
                                                'cameraModel': {
                                                    'type': ['string', 'null'],
                                                },
                                                'exposureTime': {
                                                    'type': ['number', 'null'],
                                                },
                                                'aperture': {
                                                    'type': ['number', 'null'],
                                                },
                                                'flashUsed': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'focalLength': {
                                                    'type': ['number', 'null'],
                                                },
                                                'isoSpeed': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'meteringMode': {
                                                    'type': ['string', 'null'],
                                                },
                                                'sensor': {
                                                    'type': ['string', 'null'],
                                                },
                                                'exposureMode': {
                                                    'type': ['string', 'null'],
                                                },
                                                'colorSpace': {
                                                    'type': ['string', 'null'],
                                                },
                                                'whiteBalance': {
                                                    'type': ['string', 'null'],
                                                },
                                                'exposureBias': {
                                                    'type': ['number', 'null'],
                                                },
                                                'maxApertureValue': {
                                                    'type': ['number', 'null'],
                                                },
                                                'subjectDistance': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'lens': {
                                                    'type': ['string', 'null'],
                                                },
                                                'location': {
                                                    'type': ['object', 'null'],
                                                    'properties': {
                                                        'latitude': {
                                                            'type': ['number', 'null'],
                                                        },
                                                        'longitude': {
                                                            'type': ['number', 'null'],
                                                        },
                                                        'altitude': {
                                                            'type': ['number', 'null'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'videoMediaMetadata': {
                                            'type': ['object', 'null'],
                                            'description': 'Additional metadata about video media',
                                            'properties': {
                                                'width': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'height': {
                                                    'type': ['integer', 'null'],
                                                },
                                                'durationMillis': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'files',
                                },
                                'description': 'The list of files',
                            },
                        },
                    },
                    record_extractor='$.files',
                    meta_extractor={'nextPageToken': '$.nextPageToken', 'incompleteSearch': '$.incompleteSearch'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}',
                    action=Action.GET,
                    description="Gets a file's metadata by ID",
                    query_params=['fields', 'supportsAllDrives'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                    },
                    path_params=['fileId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'The metadata for a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'id': {'type': 'string', 'description': 'The ID of the file'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the file',
                            },
                            'mimeType': {
                                'type': ['string', 'null'],
                                'description': 'The MIME type of the file',
                            },
                            'description': {
                                'type': ['string', 'null'],
                                'description': 'A short description of the file',
                            },
                            'starred': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user has starred the file',
                            },
                            'trashed': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the file has been trashed',
                            },
                            'explicitlyTrashed': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the file has been explicitly trashed',
                            },
                            'parents': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'The IDs of the parent folders',
                            },
                            'properties': {
                                'type': ['object', 'null'],
                                'additionalProperties': {'type': 'string'},
                                'description': 'A collection of arbitrary key-value pairs',
                            },
                            'appProperties': {
                                'type': ['object', 'null'],
                                'additionalProperties': {'type': 'string'},
                                'description': 'A collection of arbitrary key-value pairs private to the app',
                            },
                            'spaces': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'The list of spaces which contain the file',
                            },
                            'version': {
                                'type': ['string', 'null'],
                                'description': 'A monotonically increasing version number for the file',
                            },
                            'webContentLink': {
                                'type': ['string', 'null'],
                                'description': 'A link for downloading the content of the file',
                            },
                            'webViewLink': {
                                'type': ['string', 'null'],
                                'description': 'A link for opening the file in a relevant Google editor or viewer',
                            },
                            'iconLink': {
                                'type': ['string', 'null'],
                                'description': "A static, unauthenticated link to the file's icon",
                            },
                            'hasThumbnail': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this file has a thumbnail',
                            },
                            'thumbnailLink': {
                                'type': ['string', 'null'],
                                'description': "A short-lived link to the file's thumbnail",
                            },
                            'thumbnailVersion': {
                                'type': ['string', 'null'],
                                'description': 'The thumbnail version for use in thumbnail cache invalidation',
                            },
                            'viewedByMe': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the file has been viewed by this user',
                            },
                            'viewedByMeTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The last time the file was viewed by the user',
                            },
                            'createdTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time at which the file was created',
                            },
                            'modifiedTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The last time the file was modified by anyone',
                            },
                            'modifiedByMeTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The last time the file was modified by the user',
                            },
                            'modifiedByMe': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the file has been modified by this user',
                            },
                            'sharedWithMeTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time at which the file was shared with the user',
                            },
                            'sharingUser': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The user who shared the file with the requesting user',
                            },
                            'owners': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'description': 'Information about a Drive user',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'displayName': {
                                            'type': ['string', 'null'],
                                            'description': 'A plain text displayable name for this user',
                                        },
                                        'photoLink': {
                                            'type': ['string', 'null'],
                                            'description': "A link to the user's profile photo",
                                        },
                                        'me': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this user is the requesting user',
                                        },
                                        'permissionId': {
                                            'type': ['string', 'null'],
                                            'description': "The user's ID as visible in Permission resources",
                                        },
                                        'emailAddress': {
                                            'type': ['string', 'null'],
                                            'description': 'The email address of the user',
                                        },
                                    },
                                },
                                'description': 'The owner of this file',
                            },
                            'driveId': {
                                'type': ['string', 'null'],
                                'description': 'ID of the shared drive the file resides in',
                            },
                            'lastModifyingUser': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The last user to modify the file',
                            },
                            'shared': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the file has been shared',
                            },
                            'ownedByMe': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user owns the file',
                            },
                            'capabilities': {
                                'type': ['object', 'null'],
                                'description': 'Capabilities the current user has on this file',
                                'properties': {
                                    'canEdit': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canComment': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canShare': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canCopy': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canDownload': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canDelete': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canRename': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canTrash': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canReadRevisions': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canAddChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canListChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canRemoveChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'viewersCanCopyContent': {
                                'type': ['boolean', 'null'],
                                'description': "Whether users with only reader or commenter permission can copy the file's content",
                            },
                            'copyRequiresWriterPermission': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the options to copy, print, or download this file should be disabled',
                            },
                            'writersCanShare': {
                                'type': ['boolean', 'null'],
                                'description': "Whether users with only writer permission can modify the file's permissions",
                            },
                            'permissionIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of permission IDs for users with access to this file',
                            },
                            'folderColorRgb': {
                                'type': ['string', 'null'],
                                'description': 'The color for a folder as an RGB hex string',
                            },
                            'originalFilename': {
                                'type': ['string', 'null'],
                                'description': 'The original filename of the uploaded content',
                            },
                            'fullFileExtension': {
                                'type': ['string', 'null'],
                                'description': 'The full file extension extracted from the name field',
                            },
                            'fileExtension': {
                                'type': ['string', 'null'],
                                'description': 'The final component of fullFileExtension',
                            },
                            'md5Checksum': {
                                'type': ['string', 'null'],
                                'description': 'The MD5 checksum for the content of the file',
                            },
                            'sha1Checksum': {
                                'type': ['string', 'null'],
                                'description': 'The SHA1 checksum for the content of the file',
                            },
                            'sha256Checksum': {
                                'type': ['string', 'null'],
                                'description': 'The SHA256 checksum for the content of the file',
                            },
                            'size': {
                                'type': ['string', 'null'],
                                'description': 'Size in bytes of blobs and first party editor files',
                            },
                            'quotaBytesUsed': {
                                'type': ['string', 'null'],
                                'description': 'The number of storage quota bytes used by the file',
                            },
                            'headRevisionId': {
                                'type': ['string', 'null'],
                                'description': "The ID of the file's head revision",
                            },
                            'isAppAuthorized': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the file was created or opened by the requesting app',
                            },
                            'exportLinks': {
                                'type': ['object', 'null'],
                                'additionalProperties': {'type': 'string'},
                                'description': 'Links for exporting Docs Editors files to specific formats',
                            },
                            'shortcutDetails': {
                                'type': ['object', 'null'],
                                'description': 'Shortcut file details',
                                'properties': {
                                    'targetId': {
                                        'type': ['string', 'null'],
                                    },
                                    'targetMimeType': {
                                        'type': ['string', 'null'],
                                    },
                                    'targetResourceKey': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'contentRestrictions': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'readOnly': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'reason': {
                                            'type': ['string', 'null'],
                                        },
                                        'restrictingUser': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'restrictionTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'Restrictions for accessing the content of the file',
                            },
                            'resourceKey': {
                                'type': ['string', 'null'],
                                'description': 'A key needed to access the item via a shared link',
                            },
                            'linkShareMetadata': {
                                'type': ['object', 'null'],
                                'description': 'Contains details about the link URLs',
                                'properties': {
                                    'securityUpdateEligible': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'securityUpdateEnabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'labelInfo': {
                                'type': ['object', 'null'],
                                'description': 'An overview of the labels on the file',
                                'properties': {
                                    'labels': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'object'},
                                    },
                                },
                            },
                            'trashedTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time that the item was trashed',
                            },
                            'trashingUser': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The user who trashed the file',
                            },
                            'imageMediaMetadata': {
                                'type': ['object', 'null'],
                                'description': 'Additional metadata about image media',
                                'properties': {
                                    'width': {
                                        'type': ['integer', 'null'],
                                    },
                                    'height': {
                                        'type': ['integer', 'null'],
                                    },
                                    'rotation': {
                                        'type': ['integer', 'null'],
                                    },
                                    'time': {
                                        'type': ['string', 'null'],
                                    },
                                    'cameraMake': {
                                        'type': ['string', 'null'],
                                    },
                                    'cameraModel': {
                                        'type': ['string', 'null'],
                                    },
                                    'exposureTime': {
                                        'type': ['number', 'null'],
                                    },
                                    'aperture': {
                                        'type': ['number', 'null'],
                                    },
                                    'flashUsed': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'focalLength': {
                                        'type': ['number', 'null'],
                                    },
                                    'isoSpeed': {
                                        'type': ['integer', 'null'],
                                    },
                                    'meteringMode': {
                                        'type': ['string', 'null'],
                                    },
                                    'sensor': {
                                        'type': ['string', 'null'],
                                    },
                                    'exposureMode': {
                                        'type': ['string', 'null'],
                                    },
                                    'colorSpace': {
                                        'type': ['string', 'null'],
                                    },
                                    'whiteBalance': {
                                        'type': ['string', 'null'],
                                    },
                                    'exposureBias': {
                                        'type': ['number', 'null'],
                                    },
                                    'maxApertureValue': {
                                        'type': ['number', 'null'],
                                    },
                                    'subjectDistance': {
                                        'type': ['integer', 'null'],
                                    },
                                    'lens': {
                                        'type': ['string', 'null'],
                                    },
                                    'location': {
                                        'type': ['object', 'null'],
                                        'properties': {
                                            'latitude': {
                                                'type': ['number', 'null'],
                                            },
                                            'longitude': {
                                                'type': ['number', 'null'],
                                            },
                                            'altitude': {
                                                'type': ['number', 'null'],
                                            },
                                        },
                                    },
                                },
                            },
                            'videoMediaMetadata': {
                                'type': ['object', 'null'],
                                'description': 'Additional metadata about video media',
                                'properties': {
                                    'width': {
                                        'type': ['integer', 'null'],
                                    },
                                    'height': {
                                        'type': ['integer', 'null'],
                                    },
                                    'durationMillis': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'files',
                    },
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/download',
                    path_override=PathOverrideConfig(
                        path='/drive/v3/files/{fileId}',
                    ),
                    action=Action.DOWNLOAD,
                    description='Downloads the binary content of a file. This works for non-Google Workspace files\n(PDFs, images, zip files, etc.). For Google Docs, Sheets, Slides, or Drawings,\nuse the export action instead.\n',
                    query_params=['alt', 'acknowledgeAbuse', 'supportsAllDrives'],
                    query_params_schema={
                        'alt': {
                            'type': 'string',
                            'required': True,
                            'default': 'media',
                        },
                        'acknowledgeAbuse': {'type': 'boolean', 'required': False},
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                    },
                    path_params=['fileId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'The metadata for a file',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'id': {'type': 'string', 'description': 'The ID of the file'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the file',
                    },
                    'mimeType': {
                        'type': ['string', 'null'],
                        'description': 'The MIME type of the file',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'A short description of the file',
                    },
                    'starred': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user has starred the file',
                    },
                    'trashed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file has been trashed',
                    },
                    'explicitlyTrashed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file has been explicitly trashed',
                    },
                    'parents': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The IDs of the parent folders',
                    },
                    'properties': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'string'},
                        'description': 'A collection of arbitrary key-value pairs',
                    },
                    'appProperties': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'string'},
                        'description': 'A collection of arbitrary key-value pairs private to the app',
                    },
                    'spaces': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The list of spaces which contain the file',
                    },
                    'version': {
                        'type': ['string', 'null'],
                        'description': 'A monotonically increasing version number for the file',
                    },
                    'webContentLink': {
                        'type': ['string', 'null'],
                        'description': 'A link for downloading the content of the file',
                    },
                    'webViewLink': {
                        'type': ['string', 'null'],
                        'description': 'A link for opening the file in a relevant Google editor or viewer',
                    },
                    'iconLink': {
                        'type': ['string', 'null'],
                        'description': "A static, unauthenticated link to the file's icon",
                    },
                    'hasThumbnail': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this file has a thumbnail',
                    },
                    'thumbnailLink': {
                        'type': ['string', 'null'],
                        'description': "A short-lived link to the file's thumbnail",
                    },
                    'thumbnailVersion': {
                        'type': ['string', 'null'],
                        'description': 'The thumbnail version for use in thumbnail cache invalidation',
                    },
                    'viewedByMe': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file has been viewed by this user',
                    },
                    'viewedByMeTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The last time the file was viewed by the user',
                    },
                    'createdTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time at which the file was created',
                    },
                    'modifiedTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The last time the file was modified by anyone',
                    },
                    'modifiedByMeTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The last time the file was modified by the user',
                    },
                    'modifiedByMe': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file has been modified by this user',
                    },
                    'sharedWithMeTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time at which the file was shared with the user',
                    },
                    'sharingUser': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The user who shared the file with the requesting user',
                    },
                    'owners': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/User'},
                        'description': 'The owner of this file',
                    },
                    'driveId': {
                        'type': ['string', 'null'],
                        'description': 'ID of the shared drive the file resides in',
                    },
                    'lastModifyingUser': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The last user to modify the file',
                    },
                    'shared': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file has been shared',
                    },
                    'ownedByMe': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user owns the file',
                    },
                    'capabilities': {
                        'type': ['object', 'null'],
                        'description': 'Capabilities the current user has on this file',
                        'properties': {
                            'canEdit': {
                                'type': ['boolean', 'null'],
                            },
                            'canComment': {
                                'type': ['boolean', 'null'],
                            },
                            'canShare': {
                                'type': ['boolean', 'null'],
                            },
                            'canCopy': {
                                'type': ['boolean', 'null'],
                            },
                            'canDownload': {
                                'type': ['boolean', 'null'],
                            },
                            'canDelete': {
                                'type': ['boolean', 'null'],
                            },
                            'canRename': {
                                'type': ['boolean', 'null'],
                            },
                            'canTrash': {
                                'type': ['boolean', 'null'],
                            },
                            'canReadRevisions': {
                                'type': ['boolean', 'null'],
                            },
                            'canAddChildren': {
                                'type': ['boolean', 'null'],
                            },
                            'canListChildren': {
                                'type': ['boolean', 'null'],
                            },
                            'canRemoveChildren': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'viewersCanCopyContent': {
                        'type': ['boolean', 'null'],
                        'description': "Whether users with only reader or commenter permission can copy the file's content",
                    },
                    'copyRequiresWriterPermission': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the options to copy, print, or download this file should be disabled',
                    },
                    'writersCanShare': {
                        'type': ['boolean', 'null'],
                        'description': "Whether users with only writer permission can modify the file's permissions",
                    },
                    'permissionIds': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'List of permission IDs for users with access to this file',
                    },
                    'folderColorRgb': {
                        'type': ['string', 'null'],
                        'description': 'The color for a folder as an RGB hex string',
                    },
                    'originalFilename': {
                        'type': ['string', 'null'],
                        'description': 'The original filename of the uploaded content',
                    },
                    'fullFileExtension': {
                        'type': ['string', 'null'],
                        'description': 'The full file extension extracted from the name field',
                    },
                    'fileExtension': {
                        'type': ['string', 'null'],
                        'description': 'The final component of fullFileExtension',
                    },
                    'md5Checksum': {
                        'type': ['string', 'null'],
                        'description': 'The MD5 checksum for the content of the file',
                    },
                    'sha1Checksum': {
                        'type': ['string', 'null'],
                        'description': 'The SHA1 checksum for the content of the file',
                    },
                    'sha256Checksum': {
                        'type': ['string', 'null'],
                        'description': 'The SHA256 checksum for the content of the file',
                    },
                    'size': {
                        'type': ['string', 'null'],
                        'description': 'Size in bytes of blobs and first party editor files',
                    },
                    'quotaBytesUsed': {
                        'type': ['string', 'null'],
                        'description': 'The number of storage quota bytes used by the file',
                    },
                    'headRevisionId': {
                        'type': ['string', 'null'],
                        'description': "The ID of the file's head revision",
                    },
                    'isAppAuthorized': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file was created or opened by the requesting app',
                    },
                    'exportLinks': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'string'},
                        'description': 'Links for exporting Docs Editors files to specific formats',
                    },
                    'shortcutDetails': {
                        'type': ['object', 'null'],
                        'description': 'Shortcut file details',
                        'properties': {
                            'targetId': {
                                'type': ['string', 'null'],
                            },
                            'targetMimeType': {
                                'type': ['string', 'null'],
                            },
                            'targetResourceKey': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'contentRestrictions': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': 'object',
                            'properties': {
                                'readOnly': {
                                    'type': ['boolean', 'null'],
                                },
                                'reason': {
                                    'type': ['string', 'null'],
                                },
                                'restrictingUser': {
                                    'oneOf': [
                                        {'$ref': '#/components/schemas/User'},
                                        {'type': 'null'},
                                    ],
                                },
                                'restrictionTime': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                },
                                'type': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                        'description': 'Restrictions for accessing the content of the file',
                    },
                    'resourceKey': {
                        'type': ['string', 'null'],
                        'description': 'A key needed to access the item via a shared link',
                    },
                    'linkShareMetadata': {
                        'type': ['object', 'null'],
                        'description': 'Contains details about the link URLs',
                        'properties': {
                            'securityUpdateEligible': {
                                'type': ['boolean', 'null'],
                            },
                            'securityUpdateEnabled': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'labelInfo': {
                        'type': ['object', 'null'],
                        'description': 'An overview of the labels on the file',
                        'properties': {
                            'labels': {
                                'type': ['array', 'null'],
                                'items': {'type': 'object'},
                            },
                        },
                    },
                    'trashedTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time that the item was trashed',
                    },
                    'trashingUser': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The user who trashed the file',
                    },
                    'imageMediaMetadata': {
                        'type': ['object', 'null'],
                        'description': 'Additional metadata about image media',
                        'properties': {
                            'width': {
                                'type': ['integer', 'null'],
                            },
                            'height': {
                                'type': ['integer', 'null'],
                            },
                            'rotation': {
                                'type': ['integer', 'null'],
                            },
                            'time': {
                                'type': ['string', 'null'],
                            },
                            'cameraMake': {
                                'type': ['string', 'null'],
                            },
                            'cameraModel': {
                                'type': ['string', 'null'],
                            },
                            'exposureTime': {
                                'type': ['number', 'null'],
                            },
                            'aperture': {
                                'type': ['number', 'null'],
                            },
                            'flashUsed': {
                                'type': ['boolean', 'null'],
                            },
                            'focalLength': {
                                'type': ['number', 'null'],
                            },
                            'isoSpeed': {
                                'type': ['integer', 'null'],
                            },
                            'meteringMode': {
                                'type': ['string', 'null'],
                            },
                            'sensor': {
                                'type': ['string', 'null'],
                            },
                            'exposureMode': {
                                'type': ['string', 'null'],
                            },
                            'colorSpace': {
                                'type': ['string', 'null'],
                            },
                            'whiteBalance': {
                                'type': ['string', 'null'],
                            },
                            'exposureBias': {
                                'type': ['number', 'null'],
                            },
                            'maxApertureValue': {
                                'type': ['number', 'null'],
                            },
                            'subjectDistance': {
                                'type': ['integer', 'null'],
                            },
                            'lens': {
                                'type': ['string', 'null'],
                            },
                            'location': {
                                'type': ['object', 'null'],
                                'properties': {
                                    'latitude': {
                                        'type': ['number', 'null'],
                                    },
                                    'longitude': {
                                        'type': ['number', 'null'],
                                    },
                                    'altitude': {
                                        'type': ['number', 'null'],
                                    },
                                },
                            },
                        },
                    },
                    'videoMediaMetadata': {
                        'type': ['object', 'null'],
                        'description': 'Additional metadata about video media',
                        'properties': {
                            'width': {
                                'type': ['integer', 'null'],
                            },
                            'height': {
                                'type': ['integer', 'null'],
                            },
                            'durationMillis': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'files',
            },
        ),
        EntityDefinition(
            name='files_export',
            actions=[Action.DOWNLOAD],
            endpoints={
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/export',
                    action=Action.DOWNLOAD,
                    description='Exports a Google Workspace file (Docs, Sheets, Slides, Drawings) to a specified format.\nCommon export formats:\n- application/pdf (all types)\n- text/plain (Docs)\n- text/csv (Sheets)\n- application/vnd.openxmlformats-officedocument.wordprocessingml.document (Docs to .docx)\n- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet (Sheets to .xlsx)\n- application/vnd.openxmlformats-officedocument.presentationml.presentation (Slides to .pptx)\nNote: Export has a 10MB limit. For larger files, use the Drive UI.\n',
                    query_params=['mimeType'],
                    query_params_schema={
                        'mimeType': {'type': 'string', 'required': True},
                    },
                    path_params=['fileId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                    },
                ),
            },
        ),
        EntityDefinition(
            name='drives',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/drives',
                    action=Action.LIST,
                    description="Lists the user's shared drives",
                    query_params=[
                        'pageSize',
                        'pageToken',
                        'q',
                        'useDomainAdminAccess',
                    ],
                    query_params_schema={
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'q': {'type': 'string', 'required': False},
                        'useDomainAdminAccess': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of shared drives',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of shared drives',
                            },
                            'drives': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Representation of a shared drive',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of this shared drive'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of this shared drive',
                                        },
                                        'colorRgb': {
                                            'type': ['string', 'null'],
                                            'description': 'The color of this shared drive as an RGB hex string',
                                        },
                                        'backgroundImageLink': {
                                            'type': ['string', 'null'],
                                            'description': "A short-lived link to this shared drive's background image",
                                        },
                                        'backgroundImageFile': {
                                            'type': ['object', 'null'],
                                            'description': 'An image file and cropping parameters for the background image',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'xCoordinate': {
                                                    'type': ['number', 'null'],
                                                },
                                                'yCoordinate': {
                                                    'type': ['number', 'null'],
                                                },
                                                'width': {
                                                    'type': ['number', 'null'],
                                                },
                                            },
                                        },
                                        'capabilities': {
                                            'type': ['object', 'null'],
                                            'description': 'Capabilities the current user has on this shared drive',
                                            'properties': {
                                                'canAddChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canComment': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canCopy': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canDeleteDrive': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canDownload': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canEdit': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canListChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canManageMembers': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canReadRevisions': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canRename': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canRenameDrive': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canChangeDriveBackground': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canShare': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canChangeCopyRequiresWriterPermissionRestriction': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canChangeDomainUsersOnlyRestriction': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canChangeDriveMembersOnlyRestriction': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canChangeSharingFoldersRequiresOrganizerPermissionRestriction': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canResetDriveRestrictions': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canDeleteChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'canTrashChildren': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'themeId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the theme from which the background image and color are set',
                                        },
                                        'createdTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which the shared drive was created',
                                        },
                                        'hidden': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the shared drive is hidden from default view',
                                        },
                                        'restrictions': {
                                            'type': ['object', 'null'],
                                            'description': 'A set of restrictions that apply to this shared drive',
                                            'properties': {
                                                'copyRequiresWriterPermission': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'domainUsersOnly': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'driveMembersOnly': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'adminManagedRestrictions': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'sharingFoldersRequiresOrganizerPermission': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        'orgUnitId': {
                                            'type': ['string', 'null'],
                                            'description': 'The organizational unit of this shared drive',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'drives',
                                },
                                'description': 'The list of shared drives',
                            },
                        },
                    },
                    record_extractor='$.drives',
                    meta_extractor={'nextPageToken': '$.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/drives/{driveId}',
                    action=Action.GET,
                    description="Gets a shared drive's metadata by ID",
                    query_params=['useDomainAdminAccess'],
                    query_params_schema={
                        'useDomainAdminAccess': {'type': 'boolean', 'required': False},
                    },
                    path_params=['driveId'],
                    path_params_schema={
                        'driveId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Representation of a shared drive',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'id': {'type': 'string', 'description': 'The ID of this shared drive'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of this shared drive',
                            },
                            'colorRgb': {
                                'type': ['string', 'null'],
                                'description': 'The color of this shared drive as an RGB hex string',
                            },
                            'backgroundImageLink': {
                                'type': ['string', 'null'],
                                'description': "A short-lived link to this shared drive's background image",
                            },
                            'backgroundImageFile': {
                                'type': ['object', 'null'],
                                'description': 'An image file and cropping parameters for the background image',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'xCoordinate': {
                                        'type': ['number', 'null'],
                                    },
                                    'yCoordinate': {
                                        'type': ['number', 'null'],
                                    },
                                    'width': {
                                        'type': ['number', 'null'],
                                    },
                                },
                            },
                            'capabilities': {
                                'type': ['object', 'null'],
                                'description': 'Capabilities the current user has on this shared drive',
                                'properties': {
                                    'canAddChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canComment': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canCopy': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canDeleteDrive': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canDownload': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canEdit': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canListChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canManageMembers': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canReadRevisions': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canRename': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canRenameDrive': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canChangeDriveBackground': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canShare': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canChangeCopyRequiresWriterPermissionRestriction': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canChangeDomainUsersOnlyRestriction': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canChangeDriveMembersOnlyRestriction': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canChangeSharingFoldersRequiresOrganizerPermissionRestriction': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canResetDriveRestrictions': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canDeleteChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'canTrashChildren': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'themeId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the theme from which the background image and color are set',
                            },
                            'createdTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time at which the shared drive was created',
                            },
                            'hidden': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the shared drive is hidden from default view',
                            },
                            'restrictions': {
                                'type': ['object', 'null'],
                                'description': 'A set of restrictions that apply to this shared drive',
                                'properties': {
                                    'copyRequiresWriterPermission': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'domainUsersOnly': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'driveMembersOnly': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'adminManagedRestrictions': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'sharingFoldersRequiresOrganizerPermission': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            'orgUnitId': {
                                'type': ['string', 'null'],
                                'description': 'The organizational unit of this shared drive',
                            },
                        },
                        'x-airbyte-entity-name': 'drives',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Representation of a shared drive',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'id': {'type': 'string', 'description': 'The ID of this shared drive'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of this shared drive',
                    },
                    'colorRgb': {
                        'type': ['string', 'null'],
                        'description': 'The color of this shared drive as an RGB hex string',
                    },
                    'backgroundImageLink': {
                        'type': ['string', 'null'],
                        'description': "A short-lived link to this shared drive's background image",
                    },
                    'backgroundImageFile': {
                        'type': ['object', 'null'],
                        'description': 'An image file and cropping parameters for the background image',
                        'properties': {
                            'id': {
                                'type': ['string', 'null'],
                            },
                            'xCoordinate': {
                                'type': ['number', 'null'],
                            },
                            'yCoordinate': {
                                'type': ['number', 'null'],
                            },
                            'width': {
                                'type': ['number', 'null'],
                            },
                        },
                    },
                    'capabilities': {
                        'type': ['object', 'null'],
                        'description': 'Capabilities the current user has on this shared drive',
                        'properties': {
                            'canAddChildren': {
                                'type': ['boolean', 'null'],
                            },
                            'canComment': {
                                'type': ['boolean', 'null'],
                            },
                            'canCopy': {
                                'type': ['boolean', 'null'],
                            },
                            'canDeleteDrive': {
                                'type': ['boolean', 'null'],
                            },
                            'canDownload': {
                                'type': ['boolean', 'null'],
                            },
                            'canEdit': {
                                'type': ['boolean', 'null'],
                            },
                            'canListChildren': {
                                'type': ['boolean', 'null'],
                            },
                            'canManageMembers': {
                                'type': ['boolean', 'null'],
                            },
                            'canReadRevisions': {
                                'type': ['boolean', 'null'],
                            },
                            'canRename': {
                                'type': ['boolean', 'null'],
                            },
                            'canRenameDrive': {
                                'type': ['boolean', 'null'],
                            },
                            'canChangeDriveBackground': {
                                'type': ['boolean', 'null'],
                            },
                            'canShare': {
                                'type': ['boolean', 'null'],
                            },
                            'canChangeCopyRequiresWriterPermissionRestriction': {
                                'type': ['boolean', 'null'],
                            },
                            'canChangeDomainUsersOnlyRestriction': {
                                'type': ['boolean', 'null'],
                            },
                            'canChangeDriveMembersOnlyRestriction': {
                                'type': ['boolean', 'null'],
                            },
                            'canChangeSharingFoldersRequiresOrganizerPermissionRestriction': {
                                'type': ['boolean', 'null'],
                            },
                            'canResetDriveRestrictions': {
                                'type': ['boolean', 'null'],
                            },
                            'canDeleteChildren': {
                                'type': ['boolean', 'null'],
                            },
                            'canTrashChildren': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'themeId': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the theme from which the background image and color are set',
                    },
                    'createdTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time at which the shared drive was created',
                    },
                    'hidden': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the shared drive is hidden from default view',
                    },
                    'restrictions': {
                        'type': ['object', 'null'],
                        'description': 'A set of restrictions that apply to this shared drive',
                        'properties': {
                            'copyRequiresWriterPermission': {
                                'type': ['boolean', 'null'],
                            },
                            'domainUsersOnly': {
                                'type': ['boolean', 'null'],
                            },
                            'driveMembersOnly': {
                                'type': ['boolean', 'null'],
                            },
                            'adminManagedRestrictions': {
                                'type': ['boolean', 'null'],
                            },
                            'sharingFoldersRequiresOrganizerPermission': {
                                'type': ['boolean', 'null'],
                            },
                        },
                    },
                    'orgUnitId': {
                        'type': ['string', 'null'],
                        'description': 'The organizational unit of this shared drive',
                    },
                },
                'x-airbyte-entity-name': 'drives',
            },
        ),
        EntityDefinition(
            name='permissions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/permissions',
                    action=Action.LIST,
                    description="Lists a file's or shared drive's permissions",
                    query_params=[
                        'pageSize',
                        'pageToken',
                        'supportsAllDrives',
                        'useDomainAdminAccess',
                    ],
                    query_params_schema={
                        'pageSize': {'type': 'integer', 'required': False},
                        'pageToken': {'type': 'string', 'required': False},
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                        'useDomainAdminAccess': {'type': 'boolean', 'required': False},
                    },
                    path_params=['fileId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of permissions for a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of permissions',
                            },
                            'permissions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A permission for a file',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of this permission'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of the grantee (user, group, domain, anyone)',
                                        },
                                        'emailAddress': {
                                            'type': ['string', 'null'],
                                            'description': 'The email address of the user or group',
                                        },
                                        'domain': {
                                            'type': ['string', 'null'],
                                            'description': 'The domain to which this permission refers',
                                        },
                                        'role': {
                                            'type': ['string', 'null'],
                                            'description': 'The role granted by this permission (owner, organizer, fileOrganizer, writer, commenter, reader)',
                                        },
                                        'view': {
                                            'type': ['string', 'null'],
                                            'description': 'Indicates the view for this permission',
                                        },
                                        'allowFileDiscovery': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the permission allows the file to be discovered through search',
                                        },
                                        'displayName': {
                                            'type': ['string', 'null'],
                                            'description': 'The displayable name of the grantee',
                                        },
                                        'photoLink': {
                                            'type': ['string', 'null'],
                                            'description': "A link to the user's profile photo",
                                        },
                                        'expirationTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which this permission will expire',
                                        },
                                        'teamDrivePermissionDetails': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'teamDrivePermissionType': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'role': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'inheritedFrom': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'inherited': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                            'description': 'Deprecated - use permissionDetails instead',
                                        },
                                        'permissionDetails': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'permissionType': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'role': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'inheritedFrom': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'inherited': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                            'description': 'Details of whether the permissions on this shared drive item are inherited',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the account associated with this permission has been deleted',
                                        },
                                        'pendingOwner': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the account associated with this permission is a pending owner',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'permissions',
                                },
                                'description': 'The list of permissions',
                            },
                        },
                    },
                    record_extractor='$.permissions',
                    meta_extractor={'nextPageToken': '$.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/permissions/{permissionId}',
                    action=Action.GET,
                    description='Gets a permission by ID',
                    query_params=['supportsAllDrives', 'useDomainAdminAccess'],
                    query_params_schema={
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                        'useDomainAdminAccess': {'type': 'boolean', 'required': False},
                    },
                    path_params=['fileId', 'permissionId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                        'permissionId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A permission for a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'id': {'type': 'string', 'description': 'The ID of this permission'},
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The type of the grantee (user, group, domain, anyone)',
                            },
                            'emailAddress': {
                                'type': ['string', 'null'],
                                'description': 'The email address of the user or group',
                            },
                            'domain': {
                                'type': ['string', 'null'],
                                'description': 'The domain to which this permission refers',
                            },
                            'role': {
                                'type': ['string', 'null'],
                                'description': 'The role granted by this permission (owner, organizer, fileOrganizer, writer, commenter, reader)',
                            },
                            'view': {
                                'type': ['string', 'null'],
                                'description': 'Indicates the view for this permission',
                            },
                            'allowFileDiscovery': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the permission allows the file to be discovered through search',
                            },
                            'displayName': {
                                'type': ['string', 'null'],
                                'description': 'The displayable name of the grantee',
                            },
                            'photoLink': {
                                'type': ['string', 'null'],
                                'description': "A link to the user's profile photo",
                            },
                            'expirationTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time at which this permission will expire',
                            },
                            'teamDrivePermissionDetails': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'teamDrivePermissionType': {
                                            'type': ['string', 'null'],
                                        },
                                        'role': {
                                            'type': ['string', 'null'],
                                        },
                                        'inheritedFrom': {
                                            'type': ['string', 'null'],
                                        },
                                        'inherited': {
                                            'type': ['boolean', 'null'],
                                        },
                                    },
                                },
                                'description': 'Deprecated - use permissionDetails instead',
                            },
                            'permissionDetails': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'permissionType': {
                                            'type': ['string', 'null'],
                                        },
                                        'role': {
                                            'type': ['string', 'null'],
                                        },
                                        'inheritedFrom': {
                                            'type': ['string', 'null'],
                                        },
                                        'inherited': {
                                            'type': ['boolean', 'null'],
                                        },
                                    },
                                },
                                'description': 'Details of whether the permissions on this shared drive item are inherited',
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the account associated with this permission has been deleted',
                            },
                            'pendingOwner': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the account associated with this permission is a pending owner',
                            },
                        },
                        'x-airbyte-entity-name': 'permissions',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A permission for a file',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'id': {'type': 'string', 'description': 'The ID of this permission'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of the grantee (user, group, domain, anyone)',
                    },
                    'emailAddress': {
                        'type': ['string', 'null'],
                        'description': 'The email address of the user or group',
                    },
                    'domain': {
                        'type': ['string', 'null'],
                        'description': 'The domain to which this permission refers',
                    },
                    'role': {
                        'type': ['string', 'null'],
                        'description': 'The role granted by this permission (owner, organizer, fileOrganizer, writer, commenter, reader)',
                    },
                    'view': {
                        'type': ['string', 'null'],
                        'description': 'Indicates the view for this permission',
                    },
                    'allowFileDiscovery': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the permission allows the file to be discovered through search',
                    },
                    'displayName': {
                        'type': ['string', 'null'],
                        'description': 'The displayable name of the grantee',
                    },
                    'photoLink': {
                        'type': ['string', 'null'],
                        'description': "A link to the user's profile photo",
                    },
                    'expirationTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time at which this permission will expire',
                    },
                    'teamDrivePermissionDetails': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': 'object',
                            'properties': {
                                'teamDrivePermissionType': {
                                    'type': ['string', 'null'],
                                },
                                'role': {
                                    'type': ['string', 'null'],
                                },
                                'inheritedFrom': {
                                    'type': ['string', 'null'],
                                },
                                'inherited': {
                                    'type': ['boolean', 'null'],
                                },
                            },
                        },
                        'description': 'Deprecated - use permissionDetails instead',
                    },
                    'permissionDetails': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': 'object',
                            'properties': {
                                'permissionType': {
                                    'type': ['string', 'null'],
                                },
                                'role': {
                                    'type': ['string', 'null'],
                                },
                                'inheritedFrom': {
                                    'type': ['string', 'null'],
                                },
                                'inherited': {
                                    'type': ['boolean', 'null'],
                                },
                            },
                        },
                        'description': 'Details of whether the permissions on this shared drive item are inherited',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the account associated with this permission has been deleted',
                    },
                    'pendingOwner': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the account associated with this permission is a pending owner',
                    },
                },
                'x-airbyte-entity-name': 'permissions',
            },
        ),
        EntityDefinition(
            name='comments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/comments',
                    action=Action.LIST,
                    description="Lists a file's comments",
                    query_params=[
                        'pageSize',
                        'pageToken',
                        'startModifiedTime',
                        'includeDeleted',
                        'fields',
                    ],
                    query_params_schema={
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'startModifiedTime': {'type': 'string', 'required': False},
                        'includeDeleted': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': '*',
                        },
                    },
                    path_params=['fileId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of comments on a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of comments',
                            },
                            'comments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A comment on a file',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of the comment'},
                                        'createdTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which the comment was created',
                                        },
                                        'modifiedTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the comment or any of its replies was modified',
                                        },
                                        'author': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The author of the comment',
                                        },
                                        'htmlContent': {
                                            'type': ['string', 'null'],
                                            'description': 'The content of the comment with HTML formatting',
                                        },
                                        'content': {
                                            'type': ['string', 'null'],
                                            'description': 'The plain text content of the comment',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the comment has been deleted',
                                        },
                                        'resolved': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the comment has been resolved by one of its replies',
                                        },
                                        'quotedFileContent': {
                                            'type': ['object', 'null'],
                                            'description': 'The file content to which the comment refers',
                                            'properties': {
                                                'mimeType': {
                                                    'type': ['string', 'null'],
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                        'anchor': {
                                            'type': ['string', 'null'],
                                            'description': 'A region of the document represented as a JSON string',
                                        },
                                        'replies': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'description': 'A reply to a comment on a file',
                                                'properties': {
                                                    'kind': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Identifies what kind of resource this is',
                                                    },
                                                    'id': {'type': 'string', 'description': 'The ID of the reply'},
                                                    'createdTime': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'The time at which the reply was created',
                                                    },
                                                    'modifiedTime': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'The last time the reply was modified',
                                                    },
                                                    'author': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'description': 'Information about a Drive user',
                                                                'properties': {
                                                                    'kind': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Identifies what kind of resource this is',
                                                                    },
                                                                    'displayName': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'A plain text displayable name for this user',
                                                                    },
                                                                    'photoLink': {
                                                                        'type': ['string', 'null'],
                                                                        'description': "A link to the user's profile photo",
                                                                    },
                                                                    'me': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this user is the requesting user',
                                                                    },
                                                                    'permissionId': {
                                                                        'type': ['string', 'null'],
                                                                        'description': "The user's ID as visible in Permission resources",
                                                                    },
                                                                    'emailAddress': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The email address of the user',
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                        'description': 'The author of the reply',
                                                    },
                                                    'htmlContent': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The content of the reply with HTML formatting',
                                                    },
                                                    'content': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The plain text content of the reply',
                                                    },
                                                    'deleted': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether the reply has been deleted',
                                                    },
                                                    'action': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The action the reply performed to the parent comment (resolve, reopen)',
                                                    },
                                                },
                                                'x-airbyte-entity-name': 'replies',
                                            },
                                            'description': 'The full list of replies to the comment',
                                        },
                                        'mentionedEmailAddresses': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Email addresses mentioned in the comment',
                                        },
                                        'assigneeEmailAddress': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address of the user assigned to this comment',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'comments',
                                },
                                'description': 'The list of comments',
                            },
                        },
                    },
                    record_extractor='$.comments',
                    meta_extractor={'nextPageToken': '$.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/comments/{commentId}',
                    action=Action.GET,
                    description='Gets a comment by ID',
                    query_params=['includeDeleted', 'fields'],
                    query_params_schema={
                        'includeDeleted': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': '*',
                        },
                    },
                    path_params=['fileId', 'commentId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                        'commentId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A comment on a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'id': {'type': 'string', 'description': 'The ID of the comment'},
                            'createdTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time at which the comment was created',
                            },
                            'modifiedTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The last time the comment or any of its replies was modified',
                            },
                            'author': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The author of the comment',
                            },
                            'htmlContent': {
                                'type': ['string', 'null'],
                                'description': 'The content of the comment with HTML formatting',
                            },
                            'content': {
                                'type': ['string', 'null'],
                                'description': 'The plain text content of the comment',
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the comment has been deleted',
                            },
                            'resolved': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the comment has been resolved by one of its replies',
                            },
                            'quotedFileContent': {
                                'type': ['object', 'null'],
                                'description': 'The file content to which the comment refers',
                                'properties': {
                                    'mimeType': {
                                        'type': ['string', 'null'],
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            'anchor': {
                                'type': ['string', 'null'],
                                'description': 'A region of the document represented as a JSON string',
                            },
                            'replies': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'description': 'A reply to a comment on a file',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of the reply'},
                                        'createdTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which the reply was created',
                                        },
                                        'modifiedTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the reply was modified',
                                        },
                                        'author': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The author of the reply',
                                        },
                                        'htmlContent': {
                                            'type': ['string', 'null'],
                                            'description': 'The content of the reply with HTML formatting',
                                        },
                                        'content': {
                                            'type': ['string', 'null'],
                                            'description': 'The plain text content of the reply',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the reply has been deleted',
                                        },
                                        'action': {
                                            'type': ['string', 'null'],
                                            'description': 'The action the reply performed to the parent comment (resolve, reopen)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'replies',
                                },
                                'description': 'The full list of replies to the comment',
                            },
                            'mentionedEmailAddresses': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'Email addresses mentioned in the comment',
                            },
                            'assigneeEmailAddress': {
                                'type': ['string', 'null'],
                                'description': 'Email address of the user assigned to this comment',
                            },
                        },
                        'x-airbyte-entity-name': 'comments',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A comment on a file',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'id': {'type': 'string', 'description': 'The ID of the comment'},
                    'createdTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time at which the comment was created',
                    },
                    'modifiedTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The last time the comment or any of its replies was modified',
                    },
                    'author': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The author of the comment',
                    },
                    'htmlContent': {
                        'type': ['string', 'null'],
                        'description': 'The content of the comment with HTML formatting',
                    },
                    'content': {
                        'type': ['string', 'null'],
                        'description': 'The plain text content of the comment',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the comment has been deleted',
                    },
                    'resolved': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the comment has been resolved by one of its replies',
                    },
                    'quotedFileContent': {
                        'type': ['object', 'null'],
                        'description': 'The file content to which the comment refers',
                        'properties': {
                            'mimeType': {
                                'type': ['string', 'null'],
                            },
                            'value': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    'anchor': {
                        'type': ['string', 'null'],
                        'description': 'A region of the document represented as a JSON string',
                    },
                    'replies': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Reply'},
                        'description': 'The full list of replies to the comment',
                    },
                    'mentionedEmailAddresses': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'Email addresses mentioned in the comment',
                    },
                    'assigneeEmailAddress': {
                        'type': ['string', 'null'],
                        'description': 'Email address of the user assigned to this comment',
                    },
                },
                'x-airbyte-entity-name': 'comments',
            },
        ),
        EntityDefinition(
            name='replies',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/comments/{commentId}/replies',
                    action=Action.LIST,
                    description="Lists a comment's replies",
                    query_params=[
                        'pageSize',
                        'pageToken',
                        'includeDeleted',
                        'fields',
                    ],
                    query_params_schema={
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 20,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'includeDeleted': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': '*',
                        },
                    },
                    path_params=['fileId', 'commentId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                        'commentId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of replies to a comment',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of replies',
                            },
                            'replies': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A reply to a comment on a file',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of the reply'},
                                        'createdTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time at which the reply was created',
                                        },
                                        'modifiedTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the reply was modified',
                                        },
                                        'author': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The author of the reply',
                                        },
                                        'htmlContent': {
                                            'type': ['string', 'null'],
                                            'description': 'The content of the reply with HTML formatting',
                                        },
                                        'content': {
                                            'type': ['string', 'null'],
                                            'description': 'The plain text content of the reply',
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the reply has been deleted',
                                        },
                                        'action': {
                                            'type': ['string', 'null'],
                                            'description': 'The action the reply performed to the parent comment (resolve, reopen)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'replies',
                                },
                                'description': 'The list of replies',
                            },
                        },
                    },
                    record_extractor='$.replies',
                    meta_extractor={'nextPageToken': '$.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/comments/{commentId}/replies/{replyId}',
                    action=Action.GET,
                    description='Gets a reply by ID',
                    query_params=['includeDeleted', 'fields'],
                    query_params_schema={
                        'includeDeleted': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': '*',
                        },
                    },
                    path_params=['fileId', 'commentId', 'replyId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                        'commentId': {'type': 'string', 'required': True},
                        'replyId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A reply to a comment on a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'id': {'type': 'string', 'description': 'The ID of the reply'},
                            'createdTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The time at which the reply was created',
                            },
                            'modifiedTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The last time the reply was modified',
                            },
                            'author': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The author of the reply',
                            },
                            'htmlContent': {
                                'type': ['string', 'null'],
                                'description': 'The content of the reply with HTML formatting',
                            },
                            'content': {
                                'type': ['string', 'null'],
                                'description': 'The plain text content of the reply',
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the reply has been deleted',
                            },
                            'action': {
                                'type': ['string', 'null'],
                                'description': 'The action the reply performed to the parent comment (resolve, reopen)',
                            },
                        },
                        'x-airbyte-entity-name': 'replies',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A reply to a comment on a file',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'id': {'type': 'string', 'description': 'The ID of the reply'},
                    'createdTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time at which the reply was created',
                    },
                    'modifiedTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The last time the reply was modified',
                    },
                    'author': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The author of the reply',
                    },
                    'htmlContent': {
                        'type': ['string', 'null'],
                        'description': 'The content of the reply with HTML formatting',
                    },
                    'content': {
                        'type': ['string', 'null'],
                        'description': 'The plain text content of the reply',
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the reply has been deleted',
                    },
                    'action': {
                        'type': ['string', 'null'],
                        'description': 'The action the reply performed to the parent comment (resolve, reopen)',
                    },
                },
                'x-airbyte-entity-name': 'replies',
            },
        ),
        EntityDefinition(
            name='revisions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/revisions',
                    action=Action.LIST,
                    description="Lists a file's revisions",
                    query_params=['pageSize', 'pageToken'],
                    query_params_schema={
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                    },
                    path_params=['fileId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of revisions of a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of revisions',
                            },
                            'revisions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'The metadata for a revision to a file',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID of the revision'},
                                        'mimeType': {
                                            'type': ['string', 'null'],
                                            'description': 'The MIME type of the revision',
                                        },
                                        'modifiedTime': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The last time the revision was modified',
                                        },
                                        'keepForever': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether to keep this revision forever',
                                        },
                                        'published': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this revision is published',
                                        },
                                        'publishedLink': {
                                            'type': ['string', 'null'],
                                            'description': 'A link to the published revision',
                                        },
                                        'publishAuto': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether subsequent revisions will be automatically republished',
                                        },
                                        'publishedOutsideDomain': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this revision is published outside the domain',
                                        },
                                        'lastModifyingUser': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Information about a Drive user',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'displayName': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A plain text displayable name for this user',
                                                        },
                                                        'photoLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A link to the user's profile photo",
                                                        },
                                                        'me': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this user is the requesting user',
                                                        },
                                                        'permissionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The user's ID as visible in Permission resources",
                                                        },
                                                        'emailAddress': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email address of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The last user to modify this revision',
                                        },
                                        'originalFilename': {
                                            'type': ['string', 'null'],
                                            'description': 'The original filename used to create this revision',
                                        },
                                        'md5Checksum': {
                                            'type': ['string', 'null'],
                                            'description': "The MD5 checksum of the revision's content",
                                        },
                                        'size': {
                                            'type': ['string', 'null'],
                                            'description': "The size of the revision's content in bytes",
                                        },
                                        'exportLinks': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {'type': 'string'},
                                            'description': 'Links for exporting Docs Editors files to specific formats',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'revisions',
                                },
                                'description': 'The list of revisions',
                            },
                        },
                    },
                    record_extractor='$.revisions',
                    meta_extractor={'nextPageToken': '$.nextPageToken'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/files/{fileId}/revisions/{revisionId}',
                    action=Action.GET,
                    description="Gets a revision's metadata by ID",
                    path_params=['fileId', 'revisionId'],
                    path_params_schema={
                        'fileId': {'type': 'string', 'required': True},
                        'revisionId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'The metadata for a revision to a file',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'id': {'type': 'string', 'description': 'The ID of the revision'},
                            'mimeType': {
                                'type': ['string', 'null'],
                                'description': 'The MIME type of the revision',
                            },
                            'modifiedTime': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The last time the revision was modified',
                            },
                            'keepForever': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to keep this revision forever',
                            },
                            'published': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this revision is published',
                            },
                            'publishedLink': {
                                'type': ['string', 'null'],
                                'description': 'A link to the published revision',
                            },
                            'publishAuto': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether subsequent revisions will be automatically republished',
                            },
                            'publishedOutsideDomain': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether this revision is published outside the domain',
                            },
                            'lastModifyingUser': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The last user to modify this revision',
                            },
                            'originalFilename': {
                                'type': ['string', 'null'],
                                'description': 'The original filename used to create this revision',
                            },
                            'md5Checksum': {
                                'type': ['string', 'null'],
                                'description': "The MD5 checksum of the revision's content",
                            },
                            'size': {
                                'type': ['string', 'null'],
                                'description': "The size of the revision's content in bytes",
                            },
                            'exportLinks': {
                                'type': ['object', 'null'],
                                'additionalProperties': {'type': 'string'},
                                'description': 'Links for exporting Docs Editors files to specific formats',
                            },
                        },
                        'x-airbyte-entity-name': 'revisions',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'The metadata for a revision to a file',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'id': {'type': 'string', 'description': 'The ID of the revision'},
                    'mimeType': {
                        'type': ['string', 'null'],
                        'description': 'The MIME type of the revision',
                    },
                    'modifiedTime': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The last time the revision was modified',
                    },
                    'keepForever': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether to keep this revision forever',
                    },
                    'published': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this revision is published',
                    },
                    'publishedLink': {
                        'type': ['string', 'null'],
                        'description': 'A link to the published revision',
                    },
                    'publishAuto': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether subsequent revisions will be automatically republished',
                    },
                    'publishedOutsideDomain': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this revision is published outside the domain',
                    },
                    'lastModifyingUser': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The last user to modify this revision',
                    },
                    'originalFilename': {
                        'type': ['string', 'null'],
                        'description': 'The original filename used to create this revision',
                    },
                    'md5Checksum': {
                        'type': ['string', 'null'],
                        'description': "The MD5 checksum of the revision's content",
                    },
                    'size': {
                        'type': ['string', 'null'],
                        'description': "The size of the revision's content in bytes",
                    },
                    'exportLinks': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'string'},
                        'description': 'Links for exporting Docs Editors files to specific formats',
                    },
                },
                'x-airbyte-entity-name': 'revisions',
            },
        ),
        EntityDefinition(
            name='changes',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/changes',
                    action=Action.LIST,
                    description='Lists the changes for a user or shared drive',
                    query_params=[
                        'pageToken',
                        'pageSize',
                        'driveId',
                        'includeItemsFromAllDrives',
                        'supportsAllDrives',
                        'spaces',
                        'includeRemoved',
                        'restrictToMyDrive',
                    ],
                    query_params_schema={
                        'pageToken': {'type': 'string', 'required': True},
                        'pageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'driveId': {'type': 'string', 'required': False},
                        'includeItemsFromAllDrives': {'type': 'boolean', 'required': False},
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                        'spaces': {'type': 'string', 'required': False},
                        'includeRemoved': {
                            'type': 'boolean',
                            'required': False,
                            'default': True,
                        },
                        'restrictToMyDrive': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of changes for a user',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The page token for the next page of changes',
                            },
                            'newStartPageToken': {
                                'type': ['string', 'null'],
                                'description': 'The starting page token for future changes',
                            },
                            'changes': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A change to a file or shared drive',
                                    'properties': {
                                        'kind': {
                                            'type': ['string', 'null'],
                                            'description': 'Identifies what kind of resource this is',
                                        },
                                        'removed': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the file or shared drive has been removed',
                                        },
                                        'file': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'The metadata for a file',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'id': {'type': 'string', 'description': 'The ID of the file'},
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the file',
                                                        },
                                                        'mimeType': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The MIME type of the file',
                                                        },
                                                        'description': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A short description of the file',
                                                        },
                                                        'starred': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the user has starred the file',
                                                        },
                                                        'trashed': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the file has been trashed',
                                                        },
                                                        'explicitlyTrashed': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the file has been explicitly trashed',
                                                        },
                                                        'parents': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                            'description': 'The IDs of the parent folders',
                                                        },
                                                        'properties': {
                                                            'type': ['object', 'null'],
                                                            'additionalProperties': {'type': 'string'},
                                                            'description': 'A collection of arbitrary key-value pairs',
                                                        },
                                                        'appProperties': {
                                                            'type': ['object', 'null'],
                                                            'additionalProperties': {'type': 'string'},
                                                            'description': 'A collection of arbitrary key-value pairs private to the app',
                                                        },
                                                        'spaces': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                            'description': 'The list of spaces which contain the file',
                                                        },
                                                        'version': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A monotonically increasing version number for the file',
                                                        },
                                                        'webContentLink': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A link for downloading the content of the file',
                                                        },
                                                        'webViewLink': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A link for opening the file in a relevant Google editor or viewer',
                                                        },
                                                        'iconLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A static, unauthenticated link to the file's icon",
                                                        },
                                                        'hasThumbnail': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether this file has a thumbnail',
                                                        },
                                                        'thumbnailLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A short-lived link to the file's thumbnail",
                                                        },
                                                        'thumbnailVersion': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The thumbnail version for use in thumbnail cache invalidation',
                                                        },
                                                        'viewedByMe': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the file has been viewed by this user',
                                                        },
                                                        'viewedByMeTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The last time the file was viewed by the user',
                                                        },
                                                        'createdTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The time at which the file was created',
                                                        },
                                                        'modifiedTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The last time the file was modified by anyone',
                                                        },
                                                        'modifiedByMeTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The last time the file was modified by the user',
                                                        },
                                                        'modifiedByMe': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the file has been modified by this user',
                                                        },
                                                        'sharedWithMeTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The time at which the file was shared with the user',
                                                        },
                                                        'sharingUser': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Information about a Drive user',
                                                                    'properties': {
                                                                        'kind': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Identifies what kind of resource this is',
                                                                        },
                                                                        'displayName': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'A plain text displayable name for this user',
                                                                        },
                                                                        'photoLink': {
                                                                            'type': ['string', 'null'],
                                                                            'description': "A link to the user's profile photo",
                                                                        },
                                                                        'me': {
                                                                            'type': ['boolean', 'null'],
                                                                            'description': 'Whether this user is the requesting user',
                                                                        },
                                                                        'permissionId': {
                                                                            'type': ['string', 'null'],
                                                                            'description': "The user's ID as visible in Permission resources",
                                                                        },
                                                                        'emailAddress': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The email address of the user',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'The user who shared the file with the requesting user',
                                                        },
                                                        'owners': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'Information about a Drive user',
                                                                'properties': {
                                                                    'kind': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Identifies what kind of resource this is',
                                                                    },
                                                                    'displayName': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'A plain text displayable name for this user',
                                                                    },
                                                                    'photoLink': {
                                                                        'type': ['string', 'null'],
                                                                        'description': "A link to the user's profile photo",
                                                                    },
                                                                    'me': {
                                                                        'type': ['boolean', 'null'],
                                                                        'description': 'Whether this user is the requesting user',
                                                                    },
                                                                    'permissionId': {
                                                                        'type': ['string', 'null'],
                                                                        'description': "The user's ID as visible in Permission resources",
                                                                    },
                                                                    'emailAddress': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The email address of the user',
                                                                    },
                                                                },
                                                            },
                                                            'description': 'The owner of this file',
                                                        },
                                                        'driveId': {
                                                            'type': ['string', 'null'],
                                                            'description': 'ID of the shared drive the file resides in',
                                                        },
                                                        'lastModifyingUser': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Information about a Drive user',
                                                                    'properties': {
                                                                        'kind': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Identifies what kind of resource this is',
                                                                        },
                                                                        'displayName': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'A plain text displayable name for this user',
                                                                        },
                                                                        'photoLink': {
                                                                            'type': ['string', 'null'],
                                                                            'description': "A link to the user's profile photo",
                                                                        },
                                                                        'me': {
                                                                            'type': ['boolean', 'null'],
                                                                            'description': 'Whether this user is the requesting user',
                                                                        },
                                                                        'permissionId': {
                                                                            'type': ['string', 'null'],
                                                                            'description': "The user's ID as visible in Permission resources",
                                                                        },
                                                                        'emailAddress': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The email address of the user',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'The last user to modify the file',
                                                        },
                                                        'shared': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the file has been shared',
                                                        },
                                                        'ownedByMe': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the user owns the file',
                                                        },
                                                        'capabilities': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Capabilities the current user has on this file',
                                                            'properties': {
                                                                'canEdit': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canComment': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canShare': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canCopy': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canDownload': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canDelete': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canRename': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canTrash': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canReadRevisions': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canAddChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canListChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canRemoveChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                            },
                                                        },
                                                        'viewersCanCopyContent': {
                                                            'type': ['boolean', 'null'],
                                                            'description': "Whether users with only reader or commenter permission can copy the file's content",
                                                        },
                                                        'copyRequiresWriterPermission': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the options to copy, print, or download this file should be disabled',
                                                        },
                                                        'writersCanShare': {
                                                            'type': ['boolean', 'null'],
                                                            'description': "Whether users with only writer permission can modify the file's permissions",
                                                        },
                                                        'permissionIds': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                            'description': 'List of permission IDs for users with access to this file',
                                                        },
                                                        'folderColorRgb': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The color for a folder as an RGB hex string',
                                                        },
                                                        'originalFilename': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The original filename of the uploaded content',
                                                        },
                                                        'fullFileExtension': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The full file extension extracted from the name field',
                                                        },
                                                        'fileExtension': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The final component of fullFileExtension',
                                                        },
                                                        'md5Checksum': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The MD5 checksum for the content of the file',
                                                        },
                                                        'sha1Checksum': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The SHA1 checksum for the content of the file',
                                                        },
                                                        'sha256Checksum': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The SHA256 checksum for the content of the file',
                                                        },
                                                        'size': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Size in bytes of blobs and first party editor files',
                                                        },
                                                        'quotaBytesUsed': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The number of storage quota bytes used by the file',
                                                        },
                                                        'headRevisionId': {
                                                            'type': ['string', 'null'],
                                                            'description': "The ID of the file's head revision",
                                                        },
                                                        'isAppAuthorized': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the file was created or opened by the requesting app',
                                                        },
                                                        'exportLinks': {
                                                            'type': ['object', 'null'],
                                                            'additionalProperties': {'type': 'string'},
                                                            'description': 'Links for exporting Docs Editors files to specific formats',
                                                        },
                                                        'shortcutDetails': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Shortcut file details',
                                                            'properties': {
                                                                'targetId': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'targetMimeType': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'targetResourceKey': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                            },
                                                        },
                                                        'contentRestrictions': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'readOnly': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                    'reason': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'restrictingUser': {
                                                                        'oneOf': [
                                                                            {
                                                                                'type': 'object',
                                                                                'description': 'Information about a Drive user',
                                                                                'properties': {
                                                                                    'kind': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'Identifies what kind of resource this is',
                                                                                    },
                                                                                    'displayName': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'A plain text displayable name for this user',
                                                                                    },
                                                                                    'photoLink': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': "A link to the user's profile photo",
                                                                                    },
                                                                                    'me': {
                                                                                        'type': ['boolean', 'null'],
                                                                                        'description': 'Whether this user is the requesting user',
                                                                                    },
                                                                                    'permissionId': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': "The user's ID as visible in Permission resources",
                                                                                    },
                                                                                    'emailAddress': {
                                                                                        'type': ['string', 'null'],
                                                                                        'description': 'The email address of the user',
                                                                                    },
                                                                                },
                                                                            },
                                                                            {'type': 'null'},
                                                                        ],
                                                                    },
                                                                    'restrictionTime': {
                                                                        'type': ['string', 'null'],
                                                                        'format': 'date-time',
                                                                    },
                                                                    'type': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            'description': 'Restrictions for accessing the content of the file',
                                                        },
                                                        'resourceKey': {
                                                            'type': ['string', 'null'],
                                                            'description': 'A key needed to access the item via a shared link',
                                                        },
                                                        'linkShareMetadata': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Contains details about the link URLs',
                                                            'properties': {
                                                                'securityUpdateEligible': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'securityUpdateEnabled': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                            },
                                                        },
                                                        'labelInfo': {
                                                            'type': ['object', 'null'],
                                                            'description': 'An overview of the labels on the file',
                                                            'properties': {
                                                                'labels': {
                                                                    'type': ['array', 'null'],
                                                                    'items': {'type': 'object'},
                                                                },
                                                            },
                                                        },
                                                        'trashedTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The time that the item was trashed',
                                                        },
                                                        'trashingUser': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'Information about a Drive user',
                                                                    'properties': {
                                                                        'kind': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'Identifies what kind of resource this is',
                                                                        },
                                                                        'displayName': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'A plain text displayable name for this user',
                                                                        },
                                                                        'photoLink': {
                                                                            'type': ['string', 'null'],
                                                                            'description': "A link to the user's profile photo",
                                                                        },
                                                                        'me': {
                                                                            'type': ['boolean', 'null'],
                                                                            'description': 'Whether this user is the requesting user',
                                                                        },
                                                                        'permissionId': {
                                                                            'type': ['string', 'null'],
                                                                            'description': "The user's ID as visible in Permission resources",
                                                                        },
                                                                        'emailAddress': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The email address of the user',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'The user who trashed the file',
                                                        },
                                                        'imageMediaMetadata': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Additional metadata about image media',
                                                            'properties': {
                                                                'width': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'height': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'rotation': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'time': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'cameraMake': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'cameraModel': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'exposureTime': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'aperture': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'flashUsed': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'focalLength': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'isoSpeed': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'meteringMode': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'sensor': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'exposureMode': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'colorSpace': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'whiteBalance': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'exposureBias': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'maxApertureValue': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'subjectDistance': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'lens': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'location': {
                                                                    'type': ['object', 'null'],
                                                                    'properties': {
                                                                        'latitude': {
                                                                            'type': ['number', 'null'],
                                                                        },
                                                                        'longitude': {
                                                                            'type': ['number', 'null'],
                                                                        },
                                                                        'altitude': {
                                                                            'type': ['number', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'videoMediaMetadata': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Additional metadata about video media',
                                                            'properties': {
                                                                'width': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'height': {
                                                                    'type': ['integer', 'null'],
                                                                },
                                                                'durationMillis': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'x-airbyte-entity-name': 'files',
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The updated state of the file',
                                        },
                                        'fileId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the file which has changed',
                                        },
                                        'driveId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the shared drive associated with this change',
                                        },
                                        'drive': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Representation of a shared drive',
                                                    'properties': {
                                                        'kind': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Identifies what kind of resource this is',
                                                        },
                                                        'id': {'type': 'string', 'description': 'The ID of this shared drive'},
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of this shared drive',
                                                        },
                                                        'colorRgb': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The color of this shared drive as an RGB hex string',
                                                        },
                                                        'backgroundImageLink': {
                                                            'type': ['string', 'null'],
                                                            'description': "A short-lived link to this shared drive's background image",
                                                        },
                                                        'backgroundImageFile': {
                                                            'type': ['object', 'null'],
                                                            'description': 'An image file and cropping parameters for the background image',
                                                            'properties': {
                                                                'id': {
                                                                    'type': ['string', 'null'],
                                                                },
                                                                'xCoordinate': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'yCoordinate': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                                'width': {
                                                                    'type': ['number', 'null'],
                                                                },
                                                            },
                                                        },
                                                        'capabilities': {
                                                            'type': ['object', 'null'],
                                                            'description': 'Capabilities the current user has on this shared drive',
                                                            'properties': {
                                                                'canAddChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canComment': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canCopy': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canDeleteDrive': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canDownload': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canEdit': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canListChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canManageMembers': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canReadRevisions': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canRename': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canRenameDrive': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canChangeDriveBackground': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canShare': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canChangeCopyRequiresWriterPermissionRestriction': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canChangeDomainUsersOnlyRestriction': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canChangeDriveMembersOnlyRestriction': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canChangeSharingFoldersRequiresOrganizerPermissionRestriction': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canResetDriveRestrictions': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canDeleteChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'canTrashChildren': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                            },
                                                        },
                                                        'themeId': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the theme from which the background image and color are set',
                                                        },
                                                        'createdTime': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'The time at which the shared drive was created',
                                                        },
                                                        'hidden': {
                                                            'type': ['boolean', 'null'],
                                                            'description': 'Whether the shared drive is hidden from default view',
                                                        },
                                                        'restrictions': {
                                                            'type': ['object', 'null'],
                                                            'description': 'A set of restrictions that apply to this shared drive',
                                                            'properties': {
                                                                'copyRequiresWriterPermission': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'domainUsersOnly': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'driveMembersOnly': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'adminManagedRestrictions': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                                'sharingFoldersRequiresOrganizerPermission': {
                                                                    'type': ['boolean', 'null'],
                                                                },
                                                            },
                                                        },
                                                        'orgUnitId': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The organizational unit of this shared drive',
                                                        },
                                                    },
                                                    'x-airbyte-entity-name': 'drives',
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The updated state of the shared drive',
                                        },
                                        'time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The time of this change',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of the change (file or drive)',
                                        },
                                        'changeType': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of the change (file or drive)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'changes',
                                },
                                'description': 'The list of changes',
                            },
                        },
                    },
                    record_extractor='$.changes',
                    meta_extractor={'nextPageToken': '$.nextPageToken', 'newStartPageToken': '$.newStartPageToken'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A change to a file or shared drive',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'removed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the file or shared drive has been removed',
                    },
                    'file': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/File'},
                            {'type': 'null'},
                        ],
                        'description': 'The updated state of the file',
                    },
                    'fileId': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the file which has changed',
                    },
                    'driveId': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the shared drive associated with this change',
                    },
                    'drive': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Drive'},
                            {'type': 'null'},
                        ],
                        'description': 'The updated state of the shared drive',
                    },
                    'time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The time of this change',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of the change (file or drive)',
                    },
                    'changeType': {
                        'type': ['string', 'null'],
                        'description': 'The type of the change (file or drive)',
                    },
                },
                'x-airbyte-entity-name': 'changes',
            },
        ),
        EntityDefinition(
            name='changes_start_page_token',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/changes/startPageToken',
                    action=Action.GET,
                    description='Gets the starting pageToken for listing future changes',
                    query_params=['driveId', 'supportsAllDrives'],
                    query_params_schema={
                        'driveId': {'type': 'string', 'required': False},
                        'supportsAllDrives': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'The starting page token for listing changes',
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'startPageToken': {'type': 'string', 'description': 'The starting page token for listing changes'},
                        },
                        'x-airbyte-entity-name': 'changes_start_page_token',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'The starting page token for listing changes',
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'startPageToken': {'type': 'string', 'description': 'The starting page token for listing changes'},
                },
                'x-airbyte-entity-name': 'changes_start_page_token',
            },
        ),
        EntityDefinition(
            name='about',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/drive/v3/about',
                    action=Action.GET,
                    description="Gets information about the user, the user's Drive, and system capabilities",
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': "Information about the user, the user's Drive, and system capabilities",
                        'properties': {
                            'kind': {
                                'type': ['string', 'null'],
                                'description': 'Identifies what kind of resource this is',
                            },
                            'user': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Information about a Drive user',
                                        'properties': {
                                            'kind': {
                                                'type': ['string', 'null'],
                                                'description': 'Identifies what kind of resource this is',
                                            },
                                            'displayName': {
                                                'type': ['string', 'null'],
                                                'description': 'A plain text displayable name for this user',
                                            },
                                            'photoLink': {
                                                'type': ['string', 'null'],
                                                'description': "A link to the user's profile photo",
                                            },
                                            'me': {
                                                'type': ['boolean', 'null'],
                                                'description': 'Whether this user is the requesting user',
                                            },
                                            'permissionId': {
                                                'type': ['string', 'null'],
                                                'description': "The user's ID as visible in Permission resources",
                                            },
                                            'emailAddress': {
                                                'type': ['string', 'null'],
                                                'description': 'The email address of the user',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The authenticated user',
                            },
                            'storageQuota': {
                                'type': ['object', 'null'],
                                'description': "The user's storage quota limits and usage",
                                'properties': {
                                    'limit': {
                                        'type': ['string', 'null'],
                                        'description': 'The usage limit, if applicable',
                                    },
                                    'usage': {
                                        'type': ['string', 'null'],
                                        'description': 'The total usage across all services',
                                    },
                                    'usageInDrive': {
                                        'type': ['string', 'null'],
                                        'description': 'The usage by all files in Google Drive',
                                    },
                                    'usageInDriveTrash': {
                                        'type': ['string', 'null'],
                                        'description': 'The usage by trashed files in Google Drive',
                                    },
                                },
                            },
                            'importFormats': {
                                'type': ['object', 'null'],
                                'additionalProperties': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                },
                                'description': 'A map of source MIME type to possible targets for all supported imports',
                            },
                            'exportFormats': {
                                'type': ['object', 'null'],
                                'additionalProperties': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                },
                                'description': 'A map of source MIME type to possible targets for all supported exports',
                            },
                            'maxImportSizes': {
                                'type': ['object', 'null'],
                                'additionalProperties': {'type': 'string'},
                                'description': 'A map of maximum import sizes by MIME type',
                            },
                            'maxUploadSize': {
                                'type': ['string', 'null'],
                                'description': 'The maximum upload size in bytes',
                            },
                            'appInstalled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user has installed the requesting app',
                            },
                            'folderColorPalette': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'The currently supported folder colors as RGB hex strings',
                            },
                            'driveThemes': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'backgroundImageLink': {
                                            'type': ['string', 'null'],
                                        },
                                        'colorRgb': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'A list of themes that are supported for shared drives',
                            },
                            'canCreateDrives': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the user can create shared drives',
                            },
                            'canCreateTeamDrives': {
                                'type': ['boolean', 'null'],
                                'description': 'Deprecated - use canCreateDrives instead',
                            },
                            'teamDriveThemes': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'backgroundImageLink': {
                                            'type': ['string', 'null'],
                                        },
                                        'colorRgb': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                                'description': 'Deprecated - use driveThemes instead',
                            },
                        },
                        'x-airbyte-entity-name': 'about',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': "Information about the user, the user's Drive, and system capabilities",
                'properties': {
                    'kind': {
                        'type': ['string', 'null'],
                        'description': 'Identifies what kind of resource this is',
                    },
                    'user': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/User'},
                            {'type': 'null'},
                        ],
                        'description': 'The authenticated user',
                    },
                    'storageQuota': {
                        'type': ['object', 'null'],
                        'description': "The user's storage quota limits and usage",
                        'properties': {
                            'limit': {
                                'type': ['string', 'null'],
                                'description': 'The usage limit, if applicable',
                            },
                            'usage': {
                                'type': ['string', 'null'],
                                'description': 'The total usage across all services',
                            },
                            'usageInDrive': {
                                'type': ['string', 'null'],
                                'description': 'The usage by all files in Google Drive',
                            },
                            'usageInDriveTrash': {
                                'type': ['string', 'null'],
                                'description': 'The usage by trashed files in Google Drive',
                            },
                        },
                    },
                    'importFormats': {
                        'type': ['object', 'null'],
                        'additionalProperties': {
                            'type': 'array',
                            'items': {'type': 'string'},
                        },
                        'description': 'A map of source MIME type to possible targets for all supported imports',
                    },
                    'exportFormats': {
                        'type': ['object', 'null'],
                        'additionalProperties': {
                            'type': 'array',
                            'items': {'type': 'string'},
                        },
                        'description': 'A map of source MIME type to possible targets for all supported exports',
                    },
                    'maxImportSizes': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'string'},
                        'description': 'A map of maximum import sizes by MIME type',
                    },
                    'maxUploadSize': {
                        'type': ['string', 'null'],
                        'description': 'The maximum upload size in bytes',
                    },
                    'appInstalled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user has installed the requesting app',
                    },
                    'folderColorPalette': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The currently supported folder colors as RGB hex strings',
                    },
                    'driveThemes': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                },
                                'backgroundImageLink': {
                                    'type': ['string', 'null'],
                                },
                                'colorRgb': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                        'description': 'A list of themes that are supported for shared drives',
                    },
                    'canCreateDrives': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user can create shared drives',
                    },
                    'canCreateTeamDrives': {
                        'type': ['boolean', 'null'],
                        'description': 'Deprecated - use canCreateDrives instead',
                    },
                    'teamDriveThemes': {
                        'type': ['array', 'null'],
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                },
                                'backgroundImageLink': {
                                    'type': ['string', 'null'],
                                },
                                'colorRgb': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                        'description': 'Deprecated - use driveThemes instead',
                    },
                },
                'x-airbyte-entity-name': 'about',
            },
        ),
    ],
)