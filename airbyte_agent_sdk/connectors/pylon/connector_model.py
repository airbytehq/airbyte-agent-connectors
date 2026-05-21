"""
Connector model for pylon.

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
from airbyte_agent_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

PylonConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('f2e53e88-3c6b-4e5a-b7c2-a1d9c5e8f4b6'),
    name='pylon',
    version='0.1.10',
    base_url='https://api.usepylon.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AuthConfigSpec(
            title='API Token Authentication',
            type='object',
            required=['api_token'],
            properties={
                'api_token': AuthConfigFieldSpec(
                    title='API Token',
                    description='Your Pylon API token. Only admin users can create API tokens.',
                ),
            },
            auth_mapping={'token': '${api_token}'},
            replication_auth_key_mapping={'api_token': 'api_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='issues',
            stream_name='issues',
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
                    path='/issues',
                    action=Action.LIST,
                    description='Get a list of issues within a time range',
                    query_params=['start_time', 'end_time', 'cursor'],
                    query_params_schema={
                        'start_time': {
                            'type': 'string',
                            'required': True,
                            'default': '2024-01-01T00:00:00Z',
                            'format': 'date-time',
                        },
                        'end_time': {
                            'type': 'string',
                            'required': True,
                            'default': '2099-12-31T23:59:59Z',
                            'format': 'date-time',
                        },
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the issue'},
                                        'account': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the account',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'assignee': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email of the user',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'attachment_urls': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'The attachment URLs attached to this issue',
                                        },
                                        'author_unverified': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether any message on the issue has an unverified author identity',
                                        },
                                        'body_html': {
                                            'type': ['string', 'null'],
                                            'description': 'The body of the issue in HTML format',
                                        },
                                        'business_hours_first_response_seconds': {
                                            'type': ['integer', 'null'],
                                            'description': 'Business hours time in seconds for first response',
                                        },
                                        'business_hours_resolution_seconds': {
                                            'type': ['integer', 'null'],
                                            'description': 'Business hours time in seconds for resolution',
                                        },
                                        'business_hours_time_in_status_seconds': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {'type': 'integer'},
                                            'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                                        },
                                        'chat_widget_info': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'page_url': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The URL of the page the user was on when starting the chat widget issue',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'description': 'The time the issue was created',
                                        },
                                        'csat_responses': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'comment': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The comment of the CSAT response',
                                                    },
                                                    'score': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'The score of the CSAT response',
                                                    },
                                                },
                                            },
                                            'description': 'The CSAT responses of the issue',
                                        },
                                        'custom_fields': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {
                                                'type': 'object',
                                                'properties': {
                                                    'slug': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The slug of the custom field',
                                                    },
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The value of the custom field',
                                                    },
                                                    'values': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                        'description': 'The values for multi-valued custom fields',
                                                    },
                                                },
                                            },
                                            'description': 'Custom field values associated with the issue',
                                        },
                                        'customer_portal_visible': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the issue is visible in the customer portal',
                                        },
                                        'external_issues': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'external_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The external ID of the external issue',
                                                    },
                                                    'link': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Link to the product issue',
                                                    },
                                                    'source': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The source of the external issue',
                                                    },
                                                },
                                            },
                                            'description': 'The external issues associated with the issue',
                                        },
                                        'first_response_seconds': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time in seconds for first response',
                                        },
                                        'first_response_time': {
                                            'type': ['string', 'null'],
                                            'description': 'The time of the first response',
                                        },
                                        'latest_message_time': {
                                            'type': ['string', 'null'],
                                            'description': 'The time of the latest message in the issue',
                                        },
                                        'link': {
                                            'type': ['string', 'null'],
                                            'description': 'The link to the issue in Pylon',
                                        },
                                        'number': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of the issue',
                                        },
                                        'number_of_touches': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of times the issue has been touched',
                                        },
                                        'requester': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email of the contact',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the contact',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'resolution_seconds': {
                                            'type': ['integer', 'null'],
                                            'description': 'Time in seconds for resolution',
                                        },
                                        'resolution_time': {
                                            'type': ['string', 'null'],
                                            'description': 'The time of the resolution',
                                        },
                                        'slack': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'channel_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The Slack channel ID associated with the issue',
                                                        },
                                                        'message_ts': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The root message ID of Slack message that started issue',
                                                        },
                                                        'workspace_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The Slack workspace ID associated with the issue',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'snoozed_until_time': {
                                            'type': ['string', 'null'],
                                            'description': 'The time the issue was snoozed until',
                                        },
                                        'source': {
                                            'oneOf': [
                                                {
                                                    'type': 'string',
                                                    'enum': [
                                                        'slack',
                                                        'microsoft_teams',
                                                        'microsoft_teams_chat',
                                                        'chat_widget',
                                                        'email',
                                                        'manual',
                                                        'form',
                                                        'discord',
                                                        'whatsapp',
                                                        'sms',
                                                        'telegram',
                                                    ],
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'state': {
                                            'type': ['string', 'null'],
                                            'description': 'The state of the issue',
                                        },
                                        'tags': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Tags associated with the issue',
                                        },
                                        'team': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the team',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'The title of the issue',
                                        },
                                        'time_in_status_seconds': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': {'type': 'integer'},
                                            'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                                        },
                                        'type': {
                                            'oneOf': [
                                                {
                                                    'type': 'string',
                                                    'enum': ['conversation', 'ticket'],
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'description': 'The time the issue was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'issues',
                                    'x-airbyte-stream-name': 'issues',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Customer support threads, open issues, response timelines, and who replied',
                                        'when_to_use': 'Support issue or customer response questions',
                                        'trigger_phrases': [
                                            'did they get back',
                                            'support issue',
                                            'ticket for',
                                            'open issues',
                                            'did someone follow up',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                                        'search_strategy': 'Search by title. If no results, try resolving by account name.',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/issues',
                    action=Action.CREATE,
                    description='Create a new issue',
                    body_fields=[
                        'title',
                        'body_html',
                        'priority',
                        'requester_email',
                        'requester_name',
                        'account_id',
                        'assignee_id',
                        'team_id',
                        'tags',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the issue'},
                            'body_html': {'type': 'string', 'description': 'The HTML content of the body of the issue'},
                            'priority': {'type': 'string', 'description': 'The priority of the issue (urgent, high, medium, low)'},
                            'requester_email': {'type': 'string', 'description': 'The email of the requester'},
                            'requester_name': {'type': 'string', 'description': 'The full name of the requester'},
                            'account_id': {'type': 'string', 'description': 'The account that this issue belongs to'},
                            'assignee_id': {'type': 'string', 'description': 'The user the issue should be assigned to'},
                            'team_id': {'type': 'string', 'description': 'The ID of the team this issue should be assigned to'},
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Tags to associate with the issue',
                            },
                        },
                        'required': ['title', 'body_html'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the issue'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'assignee': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'attachment_urls': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The attachment URLs attached to this issue',
                                    },
                                    'author_unverified': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether any message on the issue has an unverified author identity',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body of the issue in HTML format',
                                    },
                                    'business_hours_first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for first response',
                                    },
                                    'business_hours_resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for resolution',
                                    },
                                    'business_hours_time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                                    },
                                    'chat_widget_info': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'page_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The URL of the page the user was on when starting the chat widget issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was created',
                                    },
                                    'csat_responses': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'comment': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The comment of the CSAT response',
                                                },
                                                'score': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The score of the CSAT response',
                                                },
                                            },
                                        },
                                        'description': 'The CSAT responses of the issue',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {
                                            'type': 'object',
                                            'properties': {
                                                'slug': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The slug of the custom field',
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The value of the custom field',
                                                },
                                                'values': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The values for multi-valued custom fields',
                                                },
                                            },
                                        },
                                        'description': 'Custom field values associated with the issue',
                                    },
                                    'customer_portal_visible': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the issue is visible in the customer portal',
                                    },
                                    'external_issues': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'external_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external ID of the external issue',
                                                },
                                                'link': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Link to the product issue',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the external issue',
                                                },
                                            },
                                        },
                                        'description': 'The external issues associated with the issue',
                                    },
                                    'first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for first response',
                                    },
                                    'first_response_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the first response',
                                    },
                                    'latest_message_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest message in the issue',
                                    },
                                    'link': {
                                        'type': ['string', 'null'],
                                        'description': 'The link to the issue in Pylon',
                                    },
                                    'number': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of the issue',
                                    },
                                    'number_of_touches': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of times the issue has been touched',
                                    },
                                    'requester': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the contact',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the contact',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for resolution',
                                    },
                                    'resolution_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the resolution',
                                    },
                                    'slack': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'channel_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack channel ID associated with the issue',
                                                    },
                                                    'message_ts': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The root message ID of Slack message that started issue',
                                                    },
                                                    'workspace_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack workspace ID associated with the issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'snoozed_until_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was snoozed until',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': [
                                                    'slack',
                                                    'microsoft_teams',
                                                    'microsoft_teams_chat',
                                                    'chat_widget',
                                                    'email',
                                                    'manual',
                                                    'form',
                                                    'discord',
                                                    'whatsapp',
                                                    'sms',
                                                    'telegram',
                                                ],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'The state of the issue',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the issue',
                                    },
                                    'team': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the team',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the issue',
                                    },
                                    'time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                                    },
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['conversation', 'ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was last updated',
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
                                'x-airbyte-stream-name': 'issues',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer support threads, open issues, response timelines, and who replied',
                                    'when_to_use': 'Support issue or customer response questions',
                                    'trigger_phrases': [
                                        'did they get back',
                                        'support issue',
                                        'ticket for',
                                        'open issues',
                                        'did someone follow up',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                                    'search_strategy': 'Search by title. If no results, try resolving by account name.',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/issues/{id}',
                    action=Action.GET,
                    description='Get a single issue by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the issue'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'assignee': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'attachment_urls': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The attachment URLs attached to this issue',
                                    },
                                    'author_unverified': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether any message on the issue has an unverified author identity',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body of the issue in HTML format',
                                    },
                                    'business_hours_first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for first response',
                                    },
                                    'business_hours_resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for resolution',
                                    },
                                    'business_hours_time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                                    },
                                    'chat_widget_info': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'page_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The URL of the page the user was on when starting the chat widget issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was created',
                                    },
                                    'csat_responses': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'comment': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The comment of the CSAT response',
                                                },
                                                'score': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The score of the CSAT response',
                                                },
                                            },
                                        },
                                        'description': 'The CSAT responses of the issue',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {
                                            'type': 'object',
                                            'properties': {
                                                'slug': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The slug of the custom field',
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The value of the custom field',
                                                },
                                                'values': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The values for multi-valued custom fields',
                                                },
                                            },
                                        },
                                        'description': 'Custom field values associated with the issue',
                                    },
                                    'customer_portal_visible': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the issue is visible in the customer portal',
                                    },
                                    'external_issues': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'external_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external ID of the external issue',
                                                },
                                                'link': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Link to the product issue',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the external issue',
                                                },
                                            },
                                        },
                                        'description': 'The external issues associated with the issue',
                                    },
                                    'first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for first response',
                                    },
                                    'first_response_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the first response',
                                    },
                                    'latest_message_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest message in the issue',
                                    },
                                    'link': {
                                        'type': ['string', 'null'],
                                        'description': 'The link to the issue in Pylon',
                                    },
                                    'number': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of the issue',
                                    },
                                    'number_of_touches': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of times the issue has been touched',
                                    },
                                    'requester': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the contact',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the contact',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for resolution',
                                    },
                                    'resolution_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the resolution',
                                    },
                                    'slack': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'channel_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack channel ID associated with the issue',
                                                    },
                                                    'message_ts': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The root message ID of Slack message that started issue',
                                                    },
                                                    'workspace_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack workspace ID associated with the issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'snoozed_until_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was snoozed until',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': [
                                                    'slack',
                                                    'microsoft_teams',
                                                    'microsoft_teams_chat',
                                                    'chat_widget',
                                                    'email',
                                                    'manual',
                                                    'form',
                                                    'discord',
                                                    'whatsapp',
                                                    'sms',
                                                    'telegram',
                                                ],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'The state of the issue',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the issue',
                                    },
                                    'team': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the team',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the issue',
                                    },
                                    'time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                                    },
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['conversation', 'ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was last updated',
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
                                'x-airbyte-stream-name': 'issues',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer support threads, open issues, response timelines, and who replied',
                                    'when_to_use': 'Support issue or customer response questions',
                                    'trigger_phrases': [
                                        'did they get back',
                                        'support issue',
                                        'ticket for',
                                        'open issues',
                                        'did someone follow up',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                                    'search_strategy': 'Search by title. If no results, try resolving by account name.',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/issues/{id}',
                    action=Action.UPDATE,
                    description='Update an existing issue by ID',
                    body_fields=[
                        'state',
                        'assignee_id',
                        'team_id',
                        'account_id',
                        'tags',
                    ],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'state': {'type': 'string', 'description': 'The state of the issue (open, snoozed, closed)'},
                            'assignee_id': {'type': 'string', 'description': 'The user the issue should be assigned to'},
                            'team_id': {'type': 'string', 'description': 'The ID of the team this issue should be assigned to'},
                            'account_id': {'type': 'string', 'description': 'The account that this issue belongs to'},
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Tags to associate with the issue',
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the issue'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'assignee': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'attachment_urls': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The attachment URLs attached to this issue',
                                    },
                                    'author_unverified': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether any message on the issue has an unverified author identity',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body of the issue in HTML format',
                                    },
                                    'business_hours_first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for first response',
                                    },
                                    'business_hours_resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for resolution',
                                    },
                                    'business_hours_time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                                    },
                                    'chat_widget_info': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'page_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The URL of the page the user was on when starting the chat widget issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was created',
                                    },
                                    'csat_responses': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'comment': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The comment of the CSAT response',
                                                },
                                                'score': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The score of the CSAT response',
                                                },
                                            },
                                        },
                                        'description': 'The CSAT responses of the issue',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {
                                            'type': 'object',
                                            'properties': {
                                                'slug': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The slug of the custom field',
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The value of the custom field',
                                                },
                                                'values': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The values for multi-valued custom fields',
                                                },
                                            },
                                        },
                                        'description': 'Custom field values associated with the issue',
                                    },
                                    'customer_portal_visible': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the issue is visible in the customer portal',
                                    },
                                    'external_issues': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'external_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external ID of the external issue',
                                                },
                                                'link': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Link to the product issue',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the external issue',
                                                },
                                            },
                                        },
                                        'description': 'The external issues associated with the issue',
                                    },
                                    'first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for first response',
                                    },
                                    'first_response_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the first response',
                                    },
                                    'latest_message_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest message in the issue',
                                    },
                                    'link': {
                                        'type': ['string', 'null'],
                                        'description': 'The link to the issue in Pylon',
                                    },
                                    'number': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of the issue',
                                    },
                                    'number_of_touches': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of times the issue has been touched',
                                    },
                                    'requester': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the contact',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the contact',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for resolution',
                                    },
                                    'resolution_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the resolution',
                                    },
                                    'slack': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'channel_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack channel ID associated with the issue',
                                                    },
                                                    'message_ts': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The root message ID of Slack message that started issue',
                                                    },
                                                    'workspace_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack workspace ID associated with the issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'snoozed_until_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was snoozed until',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': [
                                                    'slack',
                                                    'microsoft_teams',
                                                    'microsoft_teams_chat',
                                                    'chat_widget',
                                                    'email',
                                                    'manual',
                                                    'form',
                                                    'discord',
                                                    'whatsapp',
                                                    'sms',
                                                    'telegram',
                                                ],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'The state of the issue',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the issue',
                                    },
                                    'team': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the team',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the issue',
                                    },
                                    'time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                                    },
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['conversation', 'ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was last updated',
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
                                'x-airbyte-stream-name': 'issues',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer support threads, open issues, response timelines, and who replied',
                                    'when_to_use': 'Support issue or customer response questions',
                                    'trigger_phrases': [
                                        'did they get back',
                                        'support issue',
                                        'ticket for',
                                        'open issues',
                                        'did someone follow up',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                                    'search_strategy': 'Search by title. If no results, try resolving by account name.',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='DELETE',
                    path='/issues/{id}/delete',
                    path_override=PathOverrideConfig(
                        path='/issues/{id}',
                    ),
                    action=Action.DELETE,
                    description='Permanently deletes an issue by ID. This action cannot be undone.',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the issue'},
                    'account': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MiniAccount'},
                            {'type': 'null'},
                        ],
                    },
                    'assignee': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MiniUser'},
                            {'type': 'null'},
                        ],
                    },
                    'attachment_urls': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The attachment URLs attached to this issue',
                    },
                    'author_unverified': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether any message on the issue has an unverified author identity',
                    },
                    'body_html': {
                        'type': ['string', 'null'],
                        'description': 'The body of the issue in HTML format',
                    },
                    'business_hours_first_response_seconds': {
                        'type': ['integer', 'null'],
                        'description': 'Business hours time in seconds for first response',
                    },
                    'business_hours_resolution_seconds': {
                        'type': ['integer', 'null'],
                        'description': 'Business hours time in seconds for resolution',
                    },
                    'business_hours_time_in_status_seconds': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'integer'},
                        'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                    },
                    'chat_widget_info': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/IssueChatWidgetInfo'},
                            {'type': 'null'},
                        ],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'description': 'The time the issue was created',
                    },
                    'csat_responses': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/CSATResponse'},
                        'description': 'The CSAT responses of the issue',
                    },
                    'custom_fields': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'$ref': '#/components/schemas/CustomFieldValue'},
                        'description': 'Custom field values associated with the issue',
                    },
                    'customer_portal_visible': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the issue is visible in the customer portal',
                    },
                    'external_issues': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/ExternalIssue'},
                        'description': 'The external issues associated with the issue',
                    },
                    'first_response_seconds': {
                        'type': ['integer', 'null'],
                        'description': 'Time in seconds for first response',
                    },
                    'first_response_time': {
                        'type': ['string', 'null'],
                        'description': 'The time of the first response',
                    },
                    'latest_message_time': {
                        'type': ['string', 'null'],
                        'description': 'The time of the latest message in the issue',
                    },
                    'link': {
                        'type': ['string', 'null'],
                        'description': 'The link to the issue in Pylon',
                    },
                    'number': {
                        'type': ['integer', 'null'],
                        'description': 'The number of the issue',
                    },
                    'number_of_touches': {
                        'type': ['integer', 'null'],
                        'description': 'The number of times the issue has been touched',
                    },
                    'requester': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MiniContact'},
                            {'type': 'null'},
                        ],
                    },
                    'resolution_seconds': {
                        'type': ['integer', 'null'],
                        'description': 'Time in seconds for resolution',
                    },
                    'resolution_time': {
                        'type': ['string', 'null'],
                        'description': 'The time of the resolution',
                    },
                    'slack': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/SlackInfo'},
                            {'type': 'null'},
                        ],
                    },
                    'snoozed_until_time': {
                        'type': ['string', 'null'],
                        'description': 'The time the issue was snoozed until',
                    },
                    'source': {
                        'oneOf': [
                            {
                                'type': 'string',
                                'enum': [
                                    'slack',
                                    'microsoft_teams',
                                    'microsoft_teams_chat',
                                    'chat_widget',
                                    'email',
                                    'manual',
                                    'form',
                                    'discord',
                                    'whatsapp',
                                    'sms',
                                    'telegram',
                                ],
                            },
                            {'type': 'null'},
                        ],
                    },
                    'state': {
                        'type': ['string', 'null'],
                        'description': 'The state of the issue',
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'Tags associated with the issue',
                    },
                    'team': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MiniTeam'},
                            {'type': 'null'},
                        ],
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'The title of the issue',
                    },
                    'time_in_status_seconds': {
                        'type': ['object', 'null'],
                        'additionalProperties': {'type': 'integer'},
                        'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                    },
                    'type': {
                        'oneOf': [
                            {
                                'type': 'string',
                                'enum': ['conversation', 'ticket'],
                            },
                            {'type': 'null'},
                        ],
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'description': 'The time the issue was last updated',
                    },
                },
                'x-airbyte-entity-name': 'issues',
                'x-airbyte-stream-name': 'issues',
                'x-airbyte-ai-hints': {
                    'summary': 'Customer support threads, open issues, response timelines, and who replied',
                    'when_to_use': 'Support issue or customer response questions',
                    'trigger_phrases': [
                        'did they get back',
                        'support issue',
                        'ticket for',
                        'open issues',
                        'did someone follow up',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                    'search_strategy': 'Search by title. If no results, try resolving by account name.',
                },
            },
            ai_hints={
                'summary': 'Customer support threads, open issues, response timelines, and who replied',
                'when_to_use': 'Support issue or customer response questions',
                'trigger_phrases': [
                    'did they get back',
                    'support issue',
                    'ticket for',
                    'open issues',
                    'did someone follow up',
                ],
                'freshness': 'live',
                'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                'search_strategy': 'Search by title. If no results, try resolving by account name.',
            },
        ),
        EntityDefinition(
            name='issue_replies',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/issues/{id}/reply',
                    action=Action.CREATE,
                    description='Sends a customer-facing reply on an issue, visible to the requester.',
                    body_fields=[
                        'body_html',
                        'message_id',
                        'user_id',
                        'contact_id',
                        'attachment_urls',
                    ],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'body_html': {'type': 'string', 'description': 'The body of the reply message in HTML'},
                            'message_id': {'type': 'string', 'description': 'The ID of the message to reply to'},
                            'user_id': {'type': 'string', 'description': 'Optional user ID to post the message as. Only one of user_id or contact_id can be provided.'},
                            'contact_id': {'type': 'string', 'description': 'Optional contact ID to post the message as. Only one of user_id or contact_id can be provided.'},
                            'attachment_urls': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'An array of attachment URLs to attach to this reply',
                            },
                        },
                        'required': ['body_html', 'message_id'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the reply message'},
                                    'issue_id': {'type': 'string', 'description': 'The ID of the issue the reply belongs to'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='issue_assignments',
            actions=[Action.UPDATE],
            endpoints={
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/issues/{id}/assign',
                    path_override=PathOverrideConfig(
                        path='/issues/{id}',
                    ),
                    action=Action.UPDATE,
                    description='Assign an issue to a user or team, or remove the current assignment.',
                    body_fields=['assignee_id', 'team_id'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'assignee_id': {'type': 'string', 'description': 'The ID of the user to assign the issue to. Pass an empty string to unassign.'},
                            'team_id': {'type': 'string', 'description': 'The ID of the team to assign the issue to. Pass an empty string to remove team assignment.'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the issue'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'assignee': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'attachment_urls': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The attachment URLs attached to this issue',
                                    },
                                    'author_unverified': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether any message on the issue has an unverified author identity',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body of the issue in HTML format',
                                    },
                                    'business_hours_first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for first response',
                                    },
                                    'business_hours_resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for resolution',
                                    },
                                    'business_hours_time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                                    },
                                    'chat_widget_info': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'page_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The URL of the page the user was on when starting the chat widget issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was created',
                                    },
                                    'csat_responses': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'comment': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The comment of the CSAT response',
                                                },
                                                'score': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The score of the CSAT response',
                                                },
                                            },
                                        },
                                        'description': 'The CSAT responses of the issue',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {
                                            'type': 'object',
                                            'properties': {
                                                'slug': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The slug of the custom field',
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The value of the custom field',
                                                },
                                                'values': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The values for multi-valued custom fields',
                                                },
                                            },
                                        },
                                        'description': 'Custom field values associated with the issue',
                                    },
                                    'customer_portal_visible': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the issue is visible in the customer portal',
                                    },
                                    'external_issues': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'external_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external ID of the external issue',
                                                },
                                                'link': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Link to the product issue',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the external issue',
                                                },
                                            },
                                        },
                                        'description': 'The external issues associated with the issue',
                                    },
                                    'first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for first response',
                                    },
                                    'first_response_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the first response',
                                    },
                                    'latest_message_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest message in the issue',
                                    },
                                    'link': {
                                        'type': ['string', 'null'],
                                        'description': 'The link to the issue in Pylon',
                                    },
                                    'number': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of the issue',
                                    },
                                    'number_of_touches': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of times the issue has been touched',
                                    },
                                    'requester': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the contact',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the contact',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for resolution',
                                    },
                                    'resolution_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the resolution',
                                    },
                                    'slack': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'channel_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack channel ID associated with the issue',
                                                    },
                                                    'message_ts': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The root message ID of Slack message that started issue',
                                                    },
                                                    'workspace_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack workspace ID associated with the issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'snoozed_until_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was snoozed until',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': [
                                                    'slack',
                                                    'microsoft_teams',
                                                    'microsoft_teams_chat',
                                                    'chat_widget',
                                                    'email',
                                                    'manual',
                                                    'form',
                                                    'discord',
                                                    'whatsapp',
                                                    'sms',
                                                    'telegram',
                                                ],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'The state of the issue',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the issue',
                                    },
                                    'team': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the team',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the issue',
                                    },
                                    'time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                                    },
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['conversation', 'ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was last updated',
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
                                'x-airbyte-stream-name': 'issues',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer support threads, open issues, response timelines, and who replied',
                                    'when_to_use': 'Support issue or customer response questions',
                                    'trigger_phrases': [
                                        'did they get back',
                                        'support issue',
                                        'ticket for',
                                        'open issues',
                                        'did someone follow up',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                                    'search_strategy': 'Search by title. If no results, try resolving by account name.',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='issue_statuses',
            actions=[Action.UPDATE],
            endpoints={
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/issues/{id}/update-status',
                    path_override=PathOverrideConfig(
                        path='/issues/{id}',
                    ),
                    action=Action.UPDATE,
                    description='Transition an issue to a new status (new, waiting_on_you, waiting_on_customer, on_hold, closed, or a custom status slug).',
                    body_fields=['state'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'state': {'type': 'string', 'description': 'The target state for the issue (new, waiting_on_you, waiting_on_customer, on_hold, closed, or a custom status slug)'},
                        },
                        'required': ['state'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the issue'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'assignee': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'attachment_urls': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The attachment URLs attached to this issue',
                                    },
                                    'author_unverified': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether any message on the issue has an unverified author identity',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body of the issue in HTML format',
                                    },
                                    'business_hours_first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for first response',
                                    },
                                    'business_hours_resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Business hours time in seconds for resolution',
                                    },
                                    'business_hours_time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the business hours time in seconds the issue has spent in that status',
                                    },
                                    'chat_widget_info': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'page_url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The URL of the page the user was on when starting the chat widget issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was created',
                                    },
                                    'csat_responses': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'comment': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The comment of the CSAT response',
                                                },
                                                'score': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The score of the CSAT response',
                                                },
                                            },
                                        },
                                        'description': 'The CSAT responses of the issue',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {
                                            'type': 'object',
                                            'properties': {
                                                'slug': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The slug of the custom field',
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The value of the custom field',
                                                },
                                                'values': {
                                                    'type': ['array', 'null'],
                                                    'items': {'type': 'string'},
                                                    'description': 'The values for multi-valued custom fields',
                                                },
                                            },
                                        },
                                        'description': 'Custom field values associated with the issue',
                                    },
                                    'customer_portal_visible': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the issue is visible in the customer portal',
                                    },
                                    'external_issues': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'external_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The external ID of the external issue',
                                                },
                                                'link': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Link to the product issue',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the external issue',
                                                },
                                            },
                                        },
                                        'description': 'The external issues associated with the issue',
                                    },
                                    'first_response_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for first response',
                                    },
                                    'first_response_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the first response',
                                    },
                                    'latest_message_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest message in the issue',
                                    },
                                    'link': {
                                        'type': ['string', 'null'],
                                        'description': 'The link to the issue in Pylon',
                                    },
                                    'number': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of the issue',
                                    },
                                    'number_of_touches': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of times the issue has been touched',
                                    },
                                    'requester': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the contact',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the contact',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'resolution_seconds': {
                                        'type': ['integer', 'null'],
                                        'description': 'Time in seconds for resolution',
                                    },
                                    'resolution_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the resolution',
                                    },
                                    'slack': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'channel_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack channel ID associated with the issue',
                                                    },
                                                    'message_ts': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The root message ID of Slack message that started issue',
                                                    },
                                                    'workspace_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The Slack workspace ID associated with the issue',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'snoozed_until_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was snoozed until',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': [
                                                    'slack',
                                                    'microsoft_teams',
                                                    'microsoft_teams_chat',
                                                    'chat_widget',
                                                    'email',
                                                    'manual',
                                                    'form',
                                                    'discord',
                                                    'whatsapp',
                                                    'sms',
                                                    'telegram',
                                                ],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'The state of the issue',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the issue',
                                    },
                                    'team': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the team',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the issue',
                                    },
                                    'time_in_status_seconds': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': {'type': 'integer'},
                                        'description': 'A map of status slug to the time in seconds the issue has spent in that status',
                                    },
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['conversation', 'ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the issue was last updated',
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
                                'x-airbyte-stream-name': 'issues',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer support threads, open issues, response timelines, and who replied',
                                    'when_to_use': 'Support issue or customer response questions',
                                    'trigger_phrases': [
                                        'did they get back',
                                        'support issue',
                                        'ticket for',
                                        'open issues',
                                        'did someone follow up',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Did Marathon get back to us on the integration issue?', 'What are the open support tickets for Acme?', 'Who last replied to the billing thread?'],
                                    'search_strategy': 'Search by title. If no results, try resolving by account name.',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='messages',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/issues/{id}/messages',
                    action=Action.LIST,
                    description='Returns all messages on an issue (customer-facing replies and internal notes)',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the message'},
                                        'author': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'avatar_url': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'contact': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'email': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The email of the contact',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The ID of the contact',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'user': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'email': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The email of the user',
                                                                        },
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                            'description': 'The ID of the user',
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'email_info': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'bcc_emails': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                            'description': 'BCC email addresses',
                                                        },
                                                        'cc_emails': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                            'description': 'CC email addresses',
                                                        },
                                                        'from_email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Sender email address',
                                                        },
                                                        'message_id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'RFC 5322 Message-ID header value',
                                                        },
                                                        'to_emails': {
                                                            'type': ['array', 'null'],
                                                            'items': {'type': 'string'},
                                                            'description': 'Recipient email addresses',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'file_urls': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'The URLs of the files in the message',
                                        },
                                        'is_private': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Indicates if the message is private',
                                        },
                                        'message_html': {
                                            'type': ['string', 'null'],
                                            'description': 'The HTML body of the message',
                                        },
                                        'source': {
                                            'type': ['string', 'null'],
                                            'description': 'The source of the message',
                                        },
                                        'thread_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID of the thread the message belongs to',
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'description': 'The time at which the message was created',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'messages',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Customer messages across Pylon channels (Slack, email, etc.)',
                                        'when_to_use': 'Looking for customer messages or conversation content',
                                        'trigger_phrases': ['pylon message', 'customer message'],
                                        'freshness': 'live',
                                        'example_questions': ['Show recent customer messages'],
                                        'search_strategy': 'Search by content or filter by account',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the message'},
                    'author': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MessageAuthor'},
                            {'type': 'null'},
                        ],
                    },
                    'email_info': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/EmailMessageInfo'},
                            {'type': 'null'},
                        ],
                    },
                    'file_urls': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The URLs of the files in the message',
                    },
                    'is_private': {
                        'type': ['boolean', 'null'],
                        'description': 'Indicates if the message is private',
                    },
                    'message_html': {
                        'type': ['string', 'null'],
                        'description': 'The HTML body of the message',
                    },
                    'source': {
                        'type': ['string', 'null'],
                        'description': 'The source of the message',
                    },
                    'thread_id': {
                        'type': ['string', 'null'],
                        'description': 'The ID of the thread the message belongs to',
                    },
                    'timestamp': {
                        'type': ['string', 'null'],
                        'description': 'The time at which the message was created',
                    },
                },
                'x-airbyte-entity-name': 'messages',
                'x-airbyte-ai-hints': {
                    'summary': 'Customer messages across Pylon channels (Slack, email, etc.)',
                    'when_to_use': 'Looking for customer messages or conversation content',
                    'trigger_phrases': ['pylon message', 'customer message'],
                    'freshness': 'live',
                    'example_questions': ['Show recent customer messages'],
                    'search_strategy': 'Search by content or filter by account',
                },
            },
            ai_hints={
                'summary': 'Customer messages across Pylon channels (Slack, email, etc.)',
                'when_to_use': 'Looking for customer messages or conversation content',
                'trigger_phrases': ['pylon message', 'customer message'],
                'freshness': 'live',
                'example_questions': ['Show recent customer messages'],
                'search_strategy': 'Search by content or filter by account',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='messages',
                    target_entity='issues',
                    foreign_key='id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='issue_notes',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/issues/{id}/note',
                    action=Action.CREATE,
                    description='Create an internal note on an issue',
                    body_fields=['body_html', 'thread_id', 'message_id'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'body_html': {'type': 'string', 'description': 'The HTML content of the note'},
                            'thread_id': {'type': 'string', 'description': 'The ID of the thread to add the note to'},
                            'message_id': {'type': 'string', 'description': 'The ID of the message to add the note to'},
                        },
                        'required': ['body_html'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the note message'},
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The HTML content of the note',
                                    },
                                    'timestamp': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the note was created',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='issue_threads',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/issues/{id}/threads',
                    action=Action.CREATE,
                    description='Create a new thread on an issue',
                    body_fields=['name'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the thread'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the thread'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the thread',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='accounts',
            stream_name='accounts',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/accounts',
                    action=Action.LIST,
                    description='Get a list of accounts',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the account'},
                                        'channels': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'channel_id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The channel identifier',
                                                    },
                                                    'source': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The source of the channel',
                                                    },
                                                    'is_primary': {
                                                        'type': ['boolean', 'null'],
                                                        'description': 'Whether this is the primary channel',
                                                    },
                                                },
                                            },
                                            'description': 'The channels associated with the account',
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'description': 'The time the account was created',
                                        },
                                        'custom_fields': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': True,
                                            'description': 'Custom field values associated with the account',
                                        },
                                        'domain': {
                                            'type': ['string', 'null'],
                                            'description': 'The domain of the account',
                                        },
                                        'domains': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'The domains associated with the account',
                                        },
                                        'external_ids': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': True,
                                            'description': 'External IDs associated with the account',
                                        },
                                        'is_disabled': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the account is disabled',
                                        },
                                        'latest_customer_activity_time': {
                                            'type': ['string', 'null'],
                                            'description': 'The time of the latest customer activity',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the account',
                                        },
                                        'owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The email of the user',
                                                        },
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the user',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'primary_domain': {
                                            'type': ['string', 'null'],
                                            'description': 'The primary domain of the account',
                                        },
                                        'tags': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Tags associated with the account',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of the account',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'accounts',
                                    'x-airbyte-stream-name': 'accounts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Customer accounts in Pylon',
                                        'when_to_use': 'Looking up customer account details',
                                        'trigger_phrases': ['pylon account', 'customer account'],
                                        'freshness': 'live',
                                        'example_questions': ['Find an account in Pylon'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                    preferred_for_check=True,
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/accounts',
                    action=Action.CREATE,
                    description='Create a new account',
                    body_fields=[
                        'name',
                        'domains',
                        'primary_domain',
                        'owner_id',
                        'logo_url',
                        'tags',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the account'},
                            'domains': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'The domains of the account (e.g. stripe.com)',
                            },
                            'primary_domain': {'type': 'string', 'description': 'Must be in the list of domains. If there are any domains, there must be exactly one primary domain.'},
                            'owner_id': {'type': 'string', 'description': 'The ID of the owner of the account'},
                            'logo_url': {'type': 'string', 'description': 'The logo URL of the account. Must be a square .png, .jpg or .jpeg.'},
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Tags to associate with the account',
                            },
                        },
                        'required': ['name'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the account'},
                                    'channels': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'channel_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The channel identifier',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the channel',
                                                },
                                                'is_primary': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether this is the primary channel',
                                                },
                                            },
                                        },
                                        'description': 'The channels associated with the account',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the account was created',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'Custom field values associated with the account',
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                        'description': 'The domain of the account',
                                    },
                                    'domains': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The domains associated with the account',
                                    },
                                    'external_ids': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'External IDs associated with the account',
                                    },
                                    'is_disabled': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the account is disabled',
                                    },
                                    'latest_customer_activity_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest customer activity',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the account',
                                    },
                                    'owner': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'primary_domain': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary domain of the account',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the account',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'The type of the account',
                                    },
                                },
                                'x-airbyte-entity-name': 'accounts',
                                'x-airbyte-stream-name': 'accounts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer accounts in Pylon',
                                    'when_to_use': 'Looking up customer account details',
                                    'trigger_phrases': ['pylon account', 'customer account'],
                                    'freshness': 'live',
                                    'example_questions': ['Find an account in Pylon'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/accounts/{id}',
                    action=Action.GET,
                    description='Get a single account by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the account'},
                                    'channels': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'channel_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The channel identifier',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the channel',
                                                },
                                                'is_primary': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether this is the primary channel',
                                                },
                                            },
                                        },
                                        'description': 'The channels associated with the account',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the account was created',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'Custom field values associated with the account',
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                        'description': 'The domain of the account',
                                    },
                                    'domains': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The domains associated with the account',
                                    },
                                    'external_ids': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'External IDs associated with the account',
                                    },
                                    'is_disabled': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the account is disabled',
                                    },
                                    'latest_customer_activity_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest customer activity',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the account',
                                    },
                                    'owner': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'primary_domain': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary domain of the account',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the account',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'The type of the account',
                                    },
                                },
                                'x-airbyte-entity-name': 'accounts',
                                'x-airbyte-stream-name': 'accounts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer accounts in Pylon',
                                    'when_to_use': 'Looking up customer account details',
                                    'trigger_phrases': ['pylon account', 'customer account'],
                                    'freshness': 'live',
                                    'example_questions': ['Find an account in Pylon'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/accounts/{id}',
                    action=Action.UPDATE,
                    description='Update an existing account by ID',
                    body_fields=[
                        'name',
                        'domains',
                        'primary_domain',
                        'owner_id',
                        'logo_url',
                        'is_disabled',
                        'tags',
                    ],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the account'},
                            'domains': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Domains of the account. Must specify one domain as primary.',
                            },
                            'primary_domain': {'type': 'string', 'description': 'Must be in the list of domains. If there are any domains, there must be exactly one primary domain.'},
                            'owner_id': {'type': 'string', 'description': 'The ID of the owner of the account. If empty string is passed in, the owner will be removed.'},
                            'logo_url': {'type': 'string', 'description': 'Logo URL of the account'},
                            'is_disabled': {'type': 'boolean', 'description': 'Whether the account is disabled'},
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Tags to associate with the account',
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the account'},
                                    'channels': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'channel_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The channel identifier',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the channel',
                                                },
                                                'is_primary': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether this is the primary channel',
                                                },
                                            },
                                        },
                                        'description': 'The channels associated with the account',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the account was created',
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'Custom field values associated with the account',
                                    },
                                    'domain': {
                                        'type': ['string', 'null'],
                                        'description': 'The domain of the account',
                                    },
                                    'domains': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The domains associated with the account',
                                    },
                                    'external_ids': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'External IDs associated with the account',
                                    },
                                    'is_disabled': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the account is disabled',
                                    },
                                    'latest_customer_activity_time': {
                                        'type': ['string', 'null'],
                                        'description': 'The time of the latest customer activity',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the account',
                                    },
                                    'owner': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'primary_domain': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary domain of the account',
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Tags associated with the account',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'The type of the account',
                                    },
                                },
                                'x-airbyte-entity-name': 'accounts',
                                'x-airbyte-stream-name': 'accounts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer accounts in Pylon',
                                    'when_to_use': 'Looking up customer account details',
                                    'trigger_phrases': ['pylon account', 'customer account'],
                                    'freshness': 'live',
                                    'example_questions': ['Find an account in Pylon'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the account'},
                    'channels': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/AccountChannel'},
                        'description': 'The channels associated with the account',
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'description': 'The time the account was created',
                    },
                    'custom_fields': {
                        'type': ['object', 'null'],
                        'additionalProperties': True,
                        'description': 'Custom field values associated with the account',
                    },
                    'domain': {
                        'type': ['string', 'null'],
                        'description': 'The domain of the account',
                    },
                    'domains': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The domains associated with the account',
                    },
                    'external_ids': {
                        'type': ['object', 'null'],
                        'additionalProperties': True,
                        'description': 'External IDs associated with the account',
                    },
                    'is_disabled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the account is disabled',
                    },
                    'latest_customer_activity_time': {
                        'type': ['string', 'null'],
                        'description': 'The time of the latest customer activity',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the account',
                    },
                    'owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MiniUser'},
                            {'type': 'null'},
                        ],
                    },
                    'primary_domain': {
                        'type': ['string', 'null'],
                        'description': 'The primary domain of the account',
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'Tags associated with the account',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of the account',
                    },
                },
                'x-airbyte-entity-name': 'accounts',
                'x-airbyte-stream-name': 'accounts',
                'x-airbyte-ai-hints': {
                    'summary': 'Customer accounts in Pylon',
                    'when_to_use': 'Looking up customer account details',
                    'trigger_phrases': ['pylon account', 'customer account'],
                    'freshness': 'live',
                    'example_questions': ['Find an account in Pylon'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Customer accounts in Pylon',
                'when_to_use': 'Looking up customer account details',
                'trigger_phrases': ['pylon account', 'customer account'],
                'freshness': 'live',
                'example_questions': ['Find an account in Pylon'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='contacts',
            stream_name='contacts',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/contacts',
                    action=Action.LIST,
                    description='Get a list of contacts',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the contact'},
                                        'account': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The ID of the account',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'avatar_url': {
                                            'type': ['string', 'null'],
                                            'description': "The URL of the contact's avatar",
                                        },
                                        'custom_fields': {
                                            'type': ['object', 'null'],
                                            'additionalProperties': True,
                                            'description': 'Custom field values associated with the contact',
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'The primary email address of the contact',
                                        },
                                        'emails': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'All email addresses of the contact',
                                        },
                                        'integration_user_ids': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The integration user ID',
                                                    },
                                                    'source': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The source of the integration',
                                                    },
                                                },
                                            },
                                            'description': 'Integration user IDs associated with the contact',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the contact',
                                        },
                                        'phone_numbers': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Phone numbers of the contact',
                                        },
                                        'portal_role': {
                                            'type': ['string', 'null'],
                                            'description': 'The portal role of the contact',
                                        },
                                        'portal_role_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The portal role ID of the contact',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'contacts',
                                    'x-airbyte-stream-name': 'contacts',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Customer contacts associated with Pylon accounts',
                                        'when_to_use': 'Looking up customer contact information',
                                        'trigger_phrases': ['pylon contact', 'customer contact'],
                                        'freshness': 'live',
                                        'example_questions': ['Find a contact in Pylon'],
                                        'search_strategy': 'Search by name or email',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/contacts',
                    action=Action.CREATE,
                    description='Create a new contact',
                    body_fields=[
                        'name',
                        'email',
                        'account_id',
                        'avatar_url',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the contact'},
                            'email': {'type': 'string', 'description': 'The email address of the contact'},
                            'account_id': {'type': 'string', 'description': 'The ID of the account to associate this contact with'},
                            'avatar_url': {'type': 'string', 'description': "The URL of the contact's avatar"},
                        },
                        'required': ['name'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the contact'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'avatar_url': {
                                        'type': ['string', 'null'],
                                        'description': "The URL of the contact's avatar",
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'Custom field values associated with the contact',
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary email address of the contact',
                                    },
                                    'emails': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'All email addresses of the contact',
                                    },
                                    'integration_user_ids': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The integration user ID',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the integration',
                                                },
                                            },
                                        },
                                        'description': 'Integration user IDs associated with the contact',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the contact',
                                    },
                                    'phone_numbers': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Phone numbers of the contact',
                                    },
                                    'portal_role': {
                                        'type': ['string', 'null'],
                                        'description': 'The portal role of the contact',
                                    },
                                    'portal_role_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The portal role ID of the contact',
                                    },
                                },
                                'x-airbyte-entity-name': 'contacts',
                                'x-airbyte-stream-name': 'contacts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer contacts associated with Pylon accounts',
                                    'when_to_use': 'Looking up customer contact information',
                                    'trigger_phrases': ['pylon contact', 'customer contact'],
                                    'freshness': 'live',
                                    'example_questions': ['Find a contact in Pylon'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/contacts/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the contact'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'avatar_url': {
                                        'type': ['string', 'null'],
                                        'description': "The URL of the contact's avatar",
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'Custom field values associated with the contact',
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary email address of the contact',
                                    },
                                    'emails': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'All email addresses of the contact',
                                    },
                                    'integration_user_ids': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The integration user ID',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the integration',
                                                },
                                            },
                                        },
                                        'description': 'Integration user IDs associated with the contact',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the contact',
                                    },
                                    'phone_numbers': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Phone numbers of the contact',
                                    },
                                    'portal_role': {
                                        'type': ['string', 'null'],
                                        'description': 'The portal role of the contact',
                                    },
                                    'portal_role_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The portal role ID of the contact',
                                    },
                                },
                                'x-airbyte-entity-name': 'contacts',
                                'x-airbyte-stream-name': 'contacts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer contacts associated with Pylon accounts',
                                    'when_to_use': 'Looking up customer contact information',
                                    'trigger_phrases': ['pylon contact', 'customer contact'],
                                    'freshness': 'live',
                                    'example_questions': ['Find a contact in Pylon'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/contacts/{id}',
                    action=Action.UPDATE,
                    description='Update an existing contact by ID',
                    body_fields=['name', 'email', 'account_id'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the contact'},
                            'email': {'type': 'string', 'description': 'The email address of the contact'},
                            'account_id': {'type': 'string', 'description': 'The ID of the account to associate this contact with'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the contact'},
                                    'account': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the account',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'avatar_url': {
                                        'type': ['string', 'null'],
                                        'description': "The URL of the contact's avatar",
                                    },
                                    'custom_fields': {
                                        'type': ['object', 'null'],
                                        'additionalProperties': True,
                                        'description': 'Custom field values associated with the contact',
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary email address of the contact',
                                    },
                                    'emails': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'All email addresses of the contact',
                                    },
                                    'integration_user_ids': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The integration user ID',
                                                },
                                                'source': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The source of the integration',
                                                },
                                            },
                                        },
                                        'description': 'Integration user IDs associated with the contact',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the contact',
                                    },
                                    'phone_numbers': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'Phone numbers of the contact',
                                    },
                                    'portal_role': {
                                        'type': ['string', 'null'],
                                        'description': 'The portal role of the contact',
                                    },
                                    'portal_role_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The portal role ID of the contact',
                                    },
                                },
                                'x-airbyte-entity-name': 'contacts',
                                'x-airbyte-stream-name': 'contacts',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Customer contacts associated with Pylon accounts',
                                    'when_to_use': 'Looking up customer contact information',
                                    'trigger_phrases': ['pylon contact', 'customer contact'],
                                    'freshness': 'live',
                                    'example_questions': ['Find a contact in Pylon'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the contact'},
                    'account': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MiniAccount'},
                            {'type': 'null'},
                        ],
                    },
                    'avatar_url': {
                        'type': ['string', 'null'],
                        'description': "The URL of the contact's avatar",
                    },
                    'custom_fields': {
                        'type': ['object', 'null'],
                        'additionalProperties': True,
                        'description': 'Custom field values associated with the contact',
                    },
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'The primary email address of the contact',
                    },
                    'emails': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'All email addresses of the contact',
                    },
                    'integration_user_ids': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/IntegrationUserId'},
                        'description': 'Integration user IDs associated with the contact',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the contact',
                    },
                    'phone_numbers': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'Phone numbers of the contact',
                    },
                    'portal_role': {
                        'type': ['string', 'null'],
                        'description': 'The portal role of the contact',
                    },
                    'portal_role_id': {
                        'type': ['string', 'null'],
                        'description': 'The portal role ID of the contact',
                    },
                },
                'x-airbyte-entity-name': 'contacts',
                'x-airbyte-stream-name': 'contacts',
                'x-airbyte-ai-hints': {
                    'summary': 'Customer contacts associated with Pylon accounts',
                    'when_to_use': 'Looking up customer contact information',
                    'trigger_phrases': ['pylon contact', 'customer contact'],
                    'freshness': 'live',
                    'example_questions': ['Find a contact in Pylon'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Customer contacts associated with Pylon accounts',
                'when_to_use': 'Looking up customer contact information',
                'trigger_phrases': ['pylon contact', 'customer contact'],
                'freshness': 'live',
                'example_questions': ['Find a contact in Pylon'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='teams',
            stream_name='teams',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/teams',
                    action=Action.LIST,
                    description='Get a list of teams',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the team'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the team',
                                        },
                                        'users': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The email of the user',
                                                    },
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The ID of the user',
                                                    },
                                                },
                                            },
                                            'description': 'The users in the team',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'teams',
                                    'x-airbyte-stream-name': 'teams',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Support teams in Pylon for routing conversations',
                                        'when_to_use': 'Questions about team structure or routing',
                                        'trigger_phrases': ['pylon team', 'support team'],
                                        'freshness': 'static',
                                        'example_questions': ['What teams are in Pylon?'],
                                        'search_strategy': 'List all teams',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/teams',
                    action=Action.CREATE,
                    description='Create a new team',
                    body_fields=['name'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the team'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the team'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the team',
                                    },
                                    'users': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The email of the user',
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The ID of the user',
                                                },
                                            },
                                        },
                                        'description': 'The users in the team',
                                    },
                                },
                                'x-airbyte-entity-name': 'teams',
                                'x-airbyte-stream-name': 'teams',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Support teams in Pylon for routing conversations',
                                    'when_to_use': 'Questions about team structure or routing',
                                    'trigger_phrases': ['pylon team', 'support team'],
                                    'freshness': 'static',
                                    'example_questions': ['What teams are in Pylon?'],
                                    'search_strategy': 'List all teams',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/teams/{id}',
                    action=Action.GET,
                    description='Get a single team by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the team'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the team',
                                    },
                                    'users': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The email of the user',
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The ID of the user',
                                                },
                                            },
                                        },
                                        'description': 'The users in the team',
                                    },
                                },
                                'x-airbyte-entity-name': 'teams',
                                'x-airbyte-stream-name': 'teams',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Support teams in Pylon for routing conversations',
                                    'when_to_use': 'Questions about team structure or routing',
                                    'trigger_phrases': ['pylon team', 'support team'],
                                    'freshness': 'static',
                                    'example_questions': ['What teams are in Pylon?'],
                                    'search_strategy': 'List all teams',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/teams/{id}',
                    action=Action.UPDATE,
                    description='Update an existing team by ID',
                    body_fields=['name'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the team'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the team'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the team',
                                    },
                                    'users': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The email of the user',
                                                },
                                                'id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The ID of the user',
                                                },
                                            },
                                        },
                                        'description': 'The users in the team',
                                    },
                                },
                                'x-airbyte-entity-name': 'teams',
                                'x-airbyte-stream-name': 'teams',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Support teams in Pylon for routing conversations',
                                    'when_to_use': 'Questions about team structure or routing',
                                    'trigger_phrases': ['pylon team', 'support team'],
                                    'freshness': 'static',
                                    'example_questions': ['What teams are in Pylon?'],
                                    'search_strategy': 'List all teams',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the team'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the team',
                    },
                    'users': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/MiniUser'},
                        'description': 'The users in the team',
                    },
                },
                'x-airbyte-entity-name': 'teams',
                'x-airbyte-stream-name': 'teams',
                'x-airbyte-ai-hints': {
                    'summary': 'Support teams in Pylon for routing conversations',
                    'when_to_use': 'Questions about team structure or routing',
                    'trigger_phrases': ['pylon team', 'support team'],
                    'freshness': 'static',
                    'example_questions': ['What teams are in Pylon?'],
                    'search_strategy': 'List all teams',
                },
            },
            ai_hints={
                'summary': 'Support teams in Pylon for routing conversations',
                'when_to_use': 'Questions about team structure or routing',
                'trigger_phrases': ['pylon team', 'support team'],
                'freshness': 'static',
                'example_questions': ['What teams are in Pylon?'],
                'search_strategy': 'List all teams',
            },
        ),
        EntityDefinition(
            name='tags',
            stream_name='tags',
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tags',
                    action=Action.LIST,
                    description='Get all tags',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the tag'},
                                        'hex_color': {
                                            'type': ['string', 'null'],
                                            'description': "The hex code of the tag's color",
                                        },
                                        'object_type': {
                                            'type': ['string', 'null'],
                                            'description': 'The object type of the associated object',
                                        },
                                        'value': {
                                            'type': ['string', 'null'],
                                            'description': 'The tag value',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tags',
                                    'x-airbyte-stream-name': 'tags',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Tags for categorizing issues and conversations in Pylon',
                                        'when_to_use': 'Questions about available tags or categorization',
                                        'trigger_phrases': ['pylon tag'],
                                        'freshness': 'live',
                                        'example_questions': ['What tags exist in Pylon?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/tags',
                    action=Action.CREATE,
                    description='Create a new tag',
                    body_fields=['value', 'object_type', 'hex_color'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'value': {'type': 'string', 'description': 'The tag value'},
                            'object_type': {'type': 'string', 'description': 'The object type (issue, account, contact)'},
                            'hex_color': {'type': 'string', 'description': 'The hex color code of the tag'},
                        },
                        'required': ['value', 'object_type'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the tag'},
                                    'hex_color': {
                                        'type': ['string', 'null'],
                                        'description': "The hex code of the tag's color",
                                    },
                                    'object_type': {
                                        'type': ['string', 'null'],
                                        'description': 'The object type of the associated object',
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                        'description': 'The tag value',
                                    },
                                },
                                'x-airbyte-entity-name': 'tags',
                                'x-airbyte-stream-name': 'tags',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Tags for categorizing issues and conversations in Pylon',
                                    'when_to_use': 'Questions about available tags or categorization',
                                    'trigger_phrases': ['pylon tag'],
                                    'freshness': 'live',
                                    'example_questions': ['What tags exist in Pylon?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/tags/{id}',
                    action=Action.GET,
                    description='Get a tag by its ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the tag'},
                                    'hex_color': {
                                        'type': ['string', 'null'],
                                        'description': "The hex code of the tag's color",
                                    },
                                    'object_type': {
                                        'type': ['string', 'null'],
                                        'description': 'The object type of the associated object',
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                        'description': 'The tag value',
                                    },
                                },
                                'x-airbyte-entity-name': 'tags',
                                'x-airbyte-stream-name': 'tags',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Tags for categorizing issues and conversations in Pylon',
                                    'when_to_use': 'Questions about available tags or categorization',
                                    'trigger_phrases': ['pylon tag'],
                                    'freshness': 'live',
                                    'example_questions': ['What tags exist in Pylon?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/tags/{id}',
                    action=Action.UPDATE,
                    description='Update an existing tag by ID',
                    body_fields=['value', 'hex_color'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'value': {'type': 'string', 'description': 'The tag value'},
                            'hex_color': {'type': 'string', 'description': 'The hex color code of the tag'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the tag'},
                                    'hex_color': {
                                        'type': ['string', 'null'],
                                        'description': "The hex code of the tag's color",
                                    },
                                    'object_type': {
                                        'type': ['string', 'null'],
                                        'description': 'The object type of the associated object',
                                    },
                                    'value': {
                                        'type': ['string', 'null'],
                                        'description': 'The tag value',
                                    },
                                },
                                'x-airbyte-entity-name': 'tags',
                                'x-airbyte-stream-name': 'tags',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Tags for categorizing issues and conversations in Pylon',
                                    'when_to_use': 'Questions about available tags or categorization',
                                    'trigger_phrases': ['pylon tag'],
                                    'freshness': 'live',
                                    'example_questions': ['What tags exist in Pylon?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the tag'},
                    'hex_color': {
                        'type': ['string', 'null'],
                        'description': "The hex code of the tag's color",
                    },
                    'object_type': {
                        'type': ['string', 'null'],
                        'description': 'The object type of the associated object',
                    },
                    'value': {
                        'type': ['string', 'null'],
                        'description': 'The tag value',
                    },
                },
                'x-airbyte-entity-name': 'tags',
                'x-airbyte-stream-name': 'tags',
                'x-airbyte-ai-hints': {
                    'summary': 'Tags for categorizing issues and conversations in Pylon',
                    'when_to_use': 'Questions about available tags or categorization',
                    'trigger_phrases': ['pylon tag'],
                    'freshness': 'live',
                    'example_questions': ['What tags exist in Pylon?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Tags for categorizing issues and conversations in Pylon',
                'when_to_use': 'Questions about available tags or categorization',
                'trigger_phrases': ['pylon tag'],
                'freshness': 'live',
                'example_questions': ['What tags exist in Pylon?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='users',
            stream_name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/users',
                    action=Action.LIST,
                    description='Get a list of users',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the user'},
                                        'avatar_url': {
                                            'type': ['string', 'null'],
                                            'description': "The URL of the user's avatar",
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'The primary email address of the user',
                                        },
                                        'emails': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'All email addresses of the user',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the user',
                                        },
                                        'role_id': {
                                            'type': ['string', 'null'],
                                            'description': "The ID of the user's role",
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'The status of the user',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'users',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Pylon users (support agents and admins)',
                                        'when_to_use': 'Looking up support agent details',
                                        'trigger_phrases': ['pylon user', 'support agent'],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the Pylon users?'],
                                        'search_strategy': 'Search by name or email',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/users/{id}',
                    action=Action.GET,
                    description='Get a single user by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the user'},
                                    'avatar_url': {
                                        'type': ['string', 'null'],
                                        'description': "The URL of the user's avatar",
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary email address of the user',
                                    },
                                    'emails': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'All email addresses of the user',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the user',
                                    },
                                    'role_id': {
                                        'type': ['string', 'null'],
                                        'description': "The ID of the user's role",
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'The status of the user',
                                    },
                                },
                                'x-airbyte-entity-name': 'users',
                                'x-airbyte-stream-name': 'users',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Pylon users (support agents and admins)',
                                    'when_to_use': 'Looking up support agent details',
                                    'trigger_phrases': ['pylon user', 'support agent'],
                                    'freshness': 'live',
                                    'example_questions': ['Who are the Pylon users?'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the user'},
                    'avatar_url': {
                        'type': ['string', 'null'],
                        'description': "The URL of the user's avatar",
                    },
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'The primary email address of the user',
                    },
                    'emails': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'All email addresses of the user',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the user',
                    },
                    'role_id': {
                        'type': ['string', 'null'],
                        'description': "The ID of the user's role",
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'The status of the user',
                    },
                },
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
                'x-airbyte-ai-hints': {
                    'summary': 'Pylon users (support agents and admins)',
                    'when_to_use': 'Looking up support agent details',
                    'trigger_phrases': ['pylon user', 'support agent'],
                    'freshness': 'live',
                    'example_questions': ['Who are the Pylon users?'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Pylon users (support agents and admins)',
                'when_to_use': 'Looking up support agent details',
                'trigger_phrases': ['pylon user', 'support agent'],
                'freshness': 'live',
                'example_questions': ['Who are the Pylon users?'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='custom_fields',
            stream_name='custom_fields',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/custom-fields',
                    action=Action.LIST,
                    description='Get all custom fields for a given object type',
                    query_params=['object_type', 'cursor'],
                    query_params_schema={
                        'object_type': {
                            'type': 'string',
                            'required': True,
                            'default': 'issue',
                            'enum': ['account', 'issue', 'contact'],
                        },
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the custom field'},
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'description': 'The time the custom field was created',
                                        },
                                        'default_value': {
                                            'type': ['string', 'null'],
                                            'description': 'The default value for single-valued custom fields',
                                        },
                                        'default_values': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'The default values for multi-valued custom fields',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'The description of the custom field',
                                        },
                                        'is_read_only': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the custom field is read-only',
                                        },
                                        'label': {
                                            'type': ['string', 'null'],
                                            'description': 'The label of the custom field',
                                        },
                                        'number_metadata': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'currency': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Currency code',
                                                        },
                                                        'decimal_places': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'Number of decimal places',
                                                        },
                                                        'format': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Number format',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'object_type': {
                                            'type': ['string', 'null'],
                                            'description': 'The object type of the custom field',
                                        },
                                        'select_metadata': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'options': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'label': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The label of the select option',
                                                                    },
                                                                    'slug': {
                                                                        'type': ['string', 'null'],
                                                                        'description': 'The slug of the select option',
                                                                    },
                                                                },
                                                            },
                                                            'description': 'The options for the select field',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                            'description': 'The slug of the custom field',
                                        },
                                        'source': {
                                            'type': ['string', 'null'],
                                            'description': 'The source of the custom field',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of the custom field',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'description': 'The time the custom field was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'custom_fields',
                                    'x-airbyte-stream-name': 'custom_fields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom field definitions in Pylon',
                                        'when_to_use': 'Questions about custom data fields',
                                        'trigger_phrases': ['pylon custom field'],
                                        'freshness': 'static',
                                        'example_questions': ['What custom fields are defined?'],
                                        'search_strategy': 'List all custom fields',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/custom-fields/{id}',
                    action=Action.GET,
                    description='Get a custom field by its ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the custom field'},
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the custom field was created',
                                    },
                                    'default_value': {
                                        'type': ['string', 'null'],
                                        'description': 'The default value for single-valued custom fields',
                                    },
                                    'default_values': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'The default values for multi-valued custom fields',
                                    },
                                    'description': {
                                        'type': ['string', 'null'],
                                        'description': 'The description of the custom field',
                                    },
                                    'is_read_only': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the custom field is read-only',
                                    },
                                    'label': {
                                        'type': ['string', 'null'],
                                        'description': 'The label of the custom field',
                                    },
                                    'number_metadata': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'currency': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Currency code',
                                                    },
                                                    'decimal_places': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'Number of decimal places',
                                                    },
                                                    'format': {
                                                        'type': ['string', 'null'],
                                                        'description': 'Number format',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'object_type': {
                                        'type': ['string', 'null'],
                                        'description': 'The object type of the custom field',
                                    },
                                    'select_metadata': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'options': {
                                                        'type': ['array', 'null'],
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'label': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'The label of the select option',
                                                                },
                                                                'slug': {
                                                                    'type': ['string', 'null'],
                                                                    'description': 'The slug of the select option',
                                                                },
                                                            },
                                                        },
                                                        'description': 'The options for the select field',
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                        'description': 'The slug of the custom field',
                                    },
                                    'source': {
                                        'type': ['string', 'null'],
                                        'description': 'The source of the custom field',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'The type of the custom field',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the custom field was last updated',
                                    },
                                },
                                'x-airbyte-entity-name': 'custom_fields',
                                'x-airbyte-stream-name': 'custom_fields',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Custom field definitions in Pylon',
                                    'when_to_use': 'Questions about custom data fields',
                                    'trigger_phrases': ['pylon custom field'],
                                    'freshness': 'static',
                                    'example_questions': ['What custom fields are defined?'],
                                    'search_strategy': 'List all custom fields',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the custom field'},
                    'created_at': {
                        'type': ['string', 'null'],
                        'description': 'The time the custom field was created',
                    },
                    'default_value': {
                        'type': ['string', 'null'],
                        'description': 'The default value for single-valued custom fields',
                    },
                    'default_values': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                        'description': 'The default values for multi-valued custom fields',
                    },
                    'description': {
                        'type': ['string', 'null'],
                        'description': 'The description of the custom field',
                    },
                    'is_read_only': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the custom field is read-only',
                    },
                    'label': {
                        'type': ['string', 'null'],
                        'description': 'The label of the custom field',
                    },
                    'number_metadata': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/NumberMetadata'},
                            {'type': 'null'},
                        ],
                    },
                    'object_type': {
                        'type': ['string', 'null'],
                        'description': 'The object type of the custom field',
                    },
                    'select_metadata': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/SelectMetadata'},
                            {'type': 'null'},
                        ],
                    },
                    'slug': {
                        'type': ['string', 'null'],
                        'description': 'The slug of the custom field',
                    },
                    'source': {
                        'type': ['string', 'null'],
                        'description': 'The source of the custom field',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of the custom field',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'description': 'The time the custom field was last updated',
                    },
                },
                'x-airbyte-entity-name': 'custom_fields',
                'x-airbyte-stream-name': 'custom_fields',
                'x-airbyte-ai-hints': {
                    'summary': 'Custom field definitions in Pylon',
                    'when_to_use': 'Questions about custom data fields',
                    'trigger_phrases': ['pylon custom field'],
                    'freshness': 'static',
                    'example_questions': ['What custom fields are defined?'],
                    'search_strategy': 'List all custom fields',
                },
            },
            ai_hints={
                'summary': 'Custom field definitions in Pylon',
                'when_to_use': 'Questions about custom data fields',
                'trigger_phrases': ['pylon custom field'],
                'freshness': 'static',
                'example_questions': ['What custom fields are defined?'],
                'search_strategy': 'List all custom fields',
            },
        ),
        EntityDefinition(
            name='ticket_forms',
            stream_name='ticket_forms',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ticket-forms',
                    action=Action.LIST,
                    description='Get a list of ticket forms',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the ticket form'},
                                        'description_html': {
                                            'type': ['string', 'null'],
                                            'description': 'The HTML description of the ticket form',
                                        },
                                        'fields': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'description_html': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The HTML description of the field',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The name of the field',
                                                    },
                                                    'slug': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The slug of the field',
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The type of the field',
                                                    },
                                                },
                                            },
                                            'description': 'The fields of the ticket form',
                                        },
                                        'is_public': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the ticket form is public',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the ticket form',
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                            'description': 'The slug of the ticket form',
                                        },
                                        'url': {
                                            'type': ['string', 'null'],
                                            'description': 'The URL of the ticket form',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'ticket_forms',
                                    'x-airbyte-stream-name': 'ticket_forms',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Ticket form templates in Pylon',
                                        'when_to_use': 'Questions about ticket form configuration',
                                        'trigger_phrases': ['ticket form', 'form template'],
                                        'freshness': 'static',
                                        'example_questions': ['What ticket forms exist in Pylon?'],
                                        'search_strategy': 'List all ticket forms',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the ticket form'},
                    'description_html': {
                        'type': ['string', 'null'],
                        'description': 'The HTML description of the ticket form',
                    },
                    'fields': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/TicketFormField'},
                        'description': 'The fields of the ticket form',
                    },
                    'is_public': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the ticket form is public',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the ticket form',
                    },
                    'slug': {
                        'type': ['string', 'null'],
                        'description': 'The slug of the ticket form',
                    },
                    'url': {
                        'type': ['string', 'null'],
                        'description': 'The URL of the ticket form',
                    },
                },
                'x-airbyte-entity-name': 'ticket_forms',
                'x-airbyte-stream-name': 'ticket_forms',
                'x-airbyte-ai-hints': {
                    'summary': 'Ticket form templates in Pylon',
                    'when_to_use': 'Questions about ticket form configuration',
                    'trigger_phrases': ['ticket form', 'form template'],
                    'freshness': 'static',
                    'example_questions': ['What ticket forms exist in Pylon?'],
                    'search_strategy': 'List all ticket forms',
                },
            },
            ai_hints={
                'summary': 'Ticket form templates in Pylon',
                'when_to_use': 'Questions about ticket form configuration',
                'trigger_phrases': ['ticket form', 'form template'],
                'freshness': 'static',
                'example_questions': ['What ticket forms exist in Pylon?'],
                'search_strategy': 'List all ticket forms',
            },
        ),
        EntityDefinition(
            name='user_roles',
            stream_name='user_roles',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/user-roles',
                    action=Action.LIST,
                    description='Get a list of all user roles',
                    query_params=['cursor'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The ID of the user role'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the user role',
                                        },
                                        'slug': {
                                            'type': ['string', 'null'],
                                            'description': 'The slug of the user role',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'user_roles',
                                    'x-airbyte-stream-name': 'user_roles',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'User role definitions in Pylon',
                                        'when_to_use': 'Questions about role-based access or permissions',
                                        'trigger_phrases': ['pylon role', 'user role'],
                                        'freshness': 'static',
                                        'example_questions': ['What user roles are defined in Pylon?'],
                                        'search_strategy': 'List all roles',
                                    },
                                },
                            },
                            'pagination': {
                                'type': 'object',
                                'properties': {
                                    'cursor': {
                                        'type': ['string', 'null'],
                                        'description': 'The cursor for the next page of results',
                                    },
                                    'has_next_page': {'type': 'boolean', 'description': 'Indicates if there is a next page of results'},
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'next_cursor': '$.pagination.cursor', 'has_next_page': '$.pagination.has_next_page'},
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'The ID of the user role'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the user role',
                    },
                    'slug': {
                        'type': ['string', 'null'],
                        'description': 'The slug of the user role',
                    },
                },
                'x-airbyte-entity-name': 'user_roles',
                'x-airbyte-stream-name': 'user_roles',
                'x-airbyte-ai-hints': {
                    'summary': 'User role definitions in Pylon',
                    'when_to_use': 'Questions about role-based access or permissions',
                    'trigger_phrases': ['pylon role', 'user role'],
                    'freshness': 'static',
                    'example_questions': ['What user roles are defined in Pylon?'],
                    'search_strategy': 'List all roles',
                },
            },
            ai_hints={
                'summary': 'User role definitions in Pylon',
                'when_to_use': 'Questions about role-based access or permissions',
                'trigger_phrases': ['pylon role', 'user role'],
                'freshness': 'static',
                'example_questions': ['What user roles are defined in Pylon?'],
                'search_strategy': 'List all roles',
            },
        ),
        EntityDefinition(
            name='tasks',
            actions=[Action.CREATE, Action.UPDATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/tasks',
                    action=Action.CREATE,
                    description='Create a new task',
                    body_fields=[
                        'title',
                        'body_html',
                        'status',
                        'assignee_id',
                        'project_id',
                        'milestone_id',
                        'due_date',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the task'},
                            'body_html': {'type': 'string', 'description': 'The body HTML of the task'},
                            'status': {'type': 'string', 'description': 'The status of the task (not_started, in_progress, completed)'},
                            'assignee_id': {'type': 'string', 'description': 'The assignee ID for the task'},
                            'project_id': {'type': 'string', 'description': 'The project ID for the task'},
                            'milestone_id': {'type': 'string', 'description': 'The milestone ID for the task'},
                            'due_date': {'type': 'string', 'description': 'The due date for the task (RFC3339)'},
                        },
                        'required': ['title'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the task'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the task',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body HTML of the task',
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'The status of the task',
                                    },
                                    'assignee_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The assignee ID of the task',
                                    },
                                    'project_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The project ID of the task',
                                    },
                                    'milestone_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The milestone ID of the task',
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The due date of the task',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the task was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the task was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/tasks/{id}',
                    action=Action.UPDATE,
                    description='Update an existing task by ID',
                    body_fields=[
                        'title',
                        'body_html',
                        'status',
                        'assignee_id',
                    ],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the task'},
                            'body_html': {'type': 'string', 'description': 'The body HTML of the task'},
                            'status': {'type': 'string', 'description': 'The status of the task (not_started, in_progress, completed)'},
                            'assignee_id': {'type': 'string', 'description': 'The assignee ID for the task'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the task'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the task',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The body HTML of the task',
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'The status of the task',
                                    },
                                    'assignee_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The assignee ID of the task',
                                    },
                                    'project_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The project ID of the task',
                                    },
                                    'milestone_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The milestone ID of the task',
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The due date of the task',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the task was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the task was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='projects',
            actions=[Action.CREATE, Action.UPDATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/projects',
                    action=Action.CREATE,
                    description='Create a new project',
                    body_fields=[
                        'name',
                        'account_id',
                        'description_html',
                        'start_date',
                        'end_date',
                    ],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the project'},
                            'account_id': {'type': 'string', 'description': 'The account ID for the project'},
                            'description_html': {'type': 'string', 'description': 'The HTML description of the project'},
                            'start_date': {'type': 'string', 'description': 'The start date of the project (RFC3339)'},
                            'end_date': {'type': 'string', 'description': 'The end date of the project (RFC3339)'},
                        },
                        'required': ['name', 'account_id'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the project'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the project',
                                    },
                                    'description_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The HTML description of the project',
                                    },
                                    'account_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The account ID of the project',
                                    },
                                    'owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The owner ID of the project',
                                    },
                                    'start_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The start date of the project',
                                    },
                                    'end_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The end date of the project',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the project is archived',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the project was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the project was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/projects/{id}',
                    action=Action.UPDATE,
                    description='Update an existing project by ID',
                    body_fields=['name', 'description_html', 'is_archived'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the project'},
                            'description_html': {'type': 'string', 'description': 'The HTML description of the project'},
                            'is_archived': {'type': 'boolean', 'description': 'Whether the project is archived'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the project'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the project',
                                    },
                                    'description_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The HTML description of the project',
                                    },
                                    'account_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The account ID of the project',
                                    },
                                    'owner_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The owner ID of the project',
                                    },
                                    'start_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The start date of the project',
                                    },
                                    'end_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The end date of the project',
                                    },
                                    'is_archived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the project is archived',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the project was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the project was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='milestones',
            actions=[Action.CREATE, Action.UPDATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/milestones',
                    action=Action.CREATE,
                    description='Create a new milestone',
                    body_fields=['name', 'project_id', 'due_date'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the milestone'},
                            'project_id': {'type': 'string', 'description': 'The project ID for the milestone'},
                            'due_date': {'type': 'string', 'description': 'The due date of the milestone (RFC3339)'},
                        },
                        'required': ['name', 'project_id'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the milestone'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the milestone',
                                    },
                                    'project_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The project ID of the milestone',
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The due date of the milestone',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the milestone was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the milestone was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/milestones/{id}',
                    action=Action.UPDATE,
                    description='Update an existing milestone by ID',
                    body_fields=['name', 'due_date'],
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'description': 'The name of the milestone'},
                            'due_date': {'type': 'string', 'description': 'The due date of the milestone (RFC3339)'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the milestone'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the milestone',
                                    },
                                    'project_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The project ID of the milestone',
                                    },
                                    'due_date': {
                                        'type': ['string', 'null'],
                                        'description': 'The due date of the milestone',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the milestone was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the milestone was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='articles',
            actions=[Action.CREATE, Action.UPDATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/knowledge-bases/{kb_id}/articles',
                    action=Action.CREATE,
                    description='Create a new article in a knowledge base',
                    body_fields=[
                        'title',
                        'body_html',
                        'author_user_id',
                        'slug',
                        'is_published',
                    ],
                    path_params=['kb_id'],
                    path_params_schema={
                        'kb_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the article'},
                            'body_html': {'type': 'string', 'description': 'The HTML body of the article'},
                            'author_user_id': {'type': 'string', 'description': 'The ID of the user attributed as the author'},
                            'slug': {'type': 'string', 'description': 'The slug of the article'},
                            'is_published': {'type': 'boolean', 'description': 'Whether the article should be published'},
                        },
                        'required': ['title', 'body_html', 'author_user_id'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the article'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the article',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The HTML body of the article',
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                        'description': 'The slug of the article',
                                    },
                                    'is_published': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the article is published',
                                    },
                                    'author_user_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The author user ID',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the article was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the article was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='PATCH',
                    path='/knowledge-bases/{kb_id}/articles/{article_id}',
                    action=Action.UPDATE,
                    description='Update an existing article in a knowledge base',
                    body_fields=['title', 'body_html'],
                    path_params=['kb_id', 'article_id'],
                    path_params_schema={
                        'kb_id': {'type': 'string', 'required': True},
                        'article_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the article'},
                            'body_html': {'type': 'string', 'description': 'The HTML body of the article'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the article'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the article',
                                    },
                                    'body_html': {
                                        'type': ['string', 'null'],
                                        'description': 'The HTML body of the article',
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                        'description': 'The slug of the article',
                                    },
                                    'is_published': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the article is published',
                                    },
                                    'author_user_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The author user ID',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the article was created',
                                    },
                                    'updated_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the article was last updated',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='collections',
            actions=[Action.CREATE],
            endpoints={
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/knowledge-bases/{kb_id}/collections',
                    action=Action.CREATE,
                    description='Create a new collection in a knowledge base',
                    body_fields=['title', 'description', 'slug'],
                    path_params=['kb_id'],
                    path_params_schema={
                        'kb_id': {'type': 'string', 'required': True},
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'title': {'type': 'string', 'description': 'The title of the collection'},
                            'description': {'type': 'string', 'description': 'The description of the collection'},
                            'slug': {'type': 'string', 'description': 'The slug of the collection'},
                        },
                        'required': ['title'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the collection'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the collection',
                                    },
                                    'description': {
                                        'type': ['string', 'null'],
                                        'description': 'The description of the collection',
                                    },
                                    'slug': {
                                        'type': ['string', 'null'],
                                        'description': 'The slug of the collection',
                                    },
                                    'created_at': {
                                        'type': ['string', 'null'],
                                        'description': 'The time the collection was created',
                                    },
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='me',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/me',
                    action=Action.GET,
                    description='Get the currently authenticated user',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'The ID of the user'},
                                    'avatar_url': {
                                        'type': ['string', 'null'],
                                        'description': "The URL of the user's avatar",
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'The primary email address of the user',
                                    },
                                    'emails': {
                                        'type': ['array', 'null'],
                                        'items': {'type': 'string'},
                                        'description': 'All email addresses of the user',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the user',
                                    },
                                    'role_id': {
                                        'type': ['string', 'null'],
                                        'description': "The ID of the user's role",
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'The status of the user',
                                    },
                                },
                                'x-airbyte-entity-name': 'users',
                                'x-airbyte-stream-name': 'users',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Pylon users (support agents and admins)',
                                    'when_to_use': 'Looking up support agent details',
                                    'trigger_phrases': ['pylon user', 'support agent'],
                                    'freshness': 'live',
                                    'example_questions': ['Who are the Pylon users?'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='issues',
                suggested=True,
                x_airbyte_name='issues',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the issue',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Title of the issue',
                    ),
                    CacheFieldConfig(
                        name='state',
                        type=['null', 'string'],
                        description='Current state of the issue (e.g. new, in_progress, closed)',
                    ),
                    CacheFieldConfig(
                        name='source',
                        type=['null', 'string'],
                        description='Channel the issue originated from (e.g. email, slack)',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Type classification of the issue',
                    ),
                    CacheFieldConfig(
                        name='number',
                        type=['null', 'integer'],
                        description='Human-readable issue number within the workspace',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Timestamp when the issue was created, in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='latest_message_time',
                        type=['null', 'string'],
                        description='Timestamp of the most recent message on the issue, in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='resolution_time',
                        type=['null', 'string'],
                        description='Timestamp when the issue was resolved, in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='snoozed_until_time',
                        type=['null', 'string'],
                        description='Timestamp the issue is snoozed until, in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='customer_portal_visible',
                        type=['null', 'boolean'],
                        description='Whether the issue is visible in the customer portal',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='accounts',
                suggested=True,
                x_airbyte_name='accounts',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the account',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the account (customer organization)',
                    ),
                    CacheFieldConfig(
                        name='domain',
                        type=['null', 'string'],
                        description='Primary domain associated with the account',
                    ),
                    CacheFieldConfig(
                        name='primary_domain',
                        type=['null', 'string'],
                        description='Canonical primary domain for the account',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Classification of the account (e.g. customer, prospect)',
                    ),
                    CacheFieldConfig(
                        name='is_disabled',
                        type=['null', 'boolean'],
                        description='Whether the account has been disabled',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Timestamp when the account was created, in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='latest_customer_activity_time',
                        type=['null', 'string'],
                        description='Timestamp of the most recent activity from this account, in ISO 8601 format',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='contacts',
                suggested=True,
                x_airbyte_name='contacts',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the contact',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Full name of the contact',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Primary email address of the contact',
                    ),
                    CacheFieldConfig(
                        name='primary_phone_number',
                        type=['null', 'string'],
                        description='Primary phone number of the contact',
                    ),
                    CacheFieldConfig(
                        name='portal_role',
                        type=['null', 'string'],
                        description='Role the contact has in the customer portal',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='teams',
                suggested=True,
                x_airbyte_name='teams',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the team',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Name of the team',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='tags',
                suggested=True,
                x_airbyte_name='tags',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the tag',
                    ),
                    CacheFieldConfig(
                        name='value',
                        type=['null', 'string'],
                        description='Display value of the tag',
                    ),
                    CacheFieldConfig(
                        name='object_type',
                        type=['null', 'string'],
                        description='Type of object this tag applies to (e.g. issue, account)',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='users',
                suggested=True,
                x_airbyte_name='users',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the user',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Full name of the user',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Primary email address of the user',
                    ),
                    CacheFieldConfig(
                        name='role_id',
                        type=['null', 'string'],
                        description="Identifier of the user's role",
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Current status of the user (e.g. active, disabled)',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='custom_fields',
                suggested=True,
                x_airbyte_name='custom_fields',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the custom field',
                    ),
                    CacheFieldConfig(
                        name='label',
                        type=['null', 'string'],
                        description='Display label of the custom field',
                    ),
                    CacheFieldConfig(
                        name='slug',
                        type=['null', 'string'],
                        description='URL-safe identifier for the custom field',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'string'],
                        description='Data type of the custom field (e.g. text, select)',
                    ),
                    CacheFieldConfig(
                        name='object_type',
                        type=['null', 'string'],
                        description='Type of object this custom field applies to (e.g. issue, account)',
                    ),
                    CacheFieldConfig(
                        name='is_read_only',
                        type=['null', 'boolean'],
                        description='Whether the custom field is read-only',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Timestamp when the custom field was created, in ISO 8601 format',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='ticket_forms',
                suggested=True,
                x_airbyte_name='ticket_forms',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the ticket form',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the ticket form',
                    ),
                    CacheFieldConfig(
                        name='slug',
                        type=['null', 'string'],
                        description='URL-safe identifier for the ticket form',
                    ),
                    CacheFieldConfig(
                        name='is_public',
                        type=['null', 'boolean'],
                        description='Whether the ticket form is publicly accessible',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='user_roles',
                x_airbyte_name='user_roles',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type='string',
                        description='Unique identifier for the user role',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the user role',
                    ),
                    CacheFieldConfig(
                        name='slug',
                        type=['null', 'string'],
                        description='URL-safe identifier for the user role',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'issues': [
            'id',
            'title',
            'state',
            'source',
            'type',
            'number',
            'created_at',
            'latest_message_time',
            'resolution_time',
            'snoozed_until_time',
            'customer_portal_visible',
        ],
        'accounts': [
            'id',
            'name',
            'domain',
            'primary_domain',
            'type',
            'is_disabled',
            'created_at',
            'latest_customer_activity_time',
        ],
        'contacts': [
            'id',
            'name',
            'email',
            'primary_phone_number',
            'portal_role',
        ],
        'teams': ['id', 'name'],
        'tags': ['id', 'value', 'object_type'],
        'users': [
            'id',
            'name',
            'email',
            'role_id',
            'status',
        ],
        'custom_fields': [
            'id',
            'label',
            'slug',
            'type',
            'object_type',
            'is_read_only',
            'created_at',
        ],
        'ticket_forms': [
            'id',
            'name',
            'slug',
            'is_public',
        ],
        'user_roles': ['id', 'name', 'slug'],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all open issues in Pylon',
            'Show me all accounts in Pylon',
            'List all contacts in Pylon',
            'What teams are configured in my Pylon workspace?',
            'Show me all tags used in Pylon',
            'List all users in my Pylon account',
            'Show me the custom fields configured for issues',
            'List all ticket forms in Pylon',
            'What user roles are available in Pylon?',
            'Show me details for a specific issue',
            'Get details for a specific account',
            'Show me details for a specific contact',
            'Reply to the customer on an issue saying we are looking into it',
            'Send a message to the customer on the billing issue',
            'Assign an issue to a specific team member',
            'Change the status of an issue to waiting_on_customer',
            'Close an issue as resolved',
            'Delete a test issue',
        ],
        context_store_search=[
            'What are the most common issue sources this month?',
            'Show me issues assigned to a specific team',
            'Which accounts have the most open issues?',
            'Analyze issue resolution times over the last 30 days',
            'List contacts associated with a specific account',
        ],
        search=[
            'What are the most common issue sources this month?',
            'Show me issues assigned to a specific team',
            'Which accounts have the most open issues?',
            'Analyze issue resolution times over the last 30 days',
            'List contacts associated with a specific account',
        ],
        unsupported=['Delete an account', 'Schedule a meeting with a contact'],
    ),
)