"""
Connector model for pylon.

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

PylonConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('f2e53e88-3c6b-4e5a-b7c2-a1d9c5e8f4b6'),
    name='pylon',
    version='0.1.2',
    base_url='https://api.usepylon.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
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
            actions=[
                Action.LIST,
                Action.CREATE,
                Action.GET,
                Action.UPDATE,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/issues',
                    action=Action.LIST,
                    description='Get a list of issues within a time range',
                    query_params=['start_time', 'end_time', 'cursor'],
                    query_params_schema={
                        'start_time': {'type': 'string', 'required': True},
                        'end_time': {'type': 'string', 'required': True},
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
                                        'type': {
                                            'oneOf': [
                                                {
                                                    'type': 'string',
                                                    'enum': ['Conversation', 'Ticket'],
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'issues',
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
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['Conversation', 'Ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
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
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['Conversation', 'Ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
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
                                    'type': {
                                        'oneOf': [
                                            {
                                                'type': 'string',
                                                'enum': ['Conversation', 'Ticket'],
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'x-airbyte-entity-name': 'issues',
                            },
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
                    'type': {
                        'oneOf': [
                            {
                                'type': 'string',
                                'enum': ['Conversation', 'Ticket'],
                            },
                            {'type': 'null'},
                        ],
                    },
                },
                'x-airbyte-entity-name': 'issues',
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
            },
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
            },
        ),
        EntityDefinition(
            name='contacts',
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
            },
        ),
        EntityDefinition(
            name='teams',
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
            },
        ),
        EntityDefinition(
            name='tags',
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
            },
        ),
        EntityDefinition(
            name='users',
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
            },
        ),
        EntityDefinition(
            name='custom_fields',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/custom-fields',
                    action=Action.LIST,
                    description='Get all custom fields for a given object type',
                    query_params=['object_type', 'cursor'],
                    query_params_schema={
                        'object_type': {'type': 'string', 'required': True},
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
            },
        ),
        EntityDefinition(
            name='ticket_forms',
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
            },
        ),
        EntityDefinition(
            name='user_roles',
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
                            },
                            'request_id': {'type': 'string', 'description': 'The request ID for tracking'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
        ),
    ],
)