"""
Connector model for salesforce.

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

SalesforceConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('b117307c-14b6-41aa-9422-947e34922962'),
    name='salesforce',
    version='1.0.17',
    base_url='{instance_url}/services/data/v59.0',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://login.salesforce.com/services/oauth2/token',
            'auth_style': 'body',
            'body_format': 'form',
            'token_extract': ['instance_url'],
        },
        user_config_spec=AuthConfigSpec(
            title='Salesforce OAuth 2.0',
            type='object',
            required=['refresh_token'],
            properties={
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='OAuth refresh token for automatic token renewal',
                ),
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='Connected App Consumer Key',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='Connected App Consumer Secret',
                ),
            },
            auth_mapping={
                'refresh_token': '${refresh_token}',
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
            },
            replication_auth_key_mapping={
                'client_id': 'client_id',
                'client_secret': 'client_secret',
                'refresh_token': 'refresh_token',
            },
        ),
    ),
    entities=[
        EntityDefinition(
            name='sobjects',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/sobjects',
                    action=Action.LIST,
                    description='Returns a list of all available Salesforce objects (sObjects) in the organization.\nThis endpoint is used for health checks to verify authentication and connectivity.\n',
                    response_schema={
                        'type': 'object',
                        'description': 'Response from the sobjects endpoint listing all available Salesforce objects',
                        'properties': {
                            'encoding': {
                                'type': ['null', 'string'],
                                'description': 'Character encoding used',
                            },
                            'maxBatchSize': {
                                'type': ['null', 'integer'],
                                'description': 'Maximum batch size for operations',
                            },
                            'sobjects': {
                                'type': 'array',
                                'description': 'List of available Salesforce objects',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce sObject metadata',
                                    'properties': {
                                        'name': {'type': 'string', 'description': 'API name of the sObject'},
                                        'label': {
                                            'type': ['null', 'string'],
                                            'description': 'User-friendly label for the sObject',
                                        },
                                        'labelPlural': {
                                            'type': ['null', 'string'],
                                            'description': 'Plural label for the sObject',
                                        },
                                        'keyPrefix': {
                                            'type': ['null', 'string'],
                                            'description': 'Three-character prefix for record IDs',
                                        },
                                        'custom': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is a custom object',
                                        },
                                        'queryable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the object can be queried',
                                        },
                                        'searchable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the object can be searched',
                                        },
                                        'createable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether records can be created',
                                        },
                                        'updateable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether records can be updated',
                                        },
                                        'deletable': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether records can be deleted',
                                        },
                                        'urls': {
                                            'type': ['null', 'object'],
                                            'description': 'URLs for various operations on this object',
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'sobjects',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Salesforce object metadata describing available entity types',
                                        'when_to_use': 'Questions about available Salesforce objects or schema structure',
                                        'trigger_phrases': [
                                            'salesforce object',
                                            'sobject',
                                            'schema',
                                            'object type',
                                        ],
                                        'freshness': 'static',
                                        'example_questions': ['What Salesforce objects are available?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.sobjects',
                    no_pagination='Salesforce /sobjects returns the full list of SObject metadata available to the authenticated user in a single response; no pagination parameters are supported.',
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce sObject metadata',
                'properties': {
                    'name': {'type': 'string', 'description': 'API name of the sObject'},
                    'label': {
                        'type': ['null', 'string'],
                        'description': 'User-friendly label for the sObject',
                    },
                    'labelPlural': {
                        'type': ['null', 'string'],
                        'description': 'Plural label for the sObject',
                    },
                    'keyPrefix': {
                        'type': ['null', 'string'],
                        'description': 'Three-character prefix for record IDs',
                    },
                    'custom': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a custom object',
                    },
                    'queryable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the object can be queried',
                    },
                    'searchable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the object can be searched',
                    },
                    'createable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether records can be created',
                    },
                    'updateable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether records can be updated',
                    },
                    'deletable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether records can be deleted',
                    },
                    'urls': {
                        'type': ['null', 'object'],
                        'description': 'URLs for various operations on this object',
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'sobjects',
                'x-airbyte-ai-hints': {
                    'summary': 'Salesforce object metadata describing available entity types',
                    'when_to_use': 'Questions about available Salesforce objects or schema structure',
                    'trigger_phrases': [
                        'salesforce object',
                        'sobject',
                        'schema',
                        'object type',
                    ],
                    'freshness': 'static',
                    'example_questions': ['What Salesforce objects are available?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Salesforce object metadata describing available entity types',
                'when_to_use': 'Questions about available Salesforce objects or schema structure',
                'trigger_phrases': [
                    'salesforce object',
                    'sobject',
                    'schema',
                    'object type',
                ],
                'freshness': 'static',
                'example_questions': ['What Salesforce objects are available?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='accounts',
            stream_name='Account',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:accounts',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of accounts via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Account ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for accounts',
                        'properties': {
                            'totalSize': {'type': 'integer', 'description': 'Total number of records'},
                            'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                            'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Name': {'type': 'string', 'description': 'Account name'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'accounts',
                                    'x-airbyte-stream-name': 'Account',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Salesforce accounts representing companies or organizations',
                                        'when_to_use': 'Looking up company or organization details in Salesforce',
                                        'trigger_phrases': ['salesforce account', 'company', 'organization'],
                                        'freshness': 'live',
                                        'example_questions': ['Find an account in Salesforce', 'Show account details'],
                                        'search_strategy': 'Search by name or filter by type or owner',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Account/{id}',
                    action=Action.GET,
                    description='Get a single account by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Name': {'type': 'string', 'description': 'Account name'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'accounts',
                        'x-airbyte-stream-name': 'Account',
                        'x-airbyte-ai-hints': {
                            'summary': 'Salesforce accounts representing companies or organizations',
                            'when_to_use': 'Looking up company or organization details in Salesforce',
                            'trigger_phrases': ['salesforce account', 'company', 'organization'],
                            'freshness': 'live',
                            'example_questions': ['Find an account in Salesforce', 'Show account details'],
                            'search_strategy': 'Search by name or filter by type or owner',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:accounts',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for accounts using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields and objects.\nUse SOQL (list action) for structured queries with specific field conditions.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Name': {'type': 'string', 'description': 'Account name'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'accounts',
                'x-airbyte-stream-name': 'Account',
                'x-airbyte-ai-hints': {
                    'summary': 'Salesforce accounts representing companies or organizations',
                    'when_to_use': 'Looking up company or organization details in Salesforce',
                    'trigger_phrases': ['salesforce account', 'company', 'organization'],
                    'freshness': 'live',
                    'example_questions': ['Find an account in Salesforce', 'Show account details'],
                    'search_strategy': 'Search by name or filter by type or owner',
                },
            },
            ai_hints={
                'summary': 'Salesforce accounts representing companies or organizations',
                'when_to_use': 'Looking up company or organization details in Salesforce',
                'trigger_phrases': ['salesforce account', 'company', 'organization'],
                'freshness': 'live',
                'example_questions': ['Find an account in Salesforce', 'Show account details'],
                'search_strategy': 'Search by name or filter by type or owner',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='accounts',
                    target_entity='users',
                    foreign_key='OwnerId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='accounts',
                    target_entity='accounts',
                    foreign_key='ParentId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='contacts',
            stream_name='Contact',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:contacts',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of contacts via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Contact ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for contacts',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'contacts',
                                    'x-airbyte-stream-name': 'Contact',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Salesforce contacts with email, phone, and account association',
                                        'when_to_use': 'Looking up individual contact information',
                                        'trigger_phrases': ['salesforce contact', 'who is', 'contact info'],
                                        'freshness': 'live',
                                        'example_questions': ['Find a contact in Salesforce'],
                                        'search_strategy': 'Search by name, email, or account',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Contact/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'contacts',
                        'x-airbyte-stream-name': 'Contact',
                        'x-airbyte-ai-hints': {
                            'summary': 'Salesforce contacts with email, phone, and account association',
                            'when_to_use': 'Looking up individual contact information',
                            'trigger_phrases': ['salesforce contact', 'who is', 'contact info'],
                            'freshness': 'live',
                            'example_questions': ['Find a contact in Salesforce'],
                            'search_strategy': 'Search by name, email, or account',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:contacts',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for contacts using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'contacts',
                'x-airbyte-stream-name': 'Contact',
                'x-airbyte-ai-hints': {
                    'summary': 'Salesforce contacts with email, phone, and account association',
                    'when_to_use': 'Looking up individual contact information',
                    'trigger_phrases': ['salesforce contact', 'who is', 'contact info'],
                    'freshness': 'live',
                    'example_questions': ['Find a contact in Salesforce'],
                    'search_strategy': 'Search by name, email, or account',
                },
            },
            ai_hints={
                'summary': 'Salesforce contacts with email, phone, and account association',
                'when_to_use': 'Looking up individual contact information',
                'trigger_phrases': ['salesforce contact', 'who is', 'contact info'],
                'freshness': 'live',
                'example_questions': ['Find a contact in Salesforce'],
                'search_strategy': 'Search by name, email, or account',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='contacts',
                    target_entity='accounts',
                    foreign_key='AccountId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='contacts',
                    target_entity='users',
                    foreign_key='OwnerId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='contacts',
                    target_entity='contacts',
                    foreign_key='ReportsToId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='leads',
            stream_name='Lead',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:leads',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of leads via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Lead ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for leads',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'leads',
                                    'x-airbyte-stream-name': 'Lead',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sales leads with source, status, and conversion details',
                                        'when_to_use': 'Questions about leads, lead status, or lead conversion',
                                        'trigger_phrases': [
                                            'salesforce lead',
                                            'new lead',
                                            'lead status',
                                            'lead source',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show new leads', 'What leads came in this week?'],
                                        'search_strategy': 'Search by name, email, or filter by status and source',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Lead/{id}',
                    action=Action.GET,
                    description='Get a single lead by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'leads',
                        'x-airbyte-stream-name': 'Lead',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sales leads with source, status, and conversion details',
                            'when_to_use': 'Questions about leads, lead status, or lead conversion',
                            'trigger_phrases': [
                                'salesforce lead',
                                'new lead',
                                'lead status',
                                'lead source',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Show new leads', 'What leads came in this week?'],
                            'search_strategy': 'Search by name, email, or filter by status and source',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:leads',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for leads using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'leads',
                'x-airbyte-stream-name': 'Lead',
                'x-airbyte-ai-hints': {
                    'summary': 'Sales leads with source, status, and conversion details',
                    'when_to_use': 'Questions about leads, lead status, or lead conversion',
                    'trigger_phrases': [
                        'salesforce lead',
                        'new lead',
                        'lead status',
                        'lead source',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show new leads', 'What leads came in this week?'],
                    'search_strategy': 'Search by name, email, or filter by status and source',
                },
            },
            ai_hints={
                'summary': 'Sales leads with source, status, and conversion details',
                'when_to_use': 'Questions about leads, lead status, or lead conversion',
                'trigger_phrases': [
                    'salesforce lead',
                    'new lead',
                    'lead status',
                    'lead source',
                ],
                'freshness': 'live',
                'example_questions': ['Show new leads', 'What leads came in this week?'],
                'search_strategy': 'Search by name, email, or filter by status and source',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='leads',
                    target_entity='users',
                    foreign_key='OwnerId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='leads',
                    target_entity='accounts',
                    foreign_key='ConvertedAccountId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='leads',
                    target_entity='contacts',
                    foreign_key='ConvertedContactId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='leads',
                    target_entity='opportunities',
                    foreign_key='ConvertedOpportunityId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='opportunities',
            stream_name='Opportunity',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:opportunities',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of opportunities via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Opportunity ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for opportunities',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'opportunities',
                                    'x-airbyte-stream-name': 'Opportunity',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sales opportunities with stage, amount, and close date',
                                        'when_to_use': 'Questions about pipeline, deal stage, revenue, or forecasts',
                                        'trigger_phrases': [
                                            'opportunity',
                                            'deal',
                                            'pipeline',
                                            'forecast',
                                            'close date',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Show deals closing this month', 'What is the pipeline value?'],
                                        'search_strategy': 'Search by name or filter by stage, owner, or close date',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Opportunity/{id}',
                    action=Action.GET,
                    description='Get a single opportunity by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'opportunities',
                        'x-airbyte-stream-name': 'Opportunity',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sales opportunities with stage, amount, and close date',
                            'when_to_use': 'Questions about pipeline, deal stage, revenue, or forecasts',
                            'trigger_phrases': [
                                'opportunity',
                                'deal',
                                'pipeline',
                                'forecast',
                                'close date',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Show deals closing this month', 'What is the pipeline value?'],
                            'search_strategy': 'Search by name or filter by stage, owner, or close date',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:opportunities',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for opportunities using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'opportunities',
                'x-airbyte-stream-name': 'Opportunity',
                'x-airbyte-ai-hints': {
                    'summary': 'Sales opportunities with stage, amount, and close date',
                    'when_to_use': 'Questions about pipeline, deal stage, revenue, or forecasts',
                    'trigger_phrases': [
                        'opportunity',
                        'deal',
                        'pipeline',
                        'forecast',
                        'close date',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Show deals closing this month', 'What is the pipeline value?'],
                    'search_strategy': 'Search by name or filter by stage, owner, or close date',
                },
            },
            ai_hints={
                'summary': 'Sales opportunities with stage, amount, and close date',
                'when_to_use': 'Questions about pipeline, deal stage, revenue, or forecasts',
                'trigger_phrases': [
                    'opportunity',
                    'deal',
                    'pipeline',
                    'forecast',
                    'close date',
                ],
                'freshness': 'live',
                'example_questions': ['Show deals closing this month', 'What is the pipeline value?'],
                'search_strategy': 'Search by name or filter by stage, owner, or close date',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='opportunities',
                    target_entity='accounts',
                    foreign_key='AccountId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='opportunities',
                    target_entity='users',
                    foreign_key='OwnerId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='opportunities',
                    target_entity='contacts',
                    foreign_key='ContactId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='opportunities',
                    target_entity='campaigns',
                    foreign_key='CampaignId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='tasks',
            stream_name='Task',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:tasks',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of tasks via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Task ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for tasks',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Subject': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'tasks',
                                    'x-airbyte-stream-name': 'Task',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Salesforce tasks (to-dos and activities) assigned to users',
                                        'when_to_use': 'Questions about assigned tasks or activity tracking',
                                        'trigger_phrases': [
                                            'salesforce task',
                                            'to-do',
                                            'activity',
                                            'assigned task',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What tasks are assigned to me in Salesforce?'],
                                        'search_strategy': 'Filter by assignee, status, or due date',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Task/{id}',
                    action=Action.GET,
                    description='Get a single task by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Subject': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'tasks',
                        'x-airbyte-stream-name': 'Task',
                        'x-airbyte-ai-hints': {
                            'summary': 'Salesforce tasks (to-dos and activities) assigned to users',
                            'when_to_use': 'Questions about assigned tasks or activity tracking',
                            'trigger_phrases': [
                                'salesforce task',
                                'to-do',
                                'activity',
                                'assigned task',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What tasks are assigned to me in Salesforce?'],
                            'search_strategy': 'Filter by assignee, status, or due date',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:tasks',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for tasks using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Subject': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'tasks',
                'x-airbyte-stream-name': 'Task',
                'x-airbyte-ai-hints': {
                    'summary': 'Salesforce tasks (to-dos and activities) assigned to users',
                    'when_to_use': 'Questions about assigned tasks or activity tracking',
                    'trigger_phrases': [
                        'salesforce task',
                        'to-do',
                        'activity',
                        'assigned task',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What tasks are assigned to me in Salesforce?'],
                    'search_strategy': 'Filter by assignee, status, or due date',
                },
            },
            ai_hints={
                'summary': 'Salesforce tasks (to-dos and activities) assigned to users',
                'when_to_use': 'Questions about assigned tasks or activity tracking',
                'trigger_phrases': [
                    'salesforce task',
                    'to-do',
                    'activity',
                    'assigned task',
                ],
                'freshness': 'live',
                'example_questions': ['What tasks are assigned to me in Salesforce?'],
                'search_strategy': 'Filter by assignee, status, or due date',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='accounts',
                    foreign_key='AccountId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
                EntityRelationshipConfig(
                    source_entity='tasks',
                    target_entity='users',
                    foreign_key='OwnerId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='events',
            stream_name='Event',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:events',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of events via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Event ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for events',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Subject': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'events',
                                    'x-airbyte-stream-name': 'Event',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Calendar events and meetings in Salesforce',
                                        'when_to_use': 'Questions about scheduled meetings or calendar events',
                                        'trigger_phrases': ['salesforce event', 'meeting', 'calendar event'],
                                        'freshness': 'live',
                                        'example_questions': ['What meetings are scheduled this week?'],
                                        'search_strategy': 'Filter by date, owner, or related record',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Event/{id}',
                    action=Action.GET,
                    description='Get a single event by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Subject': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'events',
                        'x-airbyte-stream-name': 'Event',
                        'x-airbyte-ai-hints': {
                            'summary': 'Calendar events and meetings in Salesforce',
                            'when_to_use': 'Questions about scheduled meetings or calendar events',
                            'trigger_phrases': ['salesforce event', 'meeting', 'calendar event'],
                            'freshness': 'live',
                            'example_questions': ['What meetings are scheduled this week?'],
                            'search_strategy': 'Filter by date, owner, or related record',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:events',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for events using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Subject': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'events',
                'x-airbyte-stream-name': 'Event',
                'x-airbyte-ai-hints': {
                    'summary': 'Calendar events and meetings in Salesforce',
                    'when_to_use': 'Questions about scheduled meetings or calendar events',
                    'trigger_phrases': ['salesforce event', 'meeting', 'calendar event'],
                    'freshness': 'live',
                    'example_questions': ['What meetings are scheduled this week?'],
                    'search_strategy': 'Filter by date, owner, or related record',
                },
            },
            ai_hints={
                'summary': 'Calendar events and meetings in Salesforce',
                'when_to_use': 'Questions about scheduled meetings or calendar events',
                'trigger_phrases': ['salesforce event', 'meeting', 'calendar event'],
                'freshness': 'live',
                'example_questions': ['What meetings are scheduled this week?'],
                'search_strategy': 'Filter by date, owner, or related record',
            },
        ),
        EntityDefinition(
            name='campaigns',
            stream_name='Campaign',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:campaigns',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of campaigns via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Campaign ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for campaigns',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Name': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'Campaign',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Marketing campaigns with members, status, and response tracking',
                                        'when_to_use': 'Questions about marketing campaigns or campaign membership',
                                        'trigger_phrases': ['salesforce campaign', 'marketing campaign'],
                                        'freshness': 'live',
                                        'example_questions': ['Show active Salesforce campaigns'],
                                        'search_strategy': 'Search by name or filter by status',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Campaign/{id}',
                    action=Action.GET,
                    description='Get a single campaign by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Name': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'campaigns',
                        'x-airbyte-stream-name': 'Campaign',
                        'x-airbyte-ai-hints': {
                            'summary': 'Marketing campaigns with members, status, and response tracking',
                            'when_to_use': 'Questions about marketing campaigns or campaign membership',
                            'trigger_phrases': ['salesforce campaign', 'marketing campaign'],
                            'freshness': 'live',
                            'example_questions': ['Show active Salesforce campaigns'],
                            'search_strategy': 'Search by name or filter by status',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:campaigns',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for campaigns using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Name': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'Campaign',
                'x-airbyte-ai-hints': {
                    'summary': 'Marketing campaigns with members, status, and response tracking',
                    'when_to_use': 'Questions about marketing campaigns or campaign membership',
                    'trigger_phrases': ['salesforce campaign', 'marketing campaign'],
                    'freshness': 'live',
                    'example_questions': ['Show active Salesforce campaigns'],
                    'search_strategy': 'Search by name or filter by status',
                },
            },
            ai_hints={
                'summary': 'Marketing campaigns with members, status, and response tracking',
                'when_to_use': 'Questions about marketing campaigns or campaign membership',
                'trigger_phrases': ['salesforce campaign', 'marketing campaign'],
                'freshness': 'live',
                'example_questions': ['Show active Salesforce campaigns'],
                'search_strategy': 'Search by name or filter by status',
            },
        ),
        EntityDefinition(
            name='cases',
            stream_name='Case',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:cases',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of cases via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Case ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for cases',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'CaseNumber': {'type': 'string'},
                                        'Subject': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'cases',
                                    'x-airbyte-stream-name': 'Case',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Support cases tracking customer issues and resolutions',
                                        'when_to_use': 'Questions about support cases, customer issues, or case resolution',
                                        'trigger_phrases': ['salesforce case', 'support case', 'customer issue'],
                                        'freshness': 'live',
                                        'example_questions': ['Show open support cases', 'Find cases for an account'],
                                        'search_strategy': 'Search by subject or filter by status, priority, or owner',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Case/{id}',
                    action=Action.GET,
                    description='Get a single case by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'CaseNumber': {'type': 'string'},
                            'Subject': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'cases',
                        'x-airbyte-stream-name': 'Case',
                        'x-airbyte-ai-hints': {
                            'summary': 'Support cases tracking customer issues and resolutions',
                            'when_to_use': 'Questions about support cases, customer issues, or case resolution',
                            'trigger_phrases': ['salesforce case', 'support case', 'customer issue'],
                            'freshness': 'live',
                            'example_questions': ['Show open support cases', 'Find cases for an account'],
                            'search_strategy': 'Search by subject or filter by status, priority, or owner',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:cases',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for cases using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'CaseNumber': {'type': 'string'},
                    'Subject': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'cases',
                'x-airbyte-stream-name': 'Case',
                'x-airbyte-ai-hints': {
                    'summary': 'Support cases tracking customer issues and resolutions',
                    'when_to_use': 'Questions about support cases, customer issues, or case resolution',
                    'trigger_phrases': ['salesforce case', 'support case', 'customer issue'],
                    'freshness': 'live',
                    'example_questions': ['Show open support cases', 'Find cases for an account'],
                    'search_strategy': 'Search by subject or filter by status, priority, or owner',
                },
            },
            ai_hints={
                'summary': 'Support cases tracking customer issues and resolutions',
                'when_to_use': 'Questions about support cases, customer issues, or case resolution',
                'trigger_phrases': ['salesforce case', 'support case', 'customer issue'],
                'freshness': 'live',
                'example_questions': ['Show open support cases', 'Find cases for an account'],
                'search_strategy': 'Search by subject or filter by status, priority, or owner',
            },
        ),
        EntityDefinition(
            name='notes',
            stream_name='Note',
            actions=[Action.LIST, Action.GET, Action.API_SEARCH],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:notes',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of notes via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM Note ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for notes',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'Title': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'notes',
                                    'x-airbyte-stream-name': 'Note',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Notes attached to Salesforce records',
                                        'when_to_use': 'Looking for notes or context on Salesforce records',
                                        'trigger_phrases': ['salesforce note', 'record note'],
                                        'freshness': 'live',
                                        'example_questions': ['What notes are on this record?'],
                                        'search_strategy': 'Filter by parent record',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Note/{id}',
                    action=Action.GET,
                    description='Get a single note by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string'},
                            'Title': {'type': 'string'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'notes',
                        'x-airbyte-stream-name': 'Note',
                        'x-airbyte-ai-hints': {
                            'summary': 'Notes attached to Salesforce records',
                            'when_to_use': 'Looking for notes or context on Salesforce records',
                            'trigger_phrases': ['salesforce note', 'record note'],
                            'freshness': 'live',
                            'example_questions': ['What notes are on this record?'],
                            'search_strategy': 'Filter by parent record',
                        },
                    },
                ),
                Action.API_SEARCH: EndpointDefinition(
                    method='GET',
                    path='/search:notes',
                    path_override=PathOverrideConfig(
                        path='/search',
                    ),
                    action=Action.API_SEARCH,
                    description='Search for notes using SOSL (Salesforce Object Search Language).\nSOSL is optimized for text-based searches across multiple fields.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOSL search result',
                        'properties': {
                            'searchRecords': {
                                'type': 'array',
                                'description': 'Array of search result records',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'Id': {'type': 'string'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string'},
                    'Title': {'type': 'string'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'notes',
                'x-airbyte-stream-name': 'Note',
                'x-airbyte-ai-hints': {
                    'summary': 'Notes attached to Salesforce records',
                    'when_to_use': 'Looking for notes or context on Salesforce records',
                    'trigger_phrases': ['salesforce note', 'record note'],
                    'freshness': 'live',
                    'example_questions': ['What notes are on this record?'],
                    'search_strategy': 'Filter by parent record',
                },
            },
            ai_hints={
                'summary': 'Notes attached to Salesforce records',
                'when_to_use': 'Looking for notes or context on Salesforce records',
                'trigger_phrases': ['salesforce note', 'record note'],
                'freshness': 'live',
                'example_questions': ['What notes are on this record?'],
                'search_strategy': 'Filter by parent record',
            },
        ),
        EntityDefinition(
            name='content_versions',
            stream_name='ContentVersion',
            actions=[Action.LIST, Action.GET, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:content_versions',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of content versions (file metadata) via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\nNote: ContentVersion does not support FIELDS(STANDARD), so specific fields must be listed.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT Id, Title, FileExtension, ContentSize, ContentDocumentId, VersionNumber, IsLatest, CreatedDate, LastModifiedDate FROM ContentVersion ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for content versions',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce ContentVersion object - represents a file version in Salesforce Files',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Title': {'type': 'string', 'description': 'File title/name'},
                                        'FileExtension': {'type': 'string', 'description': 'File extension (e.g., pdf, docx)'},
                                        'ContentSize': {'type': 'integer', 'description': 'File size in bytes'},
                                        'ContentDocumentId': {'type': 'string', 'description': 'ID of the parent ContentDocument'},
                                        'VersionNumber': {'type': 'string', 'description': 'Version number of the file'},
                                        'IsLatest': {'type': 'boolean', 'description': 'Whether this is the latest version'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'content_versions',
                                    'x-airbyte-stream-name': 'ContentVersion',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'File versions stored in Salesforce Content',
                                        'when_to_use': 'Looking for files or documents in Salesforce',
                                        'trigger_phrases': ['salesforce file', 'content version', 'document'],
                                        'freshness': 'live',
                                        'example_questions': ['Find files in Salesforce'],
                                        'search_strategy': 'Search by title',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/ContentVersion/{id}',
                    action=Action.GET,
                    description="Get a single content version's metadata by ID. Returns file metadata, not the file content.\nUse the download action to retrieve the actual file binary.\n",
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce ContentVersion object - represents a file version in Salesforce Files',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Title': {'type': 'string', 'description': 'File title/name'},
                            'FileExtension': {'type': 'string', 'description': 'File extension (e.g., pdf, docx)'},
                            'ContentSize': {'type': 'integer', 'description': 'File size in bytes'},
                            'ContentDocumentId': {'type': 'string', 'description': 'ID of the parent ContentDocument'},
                            'VersionNumber': {'type': 'string', 'description': 'Version number of the file'},
                            'IsLatest': {'type': 'boolean', 'description': 'Whether this is the latest version'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'content_versions',
                        'x-airbyte-stream-name': 'ContentVersion',
                        'x-airbyte-ai-hints': {
                            'summary': 'File versions stored in Salesforce Content',
                            'when_to_use': 'Looking for files or documents in Salesforce',
                            'trigger_phrases': ['salesforce file', 'content version', 'document'],
                            'freshness': 'live',
                            'example_questions': ['Find files in Salesforce'],
                            'search_strategy': 'Search by title',
                        },
                    },
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/sobjects/ContentVersion/{id}/VersionData',
                    action=Action.DOWNLOAD,
                    description='Downloads the binary file content of a content version.\nFirst use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),\nthen use this action to download the actual file content.\nThe response is the raw binary file data.\n',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce ContentVersion object - represents a file version in Salesforce Files',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Title': {'type': 'string', 'description': 'File title/name'},
                    'FileExtension': {'type': 'string', 'description': 'File extension (e.g., pdf, docx)'},
                    'ContentSize': {'type': 'integer', 'description': 'File size in bytes'},
                    'ContentDocumentId': {'type': 'string', 'description': 'ID of the parent ContentDocument'},
                    'VersionNumber': {'type': 'string', 'description': 'Version number of the file'},
                    'IsLatest': {'type': 'boolean', 'description': 'Whether this is the latest version'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'content_versions',
                'x-airbyte-stream-name': 'ContentVersion',
                'x-airbyte-ai-hints': {
                    'summary': 'File versions stored in Salesforce Content',
                    'when_to_use': 'Looking for files or documents in Salesforce',
                    'trigger_phrases': ['salesforce file', 'content version', 'document'],
                    'freshness': 'live',
                    'example_questions': ['Find files in Salesforce'],
                    'search_strategy': 'Search by title',
                },
            },
            ai_hints={
                'summary': 'File versions stored in Salesforce Content',
                'when_to_use': 'Looking for files or documents in Salesforce',
                'trigger_phrases': ['salesforce file', 'content version', 'document'],
                'freshness': 'live',
                'example_questions': ['Find files in Salesforce'],
                'search_strategy': 'Search by title',
            },
        ),
        EntityDefinition(
            name='attachments',
            stream_name='Attachment',
            actions=[Action.LIST, Action.GET, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:attachments',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of attachments (legacy) via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\nNote: Attachments are a legacy feature; consider using ContentVersion (Salesforce Files) for new implementations.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT Id, Name, ContentType, BodyLength, ParentId, CreatedDate, LastModifiedDate FROM Attachment ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for attachments',
                        'properties': {
                            'totalSize': {'type': 'integer'},
                            'done': {'type': 'boolean'},
                            'nextRecordsUrl': {'type': 'string'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce Attachment object - legacy file attachment on a record',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Name': {'type': 'string', 'description': 'File name'},
                                        'ContentType': {'type': 'string', 'description': 'MIME type of the file'},
                                        'BodyLength': {'type': 'integer', 'description': 'File size in bytes'},
                                        'ParentId': {'type': 'string', 'description': 'ID of the parent record this attachment is attached to'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'attachments',
                                    'x-airbyte-stream-name': 'Attachment',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'File attachments on Salesforce records',
                                        'when_to_use': 'Looking for files attached to specific records',
                                        'trigger_phrases': ['salesforce attachment', 'attached file'],
                                        'freshness': 'live',
                                        'example_questions': ['What attachments are on this record?'],
                                        'search_strategy': 'Filter by parent record',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Attachment/{id}',
                    action=Action.GET,
                    description="Get a single attachment's metadata by ID. Returns file metadata, not the file content.\nUse the download action to retrieve the actual file binary.\nNote: Attachments are a legacy feature; consider using ContentVersion for new implementations.\n",
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce Attachment object - legacy file attachment on a record',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Name': {'type': 'string', 'description': 'File name'},
                            'ContentType': {'type': 'string', 'description': 'MIME type of the file'},
                            'BodyLength': {'type': 'integer', 'description': 'File size in bytes'},
                            'ParentId': {'type': 'string', 'description': 'ID of the parent record this attachment is attached to'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'attachments',
                        'x-airbyte-stream-name': 'Attachment',
                        'x-airbyte-ai-hints': {
                            'summary': 'File attachments on Salesforce records',
                            'when_to_use': 'Looking for files attached to specific records',
                            'trigger_phrases': ['salesforce attachment', 'attached file'],
                            'freshness': 'live',
                            'example_questions': ['What attachments are on this record?'],
                            'search_strategy': 'Filter by parent record',
                        },
                    },
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/sobjects/Attachment/{id}/Body',
                    action=Action.DOWNLOAD,
                    description='Downloads the binary file content of an attachment (legacy).\nFirst use the list or get action to retrieve the Attachment ID and file metadata,\nthen use this action to download the actual file content.\nNote: Attachments are a legacy feature; consider using ContentVersion for new implementations.\n',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Attachment object - legacy file attachment on a record',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Name': {'type': 'string', 'description': 'File name'},
                    'ContentType': {'type': 'string', 'description': 'MIME type of the file'},
                    'BodyLength': {'type': 'integer', 'description': 'File size in bytes'},
                    'ParentId': {'type': 'string', 'description': 'ID of the parent record this attachment is attached to'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'attachments',
                'x-airbyte-stream-name': 'Attachment',
                'x-airbyte-ai-hints': {
                    'summary': 'File attachments on Salesforce records',
                    'when_to_use': 'Looking for files attached to specific records',
                    'trigger_phrases': ['salesforce attachment', 'attached file'],
                    'freshness': 'live',
                    'example_questions': ['What attachments are on this record?'],
                    'search_strategy': 'Filter by parent record',
                },
            },
            ai_hints={
                'summary': 'File attachments on Salesforce records',
                'when_to_use': 'Looking for files attached to specific records',
                'trigger_phrases': ['salesforce attachment', 'attached file'],
                'freshness': 'live',
                'example_questions': ['What attachments are on this record?'],
                'search_strategy': 'Filter by parent record',
            },
        ),
        EntityDefinition(
            name='reports',
            stream_name='Report',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/analytics/reports',
                    action=Action.LIST,
                    description='Returns a list of reports available in the Salesforce org.\nEach report includes metadata such as Id, Name, Format, Description, and URL.\nThis uses the Analytics REST API, not SOQL.\n',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Salesforce Report metadata from the Analytics API',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Unique identifier for the report'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the report',
                                },
                                'url': {
                                    'type': ['null', 'string'],
                                    'description': 'API URL to access the report',
                                },
                                'describeUrl': {
                                    'type': ['null', 'string'],
                                    'description': 'API URL to get the report describe/metadata',
                                },
                                'instancesUrl': {
                                    'type': ['null', 'string'],
                                    'description': 'API URL for async report run instances',
                                },
                            },
                            'additionalProperties': True,
                            'x-airbyte-entity-name': 'reports',
                            'x-airbyte-stream-name': 'Report',
                            'x-airbyte-ai-hints': {
                                'summary': 'Salesforce reports with metadata and folder organization',
                                'when_to_use': 'Questions about available reports or report details',
                                'trigger_phrases': ['salesforce report', 'report list'],
                                'freshness': 'live',
                                'example_questions': ['What reports are available in Salesforce?'],
                                'search_strategy': 'Search by name or filter by folder',
                            },
                        },
                    },
                    no_pagination='Salesforce Analytics /analytics/reports returns the full list of report metadata in a single response; the Analytics Reports listing endpoint does not expose pagination parameters.',
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/analytics/reports/{id}',
                    action=Action.GET,
                    description='Executes a report synchronously and returns the report data results.\nReturns both metadata and the executed data including fact maps, aggregates, and detail rows.\nFirst use the list action to find available reports, then use this action to run a report and get its data.\nNote: Large reports may be truncated. For reports with more than 2,000 detail rows, consider using async report runs.\n',
                    query_params=['includeDetails'],
                    query_params_schema={
                        'includeDetails': {
                            'type': 'boolean',
                            'required': False,
                            'default': True,
                        },
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Executed report results including data rows, aggregates, and metadata',
                        'properties': {
                            'attributes': {
                                'type': ['null', 'object'],
                                'description': 'Report attributes including description, format, and report type',
                                'additionalProperties': True,
                            },
                            'reportMetadata': {
                                'type': ['null', 'object'],
                                'description': 'Report metadata including columns, groupings, and filters',
                                'additionalProperties': True,
                            },
                            'reportExtendedMetadata': {
                                'type': ['null', 'object'],
                                'description': 'Extended metadata including column details and data types',
                                'additionalProperties': True,
                            },
                            'factMap': {
                                'type': ['null', 'object'],
                                'description': 'Contains the report data organized by grouping keys with rows and aggregates',
                                'additionalProperties': True,
                            },
                            'groupingsDown': {
                                'type': ['null', 'object'],
                                'description': 'Row-level grouping information',
                                'additionalProperties': True,
                            },
                            'groupingsAcross': {
                                'type': ['null', 'object'],
                                'description': 'Column-level grouping information',
                                'additionalProperties': True,
                            },
                            'hasDetailRows': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the report results include detail rows',
                            },
                            'allData': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether all data is included (false if report was truncated)',
                            },
                        },
                        'additionalProperties': True,
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce Report metadata from the Analytics API',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique identifier for the report'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the report',
                    },
                    'url': {
                        'type': ['null', 'string'],
                        'description': 'API URL to access the report',
                    },
                    'describeUrl': {
                        'type': ['null', 'string'],
                        'description': 'API URL to get the report describe/metadata',
                    },
                    'instancesUrl': {
                        'type': ['null', 'string'],
                        'description': 'API URL for async report run instances',
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'reports',
                'x-airbyte-stream-name': 'Report',
                'x-airbyte-ai-hints': {
                    'summary': 'Salesforce reports with metadata and folder organization',
                    'when_to_use': 'Questions about available reports or report details',
                    'trigger_phrases': ['salesforce report', 'report list'],
                    'freshness': 'live',
                    'example_questions': ['What reports are available in Salesforce?'],
                    'search_strategy': 'Search by name or filter by folder',
                },
            },
            ai_hints={
                'summary': 'Salesforce reports with metadata and folder organization',
                'when_to_use': 'Questions about available reports or report details',
                'trigger_phrases': ['salesforce report', 'report list'],
                'freshness': 'live',
                'example_questions': ['What reports are available in Salesforce?'],
                'search_strategy': 'Search by name or filter by folder',
            },
        ),
        EntityDefinition(
            name='users',
            stream_name='User',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:users',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of users via SOQL query. Default returns up to 200 records.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM User WHERE IsActive = true ORDER BY LastModifiedDate DESC LIMIT 200',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for users',
                        'properties': {
                            'totalSize': {'type': 'integer', 'description': 'Total number of records'},
                            'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                            'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce User object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'Name': {'type': 'string', 'description': 'Full name of the user'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'User',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Salesforce users with profile, role, and activity information',
                                        'when_to_use': 'Looking up user details, owners, or assignees in Salesforce',
                                        'trigger_phrases': [
                                            'salesforce user',
                                            'owner',
                                            'assignee',
                                            'who owns',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the active users in Salesforce?', 'Show me details for the owner of this record'],
                                        'search_strategy': 'Search by name, email, or filter by active status',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/User/{id}',
                    action=Action.GET,
                    description='Get a single user by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce User object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'Name': {'type': 'string', 'description': 'Full name of the user'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'users',
                        'x-airbyte-stream-name': 'User',
                        'x-airbyte-ai-hints': {
                            'summary': 'Salesforce users with profile, role, and activity information',
                            'when_to_use': 'Looking up user details, owners, or assignees in Salesforce',
                            'trigger_phrases': [
                                'salesforce user',
                                'owner',
                                'assignee',
                                'who owns',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Who are the active users in Salesforce?', 'Show me details for the owner of this record'],
                            'search_strategy': 'Search by name, email, or filter by active status',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce User object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'Name': {'type': 'string', 'description': 'Full name of the user'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'User',
                'x-airbyte-ai-hints': {
                    'summary': 'Salesforce users with profile, role, and activity information',
                    'when_to_use': 'Looking up user details, owners, or assignees in Salesforce',
                    'trigger_phrases': [
                        'salesforce user',
                        'owner',
                        'assignee',
                        'who owns',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Who are the active users in Salesforce?', 'Show me details for the owner of this record'],
                    'search_strategy': 'Search by name, email, or filter by active status',
                },
            },
            ai_hints={
                'summary': 'Salesforce users with profile, role, and activity information',
                'when_to_use': 'Looking up user details, owners, or assignees in Salesforce',
                'trigger_phrases': [
                    'salesforce user',
                    'owner',
                    'assignee',
                    'who owns',
                ],
                'freshness': 'live',
                'example_questions': ['Who are the active users in Salesforce?', 'Show me details for the owner of this record'],
                'search_strategy': 'Search by name, email, or filter by active status',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='users',
                    target_entity='users',
                    foreign_key='ManagerId',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='opportunity_stages',
            stream_name='OpportunityStage',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query:opportunity_stages',
                    path_override=PathOverrideConfig(
                        path='/query',
                    ),
                    action=Action.LIST,
                    description='Returns a list of opportunity stages via SOQL query. Default returns all stages.\nOpportunityStage defines the sales process stages that opportunities move through.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT FIELDS(STANDARD) FROM OpportunityStage ORDER BY SortOrder ASC',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'SOQL query result for opportunity stages',
                        'properties': {
                            'totalSize': {'type': 'integer', 'description': 'Total number of records'},
                            'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                            'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results'},
                            'records': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Salesforce OpportunityStage object - uses FIELDS(STANDARD) so all standard fields are returned',
                                    'properties': {
                                        'Id': {'type': 'string', 'description': 'Unique identifier'},
                                        'MasterLabel': {'type': 'string', 'description': 'Display label for the stage'},
                                        'attributes': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {'type': 'string'},
                                                'url': {'type': 'string'},
                                            },
                                        },
                                    },
                                    'additionalProperties': True,
                                    'x-airbyte-entity-name': 'opportunity_stages',
                                    'x-airbyte-stream-name': 'OpportunityStage',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Sales process stages that opportunities move through',
                                        'when_to_use': 'Looking up opportunity stage definitions, probabilities, or sales process configuration',
                                        'trigger_phrases': [
                                            'opportunity stage',
                                            'sales stage',
                                            'pipeline stage',
                                            'stage definition',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What are the opportunity stages in our sales process?', 'Show me the default probabilities for each stage'],
                                        'search_strategy': 'List all stages or filter by active status',
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/sobjects/OpportunityStage/{id}',
                    action=Action.GET,
                    description='Get a single opportunity stage by ID. Returns all accessible fields by default.\nUse the `fields` parameter to retrieve only specific fields for better performance.\n',
                    query_params=['fields'],
                    query_params_schema={
                        'fields': {'type': 'string', 'required': False},
                    },
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Salesforce OpportunityStage object - uses FIELDS(STANDARD) so all standard fields are returned',
                        'properties': {
                            'Id': {'type': 'string', 'description': 'Unique identifier'},
                            'MasterLabel': {'type': 'string', 'description': 'Display label for the stage'},
                            'attributes': {
                                'type': 'object',
                                'properties': {
                                    'type': {'type': 'string'},
                                    'url': {'type': 'string'},
                                },
                            },
                        },
                        'additionalProperties': True,
                        'x-airbyte-entity-name': 'opportunity_stages',
                        'x-airbyte-stream-name': 'OpportunityStage',
                        'x-airbyte-ai-hints': {
                            'summary': 'Sales process stages that opportunities move through',
                            'when_to_use': 'Looking up opportunity stage definitions, probabilities, or sales process configuration',
                            'trigger_phrases': [
                                'opportunity stage',
                                'sales stage',
                                'pipeline stage',
                                'stage definition',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What are the opportunity stages in our sales process?', 'Show me the default probabilities for each stage'],
                            'search_strategy': 'List all stages or filter by active status',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Salesforce OpportunityStage object - uses FIELDS(STANDARD) so all standard fields are returned',
                'properties': {
                    'Id': {'type': 'string', 'description': 'Unique identifier'},
                    'MasterLabel': {'type': 'string', 'description': 'Display label for the stage'},
                    'attributes': {
                        'type': 'object',
                        'properties': {
                            'type': {'type': 'string'},
                            'url': {'type': 'string'},
                        },
                    },
                },
                'additionalProperties': True,
                'x-airbyte-entity-name': 'opportunity_stages',
                'x-airbyte-stream-name': 'OpportunityStage',
                'x-airbyte-ai-hints': {
                    'summary': 'Sales process stages that opportunities move through',
                    'when_to_use': 'Looking up opportunity stage definitions, probabilities, or sales process configuration',
                    'trigger_phrases': [
                        'opportunity stage',
                        'sales stage',
                        'pipeline stage',
                        'stage definition',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What are the opportunity stages in our sales process?', 'Show me the default probabilities for each stage'],
                    'search_strategy': 'List all stages or filter by active status',
                },
            },
            ai_hints={
                'summary': 'Sales process stages that opportunities move through',
                'when_to_use': 'Looking up opportunity stage definitions, probabilities, or sales process configuration',
                'trigger_phrases': [
                    'opportunity stage',
                    'sales stage',
                    'pipeline stage',
                    'stage definition',
                ],
                'freshness': 'live',
                'example_questions': ['What are the opportunity stages in our sales process?', 'Show me the default probabilities for each stage'],
                'search_strategy': 'List all stages or filter by active status',
            },
            relationships=[
                EntityRelationshipConfig(
                    source_entity='opportunity_stages',
                    target_entity='users',
                    foreign_key='CreatedById',
                    target_key='Id',
                    cardinality='many_to_one',
                ),
            ],
        ),
        EntityDefinition(
            name='query',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/query',
                    action=Action.LIST,
                    description='Execute a custom SOQL query and return results. Use this for querying any Salesforce object.\nFor pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.\n',
                    query_params=['q'],
                    query_params_schema={
                        'q': {
                            'type': 'string',
                            'required': True,
                            'default': 'SELECT Id FROM Organization LIMIT 1',
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Generic SOQL query result',
                        'properties': {
                            'totalSize': {'type': 'integer', 'description': 'Total number of records matching the query'},
                            'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                            'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results (if done is false)'},
                            'records': {
                                'type': 'array',
                                'description': 'Array of record objects',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                        'x-airbyte-entity-name': 'query',
                        'x-airbyte-ai-hints': {
                            'summary': 'SOQL query results from Salesforce',
                            'when_to_use': 'Running custom queries against Salesforce data',
                            'trigger_phrases': ['SOQL query', 'salesforce query', 'custom query'],
                            'freshness': 'live',
                            'example_questions': ['Run a query against Salesforce'],
                            'search_strategy': 'Write SOQL queries with WHERE clauses for filtering',
                        },
                    },
                    record_extractor='$.records',
                    meta_extractor={'done': '$.done', 'nextRecordsUrl': '$.nextRecordsUrl'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Generic SOQL query result',
                'properties': {
                    'totalSize': {'type': 'integer', 'description': 'Total number of records matching the query'},
                    'done': {'type': 'boolean', 'description': 'Whether all records have been returned'},
                    'nextRecordsUrl': {'type': 'string', 'description': 'URL to fetch next page of results (if done is false)'},
                    'records': {
                        'type': 'array',
                        'description': 'Array of record objects',
                        'items': {'type': 'object', 'additionalProperties': True},
                    },
                },
                'x-airbyte-entity-name': 'query',
                'x-airbyte-ai-hints': {
                    'summary': 'SOQL query results from Salesforce',
                    'when_to_use': 'Running custom queries against Salesforce data',
                    'trigger_phrases': ['SOQL query', 'salesforce query', 'custom query'],
                    'freshness': 'live',
                    'example_questions': ['Run a query against Salesforce'],
                    'search_strategy': 'Write SOQL queries with WHERE clauses for filtering',
                },
            },
            ai_hints={
                'summary': 'SOQL query results from Salesforce',
                'when_to_use': 'Running custom queries against Salesforce data',
                'trigger_phrases': ['SOQL query', 'salesforce query', 'custom query'],
                'freshness': 'live',
                'example_questions': ['Run a query against Salesforce'],
                'search_strategy': 'Write SOQL queries with WHERE clauses for filtering',
            },
        ),
    ],
    search_field_paths={
        'accounts': [
            'Id',
            'Name',
            'AccountSource',
            'BillingAddress',
            'BillingCity',
            'BillingCountry',
            'BillingPostalCode',
            'BillingState',
            'BillingStreet',
            'CreatedById',
            'CreatedDate',
            'Description',
            'Industry',
            'IsDeleted',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'NumberOfEmployees',
            'OwnerId',
            'ParentId',
            'Phone',
            'ShippingAddress',
            'ShippingCity',
            'ShippingCountry',
            'ShippingPostalCode',
            'ShippingState',
            'ShippingStreet',
            'Type',
            'Website',
            'SystemModstamp',
        ],
        'contacts': [
            'Id',
            'AccountId',
            'CreatedById',
            'CreatedDate',
            'Department',
            'Email',
            'FirstName',
            'IsDeleted',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LastName',
            'LeadSource',
            'MailingAddress',
            'MailingCity',
            'MailingCountry',
            'MailingPostalCode',
            'MailingState',
            'MailingStreet',
            'MobilePhone',
            'Name',
            'OwnerId',
            'Phone',
            'ReportsToId',
            'Title',
            'SystemModstamp',
        ],
        'leads': [
            'Id',
            'Address',
            'City',
            'Company',
            'ConvertedAccountId',
            'ConvertedContactId',
            'ConvertedDate',
            'ConvertedOpportunityId',
            'Country',
            'CreatedById',
            'CreatedDate',
            'Email',
            'FirstName',
            'Industry',
            'IsConverted',
            'IsDeleted',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LastName',
            'LeadSource',
            'MobilePhone',
            'Name',
            'NumberOfEmployees',
            'OwnerId',
            'Phone',
            'PostalCode',
            'Rating',
            'State',
            'Status',
            'Street',
            'Title',
            'Website',
            'SystemModstamp',
        ],
        'opportunities': [
            'Id',
            'AccountId',
            'Amount',
            'CampaignId',
            'CloseDate',
            'ContactId',
            'CreatedById',
            'CreatedDate',
            'Description',
            'ExpectedRevenue',
            'ForecastCategory',
            'ForecastCategoryName',
            'IsClosed',
            'IsDeleted',
            'IsWon',
            'LastActivityDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LeadSource',
            'Name',
            'NextStep',
            'OwnerId',
            'Probability',
            'StageName',
            'Type',
            'SystemModstamp',
        ],
        'tasks': [
            'Id',
            'AccountId',
            'ActivityDate',
            'CallDisposition',
            'CallDurationInSeconds',
            'CallType',
            'CompletedDateTime',
            'CreatedById',
            'CreatedDate',
            'Description',
            'IsClosed',
            'IsDeleted',
            'IsHighPriority',
            'LastModifiedById',
            'LastModifiedDate',
            'OwnerId',
            'Priority',
            'Status',
            'Subject',
            'TaskSubtype',
            'Type',
            'WhatId',
            'WhoId',
            'SystemModstamp',
        ],
        'users': [
            'Id',
            'AccountId',
            'Alias',
            'City',
            'CompanyName',
            'ContactId',
            'Country',
            'CreatedById',
            'CreatedDate',
            'Department',
            'Division',
            'Email',
            'EmployeeNumber',
            'FirstName',
            'IsActive',
            'LastLoginDate',
            'LastModifiedById',
            'LastModifiedDate',
            'LastName',
            'ManagerId',
            'MobilePhone',
            'Name',
            'Phone',
            'PostalCode',
            'ProfileId',
            'State',
            'Street',
            'Title',
            'UserRoleId',
            'UserType',
            'Username',
            'SystemModstamp',
        ],
        'opportunity_stages': [
            'Id',
            'ApiName',
            'CreatedById',
            'CreatedDate',
            'DefaultProbability',
            'Description',
            'ForecastCategory',
            'ForecastCategoryName',
            'IsActive',
            'IsClosed',
            'IsWon',
            'LastModifiedById',
            'LastModifiedDate',
            'MasterLabel',
            'SortOrder',
            'SystemModstamp',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List recent contacts in my Salesforce account',
            'List open cases in my Salesforce account',
            'Show me the notes and attachments for a recent account',
            'List all available reports in Salesforce',
            'Run my quarterly revenue report and show the results',
        ],
        context_store_search=[
            'Show me my top 5 opportunities this month',
            'List all contacts from {company} in the last quarter',
            'Search for leads in the technology sector with revenue over $10M',
            'What trends can you identify in my recent sales pipeline?',
            'Summarize the open cases for my key accounts',
            'Find upcoming events related to my most important opportunities',
            'Analyze the performance of my recent marketing campaigns',
            "Identify the highest value opportunities I'm currently tracking",
        ],
        search=[
            'Show me my top 5 opportunities this month',
            'List all contacts from {company} in the last quarter',
            'Search for leads in the technology sector with revenue over $10M',
            'What trends can you identify in my recent sales pipeline?',
            'Summarize the open cases for my key accounts',
            'Find upcoming events related to my most important opportunities',
            'Analyze the performance of my recent marketing campaigns',
            "Identify the highest value opportunities I'm currently tracking",
        ],
        unsupported=[
            'Create a new lead for {person}',
            'Update the status of my sales opportunity',
            'Schedule a follow-up meeting with {customer}',
            'Delete this old contact record',
            'Send an email to all contacts in this campaign',
        ],
    ),
    server_variable_defaults={'instance_url': 'https://login.salesforce.com'},
)