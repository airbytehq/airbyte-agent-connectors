"""
Connector model for granola.

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

GranolaConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('9023923c-002f-4131-9554-3ebdf56540a4'),
    name='granola',
    version='1.0.1',
    base_url='https://public-api.granola.ai',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Granola Enterprise API key generated from Settings > Workspaces > API tab',
                ),
            },
            auth_mapping={'token': '${api_key}'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='notes',
            stream_name='notes',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/notes',
                    action=Action.LIST,
                    description='Returns a paginated list of meeting notes',
                    query_params=[
                        'page_size',
                        'cursor',
                        'created_before',
                        'created_after',
                    ],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'cursor': {'type': 'string', 'required': False},
                        'created_before': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of notes',
                        'properties': {
                            'notes': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Granola meeting note',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique note identifier'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (note)',
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Title of the note',
                                        },
                                        'owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'The owner of the note',
                                                    'properties': {
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Name of the note owner',
                                                        },
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Email of the note owner',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Creation timestamp of the note',
                                        },
                                        'calendar_event': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Associated calendar event details',
                                                    'properties': {
                                                        'event_title': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Title of the calendar event',
                                                        },
                                                        'invitees': {
                                                            'type': ['array', 'null'],
                                                            'description': 'List of invitees',
                                                            'items': {
                                                                'type': 'object',
                                                                'description': 'A calendar event invitee',
                                                                'properties': {
                                                                    'email': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Email of the invitee',
                                                                    },
                                                                },
                                                            },
                                                        },
                                                        'organiser': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Email of the event organiser',
                                                        },
                                                        'calendar_event_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Calendar event identifier',
                                                        },
                                                        'scheduled_start_time': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'Scheduled start time of the event',
                                                        },
                                                        'scheduled_end_time': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                            'description': 'Scheduled end time of the event',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'attendees': {
                                            'type': ['array', 'null'],
                                            'description': 'List of meeting attendees',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A meeting attendee',
                                                'properties': {
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Name of the attendee',
                                                    },
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Email of the attendee',
                                                    },
                                                },
                                            },
                                        },
                                        'folder_membership': {
                                            'type': ['array', 'null'],
                                            'description': 'Folders this note belongs to',
                                            'items': {
                                                'type': 'object',
                                                'description': 'Folder the note belongs to',
                                                'properties': {
                                                    'id': {'type': 'string', 'description': 'Unique folder identifier'},
                                                    'object': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Object type (folder)',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Name of the folder',
                                                    },
                                                },
                                            },
                                        },
                                        'summary_text': {
                                            'type': ['string', 'null'],
                                            'description': 'Plain text summary of the note',
                                        },
                                        'summary_markdown': {
                                            'type': ['string', 'null'],
                                            'description': 'Markdown formatted summary of the note',
                                        },
                                        'transcript': {
                                            'type': ['array', 'null'],
                                            'description': 'Transcript of the meeting',
                                            'items': {
                                                'type': 'object',
                                                'description': 'A single transcript entry',
                                                'properties': {
                                                    'speaker': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'description': 'Speaker information in transcript',
                                                                'properties': {
                                                                    'source': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'Source of the speaker (microphone or speaker)',
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'text': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Transcript text content',
                                                    },
                                                    'start_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'Start time of the transcript segment',
                                                    },
                                                    'end_time': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'End time of the transcript segment',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'notes',
                                    'x-airbyte-stream-name': 'notes',
                                },
                            },
                            'hasMore': {'type': 'boolean', 'description': 'Whether there are more notes to fetch'},
                            'cursor': {
                                'type': ['string', 'null'],
                                'description': 'Cursor for fetching the next page',
                            },
                        },
                    },
                    record_extractor='$.notes',
                    meta_extractor={'cursor': '$.cursor', 'has_more': '$.hasMore'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/notes/{note_id}',
                    action=Action.GET,
                    description='Get a single note by ID, including full details and optionally the transcript',
                    query_params=['include'],
                    query_params_schema={
                        'include': {'type': 'string', 'required': False},
                    },
                    path_params=['note_id'],
                    path_params_schema={
                        'note_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Granola meeting note',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique note identifier'},
                            'object': {
                                'type': ['string', 'null'],
                                'description': 'Object type (note)',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'Title of the note',
                            },
                            'owner': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'The owner of the note',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                                'description': 'Name of the note owner',
                                            },
                                            'email': {
                                                'type': ['string', 'null'],
                                                'description': 'Email of the note owner',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Creation timestamp of the note',
                            },
                            'calendar_event': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Associated calendar event details',
                                        'properties': {
                                            'event_title': {
                                                'type': ['string', 'null'],
                                                'description': 'Title of the calendar event',
                                            },
                                            'invitees': {
                                                'type': ['array', 'null'],
                                                'description': 'List of invitees',
                                                'items': {
                                                    'type': 'object',
                                                    'description': 'A calendar event invitee',
                                                    'properties': {
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Email of the invitee',
                                                        },
                                                    },
                                                },
                                            },
                                            'organiser': {
                                                'type': ['string', 'null'],
                                                'description': 'Email of the event organiser',
                                            },
                                            'calendar_event_id': {
                                                'type': ['string', 'null'],
                                                'description': 'Calendar event identifier',
                                            },
                                            'scheduled_start_time': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Scheduled start time of the event',
                                            },
                                            'scheduled_end_time': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                                'description': 'Scheduled end time of the event',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'attendees': {
                                'type': ['array', 'null'],
                                'description': 'List of meeting attendees',
                                'items': {
                                    'type': 'object',
                                    'description': 'A meeting attendee',
                                    'properties': {
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Name of the attendee',
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'Email of the attendee',
                                        },
                                    },
                                },
                            },
                            'folder_membership': {
                                'type': ['array', 'null'],
                                'description': 'Folders this note belongs to',
                                'items': {
                                    'type': 'object',
                                    'description': 'Folder the note belongs to',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique folder identifier'},
                                        'object': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type (folder)',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Name of the folder',
                                        },
                                    },
                                },
                            },
                            'summary_text': {
                                'type': ['string', 'null'],
                                'description': 'Plain text summary of the note',
                            },
                            'summary_markdown': {
                                'type': ['string', 'null'],
                                'description': 'Markdown formatted summary of the note',
                            },
                            'transcript': {
                                'type': ['array', 'null'],
                                'description': 'Transcript of the meeting',
                                'items': {
                                    'type': 'object',
                                    'description': 'A single transcript entry',
                                    'properties': {
                                        'speaker': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Speaker information in transcript',
                                                    'properties': {
                                                        'source': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Source of the speaker (microphone or speaker)',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'text': {
                                            'type': ['string', 'null'],
                                            'description': 'Transcript text content',
                                        },
                                        'start_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Start time of the transcript segment',
                                        },
                                        'end_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'End time of the transcript segment',
                                        },
                                    },
                                },
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'notes',
                        'x-airbyte-stream-name': 'notes',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Granola meeting note',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique note identifier'},
                    'object': {
                        'type': ['string', 'null'],
                        'description': 'Object type (note)',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Title of the note',
                    },
                    'owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Creation timestamp of the note',
                    },
                    'calendar_event': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CalendarEvent'},
                            {'type': 'null'},
                        ],
                    },
                    'attendees': {
                        'type': ['array', 'null'],
                        'description': 'List of meeting attendees',
                        'items': {'$ref': '#/components/schemas/Attendee'},
                    },
                    'folder_membership': {
                        'type': ['array', 'null'],
                        'description': 'Folders this note belongs to',
                        'items': {'$ref': '#/components/schemas/FolderMembership'},
                    },
                    'summary_text': {
                        'type': ['string', 'null'],
                        'description': 'Plain text summary of the note',
                    },
                    'summary_markdown': {
                        'type': ['string', 'null'],
                        'description': 'Markdown formatted summary of the note',
                    },
                    'transcript': {
                        'type': ['array', 'null'],
                        'description': 'Transcript of the meeting',
                        'items': {'$ref': '#/components/schemas/TranscriptEntry'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'notes',
                'x-airbyte-stream-name': 'notes',
            },
        ),
    ],
    search_field_paths={
        'notes': [
            'created_at',
            'id',
            'object',
            'owner',
            'owner.name',
            'owner.email',
            'title',
        ],
    },
)