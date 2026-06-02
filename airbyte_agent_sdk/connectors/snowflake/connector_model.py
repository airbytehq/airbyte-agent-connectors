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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
            name='record',
            actions=[
                Action.GET,
                Action.LIST,
                Action.CREATE,
                Action.UPDATE,
                Action.DELETE,
            ],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:record_get',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.GET,
                    description='Execute a SQL SELECT statement and return the result set. Typically used to retrieve a single row by filtering on a unique identifier (e.g., SELECT * FROM users WHERE id = 42). The result is returned as rows, the same shape as the list action; when the SELECT targets one row the result contains a single row. Intended for row retrieval only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_schema={
                        'type': 'object',
                        'required': ['statement'],
                        'properties': {
                            'statement': {'type': 'string', 'description': 'SQL SELECT statement to retrieve a single record (e.g., SELECT * FROM users WHERE id = 42)'},
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'record',
                        'x-airbyte-ai-hints': {
                            'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                            'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                            'trigger_phrases': [
                                'query records',
                                'select from table',
                                'insert into table',
                                'update record',
                                'delete record',
                            ],
                            'freshness': 'live',
                            'example_questions': [
                                'Get the record with id 42 from the users table',
                                'List all records from the orders table',
                                'Insert a new row into the customers table',
                                'Update the email for user 7 in the users table',
                                'Delete the record with id 99 from the logs table',
                            ],
                            'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
                        },
                    },
                ),
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:record_list',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.LIST,
                    description="Execute a SQL SELECT query that returns multiple records from a Snowflake table or view. Use this action when you need to retrieve a set of rows, optionally with filtering, sorting, or limiting (e.g., SELECT * FROM orders WHERE status = 'active' ORDER BY created_at DESC LIMIT 100). Intended for row retrieval only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.",
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    request_schema={
                        'type': 'object',
                        'required': ['statement'],
                        'properties': {
                            'statement': {'type': 'string', 'description': "SQL SELECT statement to retrieve multiple records (e.g., SELECT * FROM orders WHERE status = 'active' LIMIT 100)"},
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'record',
                        'x-airbyte-ai-hints': {
                            'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                            'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                            'trigger_phrases': [
                                'query records',
                                'select from table',
                                'insert into table',
                                'update record',
                                'delete record',
                            ],
                            'freshness': 'live',
                            'example_questions': [
                                'Get the record with id 42 from the users table',
                                'List all records from the orders table',
                                'Insert a new row into the customers table',
                                'Update the email for user 7 in the users table',
                                'Delete the record with id 99 from the logs table',
                            ],
                            'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
                        },
                    },
                    meta_extractor={
                        'next_page_url': '@link.next',
                        'request_id': '$.requestId',
                        'statement_handle': '$.statementHandle',
                        'partition_info': '$.resultSetMetaData.partitionInfo',
                    },
                ),
                Action.CREATE: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:record_create',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.CREATE,
                    description="Execute a SQL INSERT statement to create one or more new rows in a Snowflake table (e.g., INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')). Intended for row insertion only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE TABLE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.",
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    query_params=['requestId', 'retry'],
                    query_params_schema={
                        'requestId': {'type': 'string', 'required': False},
                        'retry': {'type': 'boolean', 'required': False},
                    },
                    request_schema={
                        'type': 'object',
                        'required': ['statement'],
                        'properties': {
                            'statement': {'type': 'string', 'description': "SQL INSERT statement to create new records (e.g., INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com'))"},
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'record',
                        'x-airbyte-ai-hints': {
                            'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                            'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                            'trigger_phrases': [
                                'query records',
                                'select from table',
                                'insert into table',
                                'update record',
                                'delete record',
                            ],
                            'freshness': 'live',
                            'example_questions': [
                                'Get the record with id 42 from the users table',
                                'List all records from the orders table',
                                'Insert a new row into the customers table',
                                'Update the email for user 7 in the users table',
                                'Delete the record with id 99 from the logs table',
                            ],
                            'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
                        },
                    },
                ),
                Action.UPDATE: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:record_update',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.UPDATE,
                    description="Execute a SQL UPDATE statement to modify existing rows in a Snowflake table (e.g., UPDATE users SET email = 'new@example.com' WHERE id = 7). Intended for row modification only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, ALTER) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.",
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    query_params=['requestId', 'retry'],
                    query_params_schema={
                        'requestId': {'type': 'string', 'required': False},
                        'retry': {'type': 'boolean', 'required': False},
                    },
                    request_schema={
                        'type': 'object',
                        'required': ['statement'],
                        'properties': {
                            'statement': {'type': 'string', 'description': "SQL UPDATE statement to modify existing records (e.g., UPDATE users SET email = 'new@example.com' WHERE id = 7)"},
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'record',
                        'x-airbyte-ai-hints': {
                            'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                            'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                            'trigger_phrases': [
                                'query records',
                                'select from table',
                                'insert into table',
                                'update record',
                                'delete record',
                            ],
                            'freshness': 'live',
                            'example_questions': [
                                'Get the record with id 42 from the users table',
                                'List all records from the orders table',
                                'Insert a new row into the customers table',
                                'Update the email for user 7 in the users table',
                                'Delete the record with id 99 from the logs table',
                            ],
                            'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
                        },
                    },
                ),
                Action.DELETE: EndpointDefinition(
                    method='POST',
                    path='/api/v2/statements:record_delete',
                    path_override=PathOverrideConfig(
                        path='/api/v2/statements',
                    ),
                    action=Action.DELETE,
                    description='Execute a SQL DELETE statement to remove rows from a Snowflake table (e.g., DELETE FROM logs WHERE id = 99). Intended for row deletion only. This is not a general-purpose SQL endpoint: it does not perform DDL/DCL (DROP, TRUNCATE, GRANT, CREATE) — issue the matching CRUD action for the operation you intend. Parameterized bind variables (the SQL API bindings field / ? placeholders) are not supported in this beta; inline literal values into the statement.',
                    body_fields=[
                        'statement',
                        'database',
                        'schema',
                        'warehouse',
                        'role',
                        'timeout',
                        'parameters',
                    ],
                    query_params=['requestId', 'retry'],
                    query_params_schema={
                        'requestId': {'type': 'string', 'required': False},
                        'retry': {'type': 'boolean', 'required': False},
                    },
                    request_schema={
                        'type': 'object',
                        'required': ['statement'],
                        'properties': {
                            'statement': {'type': 'string', 'description': 'SQL DELETE statement to remove records (e.g., DELETE FROM logs WHERE id = 99)'},
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'record',
                        'x-airbyte-ai-hints': {
                            'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                            'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                            'trigger_phrases': [
                                'query records',
                                'select from table',
                                'insert into table',
                                'update record',
                                'delete record',
                            ],
                            'freshness': 'live',
                            'example_questions': [
                                'Get the record with id 42 from the users table',
                                'List all records from the orders table',
                                'Insert a new row into the customers table',
                                'Update the email for user 7 in the users table',
                                'Delete the record with id 99 from the logs table',
                            ],
                            'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
                },
                'x-airbyte-entity-name': 'record',
                'x-airbyte-ai-hints': {
                    'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                    'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                    'trigger_phrases': [
                        'query records',
                        'select from table',
                        'insert into table',
                        'update record',
                        'delete record',
                    ],
                    'freshness': 'live',
                    'example_questions': [
                        'Get the record with id 42 from the users table',
                        'List all records from the orders table',
                        'Insert a new row into the customers table',
                        'Update the email for user 7 in the users table',
                        'Delete the record with id 99 from the logs table',
                    ],
                    'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
                },
            },
            ai_hints={
                'summary': 'Read, create, update, and delete rows in Snowflake tables and views via the SQL API. Each CRUD action maps to its SQL verb.',
                'when_to_use': 'When the user wants to query, insert, update, or delete actual data records in Snowflake tables or views. Use the get action for single-row SELECT, list for multi-row SELECT, create for INSERT, update for UPDATE, and delete for DELETE.',
                'trigger_phrases': [
                    'query records',
                    'select from table',
                    'insert into table',
                    'update record',
                    'delete record',
                ],
                'freshness': 'live',
                'example_questions': [
                    'Get the record with id 42 from the users table',
                    'List all records from the orders table',
                    'Insert a new row into the customers table',
                    'Update the email for user 7 in the users table',
                    'Delete the record with id 99 from the logs table',
                ],
                'search_strategy': "Use the record action that matches the intended CRUD operation (get/list for SELECT, create for INSERT, update for UPDATE, delete for DELETE). Pass the SQL statement in the request body; it should match that action's SQL verb. Set database, schema, warehouse, and role fields as needed for execution context.",
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
                            'stats': {
                                'type': 'object',
                                'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                                'properties': {
                                    'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                                    'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                                    'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                                    'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                                },
                            },
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
                    untested=True,
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
                    'stats': {
                        'type': 'object',
                        'description': 'DML statistics returned for INSERT, UPDATE, DELETE, and MERGE statements. Not present for SELECT or SHOW queries.',
                        'properties': {
                            'numRowsInserted': {'type': 'integer', 'description': 'Number of rows inserted'},
                            'numRowsDeleted': {'type': 'integer', 'description': 'Number of rows deleted'},
                            'numRowsUpdated': {'type': 'integer', 'description': 'Number of rows updated'},
                            'numDmlDuplicates': {'type': 'integer', 'description': 'Number of duplicate rows skipped'},
                        },
                    },
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
            'Get the record with id 42 from the users table',
            'List all records from the orders table',
            'Insert a new row into the customers table',
            'Update the email for user 7 in the users table',
            'Delete the record with id 99 from the logs table',
        ],
        context_store_search=[
            'Find all tables in the ANALYTICS database',
            'Which warehouses are currently running?',
            'Show me all views in the PUBLIC schema',
            'What databases were created this month?',
            'Find all orders placed in the last 30 days',
            'Search for users with email ending in @example.com',
        ],
        search=[
            'Find all tables in the ANALYTICS database',
            'Which warehouses are currently running?',
            'Show me all views in the PUBLIC schema',
            'What databases were created this month?',
            'Find all orders placed in the last 30 days',
            'Search for users with email ending in @example.com',
        ],
    ),
    server_variable_defaults={'account': 'orgname-accountname'},
)