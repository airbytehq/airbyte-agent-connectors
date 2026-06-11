"""
Connector model for granola.

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

GranolaConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('9023923c-002f-4131-9554-3ebdf56540a4'),
    name='granola',
    version='1.0.7',
    base_url='https://public-api.granola.ai',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Granola API key. For a personal key, open the Granola desktop app and go to Settings > Connectors > API keys > Create new key. For an Enterprise API key, go to Settings > API > Create new key. On Enterprise plans, workspace admins must enable "Allow personal API keys" in Settings > Workspace > General before personal keys can be created.',
                ),
            },
            auth_mapping={'token': '${api_key}'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='notes',
            stream_name='detailed_notes',
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
                            'minimum': 1,
                            'maximum': 30,
                        },
                        'cursor': {'type': 'string', 'required': False},
                        'created_before': {
                            'type': 'string',
                            'required': False,
                            'format': 'date',
                        },
                        'created_after': {
                            'type': 'string',
                            'required': False,
                            'format': 'date',
                        },
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
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'Last updated timestamp of the note',
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
                                    'x-airbyte-stream-name': 'detailed_notes',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Meeting notes, transcripts, and action items from Granola',
                                        'when_to_use': 'Questions about what was discussed on a call, meeting decisions, or action items',
                                        'trigger_phrases': [
                                            'what was discussed',
                                            'meeting with',
                                            'call with',
                                            'action items from',
                                            'notes from',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What was discussed in the Scale Lite meeting?', 'Show me notes that mention budget reviews', 'What meetings happened this quarter?'],
                                        'search_strategy': 'Search across both title and summary_text for best results (use OR filter)',
                                    },
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
                        'include': {
                            'type': 'string',
                            'required': False,
                            'enum': ['transcript'],
                        },
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
                            'updated_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last updated timestamp of the note',
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
                        'x-airbyte-stream-name': 'detailed_notes',
                        'x-airbyte-ai-hints': {
                            'summary': 'Meeting notes, transcripts, and action items from Granola',
                            'when_to_use': 'Questions about what was discussed on a call, meeting decisions, or action items',
                            'trigger_phrases': [
                                'what was discussed',
                                'meeting with',
                                'call with',
                                'action items from',
                                'notes from',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What was discussed in the Scale Lite meeting?', 'Show me notes that mention budget reviews', 'What meetings happened this quarter?'],
                            'search_strategy': 'Search across both title and summary_text for best results (use OR filter)',
                        },
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
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last updated timestamp of the note',
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
                'x-airbyte-stream-name': 'detailed_notes',
                'x-airbyte-ai-hints': {
                    'summary': 'Meeting notes, transcripts, and action items from Granola',
                    'when_to_use': 'Questions about what was discussed on a call, meeting decisions, or action items',
                    'trigger_phrases': [
                        'what was discussed',
                        'meeting with',
                        'call with',
                        'action items from',
                        'notes from',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What was discussed in the Scale Lite meeting?', 'Show me notes that mention budget reviews', 'What meetings happened this quarter?'],
                    'search_strategy': 'Search across both title and summary_text for best results (use OR filter)',
                },
            },
            ai_hints={
                'summary': 'Meeting notes, transcripts, and action items from Granola',
                'when_to_use': 'Questions about what was discussed on a call, meeting decisions, or action items',
                'trigger_phrases': [
                    'what was discussed',
                    'meeting with',
                    'call with',
                    'action items from',
                    'notes from',
                ],
                'freshness': 'live',
                'example_questions': ['What was discussed in the Scale Lite meeting?', 'Show me notes that mention budget reviews', 'What meetings happened this quarter?'],
                'search_strategy': 'Search across both title and summary_text for best results (use OR filter)',
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='notes',
                suggested=True,
                x_airbyte_name='detailed_notes',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='The unique identifier of the note.',
                    ),
                    CacheFieldConfig(
                        name='object',
                        type=['null', 'string'],
                        description='The object type, always "note".',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='The title of the note.',
                    ),
                    CacheFieldConfig(
                        name='owner',
                        type=['null', 'object'],
                        description='The owner of the note.',
                        properties={
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'email': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='The creation time of the note in ISO 8601 format.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='The last update time of the note in ISO 8601 format.',
                    ),
                    CacheFieldConfig(
                        name='summary_text',
                        type=['null', 'string'],
                        description='Plain text summary of the note.',
                    ),
                    CacheFieldConfig(
                        name='summary_markdown',
                        type=['null', 'string'],
                        description='Markdown formatted summary of the note.',
                    ),
                    CacheFieldConfig(
                        name='attendees',
                        type=['null', 'array'],
                        description='The attendees of the meeting.',
                        properties={
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'email': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='calendar_event',
                        type=['null', 'object'],
                        description='Associated calendar event details.',
                        properties={
                            'calendar_event_id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'event_title': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'organiser': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'invitees': CacheFieldProperty(
                                type=['null', 'array'],
                                properties={
                                    'email': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'scheduled_start_time': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'scheduled_end_time': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='folder_membership',
                        type=['null', 'array'],
                        description='The folder membership of the note.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'object': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='transcript',
                        type=['null', 'array'],
                        description='Transcript of the meeting.',
                        properties={
                            'text': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'speaker': CacheFieldProperty(
                                type=['null', 'object'],
                                properties={
                                    'source': CacheFieldProperty(
                                        type=['null', 'string'],
                                    ),
                                },
                            ),
                            'start_time': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                            'end_time': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'notes': [
            'id',
            'object',
            'title',
            'owner',
            'owner.name',
            'owner.email',
            'created_at',
            'updated_at',
            'summary_text',
            'summary_markdown',
            'attendees',
            'attendees[]',
            'attendees[].name',
            'attendees[].email',
            'calendar_event',
            'calendar_event.calendar_event_id',
            'calendar_event.event_title',
            'calendar_event.organiser',
            'calendar_event.invitees',
            'calendar_event.invitees[]',
            'calendar_event.invitees[].email',
            'calendar_event.scheduled_start_time',
            'calendar_event.scheduled_end_time',
            'folder_membership',
            'folder_membership[]',
            'folder_membership[].id',
            'folder_membership[].object',
            'folder_membership[].name',
            'transcript',
            'transcript[]',
            'transcript[].text',
            'transcript[].speaker',
            'transcript[].speaker.source',
            'transcript[].start_time',
            'transcript[].end_time',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all meeting notes from Granola',
            'Show me recent meeting notes',
            'Get the details of a specific note',
            'List notes created in the last week',
        ],
        context_store_search=[
            'Find meeting notes from last month',
            'Which meetings had the most attendees?',
            'Show me notes that mention budget reviews',
            'What meetings happened this quarter?',
        ],
        search=[
            'Find meeting notes from last month',
            'Which meetings had the most attendees?',
            'Show me notes that mention budget reviews',
            'What meetings happened this quarter?',
        ],
        unsupported=[
            'Create a new meeting note',
            'Delete a meeting note',
            'Update an existing note',
            'Share a note with someone',
        ],
    ),
)