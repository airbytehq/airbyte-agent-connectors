"""
Salesforce connector.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping, TypeVar, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import SalesforceConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AccountsApiSearchParams,
    AccountsCreateParams,
    AccountsDeleteParams,
    AccountsGetParams,
    AccountsListParams,
    AccountsUpdateParams,
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    AttachmentsListParams,
    CampaignsApiSearchParams,
    CampaignsCreateParams,
    CampaignsDeleteParams,
    CampaignsGetParams,
    CampaignsListParams,
    CampaignsUpdateParams,
    CasesApiSearchParams,
    CasesCreateParams,
    CasesDeleteParams,
    CasesGetParams,
    CasesListParams,
    CasesUpdateParams,
    ContactsApiSearchParams,
    ContactsCreateParams,
    ContactsDeleteParams,
    ContactsGetParams,
    ContactsListParams,
    ContactsUpdateParams,
    ContentVersionsDownloadParams,
    ContentVersionsGetParams,
    ContentVersionsListParams,
    EventsApiSearchParams,
    EventsCreateParams,
    EventsDeleteParams,
    EventsGetParams,
    EventsListParams,
    EventsUpdateParams,
    LeadsApiSearchParams,
    LeadsCreateParams,
    LeadsDeleteParams,
    LeadsGetParams,
    LeadsListParams,
    LeadsUpdateParams,
    NotesApiSearchParams,
    NotesCreateParams,
    NotesDeleteParams,
    NotesGetParams,
    NotesListParams,
    NotesUpdateParams,
    OpportunitiesApiSearchParams,
    OpportunitiesCreateParams,
    OpportunitiesDeleteParams,
    OpportunitiesGetParams,
    OpportunitiesListParams,
    OpportunitiesUpdateParams,
    OpportunityStagesGetParams,
    OpportunityStagesListParams,
    QueryListParams,
    ReportsGetParams,
    ReportsListParams,
    SobjectsCreateParams,
    SobjectsDeleteParams,
    SobjectsGetParams,
    SobjectsListParams,
    SobjectsUpdateParams,
    TasksApiSearchParams,
    TasksCreateParams,
    TasksDeleteParams,
    TasksGetParams,
    TasksListParams,
    TasksUpdateParams,
    UsersCreateParams,
    UsersGetParams,
    UsersListParams,
    UsersUpdateParams,
    AirbyteSearchParams,
    AccountsSearchFilter,
    AccountsSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    LeadsSearchFilter,
    LeadsSearchQuery,
    OpportunitiesSearchFilter,
    OpportunitiesSearchQuery,
    TasksSearchFilter,
    TasksSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    OpportunityStagesSearchFilter,
    OpportunityStagesSearchQuery,
)
from .models import SalesforceAuthConfig

# Import response models and envelope models at runtime
from .models import (
    SalesforceCheckResult,
    SalesforceExecuteResult,
    SalesforceExecuteResultWithMeta,
    SobjectsListResult,
    AccountsListResult,
    AccountsApiSearchResult,
    ContactsListResult,
    ContactsApiSearchResult,
    LeadsListResult,
    LeadsApiSearchResult,
    OpportunitiesListResult,
    OpportunitiesApiSearchResult,
    TasksListResult,
    TasksApiSearchResult,
    EventsListResult,
    EventsApiSearchResult,
    CampaignsListResult,
    CampaignsApiSearchResult,
    CasesListResult,
    CasesApiSearchResult,
    NotesListResult,
    NotesApiSearchResult,
    ContentVersionsListResult,
    AttachmentsListResult,
    ReportsListResult,
    UsersListResult,
    OpportunityStagesListResult,
    QueryListResult,
    Account,
    Attachment,
    Campaign,
    Case,
    Contact,
    ContentVersion,
    Event,
    Lead,
    Note,
    Opportunity,
    OpportunityStage,
    Report,
    ReportResults,
    SObject,
    SObjectCreateResponse,
    SearchResult,
    Task,
    User,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    LeadsSearchData,
    LeadsSearchResult,
    OpportunitiesSearchData,
    OpportunitiesSearchResult,
    TasksSearchData,
    TasksSearchResult,
    UsersSearchData,
    UsersSearchResult,
    OpportunityStagesSearchData,
    OpportunityStagesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class SalesforceConnector:
    """
    Type-safe Salesforce API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "salesforce"
    connector_version = "1.2.0"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("sobjects", "list"): True,
        ("sobjects", "create"): None,
        ("sobjects", "get"): None,
        ("sobjects", "update"): None,
        ("sobjects", "delete"): None,
        ("accounts", "list"): True,
        ("accounts", "create"): None,
        ("accounts", "get"): None,
        ("accounts", "update"): None,
        ("accounts", "delete"): None,
        ("accounts", "api_search"): True,
        ("contacts", "list"): True,
        ("contacts", "create"): None,
        ("contacts", "get"): None,
        ("contacts", "update"): None,
        ("contacts", "delete"): None,
        ("contacts", "api_search"): True,
        ("leads", "list"): True,
        ("leads", "create"): None,
        ("leads", "get"): None,
        ("leads", "update"): None,
        ("leads", "delete"): None,
        ("leads", "api_search"): True,
        ("opportunities", "list"): True,
        ("opportunities", "create"): None,
        ("opportunities", "get"): None,
        ("opportunities", "update"): None,
        ("opportunities", "delete"): None,
        ("opportunities", "api_search"): True,
        ("tasks", "list"): True,
        ("tasks", "create"): None,
        ("tasks", "get"): None,
        ("tasks", "update"): None,
        ("tasks", "delete"): None,
        ("tasks", "api_search"): True,
        ("events", "list"): True,
        ("events", "create"): None,
        ("events", "get"): None,
        ("events", "update"): None,
        ("events", "delete"): None,
        ("events", "api_search"): True,
        ("campaigns", "list"): True,
        ("campaigns", "create"): None,
        ("campaigns", "get"): None,
        ("campaigns", "update"): None,
        ("campaigns", "delete"): None,
        ("campaigns", "api_search"): True,
        ("cases", "list"): True,
        ("cases", "create"): None,
        ("cases", "get"): None,
        ("cases", "update"): None,
        ("cases", "delete"): None,
        ("cases", "api_search"): True,
        ("notes", "list"): True,
        ("notes", "create"): None,
        ("notes", "get"): None,
        ("notes", "update"): None,
        ("notes", "delete"): None,
        ("notes", "api_search"): True,
        ("content_versions", "list"): True,
        ("content_versions", "get"): None,
        ("content_versions", "download"): None,
        ("attachments", "list"): True,
        ("attachments", "get"): None,
        ("attachments", "download"): None,
        ("reports", "list"): True,
        ("reports", "get"): None,
        ("users", "list"): True,
        ("users", "create"): None,
        ("users", "get"): None,
        ("users", "update"): None,
        ("opportunity_stages", "list"): True,
        ("opportunity_stages", "get"): None,
        ("query", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('sobjects', 'create'): {'sobject_type': 'sobjectType'},
        ('sobjects', 'get'): {'sobject_type': 'sobjectType', 'id': 'id', 'fields': 'fields'},
        ('sobjects', 'update'): {'sobject_type': 'sobjectType', 'id': 'id'},
        ('sobjects', 'delete'): {'sobject_type': 'sobjectType', 'id': 'id'},
        ('accounts', 'list'): {'q': 'q'},
        ('accounts', 'create'): {'name': 'Name', 'account_number': 'AccountNumber', 'type': 'Type', 'industry': 'Industry', 'phone': 'Phone', 'website': 'Website', 'billing_street': 'BillingStreet', 'billing_city': 'BillingCity', 'billing_state': 'BillingState', 'billing_postal_code': 'BillingPostalCode', 'billing_country': 'BillingCountry', 'annual_revenue': 'AnnualRevenue', 'number_of_employees': 'NumberOfEmployees', 'description': 'Description', 'owner_id': 'OwnerId', 'parent_id': 'ParentId'},
        ('accounts', 'get'): {'id': 'id', 'fields': 'fields'},
        ('accounts', 'update'): {'name': 'Name', 'account_number': 'AccountNumber', 'type': 'Type', 'industry': 'Industry', 'phone': 'Phone', 'website': 'Website', 'billing_street': 'BillingStreet', 'billing_city': 'BillingCity', 'billing_state': 'BillingState', 'billing_postal_code': 'BillingPostalCode', 'billing_country': 'BillingCountry', 'annual_revenue': 'AnnualRevenue', 'number_of_employees': 'NumberOfEmployees', 'description': 'Description', 'owner_id': 'OwnerId', 'parent_id': 'ParentId', 'id': 'id'},
        ('accounts', 'delete'): {'id': 'id'},
        ('accounts', 'api_search'): {'q': 'q'},
        ('contacts', 'list'): {'q': 'q'},
        ('contacts', 'create'): {'first_name': 'FirstName', 'last_name': 'LastName', 'email': 'Email', 'phone': 'Phone', 'mobile_phone': 'MobilePhone', 'title': 'Title', 'department': 'Department', 'account_id': 'AccountId', 'mailing_street': 'MailingStreet', 'mailing_city': 'MailingCity', 'mailing_state': 'MailingState', 'mailing_postal_code': 'MailingPostalCode', 'mailing_country': 'MailingCountry', 'description': 'Description', 'owner_id': 'OwnerId'},
        ('contacts', 'get'): {'id': 'id', 'fields': 'fields'},
        ('contacts', 'update'): {'first_name': 'FirstName', 'last_name': 'LastName', 'email': 'Email', 'phone': 'Phone', 'mobile_phone': 'MobilePhone', 'title': 'Title', 'department': 'Department', 'account_id': 'AccountId', 'mailing_street': 'MailingStreet', 'mailing_city': 'MailingCity', 'mailing_state': 'MailingState', 'mailing_postal_code': 'MailingPostalCode', 'mailing_country': 'MailingCountry', 'description': 'Description', 'owner_id': 'OwnerId', 'id': 'id'},
        ('contacts', 'delete'): {'id': 'id'},
        ('contacts', 'api_search'): {'q': 'q'},
        ('leads', 'list'): {'q': 'q'},
        ('leads', 'create'): {'first_name': 'FirstName', 'last_name': 'LastName', 'company': 'Company', 'title': 'Title', 'email': 'Email', 'phone': 'Phone', 'mobile_phone': 'MobilePhone', 'website': 'Website', 'status': 'Status', 'lead_source': 'LeadSource', 'industry': 'Industry', 'rating': 'Rating', 'annual_revenue': 'AnnualRevenue', 'number_of_employees': 'NumberOfEmployees', 'street': 'Street', 'city': 'City', 'state': 'State', 'postal_code': 'PostalCode', 'country': 'Country', 'description': 'Description', 'owner_id': 'OwnerId'},
        ('leads', 'get'): {'id': 'id', 'fields': 'fields'},
        ('leads', 'update'): {'first_name': 'FirstName', 'last_name': 'LastName', 'company': 'Company', 'title': 'Title', 'email': 'Email', 'phone': 'Phone', 'mobile_phone': 'MobilePhone', 'website': 'Website', 'status': 'Status', 'lead_source': 'LeadSource', 'industry': 'Industry', 'rating': 'Rating', 'annual_revenue': 'AnnualRevenue', 'number_of_employees': 'NumberOfEmployees', 'street': 'Street', 'city': 'City', 'state': 'State', 'postal_code': 'PostalCode', 'country': 'Country', 'description': 'Description', 'owner_id': 'OwnerId', 'id': 'id'},
        ('leads', 'delete'): {'id': 'id'},
        ('leads', 'api_search'): {'q': 'q'},
        ('opportunities', 'list'): {'q': 'q'},
        ('opportunities', 'create'): {'name': 'Name', 'account_id': 'AccountId', 'stage_name': 'StageName', 'close_date': 'CloseDate', 'amount': 'Amount', 'probability': 'Probability', 'type': 'Type', 'lead_source': 'LeadSource', 'next_step': 'NextStep', 'campaign_id': 'CampaignId', 'forecast_category_name': 'ForecastCategoryName', 'description': 'Description', 'owner_id': 'OwnerId'},
        ('opportunities', 'get'): {'id': 'id', 'fields': 'fields'},
        ('opportunities', 'update'): {'name': 'Name', 'account_id': 'AccountId', 'stage_name': 'StageName', 'close_date': 'CloseDate', 'amount': 'Amount', 'probability': 'Probability', 'type': 'Type', 'lead_source': 'LeadSource', 'next_step': 'NextStep', 'campaign_id': 'CampaignId', 'forecast_category_name': 'ForecastCategoryName', 'description': 'Description', 'owner_id': 'OwnerId', 'id': 'id'},
        ('opportunities', 'delete'): {'id': 'id'},
        ('opportunities', 'api_search'): {'q': 'q'},
        ('tasks', 'list'): {'q': 'q'},
        ('tasks', 'create'): {'subject': 'Subject', 'status': 'Status', 'priority': 'Priority', 'activity_date': 'ActivityDate', 'who_id': 'WhoId', 'what_id': 'WhatId', 'description': 'Description', 'type': 'Type', 'is_reminder_set': 'IsReminderSet', 'reminder_date_time': 'ReminderDateTime', 'owner_id': 'OwnerId'},
        ('tasks', 'get'): {'id': 'id', 'fields': 'fields'},
        ('tasks', 'update'): {'subject': 'Subject', 'status': 'Status', 'priority': 'Priority', 'activity_date': 'ActivityDate', 'who_id': 'WhoId', 'what_id': 'WhatId', 'description': 'Description', 'type': 'Type', 'is_reminder_set': 'IsReminderSet', 'reminder_date_time': 'ReminderDateTime', 'owner_id': 'OwnerId', 'id': 'id'},
        ('tasks', 'delete'): {'id': 'id'},
        ('tasks', 'api_search'): {'q': 'q'},
        ('events', 'list'): {'q': 'q'},
        ('events', 'create'): {'subject': 'Subject', 'start_date_time': 'StartDateTime', 'end_date_time': 'EndDateTime', 'duration_in_minutes': 'DurationInMinutes', 'location': 'Location', 'description': 'Description', 'who_id': 'WhoId', 'what_id': 'WhatId', 'is_all_day_event': 'IsAllDayEvent', 'show_as': 'ShowAs', 'owner_id': 'OwnerId'},
        ('events', 'get'): {'id': 'id', 'fields': 'fields'},
        ('events', 'update'): {'subject': 'Subject', 'start_date_time': 'StartDateTime', 'end_date_time': 'EndDateTime', 'duration_in_minutes': 'DurationInMinutes', 'location': 'Location', 'description': 'Description', 'who_id': 'WhoId', 'what_id': 'WhatId', 'is_all_day_event': 'IsAllDayEvent', 'show_as': 'ShowAs', 'owner_id': 'OwnerId', 'id': 'id'},
        ('events', 'delete'): {'id': 'id'},
        ('events', 'api_search'): {'q': 'q'},
        ('campaigns', 'list'): {'q': 'q'},
        ('campaigns', 'create'): {'name': 'Name', 'type': 'Type', 'status': 'Status', 'start_date': 'StartDate', 'end_date': 'EndDate', 'is_active': 'IsActive', 'description': 'Description', 'expected_revenue': 'ExpectedRevenue', 'budgeted_cost': 'BudgetedCost', 'actual_cost': 'ActualCost', 'expected_response': 'ExpectedResponse', 'number_sent': 'NumberSent', 'parent_id': 'ParentId', 'owner_id': 'OwnerId'},
        ('campaigns', 'get'): {'id': 'id', 'fields': 'fields'},
        ('campaigns', 'update'): {'name': 'Name', 'type': 'Type', 'status': 'Status', 'start_date': 'StartDate', 'end_date': 'EndDate', 'is_active': 'IsActive', 'description': 'Description', 'expected_revenue': 'ExpectedRevenue', 'budgeted_cost': 'BudgetedCost', 'actual_cost': 'ActualCost', 'expected_response': 'ExpectedResponse', 'number_sent': 'NumberSent', 'parent_id': 'ParentId', 'owner_id': 'OwnerId', 'id': 'id'},
        ('campaigns', 'delete'): {'id': 'id'},
        ('campaigns', 'api_search'): {'q': 'q'},
        ('cases', 'list'): {'q': 'q'},
        ('cases', 'create'): {'subject': 'Subject', 'status': 'Status', 'priority': 'Priority', 'origin': 'Origin', 'type': 'Type', 'reason': 'Reason', 'description': 'Description', 'account_id': 'AccountId', 'contact_id': 'ContactId', 'supplied_name': 'SuppliedName', 'supplied_email': 'SuppliedEmail', 'supplied_phone': 'SuppliedPhone', 'supplied_company': 'SuppliedCompany', 'owner_id': 'OwnerId', 'parent_id': 'ParentId'},
        ('cases', 'get'): {'id': 'id', 'fields': 'fields'},
        ('cases', 'update'): {'subject': 'Subject', 'status': 'Status', 'priority': 'Priority', 'origin': 'Origin', 'type': 'Type', 'reason': 'Reason', 'description': 'Description', 'account_id': 'AccountId', 'contact_id': 'ContactId', 'supplied_name': 'SuppliedName', 'supplied_email': 'SuppliedEmail', 'supplied_phone': 'SuppliedPhone', 'supplied_company': 'SuppliedCompany', 'owner_id': 'OwnerId', 'parent_id': 'ParentId', 'id': 'id'},
        ('cases', 'delete'): {'id': 'id'},
        ('cases', 'api_search'): {'q': 'q'},
        ('notes', 'list'): {'q': 'q'},
        ('notes', 'create'): {'title': 'Title', 'body': 'Body', 'parent_id': 'ParentId', 'is_private': 'IsPrivate', 'owner_id': 'OwnerId'},
        ('notes', 'get'): {'id': 'id', 'fields': 'fields'},
        ('notes', 'update'): {'title': 'Title', 'body': 'Body', 'is_private': 'IsPrivate', 'owner_id': 'OwnerId', 'id': 'id'},
        ('notes', 'delete'): {'id': 'id'},
        ('notes', 'api_search'): {'q': 'q'},
        ('content_versions', 'list'): {'q': 'q'},
        ('content_versions', 'get'): {'id': 'id', 'fields': 'fields'},
        ('content_versions', 'download'): {'id': 'id', 'range_header': 'range_header'},
        ('attachments', 'list'): {'q': 'q'},
        ('attachments', 'get'): {'id': 'id', 'fields': 'fields'},
        ('attachments', 'download'): {'id': 'id', 'range_header': 'range_header'},
        ('reports', 'get'): {'id': 'id', 'include_details': 'includeDetails'},
        ('users', 'list'): {'q': 'q'},
        ('users', 'create'): {'username': 'Username', 'first_name': 'FirstName', 'last_name': 'LastName', 'email': 'Email', 'alias': 'Alias', 'profile_id': 'ProfileId', 'user_role_id': 'UserRoleId', 'manager_id': 'ManagerId', 'time_zone_sid_key': 'TimeZoneSidKey', 'locale_sid_key': 'LocaleSidKey', 'email_encoding_key': 'EmailEncodingKey', 'language_locale_key': 'LanguageLocaleKey', 'is_active': 'IsActive', 'title': 'Title', 'department': 'Department', 'phone': 'Phone', 'mobile_phone': 'MobilePhone'},
        ('users', 'get'): {'id': 'id', 'fields': 'fields'},
        ('users', 'update'): {'username': 'Username', 'first_name': 'FirstName', 'last_name': 'LastName', 'email': 'Email', 'alias': 'Alias', 'profile_id': 'ProfileId', 'user_role_id': 'UserRoleId', 'manager_id': 'ManagerId', 'time_zone_sid_key': 'TimeZoneSidKey', 'locale_sid_key': 'LocaleSidKey', 'email_encoding_key': 'EmailEncodingKey', 'language_locale_key': 'LanguageLocaleKey', 'is_active': 'IsActive', 'title': 'Title', 'department': 'Department', 'phone': 'Phone', 'mobile_phone': 'MobilePhone', 'id': 'id'},
        ('opportunity_stages', 'list'): {'q': 'q'},
        ('opportunity_stages', 'get'): {'id': 'id', 'fields': 'fields'},
        ('query', 'list'): {'q': 'q'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (SalesforceAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: SalesforceAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        instance_url: str | None = None    ):
        """
        Initialize a new salesforce connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., SalesforceAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            instance_url: Your Salesforce instance URL (e.g., https://na1.salesforce.com)
        Examples:
            # Local mode (direct API calls)
            connector = SalesforceConnector(auth_config=SalesforceAuthConfig(refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = SalesforceConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = SalesforceConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(SalesforceConnectorModel.id),
                model=SalesforceConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or SalesforceAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if instance_url:
                config_values["instance_url"] = instance_url

            self._executor = LocalExecutor(
                model=SalesforceConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if instance_url:
                base_url = base_url.replace("{instance_url}", instance_url)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.sobjects = SobjectsQuery(self)
        self.accounts = AccountsQuery(self)
        self.contacts = ContactsQuery(self)
        self.leads = LeadsQuery(self)
        self.opportunities = OpportunitiesQuery(self)
        self.tasks = TasksQuery(self)
        self.events = EventsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.cases = CasesQuery(self)
        self.notes = NotesQuery(self)
        self.content_versions = ContentVersionsQuery(self)
        self.attachments = AttachmentsQuery(self)
        self.reports = ReportsQuery(self)
        self.users = UsersQuery(self)
        self.opportunity_stages = OpportunityStagesQuery(self)
        self.query = QueryQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["sobjects"],
        action: Literal["list"],
        params: "SobjectsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SobjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sobjects"],
        action: Literal["create"],
        params: "SobjectsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["sobjects"],
        action: Literal["get"],
        params: "SobjectsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["sobjects"],
        action: Literal["update"],
        params: "SobjectsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["sobjects"],
        action: Literal["delete"],
        params: "SobjectsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["list"],
        params: "AccountsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["create"],
        params: "AccountsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["update"],
        params: "AccountsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["delete"],
        params: "AccountsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["api_search"],
        params: "AccountsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AccountsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["list"],
        params: "ContactsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ContactsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["create"],
        params: "ContactsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["get"],
        params: "ContactsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Contact": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["update"],
        params: "ContactsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["delete"],
        params: "ContactsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["api_search"],
        params: "ContactsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ContactsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["list"],
        params: "LeadsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "LeadsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["create"],
        params: "LeadsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["get"],
        params: "LeadsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Lead": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["update"],
        params: "LeadsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["delete"],
        params: "LeadsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["api_search"],
        params: "LeadsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "LeadsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["list"],
        params: "OpportunitiesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OpportunitiesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["create"],
        params: "OpportunitiesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["get"],
        params: "OpportunitiesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Opportunity": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["update"],
        params: "OpportunitiesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["delete"],
        params: "OpportunitiesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["api_search"],
        params: "OpportunitiesApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OpportunitiesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["list"],
        params: "TasksListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TasksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["create"],
        params: "TasksCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["get"],
        params: "TasksGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Task": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["update"],
        params: "TasksUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["delete"],
        params: "TasksDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["api_search"],
        params: "TasksApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TasksApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["list"],
        params: "EventsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "EventsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["create"],
        params: "EventsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["get"],
        params: "EventsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Event": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["update"],
        params: "EventsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["delete"],
        params: "EventsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["api_search"],
        params: "EventsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "EventsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["create"],
        params: "CampaignsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["update"],
        params: "CampaignsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["delete"],
        params: "CampaignsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["api_search"],
        params: "CampaignsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CampaignsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["list"],
        params: "CasesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CasesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["create"],
        params: "CasesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["get"],
        params: "CasesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Case": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["update"],
        params: "CasesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["delete"],
        params: "CasesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["api_search"],
        params: "CasesApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CasesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["list"],
        params: "NotesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "NotesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["create"],
        params: "NotesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["get"],
        params: "NotesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Note": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["update"],
        params: "NotesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["delete"],
        params: "NotesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["api_search"],
        params: "NotesApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "NotesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["list"],
        params: "ContentVersionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ContentVersionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["get"],
        params: "ContentVersionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ContentVersion": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["download"],
        params: "ContentVersionsDownloadParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["list"],
        params: "AttachmentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AttachmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["get"],
        params: "AttachmentsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Attachment": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["download"],
        params: "AttachmentsDownloadParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["reports"],
        action: Literal["list"],
        params: "ReportsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ReportsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["reports"],
        action: Literal["get"],
        params: "ReportsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ReportResults": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["create"],
        params: "UsersCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SObjectCreateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["update"],
        params: "UsersUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunity_stages"],
        action: Literal["list"],
        params: "OpportunityStagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OpportunityStagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunity_stages"],
        action: Literal["get"],
        params: "OpportunityStagesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OpportunityStage": ...

    @overload
    async def execute(
        self,
        entity: Literal["query"],
        action: Literal["list"],
        params: "QueryListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "QueryListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "delete", "api_search", "download", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> SalesforceExecuteResult[Any] | SalesforceExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "delete", "api_search", "download", "context_store_search"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

        # Remap parameter names from snake_case (TypedDict keys) to API parameter names
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return SalesforceExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SalesforceExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SalesforceCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SalesforceCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SalesforceCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SalesforceCheckResult(
                status="unhealthy",
                error=result.error or "Unknown error during health check",
            )

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def tool_utils(
        cls,
        func: _F | None = None,
        *,
        update_docstring: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = SalesforceConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @SalesforceConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @SalesforceConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @SalesforceConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    SalesforceConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

            if update_docstring:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate

    def list_entities(self) -> list[dict[str, Any]]:
        """
        Get structured data about available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.list_entities()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(SalesforceConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """
        Get the JSON schema for an entity.

        Args:
            entity: Entity name (e.g., "contacts", "companies")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.

        Example:
            schema = connector.entity_schema("contacts")
            if schema:
                print(f"Contact properties: {list(schema.get('properties', {}).keys())}")
        """
        entity_def = next(
            (e for e in SalesforceConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SalesforceConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



class SobjectsQuery:
    """
    Query class for Sobjects entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SobjectsListResult:
        """
        Returns a list of all available Salesforce objects (sObjects) in the organization.
This endpoint is used for health checks to verify authentication and connectivity.


        Returns:
            SobjectsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sobjects", "list", params)
        # Cast generic envelope to concrete typed result
        return SobjectsListResult(
            data=result.data
        )



    async def create(
        self,
        sobject_type: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a record for any Salesforce SObject by name. Works for standard
objects (Account, Contact, ...) and custom objects (e.g. `MyObject__c`).
Pass the SObject's API name in the `sobjectType` path parameter and the
field values as a free-form JSON body.


        Args:
            sobject_type: SObject API name (e.g., `Account`, `MyCustomObject__c`).
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "sobjectType": sobject_type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sobjects", "create", params)
        return result



    async def get(
        self,
        sobject_type: str,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Fetch a single record from any SObject by id. Works for standard and
custom objects.


        Args:
            sobject_type: SObject API name.
            id: Salesforce record Id.
            fields: Comma-separated field names to return. Omit for default fields.
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "sobjectType": sobject_type,
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sobjects", "get", params)
        return result



    async def update(
        self,
        sobject_type: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update fields on an existing record. Pass only the fields you want to
change in the JSON body; Salesforce leaves the rest untouched.


        Args:
            sobject_type: SObject API name.
            id: Salesforce record Id.
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "sobjectType": sobject_type,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sobjects", "update", params)
        return result



    async def delete(
        self,
        sobject_type: str,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a record by id. Salesforce moves the record to the Recycle Bin
(15-day retention) for most objects.


        Args:
            sobject_type: SObject API name.
            id: Salesforce record Id.
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "sobjectType": sobject_type,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sobjects", "delete", params)
        return result



class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> AccountsListResult:
        """
        Returns a list of accounts via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
For "top", "largest", or "highest-value" account requests, rank by a financial account value field
such as ARR, annual recurring revenue, revenue, annual revenue, amount, or value. ARR is often a
Salesforce custom field, so prefer the customer's org-specific ARR or account value field when
available. If no better org-specific field is visible, `AnnualRevenue` is the standard Account
fallback. Do not use `NumberOfEmployees` unless the user asks for employee count, headcount,
company size, or largest employer.


        Args:
            q: SOQL query for accounts. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Account ORDER BY LastModifiedDate DESC LIMIT 50
  SELECT Id, Name, Owner.Name, Owner.Email FROM Account LIMIT 50
  SELECT Id, Name, Parent.Name, Owner.Name FROM Account WHERE Industry = 'Technology' LIMIT 50
  SELECT Id, Name, AnnualRevenue FROM Account ORDER BY AnnualRevenue DESC LIMIT 10
  SELECT Id, Name, NumberOfEmployees FROM Account ORDER BY NumberOfEmployees DESC LIMIT 10

Use dot-path traversal (Owner.Name, Parent.Name) to resolve relationship
fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        name: str,
        account_number: str | None = None,
        type: str | None = None,
        industry: str | None = None,
        phone: str | None = None,
        website: str | None = None,
        billing_street: str | None = None,
        billing_city: str | None = None,
        billing_state: str | None = None,
        billing_postal_code: str | None = None,
        billing_country: str | None = None,
        annual_revenue: float | None = None,
        number_of_employees: int | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        parent_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create an account

        Args:
            name: Account name.
            account_number: Parameter AccountNumber
            type: Parameter Type
            industry: Parameter Industry
            phone: Parameter Phone
            website: Parameter Website
            billing_street: Parameter BillingStreet
            billing_city: Parameter BillingCity
            billing_state: Parameter BillingState
            billing_postal_code: Parameter BillingPostalCode
            billing_country: Parameter BillingCountry
            annual_revenue: Parameter AnnualRevenue
            number_of_employees: Parameter NumberOfEmployees
            description: Parameter Description
            owner_id: Parameter OwnerId
            parent_id: Parameter ParentId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Name": name,
            "AccountNumber": account_number,
            "Type": type,
            "Industry": industry,
            "Phone": phone,
            "Website": website,
            "BillingStreet": billing_street,
            "BillingCity": billing_city,
            "BillingState": billing_state,
            "BillingPostalCode": billing_postal_code,
            "BillingCountry": billing_country,
            "AnnualRevenue": annual_revenue,
            "NumberOfEmployees": number_of_employees,
            "Description": description,
            "OwnerId": owner_id,
            "ParentId": parent_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Account:
        """
        Get a single account by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Account ID (18-character ID starting with '001')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Industry,AnnualRevenue,Website"

            **kwargs: Additional parameters

        Returns:
            Account
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def update(
        self,
        name: str,
        account_number: str | None = None,
        type: str | None = None,
        industry: str | None = None,
        phone: str | None = None,
        website: str | None = None,
        billing_street: str | None = None,
        billing_city: str | None = None,
        billing_state: str | None = None,
        billing_postal_code: str | None = None,
        billing_country: str | None = None,
        annual_revenue: float | None = None,
        number_of_employees: int | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        parent_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update an account

        Args:
            name: Account name.
            account_number: Parameter AccountNumber
            type: Parameter Type
            industry: Parameter Industry
            phone: Parameter Phone
            website: Parameter Website
            billing_street: Parameter BillingStreet
            billing_city: Parameter BillingCity
            billing_state: Parameter BillingState
            billing_postal_code: Parameter BillingPostalCode
            billing_country: Parameter BillingCountry
            annual_revenue: Parameter AnnualRevenue
            number_of_employees: Parameter NumberOfEmployees
            description: Parameter Description
            owner_id: Parameter OwnerId
            parent_id: Parameter ParentId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Name": name,
            "AccountNumber": account_number,
            "Type": type,
            "Industry": industry,
            "Phone": phone,
            "Website": website,
            "BillingStreet": billing_street,
            "BillingCity": billing_city,
            "BillingState": billing_state,
            "BillingPostalCode": billing_postal_code,
            "BillingCountry": billing_country,
            "AnnualRevenue": annual_revenue,
            "NumberOfEmployees": number_of_employees,
            "Description": description,
            "OwnerId": owner_id,
            "ParentId": parent_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete an account

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> AccountsApiSearchResult:
        """
        Search for accounts using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields and objects.
Use SOQL (list action) for structured queries with specific field conditions.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} IN scope RETURNING Object(fields) [LIMIT n]
Examples:
- "FIND {Acme} IN ALL FIELDS RETURNING Account(Id,Name)"
- "FIND {tech*} IN NAME FIELDS RETURNING Account(Id,Name,Industry) LIMIT 50"
- "FIND {\"exact phrase\"} RETURNING Account(Id,Name,Website)"

            **kwargs: Additional parameters

        Returns:
            AccountsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "api_search", params)
        # Cast generic envelope to concrete typed result
        return AccountsApiSearchResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: AccountsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AccountsSearchResult:
        """
        Search accounts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AccountsSearchFilter):
        - id: Unique identifier for the account record
        - name: Name of the account or company
        - account_source: Source of the account record (e.g., Web, Referral)
        - billing_address: Complete billing address as a compound field
        - billing_city: City portion of the billing address
        - billing_country: Country portion of the billing address
        - billing_postal_code: Postal code portion of the billing address
        - billing_state: State or province portion of the billing address
        - billing_street: Street address portion of the billing address
        - created_by_id: ID of the user who created this account
        - created_date: Date and time when the account was created
        - description: Text description of the account
        - industry: Primary business industry of the account
        - is_deleted: Whether the account has been moved to the Recycle Bin
        - last_activity_date: Date of the last activity associated with this account
        - last_modified_by_id: ID of the user who last modified this account
        - last_modified_date: Date and time when the account was last modified
        - number_of_employees: Number of employees at the account
        - owner_id: ID of the user who owns this account
        - parent_id: ID of the parent account, if this is a subsidiary
        - phone: Primary phone number for the account
        - shipping_address: Complete shipping address as a compound field
        - shipping_city: City portion of the shipping address
        - shipping_country: Country portion of the shipping address
        - shipping_postal_code: Postal code portion of the shipping address
        - shipping_state: State or province portion of the shipping address
        - shipping_street: Street address portion of the shipping address
        - type_: Type of account (e.g., Customer, Partner, Competitor)
        - website: Website URL for the account
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("accounts", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AccountsSearchResult(
            data=[
                AccountsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a list of contacts via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for contacts. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Contact WHERE AccountId = '001xx...' LIMIT 50
  SELECT Id, FirstName, LastName, Account.Name, Owner.Name FROM Contact LIMIT 50
  SELECT Id, Name, Email, Account.Name, ReportsTo.Name FROM Contact WHERE AccountId != null LIMIT 50

Use dot-path traversal (Account.Name, Owner.Name, ReportsTo.Name) to resolve
relationship fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        last_name: str,
        first_name: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        mobile_phone: str | None = None,
        title: str | None = None,
        department: str | None = None,
        account_id: str | None = None,
        mailing_street: str | None = None,
        mailing_city: str | None = None,
        mailing_state: str | None = None,
        mailing_postal_code: str | None = None,
        mailing_country: str | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a contact

        Args:
            first_name: Parameter FirstName
            last_name: Parameter LastName
            email: Parameter Email
            phone: Parameter Phone
            mobile_phone: Parameter MobilePhone
            title: Parameter Title
            department: Parameter Department
            account_id: Parameter AccountId
            mailing_street: Parameter MailingStreet
            mailing_city: Parameter MailingCity
            mailing_state: Parameter MailingState
            mailing_postal_code: Parameter MailingPostalCode
            mailing_country: Parameter MailingCountry
            description: Parameter Description
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "Phone": phone,
            "MobilePhone": mobile_phone,
            "Title": title,
            "Department": department,
            "AccountId": account_id,
            "MailingStreet": mailing_street,
            "MailingCity": mailing_city,
            "MailingState": mailing_state,
            "MailingPostalCode": mailing_postal_code,
            "MailingCountry": mailing_country,
            "Description": description,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Contact ID (18-character ID starting with '003')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,FirstName,LastName,Email,Phone,AccountId"

            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



    async def update(
        self,
        last_name: str,
        first_name: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        mobile_phone: str | None = None,
        title: str | None = None,
        department: str | None = None,
        account_id: str | None = None,
        mailing_street: str | None = None,
        mailing_city: str | None = None,
        mailing_state: str | None = None,
        mailing_postal_code: str | None = None,
        mailing_country: str | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a contact

        Args:
            first_name: Parameter FirstName
            last_name: Parameter LastName
            email: Parameter Email
            phone: Parameter Phone
            mobile_phone: Parameter MobilePhone
            title: Parameter Title
            department: Parameter Department
            account_id: Parameter AccountId
            mailing_street: Parameter MailingStreet
            mailing_city: Parameter MailingCity
            mailing_state: Parameter MailingState
            mailing_postal_code: Parameter MailingPostalCode
            mailing_country: Parameter MailingCountry
            description: Parameter Description
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "Phone": phone,
            "MobilePhone": mobile_phone,
            "Title": title,
            "Department": department,
            "AccountId": account_id,
            "MailingStreet": mailing_street,
            "MailingCity": mailing_city,
            "MailingState": mailing_state,
            "MailingPostalCode": mailing_postal_code,
            "MailingCountry": mailing_country,
            "Description": description,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a contact

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> ContactsApiSearchResult:
        """
        Search for contacts using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Contact(fields) [LIMIT n]
Examples:
- "FIND {John} IN NAME FIELDS RETURNING Contact(Id,FirstName,LastName,Email)"
- "FIND {*@example.com} IN EMAIL FIELDS RETURNING Contact(Id,Name,Email) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            ContactsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ContactsApiSearchResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: ContactsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ContactsSearchResult:
        """
        Search contacts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ContactsSearchFilter):
        - id: Unique identifier for the contact record
        - account_id: ID of the account this contact is associated with
        - created_by_id: ID of the user who created this contact
        - created_date: Date and time when the contact was created
        - department: Department within the account where the contact works
        - email: Email address of the contact
        - first_name: First name of the contact
        - is_deleted: Whether the contact has been moved to the Recycle Bin
        - last_activity_date: Date of the last activity associated with this contact
        - last_modified_by_id: ID of the user who last modified this contact
        - last_modified_date: Date and time when the contact was last modified
        - last_name: Last name of the contact
        - lead_source: Source from which this contact originated
        - mailing_address: Complete mailing address as a compound field
        - mailing_city: City portion of the mailing address
        - mailing_country: Country portion of the mailing address
        - mailing_postal_code: Postal code portion of the mailing address
        - mailing_state: State or province portion of the mailing address
        - mailing_street: Street address portion of the mailing address
        - mobile_phone: Mobile phone number of the contact
        - name: Full name of the contact (read-only, concatenation of first and last name)
        - owner_id: ID of the user who owns this contact
        - phone: Business phone number of the contact
        - reports_to_id: ID of the contact this contact reports to
        - title: Job title of the contact
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ContactsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("contacts", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ContactsSearchResult(
            data=[
                ContactsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class LeadsQuery:
    """
    Query class for Leads entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> LeadsListResult:
        """
        Returns a list of leads via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for leads. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Lead WHERE Status = 'Open' LIMIT 100
  SELECT Id, Name, Company, Owner.Name FROM Lead LIMIT 50
  SELECT Id, Name, Owner.Name, ConvertedAccount.Name, ConvertedContact.Name, ConvertedOpportunity.Name FROM Lead WHERE IsConverted = true LIMIT 50

Use dot-path traversal (Owner.Name, ConvertedAccount.Name, ConvertedContact.Name,
ConvertedOpportunity.Name) to resolve relationship fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            LeadsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "list", params)
        # Cast generic envelope to concrete typed result
        return LeadsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        last_name: str,
        company: str,
        first_name: str | None = None,
        title: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        mobile_phone: str | None = None,
        website: str | None = None,
        status: str | None = None,
        lead_source: str | None = None,
        industry: str | None = None,
        rating: str | None = None,
        annual_revenue: float | None = None,
        number_of_employees: int | None = None,
        street: str | None = None,
        city: str | None = None,
        state: str | None = None,
        postal_code: str | None = None,
        country: str | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a lead

        Args:
            first_name: Parameter FirstName
            last_name: Parameter LastName
            company: Parameter Company
            title: Parameter Title
            email: Parameter Email
            phone: Parameter Phone
            mobile_phone: Parameter MobilePhone
            website: Parameter Website
            status: Parameter Status
            lead_source: Parameter LeadSource
            industry: Parameter Industry
            rating: Parameter Rating
            annual_revenue: Parameter AnnualRevenue
            number_of_employees: Parameter NumberOfEmployees
            street: Parameter Street
            city: Parameter City
            state: Parameter State
            postal_code: Parameter PostalCode
            country: Parameter Country
            description: Parameter Description
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "FirstName": first_name,
            "LastName": last_name,
            "Company": company,
            "Title": title,
            "Email": email,
            "Phone": phone,
            "MobilePhone": mobile_phone,
            "Website": website,
            "Status": status,
            "LeadSource": lead_source,
            "Industry": industry,
            "Rating": rating,
            "AnnualRevenue": annual_revenue,
            "NumberOfEmployees": number_of_employees,
            "Street": street,
            "City": city,
            "State": state,
            "PostalCode": postal_code,
            "Country": country,
            "Description": description,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Lead:
        """
        Get a single lead by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Lead ID (18-character ID starting with '00Q')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,FirstName,LastName,Email,Company,Status,LeadSource"

            **kwargs: Additional parameters

        Returns:
            Lead
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "get", params)
        return result



    async def update(
        self,
        last_name: str,
        company: str,
        first_name: str | None = None,
        title: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        mobile_phone: str | None = None,
        website: str | None = None,
        status: str | None = None,
        lead_source: str | None = None,
        industry: str | None = None,
        rating: str | None = None,
        annual_revenue: float | None = None,
        number_of_employees: int | None = None,
        street: str | None = None,
        city: str | None = None,
        state: str | None = None,
        postal_code: str | None = None,
        country: str | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a lead

        Args:
            first_name: Parameter FirstName
            last_name: Parameter LastName
            company: Parameter Company
            title: Parameter Title
            email: Parameter Email
            phone: Parameter Phone
            mobile_phone: Parameter MobilePhone
            website: Parameter Website
            status: Parameter Status
            lead_source: Parameter LeadSource
            industry: Parameter Industry
            rating: Parameter Rating
            annual_revenue: Parameter AnnualRevenue
            number_of_employees: Parameter NumberOfEmployees
            street: Parameter Street
            city: Parameter City
            state: Parameter State
            postal_code: Parameter PostalCode
            country: Parameter Country
            description: Parameter Description
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "FirstName": first_name,
            "LastName": last_name,
            "Company": company,
            "Title": title,
            "Email": email,
            "Phone": phone,
            "MobilePhone": mobile_phone,
            "Website": website,
            "Status": status,
            "LeadSource": lead_source,
            "Industry": industry,
            "Rating": rating,
            "AnnualRevenue": annual_revenue,
            "NumberOfEmployees": number_of_employees,
            "Street": street,
            "City": city,
            "State": state,
            "PostalCode": postal_code,
            "Country": country,
            "Description": description,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a lead

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> LeadsApiSearchResult:
        """
        Search for leads using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Lead(fields) [LIMIT n]
Examples:
- "FIND {Smith} IN NAME FIELDS RETURNING Lead(Id,FirstName,LastName,Company,Status)"
- "FIND {marketing} IN ALL FIELDS RETURNING Lead(Id,Name,LeadSource) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            LeadsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "api_search", params)
        # Cast generic envelope to concrete typed result
        return LeadsApiSearchResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: LeadsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LeadsSearchResult:
        """
        Search leads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LeadsSearchFilter):
        - id: Unique identifier for the lead record
        - address: Complete address as a compound field
        - city: City portion of the address
        - company: Company or organization the lead works for
        - converted_account_id: ID of the account created when lead was converted
        - converted_contact_id: ID of the contact created when lead was converted
        - converted_date: Date when the lead was converted
        - converted_opportunity_id: ID of the opportunity created when lead was converted
        - country: Country portion of the address
        - created_by_id: ID of the user who created this lead
        - created_date: Date and time when the lead was created
        - email: Email address of the lead
        - first_name: First name of the lead
        - industry: Industry the lead's company operates in
        - is_converted: Whether the lead has been converted to an account, contact, and opportunity
        - is_deleted: Whether the lead has been moved to the Recycle Bin
        - last_activity_date: Date of the last activity associated with this lead
        - last_modified_by_id: ID of the user who last modified this lead
        - last_modified_date: Date and time when the lead was last modified
        - last_name: Last name of the lead
        - lead_source: Source from which this lead originated
        - mobile_phone: Mobile phone number of the lead
        - name: Full name of the lead (read-only, concatenation of first and last name)
        - number_of_employees: Number of employees at the lead's company
        - owner_id: ID of the user who owns this lead
        - phone: Phone number of the lead
        - postal_code: Postal code portion of the address
        - rating: Rating of the lead (e.g., Hot, Warm, Cold)
        - state: State or province portion of the address
        - status: Current status of the lead in the sales process
        - street: Street address portion of the address
        - title: Job title of the lead
        - website: Website URL for the lead's company
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LeadsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("leads", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LeadsSearchResult(
            data=[
                LeadsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OpportunitiesQuery:
    """
    Query class for Opportunities entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> OpportunitiesListResult:
        """
        Returns a list of opportunities via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
For "top", "largest", or "highest-value" opportunity requests, first choose a
visible financial opportunity field. Standard candidates include `Amount` for
total deal value and `ExpectedRevenue` for expected, weighted, or forecast revenue.


        Args:
            q: SOQL query for opportunities. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Opportunity WHERE StageName = 'Closed Won' LIMIT 50
  SELECT Id, Name, Amount, Account.Name, Owner.Name FROM Opportunity LIMIT 50
  SELECT Id, Name, Amount, StageName, Account.Name FROM Opportunity ORDER BY Amount DESC LIMIT 10
  SELECT Id, Name, ExpectedRevenue, Probability, Amount FROM Opportunity ORDER BY ExpectedRevenue DESC LIMIT 10
  SELECT Id, Name, StageName, Account.Name, Account.Industry, Owner.Name, Campaign.Name FROM Opportunity WHERE CloseDate = THIS_QUARTER LIMIT 50

Use dot-path traversal (Account.Name, Owner.Name, Campaign.Name) to resolve
relationship fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            OpportunitiesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "list", params)
        # Cast generic envelope to concrete typed result
        return OpportunitiesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        name: str,
        stage_name: str,
        close_date: str,
        account_id: str | None = None,
        amount: float | None = None,
        probability: float | None = None,
        type: str | None = None,
        lead_source: str | None = None,
        next_step: str | None = None,
        campaign_id: str | None = None,
        forecast_category_name: str | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create an opportunity

        Args:
            name: Parameter Name
            account_id: Parameter AccountId
            stage_name: Opportunity stage (e.g., Prospecting, Qualification, Closed Won).
            close_date: Parameter CloseDate
            amount: Parameter Amount
            probability: Parameter Probability
            type: Parameter Type
            lead_source: Parameter LeadSource
            next_step: Parameter NextStep
            campaign_id: Parameter CampaignId
            forecast_category_name: Parameter ForecastCategoryName
            description: Parameter Description
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Name": name,
            "AccountId": account_id,
            "StageName": stage_name,
            "CloseDate": close_date,
            "Amount": amount,
            "Probability": probability,
            "Type": type,
            "LeadSource": lead_source,
            "NextStep": next_step,
            "CampaignId": campaign_id,
            "ForecastCategoryName": forecast_category_name,
            "Description": description,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Opportunity:
        """
        Get a single opportunity by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Opportunity ID (18-character ID starting with '006')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Amount,StageName,CloseDate,AccountId"

            **kwargs: Additional parameters

        Returns:
            Opportunity
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "get", params)
        return result



    async def update(
        self,
        name: str,
        stage_name: str,
        close_date: str,
        account_id: str | None = None,
        amount: float | None = None,
        probability: float | None = None,
        type: str | None = None,
        lead_source: str | None = None,
        next_step: str | None = None,
        campaign_id: str | None = None,
        forecast_category_name: str | None = None,
        description: str | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update an opportunity

        Args:
            name: Parameter Name
            account_id: Parameter AccountId
            stage_name: Opportunity stage (e.g., Prospecting, Qualification, Closed Won).
            close_date: Parameter CloseDate
            amount: Parameter Amount
            probability: Parameter Probability
            type: Parameter Type
            lead_source: Parameter LeadSource
            next_step: Parameter NextStep
            campaign_id: Parameter CampaignId
            forecast_category_name: Parameter ForecastCategoryName
            description: Parameter Description
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Name": name,
            "AccountId": account_id,
            "StageName": stage_name,
            "CloseDate": close_date,
            "Amount": amount,
            "Probability": probability,
            "Type": type,
            "LeadSource": lead_source,
            "NextStep": next_step,
            "CampaignId": campaign_id,
            "ForecastCategoryName": forecast_category_name,
            "Description": description,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete an opportunity

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> OpportunitiesApiSearchResult:
        """
        Search for opportunities using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Opportunity(fields) [LIMIT n]
Examples:
- "FIND {Enterprise} IN NAME FIELDS RETURNING Opportunity(Id,Name,Amount,StageName)"
- "FIND {renewal} IN ALL FIELDS RETURNING Opportunity(Id,Name,CloseDate) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            OpportunitiesApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "api_search", params)
        # Cast generic envelope to concrete typed result
        return OpportunitiesApiSearchResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: OpportunitiesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OpportunitiesSearchResult:
        """
        Search opportunities records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OpportunitiesSearchFilter):
        - id: Unique identifier for the opportunity record
        - account_id: ID of the account associated with this opportunity
        - amount: Estimated total sale amount
        - campaign_id: ID of the campaign that generated this opportunity
        - close_date: Expected close date for the opportunity
        - contact_id: ID of the primary contact for this opportunity
        - created_by_id: ID of the user who created this opportunity
        - created_date: Date and time when the opportunity was created
        - description: Text description of the opportunity
        - expected_revenue: Expected revenue based on amount and probability
        - forecast_category: Forecast category for this opportunity
        - forecast_category_name: Name of the forecast category
        - is_closed: Whether the opportunity is closed
        - is_deleted: Whether the opportunity has been moved to the Recycle Bin
        - is_won: Whether the opportunity was won
        - last_activity_date: Date of the last activity associated with this opportunity
        - last_modified_by_id: ID of the user who last modified this opportunity
        - last_modified_date: Date and time when the opportunity was last modified
        - lead_source: Source from which this opportunity originated
        - name: Name of the opportunity
        - next_step: Description of the next step in closing the opportunity
        - owner_id: ID of the user who owns this opportunity
        - probability: Likelihood of closing the opportunity (percentage)
        - stage_name: Current stage of the opportunity in the sales process
        - type_: Type of opportunity (e.g., New Business, Existing Business)
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OpportunitiesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("opportunities", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OpportunitiesSearchResult(
            data=[
                OpportunitiesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> TasksListResult:
        """
        Returns a list of tasks via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for tasks. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Task WHERE Status = 'Not Started' LIMIT 100
  SELECT Id, Subject, Status, Owner.Name, Account.Name FROM Task LIMIT 50
  SELECT Id, Subject, Status, Owner.Name, Who.Name, What.Name FROM Task WHERE ActivityDate = THIS_WEEK LIMIT 50

Use dot-path traversal (Owner.Name, Account.Name) to resolve relationship
fields inline instead of returning raw IDs. Who.Name and What.Name resolve
polymorphic WhoId/WhatId references to the related record's name.

            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TasksListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        subject: str,
        status: str | None = None,
        priority: str | None = None,
        activity_date: str | None = None,
        who_id: str | None = None,
        what_id: str | None = None,
        description: str | None = None,
        type: str | None = None,
        is_reminder_set: bool | None = None,
        reminder_date_time: str | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a task

        Args:
            subject: Parameter Subject
            status: Task status (e.g., Not Started, In Progress, Completed).
            priority: Parameter Priority
            activity_date: Parameter ActivityDate
            who_id: Related contact or lead Id.
            what_id: Related Account, Opportunity, or other object Id.
            description: Parameter Description
            type: Parameter Type
            is_reminder_set: Parameter IsReminderSet
            reminder_date_time: Parameter ReminderDateTime
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Subject": subject,
            "Status": status,
            "Priority": priority,
            "ActivityDate": activity_date,
            "WhoId": who_id,
            "WhatId": what_id,
            "Description": description,
            "Type": type,
            "IsReminderSet": is_reminder_set,
            "ReminderDateTime": reminder_date_time,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Task:
        """
        Get a single task by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Task ID (18-character ID starting with '00T')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Subject,Status,Priority,ActivityDate,WhoId,WhatId"

            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def update(
        self,
        subject: str,
        status: str | None = None,
        priority: str | None = None,
        activity_date: str | None = None,
        who_id: str | None = None,
        what_id: str | None = None,
        description: str | None = None,
        type: str | None = None,
        is_reminder_set: bool | None = None,
        reminder_date_time: str | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a task

        Args:
            subject: Parameter Subject
            status: Task status (e.g., Not Started, In Progress, Completed).
            priority: Parameter Priority
            activity_date: Parameter ActivityDate
            who_id: Related contact or lead Id.
            what_id: Related Account, Opportunity, or other object Id.
            description: Parameter Description
            type: Parameter Type
            is_reminder_set: Parameter IsReminderSet
            reminder_date_time: Parameter ReminderDateTime
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Subject": subject,
            "Status": status,
            "Priority": priority,
            "ActivityDate": activity_date,
            "WhoId": who_id,
            "WhatId": what_id,
            "Description": description,
            "Type": type,
            "IsReminderSet": is_reminder_set,
            "ReminderDateTime": reminder_date_time,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a task

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> TasksApiSearchResult:
        """
        Search for tasks using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Task(fields) [LIMIT n]
Examples:
- "FIND {follow up} IN ALL FIELDS RETURNING Task(Id,Subject,Status,Priority)"
- "FIND {call} IN NAME FIELDS RETURNING Task(Id,Subject,ActivityDate) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            TasksApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "api_search", params)
        # Cast generic envelope to concrete typed result
        return TasksApiSearchResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: TasksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TasksSearchResult:
        """
        Search tasks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TasksSearchFilter):
        - id: Unique identifier for the task record
        - account_id: ID of the account associated with this task
        - activity_date: Due date for the task
        - call_disposition: Result of the call, if this task represents a call
        - call_duration_in_seconds: Duration of the call in seconds
        - call_type: Type of call (Inbound, Outbound, Internal)
        - completed_date_time: Date and time when the task was completed
        - created_by_id: ID of the user who created this task
        - created_date: Date and time when the task was created
        - description: Text description or notes about the task
        - is_closed: Whether the task has been completed
        - is_deleted: Whether the task has been moved to the Recycle Bin
        - is_high_priority: Whether the task is marked as high priority
        - last_modified_by_id: ID of the user who last modified this task
        - last_modified_date: Date and time when the task was last modified
        - owner_id: ID of the user who owns this task
        - priority: Priority level of the task (High, Normal, Low)
        - status: Current status of the task
        - subject: Subject or title of the task
        - task_subtype: Subtype of the task (e.g., Call, Email, Task)
        - type_: Type of task
        - what_id: ID of the related object (Account, Opportunity, etc.)
        - who_id: ID of the related person (Contact or Lead)
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TasksSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("tasks", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TasksSearchResult(
            data=[
                TasksSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class EventsQuery:
    """
    Query class for Events entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> EventsListResult:
        """
        Returns a list of events via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for events. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Event WHERE StartDateTime > TODAY LIMIT 50
  SELECT Id, Subject, StartDateTime, Owner.Name, Account.Name FROM Event LIMIT 50
  SELECT Id, Subject, StartDateTime, Owner.Name, Who.Name, What.Name FROM Event WHERE StartDateTime = THIS_WEEK LIMIT 50

Use dot-path traversal (Owner.Name, Account.Name) to resolve relationship
fields inline instead of returning raw IDs. Who.Name and What.Name resolve
polymorphic WhoId/WhatId references to the related record's name.

            **kwargs: Additional parameters

        Returns:
            EventsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "list", params)
        # Cast generic envelope to concrete typed result
        return EventsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        subject: str,
        start_date_time: str,
        duration_in_minutes: int,
        end_date_time: str | None = None,
        location: str | None = None,
        description: str | None = None,
        who_id: str | None = None,
        what_id: str | None = None,
        is_all_day_event: bool | None = None,
        show_as: str | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create an event

        Args:
            subject: Parameter Subject
            start_date_time: Parameter StartDateTime
            end_date_time: Parameter EndDateTime
            duration_in_minutes: Parameter DurationInMinutes
            location: Parameter Location
            description: Parameter Description
            who_id: Parameter WhoId
            what_id: Parameter WhatId
            is_all_day_event: Parameter IsAllDayEvent
            show_as: Parameter ShowAs
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Subject": subject,
            "StartDateTime": start_date_time,
            "EndDateTime": end_date_time,
            "DurationInMinutes": duration_in_minutes,
            "Location": location,
            "Description": description,
            "WhoId": who_id,
            "WhatId": what_id,
            "IsAllDayEvent": is_all_day_event,
            "ShowAs": show_as,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Event:
        """
        Get a single event by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Event ID (18-character ID starting with '00U')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Subject,StartDateTime,EndDateTime,Location,WhoId,WhatId"

            **kwargs: Additional parameters

        Returns:
            Event
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "get", params)
        return result



    async def update(
        self,
        subject: str,
        start_date_time: str,
        duration_in_minutes: int,
        end_date_time: str | None = None,
        location: str | None = None,
        description: str | None = None,
        who_id: str | None = None,
        what_id: str | None = None,
        is_all_day_event: bool | None = None,
        show_as: str | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update an event

        Args:
            subject: Parameter Subject
            start_date_time: Parameter StartDateTime
            end_date_time: Parameter EndDateTime
            duration_in_minutes: Parameter DurationInMinutes
            location: Parameter Location
            description: Parameter Description
            who_id: Parameter WhoId
            what_id: Parameter WhatId
            is_all_day_event: Parameter IsAllDayEvent
            show_as: Parameter ShowAs
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Subject": subject,
            "StartDateTime": start_date_time,
            "EndDateTime": end_date_time,
            "DurationInMinutes": duration_in_minutes,
            "Location": location,
            "Description": description,
            "WhoId": who_id,
            "WhatId": what_id,
            "IsAllDayEvent": is_all_day_event,
            "ShowAs": show_as,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete an event

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> EventsApiSearchResult:
        """
        Search for events using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Event(fields) [LIMIT n]
Examples:
- "FIND {meeting} IN ALL FIELDS RETURNING Event(Id,Subject,StartDateTime,Location)"
- "FIND {demo} IN NAME FIELDS RETURNING Event(Id,Subject,EndDateTime) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            EventsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "api_search", params)
        # Cast generic envelope to concrete typed result
        return EventsApiSearchResult(
            data=result.data
        )



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a list of campaigns via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for campaigns. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Campaign WHERE IsActive = true LIMIT 50
  SELECT Id, Name, Type, Status, Owner.Name FROM Campaign LIMIT 50
  SELECT Id, Name, Owner.Name, Owner.Email, StartDate FROM Campaign WHERE IsActive = true LIMIT 50

Use dot-path traversal (Owner.Name) to resolve relationship fields inline
instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        name: str,
        type: str | None = None,
        status: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        is_active: bool | None = None,
        description: str | None = None,
        expected_revenue: float | None = None,
        budgeted_cost: float | None = None,
        actual_cost: float | None = None,
        expected_response: float | None = None,
        number_sent: float | None = None,
        parent_id: str | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a campaign

        Args:
            name: Parameter Name
            type: Parameter Type
            status: Parameter Status
            start_date: Parameter StartDate
            end_date: Parameter EndDate
            is_active: Parameter IsActive
            description: Parameter Description
            expected_revenue: Parameter ExpectedRevenue
            budgeted_cost: Parameter BudgetedCost
            actual_cost: Parameter ActualCost
            expected_response: Parameter ExpectedResponse
            number_sent: Parameter NumberSent
            parent_id: Parameter ParentId
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Name": name,
            "Type": type,
            "Status": status,
            "StartDate": start_date,
            "EndDate": end_date,
            "IsActive": is_active,
            "Description": description,
            "ExpectedRevenue": expected_revenue,
            "BudgetedCost": budgeted_cost,
            "ActualCost": actual_cost,
            "ExpectedResponse": expected_response,
            "NumberSent": number_sent,
            "ParentId": parent_id,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Campaign:
        """
        Get a single campaign by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Campaign ID (18-character ID starting with '701')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Type,Status,StartDate,EndDate,IsActive"

            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def update(
        self,
        name: str,
        type: str | None = None,
        status: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        is_active: bool | None = None,
        description: str | None = None,
        expected_revenue: float | None = None,
        budgeted_cost: float | None = None,
        actual_cost: float | None = None,
        expected_response: float | None = None,
        number_sent: float | None = None,
        parent_id: str | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a campaign

        Args:
            name: Parameter Name
            type: Parameter Type
            status: Parameter Status
            start_date: Parameter StartDate
            end_date: Parameter EndDate
            is_active: Parameter IsActive
            description: Parameter Description
            expected_revenue: Parameter ExpectedRevenue
            budgeted_cost: Parameter BudgetedCost
            actual_cost: Parameter ActualCost
            expected_response: Parameter ExpectedResponse
            number_sent: Parameter NumberSent
            parent_id: Parameter ParentId
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Name": name,
            "Type": type,
            "Status": status,
            "StartDate": start_date,
            "EndDate": end_date,
            "IsActive": is_active,
            "Description": description,
            "ExpectedRevenue": expected_revenue,
            "BudgetedCost": budgeted_cost,
            "ActualCost": actual_cost,
            "ExpectedResponse": expected_response,
            "NumberSent": number_sent,
            "ParentId": parent_id,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a campaign

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> CampaignsApiSearchResult:
        """
        Search for campaigns using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Campaign(fields) [LIMIT n]
Examples:
- "FIND {webinar} IN ALL FIELDS RETURNING Campaign(Id,Name,Type,Status)"
- "FIND {2024} IN NAME FIELDS RETURNING Campaign(Id,Name,StartDate,IsActive) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            CampaignsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CampaignsApiSearchResult(
            data=result.data
        )



class CasesQuery:
    """
    Query class for Cases entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> CasesListResult:
        """
        Returns a list of cases via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for cases. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Case WHERE Status = 'New' LIMIT 100
  SELECT Id, CaseNumber, Subject, Account.Name, Owner.Name, Contact.Name FROM Case LIMIT 50
  SELECT Id, CaseNumber, Subject, Status, Account.Name, Owner.Name FROM Case WHERE Status = 'Escalated' LIMIT 50

Use dot-path traversal (Account.Name, Owner.Name, Contact.Name) to resolve
relationship fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            CasesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "list", params)
        # Cast generic envelope to concrete typed result
        return CasesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        subject: str | None = None,
        status: str | None = None,
        priority: str | None = None,
        origin: str | None = None,
        type: str | None = None,
        reason: str | None = None,
        description: str | None = None,
        account_id: str | None = None,
        contact_id: str | None = None,
        supplied_name: str | None = None,
        supplied_email: str | None = None,
        supplied_phone: str | None = None,
        supplied_company: str | None = None,
        owner_id: str | None = None,
        parent_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a case

        Args:
            subject: Parameter Subject
            status: Parameter Status
            priority: Parameter Priority
            origin: Parameter Origin
            type: Parameter Type
            reason: Parameter Reason
            description: Parameter Description
            account_id: Parameter AccountId
            contact_id: Parameter ContactId
            supplied_name: Parameter SuppliedName
            supplied_email: Parameter SuppliedEmail
            supplied_phone: Parameter SuppliedPhone
            supplied_company: Parameter SuppliedCompany
            owner_id: Parameter OwnerId
            parent_id: Parameter ParentId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Subject": subject,
            "Status": status,
            "Priority": priority,
            "Origin": origin,
            "Type": type,
            "Reason": reason,
            "Description": description,
            "AccountId": account_id,
            "ContactId": contact_id,
            "SuppliedName": supplied_name,
            "SuppliedEmail": supplied_email,
            "SuppliedPhone": supplied_phone,
            "SuppliedCompany": supplied_company,
            "OwnerId": owner_id,
            "ParentId": parent_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Case:
        """
        Get a single case by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Case ID (18-character ID starting with '500')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,CaseNumber,Subject,Status,Priority,ContactId,AccountId"

            **kwargs: Additional parameters

        Returns:
            Case
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "get", params)
        return result



    async def update(
        self,
        subject: str | None = None,
        status: str | None = None,
        priority: str | None = None,
        origin: str | None = None,
        type: str | None = None,
        reason: str | None = None,
        description: str | None = None,
        account_id: str | None = None,
        contact_id: str | None = None,
        supplied_name: str | None = None,
        supplied_email: str | None = None,
        supplied_phone: str | None = None,
        supplied_company: str | None = None,
        owner_id: str | None = None,
        parent_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a case

        Args:
            subject: Parameter Subject
            status: Parameter Status
            priority: Parameter Priority
            origin: Parameter Origin
            type: Parameter Type
            reason: Parameter Reason
            description: Parameter Description
            account_id: Parameter AccountId
            contact_id: Parameter ContactId
            supplied_name: Parameter SuppliedName
            supplied_email: Parameter SuppliedEmail
            supplied_phone: Parameter SuppliedPhone
            supplied_company: Parameter SuppliedCompany
            owner_id: Parameter OwnerId
            parent_id: Parameter ParentId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Subject": subject,
            "Status": status,
            "Priority": priority,
            "Origin": origin,
            "Type": type,
            "Reason": reason,
            "Description": description,
            "AccountId": account_id,
            "ContactId": contact_id,
            "SuppliedName": supplied_name,
            "SuppliedEmail": supplied_email,
            "SuppliedPhone": supplied_phone,
            "SuppliedCompany": supplied_company,
            "OwnerId": owner_id,
            "ParentId": parent_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a case

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> CasesApiSearchResult:
        """
        Search for cases using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Case(fields) [LIMIT n]
Examples:
- "FIND {login issue} IN ALL FIELDS RETURNING Case(Id,CaseNumber,Subject,Status)"
- "FIND {urgent} IN NAME FIELDS RETURNING Case(Id,Subject,Priority) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            CasesApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CasesApiSearchResult(
            data=result.data
        )



class NotesQuery:
    """
    Query class for Notes entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> NotesListResult:
        """
        Returns a list of notes via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for notes. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM Note WHERE ParentId = '001xx...' LIMIT 50
  SELECT Id, Title, Body, Owner.Name FROM Note LIMIT 50
  SELECT Id, Title, Owner.Name, CreatedDate FROM Note ORDER BY CreatedDate DESC LIMIT 50

Use dot-path traversal (Owner.Name) to resolve relationship fields inline
instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            NotesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "list", params)
        # Cast generic envelope to concrete typed result
        return NotesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        title: str,
        parent_id: str,
        body: str | None = None,
        is_private: bool | None = None,
        owner_id: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a classic Salesforce Note attached to a parent record (Account, Contact,
Lead, Opportunity, Case, custom object, etc.). `Title` and `ParentId` are required.


        Args:
            title: Note title, up to 80 characters.
            body: Note body content (up to ~32,000 characters).
            parent_id: Id of the parent record this note is attached to (Account, Contact, Lead, Opportunity, Case, custom object, etc.).
            is_private: When true, the note is visible only to its owner and admins.
            owner_id: Parameter OwnerId
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Title": title,
            "Body": body,
            "ParentId": parent_id,
            "IsPrivate": is_private,
            "OwnerId": owner_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Note:
        """
        Get a single note by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Note ID (18-character ID starting with '002')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Title,Body,ParentId,OwnerId"

            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "get", params)
        return result



    async def update(
        self,
        title: str | None = None,
        body: str | None = None,
        is_private: bool | None = None,
        owner_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a note

        Args:
            title: Note title, up to 80 characters.
            body: Note body content (up to ~32,000 characters).
            is_private: When true, the note is visible only to its owner and admins.
            owner_id: Parameter OwnerId
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Title": title,
            "Body": body,
            "IsPrivate": is_private,
            "OwnerId": owner_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete a note

        Args:
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "delete", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> NotesApiSearchResult:
        """
        Search for notes using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Note(fields) [LIMIT n]
Examples:
- "FIND {important} IN ALL FIELDS RETURNING Note(Id,Title,ParentId)"
- "FIND {action items} IN NAME FIELDS RETURNING Note(Id,Title,Body) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            NotesApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "api_search", params)
        # Cast generic envelope to concrete typed result
        return NotesApiSearchResult(
            data=result.data
        )



class ContentVersionsQuery:
    """
    Query class for ContentVersions entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> ContentVersionsListResult:
        """
        Returns a list of content versions (file metadata) via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
Note: ContentVersion does not support FIELDS(STANDARD), so specific fields must be listed.


        Args:
            q: SOQL query for content versions. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT Id, Title, FileExtension, ContentSize FROM ContentVersion WHERE IsLatest = true LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            ContentVersionsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "list", params)
        # Cast generic envelope to concrete typed result
        return ContentVersionsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> ContentVersion:
        """
        Get a single content version's metadata by ID. Returns file metadata, not the file content.
Use the download action to retrieve the actual file binary.


        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Title,FileExtension,ContentSize,ContentDocumentId,IsLatest"

            **kwargs: Additional parameters

        Returns:
            ContentVersion
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "get", params)
        return result



    async def download(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.


        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "download", params)
        return result


    async def download_text(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.
 and return a JSON-safe UTF-8 text chunk.
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs,
            "_airbyte_response_type": "json",
            "_airbyte_response_format": "text",
        }.items() if v is not None}

        return await self._connector.execute("content_versions", "download", params)

    async def download_base64(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.
 and return a JSON-safe base64 chunk.
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs,
            "_airbyte_response_type": "json",
            "_airbyte_response_format": "base64",
        }.items() if v is not None}

        return await self._connector.execute("content_versions", "download", params)

    async def download_local(
        self,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.
 and save to file.

        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from airbyte_agent_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> AttachmentsListResult:
        """
        Returns a list of attachments (legacy) via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
Note: Attachments are a legacy feature; consider using ContentVersion (Salesforce Files) for new implementations.


        Args:
            q: SOQL query for attachments. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT Id, Name, ContentType, BodyLength, ParentId FROM Attachment WHERE ParentId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            AttachmentsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "list", params)
        # Cast generic envelope to concrete typed result
        return AttachmentsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Attachment:
        """
        Get a single attachment's metadata by ID. Returns file metadata, not the file content.
Use the download action to retrieve the actual file binary.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.


        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,ContentType,BodyLength,ParentId"

            **kwargs: Additional parameters

        Returns:
            Attachment
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        return result



    async def download(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.


        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_text(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.
 and return a JSON-safe UTF-8 text chunk.
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs,
            "_airbyte_response_type": "json",
            "_airbyte_response_format": "text",
        }.items() if v is not None}

        return await self._connector.execute("attachments", "download", params)

    async def download_base64(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.
 and return a JSON-safe base64 chunk.
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs,
            "_airbyte_response_type": "json",
            "_airbyte_response_format": "base64",
        }.items() if v is not None}

        return await self._connector.execute("attachments", "download", params)

    async def download_local(
        self,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.
 and save to file.

        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from airbyte_agent_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class ReportsQuery:
    """
    Query class for Reports entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ReportsListResult:
        """
        Returns a list of reports available in the Salesforce org.
Each report includes metadata such as Id, Name, Format, Description, and URL.
This uses the Analytics REST API, not SOQL.


        Returns:
            ReportsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reports", "list", params)
        # Cast generic envelope to concrete typed result
        return ReportsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        include_details: bool | None = None,
        **kwargs
    ) -> ReportResults:
        """
        Executes a report synchronously and returns the report data results.
Returns both metadata and the executed data including fact maps, aggregates, and detail rows.
First use the list action to find available reports, then use this action to run a report and get its data.
Note: Large reports may be truncated. For reports with more than 2,000 detail rows, consider using async report runs.


        Args:
            id: Salesforce Report ID (18-character ID starting with '00O').
Obtain this ID from the list action.

            include_details: Whether to include detail rows in the report results. Defaults to true.
Set to false to get only summary/aggregate data.

            **kwargs: Additional parameters

        Returns:
            ReportResults
        """
        params = {k: v for k, v in {
            "id": id,
            "includeDetails": include_details,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reports", "get", params)
        return result



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a list of users via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for users. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.

Examples:
  SELECT FIELDS(STANDARD) FROM User WHERE IsActive = true ORDER BY LastModifiedDate DESC LIMIT 50
  SELECT Id, Name, Email, Manager.Name, Profile.Name FROM User WHERE IsActive = true LIMIT 50
  SELECT Id, Name, Email, Department, UserRole.Name FROM User LIMIT 50

Use dot-path traversal (Manager.Name, Profile.Name, UserRole.Name) to resolve
relationship fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        username: str,
        last_name: str,
        email: str,
        alias: str,
        profile_id: str,
        time_zone_sid_key: str,
        locale_sid_key: str,
        email_encoding_key: str,
        language_locale_key: str,
        first_name: str | None = None,
        user_role_id: str | None = None,
        manager_id: str | None = None,
        is_active: bool | None = None,
        title: str | None = None,
        department: str | None = None,
        phone: str | None = None,
        mobile_phone: str | None = None,
        **kwargs
    ) -> SObjectCreateResponse:
        """
        Create a Salesforce User. Consumes a paid user-license seat. Requires the
"Manage Internal Users" permission on the running OAuth identity.


        Args:
            username: Login name (email-format, must be unique across all Salesforce orgs).
            first_name: Parameter FirstName
            last_name: Parameter LastName
            email: Parameter Email
            alias: 1-8 character alias.
            profile_id: Salesforce profile that determines the user's base permissions.
            user_role_id: Parameter UserRoleId
            manager_id: Parameter ManagerId
            time_zone_sid_key: e.g., "America/Los_Angeles".
            locale_sid_key: e.g., "en_US".
            email_encoding_key: e.g., "UTF-8".
            language_locale_key: e.g., "en_US".
            is_active: Set to false to deactivate the user (Salesforce does not support delete).
            title: Parameter Title
            department: Parameter Department
            phone: Parameter Phone
            mobile_phone: Parameter MobilePhone
            **kwargs: Additional parameters

        Returns:
            SObjectCreateResponse
        """
        params = {k: v for k, v in {
            "Username": username,
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "Alias": alias,
            "ProfileId": profile_id,
            "UserRoleId": user_role_id,
            "ManagerId": manager_id,
            "TimeZoneSidKey": time_zone_sid_key,
            "LocaleSidKey": locale_sid_key,
            "EmailEncodingKey": email_encoding_key,
            "LanguageLocaleKey": language_locale_key,
            "IsActive": is_active,
            "Title": title,
            "Department": department,
            "Phone": phone,
            "MobilePhone": mobile_phone,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> User:
        """
        Get a single user by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce User ID (18-character ID starting with '005')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Email,Username,IsActive,ProfileId,UserRoleId"

            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



    async def update(
        self,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        alias: str | None = None,
        profile_id: str | None = None,
        user_role_id: str | None = None,
        manager_id: str | None = None,
        time_zone_sid_key: str | None = None,
        locale_sid_key: str | None = None,
        email_encoding_key: str | None = None,
        language_locale_key: str | None = None,
        is_active: bool | None = None,
        title: str | None = None,
        department: str | None = None,
        phone: str | None = None,
        mobile_phone: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update a Salesforce User. To deactivate a user (Salesforce does not allow
delete), send `{ "IsActive": false }`.


        Args:
            username: Login name (email-format, must be unique across all Salesforce orgs).
            first_name: Parameter FirstName
            last_name: Parameter LastName
            email: Parameter Email
            alias: 1-8 character alias.
            profile_id: Salesforce profile that determines the user's base permissions.
            user_role_id: Parameter UserRoleId
            manager_id: Parameter ManagerId
            time_zone_sid_key: e.g., "America/Los_Angeles".
            locale_sid_key: e.g., "en_US".
            email_encoding_key: e.g., "UTF-8".
            language_locale_key: e.g., "en_US".
            is_active: Set to false to deactivate the user (Salesforce does not support delete).
            title: Parameter Title
            department: Parameter Department
            phone: Parameter Phone
            mobile_phone: Parameter MobilePhone
            id: Parameter id
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "Username": username,
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "Alias": alias,
            "ProfileId": profile_id,
            "UserRoleId": user_role_id,
            "ManagerId": manager_id,
            "TimeZoneSidKey": time_zone_sid_key,
            "LocaleSidKey": locale_sid_key,
            "EmailEncodingKey": email_encoding_key,
            "LanguageLocaleKey": language_locale_key,
            "IsActive": is_active,
            "Title": title,
            "Department": department,
            "Phone": phone,
            "MobilePhone": mobile_phone,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "update", params)
        return result



    async def context_store_search(
        self,
        query: UsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> UsersSearchResult:
        """
        Search users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (UsersSearchFilter):
        - id: Unique identifier for the user record
        - account_id: ID of the account associated with this user (for portal users)
        - alias: Short name used to identify the user in list views and reports
        - city: City portion of the user's address
        - company_name: Name of the user's company
        - contact_id: ID of the contact associated with this user (for portal users)
        - country: Country portion of the user's address
        - created_by_id: ID of the user who created this user record
        - created_date: Date and time when the user was created
        - department: Department within the organization
        - division: Division within the organization
        - email: Email address of the user
        - employee_number: Employee number or ID assigned by the organization
        - first_name: First name of the user
        - is_active: Whether the user is active and can log in
        - last_login_date: Date and time of the user's most recent login
        - last_modified_by_id: ID of the user who last modified this user record
        - last_modified_date: Date and time when the user was last modified
        - last_name: Last name of the user
        - manager_id: ID of the user's manager
        - mobile_phone: Mobile phone number of the user
        - name: Full name of the user
        - phone: Business phone number of the user
        - postal_code: Postal code portion of the user's address
        - profile_id: ID of the user's profile
        - state: State or province portion of the user's address
        - street: Street address of the user
        - title: Job title of the user
        - user_role_id: ID of the user's role in the organization
        - user_type: Type of user license (e.g., Standard, PowerPartner)
        - username: Username for logging into Salesforce (unique across all orgs)
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UsersSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("users", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return UsersSearchResult(
            data=[
                UsersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OpportunityStagesQuery:
    """
    Query class for OpportunityStages entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> OpportunityStagesListResult:
        """
        Returns a list of opportunity stages via SOQL query. Default returns all stages.
OpportunityStage defines the sales process stages that opportunities move through.


        Args:
            q: SOQL query for opportunity stages. Default returns all stages.

Examples:
  SELECT FIELDS(STANDARD) FROM OpportunityStage ORDER BY SortOrder ASC
  SELECT Id, MasterLabel, ApiName, DefaultProbability, IsClosed, IsWon, IsActive, ForecastCategoryName FROM OpportunityStage WHERE IsActive = true ORDER BY SortOrder ASC
  SELECT Id, MasterLabel, DefaultProbability, CreatedBy.Name FROM OpportunityStage ORDER BY SortOrder ASC

Use dot-path traversal (CreatedBy.Name, LastModifiedBy.Name) to resolve
relationship fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            OpportunityStagesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunity_stages", "list", params)
        # Cast generic envelope to concrete typed result
        return OpportunityStagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> OpportunityStage:
        """
        Get a single opportunity stage by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce OpportunityStage ID
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,MasterLabel,ApiName,DefaultProbability,IsClosed,IsWon,IsActive"

            **kwargs: Additional parameters

        Returns:
            OpportunityStage
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunity_stages", "get", params)
        return result



    async def context_store_search(
        self,
        query: OpportunityStagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OpportunityStagesSearchResult:
        """
        Search opportunity_stages records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OpportunityStagesSearchFilter):
        - id: Unique identifier for the opportunity stage record
        - api_name: API name of the stage used in code and integrations
        - created_by_id: ID of the user who created this stage
        - created_date: Date and time when the stage was created
        - default_probability: Default probability percentage for opportunities at this stage
        - description: Description of the stage
        - forecast_category: Forecast category for opportunities at this stage
        - forecast_category_name: Display name of the forecast category
        - is_active: Whether the stage is currently active and can be used
        - is_closed: Whether opportunities at this stage are considered closed
        - is_won: Whether opportunities at this stage are considered won
        - last_modified_by_id: ID of the user who last modified this stage
        - last_modified_date: Date and time when the stage was last modified
        - master_label: Display label for the stage
        - sort_order: Order in which the stage appears in the sales process
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OpportunityStagesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("opportunity_stages", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OpportunityStagesSearchResult(
            data=[
                OpportunityStagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class QueryQuery:
    """
    Query class for Query entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> QueryListResult:
        """
        Execute a custom SOQL query and return results. Use this for querying any Salesforce object.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query string. Include LIMIT clause to control the number of records returned.
Examples:
- "SELECT Id, Name FROM Account LIMIT 100"
- "SELECT FIELDS(STANDARD) FROM Contact WHERE AccountId = '001xx...' LIMIT 50"
- "SELECT Id, Subject, Status FROM Case WHERE CreatedDate = TODAY"
- "SELECT Id, Name, Account.Name, Owner.Name FROM Opportunity LIMIT 50"

Use dot-path traversal (e.g. Owner.Name, Account.Name) to resolve relationship
fields inline instead of returning raw IDs.

            **kwargs: Additional parameters

        Returns:
            QueryListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("query", "list", params)
        # Cast generic envelope to concrete typed result
        return QueryListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )


