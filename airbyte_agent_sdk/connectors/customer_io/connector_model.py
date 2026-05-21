"""
Connector model for customer-io.

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
    EntityRelationshipConfig,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

CustomerIoConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('34f697bc-b989-4eda-b06f-d0f39b88825b'),
    name='customer-io',
    base_url='https://api.customer.io',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
            title='App API Key Authentication',
            type='object',
            required=['app_api_key'],
            properties={
                'app_api_key': AuthConfigFieldSpec(
                    title='App API Key',
                    description='Your Customer.io App API key. Generate one in your workspace settings at Settings > API Credentials > App API Key.\n',
                ),
            },
            auth_mapping={'token': '${app_api_key}'},
            replication_auth_key_mapping={'app_api_key': 'app_api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/campaigns',
                    action=Action.LIST,
                    description='Returns a list of all campaigns in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'campaigns': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique campaign identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign name',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign trigger type (e.g., segment, event, date, api)',
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign status (draft, active, stopped)',
                                        },
                                        'active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the campaign is active',
                                        },
                                        'created': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'first_started': {
                                            'type': ['null', 'integer'],
                                            'description': 'When the campaign was first started (Unix)',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier (format id:timestamp)',
                                        },
                                        'tags': {
                                            'type': ['null', 'array'],
                                            'description': 'Tags associated with the campaign',
                                            'items': {'type': 'string'},
                                        },
                                        'actions': {
                                            'type': ['null', 'array'],
                                            'description': 'Actions defined in this campaign',
                                            'items': {'type': 'object'},
                                        },
                                        'msg_templates': {
                                            'type': ['null', 'array'],
                                            'description': 'Message templates used in the campaign',
                                            'items': {'type': 'object'},
                                        },
                                        'trigger_segment_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Segment IDs that trigger this campaign',
                                            'items': {'type': 'integer'},
                                        },
                                        'filter_segment_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Segment IDs used for filtering',
                                            'items': {'type': 'integer'},
                                        },
                                        'frequency': {
                                            'type': ['null', 'string'],
                                            'description': 'How frequently a person can receive this campaign',
                                        },
                                        'event_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Event name that triggers the campaign',
                                        },
                                        'date_attribute': {
                                            'type': ['null', 'string'],
                                            'description': 'Date attribute used for date-triggered campaigns',
                                        },
                                        'start_hour': {
                                            'type': ['null', 'integer'],
                                            'description': 'Hour of the day to trigger (24h format)',
                                        },
                                        'start_minutes': {
                                            'type': ['null', 'integer'],
                                            'description': 'Minute of the hour to trigger',
                                        },
                                        'timezone': {
                                            'type': ['null', 'string'],
                                            'description': 'Timezone for trigger scheduling',
                                        },
                                        'use_customer_timezone': {
                                            'type': ['null', 'boolean'],
                                            'description': "Whether to use the customer's timezone",
                                        },
                                        'created_by': {
                                            'type': ['null', 'string'],
                                            'description': 'Who created the campaign',
                                        },
                                        'scheduled_start': {
                                            'type': ['null', 'integer'],
                                            'description': 'Scheduled start time (Unix)',
                                        },
                                        'scheduled_start_should_backfill': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to backfill on scheduled start',
                                        },
                                        'scheduled_stop': {
                                            'type': ['null', 'integer'],
                                            'description': 'Scheduled stop time (Unix)',
                                        },
                                        'scheduled_stop_should_sunset': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to sunset on scheduled stop',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Marketing campaigns including event-triggered, segment-triggered, and date-triggered workflows',
                                        'when_to_use': 'Questions about campaign configuration, state, triggers, or campaign listing',
                                        'trigger_phrases': [
                                            'list campaigns',
                                            'campaign status',
                                            'active campaigns',
                                            'marketing automation',
                                            'campaign details',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What campaigns are currently active?', "Show me all campaigns tagged 'onboarding'", 'Get the details of campaign 42'],
                                        'search_strategy': 'Search by campaign name; filter by state (active/draft/stopped) or type',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.campaigns',
                    no_pagination='Returns all campaigns in a single response without pagination',
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/campaigns/{campaign_id}',
                    action=Action.GET,
                    description='Returns a single campaign by ID.',
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'campaign': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique campaign identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign name',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign trigger type (e.g., segment, event, date, api)',
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                        'description': 'Campaign status (draft, active, stopped)',
                                    },
                                    'active': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the campaign is active',
                                    },
                                    'created': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'first_started': {
                                        'type': ['null', 'integer'],
                                        'description': 'When the campaign was first started (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier (format id:timestamp)',
                                    },
                                    'tags': {
                                        'type': ['null', 'array'],
                                        'description': 'Tags associated with the campaign',
                                        'items': {'type': 'string'},
                                    },
                                    'actions': {
                                        'type': ['null', 'array'],
                                        'description': 'Actions defined in this campaign',
                                        'items': {'type': 'object'},
                                    },
                                    'msg_templates': {
                                        'type': ['null', 'array'],
                                        'description': 'Message templates used in the campaign',
                                        'items': {'type': 'object'},
                                    },
                                    'trigger_segment_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Segment IDs that trigger this campaign',
                                        'items': {'type': 'integer'},
                                    },
                                    'filter_segment_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Segment IDs used for filtering',
                                        'items': {'type': 'integer'},
                                    },
                                    'frequency': {
                                        'type': ['null', 'string'],
                                        'description': 'How frequently a person can receive this campaign',
                                    },
                                    'event_name': {
                                        'type': ['null', 'string'],
                                        'description': 'Event name that triggers the campaign',
                                    },
                                    'date_attribute': {
                                        'type': ['null', 'string'],
                                        'description': 'Date attribute used for date-triggered campaigns',
                                    },
                                    'start_hour': {
                                        'type': ['null', 'integer'],
                                        'description': 'Hour of the day to trigger (24h format)',
                                    },
                                    'start_minutes': {
                                        'type': ['null', 'integer'],
                                        'description': 'Minute of the hour to trigger',
                                    },
                                    'timezone': {
                                        'type': ['null', 'string'],
                                        'description': 'Timezone for trigger scheduling',
                                    },
                                    'use_customer_timezone': {
                                        'type': ['null', 'boolean'],
                                        'description': "Whether to use the customer's timezone",
                                    },
                                    'created_by': {
                                        'type': ['null', 'string'],
                                        'description': 'Who created the campaign',
                                    },
                                    'scheduled_start': {
                                        'type': ['null', 'integer'],
                                        'description': 'Scheduled start time (Unix)',
                                    },
                                    'scheduled_start_should_backfill': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to backfill on scheduled start',
                                    },
                                    'scheduled_stop': {
                                        'type': ['null', 'integer'],
                                        'description': 'Scheduled stop time (Unix)',
                                    },
                                    'scheduled_stop_should_sunset': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to sunset on scheduled stop',
                                    },
                                },
                                'x-airbyte-entity-name': 'campaigns',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Marketing campaigns including event-triggered, segment-triggered, and date-triggered workflows',
                                    'when_to_use': 'Questions about campaign configuration, state, triggers, or campaign listing',
                                    'trigger_phrases': [
                                        'list campaigns',
                                        'campaign status',
                                        'active campaigns',
                                        'marketing automation',
                                        'campaign details',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What campaigns are currently active?', "Show me all campaigns tagged 'onboarding'", 'Get the details of campaign 42'],
                                    'search_strategy': 'Search by campaign name; filter by state (active/draft/stopped) or type',
                                },
                            },
                        },
                    },
                    record_extractor='$.campaign',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique campaign identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Campaign name',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign trigger type (e.g., segment, event, date, api)',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'Campaign status (draft, active, stopped)',
                    },
                    'active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the campaign is active',
                    },
                    'created': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'first_started': {
                        'type': ['null', 'integer'],
                        'description': 'When the campaign was first started (Unix)',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier (format id:timestamp)',
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'Tags associated with the campaign',
                        'items': {'type': 'string'},
                    },
                    'actions': {
                        'type': ['null', 'array'],
                        'description': 'Actions defined in this campaign',
                        'items': {'type': 'object'},
                    },
                    'msg_templates': {
                        'type': ['null', 'array'],
                        'description': 'Message templates used in the campaign',
                        'items': {'type': 'object'},
                    },
                    'trigger_segment_ids': {
                        'type': ['null', 'array'],
                        'description': 'Segment IDs that trigger this campaign',
                        'items': {'type': 'integer'},
                    },
                    'filter_segment_ids': {
                        'type': ['null', 'array'],
                        'description': 'Segment IDs used for filtering',
                        'items': {'type': 'integer'},
                    },
                    'frequency': {
                        'type': ['null', 'string'],
                        'description': 'How frequently a person can receive this campaign',
                    },
                    'event_name': {
                        'type': ['null', 'string'],
                        'description': 'Event name that triggers the campaign',
                    },
                    'date_attribute': {
                        'type': ['null', 'string'],
                        'description': 'Date attribute used for date-triggered campaigns',
                    },
                    'start_hour': {
                        'type': ['null', 'integer'],
                        'description': 'Hour of the day to trigger (24h format)',
                    },
                    'start_minutes': {
                        'type': ['null', 'integer'],
                        'description': 'Minute of the hour to trigger',
                    },
                    'timezone': {
                        'type': ['null', 'string'],
                        'description': 'Timezone for trigger scheduling',
                    },
                    'use_customer_timezone': {
                        'type': ['null', 'boolean'],
                        'description': "Whether to use the customer's timezone",
                    },
                    'created_by': {
                        'type': ['null', 'string'],
                        'description': 'Who created the campaign',
                    },
                    'scheduled_start': {
                        'type': ['null', 'integer'],
                        'description': 'Scheduled start time (Unix)',
                    },
                    'scheduled_start_should_backfill': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to backfill on scheduled start',
                    },
                    'scheduled_stop': {
                        'type': ['null', 'integer'],
                        'description': 'Scheduled stop time (Unix)',
                    },
                    'scheduled_stop_should_sunset': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to sunset on scheduled stop',
                    },
                },
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-ai-hints': {
                    'summary': 'Marketing campaigns including event-triggered, segment-triggered, and date-triggered workflows',
                    'when_to_use': 'Questions about campaign configuration, state, triggers, or campaign listing',
                    'trigger_phrases': [
                        'list campaigns',
                        'campaign status',
                        'active campaigns',
                        'marketing automation',
                        'campaign details',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What campaigns are currently active?', "Show me all campaigns tagged 'onboarding'", 'Get the details of campaign 42'],
                    'search_strategy': 'Search by campaign name; filter by state (active/draft/stopped) or type',
                },
            },
            ai_hints={
                'summary': 'Marketing campaigns including event-triggered, segment-triggered, and date-triggered workflows',
                'when_to_use': 'Questions about campaign configuration, state, triggers, or campaign listing',
                'trigger_phrases': [
                    'list campaigns',
                    'campaign status',
                    'active campaigns',
                    'marketing automation',
                    'campaign details',
                ],
                'freshness': 'live',
                'example_questions': ['What campaigns are currently active?', "Show me all campaigns tagged 'onboarding'", 'Get the details of campaign 42'],
                'search_strategy': 'Search by campaign name; filter by state (active/draft/stopped) or type',
            },
        ),
        EntityDefinition(
            name='campaign_actions',
            stream_name='campaigns_actions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/campaigns/{campaign_id}/actions',
                    action=Action.LIST,
                    description='Returns a paginated list of actions for a campaign.',
                    query_params=['start'],
                    query_params_schema={
                        'start': {'type': 'string', 'required': False},
                    },
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'actions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer', 'string'],
                                            'description': 'Unique action identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Action name',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Action type (email, webhook, twilio, push, slack, in_app, whatsapp)',
                                        },
                                        'campaign_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent campaign ID',
                                        },
                                        'created': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier',
                                        },
                                        'body': {
                                            'type': ['null', 'string'],
                                            'description': 'Action body content (HTML for emails)',
                                        },
                                        'layout': {
                                            'type': ['null', 'string'],
                                            'description': 'Layout template used',
                                        },
                                        'from': {
                                            'type': ['null', 'string'],
                                            'description': 'From address',
                                        },
                                        'from_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Sender identity ID',
                                        },
                                        'subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Email subject line',
                                        },
                                        'preheader_text': {
                                            'type': ['null', 'string'],
                                            'description': 'Email preheader/preview text',
                                        },
                                        'recipient': {
                                            'type': ['null', 'string'],
                                            'description': 'Recipient address',
                                        },
                                        'reply_to': {
                                            'type': ['null', 'string'],
                                            'description': 'Reply-to address',
                                        },
                                        'reply_to_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Reply-to sender identity ID',
                                        },
                                        'bcc': {
                                            'type': ['null', 'string'],
                                            'description': 'BCC addresses',
                                        },
                                        'fake_bcc': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to use fake BCC',
                                        },
                                        'headers': {
                                            'type': ['null', 'string'],
                                            'description': 'Custom email headers as JSON',
                                        },
                                        'sending_state': {
                                            'type': ['null', 'string'],
                                            'description': 'Sending behavior (automatic or draft)',
                                        },
                                        'language': {
                                            'type': ['null', 'string'],
                                            'description': 'Language variant',
                                        },
                                        'parent_action_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent action ID for language variants',
                                        },
                                        'preprocessor': {
                                            'type': ['null', 'string'],
                                            'description': 'CSS preprocessor setting',
                                        },
                                        'body_amp': {
                                            'type': ['null', 'string'],
                                            'description': 'AMP HTML body content',
                                        },
                                        'broadcast_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent broadcast ID',
                                        },
                                        'editor': {
                                            'type': ['null', 'string'],
                                            'description': 'Editor used to create the action',
                                        },
                                        'url': {
                                            'type': ['null', 'string'],
                                            'description': 'Webhook URL (for webhook actions)',
                                        },
                                        'body_plain': {
                                            'type': ['null', 'string'],
                                            'description': 'Plain text version of the action body',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaign_actions',
                                    'x-airbyte-stream-name': 'campaigns_actions',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Individual actions (emails, webhooks, push notifications) within a campaign workflow',
                                        'when_to_use': 'Questions about specific campaign steps, email content, or action configuration',
                                        'trigger_phrases': [
                                            'campaign actions',
                                            'email content',
                                            'campaign steps',
                                            'action details',
                                            'workflow actions',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What actions are in campaign 42?', 'Show me all email actions for a campaign', 'Get the subject line of action 5 in campaign 10'],
                                        'search_strategy': 'Filter by campaign_id and action type',
                                    },
                                },
                            },
                            'next': {'type': 'string', 'description': 'Cursor for the next page'},
                        },
                    },
                    record_extractor='$.actions',
                    meta_extractor={'next': '$.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/campaigns/{campaign_id}/actions/{action_id}',
                    action=Action.GET,
                    description='Returns a single campaign action by ID.',
                    path_params=['campaign_id', 'action_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'integer', 'required': True},
                        'action_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'action': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer', 'string'],
                                        'description': 'Unique action identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Action name',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Action type (email, webhook, twilio, push, slack, in_app, whatsapp)',
                                    },
                                    'campaign_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent campaign ID',
                                    },
                                    'created': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'body': {
                                        'type': ['null', 'string'],
                                        'description': 'Action body content (HTML for emails)',
                                    },
                                    'layout': {
                                        'type': ['null', 'string'],
                                        'description': 'Layout template used',
                                    },
                                    'from': {
                                        'type': ['null', 'string'],
                                        'description': 'From address',
                                    },
                                    'from_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Sender identity ID',
                                    },
                                    'subject': {
                                        'type': ['null', 'string'],
                                        'description': 'Email subject line',
                                    },
                                    'preheader_text': {
                                        'type': ['null', 'string'],
                                        'description': 'Email preheader/preview text',
                                    },
                                    'recipient': {
                                        'type': ['null', 'string'],
                                        'description': 'Recipient address',
                                    },
                                    'reply_to': {
                                        'type': ['null', 'string'],
                                        'description': 'Reply-to address',
                                    },
                                    'reply_to_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Reply-to sender identity ID',
                                    },
                                    'bcc': {
                                        'type': ['null', 'string'],
                                        'description': 'BCC addresses',
                                    },
                                    'fake_bcc': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to use fake BCC',
                                    },
                                    'headers': {
                                        'type': ['null', 'string'],
                                        'description': 'Custom email headers as JSON',
                                    },
                                    'sending_state': {
                                        'type': ['null', 'string'],
                                        'description': 'Sending behavior (automatic or draft)',
                                    },
                                    'language': {
                                        'type': ['null', 'string'],
                                        'description': 'Language variant',
                                    },
                                    'parent_action_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent action ID for language variants',
                                    },
                                    'preprocessor': {
                                        'type': ['null', 'string'],
                                        'description': 'CSS preprocessor setting',
                                    },
                                    'body_amp': {
                                        'type': ['null', 'string'],
                                        'description': 'AMP HTML body content',
                                    },
                                    'broadcast_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent broadcast ID',
                                    },
                                    'editor': {
                                        'type': ['null', 'string'],
                                        'description': 'Editor used to create the action',
                                    },
                                    'url': {
                                        'type': ['null', 'string'],
                                        'description': 'Webhook URL (for webhook actions)',
                                    },
                                    'body_plain': {
                                        'type': ['null', 'string'],
                                        'description': 'Plain text version of the action body',
                                    },
                                },
                                'x-airbyte-entity-name': 'campaign_actions',
                                'x-airbyte-stream-name': 'campaigns_actions',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Individual actions (emails, webhooks, push notifications) within a campaign workflow',
                                    'when_to_use': 'Questions about specific campaign steps, email content, or action configuration',
                                    'trigger_phrases': [
                                        'campaign actions',
                                        'email content',
                                        'campaign steps',
                                        'action details',
                                        'workflow actions',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What actions are in campaign 42?', 'Show me all email actions for a campaign', 'Get the subject line of action 5 in campaign 10'],
                                    'search_strategy': 'Filter by campaign_id and action type',
                                },
                            },
                        },
                    },
                    record_extractor='$.action',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer', 'string'],
                        'description': 'Unique action identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Action name',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Action type (email, webhook, twilio, push, slack, in_app, whatsapp)',
                    },
                    'campaign_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent campaign ID',
                    },
                    'created': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier',
                    },
                    'body': {
                        'type': ['null', 'string'],
                        'description': 'Action body content (HTML for emails)',
                    },
                    'layout': {
                        'type': ['null', 'string'],
                        'description': 'Layout template used',
                    },
                    'from': {
                        'type': ['null', 'string'],
                        'description': 'From address',
                    },
                    'from_id': {
                        'type': ['null', 'integer'],
                        'description': 'Sender identity ID',
                    },
                    'subject': {
                        'type': ['null', 'string'],
                        'description': 'Email subject line',
                    },
                    'preheader_text': {
                        'type': ['null', 'string'],
                        'description': 'Email preheader/preview text',
                    },
                    'recipient': {
                        'type': ['null', 'string'],
                        'description': 'Recipient address',
                    },
                    'reply_to': {
                        'type': ['null', 'string'],
                        'description': 'Reply-to address',
                    },
                    'reply_to_id': {
                        'type': ['null', 'integer'],
                        'description': 'Reply-to sender identity ID',
                    },
                    'bcc': {
                        'type': ['null', 'string'],
                        'description': 'BCC addresses',
                    },
                    'fake_bcc': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to use fake BCC',
                    },
                    'headers': {
                        'type': ['null', 'string'],
                        'description': 'Custom email headers as JSON',
                    },
                    'sending_state': {
                        'type': ['null', 'string'],
                        'description': 'Sending behavior (automatic or draft)',
                    },
                    'language': {
                        'type': ['null', 'string'],
                        'description': 'Language variant',
                    },
                    'parent_action_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent action ID for language variants',
                    },
                    'preprocessor': {
                        'type': ['null', 'string'],
                        'description': 'CSS preprocessor setting',
                    },
                    'body_amp': {
                        'type': ['null', 'string'],
                        'description': 'AMP HTML body content',
                    },
                    'broadcast_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent broadcast ID',
                    },
                    'editor': {
                        'type': ['null', 'string'],
                        'description': 'Editor used to create the action',
                    },
                    'url': {
                        'type': ['null', 'string'],
                        'description': 'Webhook URL (for webhook actions)',
                    },
                    'body_plain': {
                        'type': ['null', 'string'],
                        'description': 'Plain text version of the action body',
                    },
                },
                'x-airbyte-entity-name': 'campaign_actions',
                'x-airbyte-stream-name': 'campaigns_actions',
                'x-airbyte-ai-hints': {
                    'summary': 'Individual actions (emails, webhooks, push notifications) within a campaign workflow',
                    'when_to_use': 'Questions about specific campaign steps, email content, or action configuration',
                    'trigger_phrases': [
                        'campaign actions',
                        'email content',
                        'campaign steps',
                        'action details',
                        'workflow actions',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What actions are in campaign 42?', 'Show me all email actions for a campaign', 'Get the subject line of action 5 in campaign 10'],
                    'search_strategy': 'Filter by campaign_id and action type',
                },
            },
            ai_hints={
                'summary': 'Individual actions (emails, webhooks, push notifications) within a campaign workflow',
                'when_to_use': 'Questions about specific campaign steps, email content, or action configuration',
                'trigger_phrases': [
                    'campaign actions',
                    'email content',
                    'campaign steps',
                    'action details',
                    'workflow actions',
                ],
                'freshness': 'live',
                'example_questions': ['What actions are in campaign 42?', 'Show me all email actions for a campaign', 'Get the subject line of action 5 in campaign 10'],
                'search_strategy': 'Filter by campaign_id and action type',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='campaign_actions',
                    target_entity='campaigns',
                    foreign_key='campaign_id',
                    cardinality='many_to_one',
                    description='Campaign actions belong to a campaign',
                ),
            ],
        ),
        EntityDefinition(
            name='newsletters',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/newsletters',
                    action=Action.LIST,
                    description='Returns a paginated list of newsletters.',
                    query_params=['start', 'limit', 'sort'],
                    query_params_schema={
                        'start': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'sort': {
                            'type': 'string',
                            'required': False,
                            'enum': ['asc', 'desc'],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'newsletters': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique newsletter identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Newsletter name',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Channel type (email, webhook, twilio, push, in_app, inbox)',
                                        },
                                        'created': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'sent_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'When the newsletter was last sent (Unix)',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier',
                                        },
                                        'tags': {
                                            'type': ['null', 'array'],
                                            'description': 'Tags associated with the newsletter',
                                            'items': {'type': 'string'},
                                        },
                                        'content_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Content variant IDs for this newsletter',
                                            'items': {'type': 'integer'},
                                        },
                                        'recipient_segment_ids': {
                                            'type': ['null', 'array'],
                                            'description': 'Segment IDs that define the newsletter audience',
                                            'items': {'type': 'integer'},
                                        },
                                        'subscription_topic_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Subscription topic ID',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'newsletters',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Broadcast-style newsletters and one-time sends to segments',
                                        'when_to_use': 'Questions about newsletters, broadcasts, one-time email sends, or newsletter scheduling',
                                        'trigger_phrases': [
                                            'newsletters',
                                            'broadcast',
                                            'newsletter list',
                                            'email sends',
                                            'one-time send',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show me all newsletters', 'Which newsletters were sent recently?', 'Get the details of newsletter 128'],
                                        'search_strategy': 'Search by name; filter by type or sent_at timestamp',
                                    },
                                },
                            },
                            'next': {'type': 'string', 'description': 'Cursor for the next page'},
                        },
                    },
                    record_extractor='$.newsletters',
                    meta_extractor={'next': '$.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/newsletters/{newsletter_id}',
                    action=Action.GET,
                    description='Returns a single newsletter by ID.',
                    path_params=['newsletter_id'],
                    path_params_schema={
                        'newsletter_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'newsletter': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique newsletter identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Newsletter name',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Channel type (email, webhook, twilio, push, in_app, inbox)',
                                    },
                                    'created': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'sent_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'When the newsletter was last sent (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'tags': {
                                        'type': ['null', 'array'],
                                        'description': 'Tags associated with the newsletter',
                                        'items': {'type': 'string'},
                                    },
                                    'content_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Content variant IDs for this newsletter',
                                        'items': {'type': 'integer'},
                                    },
                                    'recipient_segment_ids': {
                                        'type': ['null', 'array'],
                                        'description': 'Segment IDs that define the newsletter audience',
                                        'items': {'type': 'integer'},
                                    },
                                    'subscription_topic_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Subscription topic ID',
                                    },
                                },
                                'x-airbyte-entity-name': 'newsletters',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Broadcast-style newsletters and one-time sends to segments',
                                    'when_to_use': 'Questions about newsletters, broadcasts, one-time email sends, or newsletter scheduling',
                                    'trigger_phrases': [
                                        'newsletters',
                                        'broadcast',
                                        'newsletter list',
                                        'email sends',
                                        'one-time send',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Show me all newsletters', 'Which newsletters were sent recently?', 'Get the details of newsletter 128'],
                                    'search_strategy': 'Search by name; filter by type or sent_at timestamp',
                                },
                            },
                        },
                    },
                    record_extractor='$.newsletter',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique newsletter identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Newsletter name',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Channel type (email, webhook, twilio, push, in_app, inbox)',
                    },
                    'created': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'sent_at': {
                        'type': ['null', 'integer'],
                        'description': 'When the newsletter was last sent (Unix)',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier',
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'Tags associated with the newsletter',
                        'items': {'type': 'string'},
                    },
                    'content_ids': {
                        'type': ['null', 'array'],
                        'description': 'Content variant IDs for this newsletter',
                        'items': {'type': 'integer'},
                    },
                    'recipient_segment_ids': {
                        'type': ['null', 'array'],
                        'description': 'Segment IDs that define the newsletter audience',
                        'items': {'type': 'integer'},
                    },
                    'subscription_topic_id': {
                        'type': ['null', 'integer'],
                        'description': 'Subscription topic ID',
                    },
                },
                'x-airbyte-entity-name': 'newsletters',
                'x-airbyte-ai-hints': {
                    'summary': 'Broadcast-style newsletters and one-time sends to segments',
                    'when_to_use': 'Questions about newsletters, broadcasts, one-time email sends, or newsletter scheduling',
                    'trigger_phrases': [
                        'newsletters',
                        'broadcast',
                        'newsletter list',
                        'email sends',
                        'one-time send',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show me all newsletters', 'Which newsletters were sent recently?', 'Get the details of newsletter 128'],
                    'search_strategy': 'Search by name; filter by type or sent_at timestamp',
                },
            },
            ai_hints={
                'summary': 'Broadcast-style newsletters and one-time sends to segments',
                'when_to_use': 'Questions about newsletters, broadcasts, one-time email sends, or newsletter scheduling',
                'trigger_phrases': [
                    'newsletters',
                    'broadcast',
                    'newsletter list',
                    'email sends',
                    'one-time send',
                ],
                'freshness': 'live',
                'example_questions': ['Show me all newsletters', 'Which newsletters were sent recently?', 'Get the details of newsletter 128'],
                'search_strategy': 'Search by name; filter by type or sent_at timestamp',
            },
        ),
        EntityDefinition(
            name='segments',
            actions=[Action.LIST, Action.CREATE, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/segments',
                    action=Action.LIST,
                    description='Returns all segments in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'segments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique segment identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Segment name',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Segment description',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Segment type',
                                        },
                                        'state': {
                                            'type': ['null', 'string'],
                                            'description': 'Segment processing state',
                                        },
                                        'created_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier',
                                        },
                                        'tags': {
                                            'type': ['null', 'array'],
                                            'description': 'Tags associated with the segment',
                                            'items': {'type': 'string'},
                                        },
                                        'progress': {
                                            'type': ['null', 'integer'],
                                            'description': 'Processing progress percentage',
                                        },
                                        'conditions': {
                                            'type': ['null', 'object'],
                                            'description': 'Segment filter conditions',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'segments',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Customer segments used for targeting campaigns and broadcasts',
                                        'when_to_use': 'Questions about listing or retrieving segment definitions via the API (not for search)',
                                        'trigger_phrases': [
                                            'segments',
                                            'audience',
                                            'customer group',
                                            'targeting',
                                            'segment list',
                                        ],
                                        'example_questions': ['What segments are defined?', 'Show me the details of segment 15', 'List all segments'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.segments',
                    no_pagination='Returns all segments in a single response without pagination',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/segments',
                    action=Action.CREATE,
                    description='Creates a new empty manual segment. People can be added to it separately.',
                    body_fields=['segment'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'segment': {
                                'type': 'object',
                                'required': ['name'],
                                'properties': {
                                    'name': {'type': 'string', 'description': 'Name of the manual segment'},
                                    'description': {'type': 'string', 'description': 'Optional description of the segment'},
                                },
                            },
                        },
                        'required': ['segment'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'segment': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique segment identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment name',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment description',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment type',
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment processing state',
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'tags': {
                                        'type': ['null', 'array'],
                                        'description': 'Tags associated with the segment',
                                        'items': {'type': 'string'},
                                    },
                                    'progress': {
                                        'type': ['null', 'integer'],
                                        'description': 'Processing progress percentage',
                                    },
                                    'conditions': {
                                        'type': ['null', 'object'],
                                        'description': 'Segment filter conditions',
                                    },
                                },
                                'x-airbyte-entity-name': 'segments',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer segments used for targeting campaigns and broadcasts',
                                    'when_to_use': 'Questions about listing or retrieving segment definitions via the API (not for search)',
                                    'trigger_phrases': [
                                        'segments',
                                        'audience',
                                        'customer group',
                                        'targeting',
                                        'segment list',
                                    ],
                                    'example_questions': ['What segments are defined?', 'Show me the details of segment 15', 'List all segments'],
                                },
                            },
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/segments/{segment_id}',
                    action=Action.GET,
                    description='Returns a single segment by ID.',
                    path_params=['segment_id'],
                    path_params_schema={
                        'segment_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'segment': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique segment identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment name',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment description',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment type',
                                    },
                                    'state': {
                                        'type': ['null', 'string'],
                                        'description': 'Segment processing state',
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'tags': {
                                        'type': ['null', 'array'],
                                        'description': 'Tags associated with the segment',
                                        'items': {'type': 'string'},
                                    },
                                    'progress': {
                                        'type': ['null', 'integer'],
                                        'description': 'Processing progress percentage',
                                    },
                                    'conditions': {
                                        'type': ['null', 'object'],
                                        'description': 'Segment filter conditions',
                                    },
                                },
                                'x-airbyte-entity-name': 'segments',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer segments used for targeting campaigns and broadcasts',
                                    'when_to_use': 'Questions about listing or retrieving segment definitions via the API (not for search)',
                                    'trigger_phrases': [
                                        'segments',
                                        'audience',
                                        'customer group',
                                        'targeting',
                                        'segment list',
                                    ],
                                    'example_questions': ['What segments are defined?', 'Show me the details of segment 15', 'List all segments'],
                                },
                            },
                        },
                    },
                    record_extractor='$.segment',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique segment identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Segment name',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Segment description',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Segment type',
                    },
                    'state': {
                        'type': ['null', 'string'],
                        'description': 'Segment processing state',
                    },
                    'created_at': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier',
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'Tags associated with the segment',
                        'items': {'type': 'string'},
                    },
                    'progress': {
                        'type': ['null', 'integer'],
                        'description': 'Processing progress percentage',
                    },
                    'conditions': {
                        'type': ['null', 'object'],
                        'description': 'Segment filter conditions',
                    },
                },
                'x-airbyte-entity-name': 'segments',
                'x-airbyte-ai-hints': {
                    'summary': 'Customer segments used for targeting campaigns and broadcasts',
                    'when_to_use': 'Questions about listing or retrieving segment definitions via the API (not for search)',
                    'trigger_phrases': [
                        'segments',
                        'audience',
                        'customer group',
                        'targeting',
                        'segment list',
                    ],
                    'example_questions': ['What segments are defined?', 'Show me the details of segment 15', 'List all segments'],
                },
            },
            ai_hints={
                'summary': 'Customer segments used for targeting campaigns and broadcasts',
                'when_to_use': 'Questions about listing or retrieving segment definitions via the API (not for search)',
                'trigger_phrases': [
                    'segments',
                    'audience',
                    'customer group',
                    'targeting',
                    'segment list',
                ],
                'example_questions': ['What segments are defined?', 'Show me the details of segment 15', 'List all segments'],
            },
        ),
        EntityDefinition(
            name='messages',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/messages',
                    action=Action.LIST,
                    description='Returns a paginated list of message deliveries.',
                    query_params=[
                        'start',
                        'limit',
                        'type',
                        'metric',
                        'campaign_id',
                        'newsletter_id',
                    ],
                    query_params_schema={
                        'start': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'type': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'email',
                                'webhook',
                                'twilio',
                                'whatsapp',
                                'slack',
                                'push',
                                'in_app',
                            ],
                        },
                        'metric': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'attempted',
                                'sent',
                                'delivered',
                                'opened',
                                'clicked',
                                'converted',
                                'bounced',
                                'spammed',
                                'unsubscribed',
                                'dropped',
                                'failed',
                                'undeliverable',
                            ],
                        },
                        'campaign_id': {'type': 'integer', 'required': False},
                        'newsletter_id': {'type': 'integer', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'messages': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique message delivery identifier',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Message channel type',
                                        },
                                        'created': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier',
                                        },
                                        'customer_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Customer profile ID',
                                        },
                                        'customer_identifiers': {
                                            'type': ['null', 'object'],
                                            'description': 'Customer identification details',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                    'description': "Person's ID",
                                                },
                                                'cio_id': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Customer.io internal ID',
                                                },
                                                'email': {
                                                    'type': ['null', 'string'],
                                                    'description': "Person's email address",
                                                },
                                            },
                                        },
                                        'campaign_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent campaign ID',
                                        },
                                        'newsletter_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent newsletter ID',
                                        },
                                        'broadcast_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent broadcast ID',
                                        },
                                        'content_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Newsletter content variant ID',
                                        },
                                        'action_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Action ID that sent the message',
                                        },
                                        'parent_action_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Parent action ID',
                                        },
                                        'message_template_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Message template ID',
                                        },
                                        'recipient': {
                                            'type': ['null', 'string'],
                                            'description': 'Recipient address',
                                        },
                                        'subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Message subject line',
                                        },
                                        'forgotten': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether message contents were not retained',
                                        },
                                        'failure_message': {
                                            'type': ['null', 'string'],
                                            'description': 'Failure reason if delivery failed',
                                        },
                                        'trigger_event_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Event that triggered the campaign',
                                        },
                                        'metrics': {
                                            'type': ['null', 'object'],
                                            'description': 'Delivery metrics timestamps',
                                            'properties': {
                                                'created': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'drafted': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'sent': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'delivered': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'opened': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'clicked': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'converted': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'bounced': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'failed': {
                                                    'type': ['null', 'integer'],
                                                },
                                                'undeliverable': {
                                                    'type': ['null', 'integer'],
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'messages',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Individual message deliveries including emails, push notifications, SMS, and in-app messages',
                                        'when_to_use': 'Questions about message delivery status, delivery metrics, or individual message details',
                                        'trigger_phrases': [
                                            'messages',
                                            'deliveries',
                                            'sent messages',
                                            'delivery status',
                                            'email metrics',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show me recent message deliveries', 'What is the delivery status of message abc123?', 'List all bounced email deliveries'],
                                        'search_strategy': 'Filter by type (email/push/sms), metric (sent/delivered/opened), campaign_id, or newsletter_id',
                                    },
                                },
                            },
                            'next': {'type': 'string', 'description': 'Cursor for the next page'},
                        },
                    },
                    record_extractor='$.messages',
                    meta_extractor={'next': '$.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/messages/{message_id}',
                    action=Action.GET,
                    description='Returns a single message delivery by ID. Untested because the test workspace has no message deliveries to retrieve.\n',
                    path_params=['message_id'],
                    path_params_schema={
                        'message_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'message': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'string'],
                                        'description': 'Unique message delivery identifier',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Message channel type',
                                    },
                                    'created': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'customer_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Customer profile ID',
                                    },
                                    'customer_identifiers': {
                                        'type': ['null', 'object'],
                                        'description': 'Customer identification details',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                                'description': "Person's ID",
                                            },
                                            'cio_id': {
                                                'type': ['null', 'string'],
                                                'description': 'Customer.io internal ID',
                                            },
                                            'email': {
                                                'type': ['null', 'string'],
                                                'description': "Person's email address",
                                            },
                                        },
                                    },
                                    'campaign_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent campaign ID',
                                    },
                                    'newsletter_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent newsletter ID',
                                    },
                                    'broadcast_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent broadcast ID',
                                    },
                                    'content_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Newsletter content variant ID',
                                    },
                                    'action_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Action ID that sent the message',
                                    },
                                    'parent_action_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Parent action ID',
                                    },
                                    'message_template_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Message template ID',
                                    },
                                    'recipient': {
                                        'type': ['null', 'string'],
                                        'description': 'Recipient address',
                                    },
                                    'subject': {
                                        'type': ['null', 'string'],
                                        'description': 'Message subject line',
                                    },
                                    'forgotten': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether message contents were not retained',
                                    },
                                    'failure_message': {
                                        'type': ['null', 'string'],
                                        'description': 'Failure reason if delivery failed',
                                    },
                                    'trigger_event_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Event that triggered the campaign',
                                    },
                                    'metrics': {
                                        'type': ['null', 'object'],
                                        'description': 'Delivery metrics timestamps',
                                        'properties': {
                                            'created': {
                                                'type': ['null', 'integer'],
                                            },
                                            'drafted': {
                                                'type': ['null', 'integer'],
                                            },
                                            'sent': {
                                                'type': ['null', 'integer'],
                                            },
                                            'delivered': {
                                                'type': ['null', 'integer'],
                                            },
                                            'opened': {
                                                'type': ['null', 'integer'],
                                            },
                                            'clicked': {
                                                'type': ['null', 'integer'],
                                            },
                                            'converted': {
                                                'type': ['null', 'integer'],
                                            },
                                            'bounced': {
                                                'type': ['null', 'integer'],
                                            },
                                            'failed': {
                                                'type': ['null', 'integer'],
                                            },
                                            'undeliverable': {
                                                'type': ['null', 'integer'],
                                            },
                                        },
                                    },
                                },
                                'x-airbyte-entity-name': 'messages',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Individual message deliveries including emails, push notifications, SMS, and in-app messages',
                                    'when_to_use': 'Questions about message delivery status, delivery metrics, or individual message details',
                                    'trigger_phrases': [
                                        'messages',
                                        'deliveries',
                                        'sent messages',
                                        'delivery status',
                                        'email metrics',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Show me recent message deliveries', 'What is the delivery status of message abc123?', 'List all bounced email deliveries'],
                                    'search_strategy': 'Filter by type (email/push/sms), metric (sent/delivered/opened), campaign_id, or newsletter_id',
                                },
                            },
                        },
                    },
                    record_extractor='$.message',
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique message delivery identifier',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Message channel type',
                    },
                    'created': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier',
                    },
                    'customer_id': {
                        'type': ['null', 'string'],
                        'description': 'Customer profile ID',
                    },
                    'customer_identifiers': {
                        'type': ['null', 'object'],
                        'description': 'Customer identification details',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': "Person's ID",
                            },
                            'cio_id': {
                                'type': ['null', 'string'],
                                'description': 'Customer.io internal ID',
                            },
                            'email': {
                                'type': ['null', 'string'],
                                'description': "Person's email address",
                            },
                        },
                    },
                    'campaign_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent campaign ID',
                    },
                    'newsletter_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent newsletter ID',
                    },
                    'broadcast_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent broadcast ID',
                    },
                    'content_id': {
                        'type': ['null', 'integer'],
                        'description': 'Newsletter content variant ID',
                    },
                    'action_id': {
                        'type': ['null', 'integer'],
                        'description': 'Action ID that sent the message',
                    },
                    'parent_action_id': {
                        'type': ['null', 'integer'],
                        'description': 'Parent action ID',
                    },
                    'message_template_id': {
                        'type': ['null', 'integer'],
                        'description': 'Message template ID',
                    },
                    'recipient': {
                        'type': ['null', 'string'],
                        'description': 'Recipient address',
                    },
                    'subject': {
                        'type': ['null', 'string'],
                        'description': 'Message subject line',
                    },
                    'forgotten': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether message contents were not retained',
                    },
                    'failure_message': {
                        'type': ['null', 'string'],
                        'description': 'Failure reason if delivery failed',
                    },
                    'trigger_event_id': {
                        'type': ['null', 'string'],
                        'description': 'Event that triggered the campaign',
                    },
                    'metrics': {
                        'type': ['null', 'object'],
                        'description': 'Delivery metrics timestamps',
                        'properties': {
                            'created': {
                                'type': ['null', 'integer'],
                            },
                            'drafted': {
                                'type': ['null', 'integer'],
                            },
                            'sent': {
                                'type': ['null', 'integer'],
                            },
                            'delivered': {
                                'type': ['null', 'integer'],
                            },
                            'opened': {
                                'type': ['null', 'integer'],
                            },
                            'clicked': {
                                'type': ['null', 'integer'],
                            },
                            'converted': {
                                'type': ['null', 'integer'],
                            },
                            'bounced': {
                                'type': ['null', 'integer'],
                            },
                            'failed': {
                                'type': ['null', 'integer'],
                            },
                            'undeliverable': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'messages',
                'x-airbyte-ai-hints': {
                    'summary': 'Individual message deliveries including emails, push notifications, SMS, and in-app messages',
                    'when_to_use': 'Questions about message delivery status, delivery metrics, or individual message details',
                    'trigger_phrases': [
                        'messages',
                        'deliveries',
                        'sent messages',
                        'delivery status',
                        'email metrics',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show me recent message deliveries', 'What is the delivery status of message abc123?', 'List all bounced email deliveries'],
                    'search_strategy': 'Filter by type (email/push/sms), metric (sent/delivered/opened), campaign_id, or newsletter_id',
                },
            },
            ai_hints={
                'summary': 'Individual message deliveries including emails, push notifications, SMS, and in-app messages',
                'when_to_use': 'Questions about message delivery status, delivery metrics, or individual message details',
                'trigger_phrases': [
                    'messages',
                    'deliveries',
                    'sent messages',
                    'delivery status',
                    'email metrics',
                ],
                'freshness': 'live',
                'example_questions': ['Show me recent message deliveries', 'What is the delivery status of message abc123?', 'List all bounced email deliveries'],
                'search_strategy': 'Filter by type (email/push/sms), metric (sent/delivered/opened), campaign_id, or newsletter_id',
            },
        ),
        EntityDefinition(
            name='activities',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/activities',
                    action=Action.LIST,
                    description='Returns a paginated list of activities in the workspace.',
                    query_params=[
                        'start',
                        'limit',
                        'type',
                        'name',
                    ],
                    query_params_schema={
                        'start': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'type': {'type': 'string', 'required': False},
                        'name': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'activities': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Activity identifier',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Activity type (e.g., email_sent, email_opened)',
                                        },
                                        'timestamp': {
                                            'type': ['null', 'integer'],
                                            'description': 'When the activity occurred (Unix)',
                                        },
                                        'customer_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Customer profile ID',
                                        },
                                        'customer_identifiers': {
                                            'type': ['null', 'object'],
                                            'description': 'Customer identification details',
                                            'properties': {
                                                'id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'cio_id': {
                                                    'type': ['null', 'string'],
                                                },
                                                'email': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'delivery_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Message delivery ID',
                                        },
                                        'delivery_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Delivery channel type',
                                        },
                                        'data': {
                                            'type': ['null', 'object'],
                                            'description': 'Activity-specific data payload',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'activities',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Global activity log tracking all events, deliveries, and interactions in the workspace',
                                        'when_to_use': 'Questions about recent events, customer interactions, or delivery activity',
                                        'trigger_phrases': [
                                            'activities',
                                            'activity log',
                                            'recent events',
                                            'what happened',
                                            'event history',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show me recent activities', 'What happened in the last hour?', 'List all email_opened activities'],
                                        'search_strategy': 'Filter by activity type or name; use cursor pagination for recent events',
                                    },
                                },
                            },
                            'next': {'type': 'string', 'description': 'Cursor for the next page'},
                        },
                    },
                    record_extractor='$.activities',
                    meta_extractor={'next': '$.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Activity identifier',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Activity type (e.g., email_sent, email_opened)',
                    },
                    'timestamp': {
                        'type': ['null', 'integer'],
                        'description': 'When the activity occurred (Unix)',
                    },
                    'customer_id': {
                        'type': ['null', 'string'],
                        'description': 'Customer profile ID',
                    },
                    'customer_identifiers': {
                        'type': ['null', 'object'],
                        'description': 'Customer identification details',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                            },
                            'cio_id': {
                                'type': ['null', 'string'],
                            },
                            'email': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'delivery_id': {
                        'type': ['null', 'string'],
                        'description': 'Message delivery ID',
                    },
                    'delivery_type': {
                        'type': ['null', 'string'],
                        'description': 'Delivery channel type',
                    },
                    'data': {
                        'type': ['null', 'object'],
                        'description': 'Activity-specific data payload',
                    },
                },
                'x-airbyte-entity-name': 'activities',
                'x-airbyte-ai-hints': {
                    'summary': 'Global activity log tracking all events, deliveries, and interactions in the workspace',
                    'when_to_use': 'Questions about recent events, customer interactions, or delivery activity',
                    'trigger_phrases': [
                        'activities',
                        'activity log',
                        'recent events',
                        'what happened',
                        'event history',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show me recent activities', 'What happened in the last hour?', 'List all email_opened activities'],
                    'search_strategy': 'Filter by activity type or name; use cursor pagination for recent events',
                },
            },
            ai_hints={
                'summary': 'Global activity log tracking all events, deliveries, and interactions in the workspace',
                'when_to_use': 'Questions about recent events, customer interactions, or delivery activity',
                'trigger_phrases': [
                    'activities',
                    'activity log',
                    'recent events',
                    'what happened',
                    'event history',
                ],
                'freshness': 'live',
                'example_questions': ['Show me recent activities', 'What happened in the last hour?', 'List all email_opened activities'],
                'search_strategy': 'Filter by activity type or name; use cursor pagination for recent events',
            },
        ),
        EntityDefinition(
            name='sender_identities',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/sender_identities',
                    action=Action.LIST,
                    description='Returns a paginated list of sender identities.',
                    query_params=['start', 'limit', 'sort'],
                    query_params_schema={
                        'start': {'type': 'string', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'minimum': 1,
                            'maximum': 100,
                        },
                        'sort': {
                            'type': 'string',
                            'required': False,
                            'enum': ['asc', 'desc'],
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'sender_identities': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique sender identity identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Sender display name',
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                            'description': 'Sender email address',
                                        },
                                        'address': {
                                            'type': ['null', 'string'],
                                            'description': 'Full address in "Name <email>" format',
                                        },
                                        'template_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Sender type (email or phone)',
                                        },
                                        'auto_generated': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the identity was auto-generated by Customer.io',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier',
                                        },
                                        'phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Sender phone number',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'sender_identities',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sender email addresses and identities used for sending messages',
                                        'when_to_use': 'Questions about from addresses, sender configuration, or who messages are sent from',
                                        'trigger_phrases': [
                                            'sender identities',
                                            'from address',
                                            'sender email',
                                            'who sends',
                                        ],
                                        'freshness': 'static',
                                        'example_questions': ['What sender identities are configured?', 'Show me all email senders'],
                                        'search_strategy': 'Search by sender name or email address',
                                    },
                                },
                            },
                            'next': {'type': 'string', 'description': 'Cursor for the next page'},
                        },
                    },
                    record_extractor='$.sender_identities',
                    meta_extractor={'next': '$.next'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/sender_identities/{sender_id}',
                    action=Action.GET,
                    description='Returns a single sender identity by ID.',
                    path_params=['sender_id'],
                    path_params_schema={
                        'sender_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'sender_identity': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique sender identity identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Sender display name',
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                        'description': 'Sender email address',
                                    },
                                    'address': {
                                        'type': ['null', 'string'],
                                        'description': 'Full address in "Name <email>" format',
                                    },
                                    'template_type': {
                                        'type': ['null', 'string'],
                                        'description': 'Sender type (email or phone)',
                                    },
                                    'auto_generated': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the identity was auto-generated by Customer.io',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'phone': {
                                        'type': ['null', 'string'],
                                        'description': 'Sender phone number',
                                    },
                                },
                                'x-airbyte-entity-name': 'sender_identities',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Sender email addresses and identities used for sending messages',
                                    'when_to_use': 'Questions about from addresses, sender configuration, or who messages are sent from',
                                    'trigger_phrases': [
                                        'sender identities',
                                        'from address',
                                        'sender email',
                                        'who sends',
                                    ],
                                    'freshness': 'static',
                                    'example_questions': ['What sender identities are configured?', 'Show me all email senders'],
                                    'search_strategy': 'Search by sender name or email address',
                                },
                            },
                        },
                    },
                    record_extractor='$.sender_identity',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique sender identity identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Sender display name',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'Sender email address',
                    },
                    'address': {
                        'type': ['null', 'string'],
                        'description': 'Full address in "Name <email>" format',
                    },
                    'template_type': {
                        'type': ['null', 'string'],
                        'description': 'Sender type (email or phone)',
                    },
                    'auto_generated': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the identity was auto-generated by Customer.io',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier',
                    },
                    'phone': {
                        'type': ['null', 'string'],
                        'description': 'Sender phone number',
                    },
                },
                'x-airbyte-entity-name': 'sender_identities',
                'x-airbyte-ai-hints': {
                    'summary': 'Sender email addresses and identities used for sending messages',
                    'when_to_use': 'Questions about from addresses, sender configuration, or who messages are sent from',
                    'trigger_phrases': [
                        'sender identities',
                        'from address',
                        'sender email',
                        'who sends',
                    ],
                    'freshness': 'static',
                    'example_questions': ['What sender identities are configured?', 'Show me all email senders'],
                    'search_strategy': 'Search by sender name or email address',
                },
            },
            ai_hints={
                'summary': 'Sender email addresses and identities used for sending messages',
                'when_to_use': 'Questions about from addresses, sender configuration, or who messages are sent from',
                'trigger_phrases': [
                    'sender identities',
                    'from address',
                    'sender email',
                    'who sends',
                ],
                'freshness': 'static',
                'example_questions': ['What sender identities are configured?', 'Show me all email senders'],
                'search_strategy': 'Search by sender name or email address',
            },
        ),
        EntityDefinition(
            name='snippets',
            actions=[Action.LIST, Action.CREATE, Action.UPDATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/snippets',
                    action=Action.LIST,
                    description='Returns all snippets in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'snippets': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique snippet name',
                                        },
                                        'value': {
                                            'type': ['null', 'string'],
                                            'description': 'Snippet content (liquid/HTML)',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'snippets',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reusable liquid content blocks that can be embedded in messages',
                                        'when_to_use': 'Questions about listing or managing reusable content snippets via the API (not for search)',
                                        'trigger_phrases': [
                                            'snippets',
                                            'reusable content',
                                            'liquid blocks',
                                            'content blocks',
                                        ],
                                        'example_questions': ['What snippets are available?', 'Show me all content snippets'],
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.snippets',
                    no_pagination='Returns all snippets in a single response without pagination',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/snippets',
                    action=Action.CREATE,
                    description='Creates a new reusable content snippet. Returns 422 if a snippet with the same name already exists.',
                    body_fields=['name', 'value'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Unique snippet name (used as the liquid tag identifier)'},
                            'value': {'type': 'string', 'description': 'Snippet content (plain text, HTML, or Liquid)'},
                        },
                        'required': ['name', 'value'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'snippet': {
                                'type': 'object',
                                'properties': {
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Unique snippet name',
                                    },
                                    'value': {
                                        'type': ['null', 'string'],
                                        'description': 'Snippet content (liquid/HTML)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                },
                                'x-airbyte-entity-name': 'snippets',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Reusable liquid content blocks that can be embedded in messages',
                                    'when_to_use': 'Questions about listing or managing reusable content snippets via the API (not for search)',
                                    'trigger_phrases': [
                                        'snippets',
                                        'reusable content',
                                        'liquid blocks',
                                        'content blocks',
                                    ],
                                    'example_questions': ['What snippets are available?', 'Show me all content snippets'],
                                },
                            },
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/v1/snippets',
                    action=Action.UPDATE,
                    description='Updates an existing snippet by name, or creates it if it does not exist (upsert behavior).',
                    body_fields=['name', 'value'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Snippet name to update (or create if it does not exist)'},
                            'value': {'type': 'string', 'description': 'New snippet content (plain text, HTML, or Liquid)'},
                        },
                        'required': ['name', 'value'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'snippet': {
                                'type': 'object',
                                'properties': {
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Unique snippet name',
                                    },
                                    'value': {
                                        'type': ['null', 'string'],
                                        'description': 'Snippet content (liquid/HTML)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                },
                                'x-airbyte-entity-name': 'snippets',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Reusable liquid content blocks that can be embedded in messages',
                                    'when_to_use': 'Questions about listing or managing reusable content snippets via the API (not for search)',
                                    'trigger_phrases': [
                                        'snippets',
                                        'reusable content',
                                        'liquid blocks',
                                        'content blocks',
                                    ],
                                    'example_questions': ['What snippets are available?', 'Show me all content snippets'],
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Unique snippet name',
                    },
                    'value': {
                        'type': ['null', 'string'],
                        'description': 'Snippet content (liquid/HTML)',
                    },
                    'updated_at': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                },
                'x-airbyte-entity-name': 'snippets',
                'x-airbyte-ai-hints': {
                    'summary': 'Reusable liquid content blocks that can be embedded in messages',
                    'when_to_use': 'Questions about listing or managing reusable content snippets via the API (not for search)',
                    'trigger_phrases': [
                        'snippets',
                        'reusable content',
                        'liquid blocks',
                        'content blocks',
                    ],
                    'example_questions': ['What snippets are available?', 'Show me all content snippets'],
                },
            },
            ai_hints={
                'summary': 'Reusable liquid content blocks that can be embedded in messages',
                'when_to_use': 'Questions about listing or managing reusable content snippets via the API (not for search)',
                'trigger_phrases': [
                    'snippets',
                    'reusable content',
                    'liquid blocks',
                    'content blocks',
                ],
                'example_questions': ['What snippets are available?', 'Show me all content snippets'],
            },
        ),
        EntityDefinition(
            name='collections',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/collections',
                    action=Action.LIST,
                    description='Returns all collections in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'collections': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique collection identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Collection name (used in liquid)',
                                        },
                                        'bytes': {
                                            'type': ['null', 'integer'],
                                            'description': 'Size of the collection in bytes',
                                        },
                                        'rows': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of rows/objects in the collection',
                                        },
                                        'schema': {
                                            'type': ['null', 'array'],
                                            'description': 'Top-level keys in the collection',
                                            'items': {'type': 'string'},
                                        },
                                        'created_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'collections',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Data collections used for personalization and liquid templating',
                                        'when_to_use': 'Questions about data collections, lookup tables, or personalization data',
                                        'trigger_phrases': [
                                            'collections',
                                            'data tables',
                                            'lookup data',
                                            'personalization data',
                                        ],
                                        'freshness': 'static',
                                        'example_questions': ['What collections are defined?', 'How large is the products collection?'],
                                        'search_strategy': 'Search by collection name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.collections',
                    untested=True,
                    no_pagination='Returns all collections in a single response without pagination',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/collections',
                    action=Action.CREATE,
                    description='Creates a new data collection with inline data or a URL source.',
                    body_fields=['name', 'data', 'url'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Collection name, referenced in Liquid as collection_name.property'},
                            'data': {
                                'type': 'array',
                                'description': 'Inline collection data (array of objects). Provide either data or url, not both.',
                                'items': {'type': 'object'},
                            },
                            'url': {'type': 'string', 'description': 'URL to a CSV or JSON file containing collection data. Provide either data or url, not both.'},
                        },
                        'required': ['name'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'collection': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique collection identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Collection name (used in liquid)',
                                    },
                                    'bytes': {
                                        'type': ['null', 'integer'],
                                        'description': 'Size of the collection in bytes',
                                    },
                                    'rows': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of rows/objects in the collection',
                                    },
                                    'schema': {
                                        'type': ['null', 'array'],
                                        'description': 'Top-level keys in the collection',
                                        'items': {'type': 'string'},
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                },
                                'x-airbyte-entity-name': 'collections',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Data collections used for personalization and liquid templating',
                                    'when_to_use': 'Questions about data collections, lookup tables, or personalization data',
                                    'trigger_phrases': [
                                        'collections',
                                        'data tables',
                                        'lookup data',
                                        'personalization data',
                                    ],
                                    'freshness': 'static',
                                    'example_questions': ['What collections are defined?', 'How large is the products collection?'],
                                    'search_strategy': 'Search by collection name',
                                },
                            },
                        },
                    },
                    untested=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/collections/{collection_id}',
                    action=Action.GET,
                    description='Returns a single collection by ID.',
                    path_params=['collection_id'],
                    path_params_schema={
                        'collection_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'collection': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique collection identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Collection name (used in liquid)',
                                    },
                                    'bytes': {
                                        'type': ['null', 'integer'],
                                        'description': 'Size of the collection in bytes',
                                    },
                                    'rows': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of rows/objects in the collection',
                                    },
                                    'schema': {
                                        'type': ['null', 'array'],
                                        'description': 'Top-level keys in the collection',
                                        'items': {'type': 'string'},
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                },
                                'x-airbyte-entity-name': 'collections',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Data collections used for personalization and liquid templating',
                                    'when_to_use': 'Questions about data collections, lookup tables, or personalization data',
                                    'trigger_phrases': [
                                        'collections',
                                        'data tables',
                                        'lookup data',
                                        'personalization data',
                                    ],
                                    'freshness': 'static',
                                    'example_questions': ['What collections are defined?', 'How large is the products collection?'],
                                    'search_strategy': 'Search by collection name',
                                },
                            },
                        },
                    },
                    record_extractor='$.collection',
                    untested=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/v1/collections/{collection_id}',
                    action=Action.UPDATE,
                    description="Updates an existing collection's name, data, or URL source.",
                    body_fields=['name', 'data', 'url'],
                    path_params=['collection_id'],
                    path_params_schema={
                        'collection_id': {'type': 'integer', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Rename the collection'},
                            'data': {
                                'type': 'array',
                                'description': 'Replace collection data entirely (array of objects). Provide either data or url, not both.',
                                'items': {'type': 'object'},
                            },
                            'url': {'type': 'string', 'description': 'Replace the URL source for collection data. Provide either data or url, not both.'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'collection': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique collection identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Collection name (used in liquid)',
                                    },
                                    'bytes': {
                                        'type': ['null', 'integer'],
                                        'description': 'Size of the collection in bytes',
                                    },
                                    'rows': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of rows/objects in the collection',
                                    },
                                    'schema': {
                                        'type': ['null', 'array'],
                                        'description': 'Top-level keys in the collection',
                                        'items': {'type': 'string'},
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                },
                                'x-airbyte-entity-name': 'collections',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Data collections used for personalization and liquid templating',
                                    'when_to_use': 'Questions about data collections, lookup tables, or personalization data',
                                    'trigger_phrases': [
                                        'collections',
                                        'data tables',
                                        'lookup data',
                                        'personalization data',
                                    ],
                                    'freshness': 'static',
                                    'example_questions': ['What collections are defined?', 'How large is the products collection?'],
                                    'search_strategy': 'Search by collection name',
                                },
                            },
                        },
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique collection identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Collection name (used in liquid)',
                    },
                    'bytes': {
                        'type': ['null', 'integer'],
                        'description': 'Size of the collection in bytes',
                    },
                    'rows': {
                        'type': ['null', 'integer'],
                        'description': 'Number of rows/objects in the collection',
                    },
                    'schema': {
                        'type': ['null', 'array'],
                        'description': 'Top-level keys in the collection',
                        'items': {'type': 'string'},
                    },
                    'created_at': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                },
                'x-airbyte-entity-name': 'collections',
                'x-airbyte-ai-hints': {
                    'summary': 'Data collections used for personalization and liquid templating',
                    'when_to_use': 'Questions about data collections, lookup tables, or personalization data',
                    'trigger_phrases': [
                        'collections',
                        'data tables',
                        'lookup data',
                        'personalization data',
                    ],
                    'freshness': 'static',
                    'example_questions': ['What collections are defined?', 'How large is the products collection?'],
                    'search_strategy': 'Search by collection name',
                },
            },
            ai_hints={
                'summary': 'Data collections used for personalization and liquid templating',
                'when_to_use': 'Questions about data collections, lookup tables, or personalization data',
                'trigger_phrases': [
                    'collections',
                    'data tables',
                    'lookup data',
                    'personalization data',
                ],
                'freshness': 'static',
                'example_questions': ['What collections are defined?', 'How large is the products collection?'],
                'search_strategy': 'Search by collection name',
            },
        ),
        EntityDefinition(
            name='reporting_webhooks',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/reporting_webhooks',
                    action=Action.LIST,
                    description='Returns all reporting webhooks in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'reporting_webhooks': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique webhook identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Webhook display name',
                                        },
                                        'endpoint': {
                                            'type': ['null', 'string'],
                                            'description': 'Webhook URL',
                                        },
                                        'disabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the webhook is disabled',
                                        },
                                        'full_resolution': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Send all events, not just unique',
                                        },
                                        'with_content': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Include message body in sent events',
                                        },
                                        'events': {
                                            'type': ['null', 'array'],
                                            'description': 'Event types to report',
                                            'items': {'type': 'string'},
                                        },
                                    },
                                    'x-airbyte-entity-name': 'reporting_webhooks',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Webhook endpoints configured to receive message event notifications',
                                        'when_to_use': 'Questions about webhook configuration, event reporting endpoints, or notification URLs',
                                        'trigger_phrases': [
                                            'reporting webhooks',
                                            'webhook config',
                                            'event notifications',
                                            'webhook endpoints',
                                        ],
                                        'freshness': 'static',
                                        'example_questions': ['What reporting webhooks are configured?', 'Is there a webhook for email events?'],
                                        'search_strategy': 'Search by webhook name or endpoint URL',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.reporting_webhooks',
                    untested=True,
                    no_pagination='Returns all reporting webhooks in a single response without pagination',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/reporting_webhooks',
                    action=Action.CREATE,
                    description='Creates a new reporting webhook to receive event notifications at the specified endpoint.',
                    body_fields=[
                        'name',
                        'endpoint',
                        'events',
                        'disabled',
                        'full_resolution',
                        'with_content',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Webhook display name'},
                            'endpoint': {'type': 'string', 'description': 'The URL to receive webhook notifications'},
                            'events': {
                                'type': 'array',
                                'description': 'Event types to report (e.g. customer_subscribed, email_sent, email_opened, email_clicked, email_bounced, email_converted, email_unsubscribed, sms_sent, sms_delivered, push_sent)\n',
                                'items': {'type': 'string'},
                            },
                            'disabled': {'type': 'boolean', 'description': 'Whether the webhook should be disabled initially'},
                            'full_resolution': {'type': 'boolean', 'description': 'Send all events instead of only unique events'},
                            'with_content': {'type': 'boolean', 'description': 'Include the message body in sent events'},
                        },
                        'required': ['name', 'endpoint', 'events'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique webhook identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Webhook display name',
                            },
                            'endpoint': {
                                'type': ['null', 'string'],
                                'description': 'Webhook URL',
                            },
                            'disabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the webhook is disabled',
                            },
                            'full_resolution': {
                                'type': ['null', 'boolean'],
                                'description': 'Send all events, not just unique',
                            },
                            'with_content': {
                                'type': ['null', 'boolean'],
                                'description': 'Include message body in sent events',
                            },
                            'events': {
                                'type': ['null', 'array'],
                                'description': 'Event types to report',
                                'items': {'type': 'string'},
                            },
                        },
                        'x-airbyte-entity-name': 'reporting_webhooks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Webhook endpoints configured to receive message event notifications',
                            'when_to_use': 'Questions about webhook configuration, event reporting endpoints, or notification URLs',
                            'trigger_phrases': [
                                'reporting webhooks',
                                'webhook config',
                                'event notifications',
                                'webhook endpoints',
                            ],
                            'freshness': 'static',
                            'example_questions': ['What reporting webhooks are configured?', 'Is there a webhook for email events?'],
                            'search_strategy': 'Search by webhook name or endpoint URL',
                        },
                    },
                    untested=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/reporting_webhooks/{webhook_id}',
                    action=Action.GET,
                    description='Returns a single reporting webhook by ID.',
                    path_params=['webhook_id'],
                    path_params_schema={
                        'webhook_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'reporting_webhook': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique webhook identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Webhook display name',
                                    },
                                    'endpoint': {
                                        'type': ['null', 'string'],
                                        'description': 'Webhook URL',
                                    },
                                    'disabled': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the webhook is disabled',
                                    },
                                    'full_resolution': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Send all events, not just unique',
                                    },
                                    'with_content': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Include message body in sent events',
                                    },
                                    'events': {
                                        'type': ['null', 'array'],
                                        'description': 'Event types to report',
                                        'items': {'type': 'string'},
                                    },
                                },
                                'x-airbyte-entity-name': 'reporting_webhooks',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Webhook endpoints configured to receive message event notifications',
                                    'when_to_use': 'Questions about webhook configuration, event reporting endpoints, or notification URLs',
                                    'trigger_phrases': [
                                        'reporting webhooks',
                                        'webhook config',
                                        'event notifications',
                                        'webhook endpoints',
                                    ],
                                    'freshness': 'static',
                                    'example_questions': ['What reporting webhooks are configured?', 'Is there a webhook for email events?'],
                                    'search_strategy': 'Search by webhook name or endpoint URL',
                                },
                            },
                        },
                    },
                    record_extractor='$.reporting_webhook',
                    untested=True,
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/v1/reporting_webhooks/{webhook_id}',
                    action=Action.UPDATE,
                    description="Updates an existing reporting webhook's configuration.",
                    body_fields=[
                        'name',
                        'endpoint',
                        'events',
                        'disabled',
                        'full_resolution',
                        'with_content',
                    ],
                    path_params=['webhook_id'],
                    path_params_schema={
                        'webhook_id': {'type': 'integer', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'Webhook display name'},
                            'endpoint': {'type': 'string', 'description': 'The URL to receive webhook notifications'},
                            'events': {
                                'type': 'array',
                                'description': 'Event types to report',
                                'items': {'type': 'string'},
                            },
                            'disabled': {'type': 'boolean', 'description': 'Whether the webhook is disabled'},
                            'full_resolution': {'type': 'boolean', 'description': 'Send all events instead of only unique events'},
                            'with_content': {'type': 'boolean', 'description': 'Include the message body in sent events'},
                        },
                        'required': ['name', 'endpoint', 'events'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Unique webhook identifier',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Webhook display name',
                            },
                            'endpoint': {
                                'type': ['null', 'string'],
                                'description': 'Webhook URL',
                            },
                            'disabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the webhook is disabled',
                            },
                            'full_resolution': {
                                'type': ['null', 'boolean'],
                                'description': 'Send all events, not just unique',
                            },
                            'with_content': {
                                'type': ['null', 'boolean'],
                                'description': 'Include message body in sent events',
                            },
                            'events': {
                                'type': ['null', 'array'],
                                'description': 'Event types to report',
                                'items': {'type': 'string'},
                            },
                        },
                        'x-airbyte-entity-name': 'reporting_webhooks',
                        'x-airbyte-ai-hints': {
                            'summary': 'Webhook endpoints configured to receive message event notifications',
                            'when_to_use': 'Questions about webhook configuration, event reporting endpoints, or notification URLs',
                            'trigger_phrases': [
                                'reporting webhooks',
                                'webhook config',
                                'event notifications',
                                'webhook endpoints',
                            ],
                            'freshness': 'static',
                            'example_questions': ['What reporting webhooks are configured?', 'Is there a webhook for email events?'],
                            'search_strategy': 'Search by webhook name or endpoint URL',
                        },
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique webhook identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Webhook display name',
                    },
                    'endpoint': {
                        'type': ['null', 'string'],
                        'description': 'Webhook URL',
                    },
                    'disabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the webhook is disabled',
                    },
                    'full_resolution': {
                        'type': ['null', 'boolean'],
                        'description': 'Send all events, not just unique',
                    },
                    'with_content': {
                        'type': ['null', 'boolean'],
                        'description': 'Include message body in sent events',
                    },
                    'events': {
                        'type': ['null', 'array'],
                        'description': 'Event types to report',
                        'items': {'type': 'string'},
                    },
                },
                'x-airbyte-entity-name': 'reporting_webhooks',
                'x-airbyte-ai-hints': {
                    'summary': 'Webhook endpoints configured to receive message event notifications',
                    'when_to_use': 'Questions about webhook configuration, event reporting endpoints, or notification URLs',
                    'trigger_phrases': [
                        'reporting webhooks',
                        'webhook config',
                        'event notifications',
                        'webhook endpoints',
                    ],
                    'freshness': 'static',
                    'example_questions': ['What reporting webhooks are configured?', 'Is there a webhook for email events?'],
                    'search_strategy': 'Search by webhook name or endpoint URL',
                },
            },
            ai_hints={
                'summary': 'Webhook endpoints configured to receive message event notifications',
                'when_to_use': 'Questions about webhook configuration, event reporting endpoints, or notification URLs',
                'trigger_phrases': [
                    'reporting webhooks',
                    'webhook config',
                    'event notifications',
                    'webhook endpoints',
                ],
                'freshness': 'static',
                'example_questions': ['What reporting webhooks are configured?', 'Is there a webhook for email events?'],
                'search_strategy': 'Search by webhook name or endpoint URL',
            },
        ),
        EntityDefinition(
            name='exports',
            actions=[Action.LIST, Action.CREATE, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/exports',
                    action=Action.LIST,
                    description='Returns all exports in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'exports': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique export identifier',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Export type',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Export state (done, pending, in_progress)',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Export description',
                                        },
                                        'total': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of entries (0 until complete)',
                                        },
                                        'downloads': {
                                            'type': ['null', 'integer'],
                                            'description': 'Total download count',
                                        },
                                        'failed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the export failed',
                                        },
                                        'created_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'deduplicate_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Deduplication identifier',
                                        },
                                        'user_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'User who created the export',
                                        },
                                        'user_email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email of the user who created the export',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'exports',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Data export jobs for bulk downloading customer, delivery, or activity data',
                                        'when_to_use': 'Questions about data exports, bulk downloads, or export job status',
                                        'trigger_phrases': [
                                            'exports',
                                            'data export',
                                            'bulk download',
                                            'export status',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What exports have been created?', 'Are there any pending exports?', 'Show me the status of export 99'],
                                        'search_strategy': 'Filter by export type or status (done/pending/in_progress)',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.exports',
                    untested=True,
                    no_pagination='Returns all exports in a single response without pagination',
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/exports/customers',
                    action=Action.CREATE,
                    description='Triggers a new export of customer data. Use filters to select which customers to export.',
                    body_fields=['filters'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'filters': {'type': 'object', 'description': 'Audience filter conditions to select which customers to export. Uses boolean logic with "and", "or", "not" arrays of conditions, "segment" objects with an "id" field, and "attribute" objects with "field", "operator", and "value" fields. Example: {"and": [{"segment": {"id": 3}}, {"attribute": {"field": "plan", "operator": "eq", "value": "premium"}}]}\n'},
                        },
                        'required': ['filters'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'export': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique export identifier',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Export type',
                                    },
                                    'status': {
                                        'type': ['null', 'string'],
                                        'description': 'Export state (done, pending, in_progress)',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Export description',
                                    },
                                    'total': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of entries (0 until complete)',
                                    },
                                    'downloads': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total download count',
                                    },
                                    'failed': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the export failed',
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'user_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'User who created the export',
                                    },
                                    'user_email': {
                                        'type': ['null', 'string'],
                                        'description': 'Email of the user who created the export',
                                    },
                                },
                                'x-airbyte-entity-name': 'exports',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Data export jobs for bulk downloading customer, delivery, or activity data',
                                    'when_to_use': 'Questions about data exports, bulk downloads, or export job status',
                                    'trigger_phrases': [
                                        'exports',
                                        'data export',
                                        'bulk download',
                                        'export status',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What exports have been created?', 'Are there any pending exports?', 'Show me the status of export 99'],
                                    'search_strategy': 'Filter by export type or status (done/pending/in_progress)',
                                },
                            },
                        },
                    },
                    untested=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/exports/{export_id}',
                    action=Action.GET,
                    description='Returns a single export by ID.',
                    path_params=['export_id'],
                    path_params_schema={
                        'export_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'export': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique export identifier',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Export type',
                                    },
                                    'status': {
                                        'type': ['null', 'string'],
                                        'description': 'Export state (done, pending, in_progress)',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Export description',
                                    },
                                    'total': {
                                        'type': ['null', 'integer'],
                                        'description': 'Number of entries (0 until complete)',
                                    },
                                    'downloads': {
                                        'type': ['null', 'integer'],
                                        'description': 'Total download count',
                                    },
                                    'failed': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the export failed',
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'deduplicate_id': {
                                        'type': ['null', 'string'],
                                        'description': 'Deduplication identifier',
                                    },
                                    'user_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'User who created the export',
                                    },
                                    'user_email': {
                                        'type': ['null', 'string'],
                                        'description': 'Email of the user who created the export',
                                    },
                                },
                                'x-airbyte-entity-name': 'exports',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Data export jobs for bulk downloading customer, delivery, or activity data',
                                    'when_to_use': 'Questions about data exports, bulk downloads, or export job status',
                                    'trigger_phrases': [
                                        'exports',
                                        'data export',
                                        'bulk download',
                                        'export status',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What exports have been created?', 'Are there any pending exports?', 'Show me the status of export 99'],
                                    'search_strategy': 'Filter by export type or status (done/pending/in_progress)',
                                },
                            },
                        },
                    },
                    record_extractor='$.export',
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique export identifier',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Export type',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Export state (done, pending, in_progress)',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Export description',
                    },
                    'total': {
                        'type': ['null', 'integer'],
                        'description': 'Number of entries (0 until complete)',
                    },
                    'downloads': {
                        'type': ['null', 'integer'],
                        'description': 'Total download count',
                    },
                    'failed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the export failed',
                    },
                    'created_at': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'deduplicate_id': {
                        'type': ['null', 'string'],
                        'description': 'Deduplication identifier',
                    },
                    'user_id': {
                        'type': ['null', 'integer'],
                        'description': 'User who created the export',
                    },
                    'user_email': {
                        'type': ['null', 'string'],
                        'description': 'Email of the user who created the export',
                    },
                },
                'x-airbyte-entity-name': 'exports',
                'x-airbyte-ai-hints': {
                    'summary': 'Data export jobs for bulk downloading customer, delivery, or activity data',
                    'when_to_use': 'Questions about data exports, bulk downloads, or export job status',
                    'trigger_phrases': [
                        'exports',
                        'data export',
                        'bulk download',
                        'export status',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What exports have been created?', 'Are there any pending exports?', 'Show me the status of export 99'],
                    'search_strategy': 'Filter by export type or status (done/pending/in_progress)',
                },
            },
            ai_hints={
                'summary': 'Data export jobs for bulk downloading customer, delivery, or activity data',
                'when_to_use': 'Questions about data exports, bulk downloads, or export job status',
                'trigger_phrases': [
                    'exports',
                    'data export',
                    'bulk download',
                    'export status',
                ],
                'freshness': 'live',
                'example_questions': ['What exports have been created?', 'Are there any pending exports?', 'Show me the status of export 99'],
                'search_strategy': 'Filter by export type or status (done/pending/in_progress)',
            },
        ),
        EntityDefinition(
            name='transactional_messages',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/transactional',
                    action=Action.LIST,
                    description='Returns a list of all transactional message templates in the workspace.',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'messages': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique transactional message identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Transactional message template name',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description of the transactional message',
                                        },
                                        'send_to_unsubscribed': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to send to unsubscribed recipients',
                                        },
                                        'link_tracking': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether link tracking is enabled',
                                        },
                                        'open_tracking': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether open tracking is enabled',
                                        },
                                        'hide_message_body': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to hide the message body (disable message retention)',
                                        },
                                        'queue_drafts': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to queue messages as drafts instead of sending immediately',
                                        },
                                        'trigger_name': {
                                            'type': ['null', 'string'],
                                            'description': 'Trigger name used to reference this transactional message via API',
                                        },
                                        'created_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'transactional_messages',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Transactional message templates for sending one-to-one messages like receipts and password resets',
                                        'when_to_use': 'Questions about transactional message templates, their settings, or listing available templates',
                                        'trigger_phrases': [
                                            'transactional messages',
                                            'transactional templates',
                                            'email templates',
                                            'message templates',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What transactional message templates are configured?', 'Show me the details of transactional message 5', 'List all transactional templates'],
                                        'search_strategy': 'Search by template name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.messages',
                    no_pagination='Returns all transactional messages in a single response without pagination',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/v1/transactional/{transactional_id}',
                    action=Action.GET,
                    description='Returns a single transactional message template by ID.',
                    path_params=['transactional_id'],
                    path_params_schema={
                        'transactional_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'message': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique transactional message identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Transactional message template name',
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                        'description': 'Description of the transactional message',
                                    },
                                    'send_to_unsubscribed': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to send to unsubscribed recipients',
                                    },
                                    'link_tracking': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether link tracking is enabled',
                                    },
                                    'open_tracking': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether open tracking is enabled',
                                    },
                                    'hide_message_body': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to hide the message body (disable message retention)',
                                    },
                                    'queue_drafts': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to queue messages as drafts instead of sending immediately',
                                    },
                                    'trigger_name': {
                                        'type': ['null', 'string'],
                                        'description': 'Trigger name used to reference this transactional message via API',
                                    },
                                    'created_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                },
                                'x-airbyte-entity-name': 'transactional_messages',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Transactional message templates for sending one-to-one messages like receipts and password resets',
                                    'when_to_use': 'Questions about transactional message templates, their settings, or listing available templates',
                                    'trigger_phrases': [
                                        'transactional messages',
                                        'transactional templates',
                                        'email templates',
                                        'message templates',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What transactional message templates are configured?', 'Show me the details of transactional message 5', 'List all transactional templates'],
                                    'search_strategy': 'Search by template name',
                                },
                            },
                        },
                    },
                    record_extractor='$.message',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique transactional message identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Transactional message template name',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the transactional message',
                    },
                    'send_to_unsubscribed': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to send to unsubscribed recipients',
                    },
                    'link_tracking': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether link tracking is enabled',
                    },
                    'open_tracking': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether open tracking is enabled',
                    },
                    'hide_message_body': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to hide the message body (disable message retention)',
                    },
                    'queue_drafts': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to queue messages as drafts instead of sending immediately',
                    },
                    'trigger_name': {
                        'type': ['null', 'string'],
                        'description': 'Trigger name used to reference this transactional message via API',
                    },
                    'created_at': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated_at': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                },
                'x-airbyte-entity-name': 'transactional_messages',
                'x-airbyte-ai-hints': {
                    'summary': 'Transactional message templates for sending one-to-one messages like receipts and password resets',
                    'when_to_use': 'Questions about transactional message templates, their settings, or listing available templates',
                    'trigger_phrases': [
                        'transactional messages',
                        'transactional templates',
                        'email templates',
                        'message templates',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What transactional message templates are configured?', 'Show me the details of transactional message 5', 'List all transactional templates'],
                    'search_strategy': 'Search by template name',
                },
            },
            ai_hints={
                'summary': 'Transactional message templates for sending one-to-one messages like receipts and password resets',
                'when_to_use': 'Questions about transactional message templates, their settings, or listing available templates',
                'trigger_phrases': [
                    'transactional messages',
                    'transactional templates',
                    'email templates',
                    'message templates',
                ],
                'freshness': 'live',
                'example_questions': ['What transactional message templates are configured?', 'Show me the details of transactional message 5', 'List all transactional templates'],
                'search_strategy': 'Search by template name',
            },
        ),
        EntityDefinition(
            name='transactional_message_contents',
            actions=[Action.LIST, Action.UPDATE],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/v1/transactional/{transactional_id}/contents',
                    action=Action.LIST,
                    description='Returns all content variants (including language translations) for a transactional message template.',
                    path_params=['transactional_id'],
                    path_params_schema={
                        'transactional_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'contents': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Unique content variant identifier',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Content variant name',
                                        },
                                        'created': {
                                            'type': ['null', 'integer'],
                                            'description': 'Creation timestamp (Unix)',
                                        },
                                        'updated': {
                                            'type': ['null', 'integer'],
                                            'description': 'Last update timestamp (Unix)',
                                        },
                                        'body': {
                                            'type': ['null', 'string'],
                                            'description': 'HTML body content of the message',
                                        },
                                        'language': {
                                            'type': ['null', 'string'],
                                            'description': 'Language code for this variant (empty string for default language)',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Channel type (email or push)',
                                        },
                                        'from': {
                                            'type': ['null', 'string'],
                                            'description': 'Sender email address',
                                        },
                                        'from_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Sender identity ID',
                                        },
                                        'reply_to': {
                                            'type': ['null', 'string'],
                                            'description': 'Reply-to email address',
                                        },
                                        'reply_to_id': {
                                            'type': ['null', 'integer'],
                                            'description': 'Reply-to sender identity ID',
                                        },
                                        'preprocessor': {
                                            'type': ['null', 'string'],
                                            'description': 'CSS preprocessor setting (e.g. premailer)',
                                        },
                                        'recipient': {
                                            'type': ['null', 'string'],
                                            'description': 'Recipient expression (e.g. "{{customer.email}}")',
                                        },
                                        'subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Email subject line',
                                        },
                                        'bcc': {
                                            'type': ['null', 'string'],
                                            'description': 'BCC addresses',
                                        },
                                        'fake_bcc': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to use fake BCC',
                                        },
                                        'preheader_text': {
                                            'type': ['null', 'string'],
                                            'description': 'Email preheader/preview text',
                                        },
                                        'body_amp': {
                                            'type': ['null', 'string'],
                                            'description': 'AMP HTML body content',
                                        },
                                        'headers': {
                                            'type': ['null', 'string'],
                                            'description': 'Custom email headers as a JSON string',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'transactional_message_contents',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Content variants and language translations of transactional message templates',
                                        'when_to_use': 'Questions about the content, body, subject, or language variants of a transactional message template',
                                        'trigger_phrases': [
                                            'transactional content',
                                            'template content',
                                            'template variants',
                                            'message body',
                                            'language variant',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show me the content of transactional message 3', 'What language variants exist for template 5?', 'Update the subject of transactional template content 139'],
                                        'search_strategy': 'Access via parent transactional message ID',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.contents',
                    no_pagination='Returns all content variants in a single response without pagination',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PUT',
                    path='/v1/transactional/{transactional_id}/content/{content_id}',
                    action=Action.UPDATE,
                    description='Updates the content of a specific variant of a transactional message template by content ID.',
                    body_fields=[
                        'body',
                        'from_id',
                        'reply_to_id',
                        'recipient',
                        'subject',
                        'preheader_text',
                        'body_amp',
                        'headers',
                    ],
                    path_params=['transactional_id', 'content_id'],
                    path_params_schema={
                        'transactional_id': {'type': 'integer', 'required': True},
                        'content_id': {'type': 'integer', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'body': {'type': 'string', 'description': 'HTML body content of the message'},
                            'from_id': {'type': 'integer', 'description': 'Sender identity ID'},
                            'reply_to_id': {
                                'type': ['integer', 'null'],
                                'description': 'Reply-to sender identity ID',
                            },
                            'recipient': {'type': 'string', 'description': 'Recipient expression (e.g. "{{customer.email}}")'},
                            'subject': {'type': 'string', 'description': 'Email subject line'},
                            'preheader_text': {'type': 'string', 'description': 'Email preheader/preview text'},
                            'body_amp': {'type': 'string', 'description': 'AMP HTML body content'},
                            'headers': {
                                'type': 'array',
                                'description': 'Custom email headers as an array of name-value objects',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'Header name'},
                                        'value': {'type': 'string', 'description': 'Header value'},
                                    },
                                },
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'content': {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Unique content variant identifier',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Content variant name',
                                    },
                                    'created': {
                                        'type': ['null', 'integer'],
                                        'description': 'Creation timestamp (Unix)',
                                    },
                                    'updated': {
                                        'type': ['null', 'integer'],
                                        'description': 'Last update timestamp (Unix)',
                                    },
                                    'body': {
                                        'type': ['null', 'string'],
                                        'description': 'HTML body content of the message',
                                    },
                                    'language': {
                                        'type': ['null', 'string'],
                                        'description': 'Language code for this variant (empty string for default language)',
                                    },
                                    'type': {
                                        'type': ['null', 'string'],
                                        'description': 'Channel type (email or push)',
                                    },
                                    'from': {
                                        'type': ['null', 'string'],
                                        'description': 'Sender email address',
                                    },
                                    'from_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Sender identity ID',
                                    },
                                    'reply_to': {
                                        'type': ['null', 'string'],
                                        'description': 'Reply-to email address',
                                    },
                                    'reply_to_id': {
                                        'type': ['null', 'integer'],
                                        'description': 'Reply-to sender identity ID',
                                    },
                                    'preprocessor': {
                                        'type': ['null', 'string'],
                                        'description': 'CSS preprocessor setting (e.g. premailer)',
                                    },
                                    'recipient': {
                                        'type': ['null', 'string'],
                                        'description': 'Recipient expression (e.g. "{{customer.email}}")',
                                    },
                                    'subject': {
                                        'type': ['null', 'string'],
                                        'description': 'Email subject line',
                                    },
                                    'bcc': {
                                        'type': ['null', 'string'],
                                        'description': 'BCC addresses',
                                    },
                                    'fake_bcc': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether to use fake BCC',
                                    },
                                    'preheader_text': {
                                        'type': ['null', 'string'],
                                        'description': 'Email preheader/preview text',
                                    },
                                    'body_amp': {
                                        'type': ['null', 'string'],
                                        'description': 'AMP HTML body content',
                                    },
                                    'headers': {
                                        'type': ['null', 'string'],
                                        'description': 'Custom email headers as a JSON string',
                                    },
                                },
                                'x-airbyte-entity-name': 'transactional_message_contents',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Content variants and language translations of transactional message templates',
                                    'when_to_use': 'Questions about the content, body, subject, or language variants of a transactional message template',
                                    'trigger_phrases': [
                                        'transactional content',
                                        'template content',
                                        'template variants',
                                        'message body',
                                        'language variant',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Show me the content of transactional message 3', 'What language variants exist for template 5?', 'Update the subject of transactional template content 139'],
                                    'search_strategy': 'Access via parent transactional message ID',
                                },
                            },
                        },
                    },
                    record_extractor='$.content',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {
                        'type': ['null', 'integer'],
                        'description': 'Unique content variant identifier',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Content variant name',
                    },
                    'created': {
                        'type': ['null', 'integer'],
                        'description': 'Creation timestamp (Unix)',
                    },
                    'updated': {
                        'type': ['null', 'integer'],
                        'description': 'Last update timestamp (Unix)',
                    },
                    'body': {
                        'type': ['null', 'string'],
                        'description': 'HTML body content of the message',
                    },
                    'language': {
                        'type': ['null', 'string'],
                        'description': 'Language code for this variant (empty string for default language)',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Channel type (email or push)',
                    },
                    'from': {
                        'type': ['null', 'string'],
                        'description': 'Sender email address',
                    },
                    'from_id': {
                        'type': ['null', 'integer'],
                        'description': 'Sender identity ID',
                    },
                    'reply_to': {
                        'type': ['null', 'string'],
                        'description': 'Reply-to email address',
                    },
                    'reply_to_id': {
                        'type': ['null', 'integer'],
                        'description': 'Reply-to sender identity ID',
                    },
                    'preprocessor': {
                        'type': ['null', 'string'],
                        'description': 'CSS preprocessor setting (e.g. premailer)',
                    },
                    'recipient': {
                        'type': ['null', 'string'],
                        'description': 'Recipient expression (e.g. "{{customer.email}}")',
                    },
                    'subject': {
                        'type': ['null', 'string'],
                        'description': 'Email subject line',
                    },
                    'bcc': {
                        'type': ['null', 'string'],
                        'description': 'BCC addresses',
                    },
                    'fake_bcc': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to use fake BCC',
                    },
                    'preheader_text': {
                        'type': ['null', 'string'],
                        'description': 'Email preheader/preview text',
                    },
                    'body_amp': {
                        'type': ['null', 'string'],
                        'description': 'AMP HTML body content',
                    },
                    'headers': {
                        'type': ['null', 'string'],
                        'description': 'Custom email headers as a JSON string',
                    },
                },
                'x-airbyte-entity-name': 'transactional_message_contents',
                'x-airbyte-ai-hints': {
                    'summary': 'Content variants and language translations of transactional message templates',
                    'when_to_use': 'Questions about the content, body, subject, or language variants of a transactional message template',
                    'trigger_phrases': [
                        'transactional content',
                        'template content',
                        'template variants',
                        'message body',
                        'language variant',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show me the content of transactional message 3', 'What language variants exist for template 5?', 'Update the subject of transactional template content 139'],
                    'search_strategy': 'Access via parent transactional message ID',
                },
            },
            ai_hints={
                'summary': 'Content variants and language translations of transactional message templates',
                'when_to_use': 'Questions about the content, body, subject, or language variants of a transactional message template',
                'trigger_phrases': [
                    'transactional content',
                    'template content',
                    'template variants',
                    'message body',
                    'language variant',
                ],
                'freshness': 'live',
                'example_questions': ['Show me the content of transactional message 3', 'What language variants exist for template 5?', 'Update the subject of transactional template content 139'],
                'search_strategy': 'Access via parent transactional message ID',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='transactional_message_contents',
                    target_entity='transactional_messages',
                    foreign_key='transactional_id',
                    cardinality='many_to_one',
                    description='Scoping-only relationship: transactional_id is a required path parameter for contents endpoints, not a field on emitted records. Declares how to resolve the parent transactional message for per-entity health checks.\n',
                ),
            ],
        ),
        EntityDefinition(
            name='transactional_email',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/send/email',
                    action=Action.CREATE,
                    description='Sends a transactional email to a single recipient. Can use a pre-built template (via transactional_message_id) or provide inline content (subject, body, from). Creates the recipient profile if it does not already exist.\n',
                    body_fields=[
                        'transactional_message_id',
                        'to',
                        'identifiers',
                        'message_data',
                        'from',
                        'subject',
                        'body',
                        'body_plain',
                        'reply_to',
                        'bcc',
                        'headers',
                        'preheader_text',
                        'attachments',
                        'disable_message_retention',
                        'send_to_unsubscribed',
                        'tracked',
                        'queue_draft',
                        'send_at',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'transactional_message_id': {
                                'type': ['integer', 'string'],
                                'description': 'Template ID (number) or trigger name (string). Required if not providing inline body/subject/from.',
                            },
                            'to': {'type': 'string', 'description': 'Recipient email address. Supports display name format: "Name <email>"'},
                            'identifiers': {'type': 'object', 'description': 'Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}'},
                            'message_data': {'type': 'object', 'description': 'Key-value pairs available as {{trigger.<key>}} in templates'},
                            'from': {'type': 'string', 'description': 'Sender address (must be verified domain). Overrides template if provided.'},
                            'subject': {'type': 'string', 'description': 'Email subject line. Overrides template if provided.'},
                            'body': {'type': 'string', 'description': 'HTML email body. Overrides template if provided.'},
                            'body_plain': {'type': 'string', 'description': 'Plaintext email body'},
                            'reply_to': {'type': 'string', 'description': 'Reply-to email address'},
                            'bcc': {'type': 'string', 'description': 'BCC address(es), comma-separated. Max 15 total recipients.'},
                            'headers': {'type': 'object', 'description': 'Custom email headers (ASCII only)'},
                            'preheader_text': {'type': 'string', 'description': 'Email preview text'},
                            'attachments': {'type': 'object', 'description': 'Map of filename to base64 content: {"file.pdf": "<base64>"}. Max 2MB total.'},
                            'disable_message_retention': {'type': 'boolean', 'description': 'Do not store message body (for sensitive data)'},
                            'send_to_unsubscribed': {'type': 'boolean', 'description': 'Send even if person is unsubscribed'},
                            'tracked': {'type': 'boolean', 'description': 'Enable open and click tracking'},
                            'queue_draft': {'type': 'boolean', 'description': 'Queue as draft instead of sending immediately'},
                            'send_at': {'type': 'integer', 'description': 'Unix timestamp for scheduled delivery (up to 90 days in the future)'},
                        },
                        'required': ['to', 'identifiers'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'delivery_id': {
                                'type': ['null', 'string'],
                                'description': 'Unique delivery identifier for tracking the message',
                            },
                            'queued_at': {
                                'type': ['null', 'integer'],
                                'description': 'Unix timestamp when the message was queued',
                            },
                        },
                    },
                    untested=True,
                    ai_hints={
                        'summary': 'Send a one-to-one transactional email (order confirmations, password resets, etc.)',
                        'when_to_use': 'When the user wants to send a single transactional email to a specific person',
                        'trigger_phrases': ['send email', 'transactional email', 'send notification email'],
                    },
                ),
            },
        ),
        EntityDefinition(
            name='transactional_sms',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/send/sms',
                    action=Action.CREATE,
                    description='Sends a transactional SMS to a single recipient. Always requires a pre-built template (transactional_message_id). Requires Twilio integration to be configured in the workspace.\n',
                    body_fields=[
                        'transactional_message_id',
                        'to',
                        'identifiers',
                        'message_data',
                        'from',
                        'send_to_unsubscribed',
                        'tracked',
                        'queue_draft',
                        'disable_message_retention',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'transactional_message_id': {
                                'type': ['integer', 'string'],
                                'description': 'Template ID (number) or trigger name (string). Always required for SMS.',
                            },
                            'to': {'type': 'string', 'description': 'Phone number in E.164 format (e.g. +15551234567)'},
                            'identifiers': {'type': 'object', 'description': 'Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}'},
                            'message_data': {'type': 'object', 'description': 'Key-value pairs available as {{trigger.<key>}} in templates'},
                            'from': {'type': 'string', 'description': 'Override sender phone number (must be verified in Twilio)'},
                            'send_to_unsubscribed': {'type': 'boolean', 'description': 'Send even if person is unsubscribed'},
                            'tracked': {'type': 'boolean', 'description': 'Enable link tracking'},
                            'queue_draft': {'type': 'boolean', 'description': 'Queue as draft instead of sending immediately'},
                            'disable_message_retention': {'type': 'boolean', 'description': 'Do not store message content'},
                        },
                        'required': ['transactional_message_id', 'to', 'identifiers'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'delivery_id': {
                                'type': ['null', 'string'],
                                'description': 'Unique delivery identifier for tracking the message',
                            },
                            'queued_at': {
                                'type': ['null', 'integer'],
                                'description': 'Unix timestamp when the message was queued',
                            },
                        },
                    },
                    untested=True,
                    ai_hints={
                        'summary': 'Send a one-to-one transactional SMS via Twilio',
                        'when_to_use': 'When the user wants to send a single SMS to a specific person',
                        'trigger_phrases': ['send sms', 'send text message', 'transactional sms'],
                    },
                ),
            },
        ),
        EntityDefinition(
            name='transactional_push',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/send/push',
                    action=Action.CREATE,
                    description='Sends a transactional push notification to a single recipient. Can use a template or provide inline title and message. Requires push notifications to be configured in the workspace.\n',
                    body_fields=[
                        'transactional_message_id',
                        'to',
                        'identifiers',
                        'message_data',
                        'title',
                        'message',
                        'link',
                        'image_url',
                        'custom_data',
                        'custom_payload',
                        'sound',
                        'send_to_unsubscribed',
                        'queue_draft',
                        'disable_message_retention',
                        'send_at',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'transactional_message_id': {
                                'type': ['integer', 'string'],
                                'description': 'Template ID or trigger name. Required if not providing inline title/message.',
                            },
                            'to': {'type': 'string', 'description': 'Device target: "last_used" for most recent device, or a specific device token. Defaults to all devices.'},
                            'identifiers': {'type': 'object', 'description': 'Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}'},
                            'message_data': {'type': 'object', 'description': 'Key-value pairs available as {{trigger.<key>}} in templates'},
                            'title': {'type': 'string', 'description': 'Push notification title (overrides template)'},
                            'message': {'type': 'string', 'description': 'Push notification body (overrides template)'},
                            'link': {'type': 'string', 'description': 'Deep link URL'},
                            'image_url': {'type': 'string', 'description': 'Image URL to display in the notification'},
                            'custom_data': {'type': 'object', 'description': 'Custom key-value data included in the push payload'},
                            'custom_payload': {'type': 'object', 'description': 'Platform-specific payload overrides (iOS/Android)'},
                            'sound': {'type': 'string', 'description': 'Notification sound name'},
                            'send_to_unsubscribed': {'type': 'boolean', 'description': 'Send even if person is unsubscribed'},
                            'queue_draft': {'type': 'boolean', 'description': 'Queue as draft instead of sending immediately'},
                            'disable_message_retention': {'type': 'boolean', 'description': 'Do not store message content'},
                            'send_at': {'type': 'integer', 'description': 'Unix timestamp for scheduled delivery'},
                        },
                        'required': ['identifiers'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'delivery_id': {
                                'type': ['null', 'string'],
                                'description': 'Unique delivery identifier for tracking the message',
                            },
                            'queued_at': {
                                'type': ['null', 'integer'],
                                'description': 'Unix timestamp when the message was queued',
                            },
                        },
                    },
                    untested=True,
                    ai_hints={
                        'summary': 'Send a one-to-one transactional push notification to mobile or web',
                        'when_to_use': 'When the user wants to send a push notification to a specific person',
                        'trigger_phrases': ['send push', 'push notification', 'send mobile notification'],
                    },
                ),
            },
        ),
        EntityDefinition(
            name='transactional_inbox_message',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/send/inbox_message',
                    action=Action.CREATE,
                    description="Sends a transactional in-app inbox message to a single recipient. Always requires a pre-built Inbox-type transactional message template (transactional_message_id). Messages appear in the recipient's notification inbox via the Customer.io SDK.\n",
                    body_fields=['transactional_message_id', 'identifiers', 'message_data'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'transactional_message_id': {
                                'type': ['integer', 'string'],
                                'description': 'Template ID or trigger name. Must reference an Inbox-type transactional message.',
                            },
                            'identifiers': {'type': 'object', 'description': 'Recipient identity. One of: {"id": "..."}, {"email": "..."}, or {"cio_id": "..."}'},
                            'message_data': {'type': 'object', 'description': 'Key-value pairs available as {{trigger.<key>}} in the inbox message template'},
                        },
                        'required': ['transactional_message_id', 'identifiers'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'delivery_id': {
                                'type': ['null', 'string'],
                                'description': 'Unique delivery identifier for tracking the message',
                            },
                            'queued_at': {
                                'type': ['null', 'integer'],
                                'description': 'Unix timestamp when the message was queued',
                            },
                        },
                    },
                    untested=True,
                    ai_hints={
                        'summary': "Send an in-app inbox message to a user's notification center",
                        'when_to_use': 'When the user wants to send an in-app notification via the Customer.io SDK inbox',
                        'trigger_phrases': ['send inbox message', 'in-app message', 'inbox notification'],
                    },
                ),
            },
        ),
        EntityDefinition(
            name='broadcast_trigger',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/v1/campaigns/{campaign_id}/triggers',
                    action=Action.CREATE,
                    description='Triggers an API-triggered broadcast campaign. The broadcast must be configured as API-triggered in the Customer.io UI. Cannot be triggered more than once every 10 seconds, with a maximum of 5 queued broadcasts per campaign. Recipients must already exist in the workspace.\n',
                    body_fields=[
                        'data',
                        'recipients',
                        'ids',
                        'emails',
                        'per_user_data',
                        'data_file_url',
                        'id_ignore_missing',
                        'email_ignore_missing',
                        'email_add_duplicates',
                    ],
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'integer', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'data': {'type': 'object', 'description': 'Global data available as {{trigger.<key>}} in broadcast messages'},
                            'recipients': {'type': 'object', 'description': 'Filter object to define audience (overrides UI-defined recipients). Supports and/or/not/segment/attribute conditions.'},
                            'ids': {
                                'type': 'array',
                                'description': 'List of profile IDs to target (max 10,000)',
                                'items': {'type': 'string'},
                            },
                            'emails': {
                                'type': 'array',
                                'description': 'List of email addresses to target (max 10,000)',
                                'items': {'type': 'string'},
                            },
                            'per_user_data': {
                                'type': 'array',
                                'description': 'Per-recipient custom data: [{"id": "user1", "data": {...}}, ...]',
                                'items': {'type': 'object'},
                            },
                            'data_file_url': {'type': 'string', 'description': 'URL to a JSON Lines file with per-user data'},
                            'id_ignore_missing': {'type': 'boolean', 'description': 'Ignore IDs that do not match existing profiles (default false)'},
                            'email_ignore_missing': {'type': 'boolean', 'description': 'Ignore emails that do not match existing profiles'},
                            'email_add_duplicates': {'type': 'boolean', 'description': 'Send to all profiles sharing an email address'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': ['null', 'integer'],
                                'description': 'Trigger ID for checking broadcast status',
                            },
                        },
                    },
                    untested=True,
                    ai_hints={
                        'summary': 'Trigger an API-triggered broadcast campaign to send messages to a group of people',
                        'when_to_use': 'When the user wants to trigger or fire a broadcast campaign via the API',
                        'trigger_phrases': ['trigger broadcast', 'fire broadcast', 'send broadcast'],
                    },
                ),
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='campaigns',
                suggested=True,
                x_airbyte_name='campaigns',
                fields=[
                    CacheFieldConfig(
                        name='actions',
                        type=['null', 'array'],
                        description='Actions defined in this campaign',
                    ),
                    CacheFieldConfig(
                        name='active',
                        type=['null', 'boolean'],
                        description='Whether the campaign is active',
                    ),
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Creation timestamp (Unix)',
                    ),
                    CacheFieldConfig(
                        name='created_by',
                        type=['null', 'string'],
                        description='Who created the campaign',
                    ),
                    CacheFieldConfig(
                        name='date_attribute',
                        type=['null', 'string'],
                        description='Date attribute used for date-triggered campaigns',
                    ),
                    CacheFieldConfig(
                        name='deduplicate_id',
                        type=['null', 'string'],
                        description='Deduplication identifier',
                    ),
                    CacheFieldConfig(
                        name='event_name',
                        type=['null', 'string'],
                        description='Event name that triggers the campaign',
                    ),
                    CacheFieldConfig(
                        name='first_started',
                        type=['null', 'integer'],
                        description='When the campaign was first started (Unix)',
                    ),
                    CacheFieldConfig(
                        name='frequency',
                        type=['null', 'string'],
                        description='How frequently a person can receive this campaign',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique campaign identifier',
                    ),
                    CacheFieldConfig(
                        name='msg_templates',
                        type=['null', 'array'],
                        description='Message templates used in the campaign',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Campaign name',
                    ),
                    CacheFieldConfig(
                        name='start_hour',
                        type=['null', 'integer'],
                        description='Hour of the day to trigger',
                    ),
                    CacheFieldConfig(
                        name='start_minutes',
                        type=['null', 'integer'],
                        description='Minute of the hour to trigger',
                    ),
                    CacheFieldConfig(
                        name='state',
                        type=['null', 'string'],
                        description='Campaign status (draft, active, stopped)',
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['null', 'array'],
                        description='Tags associated with the campaign',
                    ),
                    CacheFieldConfig(
                        name='timezone',
                        type=['null', 'string'],
                        description='Timezone for trigger scheduling',
                    ),
                    CacheFieldConfig(
                        name='trigger_segment_ids',
                        type=['null', 'array'],
                        description='Segment IDs that trigger this campaign',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Campaign trigger type',
                    ),
                    CacheFieldConfig(
                        name='updated',
                        type=['null', 'integer'],
                        description='Last update timestamp (Unix)',
                    ),
                    CacheFieldConfig(
                        name='use_customer_timezone',
                        type=['null', 'boolean'],
                        description="Whether to use the customer's timezone",
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='campaign_actions',
                suggested=True,
                x_airbyte_name='campaigns_actions',
                fields=[
                    CacheFieldConfig(
                        name='bcc',
                        type=['null', 'string'],
                        description='BCC addresses',
                    ),
                    CacheFieldConfig(
                        name='body',
                        type=['null', 'string'],
                        description='Action body content (HTML for emails)',
                    ),
                    CacheFieldConfig(
                        name='campaign_id',
                        type=['null', 'integer'],
                        description='Parent campaign ID',
                    ),
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Creation timestamp (Unix)',
                    ),
                    CacheFieldConfig(
                        name='deduplicate_id',
                        type=['null', 'string'],
                        description='Deduplication identifier',
                    ),
                    CacheFieldConfig(
                        name='editor',
                        type=['null', 'string'],
                        description='Editor used to create the action',
                    ),
                    CacheFieldConfig(
                        name='fake_bcc',
                        type=['null', 'boolean'],
                        description='Whether to use fake BCC',
                    ),
                    CacheFieldConfig(
                        name='from',
                        type=['null', 'string'],
                        description='From address',
                    ),
                    CacheFieldConfig(
                        name='from_id',
                        type=['null', 'string'],
                        description='Sender identity ID',
                    ),
                    CacheFieldConfig(
                        name='headers',
                        type=['null', 'string'],
                        description='Custom email headers as JSON',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique action identifier',
                    ),
                    CacheFieldConfig(
                        name='language',
                        type=['null', 'string'],
                        description='Language variant',
                    ),
                    CacheFieldConfig(
                        name='layout',
                        type=['null', 'string'],
                        description='Layout template used',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Action name',
                    ),
                    CacheFieldConfig(
                        name='parent_action_id',
                        type=['null', 'integer'],
                        description='Parent action ID for language variants',
                    ),
                    CacheFieldConfig(
                        name='preheader_text',
                        type=['null', 'string'],
                        description='Email preheader/preview text',
                    ),
                    CacheFieldConfig(
                        name='preprocessor',
                        type=['null', 'string'],
                        description='CSS preprocessor setting',
                    ),
                    CacheFieldConfig(
                        name='recipient',
                        type=['null', 'string'],
                        description='Recipient address',
                    ),
                    CacheFieldConfig(
                        name='recipient_environment_id',
                        type=['null', 'integer'],
                        description='Recipient environment ID',
                    ),
                    CacheFieldConfig(
                        name='reply_to',
                        type=['null', 'string'],
                        description='Reply-to address',
                    ),
                    CacheFieldConfig(
                        name='reply_to_id',
                        type=['null', 'string'],
                        description='Reply-to sender identity ID',
                    ),
                    CacheFieldConfig(
                        name='request_method',
                        type=['null', 'string'],
                        description='HTTP request method for webhook actions',
                    ),
                    CacheFieldConfig(
                        name='sending_state',
                        type=['null', 'string'],
                        description='Sending behavior (automatic or draft)',
                    ),
                    CacheFieldConfig(
                        name='subject',
                        type=['null', 'string'],
                        description='Email subject line',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Action type (email, webhook, twilio, push, slack, in_app, whatsapp)',
                    ),
                    CacheFieldConfig(
                        name='updated',
                        type=['null', 'integer'],
                        description='Last update timestamp (Unix)',
                    ),
                    CacheFieldConfig(
                        name='url',
                        type=['null', 'string'],
                        description='Webhook URL (for webhook actions)',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='newsletters',
                suggested=True,
                x_airbyte_name='newsletters',
                fields=[
                    CacheFieldConfig(
                        name='content_ids',
                        type=['null', 'array'],
                        description='Content variant IDs for this newsletter',
                    ),
                    CacheFieldConfig(
                        name='created',
                        type=['null', 'integer'],
                        description='Creation timestamp (Unix)',
                    ),
                    CacheFieldConfig(
                        name='deduplicate_id',
                        type=['null', 'string'],
                        description='Deduplication identifier',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Unique newsletter identifier',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Newsletter name',
                    ),
                    CacheFieldConfig(
                        name='sent_at',
                        type=['null', 'integer'],
                        description='When the newsletter was last sent (Unix)',
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['null', 'array'],
                        description='Tags associated with the newsletter',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Channel type (email, webhook, twilio, push, in_app, inbox)',
                    ),
                    CacheFieldConfig(
                        name='updated',
                        type=['null', 'integer'],
                        description='Last update timestamp (Unix)',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'campaigns': [
            'actions',
            'actions[]',
            'active',
            'created',
            'created_by',
            'date_attribute',
            'deduplicate_id',
            'event_name',
            'first_started',
            'frequency',
            'id',
            'msg_templates',
            'msg_templates[]',
            'name',
            'start_hour',
            'start_minutes',
            'state',
            'tags',
            'tags[]',
            'timezone',
            'trigger_segment_ids',
            'trigger_segment_ids[]',
            'type',
            'updated',
            'use_customer_timezone',
        ],
        'campaign_actions': [
            'bcc',
            'body',
            'campaign_id',
            'created',
            'deduplicate_id',
            'editor',
            'fake_bcc',
            'from',
            'from_id',
            'headers',
            'id',
            'language',
            'layout',
            'name',
            'parent_action_id',
            'preheader_text',
            'preprocessor',
            'recipient',
            'recipient_environment_id',
            'reply_to',
            'reply_to_id',
            'request_method',
            'sending_state',
            'subject',
            'type',
            'updated',
            'url',
        ],
        'newsletters': [
            'content_ids',
            'content_ids[]',
            'created',
            'deduplicate_id',
            'id',
            'name',
            'sent_at',
            'tags',
            'tags[]',
            'type',
            'updated',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all campaigns in Customer.io',
            'Show me all newsletters',
            'What segments are defined in my workspace?',
            'Get the details of campaign 42',
            'List all sender identities',
            'Show me all reporting webhooks',
            'What snippets do we have?',
            'List all collections',
            'Show recent activities',
            "Create a snippet called 'footer' with content '<p>Thanks!</p>'",
            "Update the snippet 'header' to say 'Welcome back!'",
            "Create a new collection called 'products'",
            'Create a reporting webhook for email events',
            "Create a manual segment called 'VIP Customers'",
            'Export all customers matching a segment',
            'Send a transactional email to user@example.com',
            'Send an SMS notification to +15551234567',
            'Send a push notification to user 123',
            'Trigger broadcast campaign 42',
            'List all transactional message templates',
            'Get the details of transactional message 5',
            'Show the content variants of transactional template 3',
            'Update the subject of transactional content 139 in template 3',
        ],
        context_store_search=[
            'Which campaigns are currently active?',
            'Find newsletters sent in the last month',
            'What are the most recent email deliveries?',
            'Which exports have completed?',
        ],
        search=[
            'Which campaigns are currently active?',
            'Find newsletters sent in the last month',
            'What are the most recent email deliveries?',
            'Which exports have completed?',
        ],
        unsupported=[
            'Create a new campaign',
            'Delete a segment',
            'Delete a snippet',
            'Delete a collection',
            'Delete a reporting webhook',
            'Delete a newsletter',
            'Send a newsletter via API',
            'Schedule a newsletter via API',
        ],
    ),
)