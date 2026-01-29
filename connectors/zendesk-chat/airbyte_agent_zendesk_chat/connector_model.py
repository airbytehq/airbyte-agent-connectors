"""
Connector model for zendesk-chat.

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

ZendeskChatConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('40d24d0f-b8f9-4fe0-9e6c-b06c0f3f45e4'),
    name='zendesk-chat',
    version='0.1.6',
    base_url='https://{subdomain}.zendesk.com/api/v2/chat',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='OAuth 2.0 Access Token',
            description='Authenticate using an OAuth 2.0 access token from Zendesk',
            type='object',
            required=['access_token'],
            properties={
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Your Zendesk Chat OAuth 2.0 access token',
                ),
            },
            auth_mapping={'token': '${access_token}'},
            replication_auth_key_mapping={'credentials.access_token': 'access_token'},
            replication_auth_key_constants={'credentials.credentials': 'access_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='accounts',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/account',
                    action=Action.GET,
                    description='Returns the account information for the authenticated user',
                    response_schema={
                        'type': 'object',
                        'description': 'Zendesk Chat account information',
                        'properties': {
                            'account_key': {'type': 'string', 'description': 'Unique account key identifier'},
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'Account status',
                            },
                            'create_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the account was created',
                            },
                            'billing': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Account billing information',
                                        'properties': {
                                            'company': {
                                                'type': ['string', 'null'],
                                            },
                                            'first_name': {
                                                'type': ['string', 'null'],
                                            },
                                            'last_name': {
                                                'type': ['string', 'null'],
                                            },
                                            'email': {
                                                'type': ['string', 'null'],
                                            },
                                            'phone': {
                                                'type': ['string', 'null'],
                                            },
                                            'address1': {
                                                'type': ['string', 'null'],
                                            },
                                            'address2': {
                                                'type': ['string', 'null'],
                                            },
                                            'city': {
                                                'type': ['string', 'null'],
                                            },
                                            'state': {
                                                'type': ['string', 'null'],
                                            },
                                            'postal_code': {
                                                'type': ['string', 'null'],
                                            },
                                            'country_code': {
                                                'type': ['string', 'null'],
                                            },
                                            'additional_info': {
                                                'type': ['string', 'null'],
                                            },
                                            'cycle': {
                                                'type': ['integer', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Billing information',
                            },
                            'plan': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Account plan details',
                                        'properties': {
                                            'name': {
                                                'type': ['string', 'null'],
                                            },
                                            'price': {
                                                'type': ['number', 'null'],
                                            },
                                            'max_agents': {
                                                'type': ['integer', 'null'],
                                            },
                                            'max_departments': {
                                                'type': ['string', 'null'],
                                            },
                                            'max_concurrent_chats': {
                                                'type': ['string', 'null'],
                                            },
                                            'max_history_search_days': {
                                                'type': ['string', 'null'],
                                            },
                                            'max_advanced_triggers': {
                                                'type': ['string', 'null'],
                                            },
                                            'max_basic_triggers': {
                                                'type': ['string', 'null'],
                                            },
                                            'analytics': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'file_upload': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'rest_api': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'goals': {
                                                'type': ['integer', 'null'],
                                            },
                                            'high_load': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'integrations': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'ip_restriction': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'monitoring': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'operating_hours': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'sla': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'support': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'unbranding': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'agent_leaderboard': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'agent_reports': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'chat_reports': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'daily_reports': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'email_reports': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'widget_customization': {
                                                'type': ['string', 'null'],
                                            },
                                            'long_desc': {
                                                'type': ['string', 'null'],
                                            },
                                            'short_desc': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Account plan details',
                            },
                        },
                        'required': ['account_key'],
                        'x-airbyte-entity-name': 'accounts',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zendesk Chat account information',
                'properties': {
                    'account_key': {'type': 'string', 'description': 'Unique account key identifier'},
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Account status',
                    },
                    'create_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the account was created',
                    },
                    'billing': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Billing'},
                            {'type': 'null'},
                        ],
                        'description': 'Billing information',
                    },
                    'plan': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Plan'},
                            {'type': 'null'},
                        ],
                        'description': 'Account plan details',
                    },
                },
                'required': ['account_key'],
                'x-airbyte-entity-name': 'accounts',
            },
        ),
        EntityDefinition(
            name='agents',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/agents',
                    action=Action.LIST,
                    description='List all agents',
                    query_params=['limit', 'since_id'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Zendesk Chat agent',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique agent identifier'},
                                'email': {
                                    'type': ['string', 'null'],
                                    'description': 'Agent email address',
                                },
                                'display_name': {
                                    'type': ['string', 'null'],
                                    'description': 'Agent display name shown in chat',
                                },
                                'first_name': {
                                    'type': ['string', 'null'],
                                    'description': 'Agent first name',
                                },
                                'last_name': {
                                    'type': ['string', 'null'],
                                    'description': 'Agent last name',
                                },
                                'enabled': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether agent is enabled for chat',
                                },
                                'role_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Agent role ID',
                                },
                                'roles': {
                                    'oneOf': [
                                        {
                                            'type': 'object',
                                            'description': 'Agent role flags',
                                            'properties': {
                                                'administrator': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'owner': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                        {'type': 'null'},
                                    ],
                                    'description': 'Agent role flags',
                                },
                                'departments': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                    'description': 'Department IDs agent belongs to',
                                },
                                'enabled_departments': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                    'description': 'Department IDs where agent is enabled',
                                },
                                'skills': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                    'description': 'Skill IDs assigned to agent',
                                },
                                'scope': {
                                    'type': ['string', 'null'],
                                    'description': 'Agent scope',
                                },
                                'create_date': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When agent was created',
                                },
                                'last_login': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'Last login timestamp',
                                },
                                'login_count': {
                                    'type': ['integer', 'null'],
                                    'description': 'Total login count',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'agents',
                        },
                    },
                    record_extractor='$',
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/agents/{agent_id}',
                    action=Action.GET,
                    description='Get an agent',
                    path_params=['agent_id'],
                    path_params_schema={
                        'agent_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Zendesk Chat agent',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique agent identifier'},
                            'email': {
                                'type': ['string', 'null'],
                                'description': 'Agent email address',
                            },
                            'display_name': {
                                'type': ['string', 'null'],
                                'description': 'Agent display name shown in chat',
                            },
                            'first_name': {
                                'type': ['string', 'null'],
                                'description': 'Agent first name',
                            },
                            'last_name': {
                                'type': ['string', 'null'],
                                'description': 'Agent last name',
                            },
                            'enabled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether agent is enabled for chat',
                            },
                            'role_id': {
                                'type': ['integer', 'null'],
                                'description': 'Agent role ID',
                            },
                            'roles': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'description': 'Agent role flags',
                                        'properties': {
                                            'administrator': {
                                                'type': ['boolean', 'null'],
                                            },
                                            'owner': {
                                                'type': ['boolean', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                                'description': 'Agent role flags',
                            },
                            'departments': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                                'description': 'Department IDs agent belongs to',
                            },
                            'enabled_departments': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                                'description': 'Department IDs where agent is enabled',
                            },
                            'skills': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                                'description': 'Skill IDs assigned to agent',
                            },
                            'scope': {
                                'type': ['string', 'null'],
                                'description': 'Agent scope',
                            },
                            'create_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When agent was created',
                            },
                            'last_login': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'Last login timestamp',
                            },
                            'login_count': {
                                'type': ['integer', 'null'],
                                'description': 'Total login count',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'agents',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zendesk Chat agent',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique agent identifier'},
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'Agent email address',
                    },
                    'display_name': {
                        'type': ['string', 'null'],
                        'description': 'Agent display name shown in chat',
                    },
                    'first_name': {
                        'type': ['string', 'null'],
                        'description': 'Agent first name',
                    },
                    'last_name': {
                        'type': ['string', 'null'],
                        'description': 'Agent last name',
                    },
                    'enabled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether agent is enabled for chat',
                    },
                    'role_id': {
                        'type': ['integer', 'null'],
                        'description': 'Agent role ID',
                    },
                    'roles': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/AgentRoles'},
                            {'type': 'null'},
                        ],
                        'description': 'Agent role flags',
                    },
                    'departments': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                        'description': 'Department IDs agent belongs to',
                    },
                    'enabled_departments': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                        'description': 'Department IDs where agent is enabled',
                    },
                    'skills': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                        'description': 'Skill IDs assigned to agent',
                    },
                    'scope': {
                        'type': ['string', 'null'],
                        'description': 'Agent scope',
                    },
                    'create_date': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When agent was created',
                    },
                    'last_login': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'Last login timestamp',
                    },
                    'login_count': {
                        'type': ['integer', 'null'],
                        'description': 'Total login count',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'agents',
            },
        ),
        EntityDefinition(
            name='agent_timeline',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/incremental/agent_timeline',
                    action=Action.LIST,
                    description='List agent timeline (incremental export)',
                    query_params=['start_time', 'limit', 'fields'],
                    query_params_schema={
                        'start_time': {'type': 'integer', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'agent_timeline(*)',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'agent_timeline': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Agent activity timeline entry',
                                    'properties': {
                                        'agent_id': {'type': 'integer', 'description': 'Agent identifier'},
                                        'start_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                        },
                                        'duration': {
                                            'type': ['number', 'null'],
                                        },
                                        'engagement_count': {
                                            'type': ['integer', 'null'],
                                        },
                                    },
                                    'required': ['agent_id'],
                                    'x-airbyte-entity-name': 'agent_timeline',
                                },
                            },
                            'next_page': {
                                'type': ['string', 'null'],
                            },
                            'count': {'type': 'integer'},
                            'end_time': {
                                'type': ['integer', 'null'],
                            },
                        },
                    },
                    record_extractor='$.agent_timeline',
                    meta_extractor={'next_page': '$.next_page', 'count': '$.count'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Agent activity timeline entry',
                'properties': {
                    'agent_id': {'type': 'integer', 'description': 'Agent identifier'},
                    'start_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'status': {
                        'type': ['string', 'null'],
                    },
                    'duration': {
                        'type': ['number', 'null'],
                    },
                    'engagement_count': {
                        'type': ['integer', 'null'],
                    },
                },
                'required': ['agent_id'],
                'x-airbyte-entity-name': 'agent_timeline',
            },
        ),
        EntityDefinition(
            name='bans',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/bans',
                    action=Action.LIST,
                    description='List all bans',
                    query_params=['limit', 'since_id'],
                    query_params_schema={
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'since_id': {'type': 'integer', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'ip_address': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Banned visitor',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique ban identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Ban type (ip_address or visitor)',
                                        },
                                        'ip_address': {
                                            'type': ['string', 'null'],
                                        },
                                        'visitor_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'visitor_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'reason': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'bans',
                                },
                            },
                            'visitor': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Banned visitor',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'Unique ban identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Ban type (ip_address or visitor)',
                                        },
                                        'ip_address': {
                                            'type': ['string', 'null'],
                                        },
                                        'visitor_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'visitor_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'reason': {
                                            'type': ['string', 'null'],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'bans',
                                },
                            },
                        },
                    },
                    record_extractor='$[*][*]',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/bans/{ban_id}',
                    action=Action.GET,
                    description='Get a ban',
                    path_params=['ban_id'],
                    path_params_schema={
                        'ban_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Banned visitor',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique ban identifier'},
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'Ban type (ip_address or visitor)',
                            },
                            'ip_address': {
                                'type': ['string', 'null'],
                            },
                            'visitor_id': {
                                'type': ['string', 'null'],
                            },
                            'visitor_name': {
                                'type': ['string', 'null'],
                            },
                            'reason': {
                                'type': ['string', 'null'],
                            },
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'bans',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Banned visitor',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique ban identifier'},
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Ban type (ip_address or visitor)',
                    },
                    'ip_address': {
                        'type': ['string', 'null'],
                    },
                    'visitor_id': {
                        'type': ['string', 'null'],
                    },
                    'visitor_name': {
                        'type': ['string', 'null'],
                    },
                    'reason': {
                        'type': ['string', 'null'],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'bans',
            },
        ),
        EntityDefinition(
            name='chats',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/incremental/chats',
                    action=Action.LIST,
                    description='List chats (incremental export)',
                    query_params=['start_time', 'limit', 'fields'],
                    query_params_schema={
                        'start_time': {'type': 'integer', 'required': False},
                        'limit': {
                            'type': 'integer',
                            'required': False,
                            'default': 1000,
                        },
                        'fields': {
                            'type': 'string',
                            'required': False,
                            'default': 'chats(*)',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'chats': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Chat conversation transcript',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique chat identifier'},
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'update_timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'duration': {
                                            'type': ['integer', 'null'],
                                        },
                                        'department_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'department_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'agent_ids': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'agent_names': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'visitor': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'phone': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'notes': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'session': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'browser': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'platform': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'user_agent': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'ip': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'city': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'region': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_code': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'country_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'start_date': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                        },
                                                        'end_date': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'history': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'timestamp': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'nick': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'msg': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'msg_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'channel': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'department_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'department_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'rating': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'new_rating': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'tags': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                    },
                                                    'new_tags': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'string'},
                                                    },
                                                    'options': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'engagements': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'agent_id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'agent_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'agent_full_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'department_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'timestamp': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'duration': {
                                                        'type': ['number', 'null'],
                                                    },
                                                    'accepted': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'assigned': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'started_by': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'rating': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'comment': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'count': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'total': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                    'agent': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                    'visitor': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'response_time': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'first': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                    'avg': {
                                                                        'type': ['number', 'null'],
                                                                    },
                                                                    'max': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                    'skills_requested': {
                                                        'type': ['array', 'null'],
                                                        'items': {'type': 'integer'},
                                                    },
                                                    'skills_fulfilled': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'conversions': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'goal_id': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                    'goal_name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'timestamp': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                    'attribution': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'agent_id': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                    'agent_name': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'department_id': {
                                                                        'type': ['integer', 'null'],
                                                                    },
                                                                    'department_name': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'chat_timestamp': {
                                                                        'type': ['string', 'null'],
                                                                        'format': 'date-time',
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                },
                                            },
                                        },
                                        'count': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'total': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'agent': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'visitor': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'response_time': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'first': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'avg': {
                                                            'type': ['number', 'null'],
                                                        },
                                                        'max': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'rating': {
                                            'type': ['string', 'null'],
                                        },
                                        'comment': {
                                            'type': ['string', 'null'],
                                        },
                                        'tags': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'started_by': {
                                            'type': ['string', 'null'],
                                        },
                                        'triggered': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'triggered_response': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'missed': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'unread': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'deleted': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'message': {
                                            'type': ['string', 'null'],
                                        },
                                        'webpath': {
                                            'type': ['array', 'null'],
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'from': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'timestamp': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                    },
                                                },
                                            },
                                        },
                                        'zendesk_ticket_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'Associated Zendesk Support ticket ID',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'chats',
                                },
                            },
                            'next_page': {
                                'type': ['string', 'null'],
                            },
                            'count': {'type': 'integer'},
                            'end_id': {
                                'type': ['string', 'null'],
                            },
                            'end_time': {
                                'type': ['integer', 'null'],
                            },
                        },
                    },
                    record_extractor='$.chats',
                    meta_extractor={'next_page': '$.next_page', 'count': '$.count'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/chats/{chat_id}',
                    action=Action.GET,
                    description='Get a chat',
                    path_params=['chat_id'],
                    path_params_schema={
                        'chat_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Chat conversation transcript',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Unique chat identifier'},
                            'type': {
                                'type': ['string', 'null'],
                            },
                            'timestamp': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                            },
                            'update_timestamp': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                            },
                            'duration': {
                                'type': ['integer', 'null'],
                            },
                            'department_id': {
                                'type': ['integer', 'null'],
                            },
                            'department_name': {
                                'type': ['string', 'null'],
                            },
                            'agent_ids': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                            },
                            'agent_names': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                            },
                            'visitor': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['string', 'null'],
                                            },
                                            'name': {
                                                'type': ['string', 'null'],
                                            },
                                            'email': {
                                                'type': ['string', 'null'],
                                            },
                                            'phone': {
                                                'type': ['string', 'null'],
                                            },
                                            'notes': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'session': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['string', 'null'],
                                            },
                                            'browser': {
                                                'type': ['string', 'null'],
                                            },
                                            'platform': {
                                                'type': ['string', 'null'],
                                            },
                                            'user_agent': {
                                                'type': ['string', 'null'],
                                            },
                                            'ip': {
                                                'type': ['string', 'null'],
                                            },
                                            'city': {
                                                'type': ['string', 'null'],
                                            },
                                            'region': {
                                                'type': ['string', 'null'],
                                            },
                                            'country_code': {
                                                'type': ['string', 'null'],
                                            },
                                            'country_name': {
                                                'type': ['string', 'null'],
                                            },
                                            'start_date': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                            },
                                            'end_date': {
                                                'type': ['string', 'null'],
                                                'format': 'date-time',
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'history': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'type': {
                                            'type': ['string', 'null'],
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                        },
                                        'nick': {
                                            'type': ['string', 'null'],
                                        },
                                        'msg': {
                                            'type': ['string', 'null'],
                                        },
                                        'msg_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'channel': {
                                            'type': ['string', 'null'],
                                        },
                                        'department_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'department_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'rating': {
                                            'type': ['string', 'null'],
                                        },
                                        'new_rating': {
                                            'type': ['string', 'null'],
                                        },
                                        'tags': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'new_tags': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                        },
                                        'options': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                },
                            },
                            'engagements': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'agent_id': {
                                            'type': ['string', 'null'],
                                        },
                                        'agent_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'agent_full_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'department_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'duration': {
                                            'type': ['number', 'null'],
                                        },
                                        'accepted': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'assigned': {
                                            'type': ['boolean', 'null'],
                                        },
                                        'started_by': {
                                            'type': ['string', 'null'],
                                        },
                                        'rating': {
                                            'type': ['string', 'null'],
                                        },
                                        'comment': {
                                            'type': ['string', 'null'],
                                        },
                                        'count': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'total': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'agent': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'visitor': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'response_time': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'first': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'avg': {
                                                            'type': ['number', 'null'],
                                                        },
                                                        'max': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'skills_requested': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'integer'},
                                        },
                                        'skills_fulfilled': {
                                            'type': ['boolean', 'null'],
                                        },
                                    },
                                },
                            },
                            'conversions': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['string', 'null'],
                                        },
                                        'goal_id': {
                                            'type': ['integer', 'null'],
                                        },
                                        'goal_name': {
                                            'type': ['string', 'null'],
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                        'attribution': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'agent_id': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'agent_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'department_id': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                        'department_name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'chat_timestamp': {
                                                            'type': ['string', 'null'],
                                                            'format': 'date-time',
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                    },
                                },
                            },
                            'count': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'total': {
                                                'type': ['integer', 'null'],
                                            },
                                            'agent': {
                                                'type': ['integer', 'null'],
                                            },
                                            'visitor': {
                                                'type': ['integer', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'response_time': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'first': {
                                                'type': ['integer', 'null'],
                                            },
                                            'avg': {
                                                'type': ['number', 'null'],
                                            },
                                            'max': {
                                                'type': ['integer', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                            'rating': {
                                'type': ['string', 'null'],
                            },
                            'comment': {
                                'type': ['string', 'null'],
                            },
                            'tags': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                            },
                            'started_by': {
                                'type': ['string', 'null'],
                            },
                            'triggered': {
                                'type': ['boolean', 'null'],
                            },
                            'triggered_response': {
                                'type': ['boolean', 'null'],
                            },
                            'missed': {
                                'type': ['boolean', 'null'],
                            },
                            'unread': {
                                'type': ['boolean', 'null'],
                            },
                            'deleted': {
                                'type': ['boolean', 'null'],
                            },
                            'message': {
                                'type': ['string', 'null'],
                            },
                            'webpath': {
                                'type': ['array', 'null'],
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'from': {
                                            'type': ['string', 'null'],
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                        },
                                    },
                                },
                            },
                            'zendesk_ticket_id': {
                                'type': ['integer', 'null'],
                                'description': 'Associated Zendesk Support ticket ID',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'chats',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Chat conversation transcript',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique chat identifier'},
                    'type': {
                        'type': ['string', 'null'],
                    },
                    'timestamp': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'update_timestamp': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                    },
                    'duration': {
                        'type': ['integer', 'null'],
                    },
                    'department_id': {
                        'type': ['integer', 'null'],
                    },
                    'department_name': {
                        'type': ['string', 'null'],
                    },
                    'agent_ids': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'agent_names': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'visitor': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Visitor'},
                            {'type': 'null'},
                        ],
                    },
                    'session': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ChatSession'},
                            {'type': 'null'},
                        ],
                    },
                    'history': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/ChatHistoryItem'},
                    },
                    'engagements': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/ChatEngagement'},
                    },
                    'conversions': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/ChatConversion'},
                    },
                    'count': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/MessageCount'},
                            {'type': 'null'},
                        ],
                    },
                    'response_time': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ResponseTime'},
                            {'type': 'null'},
                        ],
                    },
                    'rating': {
                        'type': ['string', 'null'],
                    },
                    'comment': {
                        'type': ['string', 'null'],
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'started_by': {
                        'type': ['string', 'null'],
                    },
                    'triggered': {
                        'type': ['boolean', 'null'],
                    },
                    'triggered_response': {
                        'type': ['boolean', 'null'],
                    },
                    'missed': {
                        'type': ['boolean', 'null'],
                    },
                    'unread': {
                        'type': ['boolean', 'null'],
                    },
                    'deleted': {
                        'type': ['boolean', 'null'],
                    },
                    'message': {
                        'type': ['string', 'null'],
                    },
                    'webpath': {
                        'type': ['array', 'null'],
                        'items': {'$ref': '#/components/schemas/WebpathItem'},
                    },
                    'zendesk_ticket_id': {
                        'type': ['integer', 'null'],
                        'description': 'Associated Zendesk Support ticket ID',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'chats',
            },
        ),
        EntityDefinition(
            name='departments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/departments',
                    action=Action.LIST,
                    description='List all departments',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'description': {
                                    'type': ['string', 'null'],
                                },
                                'enabled': {
                                    'type': ['boolean', 'null'],
                                },
                                'members': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                },
                                'settings': {
                                    'oneOf': [
                                        {
                                            'type': 'object',
                                            'properties': {
                                                'chat_limit': {
                                                    'type': ['integer', 'null'],
                                                },
                                            },
                                        },
                                        {'type': 'null'},
                                    ],
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'departments',
                        },
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/departments/{department_id}',
                    action=Action.GET,
                    description='Get a department',
                    path_params=['department_id'],
                    path_params_schema={
                        'department_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'description': {
                                'type': ['string', 'null'],
                            },
                            'enabled': {
                                'type': ['boolean', 'null'],
                            },
                            'members': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                            },
                            'settings': {
                                'oneOf': [
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'chat_limit': {
                                                'type': ['integer', 'null'],
                                            },
                                        },
                                    },
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'departments',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'description': {
                        'type': ['string', 'null'],
                    },
                    'enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'members': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'settings': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/DepartmentSettings'},
                            {'type': 'null'},
                        ],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'departments',
            },
        ),
        EntityDefinition(
            name='goals',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/goals',
                    action=Action.LIST,
                    description='List all goals',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'description': {
                                    'type': ['string', 'null'],
                                },
                                'enabled': {
                                    'type': ['boolean', 'null'],
                                },
                                'attribution_model': {
                                    'type': ['string', 'null'],
                                },
                                'attribution_window': {
                                    'type': ['integer', 'null'],
                                },
                                'attribution_period': {
                                    'type': ['integer', 'null'],
                                },
                                'settings': {
                                    'type': ['object', 'null'],
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'goals',
                        },
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/goals/{goal_id}',
                    action=Action.GET,
                    description='Get a goal',
                    path_params=['goal_id'],
                    path_params_schema={
                        'goal_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'description': {
                                'type': ['string', 'null'],
                            },
                            'enabled': {
                                'type': ['boolean', 'null'],
                            },
                            'attribution_model': {
                                'type': ['string', 'null'],
                            },
                            'attribution_window': {
                                'type': ['integer', 'null'],
                            },
                            'attribution_period': {
                                'type': ['integer', 'null'],
                            },
                            'settings': {
                                'type': ['object', 'null'],
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'goals',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'description': {
                        'type': ['string', 'null'],
                    },
                    'enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'attribution_model': {
                        'type': ['string', 'null'],
                    },
                    'attribution_window': {
                        'type': ['integer', 'null'],
                    },
                    'attribution_period': {
                        'type': ['integer', 'null'],
                    },
                    'settings': {
                        'type': ['object', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'goals',
            },
        ),
        EntityDefinition(
            name='roles',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/roles',
                    action=Action.LIST,
                    description='List all roles',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'description': {
                                    'type': ['string', 'null'],
                                },
                                'enabled': {
                                    'type': ['boolean', 'null'],
                                },
                                'permissions': {
                                    'type': ['object', 'null'],
                                },
                                'members_count': {
                                    'type': ['integer', 'null'],
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'roles',
                        },
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/roles/{role_id}',
                    action=Action.GET,
                    description='Get a role',
                    path_params=['role_id'],
                    path_params_schema={
                        'role_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'description': {
                                'type': ['string', 'null'],
                            },
                            'enabled': {
                                'type': ['boolean', 'null'],
                            },
                            'permissions': {
                                'type': ['object', 'null'],
                            },
                            'members_count': {
                                'type': ['integer', 'null'],
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'roles',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'description': {
                        'type': ['string', 'null'],
                    },
                    'enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'permissions': {
                        'type': ['object', 'null'],
                    },
                    'members_count': {
                        'type': ['integer', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'roles',
            },
        ),
        EntityDefinition(
            name='routing_settings',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/routing_settings/account',
                    action=Action.GET,
                    description='Get routing settings',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'routing_mode': {
                                        'type': ['string', 'null'],
                                    },
                                    'chat_limit': {
                                        'type': ['object', 'null'],
                                    },
                                    'skill_routing': {
                                        'type': ['object', 'null'],
                                    },
                                    'reassignment': {
                                        'type': ['object', 'null'],
                                    },
                                    'auto_idle': {
                                        'type': ['object', 'null'],
                                    },
                                    'auto_accept': {
                                        'type': ['object', 'null'],
                                    },
                                },
                                'x-airbyte-entity-name': 'routing_settings',
                            },
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'routing_mode': {
                        'type': ['string', 'null'],
                    },
                    'chat_limit': {
                        'type': ['object', 'null'],
                    },
                    'skill_routing': {
                        'type': ['object', 'null'],
                    },
                    'reassignment': {
                        'type': ['object', 'null'],
                    },
                    'auto_idle': {
                        'type': ['object', 'null'],
                    },
                    'auto_accept': {
                        'type': ['object', 'null'],
                    },
                },
                'x-airbyte-entity-name': 'routing_settings',
            },
        ),
        EntityDefinition(
            name='shortcuts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/shortcuts',
                    action=Action.LIST,
                    description='List all shortcuts',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Shortcut name/identifier'},
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'message': {
                                    'type': ['string', 'null'],
                                },
                                'options': {
                                    'type': ['string', 'null'],
                                },
                                'tags': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'string'},
                                },
                                'departments': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                },
                                'agents': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                },
                                'scope': {
                                    'type': ['string', 'null'],
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'shortcuts',
                        },
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/shortcuts/{shortcut_id}',
                    action=Action.GET,
                    description='Get a shortcut',
                    path_params=['shortcut_id'],
                    path_params_schema={
                        'shortcut_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Shortcut name/identifier'},
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'message': {
                                'type': ['string', 'null'],
                            },
                            'options': {
                                'type': ['string', 'null'],
                            },
                            'tags': {
                                'type': ['array', 'null'],
                                'items': {'type': 'string'},
                            },
                            'departments': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                            },
                            'agents': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                            },
                            'scope': {
                                'type': ['string', 'null'],
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'shortcuts',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Shortcut name/identifier'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'message': {
                        'type': ['string', 'null'],
                    },
                    'options': {
                        'type': ['string', 'null'],
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'items': {'type': 'string'},
                    },
                    'departments': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'agents': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'scope': {
                        'type': ['string', 'null'],
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'shortcuts',
            },
        ),
        EntityDefinition(
            name='skills',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/skills',
                    action=Action.LIST,
                    description='List all skills',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'description': {
                                    'type': ['string', 'null'],
                                },
                                'enabled': {
                                    'type': ['boolean', 'null'],
                                },
                                'members': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'skills',
                        },
                    },
                    record_extractor='$',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/skills/{skill_id}',
                    action=Action.GET,
                    description='Get a skill',
                    path_params=['skill_id'],
                    path_params_schema={
                        'skill_id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'name': {
                                'type': ['string', 'null'],
                            },
                            'description': {
                                'type': ['string', 'null'],
                            },
                            'enabled': {
                                'type': ['boolean', 'null'],
                            },
                            'members': {
                                'type': ['array', 'null'],
                                'items': {'type': 'integer'},
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'skills',
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'description': {
                        'type': ['string', 'null'],
                    },
                    'enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'members': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'skills',
            },
        ),
        EntityDefinition(
            name='triggers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/triggers',
                    action=Action.LIST,
                    description='List all triggers',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'name': {
                                    'type': ['string', 'null'],
                                },
                                'description': {
                                    'type': ['string', 'null'],
                                },
                                'enabled': {
                                    'type': ['boolean', 'null'],
                                },
                                'run_once': {
                                    'type': ['boolean', 'null'],
                                },
                                'conditions': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'object'},
                                },
                                'actions': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'object'},
                                },
                                'departments': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'integer'},
                                },
                                'definition': {
                                    'type': ['object', 'null'],
                                    'description': 'Trigger definition with conditions, events, and actions',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'triggers',
                        },
                    },
                    record_extractor='$',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {
                        'type': ['string', 'null'],
                    },
                    'description': {
                        'type': ['string', 'null'],
                    },
                    'enabled': {
                        'type': ['boolean', 'null'],
                    },
                    'run_once': {
                        'type': ['boolean', 'null'],
                    },
                    'conditions': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'actions': {
                        'type': ['array', 'null'],
                        'items': {'type': 'object'},
                    },
                    'departments': {
                        'type': ['array', 'null'],
                        'items': {'type': 'integer'},
                    },
                    'definition': {
                        'type': ['object', 'null'],
                        'description': 'Trigger definition with conditions, events, and actions',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'triggers',
            },
        ),
    ],
    search_field_paths={
        'agents': [
            'id',
            'email',
            'display_name',
            'first_name',
            'last_name',
            'enabled',
            'role_id',
            'departments',
            'departments[]',
            'create_date',
        ],
        'chats': [
            'id',
            'timestamp',
            'update_timestamp',
            'department_id',
            'department_name',
            'duration',
            'rating',
            'missed',
            'agent_ids',
            'agent_ids[]',
        ],
        'departments': [
            'id',
            'name',
            'enabled',
            'members',
            'members[]',
        ],
        'shortcuts': [
            'id',
            'name',
            'message',
            'tags',
            'tags[]',
        ],
        'triggers': ['id', 'name', 'enabled'],
    },
)