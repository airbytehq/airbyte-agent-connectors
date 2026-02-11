"""
Connector model for gmail.

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

GmailConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('f7833dac-fc18-4feb-a2a9-94b22001edc6'),
    name='gmail',
    version='0.1.0',
    base_url='https://gmail.googleapis.com',
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
            required=['refresh_token'],
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
                'client_id': 'client_id',
                'client_secret': 'client_secret',
                'client_refresh_token': 'refresh_token',
            },
        ),
    ),
    entities=[
        EntityDefinition(
            name='profile',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/profile',
                    action=Action.GET,
                    description="Gets the current user's Gmail profile including email address and mailbox statistics",
                    response_schema={
                        'type': 'object',
                        'description': 'Gmail user profile information',
                        'properties': {
                            'emailAddress': {
                                'type': ['string', 'null'],
                                'description': "The user's email address",
                            },
                            'messagesTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of messages in the mailbox',
                            },
                            'threadsTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of threads in the mailbox',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': "The ID of the mailbox's current history record",
                            },
                        },
                        'x-airbyte-entity-name': 'profile',
                    },
                    record_extractor='$',
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Gmail user profile information',
                'properties': {
                    'emailAddress': {
                        'type': ['string', 'null'],
                        'description': "The user's email address",
                    },
                    'messagesTotal': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of messages in the mailbox',
                    },
                    'threadsTotal': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of threads in the mailbox',
                    },
                    'historyId': {
                        'type': ['string', 'null'],
                        'description': "The ID of the mailbox's current history record",
                    },
                },
                'x-airbyte-entity-name': 'profile',
            },
        ),
        EntityDefinition(
            name='messages',
            actions=[
                Action.LIST,
                Action.GET,
                Action.CREATE,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/messages',
                    action=Action.LIST,
                    description="Lists the messages in the user's mailbox. Returns message IDs and thread IDs.",
                    query_params=[
                        'maxResults',
                        'pageToken',
                        'q',
                        'labelIds',
                        'includeSpamTrash',
                    ],
                    query_params_schema={
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'q': {'type': 'string', 'required': False},
                        'labelIds': {'type': 'string', 'required': False},
                        'includeSpamTrash': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from listing messages',
                        'properties': {
                            'messages': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A lightweight reference to a message (used in list responses)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                                        'threadId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the thread the message belongs to',
                                        },
                                    },
                                },
                                'description': 'List of message references',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'Token to retrieve the next page of results',
                            },
                            'resultSizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated total number of results',
                            },
                        },
                    },
                    record_extractor='$.messages',
                    meta_extractor={'nextPageToken': '$.nextPageToken', 'resultSizeEstimate': '$.resultSizeEstimate'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/messages/{messageId}',
                    action=Action.GET,
                    description='Gets the full email message content including headers, body, and attachments metadata',
                    query_params=['format', 'metadataHeaders'],
                    query_params_schema={
                        'format': {
                            'type': 'string',
                            'required': False,
                            'default': 'full',
                        },
                        'metadataHeaders': {'type': 'string', 'required': False},
                    },
                    path_params=['messageId'],
                    path_params_schema={
                        'messageId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail email message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                            'threadId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the thread the message belongs to',
                            },
                            'labelIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of label IDs applied to this message',
                            },
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this message',
                            },
                            'internalDate': {
                                'type': ['string', 'null'],
                                'description': 'The internal message creation timestamp (epoch ms)',
                            },
                            'sizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated size in bytes of the message',
                            },
                            'raw': {
                                'type': ['string', 'null'],
                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                            },
                            'payload': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A single MIME message part',
                                        'properties': {
                                            'partId': {
                                                'type': ['string', 'null'],
                                                'description': 'The immutable ID of the message part',
                                            },
                                            'mimeType': {
                                                'type': ['string', 'null'],
                                                'description': 'The MIME type of the message part',
                                            },
                                            'filename': {
                                                'type': ['string', 'null'],
                                                'description': 'The filename of the attachment (if present)',
                                            },
                                            'headers': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A single email header key-value pair',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                        },
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The value of the header',
                                                        },
                                                    },
                                                },
                                                'description': 'List of headers on this message part',
                                            },
                                            'body': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'The body data of a MIME message part',
                                                        'properties': {
                                                            'attachmentId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                            },
                                                            'size': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'Number of bytes for the message part data',
                                                            },
                                                            'data': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The body data of the message part (base64url encoded)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The message part body',
                                            },
                                            'parts': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'object'},
                                                'description': 'Child MIME message parts (for multipart messages)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The parsed email structure in the payload',
                            },
                        },
                        'x-airbyte-entity-name': 'messages',
                    },
                    record_extractor='$',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/messages/send',
                    action=Action.CREATE,
                    description="Sends a new email message. The message should be provided as a base64url-encoded\nRFC 2822 formatted string in the 'raw' field.\n",
                    body_fields=['raw', 'threadId'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for sending a message',
                        'properties': {
                            'raw': {'type': 'string', 'description': 'The entire email message in RFC 2822 format, base64url encoded'},
                            'threadId': {'type': 'string', 'description': 'The thread ID to reply to (for threading replies in a conversation)'},
                        },
                        'required': ['raw'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail email message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                            'threadId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the thread the message belongs to',
                            },
                            'labelIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of label IDs applied to this message',
                            },
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this message',
                            },
                            'internalDate': {
                                'type': ['string', 'null'],
                                'description': 'The internal message creation timestamp (epoch ms)',
                            },
                            'sizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated size in bytes of the message',
                            },
                            'raw': {
                                'type': ['string', 'null'],
                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                            },
                            'payload': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A single MIME message part',
                                        'properties': {
                                            'partId': {
                                                'type': ['string', 'null'],
                                                'description': 'The immutable ID of the message part',
                                            },
                                            'mimeType': {
                                                'type': ['string', 'null'],
                                                'description': 'The MIME type of the message part',
                                            },
                                            'filename': {
                                                'type': ['string', 'null'],
                                                'description': 'The filename of the attachment (if present)',
                                            },
                                            'headers': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A single email header key-value pair',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                        },
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The value of the header',
                                                        },
                                                    },
                                                },
                                                'description': 'List of headers on this message part',
                                            },
                                            'body': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'The body data of a MIME message part',
                                                        'properties': {
                                                            'attachmentId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                            },
                                                            'size': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'Number of bytes for the message part data',
                                                            },
                                                            'data': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The body data of the message part (base64url encoded)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The message part body',
                                            },
                                            'parts': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'object'},
                                                'description': 'Child MIME message parts (for multipart messages)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The parsed email structure in the payload',
                            },
                        },
                        'x-airbyte-entity-name': 'messages',
                    },
                    record_extractor='$',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/messages/{messageId}/modify',
                    action=Action.UPDATE,
                    description='Modifies the labels on a message. Use this to archive (remove INBOX label),\nmark as read (remove UNREAD label), mark as unread (add UNREAD label),\nstar (add STARRED label), or apply custom labels.\n',
                    body_fields=['addLabelIds', 'removeLabelIds'],
                    path_params=['messageId'],
                    path_params_schema={
                        'messageId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for modifying message labels',
                        'properties': {
                            'addLabelIds': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'A list of label IDs to add to the message (e.g. STARRED, UNREAD, or custom label IDs)',
                            },
                            'removeLabelIds': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'A list of label IDs to remove from the message (e.g. INBOX to archive, UNREAD to mark as read)',
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail email message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                            'threadId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the thread the message belongs to',
                            },
                            'labelIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of label IDs applied to this message',
                            },
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this message',
                            },
                            'internalDate': {
                                'type': ['string', 'null'],
                                'description': 'The internal message creation timestamp (epoch ms)',
                            },
                            'sizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated size in bytes of the message',
                            },
                            'raw': {
                                'type': ['string', 'null'],
                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                            },
                            'payload': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A single MIME message part',
                                        'properties': {
                                            'partId': {
                                                'type': ['string', 'null'],
                                                'description': 'The immutable ID of the message part',
                                            },
                                            'mimeType': {
                                                'type': ['string', 'null'],
                                                'description': 'The MIME type of the message part',
                                            },
                                            'filename': {
                                                'type': ['string', 'null'],
                                                'description': 'The filename of the attachment (if present)',
                                            },
                                            'headers': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A single email header key-value pair',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                        },
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The value of the header',
                                                        },
                                                    },
                                                },
                                                'description': 'List of headers on this message part',
                                            },
                                            'body': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'The body data of a MIME message part',
                                                        'properties': {
                                                            'attachmentId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                            },
                                                            'size': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'Number of bytes for the message part data',
                                                            },
                                                            'data': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The body data of the message part (base64url encoded)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The message part body',
                                            },
                                            'parts': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'object'},
                                                'description': 'Child MIME message parts (for multipart messages)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The parsed email structure in the payload',
                            },
                        },
                        'x-airbyte-entity-name': 'messages',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Gmail email message',
                'properties': {
                    'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                    'threadId': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the thread the message belongs to',
                    },
                    'labelIds': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'List of label IDs applied to this message',
                    },
                    'snippet': {
                        'type': ['string', 'null'],
                        'description': 'A short part of the message text',
                    },
                    'historyId': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the last history record that modified this message',
                    },
                    'internalDate': {
                        'type': ['string', 'null'],
                        'description': 'The internal message creation timestamp (epoch ms)',
                    },
                    'sizeEstimate': {
                        'type': ['integer', 'null'],
                        'description': 'Estimated size in bytes of the message',
                    },
                    'raw': {
                        'type': ['string', 'null'],
                        'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                    },
                    'payload': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MessagePart'},
                            {'type': 'null'},
                        ],
                        'description': 'The parsed email structure in the payload',
                    },
                },
                'x-airbyte-entity-name': 'messages',
            },
        ),
        EntityDefinition(
            name='labels',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/labels',
                    action=Action.LIST,
                    description="Lists all labels in the user's mailbox including system and user-created labels",
                    response_schema={
                        'type': 'object',
                        'description': 'Response from listing labels',
                        'properties': {
                            'labels': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Gmail label used to organize messages and threads',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The immutable ID of the label'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The display name of the label',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The owner type for the label (system or user)',
                                        },
                                        'messageListVisibility': {
                                            'type': ['string', 'null'],
                                            'description': 'The visibility of messages with this label in the message list (show or hide)',
                                        },
                                        'labelListVisibility': {
                                            'type': ['string', 'null'],
                                            'description': 'The visibility of the label in the label list (labelShow, labelShowIfUnread, labelHide)',
                                        },
                                        'messagesTotal': {
                                            'type': ['integer', 'null'],
                                            'description': 'The total number of messages with the label',
                                        },
                                        'messagesUnread': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of unread messages with the label',
                                        },
                                        'threadsTotal': {
                                            'type': ['integer', 'null'],
                                            'description': 'The total number of threads with the label',
                                        },
                                        'threadsUnread': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of unread threads with the label',
                                        },
                                        'color': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'The color to assign to a label',
                                                    'properties': {
                                                        'textColor': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The text color of the label as a hex string (#RRGGBB)',
                                                        },
                                                        'backgroundColor': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The background color of the label as a hex string (#RRGGBB)',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The color assigned to the label',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'labels',
                                },
                                'description': 'List of labels',
                            },
                        },
                    },
                    record_extractor='$.labels',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/labels',
                    action=Action.CREATE,
                    description="Creates a new label in the user's mailbox",
                    body_fields=[
                        'name',
                        'messageListVisibility',
                        'labelListVisibility',
                        'color',
                    ],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating a label',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The display name of the label'},
                            'messageListVisibility': {
                                'type': 'string',
                                'description': 'The visibility of messages with this label in the message list (show or hide)',
                                'enum': ['show', 'hide'],
                            },
                            'labelListVisibility': {
                                'type': 'string',
                                'description': 'The visibility of the label in the label list',
                                'enum': ['labelShow', 'labelShowIfUnread', 'labelHide'],
                            },
                            'color': {
                                'type': 'object',
                                'description': 'The color to assign to the label',
                                'properties': {
                                    'textColor': {'type': 'string', 'description': 'The text color of the label as a hex string (#RRGGBB)'},
                                    'backgroundColor': {'type': 'string', 'description': 'The background color of the label as a hex string (#RRGGBB)'},
                                },
                            },
                        },
                        'required': ['name'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail label used to organize messages and threads',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the label'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The display name of the label',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The owner type for the label (system or user)',
                            },
                            'messageListVisibility': {
                                'type': ['string', 'null'],
                                'description': 'The visibility of messages with this label in the message list (show or hide)',
                            },
                            'labelListVisibility': {
                                'type': ['string', 'null'],
                                'description': 'The visibility of the label in the label list (labelShow, labelShowIfUnread, labelHide)',
                            },
                            'messagesTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of messages with the label',
                            },
                            'messagesUnread': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unread messages with the label',
                            },
                            'threadsTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of threads with the label',
                            },
                            'threadsUnread': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unread threads with the label',
                            },
                            'color': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'The color to assign to a label',
                                        'properties': {
                                            'textColor': {
                                                'type': ['string', 'null'],
                                                'description': 'The text color of the label as a hex string (#RRGGBB)',
                                            },
                                            'backgroundColor': {
                                                'type': ['string', 'null'],
                                                'description': 'The background color of the label as a hex string (#RRGGBB)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The color assigned to the label',
                            },
                        },
                        'x-airbyte-entity-name': 'labels',
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/labels/{labelId}',
                    action=Action.GET,
                    description='Gets a specific label by ID including message and thread counts',
                    path_params=['labelId'],
                    path_params_schema={
                        'labelId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail label used to organize messages and threads',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the label'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The display name of the label',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The owner type for the label (system or user)',
                            },
                            'messageListVisibility': {
                                'type': ['string', 'null'],
                                'description': 'The visibility of messages with this label in the message list (show or hide)',
                            },
                            'labelListVisibility': {
                                'type': ['string', 'null'],
                                'description': 'The visibility of the label in the label list (labelShow, labelShowIfUnread, labelHide)',
                            },
                            'messagesTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of messages with the label',
                            },
                            'messagesUnread': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unread messages with the label',
                            },
                            'threadsTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of threads with the label',
                            },
                            'threadsUnread': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unread threads with the label',
                            },
                            'color': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'The color to assign to a label',
                                        'properties': {
                                            'textColor': {
                                                'type': ['string', 'null'],
                                                'description': 'The text color of the label as a hex string (#RRGGBB)',
                                            },
                                            'backgroundColor': {
                                                'type': ['string', 'null'],
                                                'description': 'The background color of the label as a hex string (#RRGGBB)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The color assigned to the label',
                            },
                        },
                        'x-airbyte-entity-name': 'labels',
                    },
                    record_extractor='$',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/gmail/v1/users/me/labels/{labelId}',
                    action=Action.UPDATE,
                    description='Updates the specified label',
                    body_fields=[
                        'id',
                        'name',
                        'messageListVisibility',
                        'labelListVisibility',
                        'color',
                    ],
                    path_params=['labelId'],
                    path_params_schema={
                        'labelId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for updating a label',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The ID of the label (must match the path parameter)'},
                            'name': {'type': 'string', 'description': 'The new display name of the label'},
                            'messageListVisibility': {
                                'type': 'string',
                                'description': 'The visibility of messages with this label in the message list',
                                'enum': ['show', 'hide'],
                            },
                            'labelListVisibility': {
                                'type': 'string',
                                'description': 'The visibility of the label in the label list',
                                'enum': ['labelShow', 'labelShowIfUnread', 'labelHide'],
                            },
                            'color': {
                                'type': 'object',
                                'description': 'The color to assign to the label',
                                'properties': {
                                    'textColor': {'type': 'string', 'description': 'The text color of the label as a hex string (#RRGGBB)'},
                                    'backgroundColor': {'type': 'string', 'description': 'The background color of the label as a hex string (#RRGGBB)'},
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail label used to organize messages and threads',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the label'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The display name of the label',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The owner type for the label (system or user)',
                            },
                            'messageListVisibility': {
                                'type': ['string', 'null'],
                                'description': 'The visibility of messages with this label in the message list (show or hide)',
                            },
                            'labelListVisibility': {
                                'type': ['string', 'null'],
                                'description': 'The visibility of the label in the label list (labelShow, labelShowIfUnread, labelHide)',
                            },
                            'messagesTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of messages with the label',
                            },
                            'messagesUnread': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unread messages with the label',
                            },
                            'threadsTotal': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of threads with the label',
                            },
                            'threadsUnread': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unread threads with the label',
                            },
                            'color': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'The color to assign to a label',
                                        'properties': {
                                            'textColor': {
                                                'type': ['string', 'null'],
                                                'description': 'The text color of the label as a hex string (#RRGGBB)',
                                            },
                                            'backgroundColor': {
                                                'type': ['string', 'null'],
                                                'description': 'The background color of the label as a hex string (#RRGGBB)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The color assigned to the label',
                            },
                        },
                        'x-airbyte-entity-name': 'labels',
                    },
                    record_extractor='$',
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/gmail/v1/users/me/labels/{labelId}',
                    action=Action.DELETE,
                    description='Deletes the specified label and removes it from any messages and threads',
                    path_params=['labelId'],
                    path_params_schema={
                        'labelId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Gmail label used to organize messages and threads',
                'properties': {
                    'id': {'type': 'string', 'description': 'The immutable ID of the label'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The display name of the label',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The owner type for the label (system or user)',
                    },
                    'messageListVisibility': {
                        'type': ['string', 'null'],
                        'description': 'The visibility of messages with this label in the message list (show or hide)',
                    },
                    'labelListVisibility': {
                        'type': ['string', 'null'],
                        'description': 'The visibility of the label in the label list (labelShow, labelShowIfUnread, labelHide)',
                    },
                    'messagesTotal': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of messages with the label',
                    },
                    'messagesUnread': {
                        'type': ['integer', 'null'],
                        'description': 'The number of unread messages with the label',
                    },
                    'threadsTotal': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of threads with the label',
                    },
                    'threadsUnread': {
                        'type': ['integer', 'null'],
                        'description': 'The number of unread threads with the label',
                    },
                    'color': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LabelColor'},
                            {'type': 'null'},
                        ],
                        'description': 'The color assigned to the label',
                    },
                },
                'x-airbyte-entity-name': 'labels',
            },
        ),
        EntityDefinition(
            name='drafts',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
                Action.DELETE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/drafts',
                    action=Action.LIST,
                    description="Lists the drafts in the user's mailbox",
                    query_params=[
                        'maxResults',
                        'pageToken',
                        'q',
                        'includeSpamTrash',
                    ],
                    query_params_schema={
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'q': {'type': 'string', 'required': False},
                        'includeSpamTrash': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from listing drafts',
                        'properties': {
                            'drafts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A lightweight reference to a draft (used in list responses)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The immutable ID of the draft'},
                                        'message': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A lightweight reference to a message (used in list responses)',
                                                    'properties': {
                                                        'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                                                        'threadId': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the thread the message belongs to',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The message content of the draft (lightweight reference)',
                                        },
                                    },
                                },
                                'description': 'List of draft references',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'Token to retrieve the next page of results',
                            },
                            'resultSizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated total number of results',
                            },
                        },
                    },
                    record_extractor='$.drafts',
                    meta_extractor={'nextPageToken': '$.nextPageToken', 'resultSizeEstimate': '$.resultSizeEstimate'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/drafts',
                    action=Action.CREATE,
                    description='Creates a new draft with the specified message content',
                    body_fields=['message'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating or updating a draft',
                        'properties': {
                            'message': {
                                'type': 'object',
                                'description': 'The draft message content',
                                'required': ['raw'],
                                'properties': {
                                    'raw': {'type': 'string', 'description': 'The draft message in RFC 2822 format, base64url encoded'},
                                    'threadId': {'type': 'string', 'description': 'The thread ID for the draft (for threading in a conversation)'},
                                },
                            },
                        },
                        'required': ['message'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail draft message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the draft'},
                            'message': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A Gmail email message',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                                            'threadId': {
                                                'type': ['string', 'null'],
                                                'description': 'The ID of the thread the message belongs to',
                                            },
                                            'labelIds': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'string'},
                                                'description': 'List of label IDs applied to this message',
                                            },
                                            'snippet': {
                                                'type': ['string', 'null'],
                                                'description': 'A short part of the message text',
                                            },
                                            'historyId': {
                                                'type': ['string', 'null'],
                                                'description': 'The ID of the last history record that modified this message',
                                            },
                                            'internalDate': {
                                                'type': ['string', 'null'],
                                                'description': 'The internal message creation timestamp (epoch ms)',
                                            },
                                            'sizeEstimate': {
                                                'type': ['integer', 'null'],
                                                'description': 'Estimated size in bytes of the message',
                                            },
                                            'raw': {
                                                'type': ['string', 'null'],
                                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                                            },
                                            'payload': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'A single MIME message part',
                                                        'properties': {
                                                            'partId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the message part',
                                                            },
                                                            'mimeType': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The MIME type of the message part',
                                                            },
                                                            'filename': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The filename of the attachment (if present)',
                                                            },
                                                            'headers': {
                                                                'type': ['array', 'null'],
                                                                'items': {
                                                                    'type': 'object',
                                                                    'description': 'A single email header key-value pair',
                                                                    'properties': {
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                                        },
                                                                        'value': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The value of the header',
                                                                        },
                                                                    },
                                                                },
                                                                'description': 'List of headers on this message part',
                                                            },
                                                            'body': {
                                                                'oneOf': [
                                                                    {
                                                                        'type': 'object',
                                                                        'description': 'The body data of a MIME message part',
                                                                        'properties': {
                                                                            'attachmentId': {
                                                                                'type': ['string', 'null'],
                                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                                            },
                                                                            'size': {
                                                                                'type': ['integer', 'null'],
                                                                                'description': 'Number of bytes for the message part data',
                                                                            },
                                                                            'data': {
                                                                                'type': ['string', 'null'],
                                                                                'description': 'The body data of the message part (base64url encoded)',
                                                                            },
                                                                        },
                                                                    },
                                                                    {'type': 'null'},
                                                                ],
                                                                'description': 'The message part body',
                                                            },
                                                            'parts': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                                'description': 'Child MIME message parts (for multipart messages)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The parsed email structure in the payload',
                                            },
                                        },
                                        'x-airbyte-entity-name': 'messages',
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The message content of the draft',
                            },
                        },
                        'x-airbyte-entity-name': 'drafts',
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/drafts/{draftId}',
                    action=Action.GET,
                    description='Gets the specified draft including its message content',
                    query_params=['format'],
                    query_params_schema={
                        'format': {
                            'type': 'string',
                            'required': False,
                            'default': 'full',
                        },
                    },
                    path_params=['draftId'],
                    path_params_schema={
                        'draftId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail draft message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the draft'},
                            'message': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A Gmail email message',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                                            'threadId': {
                                                'type': ['string', 'null'],
                                                'description': 'The ID of the thread the message belongs to',
                                            },
                                            'labelIds': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'string'},
                                                'description': 'List of label IDs applied to this message',
                                            },
                                            'snippet': {
                                                'type': ['string', 'null'],
                                                'description': 'A short part of the message text',
                                            },
                                            'historyId': {
                                                'type': ['string', 'null'],
                                                'description': 'The ID of the last history record that modified this message',
                                            },
                                            'internalDate': {
                                                'type': ['string', 'null'],
                                                'description': 'The internal message creation timestamp (epoch ms)',
                                            },
                                            'sizeEstimate': {
                                                'type': ['integer', 'null'],
                                                'description': 'Estimated size in bytes of the message',
                                            },
                                            'raw': {
                                                'type': ['string', 'null'],
                                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                                            },
                                            'payload': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'A single MIME message part',
                                                        'properties': {
                                                            'partId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the message part',
                                                            },
                                                            'mimeType': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The MIME type of the message part',
                                                            },
                                                            'filename': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The filename of the attachment (if present)',
                                                            },
                                                            'headers': {
                                                                'type': ['array', 'null'],
                                                                'items': {
                                                                    'type': 'object',
                                                                    'description': 'A single email header key-value pair',
                                                                    'properties': {
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                                        },
                                                                        'value': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The value of the header',
                                                                        },
                                                                    },
                                                                },
                                                                'description': 'List of headers on this message part',
                                                            },
                                                            'body': {
                                                                'oneOf': [
                                                                    {
                                                                        'type': 'object',
                                                                        'description': 'The body data of a MIME message part',
                                                                        'properties': {
                                                                            'attachmentId': {
                                                                                'type': ['string', 'null'],
                                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                                            },
                                                                            'size': {
                                                                                'type': ['integer', 'null'],
                                                                                'description': 'Number of bytes for the message part data',
                                                                            },
                                                                            'data': {
                                                                                'type': ['string', 'null'],
                                                                                'description': 'The body data of the message part (base64url encoded)',
                                                                            },
                                                                        },
                                                                    },
                                                                    {'type': 'null'},
                                                                ],
                                                                'description': 'The message part body',
                                                            },
                                                            'parts': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                                'description': 'Child MIME message parts (for multipart messages)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The parsed email structure in the payload',
                                            },
                                        },
                                        'x-airbyte-entity-name': 'messages',
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The message content of the draft',
                            },
                        },
                        'x-airbyte-entity-name': 'drafts',
                    },
                    record_extractor='$',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/gmail/v1/users/me/drafts/{draftId}',
                    action=Action.UPDATE,
                    description="Replaces a draft's content with the specified message content",
                    body_fields=['message'],
                    path_params=['draftId'],
                    path_params_schema={
                        'draftId': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for creating or updating a draft',
                        'properties': {
                            'message': {
                                'type': 'object',
                                'description': 'The draft message content',
                                'required': ['raw'],
                                'properties': {
                                    'raw': {'type': 'string', 'description': 'The draft message in RFC 2822 format, base64url encoded'},
                                    'threadId': {'type': 'string', 'description': 'The thread ID for the draft (for threading in a conversation)'},
                                },
                            },
                        },
                        'required': ['message'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail draft message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the draft'},
                            'message': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A Gmail email message',
                                        'properties': {
                                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                                            'threadId': {
                                                'type': ['string', 'null'],
                                                'description': 'The ID of the thread the message belongs to',
                                            },
                                            'labelIds': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'string'},
                                                'description': 'List of label IDs applied to this message',
                                            },
                                            'snippet': {
                                                'type': ['string', 'null'],
                                                'description': 'A short part of the message text',
                                            },
                                            'historyId': {
                                                'type': ['string', 'null'],
                                                'description': 'The ID of the last history record that modified this message',
                                            },
                                            'internalDate': {
                                                'type': ['string', 'null'],
                                                'description': 'The internal message creation timestamp (epoch ms)',
                                            },
                                            'sizeEstimate': {
                                                'type': ['integer', 'null'],
                                                'description': 'Estimated size in bytes of the message',
                                            },
                                            'raw': {
                                                'type': ['string', 'null'],
                                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                                            },
                                            'payload': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'A single MIME message part',
                                                        'properties': {
                                                            'partId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the message part',
                                                            },
                                                            'mimeType': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The MIME type of the message part',
                                                            },
                                                            'filename': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The filename of the attachment (if present)',
                                                            },
                                                            'headers': {
                                                                'type': ['array', 'null'],
                                                                'items': {
                                                                    'type': 'object',
                                                                    'description': 'A single email header key-value pair',
                                                                    'properties': {
                                                                        'name': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                                        },
                                                                        'value': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The value of the header',
                                                                        },
                                                                    },
                                                                },
                                                                'description': 'List of headers on this message part',
                                                            },
                                                            'body': {
                                                                'oneOf': [
                                                                    {
                                                                        'type': 'object',
                                                                        'description': 'The body data of a MIME message part',
                                                                        'properties': {
                                                                            'attachmentId': {
                                                                                'type': ['string', 'null'],
                                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                                            },
                                                                            'size': {
                                                                                'type': ['integer', 'null'],
                                                                                'description': 'Number of bytes for the message part data',
                                                                            },
                                                                            'data': {
                                                                                'type': ['string', 'null'],
                                                                                'description': 'The body data of the message part (base64url encoded)',
                                                                            },
                                                                        },
                                                                    },
                                                                    {'type': 'null'},
                                                                ],
                                                                'description': 'The message part body',
                                                            },
                                                            'parts': {
                                                                'type': ['array', 'null'],
                                                                'items': {'type': 'object'},
                                                                'description': 'Child MIME message parts (for multipart messages)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The parsed email structure in the payload',
                                            },
                                        },
                                        'x-airbyte-entity-name': 'messages',
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The message content of the draft',
                            },
                        },
                        'x-airbyte-entity-name': 'drafts',
                    },
                    record_extractor='$',
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/gmail/v1/users/me/drafts/{draftId}',
                    action=Action.DELETE,
                    description='Immediately and permanently deletes the specified draft (does not move to trash)',
                    path_params=['draftId'],
                    path_params_schema={
                        'draftId': {'type': 'string', 'required': True},
                    },
                    no_content_response=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Gmail draft message',
                'properties': {
                    'id': {'type': 'string', 'description': 'The immutable ID of the draft'},
                    'message': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Message'},
                            {'type': 'null'},
                        ],
                        'description': 'The message content of the draft',
                    },
                },
                'x-airbyte-entity-name': 'drafts',
            },
        ),
        EntityDefinition(
            name='drafts_send',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/drafts/send',
                    action=Action.CREATE,
                    description='Sends the specified existing draft to its recipients',
                    body_fields=['id'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for sending an existing draft',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The ID of the draft to send'},
                        },
                        'required': ['id'],
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail email message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                            'threadId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the thread the message belongs to',
                            },
                            'labelIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of label IDs applied to this message',
                            },
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this message',
                            },
                            'internalDate': {
                                'type': ['string', 'null'],
                                'description': 'The internal message creation timestamp (epoch ms)',
                            },
                            'sizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated size in bytes of the message',
                            },
                            'raw': {
                                'type': ['string', 'null'],
                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                            },
                            'payload': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A single MIME message part',
                                        'properties': {
                                            'partId': {
                                                'type': ['string', 'null'],
                                                'description': 'The immutable ID of the message part',
                                            },
                                            'mimeType': {
                                                'type': ['string', 'null'],
                                                'description': 'The MIME type of the message part',
                                            },
                                            'filename': {
                                                'type': ['string', 'null'],
                                                'description': 'The filename of the attachment (if present)',
                                            },
                                            'headers': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A single email header key-value pair',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                        },
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The value of the header',
                                                        },
                                                    },
                                                },
                                                'description': 'List of headers on this message part',
                                            },
                                            'body': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'The body data of a MIME message part',
                                                        'properties': {
                                                            'attachmentId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                            },
                                                            'size': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'Number of bytes for the message part data',
                                                            },
                                                            'data': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The body data of the message part (base64url encoded)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The message part body',
                                            },
                                            'parts': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'object'},
                                                'description': 'Child MIME message parts (for multipart messages)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The parsed email structure in the payload',
                            },
                        },
                        'x-airbyte-entity-name': 'messages',
                    },
                    record_extractor='$',
                ),
            },
        ),
        EntityDefinition(
            name='threads',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/threads',
                    action=Action.LIST,
                    description="Lists the threads in the user's mailbox",
                    query_params=[
                        'maxResults',
                        'pageToken',
                        'q',
                        'labelIds',
                        'includeSpamTrash',
                    ],
                    query_params_schema={
                        'maxResults': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'pageToken': {'type': 'string', 'required': False},
                        'q': {'type': 'string', 'required': False},
                        'labelIds': {'type': 'string', 'required': False},
                        'includeSpamTrash': {
                            'type': 'boolean',
                            'required': False,
                            'default': False,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Response from listing threads',
                        'properties': {
                            'threads': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A lightweight reference to a thread (used in list responses)',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The immutable ID of the thread'},
                                        'snippet': {
                                            'type': ['string', 'null'],
                                            'description': 'A short part of the message text',
                                        },
                                        'historyId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the last history record that modified this thread',
                                        },
                                    },
                                },
                                'description': 'List of thread references',
                            },
                            'nextPageToken': {
                                'type': ['string', 'null'],
                                'description': 'Token to retrieve the next page of results',
                            },
                            'resultSizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated total number of results',
                            },
                        },
                    },
                    record_extractor='$.threads',
                    meta_extractor={'nextPageToken': '$.nextPageToken', 'resultSizeEstimate': '$.resultSizeEstimate'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/gmail/v1/users/me/threads/{threadId}',
                    action=Action.GET,
                    description='Gets the specified thread including all messages in the conversation',
                    query_params=['format', 'metadataHeaders'],
                    query_params_schema={
                        'format': {
                            'type': 'string',
                            'required': False,
                            'default': 'full',
                        },
                        'metadataHeaders': {'type': 'string', 'required': False},
                    },
                    path_params=['threadId'],
                    path_params_schema={
                        'threadId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail thread (email conversation)',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the thread'},
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this thread',
                            },
                            'messages': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'description': 'A Gmail email message',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                                        'threadId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the thread the message belongs to',
                                        },
                                        'labelIds': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'List of label IDs applied to this message',
                                        },
                                        'snippet': {
                                            'type': ['string', 'null'],
                                            'description': 'A short part of the message text',
                                        },
                                        'historyId': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the last history record that modified this message',
                                        },
                                        'internalDate': {
                                            'type': ['string', 'null'],
                                            'description': 'The internal message creation timestamp (epoch ms)',
                                        },
                                        'sizeEstimate': {
                                            'type': ['integer', 'null'],
                                            'description': 'Estimated size in bytes of the message',
                                        },
                                        'raw': {
                                            'type': ['string', 'null'],
                                            'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                                        },
                                        'payload': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'A single MIME message part',
                                                    'properties': {
                                                        'partId': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The immutable ID of the message part',
                                                        },
                                                        'mimeType': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The MIME type of the message part',
                                                        },
                                                        'filename': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The filename of the attachment (if present)',
                                                        },
                                                        'headers': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'A single email header key-value pair',
                                                                'properties': {
                                                                    'name': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                                    },
                                                                    'value': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The value of the header',
                                                                    },
                                                                },
                                                            },
                                                            'description': 'List of headers on this message part',
                                                        },
                                                        'body': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'description': 'The body data of a MIME message part',
                                                                    'properties': {
                                                                        'attachmentId': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                                        },
                                                                        'size': {
                                                                            'type': ['integer', 'null'],
                                                                            'description': 'Number of bytes for the message part data',
                                                                        },
                                                                        'data': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The body data of the message part (base64url encoded)',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                            'description': 'The message part body',
                                                        },
                                                        'parts': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'object'},
                                                            'description': 'Child MIME message parts (for multipart messages)',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'The parsed email structure in the payload',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'messages',
                                },
                                'description': 'The list of messages in the thread',
                            },
                        },
                        'x-airbyte-entity-name': 'threads',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Gmail thread (email conversation)',
                'properties': {
                    'id': {'type': 'string', 'description': 'The immutable ID of the thread'},
                    'snippet': {
                        'type': ['string', 'null'],
                        'description': 'A short part of the message text',
                    },
                    'historyId': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the last history record that modified this thread',
                    },
                    'messages': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/Message'},
                        'description': 'The list of messages in the thread',
                    },
                },
                'x-airbyte-entity-name': 'threads',
            },
        ),
        EntityDefinition(
            name='messages_trash',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/messages/{messageId}/trash',
                    action=Action.CREATE,
                    description='Moves the specified message to the trash',
                    path_params=['messageId'],
                    path_params_schema={
                        'messageId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail email message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                            'threadId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the thread the message belongs to',
                            },
                            'labelIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of label IDs applied to this message',
                            },
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this message',
                            },
                            'internalDate': {
                                'type': ['string', 'null'],
                                'description': 'The internal message creation timestamp (epoch ms)',
                            },
                            'sizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated size in bytes of the message',
                            },
                            'raw': {
                                'type': ['string', 'null'],
                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                            },
                            'payload': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A single MIME message part',
                                        'properties': {
                                            'partId': {
                                                'type': ['string', 'null'],
                                                'description': 'The immutable ID of the message part',
                                            },
                                            'mimeType': {
                                                'type': ['string', 'null'],
                                                'description': 'The MIME type of the message part',
                                            },
                                            'filename': {
                                                'type': ['string', 'null'],
                                                'description': 'The filename of the attachment (if present)',
                                            },
                                            'headers': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A single email header key-value pair',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                        },
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The value of the header',
                                                        },
                                                    },
                                                },
                                                'description': 'List of headers on this message part',
                                            },
                                            'body': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'The body data of a MIME message part',
                                                        'properties': {
                                                            'attachmentId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                            },
                                                            'size': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'Number of bytes for the message part data',
                                                            },
                                                            'data': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The body data of the message part (base64url encoded)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The message part body',
                                            },
                                            'parts': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'object'},
                                                'description': 'Child MIME message parts (for multipart messages)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The parsed email structure in the payload',
                            },
                        },
                        'x-airbyte-entity-name': 'messages',
                    },
                    record_extractor='$',
                ),
            },
        ),
        EntityDefinition(
            name='messages_untrash',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/messages/{messageId}/untrash',
                    action=Action.CREATE,
                    description='Removes the specified message from the trash',
                    path_params=['messageId'],
                    path_params_schema={
                        'messageId': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Gmail email message',
                        'properties': {
                            'id': {'type': 'string', 'description': 'The immutable ID of the message'},
                            'threadId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the thread the message belongs to',
                            },
                            'labelIds': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                                'description': 'List of label IDs applied to this message',
                            },
                            'snippet': {
                                'type': ['string', 'null'],
                                'description': 'A short part of the message text',
                            },
                            'historyId': {
                                'type': ['string', 'null'],
                                'description': 'The ID of the last history record that modified this message',
                            },
                            'internalDate': {
                                'type': ['string', 'null'],
                                'description': 'The internal message creation timestamp (epoch ms)',
                            },
                            'sizeEstimate': {
                                'type': ['integer', 'null'],
                                'description': 'Estimated size in bytes of the message',
                            },
                            'raw': {
                                'type': ['string', 'null'],
                                'description': 'The entire email message in RFC 2822 format (base64url encoded, only when format=raw)',
                            },
                            'payload': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'A single MIME message part',
                                        'properties': {
                                            'partId': {
                                                'type': ['string', 'null'],
                                                'description': 'The immutable ID of the message part',
                                            },
                                            'mimeType': {
                                                'type': ['string', 'null'],
                                                'description': 'The MIME type of the message part',
                                            },
                                            'filename': {
                                                'type': ['string', 'null'],
                                                'description': 'The filename of the attachment (if present)',
                                            },
                                            'headers': {
                                                'type': ['array', 'null'],
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A single email header key-value pair',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The name of the header (e.g. From, To, Subject, Date)',
                                                        },
                                                        'value': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The value of the header',
                                                        },
                                                    },
                                                },
                                                'description': 'List of headers on this message part',
                                            },
                                            'body': {
                                                'oneOf': [
                                                    {
                                                        'type': 'object',
                                                        'description': 'The body data of a MIME message part',
                                                        'properties': {
                                                            'attachmentId': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The immutable ID of the attachment (present when body is an attachment)',
                                                            },
                                                            'size': {
                                                                'type': ['integer', 'null'],
                                                                'description': 'Number of bytes for the message part data',
                                                            },
                                                            'data': {
                                                                'type': ['string', 'null'],
                                                                'description': 'The body data of the message part (base64url encoded)',
                                                            },
                                                        },
                                                    },
                                                    {'type': 'null'},
                                                ],
                                                'description': 'The message part body',
                                            },
                                            'parts': {
                                                'type': ['array', 'null'],
                                                'items': {'type': 'object'},
                                                'description': 'Child MIME message parts (for multipart messages)',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The parsed email structure in the payload',
                            },
                        },
                        'x-airbyte-entity-name': 'messages',
                    },
                    record_extractor='$',
                ),
            },
        ),
    ],
)