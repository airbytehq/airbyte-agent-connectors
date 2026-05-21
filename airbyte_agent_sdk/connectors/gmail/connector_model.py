"""
Connector model for gmail.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from airbyte_agent_sdk.types import (
    Action,
    AuthConfig,
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
    CacheFieldProperty,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

GmailConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('f7833dac-fc18-4feb-a2a9-94b22001edc6'),
    name='gmail',
    version='0.1.4',
    base_url='https://gmail.googleapis.com',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://oauth2.googleapis.com/token',
        },
        user_config_spec=AuthConfigSpec(
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
                'credentials.client_id': 'client_id',
                'credentials.client_secret': 'client_secret',
                'credentials.client_refresh_token': 'refresh_token',
            },
            replication_auth_key_constants={'credentials.auth_type': 'Client'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='profile',
            stream_name='profile',
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
                        'x-airbyte-stream-name': 'profile',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail user profile with email address and account info',
                            'when_to_use': 'Questions about the current email account',
                            'trigger_phrases': ['gmail profile', 'my email', 'email address'],
                            'freshness': 'live',
                            'example_questions': ['What is my Gmail address?'],
                            'search_strategy': 'Retrieve the authenticated user profile',
                        },
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
                'x-airbyte-stream-name': 'profile',
                'x-airbyte-ai-hints': {
                    'summary': 'Gmail user profile with email address and account info',
                    'when_to_use': 'Questions about the current email account',
                    'trigger_phrases': ['gmail profile', 'my email', 'email address'],
                    'freshness': 'live',
                    'example_questions': ['What is my Gmail address?'],
                    'search_strategy': 'Retrieve the authenticated user profile',
                },
            },
            ai_hints={
                'summary': 'Gmail user profile with email address and account info',
                'when_to_use': 'Questions about the current email account',
                'trigger_phrases': ['gmail profile', 'my email', 'email address'],
                'freshness': 'live',
                'example_questions': ['What is my Gmail address?'],
                'search_strategy': 'Retrieve the authenticated user profile',
            },
        ),
        EntityDefinition(
            name='messages',
            stream_name='messages_details',
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
                            'minimum': 1,
                            'maximum': 500,
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
                            'enum': [
                                'full',
                                'metadata',
                                'minimal',
                                'raw',
                            ],
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
                        'x-airbyte-stream-name': 'messages_details',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                            'trigger_phrases': [
                                'search email',
                                'find email',
                                'show emails',
                                'recent emails',
                                'latest emails',
                                'show latest emails',
                                'show inbox',
                                'email',
                                'gmail message',
                                'inbox',
                                'who emailed',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                        },
                    },
                    record_extractor='$',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/gmail/v1/users/me/messages/send',
                    action=Action.CREATE,
                    description="Sends a new email message. The message should be provided as a base64url-encoded\nRFC 2822 formatted string in the 'raw' field. Build the complete MIME message\nfirst, including headers such as To and Subject plus a blank line before the\nbody, then base64url-encode that message before calling this operation.\n",
                    body_fields=['raw', 'threadId'],
                    request_schema={
                        'type': 'object',
                        'description': 'Parameters for sending a message. The raw value must be a base64url-encoded\nRFC 2822/MIME email, not plain body text.\n',
                        'properties': {
                            'raw': {
                                'type': 'string',
                                'description': 'Base64url-encoded RFC 2822/MIME email; construct headers plus a blank line plus body, then URL-safe-base64 encode the UTF-8 bytes before sending.',
                                'x-airbyte-ai-hints': {'encoding': 'Do not send plain text here; send the base64url encoding of the complete RFC 2822/MIME message.'},
                            },
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
                        'x-airbyte-stream-name': 'messages_details',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                            'trigger_phrases': [
                                'search email',
                                'find email',
                                'show emails',
                                'recent emails',
                                'latest emails',
                                'show latest emails',
                                'show inbox',
                                'email',
                                'gmail message',
                                'inbox',
                                'who emailed',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                        },
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
                        'x-airbyte-stream-name': 'messages_details',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                            'trigger_phrases': [
                                'search email',
                                'find email',
                                'show emails',
                                'recent emails',
                                'latest emails',
                                'show latest emails',
                                'show inbox',
                                'email',
                                'gmail message',
                                'inbox',
                                'who emailed',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                        },
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
                'x-airbyte-stream-name': 'messages_details',
                'x-airbyte-ai-hints': {
                    'summary': 'Gmail email messages with subject, sender, body, and attachments',
                    'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                    'trigger_phrases': [
                        'search email',
                        'find email',
                        'show emails',
                        'recent emails',
                        'latest emails',
                        'show latest emails',
                        'show inbox',
                        'email',
                        'gmail message',
                        'inbox',
                        'who emailed',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                    'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                },
            },
            ai_hints={
                'summary': 'Gmail email messages with subject, sender, body, and attachments',
                'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                'trigger_phrases': [
                    'search email',
                    'find email',
                    'show emails',
                    'recent emails',
                    'latest emails',
                    'show latest emails',
                    'show inbox',
                    'email',
                    'gmail message',
                    'inbox',
                    'who emailed',
                ],
                'freshness': 'live',
                'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
            },
        ),
        EntityDefinition(
            name='labels',
            stream_name='labels',
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
                                    'x-airbyte-stream-name': 'labels',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Gmail labels for organizing and categorizing emails',
                                        'when_to_use': 'Questions about email labels or folder organization',
                                        'trigger_phrases': ['gmail label', 'email folder', 'inbox label'],
                                        'freshness': 'live',
                                        'example_questions': ['What labels are in my Gmail?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                                'description': 'List of labels',
                            },
                        },
                    },
                    record_extractor='$.labels',
                    no_pagination='The Gmail API /users/{userId}/labels endpoint returns the full list of labels available to the authenticated user in a single response; it does not expose pageToken/pagination parameters.',
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
                        'x-airbyte-stream-name': 'labels',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail labels for organizing and categorizing emails',
                            'when_to_use': 'Questions about email labels or folder organization',
                            'trigger_phrases': ['gmail label', 'email folder', 'inbox label'],
                            'freshness': 'live',
                            'example_questions': ['What labels are in my Gmail?'],
                            'search_strategy': 'Search by name',
                        },
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
                        'x-airbyte-stream-name': 'labels',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail labels for organizing and categorizing emails',
                            'when_to_use': 'Questions about email labels or folder organization',
                            'trigger_phrases': ['gmail label', 'email folder', 'inbox label'],
                            'freshness': 'live',
                            'example_questions': ['What labels are in my Gmail?'],
                            'search_strategy': 'Search by name',
                        },
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
                        'x-airbyte-stream-name': 'labels',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail labels for organizing and categorizing emails',
                            'when_to_use': 'Questions about email labels or folder organization',
                            'trigger_phrases': ['gmail label', 'email folder', 'inbox label'],
                            'freshness': 'live',
                            'example_questions': ['What labels are in my Gmail?'],
                            'search_strategy': 'Search by name',
                        },
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
                'x-airbyte-stream-name': 'labels',
                'x-airbyte-ai-hints': {
                    'summary': 'Gmail labels for organizing and categorizing emails',
                    'when_to_use': 'Questions about email labels or folder organization',
                    'trigger_phrases': ['gmail label', 'email folder', 'inbox label'],
                    'freshness': 'live',
                    'example_questions': ['What labels are in my Gmail?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Gmail labels for organizing and categorizing emails',
                'when_to_use': 'Questions about email labels or folder organization',
                'trigger_phrases': ['gmail label', 'email folder', 'inbox label'],
                'freshness': 'live',
                'example_questions': ['What labels are in my Gmail?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='drafts',
            stream_name='drafts',
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
                            'minimum': 1,
                            'maximum': 500,
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
                        'description': 'Parameters for creating or updating a draft. The nested message.raw value must\nbe a base64url-encoded RFC 2822/MIME email, not plain body text.\n',
                        'properties': {
                            'message': {
                                'type': 'object',
                                'description': 'The draft message content encoded in Gmail raw message format',
                                'required': ['raw'],
                                'properties': {
                                    'raw': {
                                        'type': 'string',
                                        'description': 'Base64url-encoded RFC 2822/MIME email; construct headers plus a blank line plus body, then URL-safe-base64 encode the UTF-8 bytes before creating or updating the draft.',
                                        'x-airbyte-ai-hints': {'encoding': 'Do not send plain text here; send the base64url encoding of the complete RFC 2822/MIME message.'},
                                    },
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
                                        'x-airbyte-stream-name': 'messages_details',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                                            'trigger_phrases': [
                                                'search email',
                                                'find email',
                                                'show emails',
                                                'recent emails',
                                                'latest emails',
                                                'show latest emails',
                                                'show inbox',
                                                'email',
                                                'gmail message',
                                                'inbox',
                                                'who emailed',
                                            ],
                                            'freshness': 'live',
                                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The message content of the draft',
                            },
                        },
                        'x-airbyte-entity-name': 'drafts',
                        'x-airbyte-stream-name': 'drafts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Email drafts saved in Gmail',
                            'when_to_use': 'Looking for unsent email drafts',
                            'trigger_phrases': ['email draft', 'unsent email', 'draft message'],
                            'freshness': 'live',
                            'example_questions': ['Show my email drafts'],
                            'search_strategy': 'Search by subject or recipient',
                        },
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
                            'enum': [
                                'full',
                                'metadata',
                                'minimal',
                                'raw',
                            ],
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
                                        'x-airbyte-stream-name': 'messages_details',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                                            'trigger_phrases': [
                                                'search email',
                                                'find email',
                                                'show emails',
                                                'recent emails',
                                                'latest emails',
                                                'show latest emails',
                                                'show inbox',
                                                'email',
                                                'gmail message',
                                                'inbox',
                                                'who emailed',
                                            ],
                                            'freshness': 'live',
                                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The message content of the draft',
                            },
                        },
                        'x-airbyte-entity-name': 'drafts',
                        'x-airbyte-stream-name': 'drafts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Email drafts saved in Gmail',
                            'when_to_use': 'Looking for unsent email drafts',
                            'trigger_phrases': ['email draft', 'unsent email', 'draft message'],
                            'freshness': 'live',
                            'example_questions': ['Show my email drafts'],
                            'search_strategy': 'Search by subject or recipient',
                        },
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
                        'description': 'Parameters for creating or updating a draft. The nested message.raw value must\nbe a base64url-encoded RFC 2822/MIME email, not plain body text.\n',
                        'properties': {
                            'message': {
                                'type': 'object',
                                'description': 'The draft message content encoded in Gmail raw message format',
                                'required': ['raw'],
                                'properties': {
                                    'raw': {
                                        'type': 'string',
                                        'description': 'Base64url-encoded RFC 2822/MIME email; construct headers plus a blank line plus body, then URL-safe-base64 encode the UTF-8 bytes before creating or updating the draft.',
                                        'x-airbyte-ai-hints': {'encoding': 'Do not send plain text here; send the base64url encoding of the complete RFC 2822/MIME message.'},
                                    },
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
                                        'x-airbyte-stream-name': 'messages_details',
                                        'x-airbyte-ai-hints': {
                                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                                            'trigger_phrases': [
                                                'search email',
                                                'find email',
                                                'show emails',
                                                'recent emails',
                                                'latest emails',
                                                'show latest emails',
                                                'show inbox',
                                                'email',
                                                'gmail message',
                                                'inbox',
                                                'who emailed',
                                            ],
                                            'freshness': 'live',
                                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'The message content of the draft',
                            },
                        },
                        'x-airbyte-entity-name': 'drafts',
                        'x-airbyte-stream-name': 'drafts',
                        'x-airbyte-ai-hints': {
                            'summary': 'Email drafts saved in Gmail',
                            'when_to_use': 'Looking for unsent email drafts',
                            'trigger_phrases': ['email draft', 'unsent email', 'draft message'],
                            'freshness': 'live',
                            'example_questions': ['Show my email drafts'],
                            'search_strategy': 'Search by subject or recipient',
                        },
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
                'x-airbyte-stream-name': 'drafts',
                'x-airbyte-ai-hints': {
                    'summary': 'Email drafts saved in Gmail',
                    'when_to_use': 'Looking for unsent email drafts',
                    'trigger_phrases': ['email draft', 'unsent email', 'draft message'],
                    'freshness': 'live',
                    'example_questions': ['Show my email drafts'],
                    'search_strategy': 'Search by subject or recipient',
                },
            },
            ai_hints={
                'summary': 'Email drafts saved in Gmail',
                'when_to_use': 'Looking for unsent email drafts',
                'trigger_phrases': ['email draft', 'unsent email', 'draft message'],
                'freshness': 'live',
                'example_questions': ['Show my email drafts'],
                'search_strategy': 'Search by subject or recipient',
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
                        'x-airbyte-stream-name': 'messages_details',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                            'trigger_phrases': [
                                'search email',
                                'find email',
                                'show emails',
                                'recent emails',
                                'latest emails',
                                'show latest emails',
                                'show inbox',
                                'email',
                                'gmail message',
                                'inbox',
                                'who emailed',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                        },
                    },
                    record_extractor='$',
                ),
            },
        ),
        EntityDefinition(
            name='threads',
            stream_name='threads',
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
                            'minimum': 1,
                            'maximum': 500,
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
                            'enum': ['full', 'metadata', 'minimal'],
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
                                    'x-airbyte-stream-name': 'messages_details',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Gmail email messages with subject, sender, body, and attachments',
                                        'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                                        'trigger_phrases': [
                                            'search email',
                                            'find email',
                                            'show emails',
                                            'recent emails',
                                            'latest emails',
                                            'show latest emails',
                                            'show inbox',
                                            'email',
                                            'gmail message',
                                            'inbox',
                                            'who emailed',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                                        'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                                    },
                                },
                                'description': 'The list of messages in the thread',
                            },
                        },
                        'x-airbyte-entity-name': 'threads',
                        'x-airbyte-stream-name': 'threads',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail conversation threads grouping related messages',
                            'when_to_use': 'Looking at email conversations, thread history, or related message chains',
                            'trigger_phrases': [
                                'email thread',
                                'conversation',
                                'email chain',
                                'show conversation',
                                'find thread',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Show the email thread about a topic', 'Find conversations with a person', 'Show the conversation with finance about invoices'],
                            'search_strategy': 'Use `threads.context_store_search` first for conversation lookups. Search by subject, participant, or snippet.',
                        },
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
                'x-airbyte-stream-name': 'threads',
                'x-airbyte-ai-hints': {
                    'summary': 'Gmail conversation threads grouping related messages',
                    'when_to_use': 'Looking at email conversations, thread history, or related message chains',
                    'trigger_phrases': [
                        'email thread',
                        'conversation',
                        'email chain',
                        'show conversation',
                        'find thread',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show the email thread about a topic', 'Find conversations with a person', 'Show the conversation with finance about invoices'],
                    'search_strategy': 'Use `threads.context_store_search` first for conversation lookups. Search by subject, participant, or snippet.',
                },
            },
            ai_hints={
                'summary': 'Gmail conversation threads grouping related messages',
                'when_to_use': 'Looking at email conversations, thread history, or related message chains',
                'trigger_phrases': [
                    'email thread',
                    'conversation',
                    'email chain',
                    'show conversation',
                    'find thread',
                ],
                'freshness': 'live',
                'example_questions': ['Show the email thread about a topic', 'Find conversations with a person', 'Show the conversation with finance about invoices'],
                'search_strategy': 'Use `threads.context_store_search` first for conversation lookups. Search by subject, participant, or snippet.',
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
                        'x-airbyte-stream-name': 'messages_details',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                            'trigger_phrases': [
                                'search email',
                                'find email',
                                'show emails',
                                'recent emails',
                                'latest emails',
                                'show latest emails',
                                'show inbox',
                                'email',
                                'gmail message',
                                'inbox',
                                'who emailed',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                        },
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
                        'x-airbyte-stream-name': 'messages_details',
                        'x-airbyte-ai-hints': {
                            'summary': 'Gmail email messages with subject, sender, body, and attachments',
                            'when_to_use': 'Looking for emails, searching inbox, finding recent messages, or showing specific emails',
                            'trigger_phrases': [
                                'search email',
                                'find email',
                                'show emails',
                                'recent emails',
                                'latest emails',
                                'show latest emails',
                                'show inbox',
                                'email',
                                'gmail message',
                                'inbox',
                                'who emailed',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Find emails from a specific sender', 'Show unread messages', 'What are my latest emails about billing?'],
                            'search_strategy': 'Use `messages.context_store_search` first for normal read/search questions. For latest or recent emails, sort by `internalDate` descending. Read From, To, Subject, and Date from `payload.headers`. Use snippet for previews and message body fields when needed.',
                        },
                    },
                    record_extractor='$',
                ),
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='profile',
                x_airbyte_name='profile',
                fields=[
                    CacheFieldConfig(
                        name='emailAddress',
                        type=['string', 'null'],
                        description='Email address of the authenticated Gmail account',
                    ),
                    CacheFieldConfig(
                        name='historyId',
                        type=['string', 'null'],
                        description='Mailbox history record identifier used for incremental sync',
                    ),
                    CacheFieldConfig(
                        name='messagesTotal',
                        type=['number', 'null'],
                        description='Total number of messages currently in the mailbox',
                    ),
                    CacheFieldConfig(
                        name='threadsTotal',
                        type=['number', 'null'],
                        description='Total number of threads currently in the mailbox',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='messages',
                suggested=True,
                x_airbyte_name='messages_details',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the message',
                    ),
                    CacheFieldConfig(
                        name='threadId',
                        type=['string', 'null'],
                        description='Identifier of the thread this message belongs to',
                    ),
                    CacheFieldConfig(
                        name='labelIds',
                        type=['array', 'null'],
                        description='Labels applied to the message',
                    ),
                    CacheFieldConfig(
                        name='snippet',
                        type=['string', 'null'],
                        description='Short snippet of the message text',
                    ),
                    CacheFieldConfig(
                        name='historyId',
                        type=['string', 'null'],
                        description='Mailbox history record identifier for the message',
                    ),
                    CacheFieldConfig(
                        name='internalDate',
                        type=['string', 'null'],
                        description='Internal message creation timestamp in epoch milliseconds',
                    ),
                    CacheFieldConfig(
                        name='sizeEstimate',
                        type=['integer', 'null'],
                        description='Estimated size of the message in bytes',
                    ),
                    CacheFieldConfig(
                        name='payload',
                        type=['object', 'null'],
                        description='Parsed MIME payload including headers, body, nested MIME parts, and attachment metadata. Use payload.headers for sender, recipients, subject, date, and other email headers.',
                        properties={
                            'partId': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'mimeType': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'filename': CacheFieldProperty(
                                type=['string', 'null'],
                            ),
                            'headers': CacheFieldProperty(
                                type=['array', 'null'],
                                properties={
                                    'name': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                    'value': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                },
                            ),
                            'body': CacheFieldProperty(
                                type=['object', 'null'],
                                properties={
                                    'attachmentId': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                    'size': CacheFieldProperty(
                                        type=['integer', 'null'],
                                    ),
                                    'data': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                },
                            ),
                            'parts': CacheFieldProperty(
                                type=['array', 'null'],
                                properties={
                                    'partId': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                    'mimeType': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                    'filename': CacheFieldProperty(
                                        type=['string', 'null'],
                                    ),
                                    'headers': CacheFieldProperty(
                                        type=['array', 'null'],
                                        properties={
                                            'name': CacheFieldProperty(
                                                type=['string', 'null'],
                                            ),
                                            'value': CacheFieldProperty(
                                                type=['string', 'null'],
                                            ),
                                        },
                                    ),
                                    'body': CacheFieldProperty(
                                        type=['object', 'null'],
                                        properties={
                                            'attachmentId': CacheFieldProperty(
                                                type=['string', 'null'],
                                            ),
                                            'size': CacheFieldProperty(
                                                type=['integer', 'null'],
                                            ),
                                            'data': CacheFieldProperty(
                                                type=['string', 'null'],
                                            ),
                                        },
                                    ),
                                },
                            ),
                        },
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='labels',
                x_airbyte_name='labels',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the label',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['string', 'null'],
                        description='Display name of the label',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['string', 'null'],
                        description='Label type: `system` or `user`',
                    ),
                    CacheFieldConfig(
                        name='labelListVisibility',
                        type=['string', 'null'],
                        description='Visibility of the label in the label list',
                    ),
                    CacheFieldConfig(
                        name='messageListVisibility',
                        type=['string', 'null'],
                        description='Visibility of the label when viewing a message list',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='drafts',
                x_airbyte_name='drafts',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the draft',
                    ),
                    CacheFieldConfig(
                        name='message',
                        type=['object', 'null'],
                        description='Draft message payload (headers, body, and metadata)',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='threads',
                suggested=True,
                x_airbyte_name='threads',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the thread',
                    ),
                    CacheFieldConfig(
                        name='historyId',
                        type=['string', 'null'],
                        description='Mailbox history record identifier for the thread',
                    ),
                    CacheFieldConfig(
                        name='snippet',
                        type=['string', 'null'],
                        description="Short snippet of the thread's most recent message",
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'profile': [
            'emailAddress',
            'historyId',
            'messagesTotal',
            'threadsTotal',
        ],
        'messages': [
            'id',
            'threadId',
            'labelIds',
            'labelIds[]',
            'snippet',
            'historyId',
            'internalDate',
            'sizeEstimate',
            'payload',
            'payload.partId',
            'payload.mimeType',
            'payload.filename',
            'payload.headers',
            'payload.headers[]',
            'payload.headers[].name',
            'payload.headers[].value',
            'payload.body',
            'payload.body.attachmentId',
            'payload.body.size',
            'payload.body.data',
            'payload.parts',
            'payload.parts[]',
            'payload.parts[].partId',
            'payload.parts[].mimeType',
            'payload.parts[].filename',
            'payload.parts[].headers',
            'payload.parts[].headers[]',
            'payload.parts[].headers[].name',
            'payload.parts[].headers[].value',
            'payload.parts[].body',
            'payload.parts[].body.attachmentId',
            'payload.parts[].body.size',
            'payload.parts[].body.data',
        ],
        'labels': [
            'id',
            'name',
            'type',
            'labelListVisibility',
            'messageListVisibility',
        ],
        'drafts': ['id', 'message'],
        'threads': ['id', 'historyId', 'snippet'],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List my recent emails',
            'Show me unread messages in my inbox',
            'Get the details of a specific email',
            'List all my Gmail labels',
            'Show me details for a specific label',
            'List my email drafts',
            'Get the content of a specific draft',
            'List my email threads',
            'Show me the full thread for a conversation',
            'Get my Gmail profile information',
            'Send an email to someone',
            'Create a new email draft',
            'Archive a message by removing the INBOX label',
            'Mark a message as read',
            'Mark a message as unread',
            'Move a message to trash',
            'Create a new label',
            'Update a label name or settings',
            'Delete a label',
        ],
        context_store_search=[
            'Search for messages matching a query',
            'Find emails from a specific sender',
            'Show me emails with attachments',
            'Show me my latest emails',
            'Find recent unread emails about {topic}',
            'Show the conversation with {person} about {topic}',
        ],
        search=[
            'Search for messages matching a query',
            'Find emails from a specific sender',
            'Show me emails with attachments',
            'Show me my latest emails',
            'Find recent unread emails about {topic}',
            'Show the conversation with {person} about {topic}',
        ],
        unsupported=[
            'Attach a file to an email',
            'Forward an email to someone',
            'Create a filter or rule',
            'Manage Gmail settings',
            'Access Google Calendar events',
            'Manage contacts',
        ],
    ),
)