"""
Connector model for twilio.

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

TwilioConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('b9dc6155-672e-42ea-b10d-9f1f1fb95ab1'),
    name='twilio',
    version='1.0.1',
    base_url='https://api.twilio.com/2010-04-01',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
            title='Twilio Authentication',
            type='object',
            required=['account_sid', 'auth_token'],
            properties={
                'account_sid': AuthConfigFieldSpec(
                    title='Account SID',
                    description='Your Twilio Account SID (starts with AC)',
                    pattern='^AC',
                ),
                'auth_token': AuthConfigFieldSpec(
                    title='Auth Token',
                    description='Your Twilio Auth Token',
                ),
            },
            auth_mapping={'username': '${account_sid}', 'password': '${auth_token}'},
            replication_auth_key_mapping={'account_sid': 'account_sid', 'auth_token': 'auth_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='accounts',
            stream_name='accounts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts.json',
                    action=Action.LIST,
                    description='Returns a list of accounts associated with the authenticated account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of accounts',
                        'properties': {
                            'accounts': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio account',
                                    'properties': {
                                        'auth_token': {
                                            'type': ['null', 'string'],
                                            'description': 'The authentication token for the account',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The timestamp when the account was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The timestamp when the account was last updated',
                                        },
                                        'friendly_name': {
                                            'type': ['null', 'string'],
                                            'description': 'A user-defined friendly name for the account',
                                        },
                                        'owner_account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the owner account',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the account',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'The current status of the account',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for accessing various subresources related to the account',
                                            'additionalProperties': True,
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'The type of the account',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI for accessing the account resource',
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'accounts',
                                    'x-airbyte-stream-name': 'accounts',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.accounts',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{sid}.json',
                    action=Action.GET,
                    description='Get a single account by SID',
                    path_params=['sid'],
                    path_params_schema={
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio account',
                        'properties': {
                            'auth_token': {
                                'type': ['null', 'string'],
                                'description': 'The authentication token for the account',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The timestamp when the account was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The timestamp when the account was last updated',
                            },
                            'friendly_name': {
                                'type': ['null', 'string'],
                                'description': 'A user-defined friendly name for the account',
                            },
                            'owner_account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the owner account',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the account',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'The current status of the account',
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'URIs for accessing various subresources related to the account',
                                'additionalProperties': True,
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'The type of the account',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI for accessing the account resource',
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'accounts',
                        'x-airbyte-stream-name': 'accounts',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio account',
                'properties': {
                    'auth_token': {
                        'type': ['null', 'string'],
                        'description': 'The authentication token for the account',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The timestamp when the account was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The timestamp when the account was last updated',
                    },
                    'friendly_name': {
                        'type': ['null', 'string'],
                        'description': 'A user-defined friendly name for the account',
                    },
                    'owner_account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the owner account',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the account',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The current status of the account',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for accessing various subresources related to the account',
                        'additionalProperties': True,
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'The type of the account',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI for accessing the account resource',
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'accounts',
                'x-airbyte-stream-name': 'accounts',
            },
        ),
        EntityDefinition(
            name='calls',
            stream_name='calls',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Calls.json',
                    action=Action.LIST,
                    description='Returns a list of calls made to and from an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of calls',
                        'properties': {
                            'calls': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio call',
                                    'properties': {
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the call',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the call record was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the call record was last updated',
                                        },
                                        'parent_call_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the parent call if this is a child call',
                                        },
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the account associated with the call',
                                        },
                                        'to': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number that received the call',
                                        },
                                        'to_formatted': {
                                            'type': ['null', 'string'],
                                            'description': 'The formatted version of the to phone number',
                                        },
                                        'from': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number that made the call',
                                        },
                                        'from_formatted': {
                                            'type': ['null', 'string'],
                                            'description': 'The formatted version of the from phone number',
                                        },
                                        'phone_number_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the phone number used for the call',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'The current status of the call',
                                        },
                                        'start_time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the call started',
                                        },
                                        'end_time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the call ended',
                                        },
                                        'duration': {
                                            'type': ['null', 'string'],
                                            'description': 'The duration of the call in seconds',
                                        },
                                        'price': {
                                            'type': ['null', 'string'],
                                            'description': 'The cost of the call',
                                        },
                                        'price_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The currency unit of the call cost',
                                        },
                                        'direction': {
                                            'type': ['null', 'string'],
                                            'description': 'The direction of the call (inbound or outbound)',
                                        },
                                        'answered_by': {
                                            'type': ['null', 'string'],
                                            'description': 'The entity that answered the call',
                                        },
                                        'annotation': {
                                            'type': ['null', 'string'],
                                            'description': 'Any additional notes added to the call',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The version of the Twilio API used for this call',
                                        },
                                        'forwarded_from': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number that initiated call forwarding',
                                        },
                                        'group_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier of the call group',
                                        },
                                        'caller_name': {
                                            'type': ['null', 'string'],
                                            'description': 'The name of the caller as supplied by caller ID',
                                        },
                                        'queue_time': {
                                            'type': ['null', 'string'],
                                            'description': 'The time the call spent in a queue',
                                        },
                                        'trunk_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier of the trunk used for the call',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI for this call record',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for related subresources',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'calls',
                                    'x-airbyte-stream-name': 'calls',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.calls',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Calls/{sid}.json',
                    action=Action.GET,
                    description='Get a single call by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio call',
                        'properties': {
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the call',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the call record was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the call record was last updated',
                            },
                            'parent_call_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the parent call if this is a child call',
                            },
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the account associated with the call',
                            },
                            'to': {
                                'type': ['null', 'string'],
                                'description': 'The phone number that received the call',
                            },
                            'to_formatted': {
                                'type': ['null', 'string'],
                                'description': 'The formatted version of the to phone number',
                            },
                            'from': {
                                'type': ['null', 'string'],
                                'description': 'The phone number that made the call',
                            },
                            'from_formatted': {
                                'type': ['null', 'string'],
                                'description': 'The formatted version of the from phone number',
                            },
                            'phone_number_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the phone number used for the call',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'The current status of the call',
                            },
                            'start_time': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the call started',
                            },
                            'end_time': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the call ended',
                            },
                            'duration': {
                                'type': ['null', 'string'],
                                'description': 'The duration of the call in seconds',
                            },
                            'price': {
                                'type': ['null', 'string'],
                                'description': 'The cost of the call',
                            },
                            'price_unit': {
                                'type': ['null', 'string'],
                                'description': 'The currency unit of the call cost',
                            },
                            'direction': {
                                'type': ['null', 'string'],
                                'description': 'The direction of the call (inbound or outbound)',
                            },
                            'answered_by': {
                                'type': ['null', 'string'],
                                'description': 'The entity that answered the call',
                            },
                            'annotation': {
                                'type': ['null', 'string'],
                                'description': 'Any additional notes added to the call',
                            },
                            'api_version': {
                                'type': ['null', 'string'],
                                'description': 'The version of the Twilio API used for this call',
                            },
                            'forwarded_from': {
                                'type': ['null', 'string'],
                                'description': 'The phone number that initiated call forwarding',
                            },
                            'group_sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier of the call group',
                            },
                            'caller_name': {
                                'type': ['null', 'string'],
                                'description': 'The name of the caller as supplied by caller ID',
                            },
                            'queue_time': {
                                'type': ['null', 'string'],
                                'description': 'The time the call spent in a queue',
                            },
                            'trunk_sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier of the trunk used for the call',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI for this call record',
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'URIs for related subresources',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'calls',
                        'x-airbyte-stream-name': 'calls',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio call',
                'properties': {
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the call',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the call record was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the call record was last updated',
                    },
                    'parent_call_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the parent call if this is a child call',
                    },
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the account associated with the call',
                    },
                    'to': {
                        'type': ['null', 'string'],
                        'description': 'The phone number that received the call',
                    },
                    'to_formatted': {
                        'type': ['null', 'string'],
                        'description': 'The formatted version of the to phone number',
                    },
                    'from': {
                        'type': ['null', 'string'],
                        'description': 'The phone number that made the call',
                    },
                    'from_formatted': {
                        'type': ['null', 'string'],
                        'description': 'The formatted version of the from phone number',
                    },
                    'phone_number_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the phone number used for the call',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The current status of the call',
                    },
                    'start_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the call started',
                    },
                    'end_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the call ended',
                    },
                    'duration': {
                        'type': ['null', 'string'],
                        'description': 'The duration of the call in seconds',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'The cost of the call',
                    },
                    'price_unit': {
                        'type': ['null', 'string'],
                        'description': 'The currency unit of the call cost',
                    },
                    'direction': {
                        'type': ['null', 'string'],
                        'description': 'The direction of the call (inbound or outbound)',
                    },
                    'answered_by': {
                        'type': ['null', 'string'],
                        'description': 'The entity that answered the call',
                    },
                    'annotation': {
                        'type': ['null', 'string'],
                        'description': 'Any additional notes added to the call',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The version of the Twilio API used for this call',
                    },
                    'forwarded_from': {
                        'type': ['null', 'string'],
                        'description': 'The phone number that initiated call forwarding',
                    },
                    'group_sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the call group',
                    },
                    'caller_name': {
                        'type': ['null', 'string'],
                        'description': 'The name of the caller as supplied by caller ID',
                    },
                    'queue_time': {
                        'type': ['null', 'string'],
                        'description': 'The time the call spent in a queue',
                    },
                    'trunk_sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the trunk used for the call',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI for this call record',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for related subresources',
                        'additionalProperties': True,
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'calls',
                'x-airbyte-stream-name': 'calls',
            },
        ),
        EntityDefinition(
            name='messages',
            stream_name='messages',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Messages.json',
                    action=Action.LIST,
                    description='Returns a list of messages associated with an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of messages',
                        'properties': {
                            'messages': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio message',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the account associated with this message',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The version of the Twilio API used',
                                        },
                                        'body': {
                                            'type': ['null', 'string'],
                                            'description': 'The text body of the message',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the message was created',
                                        },
                                        'date_sent': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the message was sent',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'The date and time when the message was last updated',
                                        },
                                        'direction': {
                                            'type': ['null', 'string'],
                                            'description': 'The direction of the message',
                                        },
                                        'error_code': {
                                            'type': ['null', 'string'],
                                            'description': 'The error code associated with the message if any',
                                        },
                                        'error_message': {
                                            'type': ['null', 'string'],
                                            'description': 'The error message description if the message failed',
                                        },
                                        'from': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number or sender ID that sent the message',
                                        },
                                        'messaging_service_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the messaging service',
                                        },
                                        'num_media': {
                                            'type': ['null', 'string'],
                                            'description': 'The number of media files included in the message',
                                        },
                                        'num_segments': {
                                            'type': ['null', 'string'],
                                            'description': 'The number of message segments',
                                        },
                                        'price': {
                                            'type': ['null', 'string'],
                                            'description': 'The cost of the message',
                                        },
                                        'price_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The currency unit used for pricing',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for this message',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'The status of the message',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'Links to subresources related to the message',
                                            'additionalProperties': True,
                                        },
                                        'to': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number or recipient ID the message was sent to',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI for this message',
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'messages',
                                    'x-airbyte-stream-name': 'messages',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.messages',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Messages/{sid}.json',
                    action=Action.GET,
                    description='Get a single message by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio message',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the account associated with this message',
                            },
                            'api_version': {
                                'type': ['null', 'string'],
                                'description': 'The version of the Twilio API used',
                            },
                            'body': {
                                'type': ['null', 'string'],
                                'description': 'The text body of the message',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the message was created',
                            },
                            'date_sent': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the message was sent',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'The date and time when the message was last updated',
                            },
                            'direction': {
                                'type': ['null', 'string'],
                                'description': 'The direction of the message',
                            },
                            'error_code': {
                                'type': ['null', 'string'],
                                'description': 'The error code associated with the message if any',
                            },
                            'error_message': {
                                'type': ['null', 'string'],
                                'description': 'The error message description if the message failed',
                            },
                            'from': {
                                'type': ['null', 'string'],
                                'description': 'The phone number or sender ID that sent the message',
                            },
                            'messaging_service_sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the messaging service',
                            },
                            'num_media': {
                                'type': ['null', 'string'],
                                'description': 'The number of media files included in the message',
                            },
                            'num_segments': {
                                'type': ['null', 'string'],
                                'description': 'The number of message segments',
                            },
                            'price': {
                                'type': ['null', 'string'],
                                'description': 'The cost of the message',
                            },
                            'price_unit': {
                                'type': ['null', 'string'],
                                'description': 'The currency unit used for pricing',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for this message',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'The status of the message',
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'Links to subresources related to the message',
                                'additionalProperties': True,
                            },
                            'to': {
                                'type': ['null', 'string'],
                                'description': 'The phone number or recipient ID the message was sent to',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI for this message',
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'messages',
                        'x-airbyte-stream-name': 'messages',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio message',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the account associated with this message',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The version of the Twilio API used',
                    },
                    'body': {
                        'type': ['null', 'string'],
                        'description': 'The text body of the message',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the message was created',
                    },
                    'date_sent': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the message was sent',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'The date and time when the message was last updated',
                    },
                    'direction': {
                        'type': ['null', 'string'],
                        'description': 'The direction of the message',
                    },
                    'error_code': {
                        'type': ['null', 'string'],
                        'description': 'The error code associated with the message if any',
                    },
                    'error_message': {
                        'type': ['null', 'string'],
                        'description': 'The error message description if the message failed',
                    },
                    'from': {
                        'type': ['null', 'string'],
                        'description': 'The phone number or sender ID that sent the message',
                    },
                    'messaging_service_sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the messaging service',
                    },
                    'num_media': {
                        'type': ['null', 'string'],
                        'description': 'The number of media files included in the message',
                    },
                    'num_segments': {
                        'type': ['null', 'string'],
                        'description': 'The number of message segments',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'The cost of the message',
                    },
                    'price_unit': {
                        'type': ['null', 'string'],
                        'description': 'The currency unit used for pricing',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for this message',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The status of the message',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'Links to subresources related to the message',
                        'additionalProperties': True,
                    },
                    'to': {
                        'type': ['null', 'string'],
                        'description': 'The phone number or recipient ID the message was sent to',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI for this message',
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'messages',
                'x-airbyte-stream-name': 'messages',
            },
        ),
        EntityDefinition(
            name='incoming_phone_numbers',
            stream_name='incoming_phone_numbers',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/IncomingPhoneNumbers.json',
                    action=Action.LIST,
                    description='Returns a list of incoming phone numbers for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of incoming phone numbers',
                        'properties': {
                            'incoming_phone_numbers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio incoming phone number',
                                    'properties': {
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of this phone number',
                                        },
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the account that owns this phone number',
                                        },
                                        'friendly_name': {
                                            'type': ['null', 'string'],
                                            'description': 'A user-assigned friendly name for this phone number',
                                        },
                                        'phone_number': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number in E.164 format',
                                        },
                                        'voice_url': {
                                            'type': ['null', 'string'],
                                            'description': 'URL for incoming voice calls',
                                        },
                                        'voice_method': {
                                            'type': ['null', 'string'],
                                            'description': 'HTTP method for voice URL',
                                        },
                                        'voice_fallback_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Fallback URL for voice call errors',
                                        },
                                        'voice_fallback_method': {
                                            'type': ['null', 'string'],
                                            'description': 'HTTP method for voice fallback URL',
                                        },
                                        'voice_caller_id_lookup': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Caller ID lookup setting',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the phone number was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the phone number was last updated',
                                        },
                                        'sms_url': {
                                            'type': ['null', 'string'],
                                            'description': 'URL for incoming SMS messages',
                                        },
                                        'sms_method': {
                                            'type': ['null', 'string'],
                                            'description': 'HTTP method for SMS URL',
                                        },
                                        'sms_fallback_url': {
                                            'type': ['null', 'string'],
                                            'description': 'Fallback URL for SMS errors',
                                        },
                                        'sms_fallback_method': {
                                            'type': ['null', 'string'],
                                            'description': 'HTTP method for SMS fallback URL',
                                        },
                                        'address_requirements': {
                                            'type': ['null', 'string'],
                                            'description': 'Address requirements for this phone number',
                                        },
                                        'beta': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the phone number is in beta',
                                        },
                                        'capabilities': {
                                            'type': ['null', 'object'],
                                            'description': 'Capabilities of this phone number',
                                            'additionalProperties': True,
                                            'properties': {
                                                'voice': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'sms': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'mms': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'fax': {
                                                    'type': ['null', 'boolean'],
                                                },
                                            },
                                        },
                                        'voice_receive_mode': {
                                            'type': ['null', 'string'],
                                            'description': 'Receive mode setting',
                                        },
                                        'status_callback': {
                                            'type': ['null', 'string'],
                                            'description': 'Status callback URL',
                                        },
                                        'status_callback_method': {
                                            'type': ['null', 'string'],
                                            'description': 'HTTP method for status callback',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The Twilio API version',
                                        },
                                        'voice_application_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the voice application',
                                        },
                                        'sms_application_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the SMS application',
                                        },
                                        'origin': {
                                            'type': ['null', 'string'],
                                            'description': 'Origin of this phone number',
                                        },
                                        'trunk_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the associated trunk',
                                        },
                                        'emergency_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Emergency status',
                                        },
                                        'emergency_address_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the emergency address',
                                        },
                                        'emergency_address_status': {
                                            'type': ['null', 'string'],
                                            'description': 'Status of the emergency address',
                                        },
                                        'address_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the associated address',
                                        },
                                        'identity_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the identity',
                                        },
                                        'bundle_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'SID of the bundle',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of this phone number',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'Status of the phone number',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'The type of the phone number',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for related sub-resources',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'incoming_phone_numbers',
                                    'x-airbyte-stream-name': 'incoming_phone_numbers',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.incoming_phone_numbers',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/IncomingPhoneNumbers/{sid}.json',
                    action=Action.GET,
                    description='Get a single incoming phone number by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio incoming phone number',
                        'properties': {
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of this phone number',
                            },
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the account that owns this phone number',
                            },
                            'friendly_name': {
                                'type': ['null', 'string'],
                                'description': 'A user-assigned friendly name for this phone number',
                            },
                            'phone_number': {
                                'type': ['null', 'string'],
                                'description': 'The phone number in E.164 format',
                            },
                            'voice_url': {
                                'type': ['null', 'string'],
                                'description': 'URL for incoming voice calls',
                            },
                            'voice_method': {
                                'type': ['null', 'string'],
                                'description': 'HTTP method for voice URL',
                            },
                            'voice_fallback_url': {
                                'type': ['null', 'string'],
                                'description': 'Fallback URL for voice call errors',
                            },
                            'voice_fallback_method': {
                                'type': ['null', 'string'],
                                'description': 'HTTP method for voice fallback URL',
                            },
                            'voice_caller_id_lookup': {
                                'type': ['null', 'boolean'],
                                'description': 'Caller ID lookup setting',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the phone number was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the phone number was last updated',
                            },
                            'sms_url': {
                                'type': ['null', 'string'],
                                'description': 'URL for incoming SMS messages',
                            },
                            'sms_method': {
                                'type': ['null', 'string'],
                                'description': 'HTTP method for SMS URL',
                            },
                            'sms_fallback_url': {
                                'type': ['null', 'string'],
                                'description': 'Fallback URL for SMS errors',
                            },
                            'sms_fallback_method': {
                                'type': ['null', 'string'],
                                'description': 'HTTP method for SMS fallback URL',
                            },
                            'address_requirements': {
                                'type': ['null', 'string'],
                                'description': 'Address requirements for this phone number',
                            },
                            'beta': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the phone number is in beta',
                            },
                            'capabilities': {
                                'type': ['null', 'object'],
                                'description': 'Capabilities of this phone number',
                                'additionalProperties': True,
                                'properties': {
                                    'voice': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'sms': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'mms': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'fax': {
                                        'type': ['null', 'boolean'],
                                    },
                                },
                            },
                            'voice_receive_mode': {
                                'type': ['null', 'string'],
                                'description': 'Receive mode setting',
                            },
                            'status_callback': {
                                'type': ['null', 'string'],
                                'description': 'Status callback URL',
                            },
                            'status_callback_method': {
                                'type': ['null', 'string'],
                                'description': 'HTTP method for status callback',
                            },
                            'api_version': {
                                'type': ['null', 'string'],
                                'description': 'The Twilio API version',
                            },
                            'voice_application_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the voice application',
                            },
                            'sms_application_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the SMS application',
                            },
                            'origin': {
                                'type': ['null', 'string'],
                                'description': 'Origin of this phone number',
                            },
                            'trunk_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the associated trunk',
                            },
                            'emergency_status': {
                                'type': ['null', 'string'],
                                'description': 'Emergency status',
                            },
                            'emergency_address_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the emergency address',
                            },
                            'emergency_address_status': {
                                'type': ['null', 'string'],
                                'description': 'Status of the emergency address',
                            },
                            'address_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the associated address',
                            },
                            'identity_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the identity',
                            },
                            'bundle_sid': {
                                'type': ['null', 'string'],
                                'description': 'SID of the bundle',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI of this phone number',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'Status of the phone number',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'The type of the phone number',
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'URIs for related sub-resources',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'incoming_phone_numbers',
                        'x-airbyte-stream-name': 'incoming_phone_numbers',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio incoming phone number',
                'properties': {
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of this phone number',
                    },
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the account that owns this phone number',
                    },
                    'friendly_name': {
                        'type': ['null', 'string'],
                        'description': 'A user-assigned friendly name for this phone number',
                    },
                    'phone_number': {
                        'type': ['null', 'string'],
                        'description': 'The phone number in E.164 format',
                    },
                    'voice_url': {
                        'type': ['null', 'string'],
                        'description': 'URL for incoming voice calls',
                    },
                    'voice_method': {
                        'type': ['null', 'string'],
                        'description': 'HTTP method for voice URL',
                    },
                    'voice_fallback_url': {
                        'type': ['null', 'string'],
                        'description': 'Fallback URL for voice call errors',
                    },
                    'voice_fallback_method': {
                        'type': ['null', 'string'],
                        'description': 'HTTP method for voice fallback URL',
                    },
                    'voice_caller_id_lookup': {
                        'type': ['null', 'boolean'],
                        'description': 'Caller ID lookup setting',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the phone number was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the phone number was last updated',
                    },
                    'sms_url': {
                        'type': ['null', 'string'],
                        'description': 'URL for incoming SMS messages',
                    },
                    'sms_method': {
                        'type': ['null', 'string'],
                        'description': 'HTTP method for SMS URL',
                    },
                    'sms_fallback_url': {
                        'type': ['null', 'string'],
                        'description': 'Fallback URL for SMS errors',
                    },
                    'sms_fallback_method': {
                        'type': ['null', 'string'],
                        'description': 'HTTP method for SMS fallback URL',
                    },
                    'address_requirements': {
                        'type': ['null', 'string'],
                        'description': 'Address requirements for this phone number',
                    },
                    'beta': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the phone number is in beta',
                    },
                    'capabilities': {
                        'type': ['null', 'object'],
                        'description': 'Capabilities of this phone number',
                        'additionalProperties': True,
                        'properties': {
                            'voice': {
                                'type': ['null', 'boolean'],
                            },
                            'sms': {
                                'type': ['null', 'boolean'],
                            },
                            'mms': {
                                'type': ['null', 'boolean'],
                            },
                            'fax': {
                                'type': ['null', 'boolean'],
                            },
                        },
                    },
                    'voice_receive_mode': {
                        'type': ['null', 'string'],
                        'description': 'Receive mode setting',
                    },
                    'status_callback': {
                        'type': ['null', 'string'],
                        'description': 'Status callback URL',
                    },
                    'status_callback_method': {
                        'type': ['null', 'string'],
                        'description': 'HTTP method for status callback',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The Twilio API version',
                    },
                    'voice_application_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the voice application',
                    },
                    'sms_application_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the SMS application',
                    },
                    'origin': {
                        'type': ['null', 'string'],
                        'description': 'Origin of this phone number',
                    },
                    'trunk_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the associated trunk',
                    },
                    'emergency_status': {
                        'type': ['null', 'string'],
                        'description': 'Emergency status',
                    },
                    'emergency_address_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the emergency address',
                    },
                    'emergency_address_status': {
                        'type': ['null', 'string'],
                        'description': 'Status of the emergency address',
                    },
                    'address_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the associated address',
                    },
                    'identity_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the identity',
                    },
                    'bundle_sid': {
                        'type': ['null', 'string'],
                        'description': 'SID of the bundle',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of this phone number',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'Status of the phone number',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'The type of the phone number',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for related sub-resources',
                        'additionalProperties': True,
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'incoming_phone_numbers',
                'x-airbyte-stream-name': 'incoming_phone_numbers',
            },
        ),
        EntityDefinition(
            name='recordings',
            stream_name='recordings',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Recordings.json',
                    action=Action.LIST,
                    description='Returns a list of recordings for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of recordings',
                        'properties': {
                            'recordings': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio recording',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID that owns the recording',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The API version used when the recording was created',
                                        },
                                        'call_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the associated call',
                                        },
                                        'conference_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the associated conference',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the recording was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the recording was last updated',
                                        },
                                        'start_time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the recording started',
                                        },
                                        'duration': {
                                            'type': ['null', 'string'],
                                            'description': 'Duration in seconds',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier of the recording',
                                        },
                                        'price': {
                                            'type': ['null', 'string'],
                                            'description': 'The cost of storing the recording',
                                        },
                                        'price_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The currency unit',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'The status of the recording',
                                        },
                                        'channels': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of audio channels',
                                        },
                                        'source': {
                                            'type': ['null', 'string'],
                                            'description': 'The source of the recording',
                                        },
                                        'error_code': {
                                            'type': ['null', 'string'],
                                            'description': 'The error code if any',
                                        },
                                        'media_url': {
                                            'type': ['null', 'string'],
                                            'description': 'URL to the recording audio file',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of the recording resource',
                                        },
                                        'encryption_details': {
                                            'type': ['null', 'object'],
                                            'description': 'Encryption details for the recording',
                                            'additionalProperties': True,
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for subresources',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'recordings',
                                    'x-airbyte-stream-name': 'recordings',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.recordings',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Recordings/{sid}.json',
                    action=Action.GET,
                    description='Get a single recording by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio recording',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The account SID that owns the recording',
                            },
                            'api_version': {
                                'type': ['null', 'string'],
                                'description': 'The API version used when the recording was created',
                            },
                            'call_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the associated call',
                            },
                            'conference_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the associated conference',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the recording was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the recording was last updated',
                            },
                            'start_time': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the recording started',
                            },
                            'duration': {
                                'type': ['null', 'string'],
                                'description': 'Duration in seconds',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier of the recording',
                            },
                            'price': {
                                'type': ['null', 'string'],
                                'description': 'The cost of storing the recording',
                            },
                            'price_unit': {
                                'type': ['null', 'string'],
                                'description': 'The currency unit',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'The status of the recording',
                            },
                            'channels': {
                                'type': ['null', 'integer'],
                                'description': 'Number of audio channels',
                            },
                            'source': {
                                'type': ['null', 'string'],
                                'description': 'The source of the recording',
                            },
                            'error_code': {
                                'type': ['null', 'string'],
                                'description': 'The error code if any',
                            },
                            'media_url': {
                                'type': ['null', 'string'],
                                'description': 'URL to the recording audio file',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI of the recording resource',
                            },
                            'encryption_details': {
                                'type': ['null', 'object'],
                                'description': 'Encryption details for the recording',
                                'additionalProperties': True,
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'URIs for subresources',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'recordings',
                        'x-airbyte-stream-name': 'recordings',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio recording',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID that owns the recording',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The API version used when the recording was created',
                    },
                    'call_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the associated call',
                    },
                    'conference_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the associated conference',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the recording was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the recording was last updated',
                    },
                    'start_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the recording started',
                    },
                    'duration': {
                        'type': ['null', 'string'],
                        'description': 'Duration in seconds',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the recording',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'The cost of storing the recording',
                    },
                    'price_unit': {
                        'type': ['null', 'string'],
                        'description': 'The currency unit',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The status of the recording',
                    },
                    'channels': {
                        'type': ['null', 'integer'],
                        'description': 'Number of audio channels',
                    },
                    'source': {
                        'type': ['null', 'string'],
                        'description': 'The source of the recording',
                    },
                    'error_code': {
                        'type': ['null', 'string'],
                        'description': 'The error code if any',
                    },
                    'media_url': {
                        'type': ['null', 'string'],
                        'description': 'URL to the recording audio file',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of the recording resource',
                    },
                    'encryption_details': {
                        'type': ['null', 'object'],
                        'description': 'Encryption details for the recording',
                        'additionalProperties': True,
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for subresources',
                        'additionalProperties': True,
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'recordings',
                'x-airbyte-stream-name': 'recordings',
            },
        ),
        EntityDefinition(
            name='conferences',
            stream_name='conferences',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Conferences.json',
                    action=Action.LIST,
                    description='Returns a list of conferences for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of conferences',
                        'properties': {
                            'conferences': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio conference',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID associated with the conference',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the conference was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the conference was last updated',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The Twilio API version used',
                                        },
                                        'friendly_name': {
                                            'type': ['null', 'string'],
                                            'description': 'A friendly name for the conference',
                                        },
                                        'region': {
                                            'type': ['null', 'string'],
                                            'description': 'The region where the conference is hosted',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier of the conference',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'The current status of the conference',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of the conference resource',
                                        },
                                        'reason_conference_ended': {
                                            'type': ['null', 'string'],
                                            'description': 'The reason for the conference ending',
                                        },
                                        'call_sid_ending_conference': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the call that ended the conference',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for related subresources',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'conferences',
                                    'x-airbyte-stream-name': 'conferences',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.conferences',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Conferences/{sid}.json',
                    action=Action.GET,
                    description='Get a single conference by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio conference',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The account SID associated with the conference',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the conference was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the conference was last updated',
                            },
                            'api_version': {
                                'type': ['null', 'string'],
                                'description': 'The Twilio API version used',
                            },
                            'friendly_name': {
                                'type': ['null', 'string'],
                                'description': 'A friendly name for the conference',
                            },
                            'region': {
                                'type': ['null', 'string'],
                                'description': 'The region where the conference is hosted',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier of the conference',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'The current status of the conference',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI of the conference resource',
                            },
                            'reason_conference_ended': {
                                'type': ['null', 'string'],
                                'description': 'The reason for the conference ending',
                            },
                            'call_sid_ending_conference': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the call that ended the conference',
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'URIs for related subresources',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'conferences',
                        'x-airbyte-stream-name': 'conferences',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio conference',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID associated with the conference',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the conference was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the conference was last updated',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The Twilio API version used',
                    },
                    'friendly_name': {
                        'type': ['null', 'string'],
                        'description': 'A friendly name for the conference',
                    },
                    'region': {
                        'type': ['null', 'string'],
                        'description': 'The region where the conference is hosted',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the conference',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The current status of the conference',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of the conference resource',
                    },
                    'reason_conference_ended': {
                        'type': ['null', 'string'],
                        'description': 'The reason for the conference ending',
                    },
                    'call_sid_ending_conference': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the call that ended the conference',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for related subresources',
                        'additionalProperties': True,
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'conferences',
                'x-airbyte-stream-name': 'conferences',
            },
        ),
        EntityDefinition(
            name='usage_records',
            stream_name='usage_records',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Usage/Records.json',
                    action=Action.LIST,
                    description='Returns a list of usage records for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of usage records',
                        'properties': {
                            'usage_records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio usage record',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID associated with this usage record',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The Twilio API version used',
                                        },
                                        'as_of': {
                                            'type': ['null', 'string'],
                                            'description': 'The timestamp indicating data accuracy cutoff',
                                        },
                                        'category': {
                                            'type': ['null', 'string'],
                                            'description': 'The usage category (calls, SMS, recordings, etc.)',
                                        },
                                        'count': {
                                            'type': ['null', 'string'],
                                            'description': 'The number of units consumed',
                                        },
                                        'count_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The unit of measurement for count',
                                        },
                                        'description': {
                                            'type': ['null', 'string'],
                                            'description': 'A description of the usage record',
                                        },
                                        'end_date': {
                                            'type': ['null', 'string'],
                                            'description': 'The end date of the usage period',
                                        },
                                        'price': {
                                            'type': ['null', 'string'],
                                            'description': 'The total price for consumed units',
                                        },
                                        'price_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The currency unit',
                                        },
                                        'start_date': {
                                            'type': ['null', 'string'],
                                            'description': 'The start date of the usage period',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for subresources',
                                            'additionalProperties': True,
                                        },
                                        'usage': {
                                            'type': ['null', 'string'],
                                            'description': 'The total usage value',
                                        },
                                        'usage_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The unit of measurement for usage',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of the usage record',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'usage_records',
                                    'x-airbyte-stream-name': 'usage_records',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.usage_records',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio usage record',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID associated with this usage record',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The Twilio API version used',
                    },
                    'as_of': {
                        'type': ['null', 'string'],
                        'description': 'The timestamp indicating data accuracy cutoff',
                    },
                    'category': {
                        'type': ['null', 'string'],
                        'description': 'The usage category (calls, SMS, recordings, etc.)',
                    },
                    'count': {
                        'type': ['null', 'string'],
                        'description': 'The number of units consumed',
                    },
                    'count_unit': {
                        'type': ['null', 'string'],
                        'description': 'The unit of measurement for count',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'A description of the usage record',
                    },
                    'end_date': {
                        'type': ['null', 'string'],
                        'description': 'The end date of the usage period',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'The total price for consumed units',
                    },
                    'price_unit': {
                        'type': ['null', 'string'],
                        'description': 'The currency unit',
                    },
                    'start_date': {
                        'type': ['null', 'string'],
                        'description': 'The start date of the usage period',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for subresources',
                        'additionalProperties': True,
                    },
                    'usage': {
                        'type': ['null', 'string'],
                        'description': 'The total usage value',
                    },
                    'usage_unit': {
                        'type': ['null', 'string'],
                        'description': 'The unit of measurement for usage',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of the usage record',
                    },
                },
                'x-airbyte-entity-name': 'usage_records',
                'x-airbyte-stream-name': 'usage_records',
            },
        ),
        EntityDefinition(
            name='addresses',
            stream_name='addresses',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Addresses.json',
                    action=Action.LIST,
                    description='Returns a list of addresses for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of addresses',
                        'properties': {
                            'addresses': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio address',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID associated with this address',
                                        },
                                        'city': {
                                            'type': ['null', 'string'],
                                            'description': 'The city of the address',
                                        },
                                        'customer_name': {
                                            'type': ['null', 'string'],
                                            'description': 'The customer name associated with this address',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the address was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the address was last updated',
                                        },
                                        'emergency_enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether emergency services are enabled',
                                        },
                                        'friendly_name': {
                                            'type': ['null', 'string'],
                                            'description': 'A friendly name for the address',
                                        },
                                        'iso_country': {
                                            'type': ['null', 'string'],
                                            'description': 'The ISO 3166-1 alpha-2 country code',
                                        },
                                        'postal_code': {
                                            'type': ['null', 'string'],
                                            'description': 'The postal code',
                                        },
                                        'region': {
                                            'type': ['null', 'string'],
                                            'description': 'The region or state',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier of the address',
                                        },
                                        'street': {
                                            'type': ['null', 'string'],
                                            'description': 'The street address',
                                        },
                                        'street_secondary': {
                                            'type': ['null', 'string'],
                                            'description': 'Additional street information (suite number, etc.)',
                                        },
                                        'validated': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the address has been validated',
                                        },
                                        'verified': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the address has been verified',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of the address resource',
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'addresses',
                                    'x-airbyte-stream-name': 'addresses',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.addresses',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Addresses/{sid}.json',
                    action=Action.GET,
                    description='Get a single address by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio address',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The account SID associated with this address',
                            },
                            'city': {
                                'type': ['null', 'string'],
                                'description': 'The city of the address',
                            },
                            'customer_name': {
                                'type': ['null', 'string'],
                                'description': 'The customer name associated with this address',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the address was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the address was last updated',
                            },
                            'emergency_enabled': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether emergency services are enabled',
                            },
                            'friendly_name': {
                                'type': ['null', 'string'],
                                'description': 'A friendly name for the address',
                            },
                            'iso_country': {
                                'type': ['null', 'string'],
                                'description': 'The ISO 3166-1 alpha-2 country code',
                            },
                            'postal_code': {
                                'type': ['null', 'string'],
                                'description': 'The postal code',
                            },
                            'region': {
                                'type': ['null', 'string'],
                                'description': 'The region or state',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier of the address',
                            },
                            'street': {
                                'type': ['null', 'string'],
                                'description': 'The street address',
                            },
                            'street_secondary': {
                                'type': ['null', 'string'],
                                'description': 'Additional street information (suite number, etc.)',
                            },
                            'validated': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the address has been validated',
                            },
                            'verified': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the address has been verified',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI of the address resource',
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'addresses',
                        'x-airbyte-stream-name': 'addresses',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio address',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID associated with this address',
                    },
                    'city': {
                        'type': ['null', 'string'],
                        'description': 'The city of the address',
                    },
                    'customer_name': {
                        'type': ['null', 'string'],
                        'description': 'The customer name associated with this address',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the address was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the address was last updated',
                    },
                    'emergency_enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether emergency services are enabled',
                    },
                    'friendly_name': {
                        'type': ['null', 'string'],
                        'description': 'A friendly name for the address',
                    },
                    'iso_country': {
                        'type': ['null', 'string'],
                        'description': 'The ISO 3166-1 alpha-2 country code',
                    },
                    'postal_code': {
                        'type': ['null', 'string'],
                        'description': 'The postal code',
                    },
                    'region': {
                        'type': ['null', 'string'],
                        'description': 'The region or state',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier of the address',
                    },
                    'street': {
                        'type': ['null', 'string'],
                        'description': 'The street address',
                    },
                    'street_secondary': {
                        'type': ['null', 'string'],
                        'description': 'Additional street information (suite number, etc.)',
                    },
                    'validated': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the address has been validated',
                    },
                    'verified': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the address has been verified',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of the address resource',
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'addresses',
                'x-airbyte-stream-name': 'addresses',
            },
        ),
        EntityDefinition(
            name='queues',
            stream_name='queues',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Queues.json',
                    action=Action.LIST,
                    description='Returns a list of queues for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of queues',
                        'properties': {
                            'queues': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio queue',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID that owns this queue',
                                        },
                                        'average_wait_time': {
                                            'type': ['null', 'integer'],
                                            'description': 'Average wait time in seconds',
                                        },
                                        'current_size': {
                                            'type': ['null', 'integer'],
                                            'description': 'Current number of callers waiting',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the queue was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the queue was last updated',
                                        },
                                        'friendly_name': {
                                            'type': ['null', 'string'],
                                            'description': 'A friendly name for the queue',
                                        },
                                        'max_size': {
                                            'type': ['null', 'integer'],
                                            'description': 'Maximum number of callers allowed',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the queue',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI for this queue resource',
                                        },
                                        'subresource_uris': {
                                            'type': ['null', 'object'],
                                            'description': 'URIs for related subresources',
                                            'additionalProperties': True,
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'queues',
                                    'x-airbyte-stream-name': 'queues',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.queues',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Queues/{sid}.json',
                    action=Action.GET,
                    description='Get a single queue by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio queue',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The account SID that owns this queue',
                            },
                            'average_wait_time': {
                                'type': ['null', 'integer'],
                                'description': 'Average wait time in seconds',
                            },
                            'current_size': {
                                'type': ['null', 'integer'],
                                'description': 'Current number of callers waiting',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the queue was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the queue was last updated',
                            },
                            'friendly_name': {
                                'type': ['null', 'string'],
                                'description': 'A friendly name for the queue',
                            },
                            'max_size': {
                                'type': ['null', 'integer'],
                                'description': 'Maximum number of callers allowed',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the queue',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI for this queue resource',
                            },
                            'subresource_uris': {
                                'type': ['null', 'object'],
                                'description': 'URIs for related subresources',
                                'additionalProperties': True,
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'queues',
                        'x-airbyte-stream-name': 'queues',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio queue',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID that owns this queue',
                    },
                    'average_wait_time': {
                        'type': ['null', 'integer'],
                        'description': 'Average wait time in seconds',
                    },
                    'current_size': {
                        'type': ['null', 'integer'],
                        'description': 'Current number of callers waiting',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the queue was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the queue was last updated',
                    },
                    'friendly_name': {
                        'type': ['null', 'string'],
                        'description': 'A friendly name for the queue',
                    },
                    'max_size': {
                        'type': ['null', 'integer'],
                        'description': 'Maximum number of callers allowed',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the queue',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI for this queue resource',
                    },
                    'subresource_uris': {
                        'type': ['null', 'object'],
                        'description': 'URIs for related subresources',
                        'additionalProperties': True,
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'queues',
                'x-airbyte-stream-name': 'queues',
            },
        ),
        EntityDefinition(
            name='transcriptions',
            stream_name='transcriptions',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Transcriptions.json',
                    action=Action.LIST,
                    description='Returns a list of transcriptions for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of transcriptions',
                        'properties': {
                            'transcriptions': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio transcription',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID',
                                        },
                                        'api_version': {
                                            'type': ['null', 'string'],
                                            'description': 'The API version used',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the transcription was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the transcription was last updated',
                                        },
                                        'duration': {
                                            'type': ['null', 'string'],
                                            'description': 'Duration of the audio recording in seconds',
                                        },
                                        'price': {
                                            'type': ['null', 'string'],
                                            'description': 'The cost of the transcription',
                                        },
                                        'price_unit': {
                                            'type': ['null', 'string'],
                                            'description': 'The currency unit',
                                        },
                                        'recording_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The SID of the associated recording',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier for the transcription',
                                        },
                                        'status': {
                                            'type': ['null', 'string'],
                                            'description': 'The status of the transcription',
                                        },
                                        'transcription_text': {
                                            'type': ['null', 'string'],
                                            'description': 'The text content of the transcription',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'The type of transcription',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of the transcription',
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'transcriptions',
                                    'x-airbyte-stream-name': 'transcriptions',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.transcriptions',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/Transcriptions/{sid}.json',
                    action=Action.GET,
                    description='Get a single transcription by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio transcription',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The account SID',
                            },
                            'api_version': {
                                'type': ['null', 'string'],
                                'description': 'The API version used',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the transcription was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the transcription was last updated',
                            },
                            'duration': {
                                'type': ['null', 'string'],
                                'description': 'Duration of the audio recording in seconds',
                            },
                            'price': {
                                'type': ['null', 'string'],
                                'description': 'The cost of the transcription',
                            },
                            'price_unit': {
                                'type': ['null', 'string'],
                                'description': 'The currency unit',
                            },
                            'recording_sid': {
                                'type': ['null', 'string'],
                                'description': 'The SID of the associated recording',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier for the transcription',
                            },
                            'status': {
                                'type': ['null', 'string'],
                                'description': 'The status of the transcription',
                            },
                            'transcription_text': {
                                'type': ['null', 'string'],
                                'description': 'The text content of the transcription',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'The type of transcription',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI of the transcription',
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'transcriptions',
                        'x-airbyte-stream-name': 'transcriptions',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio transcription',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID',
                    },
                    'api_version': {
                        'type': ['null', 'string'],
                        'description': 'The API version used',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the transcription was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the transcription was last updated',
                    },
                    'duration': {
                        'type': ['null', 'string'],
                        'description': 'Duration of the audio recording in seconds',
                    },
                    'price': {
                        'type': ['null', 'string'],
                        'description': 'The cost of the transcription',
                    },
                    'price_unit': {
                        'type': ['null', 'string'],
                        'description': 'The currency unit',
                    },
                    'recording_sid': {
                        'type': ['null', 'string'],
                        'description': 'The SID of the associated recording',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier for the transcription',
                    },
                    'status': {
                        'type': ['null', 'string'],
                        'description': 'The status of the transcription',
                    },
                    'transcription_text': {
                        'type': ['null', 'string'],
                        'description': 'The text content of the transcription',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'The type of transcription',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of the transcription',
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'transcriptions',
                'x-airbyte-stream-name': 'transcriptions',
            },
        ),
        EntityDefinition(
            name='outgoing_caller_ids',
            stream_name='outgoing_caller_ids',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/OutgoingCallerIds.json',
                    action=Action.LIST,
                    description='Returns a list of outgoing caller IDs for an account',
                    query_params=['PageSize'],
                    query_params_schema={
                        'PageSize': {
                            'type': 'integer',
                            'required': False,
                            'default': 50,
                        },
                    },
                    path_params=['AccountSid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of outgoing caller IDs',
                        'properties': {
                            'outgoing_caller_ids': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Twilio outgoing caller ID',
                                    'properties': {
                                        'account_sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The account SID',
                                        },
                                        'date_created': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the outgoing caller ID was created',
                                        },
                                        'date_updated': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'When the outgoing caller ID was last updated',
                                        },
                                        'friendly_name': {
                                            'type': ['null', 'string'],
                                            'description': 'A friendly name',
                                        },
                                        'phone_number': {
                                            'type': ['null', 'string'],
                                            'description': 'The phone number',
                                        },
                                        'sid': {
                                            'type': ['null', 'string'],
                                            'description': 'The unique identifier',
                                        },
                                        'uri': {
                                            'type': ['null', 'string'],
                                            'description': 'The URI of the resource',
                                        },
                                    },
                                    'required': ['sid'],
                                    'x-airbyte-entity-name': 'outgoing_caller_ids',
                                    'x-airbyte-stream-name': 'outgoing_caller_ids',
                                },
                            },
                            'first_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'next_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'previous_page_uri': {
                                'type': ['null', 'string'],
                            },
                            'page': {
                                'type': ['null', 'integer'],
                            },
                            'page_size': {
                                'type': ['null', 'integer'],
                            },
                            'uri': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    record_extractor='$.outgoing_caller_ids',
                    meta_extractor={
                        'next_page_uri': '$.next_page_uri',
                        'first_page_uri': '$.first_page_uri',
                        'page': '$.page',
                        'page_size': '$.page_size',
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/Accounts/{AccountSid}/OutgoingCallerIds/{sid}.json',
                    action=Action.GET,
                    description='Get a single outgoing caller ID by SID',
                    path_params=['AccountSid', 'sid'],
                    path_params_schema={
                        'AccountSid': {'type': 'string', 'required': True},
                        'sid': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Twilio outgoing caller ID',
                        'properties': {
                            'account_sid': {
                                'type': ['null', 'string'],
                                'description': 'The account SID',
                            },
                            'date_created': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the outgoing caller ID was created',
                            },
                            'date_updated': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'When the outgoing caller ID was last updated',
                            },
                            'friendly_name': {
                                'type': ['null', 'string'],
                                'description': 'A friendly name',
                            },
                            'phone_number': {
                                'type': ['null', 'string'],
                                'description': 'The phone number',
                            },
                            'sid': {
                                'type': ['null', 'string'],
                                'description': 'The unique identifier',
                            },
                            'uri': {
                                'type': ['null', 'string'],
                                'description': 'The URI of the resource',
                            },
                        },
                        'required': ['sid'],
                        'x-airbyte-entity-name': 'outgoing_caller_ids',
                        'x-airbyte-stream-name': 'outgoing_caller_ids',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Twilio outgoing caller ID',
                'properties': {
                    'account_sid': {
                        'type': ['null', 'string'],
                        'description': 'The account SID',
                    },
                    'date_created': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the outgoing caller ID was created',
                    },
                    'date_updated': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'When the outgoing caller ID was last updated',
                    },
                    'friendly_name': {
                        'type': ['null', 'string'],
                        'description': 'A friendly name',
                    },
                    'phone_number': {
                        'type': ['null', 'string'],
                        'description': 'The phone number',
                    },
                    'sid': {
                        'type': ['null', 'string'],
                        'description': 'The unique identifier',
                    },
                    'uri': {
                        'type': ['null', 'string'],
                        'description': 'The URI of the resource',
                    },
                },
                'required': ['sid'],
                'x-airbyte-entity-name': 'outgoing_caller_ids',
                'x-airbyte-stream-name': 'outgoing_caller_ids',
            },
        ),
    ],
    search_field_paths={
        'accounts': [
            'sid',
            'friendly_name',
            'status',
            'type',
            'owner_account_sid',
            'date_created',
            'date_updated',
            'uri',
        ],
        'calls': [
            'sid',
            'account_sid',
            'to',
            'from',
            'status',
            'direction',
            'duration',
            'price',
            'price_unit',
            'start_time',
            'end_time',
            'date_created',
            'date_updated',
        ],
        'messages': [
            'sid',
            'account_sid',
            'to',
            'from',
            'body',
            'status',
            'direction',
            'price',
            'price_unit',
            'date_created',
            'date_sent',
            'error_code',
            'error_message',
            'num_segments',
            'num_media',
        ],
        'incoming_phone_numbers': [
            'sid',
            'account_sid',
            'phone_number',
            'friendly_name',
            'status',
            'capabilities',
            'date_created',
            'date_updated',
        ],
        'recordings': [
            'sid',
            'account_sid',
            'call_sid',
            'duration',
            'status',
            'channels',
            'price',
            'price_unit',
            'date_created',
            'start_time',
        ],
        'conferences': [
            'sid',
            'account_sid',
            'friendly_name',
            'status',
            'region',
            'date_created',
            'date_updated',
        ],
        'usage_records': [
            'account_sid',
            'category',
            'description',
            'usage',
            'usage_unit',
            'count',
            'count_unit',
            'price',
            'price_unit',
            'start_date',
            'end_date',
        ],
        'addresses': [
            'sid',
            'account_sid',
            'customer_name',
            'friendly_name',
            'street',
            'city',
            'region',
            'postal_code',
            'iso_country',
            'validated',
            'verified',
        ],
        'queues': [
            'sid',
            'account_sid',
            'friendly_name',
            'current_size',
            'max_size',
            'average_wait_time',
            'date_created',
            'date_updated',
        ],
        'transcriptions': [
            'sid',
            'account_sid',
            'recording_sid',
            'status',
            'duration',
            'price',
            'price_unit',
            'date_created',
            'date_updated',
        ],
        'outgoing_caller_ids': [
            'sid',
            'account_sid',
            'phone_number',
            'friendly_name',
            'date_created',
            'date_updated',
        ],
    },
)