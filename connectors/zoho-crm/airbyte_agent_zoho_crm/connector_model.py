"""
Connector model for zoho-crm.

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

ZohoCrmConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('4942d392-c7b5-4271-91f9-3b4f4e51eb3e'),
    name='zoho-crm',
    version='1.0.2',
    base_url='https://www.zohoapis.{dc_region}',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://accounts.zoho.com/oauth/v2/token',
            'auth_style': 'body',
            'body_format': 'form',
            'additional_headers': {'Authorization': 'Zoho-oauthtoken {{ access_token }}'},
        },
        user_config_spec=AirbyteAuthConfig(
            title='Zoho CRM OAuth 2.0',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='OAuth 2.0 Client ID from Zoho Developer Console',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='OAuth 2.0 Client Secret from Zoho Developer Console',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='OAuth 2.0 Refresh Token (does not expire)',
                ),
            },
            auth_mapping={
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
                'refresh_token': '${refresh_token}',
            },
            replication_auth_key_mapping={
                'client_id': 'client_id',
                'client_secret': 'client_secret',
                'refresh_token': 'refresh_token',
            },
            additional_headers={'Authorization': 'Zoho-oauthtoken {{ access_token }}'},
            replication_auth_key_constants={'environment': 'Production'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='leads',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Leads',
                    action=Action.LIST,
                    description='Returns a paginated list of leads',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of leads',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM lead object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique lead identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Company': {
                                            'type': ['null', 'string'],
                                            'description': 'Company name',
                                        },
                                        'First_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'First name',
                                        },
                                        'Last_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Last name',
                                        },
                                        'Full_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Full name',
                                        },
                                        'Email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address',
                                        },
                                        'Phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'Mobile': {
                                            'type': ['null', 'string'],
                                            'description': 'Mobile number',
                                        },
                                        'Fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'Title': {
                                            'type': ['null', 'string'],
                                            'description': 'Job title',
                                        },
                                        'Lead_Source': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead source',
                                        },
                                        'Industry': {
                                            'type': ['null', 'string'],
                                            'description': 'Industry',
                                        },
                                        'Annual_Revenue': {
                                            'type': ['null', 'number'],
                                            'description': 'Annual revenue',
                                        },
                                        'No_of_Employees': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of employees',
                                        },
                                        'Rating': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead rating',
                                        },
                                        'Lead_Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead status',
                                        },
                                        'Website': {
                                            'type': ['null', 'string'],
                                            'description': 'Website URL',
                                        },
                                        'Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Street address',
                                        },
                                        'City': {
                                            'type': ['null', 'string'],
                                            'description': 'City',
                                        },
                                        'State': {
                                            'type': ['null', 'string'],
                                            'description': 'State',
                                        },
                                        'Zip_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'ZIP/postal code',
                                        },
                                        'Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Country',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Converted_Detail': {
                                            'type': ['null', 'object'],
                                            'description': 'Conversion details if lead was converted',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'leads',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Leads/{id}',
                    action=Action.GET,
                    description='Get a single lead by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of leads',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM lead object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique lead identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Company': {
                                            'type': ['null', 'string'],
                                            'description': 'Company name',
                                        },
                                        'First_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'First name',
                                        },
                                        'Last_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Last name',
                                        },
                                        'Full_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Full name',
                                        },
                                        'Email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address',
                                        },
                                        'Phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'Mobile': {
                                            'type': ['null', 'string'],
                                            'description': 'Mobile number',
                                        },
                                        'Fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'Title': {
                                            'type': ['null', 'string'],
                                            'description': 'Job title',
                                        },
                                        'Lead_Source': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead source',
                                        },
                                        'Industry': {
                                            'type': ['null', 'string'],
                                            'description': 'Industry',
                                        },
                                        'Annual_Revenue': {
                                            'type': ['null', 'number'],
                                            'description': 'Annual revenue',
                                        },
                                        'No_of_Employees': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of employees',
                                        },
                                        'Rating': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead rating',
                                        },
                                        'Lead_Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead status',
                                        },
                                        'Website': {
                                            'type': ['null', 'string'],
                                            'description': 'Website URL',
                                        },
                                        'Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Street address',
                                        },
                                        'City': {
                                            'type': ['null', 'string'],
                                            'description': 'City',
                                        },
                                        'State': {
                                            'type': ['null', 'string'],
                                            'description': 'State',
                                        },
                                        'Zip_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'ZIP/postal code',
                                        },
                                        'Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Country',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Converted_Detail': {
                                            'type': ['null', 'object'],
                                            'description': 'Conversion details if lead was converted',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'leads',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM lead object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique lead identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Company': {
                        'type': ['null', 'string'],
                        'description': 'Company name',
                    },
                    'First_Name': {
                        'type': ['null', 'string'],
                        'description': 'First name',
                    },
                    'Last_Name': {
                        'type': ['null', 'string'],
                        'description': 'Last name',
                    },
                    'Full_Name': {
                        'type': ['null', 'string'],
                        'description': 'Full name',
                    },
                    'Email': {
                        'type': ['null', 'string'],
                        'description': 'Email address',
                    },
                    'Phone': {
                        'type': ['null', 'string'],
                        'description': 'Phone number',
                    },
                    'Mobile': {
                        'type': ['null', 'string'],
                        'description': 'Mobile number',
                    },
                    'Fax': {
                        'type': ['null', 'string'],
                        'description': 'Fax number',
                    },
                    'Title': {
                        'type': ['null', 'string'],
                        'description': 'Job title',
                    },
                    'Lead_Source': {
                        'type': ['null', 'string'],
                        'description': 'Lead source',
                    },
                    'Industry': {
                        'type': ['null', 'string'],
                        'description': 'Industry',
                    },
                    'Annual_Revenue': {
                        'type': ['null', 'number'],
                        'description': 'Annual revenue',
                    },
                    'No_of_Employees': {
                        'type': ['null', 'integer'],
                        'description': 'Number of employees',
                    },
                    'Rating': {
                        'type': ['null', 'string'],
                        'description': 'Lead rating',
                    },
                    'Lead_Status': {
                        'type': ['null', 'string'],
                        'description': 'Lead status',
                    },
                    'Website': {
                        'type': ['null', 'string'],
                        'description': 'Website URL',
                    },
                    'Street': {
                        'type': ['null', 'string'],
                        'description': 'Street address',
                    },
                    'City': {
                        'type': ['null', 'string'],
                        'description': 'City',
                    },
                    'State': {
                        'type': ['null', 'string'],
                        'description': 'State',
                    },
                    'Zip_Code': {
                        'type': ['null', 'string'],
                        'description': 'ZIP/postal code',
                    },
                    'Country': {
                        'type': ['null', 'string'],
                        'description': 'Country',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Converted_Detail': {
                        'type': ['null', 'object'],
                        'description': 'Conversion details if lead was converted',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'leads',
            },
        ),
        EntityDefinition(
            name='contacts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Contacts',
                    action=Action.LIST,
                    description='Returns a paginated list of contacts',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of contacts',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM contact object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique contact identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'First_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'First name',
                                        },
                                        'Last_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Last name',
                                        },
                                        'Full_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Full name',
                                        },
                                        'Email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address',
                                        },
                                        'Phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'Mobile': {
                                            'type': ['null', 'string'],
                                            'description': 'Mobile number',
                                        },
                                        'Fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'Title': {
                                            'type': ['null', 'string'],
                                            'description': 'Job title',
                                        },
                                        'Department': {
                                            'type': ['null', 'string'],
                                            'description': 'Department',
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Lead_Source': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead source',
                                        },
                                        'Date_of_Birth': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Date of birth',
                                        },
                                        'Mailing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing street address',
                                        },
                                        'Mailing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing city',
                                        },
                                        'Mailing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing state',
                                        },
                                        'Mailing_Zip': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing ZIP/postal code',
                                        },
                                        'Mailing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing country',
                                        },
                                        'Other_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Other street address',
                                        },
                                        'Other_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Other city',
                                        },
                                        'Other_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Other state',
                                        },
                                        'Other_Zip': {
                                            'type': ['null', 'string'],
                                            'description': 'Other ZIP/postal code',
                                        },
                                        'Other_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Other country',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'contacts',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Contacts/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of contacts',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM contact object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique contact identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'First_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'First name',
                                        },
                                        'Last_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Last name',
                                        },
                                        'Full_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Full name',
                                        },
                                        'Email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email address',
                                        },
                                        'Phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'Mobile': {
                                            'type': ['null', 'string'],
                                            'description': 'Mobile number',
                                        },
                                        'Fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'Title': {
                                            'type': ['null', 'string'],
                                            'description': 'Job title',
                                        },
                                        'Department': {
                                            'type': ['null', 'string'],
                                            'description': 'Department',
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Lead_Source': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead source',
                                        },
                                        'Date_of_Birth': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Date of birth',
                                        },
                                        'Mailing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing street address',
                                        },
                                        'Mailing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing city',
                                        },
                                        'Mailing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing state',
                                        },
                                        'Mailing_Zip': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing ZIP/postal code',
                                        },
                                        'Mailing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Mailing country',
                                        },
                                        'Other_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Other street address',
                                        },
                                        'Other_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Other city',
                                        },
                                        'Other_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Other state',
                                        },
                                        'Other_Zip': {
                                            'type': ['null', 'string'],
                                            'description': 'Other ZIP/postal code',
                                        },
                                        'Other_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Other country',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'contacts',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM contact object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique contact identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'First_Name': {
                        'type': ['null', 'string'],
                        'description': 'First name',
                    },
                    'Last_Name': {
                        'type': ['null', 'string'],
                        'description': 'Last name',
                    },
                    'Full_Name': {
                        'type': ['null', 'string'],
                        'description': 'Full name',
                    },
                    'Email': {
                        'type': ['null', 'string'],
                        'description': 'Email address',
                    },
                    'Phone': {
                        'type': ['null', 'string'],
                        'description': 'Phone number',
                    },
                    'Mobile': {
                        'type': ['null', 'string'],
                        'description': 'Mobile number',
                    },
                    'Fax': {
                        'type': ['null', 'string'],
                        'description': 'Fax number',
                    },
                    'Title': {
                        'type': ['null', 'string'],
                        'description': 'Job title',
                    },
                    'Department': {
                        'type': ['null', 'string'],
                        'description': 'Department',
                    },
                    'Account_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Lead_Source': {
                        'type': ['null', 'string'],
                        'description': 'Lead source',
                    },
                    'Date_of_Birth': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Date of birth',
                    },
                    'Mailing_Street': {
                        'type': ['null', 'string'],
                        'description': 'Mailing street address',
                    },
                    'Mailing_City': {
                        'type': ['null', 'string'],
                        'description': 'Mailing city',
                    },
                    'Mailing_State': {
                        'type': ['null', 'string'],
                        'description': 'Mailing state',
                    },
                    'Mailing_Zip': {
                        'type': ['null', 'string'],
                        'description': 'Mailing ZIP/postal code',
                    },
                    'Mailing_Country': {
                        'type': ['null', 'string'],
                        'description': 'Mailing country',
                    },
                    'Other_Street': {
                        'type': ['null', 'string'],
                        'description': 'Other street address',
                    },
                    'Other_City': {
                        'type': ['null', 'string'],
                        'description': 'Other city',
                    },
                    'Other_State': {
                        'type': ['null', 'string'],
                        'description': 'Other state',
                    },
                    'Other_Zip': {
                        'type': ['null', 'string'],
                        'description': 'Other ZIP/postal code',
                    },
                    'Other_Country': {
                        'type': ['null', 'string'],
                        'description': 'Other country',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'contacts',
            },
        ),
        EntityDefinition(
            name='accounts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Accounts',
                    action=Action.LIST,
                    description='Returns a paginated list of accounts',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of accounts',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM account (company) object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique account identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Account/company name',
                                        },
                                        'Account_Number': {
                                            'type': ['null', 'string'],
                                            'description': 'Account number',
                                        },
                                        'Account_Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Account type',
                                        },
                                        'Industry': {
                                            'type': ['null', 'string'],
                                            'description': 'Industry',
                                        },
                                        'Annual_Revenue': {
                                            'type': ['null', 'number'],
                                            'description': 'Annual revenue',
                                        },
                                        'Employees': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of employees',
                                        },
                                        'Phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'Fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'Website': {
                                            'type': ['null', 'string'],
                                            'description': 'Website URL',
                                        },
                                        'Ownership': {
                                            'type': ['null', 'string'],
                                            'description': 'Ownership type',
                                        },
                                        'Rating': {
                                            'type': ['null', 'string'],
                                            'description': 'Account rating',
                                        },
                                        'SIC_Code': {
                                            'type': ['null', 'integer'],
                                            'description': 'SIC code',
                                        },
                                        'Ticker_Symbol': {
                                            'type': ['null', 'string'],
                                            'description': 'Ticker symbol',
                                        },
                                        'Parent_Account': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Billing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing street address',
                                        },
                                        'Billing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing city',
                                        },
                                        'Billing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing state',
                                        },
                                        'Billing_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing ZIP/postal code',
                                        },
                                        'Billing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing country',
                                        },
                                        'Shipping_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping street address',
                                        },
                                        'Shipping_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping city',
                                        },
                                        'Shipping_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping state',
                                        },
                                        'Shipping_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping ZIP/postal code',
                                        },
                                        'Shipping_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping country',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'accounts',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Accounts/{id}',
                    action=Action.GET,
                    description='Get a single account by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of accounts',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM account (company) object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique account identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Account/company name',
                                        },
                                        'Account_Number': {
                                            'type': ['null', 'string'],
                                            'description': 'Account number',
                                        },
                                        'Account_Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Account type',
                                        },
                                        'Industry': {
                                            'type': ['null', 'string'],
                                            'description': 'Industry',
                                        },
                                        'Annual_Revenue': {
                                            'type': ['null', 'number'],
                                            'description': 'Annual revenue',
                                        },
                                        'Employees': {
                                            'type': ['null', 'integer'],
                                            'description': 'Number of employees',
                                        },
                                        'Phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'Fax': {
                                            'type': ['null', 'string'],
                                            'description': 'Fax number',
                                        },
                                        'Website': {
                                            'type': ['null', 'string'],
                                            'description': 'Website URL',
                                        },
                                        'Ownership': {
                                            'type': ['null', 'string'],
                                            'description': 'Ownership type',
                                        },
                                        'Rating': {
                                            'type': ['null', 'string'],
                                            'description': 'Account rating',
                                        },
                                        'SIC_Code': {
                                            'type': ['null', 'integer'],
                                            'description': 'SIC code',
                                        },
                                        'Ticker_Symbol': {
                                            'type': ['null', 'string'],
                                            'description': 'Ticker symbol',
                                        },
                                        'Parent_Account': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Billing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing street address',
                                        },
                                        'Billing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing city',
                                        },
                                        'Billing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing state',
                                        },
                                        'Billing_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing ZIP/postal code',
                                        },
                                        'Billing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing country',
                                        },
                                        'Shipping_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping street address',
                                        },
                                        'Shipping_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping city',
                                        },
                                        'Shipping_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping state',
                                        },
                                        'Shipping_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping ZIP/postal code',
                                        },
                                        'Shipping_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping country',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'accounts',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM account (company) object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique account identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Account_Name': {
                        'type': ['null', 'string'],
                        'description': 'Account/company name',
                    },
                    'Account_Number': {
                        'type': ['null', 'string'],
                        'description': 'Account number',
                    },
                    'Account_Type': {
                        'type': ['null', 'string'],
                        'description': 'Account type',
                    },
                    'Industry': {
                        'type': ['null', 'string'],
                        'description': 'Industry',
                    },
                    'Annual_Revenue': {
                        'type': ['null', 'number'],
                        'description': 'Annual revenue',
                    },
                    'Employees': {
                        'type': ['null', 'integer'],
                        'description': 'Number of employees',
                    },
                    'Phone': {
                        'type': ['null', 'string'],
                        'description': 'Phone number',
                    },
                    'Fax': {
                        'type': ['null', 'string'],
                        'description': 'Fax number',
                    },
                    'Website': {
                        'type': ['null', 'string'],
                        'description': 'Website URL',
                    },
                    'Ownership': {
                        'type': ['null', 'string'],
                        'description': 'Ownership type',
                    },
                    'Rating': {
                        'type': ['null', 'string'],
                        'description': 'Account rating',
                    },
                    'SIC_Code': {
                        'type': ['null', 'integer'],
                        'description': 'SIC code',
                    },
                    'Ticker_Symbol': {
                        'type': ['null', 'string'],
                        'description': 'Ticker symbol',
                    },
                    'Parent_Account': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Billing_Street': {
                        'type': ['null', 'string'],
                        'description': 'Billing street address',
                    },
                    'Billing_City': {
                        'type': ['null', 'string'],
                        'description': 'Billing city',
                    },
                    'Billing_State': {
                        'type': ['null', 'string'],
                        'description': 'Billing state',
                    },
                    'Billing_Code': {
                        'type': ['null', 'string'],
                        'description': 'Billing ZIP/postal code',
                    },
                    'Billing_Country': {
                        'type': ['null', 'string'],
                        'description': 'Billing country',
                    },
                    'Shipping_Street': {
                        'type': ['null', 'string'],
                        'description': 'Shipping street address',
                    },
                    'Shipping_City': {
                        'type': ['null', 'string'],
                        'description': 'Shipping city',
                    },
                    'Shipping_State': {
                        'type': ['null', 'string'],
                        'description': 'Shipping state',
                    },
                    'Shipping_Code': {
                        'type': ['null', 'string'],
                        'description': 'Shipping ZIP/postal code',
                    },
                    'Shipping_Country': {
                        'type': ['null', 'string'],
                        'description': 'Shipping country',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'accounts',
            },
        ),
        EntityDefinition(
            name='deals',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Deals',
                    action=Action.LIST,
                    description='Returns a paginated list of deals',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of deals',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM deal (opportunity) object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique deal identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Deal_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Deal name',
                                        },
                                        'Amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Deal amount',
                                        },
                                        'Stage': {
                                            'type': ['null', 'string'],
                                            'description': 'Deal stage',
                                        },
                                        'Probability': {
                                            'type': ['null', 'integer'],
                                            'description': 'Win probability percentage',
                                        },
                                        'Closing_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Expected closing date',
                                        },
                                        'Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Deal type',
                                        },
                                        'Next_Step': {
                                            'type': ['null', 'string'],
                                            'description': 'Next step',
                                        },
                                        'Lead_Source': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead source',
                                        },
                                        'Contact_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Campaign_Source': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Pipeline': {
                                            'type': ['null', 'object'],
                                            'description': 'Sales pipeline reference',
                                            'properties': {
                                                'name': {'type': 'string'},
                                                'id': {'type': 'string'},
                                            },
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'deals',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Deals/{id}',
                    action=Action.GET,
                    description='Get a single deal by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of deals',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM deal (opportunity) object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique deal identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Deal_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Deal name',
                                        },
                                        'Amount': {
                                            'type': ['null', 'number'],
                                            'description': 'Deal amount',
                                        },
                                        'Stage': {
                                            'type': ['null', 'string'],
                                            'description': 'Deal stage',
                                        },
                                        'Probability': {
                                            'type': ['null', 'integer'],
                                            'description': 'Win probability percentage',
                                        },
                                        'Closing_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Expected closing date',
                                        },
                                        'Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Deal type',
                                        },
                                        'Next_Step': {
                                            'type': ['null', 'string'],
                                            'description': 'Next step',
                                        },
                                        'Lead_Source': {
                                            'type': ['null', 'string'],
                                            'description': 'Lead source',
                                        },
                                        'Contact_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Campaign_Source': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Pipeline': {
                                            'type': ['null', 'object'],
                                            'description': 'Sales pipeline reference',
                                            'properties': {
                                                'name': {'type': 'string'},
                                                'id': {'type': 'string'},
                                            },
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'deals',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM deal (opportunity) object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique deal identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Deal_Name': {
                        'type': ['null', 'string'],
                        'description': 'Deal name',
                    },
                    'Amount': {
                        'type': ['null', 'number'],
                        'description': 'Deal amount',
                    },
                    'Stage': {
                        'type': ['null', 'string'],
                        'description': 'Deal stage',
                    },
                    'Probability': {
                        'type': ['null', 'integer'],
                        'description': 'Win probability percentage',
                    },
                    'Closing_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Expected closing date',
                    },
                    'Type': {
                        'type': ['null', 'string'],
                        'description': 'Deal type',
                    },
                    'Next_Step': {
                        'type': ['null', 'string'],
                        'description': 'Next step',
                    },
                    'Lead_Source': {
                        'type': ['null', 'string'],
                        'description': 'Lead source',
                    },
                    'Contact_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Account_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Campaign_Source': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Pipeline': {
                        'type': ['null', 'object'],
                        'description': 'Sales pipeline reference',
                        'properties': {
                            'name': {'type': 'string'},
                            'id': {'type': 'string'},
                        },
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'deals',
            },
        ),
        EntityDefinition(
            name='campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Campaigns',
                    action=Action.LIST,
                    description='Returns a paginated list of campaigns',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of campaigns',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM campaign object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Campaign_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign name',
                                        },
                                        'Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign type',
                                        },
                                        'Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign status',
                                        },
                                        'Start_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Campaign start date',
                                        },
                                        'End_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Campaign end date',
                                        },
                                        'Expected_Revenue': {
                                            'type': ['null', 'number'],
                                            'description': 'Expected revenue',
                                        },
                                        'Budgeted_Cost': {
                                            'type': ['null', 'number'],
                                            'description': 'Budgeted cost',
                                        },
                                        'Actual_Cost': {
                                            'type': ['null', 'number'],
                                            'description': 'Actual cost',
                                        },
                                        'Num_sent': {
                                            'type': ['null', 'string'],
                                            'description': 'Number of messages sent',
                                        },
                                        'Expected_Response': {
                                            'type': ['null', 'integer'],
                                            'description': 'Expected response count',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'campaigns',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Campaigns/{id}',
                    action=Action.GET,
                    description='Get a single campaign by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of campaigns',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM campaign object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Campaign_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign name',
                                        },
                                        'Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign type',
                                        },
                                        'Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Campaign status',
                                        },
                                        'Start_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Campaign start date',
                                        },
                                        'End_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Campaign end date',
                                        },
                                        'Expected_Revenue': {
                                            'type': ['null', 'number'],
                                            'description': 'Expected revenue',
                                        },
                                        'Budgeted_Cost': {
                                            'type': ['null', 'number'],
                                            'description': 'Budgeted cost',
                                        },
                                        'Actual_Cost': {
                                            'type': ['null', 'number'],
                                            'description': 'Actual cost',
                                        },
                                        'Num_sent': {
                                            'type': ['null', 'string'],
                                            'description': 'Number of messages sent',
                                        },
                                        'Expected_Response': {
                                            'type': ['null', 'integer'],
                                            'description': 'Expected response count',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'campaigns',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM campaign object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique campaign identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Campaign_Name': {
                        'type': ['null', 'string'],
                        'description': 'Campaign name',
                    },
                    'Type': {
                        'type': ['null', 'string'],
                        'description': 'Campaign type',
                    },
                    'Status': {
                        'type': ['null', 'string'],
                        'description': 'Campaign status',
                    },
                    'Start_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Campaign start date',
                    },
                    'End_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Campaign end date',
                    },
                    'Expected_Revenue': {
                        'type': ['null', 'number'],
                        'description': 'Expected revenue',
                    },
                    'Budgeted_Cost': {
                        'type': ['null', 'number'],
                        'description': 'Budgeted cost',
                    },
                    'Actual_Cost': {
                        'type': ['null', 'number'],
                        'description': 'Actual cost',
                    },
                    'Num_sent': {
                        'type': ['null', 'string'],
                        'description': 'Number of messages sent',
                    },
                    'Expected_Response': {
                        'type': ['null', 'integer'],
                        'description': 'Expected response count',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='tasks',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Tasks',
                    action=Action.LIST,
                    description='Returns a paginated list of tasks',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM task object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique task identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Task subject',
                                        },
                                        'Due_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Due date',
                                        },
                                        'Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Task status',
                                        },
                                        'Priority': {
                                            'type': ['null', 'string'],
                                            'description': 'Task priority',
                                        },
                                        'Send_Notification_Email': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to send notification email',
                                        },
                                        'Remind_At': {
                                            'type': ['null', 'object'],
                                            'description': 'Reminder settings',
                                        },
                                        'Who_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'What_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Recurring_Activity': {
                                            'type': ['null', 'object'],
                                            'description': 'Recurring activity settings',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                        'Closed_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Time the task was closed',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Tasks/{id}',
                    action=Action.GET,
                    description='Get a single task by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of tasks',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM task object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique task identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Task subject',
                                        },
                                        'Due_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Due date',
                                        },
                                        'Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Task status',
                                        },
                                        'Priority': {
                                            'type': ['null', 'string'],
                                            'description': 'Task priority',
                                        },
                                        'Send_Notification_Email': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether to send notification email',
                                        },
                                        'Remind_At': {
                                            'type': ['null', 'object'],
                                            'description': 'Reminder settings',
                                        },
                                        'Who_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'What_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Recurring_Activity': {
                                            'type': ['null', 'object'],
                                            'description': 'Recurring activity settings',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                        'Closed_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Time the task was closed',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'tasks',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM task object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique task identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Subject': {
                        'type': ['null', 'string'],
                        'description': 'Task subject',
                    },
                    'Due_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Due date',
                    },
                    'Status': {
                        'type': ['null', 'string'],
                        'description': 'Task status',
                    },
                    'Priority': {
                        'type': ['null', 'string'],
                        'description': 'Task priority',
                    },
                    'Send_Notification_Email': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether to send notification email',
                    },
                    'Remind_At': {
                        'type': ['null', 'object'],
                        'description': 'Reminder settings',
                    },
                    'Who_Id': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'What_Id': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Recurring_Activity': {
                        'type': ['null', 'object'],
                        'description': 'Recurring activity settings',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                    'Closed_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Time the task was closed',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'tasks',
            },
        ),
        EntityDefinition(
            name='events',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Events',
                    action=Action.LIST,
                    description='Returns a paginated list of events (meetings/calendar events)',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of events',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM event (meeting/calendar) object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique event identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Event_Title': {
                                            'type': ['null', 'string'],
                                            'description': 'Event title',
                                        },
                                        'Start_DateTime': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Event start date and time',
                                        },
                                        'End_DateTime': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Event end date and time',
                                        },
                                        'All_day': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is an all-day event',
                                        },
                                        'Location': {
                                            'type': ['null', 'string'],
                                            'description': 'Event location',
                                        },
                                        'Participants': {
                                            'type': ['null', 'array'],
                                            'description': 'List of event participants',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'Email': {'type': 'string'},
                                                    'invited': {'type': 'boolean'},
                                                    'type': {'type': 'string'},
                                                    'participant': {'type': 'string'},
                                                    'status': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'Who_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'What_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Remind_At': {
                                            'type': ['null', 'object'],
                                            'description': 'Reminder settings',
                                        },
                                        'Recurring_Activity': {
                                            'type': ['null', 'object'],
                                            'description': 'Recurring activity settings',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'events',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Events/{id}',
                    action=Action.GET,
                    description='Get a single event by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of events',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM event (meeting/calendar) object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique event identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Event_Title': {
                                            'type': ['null', 'string'],
                                            'description': 'Event title',
                                        },
                                        'Start_DateTime': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Event start date and time',
                                        },
                                        'End_DateTime': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Event end date and time',
                                        },
                                        'All_day': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is an all-day event',
                                        },
                                        'Location': {
                                            'type': ['null', 'string'],
                                            'description': 'Event location',
                                        },
                                        'Participants': {
                                            'type': ['null', 'array'],
                                            'description': 'List of event participants',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'name': {'type': 'string'},
                                                    'Email': {'type': 'string'},
                                                    'invited': {'type': 'boolean'},
                                                    'type': {'type': 'string'},
                                                    'participant': {'type': 'string'},
                                                    'status': {'type': 'string'},
                                                },
                                            },
                                        },
                                        'Who_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'What_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Remind_At': {
                                            'type': ['null', 'object'],
                                            'description': 'Reminder settings',
                                        },
                                        'Recurring_Activity': {
                                            'type': ['null', 'object'],
                                            'description': 'Recurring activity settings',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'events',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM event (meeting/calendar) object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique event identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Event_Title': {
                        'type': ['null', 'string'],
                        'description': 'Event title',
                    },
                    'Start_DateTime': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Event start date and time',
                    },
                    'End_DateTime': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Event end date and time',
                    },
                    'All_day': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is an all-day event',
                    },
                    'Location': {
                        'type': ['null', 'string'],
                        'description': 'Event location',
                    },
                    'Participants': {
                        'type': ['null', 'array'],
                        'description': 'List of event participants',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string'},
                                'Email': {'type': 'string'},
                                'invited': {'type': 'boolean'},
                                'type': {'type': 'string'},
                                'participant': {'type': 'string'},
                                'status': {'type': 'string'},
                            },
                        },
                    },
                    'Who_Id': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'What_Id': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Remind_At': {
                        'type': ['null', 'object'],
                        'description': 'Reminder settings',
                    },
                    'Recurring_Activity': {
                        'type': ['null', 'object'],
                        'description': 'Recurring activity settings',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'events',
            },
        ),
        EntityDefinition(
            name='calls',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Calls',
                    action=Action.LIST,
                    description='Returns a paginated list of calls',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of calls',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM call object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique call identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Call subject',
                                        },
                                        'Call_Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Call type (Inbound/Outbound)',
                                        },
                                        'Call_Start_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Call start time',
                                        },
                                        'Call_Duration': {
                                            'type': ['null', 'string'],
                                            'description': 'Call duration',
                                        },
                                        'Call_Duration_in_seconds': {
                                            'type': ['null', 'number'],
                                            'description': 'Call duration in seconds',
                                        },
                                        'Call_Purpose': {
                                            'type': ['null', 'string'],
                                            'description': 'Call purpose',
                                        },
                                        'Call_Result': {
                                            'type': ['null', 'string'],
                                            'description': 'Call result',
                                        },
                                        'Who_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'What_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Caller_ID': {
                                            'type': ['null', 'string'],
                                            'description': 'Caller ID',
                                        },
                                        'Outgoing_Call_Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Outgoing call status',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'calls',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Calls/{id}',
                    action=Action.GET,
                    description='Get a single call by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of calls',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM call object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique call identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Call subject',
                                        },
                                        'Call_Type': {
                                            'type': ['null', 'string'],
                                            'description': 'Call type (Inbound/Outbound)',
                                        },
                                        'Call_Start_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Call start time',
                                        },
                                        'Call_Duration': {
                                            'type': ['null', 'string'],
                                            'description': 'Call duration',
                                        },
                                        'Call_Duration_in_seconds': {
                                            'type': ['null', 'number'],
                                            'description': 'Call duration in seconds',
                                        },
                                        'Call_Purpose': {
                                            'type': ['null', 'string'],
                                            'description': 'Call purpose',
                                        },
                                        'Call_Result': {
                                            'type': ['null', 'string'],
                                            'description': 'Call result',
                                        },
                                        'Who_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'What_Id': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Caller_ID': {
                                            'type': ['null', 'string'],
                                            'description': 'Caller ID',
                                        },
                                        'Outgoing_Call_Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Outgoing call status',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'calls',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM call object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique call identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Subject': {
                        'type': ['null', 'string'],
                        'description': 'Call subject',
                    },
                    'Call_Type': {
                        'type': ['null', 'string'],
                        'description': 'Call type (Inbound/Outbound)',
                    },
                    'Call_Start_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Call start time',
                    },
                    'Call_Duration': {
                        'type': ['null', 'string'],
                        'description': 'Call duration',
                    },
                    'Call_Duration_in_seconds': {
                        'type': ['null', 'number'],
                        'description': 'Call duration in seconds',
                    },
                    'Call_Purpose': {
                        'type': ['null', 'string'],
                        'description': 'Call purpose',
                    },
                    'Call_Result': {
                        'type': ['null', 'string'],
                        'description': 'Call result',
                    },
                    'Who_Id': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'What_Id': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Caller_ID': {
                        'type': ['null', 'string'],
                        'description': 'Caller ID',
                    },
                    'Outgoing_Call_Status': {
                        'type': ['null', 'string'],
                        'description': 'Outgoing call status',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'calls',
            },
        ),
        EntityDefinition(
            name='products',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Products',
                    action=Action.LIST,
                    description='Returns a paginated list of products',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of products',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM product object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique product identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Product_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Product name',
                                        },
                                        'Product_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Product code',
                                        },
                                        'Product_Category': {
                                            'type': ['null', 'string'],
                                            'description': 'Product category',
                                        },
                                        'Product_Active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the product is active',
                                        },
                                        'Unit_Price': {
                                            'type': ['null', 'number'],
                                            'description': 'Unit price',
                                        },
                                        'Commission_Rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Commission rate',
                                        },
                                        'Manufacturer': {
                                            'type': ['null', 'string'],
                                            'description': 'Manufacturer',
                                        },
                                        'Sales_Start_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Sales start date',
                                        },
                                        'Sales_End_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Sales end date',
                                        },
                                        'Support_Start_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Support start date',
                                        },
                                        'Support_Expiry_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Support expiry date',
                                        },
                                        'Qty_in_Stock': {
                                            'type': ['null', 'number'],
                                            'description': 'Quantity in stock',
                                        },
                                        'Qty_in_Demand': {
                                            'type': ['null', 'number'],
                                            'description': 'Quantity in demand',
                                        },
                                        'Qty_Ordered': {
                                            'type': ['null', 'number'],
                                            'description': 'Quantity ordered',
                                        },
                                        'Reorder_Level': {
                                            'type': ['null', 'number'],
                                            'description': 'Reorder level',
                                        },
                                        'Handler': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Tax': {
                                            'type': ['null', 'array'],
                                            'description': 'Tax list',
                                            'items': {'type': 'string'},
                                        },
                                        'Vendor_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'products',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Products/{id}',
                    action=Action.GET,
                    description='Get a single product by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of products',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM product object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique product identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Product_Name': {
                                            'type': ['null', 'string'],
                                            'description': 'Product name',
                                        },
                                        'Product_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Product code',
                                        },
                                        'Product_Category': {
                                            'type': ['null', 'string'],
                                            'description': 'Product category',
                                        },
                                        'Product_Active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the product is active',
                                        },
                                        'Unit_Price': {
                                            'type': ['null', 'number'],
                                            'description': 'Unit price',
                                        },
                                        'Commission_Rate': {
                                            'type': ['null', 'number'],
                                            'description': 'Commission rate',
                                        },
                                        'Manufacturer': {
                                            'type': ['null', 'string'],
                                            'description': 'Manufacturer',
                                        },
                                        'Sales_Start_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Sales start date',
                                        },
                                        'Sales_End_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Sales end date',
                                        },
                                        'Support_Start_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Support start date',
                                        },
                                        'Support_Expiry_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Support expiry date',
                                        },
                                        'Qty_in_Stock': {
                                            'type': ['null', 'number'],
                                            'description': 'Quantity in stock',
                                        },
                                        'Qty_in_Demand': {
                                            'type': ['null', 'number'],
                                            'description': 'Quantity in demand',
                                        },
                                        'Qty_Ordered': {
                                            'type': ['null', 'number'],
                                            'description': 'Quantity ordered',
                                        },
                                        'Reorder_Level': {
                                            'type': ['null', 'number'],
                                            'description': 'Reorder level',
                                        },
                                        'Handler': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Tax': {
                                            'type': ['null', 'array'],
                                            'description': 'Tax list',
                                            'items': {'type': 'string'},
                                        },
                                        'Vendor_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'products',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM product object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique product identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Product_Name': {
                        'type': ['null', 'string'],
                        'description': 'Product name',
                    },
                    'Product_Code': {
                        'type': ['null', 'string'],
                        'description': 'Product code',
                    },
                    'Product_Category': {
                        'type': ['null', 'string'],
                        'description': 'Product category',
                    },
                    'Product_Active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the product is active',
                    },
                    'Unit_Price': {
                        'type': ['null', 'number'],
                        'description': 'Unit price',
                    },
                    'Commission_Rate': {
                        'type': ['null', 'number'],
                        'description': 'Commission rate',
                    },
                    'Manufacturer': {
                        'type': ['null', 'string'],
                        'description': 'Manufacturer',
                    },
                    'Sales_Start_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Sales start date',
                    },
                    'Sales_End_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Sales end date',
                    },
                    'Support_Start_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Support start date',
                    },
                    'Support_Expiry_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Support expiry date',
                    },
                    'Qty_in_Stock': {
                        'type': ['null', 'number'],
                        'description': 'Quantity in stock',
                    },
                    'Qty_in_Demand': {
                        'type': ['null', 'number'],
                        'description': 'Quantity in demand',
                    },
                    'Qty_Ordered': {
                        'type': ['null', 'number'],
                        'description': 'Quantity ordered',
                    },
                    'Reorder_Level': {
                        'type': ['null', 'number'],
                        'description': 'Reorder level',
                    },
                    'Handler': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Tax': {
                        'type': ['null', 'array'],
                        'description': 'Tax list',
                        'items': {'type': 'string'},
                    },
                    'Vendor_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'products',
            },
        ),
        EntityDefinition(
            name='quotes',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Quotes',
                    action=Action.LIST,
                    description='Returns a paginated list of quotes',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of quotes',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM quote object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique quote identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Quote subject',
                                        },
                                        'Quote_Stage': {
                                            'type': ['null', 'string'],
                                            'description': 'Quote stage',
                                        },
                                        'Valid_Till': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Valid until date',
                                        },
                                        'Deal_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Contact_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Carrier': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping carrier',
                                        },
                                        'Shipping_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping street address',
                                        },
                                        'Shipping_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping city',
                                        },
                                        'Shipping_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping state',
                                        },
                                        'Shipping_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping ZIP/postal code',
                                        },
                                        'Shipping_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping country',
                                        },
                                        'Billing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing street address',
                                        },
                                        'Billing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing city',
                                        },
                                        'Billing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing state',
                                        },
                                        'Billing_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing ZIP/postal code',
                                        },
                                        'Billing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing country',
                                        },
                                        'Sub_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Subtotal amount',
                                        },
                                        'Tax': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax amount',
                                        },
                                        'Adjustment': {
                                            'type': ['null', 'number'],
                                            'description': 'Adjustment amount',
                                        },
                                        'Grand_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Grand total amount',
                                        },
                                        'Discount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount amount',
                                        },
                                        'Terms_and_Conditions': {
                                            'type': ['null', 'string'],
                                            'description': 'Terms and conditions',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'quotes',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Quotes/{id}',
                    action=Action.GET,
                    description='Get a single quote by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of quotes',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM quote object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique quote identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Quote subject',
                                        },
                                        'Quote_Stage': {
                                            'type': ['null', 'string'],
                                            'description': 'Quote stage',
                                        },
                                        'Valid_Till': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Valid until date',
                                        },
                                        'Deal_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Contact_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Carrier': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping carrier',
                                        },
                                        'Shipping_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping street address',
                                        },
                                        'Shipping_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping city',
                                        },
                                        'Shipping_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping state',
                                        },
                                        'Shipping_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping ZIP/postal code',
                                        },
                                        'Shipping_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping country',
                                        },
                                        'Billing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing street address',
                                        },
                                        'Billing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing city',
                                        },
                                        'Billing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing state',
                                        },
                                        'Billing_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing ZIP/postal code',
                                        },
                                        'Billing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing country',
                                        },
                                        'Sub_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Subtotal amount',
                                        },
                                        'Tax': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax amount',
                                        },
                                        'Adjustment': {
                                            'type': ['null', 'number'],
                                            'description': 'Adjustment amount',
                                        },
                                        'Grand_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Grand total amount',
                                        },
                                        'Discount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount amount',
                                        },
                                        'Terms_and_Conditions': {
                                            'type': ['null', 'string'],
                                            'description': 'Terms and conditions',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'quotes',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM quote object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique quote identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Subject': {
                        'type': ['null', 'string'],
                        'description': 'Quote subject',
                    },
                    'Quote_Stage': {
                        'type': ['null', 'string'],
                        'description': 'Quote stage',
                    },
                    'Valid_Till': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Valid until date',
                    },
                    'Deal_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Contact_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Account_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Carrier': {
                        'type': ['null', 'string'],
                        'description': 'Shipping carrier',
                    },
                    'Shipping_Street': {
                        'type': ['null', 'string'],
                        'description': 'Shipping street address',
                    },
                    'Shipping_City': {
                        'type': ['null', 'string'],
                        'description': 'Shipping city',
                    },
                    'Shipping_State': {
                        'type': ['null', 'string'],
                        'description': 'Shipping state',
                    },
                    'Shipping_Code': {
                        'type': ['null', 'string'],
                        'description': 'Shipping ZIP/postal code',
                    },
                    'Shipping_Country': {
                        'type': ['null', 'string'],
                        'description': 'Shipping country',
                    },
                    'Billing_Street': {
                        'type': ['null', 'string'],
                        'description': 'Billing street address',
                    },
                    'Billing_City': {
                        'type': ['null', 'string'],
                        'description': 'Billing city',
                    },
                    'Billing_State': {
                        'type': ['null', 'string'],
                        'description': 'Billing state',
                    },
                    'Billing_Code': {
                        'type': ['null', 'string'],
                        'description': 'Billing ZIP/postal code',
                    },
                    'Billing_Country': {
                        'type': ['null', 'string'],
                        'description': 'Billing country',
                    },
                    'Sub_Total': {
                        'type': ['null', 'number'],
                        'description': 'Subtotal amount',
                    },
                    'Tax': {
                        'type': ['null', 'number'],
                        'description': 'Tax amount',
                    },
                    'Adjustment': {
                        'type': ['null', 'number'],
                        'description': 'Adjustment amount',
                    },
                    'Grand_Total': {
                        'type': ['null', 'number'],
                        'description': 'Grand total amount',
                    },
                    'Discount': {
                        'type': ['null', 'number'],
                        'description': 'Discount amount',
                    },
                    'Terms_and_Conditions': {
                        'type': ['null', 'string'],
                        'description': 'Terms and conditions',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'quotes',
            },
        ),
        EntityDefinition(
            name='invoices',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Invoices',
                    action=Action.LIST,
                    description='Returns a paginated list of invoices',
                    query_params=[
                        'page',
                        'per_page',
                        'page_token',
                        'sort_by',
                        'sort_order',
                    ],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 200,
                        },
                        'page_token': {'type': 'string', 'required': False},
                        'sort_by': {'type': 'string', 'required': False},
                        'sort_order': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of invoices',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM invoice object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique invoice identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice subject',
                                        },
                                        'Invoice_Number': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice number',
                                        },
                                        'Invoice_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Invoice date',
                                        },
                                        'Due_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Due date',
                                        },
                                        'Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice status',
                                        },
                                        'Sales_Order': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Contact_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Deal_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Purchase_Order': {
                                            'type': ['null', 'string'],
                                            'description': 'Purchase order number',
                                        },
                                        'Excise_Duty': {
                                            'type': ['null', 'number'],
                                            'description': 'Excise duty amount',
                                        },
                                        'Billing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing street address',
                                        },
                                        'Billing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing city',
                                        },
                                        'Billing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing state',
                                        },
                                        'Billing_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing ZIP/postal code',
                                        },
                                        'Billing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing country',
                                        },
                                        'Shipping_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping street address',
                                        },
                                        'Shipping_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping city',
                                        },
                                        'Shipping_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping state',
                                        },
                                        'Shipping_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping ZIP/postal code',
                                        },
                                        'Shipping_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping country',
                                        },
                                        'Sub_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Subtotal amount',
                                        },
                                        'Tax': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax amount',
                                        },
                                        'Adjustment': {
                                            'type': ['null', 'number'],
                                            'description': 'Adjustment amount',
                                        },
                                        'Grand_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Grand total amount',
                                        },
                                        'Discount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount amount',
                                        },
                                        'Terms_and_Conditions': {
                                            'type': ['null', 'string'],
                                            'description': 'Terms and conditions',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'invoices',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data',
                    meta_extractor={'pagination': '$.info'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/crm/v2/Invoices/{id}',
                    action=Action.GET,
                    description='Get a single invoice by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of invoices',
                        'properties': {
                            'data': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Zoho CRM invoice object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique invoice identifier'},
                                        'Owner': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Record owner reference',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Owner name'},
                                                        'id': {'type': 'string', 'description': 'Owner ID'},
                                                        'email': {'type': 'string', 'description': 'Owner email address'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Subject': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice subject',
                                        },
                                        'Invoice_Number': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice number',
                                        },
                                        'Invoice_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Invoice date',
                                        },
                                        'Due_Date': {
                                            'type': ['null', 'string'],
                                            'format': 'date',
                                            'description': 'Due date',
                                        },
                                        'Status': {
                                            'type': ['null', 'string'],
                                            'description': 'Invoice status',
                                        },
                                        'Sales_Order': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Contact_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Account_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Deal_Name': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'Lookup reference to another record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'Referenced record name'},
                                                        'id': {'type': 'string', 'description': 'Referenced record ID'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Purchase_Order': {
                                            'type': ['null', 'string'],
                                            'description': 'Purchase order number',
                                        },
                                        'Excise_Duty': {
                                            'type': ['null', 'number'],
                                            'description': 'Excise duty amount',
                                        },
                                        'Billing_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing street address',
                                        },
                                        'Billing_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing city',
                                        },
                                        'Billing_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing state',
                                        },
                                        'Billing_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing ZIP/postal code',
                                        },
                                        'Billing_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Billing country',
                                        },
                                        'Shipping_Street': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping street address',
                                        },
                                        'Shipping_City': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping city',
                                        },
                                        'Shipping_State': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping state',
                                        },
                                        'Shipping_Code': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping ZIP/postal code',
                                        },
                                        'Shipping_Country': {
                                            'type': ['null', 'string'],
                                            'description': 'Shipping country',
                                        },
                                        'Sub_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Subtotal amount',
                                        },
                                        'Tax': {
                                            'type': ['null', 'number'],
                                            'description': 'Tax amount',
                                        },
                                        'Adjustment': {
                                            'type': ['null', 'number'],
                                            'description': 'Adjustment amount',
                                        },
                                        'Grand_Total': {
                                            'type': ['null', 'number'],
                                            'description': 'Grand total amount',
                                        },
                                        'Discount': {
                                            'type': ['null', 'number'],
                                            'description': 'Discount amount',
                                        },
                                        'Terms_and_Conditions': {
                                            'type': ['null', 'string'],
                                            'description': 'Terms and conditions',
                                        },
                                        'Description': {
                                            'type': ['null', 'string'],
                                            'description': 'Description',
                                        },
                                        'Created_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Record creation timestamp',
                                        },
                                        'Modified_Time': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last modification timestamp',
                                        },
                                        'Created_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who created the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Modified_By': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'description': 'User who last modified the record',
                                                    'properties': {
                                                        'name': {'type': 'string', 'description': 'User name'},
                                                        'id': {'type': 'string', 'description': 'User ID'},
                                                        'email': {'type': 'string', 'description': 'User email'},
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                        },
                                        'Record_Status__s': {
                                            'type': ['null', 'string'],
                                            'description': 'Record status',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'invoices',
                                },
                            },
                            'info': {
                                'type': 'object',
                                'description': 'Pagination metadata',
                                'properties': {
                                    'per_page': {'type': 'integer', 'description': 'Records per page'},
                                    'count': {'type': 'integer', 'description': 'Number of records in current page'},
                                    'page': {'type': 'integer', 'description': 'Current page number'},
                                    'more_records': {'type': 'boolean', 'description': 'Whether more records exist'},
                                    'sort_by': {'type': 'string', 'description': 'Field sorted by'},
                                    'sort_order': {'type': 'string', 'description': 'Sort direction'},
                                },
                            },
                        },
                    },
                    record_extractor='$.data[0]',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Zoho CRM invoice object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique invoice identifier'},
                    'Owner': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/Owner'},
                            {'type': 'null'},
                        ],
                    },
                    'Subject': {
                        'type': ['null', 'string'],
                        'description': 'Invoice subject',
                    },
                    'Invoice_Number': {
                        'type': ['null', 'string'],
                        'description': 'Invoice number',
                    },
                    'Invoice_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Invoice date',
                    },
                    'Due_Date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Due date',
                    },
                    'Status': {
                        'type': ['null', 'string'],
                        'description': 'Invoice status',
                    },
                    'Sales_Order': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Contact_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Account_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Deal_Name': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/LookupRef'},
                            {'type': 'null'},
                        ],
                    },
                    'Purchase_Order': {
                        'type': ['null', 'string'],
                        'description': 'Purchase order number',
                    },
                    'Excise_Duty': {
                        'type': ['null', 'number'],
                        'description': 'Excise duty amount',
                    },
                    'Billing_Street': {
                        'type': ['null', 'string'],
                        'description': 'Billing street address',
                    },
                    'Billing_City': {
                        'type': ['null', 'string'],
                        'description': 'Billing city',
                    },
                    'Billing_State': {
                        'type': ['null', 'string'],
                        'description': 'Billing state',
                    },
                    'Billing_Code': {
                        'type': ['null', 'string'],
                        'description': 'Billing ZIP/postal code',
                    },
                    'Billing_Country': {
                        'type': ['null', 'string'],
                        'description': 'Billing country',
                    },
                    'Shipping_Street': {
                        'type': ['null', 'string'],
                        'description': 'Shipping street address',
                    },
                    'Shipping_City': {
                        'type': ['null', 'string'],
                        'description': 'Shipping city',
                    },
                    'Shipping_State': {
                        'type': ['null', 'string'],
                        'description': 'Shipping state',
                    },
                    'Shipping_Code': {
                        'type': ['null', 'string'],
                        'description': 'Shipping ZIP/postal code',
                    },
                    'Shipping_Country': {
                        'type': ['null', 'string'],
                        'description': 'Shipping country',
                    },
                    'Sub_Total': {
                        'type': ['null', 'number'],
                        'description': 'Subtotal amount',
                    },
                    'Tax': {
                        'type': ['null', 'number'],
                        'description': 'Tax amount',
                    },
                    'Adjustment': {
                        'type': ['null', 'number'],
                        'description': 'Adjustment amount',
                    },
                    'Grand_Total': {
                        'type': ['null', 'number'],
                        'description': 'Grand total amount',
                    },
                    'Discount': {
                        'type': ['null', 'number'],
                        'description': 'Discount amount',
                    },
                    'Terms_and_Conditions': {
                        'type': ['null', 'string'],
                        'description': 'Terms and conditions',
                    },
                    'Description': {
                        'type': ['null', 'string'],
                        'description': 'Description',
                    },
                    'Created_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Record creation timestamp',
                    },
                    'Modified_Time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Last modification timestamp',
                    },
                    'Created_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/CreatedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Modified_By': {
                        'oneOf': [
                            {'$ref': '#/components/schemas/ModifiedBy'},
                            {'type': 'null'},
                        ],
                    },
                    'Record_Status__s': {
                        'type': ['null', 'string'],
                        'description': 'Record status',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'invoices',
            },
        ),
    ],
    search_field_paths={
        'leads': [
            'id',
            'First_Name',
            'Last_Name',
            'Full_Name',
            'Email',
            'Phone',
            'Mobile',
            'Company',
            'Title',
            'Lead_Source',
            'Industry',
            'Annual_Revenue',
            'No_of_Employees',
            'Rating',
            'Lead_Status',
            'Website',
            'City',
            'State',
            'Country',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'contacts': [
            'id',
            'First_Name',
            'Last_Name',
            'Full_Name',
            'Email',
            'Phone',
            'Mobile',
            'Title',
            'Department',
            'Lead_Source',
            'Date_of_Birth',
            'Mailing_City',
            'Mailing_State',
            'Mailing_Country',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'accounts': [
            'id',
            'Account_Name',
            'Account_Number',
            'Account_Type',
            'Industry',
            'Annual_Revenue',
            'Employees',
            'Phone',
            'Website',
            'Ownership',
            'Rating',
            'Billing_City',
            'Billing_State',
            'Billing_Country',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'deals': [
            'id',
            'Deal_Name',
            'Amount',
            'Stage',
            'Probability',
            'Closing_Date',
            'Type',
            'Next_Step',
            'Lead_Source',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'campaigns': [
            'id',
            'Campaign_Name',
            'Type',
            'Status',
            'Start_Date',
            'End_Date',
            'Expected_Revenue',
            'Budgeted_Cost',
            'Actual_Cost',
            'Num_sent',
            'Expected_Response',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'tasks': [
            'id',
            'Subject',
            'Due_Date',
            'Status',
            'Priority',
            'Send_Notification_Email',
            'Description',
            'Created_Time',
            'Modified_Time',
            'Closed_Time',
        ],
        'events': [
            'id',
            'Event_Title',
            'Start_DateTime',
            'End_DateTime',
            'All_day',
            'Location',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'calls': [
            'id',
            'Subject',
            'Call_Type',
            'Call_Start_Time',
            'Call_Duration',
            'Call_Duration_in_seconds',
            'Call_Purpose',
            'Call_Result',
            'Caller_ID',
            'Outgoing_Call_Status',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'products': [
            'id',
            'Product_Name',
            'Product_Code',
            'Product_Category',
            'Product_Active',
            'Unit_Price',
            'Commission_Rate',
            'Manufacturer',
            'Sales_Start_Date',
            'Sales_End_Date',
            'Qty_in_Stock',
            'Qty_in_Demand',
            'Qty_Ordered',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'quotes': [
            'id',
            'Subject',
            'Quote_Stage',
            'Valid_Till',
            'Carrier',
            'Sub_Total',
            'Tax',
            'Adjustment',
            'Grand_Total',
            'Discount',
            'Terms_and_Conditions',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
        'invoices': [
            'id',
            'Subject',
            'Invoice_Number',
            'Invoice_Date',
            'Due_Date',
            'Status',
            'Purchase_Order',
            'Sub_Total',
            'Tax',
            'Adjustment',
            'Grand_Total',
            'Discount',
            'Excise_Duty',
            'Terms_and_Conditions',
            'Description',
            'Created_Time',
            'Modified_Time',
        ],
    },
    server_variable_defaults={'dc_region': 'com'},
)