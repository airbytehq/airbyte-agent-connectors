"""
Connector model for snowflake.

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
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from airbyte_agent_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

SnowflakeConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('e2d65910-8c8b-40a1-ae7d-ee2416b2bfa2'),
    name='snowflake',
    base_url='https://{account}.snowflakecomputing.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'additional_headers': {'X-Snowflake-Authorization-Token-Type': 'PROGRAMMATIC_ACCESS_TOKEN'},
        },
        user_config_spec=AuthConfigSpec(
            title='PAT Authentication',
            type='object',
            required=['programmatic_access_token'],
            properties={
                'programmatic_access_token': AuthConfigFieldSpec(
                    title='Programmatic Access Token',
                    description='Snowflake Programmatic Access Token (PAT) for authentication. Generate one via ALTER USER ADD PROGRAMMATIC ACCESS TOKEN in Snowflake.',
                    airbyte_secret=True,
                ),
            },
            auth_mapping={'token': '${programmatic_access_token}'},
            replication_auth_key_mapping={'credentials.programmatic_access_token': 'programmatic_access_token'},
            additional_headers={'X-Snowflake-Authorization-Token-Type': 'PROGRAMMATIC_ACCESS_TOKEN'},
            replication_auth_key_constants={'credentials.auth_type': 'Programmatic Access Token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='databases',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:databases',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description='List databases',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_body_defaults={'statement': 'SHOW DATABASES'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'statement': {
                                'type': 'string',
                                'default': 'SHOW DATABASES',
                                'enum': ['SHOW DATABASES'],
                                'description': 'SQL statement to execute',
                            },
                            'database': {'type': 'string', 'description': 'Database context for the statement'},
                            'schema': {'type': 'string', 'description': 'Schema context for the statement'},
                            'warehouse': {'type': 'string', 'description': 'Warehouse to use for execution'},
                            'role': {'type': 'string', 'description': 'Role to use for execution'},
                            'timeout': {'type': 'integer', 'description': 'Timeout in seconds for the statement execution'},
                            'parameters': {
                                'type': 'object',
                                'description': 'Session parameters for the statement execution',
                                'additionalProperties': True,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'databases',
                        'x-airbyte-ai-hints': {
                            'summary': 'Snowflake databases accessible to the current user',
                            'when_to_use': 'When listing available databases or checking database metadata',
                            'trigger_phrases': ['list databases', 'show databases', 'what databases exist'],
                            'freshness': 'live',
                            'example_questions': ['What databases are available in Snowflake?', 'List all Snowflake databases'],
                            'search_strategy': 'Execute SHOW DATABASES via the SQL API',
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'databases',
                'x-airbyte-ai-hints': {
                    'summary': 'Snowflake databases accessible to the current user',
                    'when_to_use': 'When listing available databases or checking database metadata',
                    'trigger_phrases': ['list databases', 'show databases', 'what databases exist'],
                    'freshness': 'live',
                    'example_questions': ['What databases are available in Snowflake?', 'List all Snowflake databases'],
                    'search_strategy': 'Execute SHOW DATABASES via the SQL API',
                },
            },
            ai_hints={
                'summary': 'Snowflake databases accessible to the current user',
                'when_to_use': 'When listing available databases or checking database metadata',
                'trigger_phrases': ['list databases', 'show databases', 'what databases exist'],
                'freshness': 'live',
                'example_questions': ['What databases are available in Snowflake?', 'List all Snowflake databases'],
                'search_strategy': 'Execute SHOW DATABASES via the SQL API',
            },
        ),
        EntityDefinition(
            name='schemas',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:schemas',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description='List schemas',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_body_defaults={'statement': 'SHOW SCHEMAS'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'statement': {
                                'type': 'string',
                                'default': 'SHOW SCHEMAS',
                                'enum': ['SHOW SCHEMAS'],
                                'description': 'SQL statement to execute',
                            },
                            'database': {'type': 'string', 'description': 'Database context for the statement'},
                            'schema': {'type': 'string', 'description': 'Schema context for the statement'},
                            'warehouse': {'type': 'string', 'description': 'Warehouse to use for execution'},
                            'role': {'type': 'string', 'description': 'Role to use for execution'},
                            'timeout': {'type': 'integer', 'description': 'Timeout in seconds for the statement execution'},
                            'parameters': {
                                'type': 'object',
                                'description': 'Session parameters for the statement execution',
                                'additionalProperties': True,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'schemas',
                        'x-airbyte-ai-hints': {
                            'summary': 'Snowflake schemas within databases',
                            'when_to_use': 'When listing schemas or exploring database structure',
                            'trigger_phrases': ['list schemas', 'show schemas', 'what schemas exist'],
                            'freshness': 'live',
                            'example_questions': ['What schemas are in this database?', 'Show all schemas'],
                            'search_strategy': 'Execute SHOW SCHEMAS via the SQL API',
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'schemas',
                'x-airbyte-ai-hints': {
                    'summary': 'Snowflake schemas within databases',
                    'when_to_use': 'When listing schemas or exploring database structure',
                    'trigger_phrases': ['list schemas', 'show schemas', 'what schemas exist'],
                    'freshness': 'live',
                    'example_questions': ['What schemas are in this database?', 'Show all schemas'],
                    'search_strategy': 'Execute SHOW SCHEMAS via the SQL API',
                },
            },
            ai_hints={
                'summary': 'Snowflake schemas within databases',
                'when_to_use': 'When listing schemas or exploring database structure',
                'trigger_phrases': ['list schemas', 'show schemas', 'what schemas exist'],
                'freshness': 'live',
                'example_questions': ['What schemas are in this database?', 'Show all schemas'],
                'search_strategy': 'Execute SHOW SCHEMAS via the SQL API',
            },
        ),
        EntityDefinition(
            name='tables',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:tables',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description='List tables',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_body_defaults={'statement': 'SHOW TABLES'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'statement': {
                                'type': 'string',
                                'default': 'SHOW TABLES',
                                'enum': ['SHOW TABLES'],
                                'description': 'SQL statement to execute',
                            },
                            'database': {'type': 'string', 'description': 'Database context for the statement'},
                            'schema': {'type': 'string', 'description': 'Schema context for the statement'},
                            'warehouse': {'type': 'string', 'description': 'Warehouse to use for execution'},
                            'role': {'type': 'string', 'description': 'Role to use for execution'},
                            'timeout': {'type': 'integer', 'description': 'Timeout in seconds for the statement execution'},
                            'parameters': {
                                'type': 'object',
                                'description': 'Session parameters for the statement execution',
                                'additionalProperties': True,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'tables',
                        'x-airbyte-ai-hints': {
                            'summary': 'Snowflake tables with metadata like row count, size, and clustering',
                            'when_to_use': 'When listing tables or checking table properties',
                            'trigger_phrases': ['list tables', 'show tables', 'what tables exist'],
                            'freshness': 'live',
                            'example_questions': ['What tables are available?', 'Show me all tables in the database'],
                            'search_strategy': 'Execute SHOW TABLES via the SQL API',
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'tables',
                'x-airbyte-ai-hints': {
                    'summary': 'Snowflake tables with metadata like row count, size, and clustering',
                    'when_to_use': 'When listing tables or checking table properties',
                    'trigger_phrases': ['list tables', 'show tables', 'what tables exist'],
                    'freshness': 'live',
                    'example_questions': ['What tables are available?', 'Show me all tables in the database'],
                    'search_strategy': 'Execute SHOW TABLES via the SQL API',
                },
            },
            ai_hints={
                'summary': 'Snowflake tables with metadata like row count, size, and clustering',
                'when_to_use': 'When listing tables or checking table properties',
                'trigger_phrases': ['list tables', 'show tables', 'what tables exist'],
                'freshness': 'live',
                'example_questions': ['What tables are available?', 'Show me all tables in the database'],
                'search_strategy': 'Execute SHOW TABLES via the SQL API',
            },
        ),
        EntityDefinition(
            name='views',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:views',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description='List views',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_body_defaults={'statement': 'SHOW VIEWS'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'statement': {
                                'type': 'string',
                                'default': 'SHOW VIEWS',
                                'enum': ['SHOW VIEWS'],
                                'description': 'SQL statement to execute',
                            },
                            'database': {'type': 'string', 'description': 'Database context for the statement'},
                            'schema': {'type': 'string', 'description': 'Schema context for the statement'},
                            'warehouse': {'type': 'string', 'description': 'Warehouse to use for execution'},
                            'role': {'type': 'string', 'description': 'Role to use for execution'},
                            'timeout': {'type': 'integer', 'description': 'Timeout in seconds for the statement execution'},
                            'parameters': {
                                'type': 'object',
                                'description': 'Session parameters for the statement execution',
                                'additionalProperties': True,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'views',
                        'x-airbyte-ai-hints': {
                            'summary': 'Snowflake views including materialized views',
                            'when_to_use': 'When listing views or checking view definitions',
                            'trigger_phrases': ['list views', 'show views', 'what views exist'],
                            'freshness': 'live',
                            'example_questions': ['What views are defined?', 'Show all views in the schema'],
                            'search_strategy': 'Execute SHOW VIEWS via the SQL API',
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'views',
                'x-airbyte-ai-hints': {
                    'summary': 'Snowflake views including materialized views',
                    'when_to_use': 'When listing views or checking view definitions',
                    'trigger_phrases': ['list views', 'show views', 'what views exist'],
                    'freshness': 'live',
                    'example_questions': ['What views are defined?', 'Show all views in the schema'],
                    'search_strategy': 'Execute SHOW VIEWS via the SQL API',
                },
            },
            ai_hints={
                'summary': 'Snowflake views including materialized views',
                'when_to_use': 'When listing views or checking view definitions',
                'trigger_phrases': ['list views', 'show views', 'what views exist'],
                'freshness': 'live',
                'example_questions': ['What views are defined?', 'Show all views in the schema'],
                'search_strategy': 'Execute SHOW VIEWS via the SQL API',
            },
        ),
        EntityDefinition(
            name='warehouses',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:warehouses',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description='List warehouses',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_body_defaults={'statement': 'SHOW WAREHOUSES'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'statement': {
                                'type': 'string',
                                'default': 'SHOW WAREHOUSES',
                                'enum': ['SHOW WAREHOUSES'],
                                'description': 'SQL statement to execute',
                            },
                            'database': {'type': 'string', 'description': 'Database context for the statement'},
                            'schema': {'type': 'string', 'description': 'Schema context for the statement'},
                            'warehouse': {'type': 'string', 'description': 'Warehouse to use for execution'},
                            'role': {'type': 'string', 'description': 'Role to use for execution'},
                            'timeout': {'type': 'integer', 'description': 'Timeout in seconds for the statement execution'},
                            'parameters': {
                                'type': 'object',
                                'description': 'Session parameters for the statement execution',
                                'additionalProperties': True,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'warehouses',
                        'x-airbyte-ai-hints': {
                            'summary': 'Snowflake virtual warehouses with state, size, and configuration',
                            'when_to_use': 'When listing warehouses or checking warehouse status',
                            'trigger_phrases': ['list warehouses', 'show warehouses', 'warehouse status'],
                            'freshness': 'live',
                            'example_questions': ['What warehouses are configured?', 'Which warehouses are running?'],
                            'search_strategy': 'Execute SHOW WAREHOUSES via the SQL API',
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'warehouses',
                'x-airbyte-ai-hints': {
                    'summary': 'Snowflake virtual warehouses with state, size, and configuration',
                    'when_to_use': 'When listing warehouses or checking warehouse status',
                    'trigger_phrases': ['list warehouses', 'show warehouses', 'warehouse status'],
                    'freshness': 'live',
                    'example_questions': ['What warehouses are configured?', 'Which warehouses are running?'],
                    'search_strategy': 'Execute SHOW WAREHOUSES via the SQL API',
                },
            },
            ai_hints={
                'summary': 'Snowflake virtual warehouses with state, size, and configuration',
                'when_to_use': 'When listing warehouses or checking warehouse status',
                'trigger_phrases': ['list warehouses', 'show warehouses', 'warehouse status'],
                'freshness': 'live',
                'example_questions': ['What warehouses are configured?', 'Which warehouses are running?'],
                'search_strategy': 'Execute SHOW WAREHOUSES via the SQL API',
            },
        ),
        EntityDefinition(
            name='columns',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:columns',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description='List columns',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_body_defaults={'statement': 'SHOW COLUMNS'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'statement': {
                                'type': 'string',
                                'default': 'SHOW COLUMNS',
                                'enum': ['SHOW COLUMNS'],
                                'description': 'SQL statement to execute',
                            },
                            'database': {'type': 'string', 'description': 'Database context for the statement'},
                            'schema': {'type': 'string', 'description': 'Schema context for the statement'},
                            'warehouse': {'type': 'string', 'description': 'Warehouse to use for execution'},
                            'role': {'type': 'string', 'description': 'Role to use for execution'},
                            'timeout': {'type': 'integer', 'description': 'Timeout in seconds for the statement execution'},
                            'parameters': {
                                'type': 'object',
                                'description': 'Session parameters for the statement execution',
                                'additionalProperties': True,
                            },
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'columns',
                        'x-airbyte-ai-hints': {
                            'summary': 'Snowflake table and view columns with data types and metadata',
                            'when_to_use': 'When listing columns or inspecting table schema',
                            'trigger_phrases': [
                                'list columns',
                                'show columns',
                                'what columns exist',
                                'table schema',
                            ],
                            'freshness': 'live',
                            'example_questions': ['What columns does this table have?', 'Show me the column definitions'],
                            'search_strategy': 'Execute SHOW COLUMNS via the SQL API',
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'columns',
                'x-airbyte-ai-hints': {
                    'summary': 'Snowflake table and view columns with data types and metadata',
                    'when_to_use': 'When listing columns or inspecting table schema',
                    'trigger_phrases': [
                        'list columns',
                        'show columns',
                        'what columns exist',
                        'table schema',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What columns does this table have?', 'Show me the column definitions'],
                    'search_strategy': 'Execute SHOW COLUMNS via the SQL API',
                },
            },
            ai_hints={
                'summary': 'Snowflake table and view columns with data types and metadata',
                'when_to_use': 'When listing columns or inspecting table schema',
                'trigger_phrases': [
                    'list columns',
                    'show columns',
                    'what columns exist',
                    'table schema',
                ],
                'freshness': 'live',
                'example_questions': ['What columns does this table have?', 'Show me the column definitions'],
                'search_strategy': 'Execute SHOW COLUMNS via the SQL API',
            },
        ),
        EntityDefinition(
            name='result_partitions',
            actions=[Action.GET],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/api/v2/statements/{statementHandle}:partition',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements/{statementHandle}',
                    ),
                    action=Action.GET,
                    description='Continuation helper for Snowflake list actions. Use this only after a databases, schemas, tables, views, warehouses, or columns list response includes a next_page_url or multiple partitionInfo entries. The initial list response contains partition 0; call this action with partition 1, 2, and so on to retrieve additional rows for the same SHOW statement. This is not a standalone Snowflake resource and does not execute new SQL.',
                    query_params=['partition', 'requestId'],
                    query_params_schema={
                        'partition': {
                            'type': 'integer',
                            'required': True,
                            'minimum': 0,
                        },
                        'requestId': {'type': 'string', 'required': False},
                    },
                    path_params=['statementHandle'],
                    path_params_schema={
                        'statementHandle': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                            'resultSetMetaData': {
                                'type': 'object',
                                'description': 'Metadata about the result set',
                                'properties': {
                                    'numRows': {'type': 'integer', 'description': 'Total number of rows in the result set'},
                                    'format': {'type': 'string', 'description': 'Format of the result data (e.g., jsonv2)'},
                                    'rowType': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Column metadata describing a single column in the result set',
                                            'properties': {
                                                'name': {'type': 'string', 'description': 'Column name'},
                                                'database': {'type': 'string', 'description': 'Database name'},
                                                'schema': {'type': 'string', 'description': 'Schema name'},
                                                'table': {'type': 'string', 'description': 'Table name'},
                                                'type': {'type': 'string', 'description': 'Snowflake data type (text, fixed, real, boolean, etc.)'},
                                                'scale': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Decimal scale for numeric types',
                                                },
                                                'precision': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Numeric precision',
                                                },
                                                'length': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum character length',
                                                },
                                                'nullable': {'type': 'boolean', 'description': 'Whether the column allows null values'},
                                                'byteLength': {
                                                    'oneOf': [
                                                        {'type': 'integer'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Maximum byte length',
                                                },
                                                'collation': {
                                                    'oneOf': [
                                                        {'type': 'string'},
                                                        {'type': 'null'},
                                                    ],
                                                    'description': 'Collation specification',
                                                },
                                            },
                                        },
                                        'description': 'Column metadata for each column in the result set',
                                    },
                                    'partitionInfo': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'description': 'Information about a result partition',
                                            'properties': {
                                                'rowCount': {'type': 'integer', 'description': 'Number of rows in this partition'},
                                                'uncompressedSize': {'type': 'integer', 'description': 'Uncompressed size of the partition in bytes'},
                                                'compressedSize': {'type': 'integer', 'description': 'Compressed size of the partition in bytes'},
                                            },
                                        },
                                        'description': 'Information about result partitions',
                                    },
                                },
                            },
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'array',
                                    'items': {
                                        'oneOf': [
                                            {'type': 'string'},
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                                'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                            },
                            'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                            'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                            'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                            'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                            'message': {'type': 'string', 'description': 'Human-readable status message'},
                            'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                        },
                        'x-airbyte-entity-name': 'result_partitions',
                        'x-airbyte-ai-hints': {
                            'summary': 'Continuation helper for additional Snowflake list result partitions',
                            'when_to_use': 'Use only after a Snowflake list response includes a next_page_url or multiple resultSetMetaData.partitionInfo entries. The original list response contains partition 0; request partition 1 or higher here to fetch more rows for the same SHOW result set.',
                            'trigger_phrases': [
                                'next partition',
                                'more Snowflake results',
                                'continue pagination',
                                'fetch the next page',
                            ],
                            'freshness': 'live',
                            'example_questions': ['Fetch the next Snowflake result partition', 'Continue the previous Snowflake columns listing'],
                            'search_strategy': 'Reuse the statement_handle and request_id returned in the prior list action metadata, then call this get action with the next partition number. Do not use this entity to execute new SQL or discover metadata from scratch.',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'requestId': {'type': 'string', 'description': 'Unique request identifier for the API call'},
                    'resultSetMetaData': {'$ref': '#/components/schemas/ResultSetMetaData'},
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'array',
                            'items': {
                                'oneOf': [
                                    {'type': 'string'},
                                    {'type': 'null'},
                                ],
                            },
                        },
                        'description': 'Result rows as an array of arrays. Each inner array is a row with values as strings, matching the column order from resultSetMetaData.rowType.',
                    },
                    'code': {'type': 'string', 'description': 'Snowflake status code (e.g., 090001 for success)'},
                    'statementStatusUrl': {'type': 'string', 'description': 'URL to check statement execution status'},
                    'sqlState': {'type': 'string', 'description': 'SQL state code (e.g., 00000 for success)'},
                    'statementHandle': {'type': 'string', 'description': 'Unique handle for the executed statement'},
                    'message': {'type': 'string', 'description': 'Human-readable status message'},
                    'createdOn': {'type': 'integer', 'description': 'Unix timestamp (milliseconds) when the statement was created'},
                },
                'x-airbyte-entity-name': 'result_partitions',
                'x-airbyte-ai-hints': {
                    'summary': 'Continuation helper for additional Snowflake list result partitions',
                    'when_to_use': 'Use only after a Snowflake list response includes a next_page_url or multiple resultSetMetaData.partitionInfo entries. The original list response contains partition 0; request partition 1 or higher here to fetch more rows for the same SHOW result set.',
                    'trigger_phrases': [
                        'next partition',
                        'more Snowflake results',
                        'continue pagination',
                        'fetch the next page',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Fetch the next Snowflake result partition', 'Continue the previous Snowflake columns listing'],
                    'search_strategy': 'Reuse the statement_handle and request_id returned in the prior list action metadata, then call this get action with the next partition number. Do not use this entity to execute new SQL or discover metadata from scratch.',
                },
            },
            ai_hints={
                'summary': 'Continuation helper for additional Snowflake list result partitions',
                'when_to_use': 'Use only after a Snowflake list response includes a next_page_url or multiple resultSetMetaData.partitionInfo entries. The original list response contains partition 0; request partition 1 or higher here to fetch more rows for the same SHOW result set.',
                'trigger_phrases': [
                    'next partition',
                    'more Snowflake results',
                    'continue pagination',
                    'fetch the next page',
                ],
                'freshness': 'live',
                'example_questions': ['Fetch the next Snowflake result partition', 'Continue the previous Snowflake columns listing'],
                'search_strategy': 'Reuse the statement_handle and request_id returned in the prior list action metadata, then call this get action with the next partition number. Do not use this entity to execute new SQL or discover metadata from scratch.',
            },
        ),
    ],
    example_questions=ExampleQuestions(
        direct=[
            'List all databases in Snowflake',
            'Show me all schemas',
            'What tables are available?',
            'List all views',
            'Show me the warehouses',
            'What columns does my data have?',
        ],
        context_store_search=[
            'Find all tables in the ANALYTICS database',
            'Which warehouses are currently running?',
            'Show me all views in the PUBLIC schema',
            'What databases were created this month?',
        ],
        search=[
            'Find all tables in the ANALYTICS database',
            'Which warehouses are currently running?',
            'Show me all views in the PUBLIC schema',
            'What databases were created this month?',
        ],
        unsupported=[
            'Create a new database',
            'Drop a table',
            'Run a custom SQL query',
            'Insert data into a table',
        ],
    ),
    server_variable_defaults={'account': 'orgname-accountname'},
)