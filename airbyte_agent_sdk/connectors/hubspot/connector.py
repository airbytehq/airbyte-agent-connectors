"""
Hubspot connector.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import HubspotConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AssociationsCreateParams,
    AssociationsDeleteParams,
    AssociationsListParams,
    CallsCreateParams,
    CallsCreateParamsAssociationsItem,
    CallsCreateParamsProperties,
    CallsDeleteParams,
    CallsGetParams,
    CallsListParams,
    CallsUpdateParams,
    CallsUpdateParamsProperties,
    CompaniesApiSearchParams,
    CompaniesApiSearchParamsFiltergroupsItem,
    CompaniesApiSearchParamsSortsItem,
    CompaniesCreateParams,
    CompaniesCreateParamsProperties,
    CompaniesGetParams,
    CompaniesListParams,
    CompaniesUpdateParams,
    CompaniesUpdateParamsProperties,
    ContactsApiSearchParams,
    ContactsApiSearchParamsFiltergroupsItem,
    ContactsApiSearchParamsSortsItem,
    ContactsCreateParams,
    ContactsCreateParamsProperties,
    ContactsGetParams,
    ContactsListParams,
    ContactsUpdateParams,
    ContactsUpdateParamsProperties,
    DealsApiSearchParams,
    DealsApiSearchParamsFiltergroupsItem,
    DealsApiSearchParamsSortsItem,
    DealsCreateParams,
    DealsCreateParamsProperties,
    DealsGetParams,
    DealsListParams,
    DealsUpdateParams,
    DealsUpdateParamsProperties,
    EmailsCreateParams,
    EmailsCreateParamsAssociationsItem,
    EmailsCreateParamsProperties,
    EmailsDeleteParams,
    EmailsGetParams,
    EmailsListParams,
    EmailsUpdateParams,
    EmailsUpdateParamsProperties,
    MeetingsCreateParams,
    MeetingsCreateParamsAssociationsItem,
    MeetingsCreateParamsProperties,
    MeetingsDeleteParams,
    MeetingsGetParams,
    MeetingsListParams,
    MeetingsUpdateParams,
    MeetingsUpdateParamsProperties,
    NotesCreateParams,
    NotesCreateParamsAssociationsItem,
    NotesCreateParamsProperties,
    NotesDeleteParams,
    NotesGetParams,
    NotesListParams,
    NotesUpdateParams,
    NotesUpdateParamsProperties,
    ObjectsGetParams,
    ObjectsListParams,
    SchemasGetParams,
    SchemasListParams,
    TasksCreateParams,
    TasksCreateParamsAssociationsItem,
    TasksCreateParamsProperties,
    TasksDeleteParams,
    TasksGetParams,
    TasksListParams,
    TasksUpdateParams,
    TasksUpdateParamsProperties,
    TicketsApiSearchParams,
    TicketsApiSearchParamsFiltergroupsItem,
    TicketsApiSearchParamsSortsItem,
    TicketsCreateParams,
    TicketsCreateParamsProperties,
    TicketsGetParams,
    TicketsListParams,
    TicketsUpdateParams,
    TicketsUpdateParamsProperties,
    AirbyteSearchParams,
    CompaniesSearchFilter,
    CompaniesSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    DealsSearchFilter,
    DealsSearchQuery,
    TicketsSearchFilter,
    TicketsSearchQuery,
    NotesSearchFilter,
    NotesSearchQuery,
    CallsSearchFilter,
    CallsSearchQuery,
    EmailsSearchFilter,
    EmailsSearchQuery,
    MeetingsSearchFilter,
    MeetingsSearchQuery,
    TasksSearchFilter,
    TasksSearchQuery,
)
from .models import HubspotOauth2AuthConfig, HubspotPrivateAppAuthConfig
from .models import HubspotAuthConfig

# Import response models and envelope models at runtime
from .models import (
    HubspotCheckResult,
    HubspotExecuteResult,
    HubspotExecuteResultWithMeta,
    ContactsListResult,
    ContactsApiSearchResult,
    CompaniesListResult,
    CompaniesApiSearchResult,
    DealsListResult,
    DealsApiSearchResult,
    TicketsListResult,
    TicketsApiSearchResult,
    NotesListResult,
    CallsListResult,
    EmailsListResult,
    MeetingsListResult,
    TasksListResult,
    SchemasListResult,
    ObjectsListResult,
    AssociationsListResult,
    AssociationListResult,
    AssociationResult,
    CRMObject,
    Call,
    Company,
    Contact,
    Deal,
    Email,
    Meeting,
    Note,
    Schema,
    Task,
    Ticket,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CompaniesSearchData,
    CompaniesSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    DealsSearchData,
    DealsSearchResult,
    TicketsSearchData,
    TicketsSearchResult,
    NotesSearchData,
    NotesSearchResult,
    CallsSearchData,
    CallsSearchResult,
    EmailsSearchData,
    EmailsSearchResult,
    MeetingsSearchData,
    MeetingsSearchResult,
    TasksSearchData,
    TasksSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class HubspotConnector:
    """
    Type-safe Hubspot API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "hubspot"
    connector_version = "0.1.20"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("contacts", "list"): True,
        ("contacts", "create"): None,
        ("contacts", "get"): None,
        ("contacts", "update"): None,
        ("contacts", "api_search"): True,
        ("companies", "list"): True,
        ("companies", "create"): None,
        ("companies", "get"): None,
        ("companies", "update"): None,
        ("companies", "api_search"): True,
        ("deals", "list"): True,
        ("deals", "create"): None,
        ("deals", "get"): None,
        ("deals", "update"): None,
        ("deals", "api_search"): True,
        ("tickets", "list"): True,
        ("tickets", "create"): None,
        ("tickets", "get"): None,
        ("tickets", "update"): None,
        ("tickets", "api_search"): True,
        ("notes", "list"): True,
        ("notes", "create"): None,
        ("notes", "get"): None,
        ("notes", "update"): None,
        ("notes", "delete"): None,
        ("calls", "list"): True,
        ("calls", "create"): None,
        ("calls", "get"): None,
        ("calls", "update"): None,
        ("calls", "delete"): None,
        ("emails", "list"): True,
        ("emails", "create"): None,
        ("emails", "get"): None,
        ("emails", "update"): None,
        ("emails", "delete"): None,
        ("meetings", "list"): True,
        ("meetings", "create"): None,
        ("meetings", "get"): None,
        ("meetings", "update"): None,
        ("meetings", "delete"): None,
        ("tasks", "list"): True,
        ("tasks", "create"): None,
        ("tasks", "get"): None,
        ("tasks", "update"): None,
        ("tasks", "delete"): None,
        ("schemas", "list"): True,
        ("schemas", "get"): None,
        ("objects", "list"): True,
        ("objects", "get"): None,
        ("associations", "list"): True,
        ("associations", "create"): None,
        ("associations", "delete"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('contacts', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('contacts', 'create'): {'properties': 'properties'},
        ('contacts', 'get'): {'contact_id': 'contactId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('contacts', 'update'): {'properties': 'properties', 'contact_id': 'contactId'},
        ('contacts', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('companies', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('companies', 'create'): {'properties': 'properties'},
        ('companies', 'get'): {'company_id': 'companyId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('companies', 'update'): {'properties': 'properties', 'company_id': 'companyId'},
        ('companies', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('deals', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('deals', 'create'): {'properties': 'properties'},
        ('deals', 'get'): {'deal_id': 'dealId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('deals', 'update'): {'properties': 'properties', 'deal_id': 'dealId'},
        ('deals', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('tickets', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('tickets', 'create'): {'properties': 'properties'},
        ('tickets', 'get'): {'ticket_id': 'ticketId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('tickets', 'update'): {'properties': 'properties', 'ticket_id': 'ticketId'},
        ('tickets', 'api_search'): {'filter_groups': 'filterGroups', 'properties': 'properties', 'limit': 'limit', 'after': 'after', 'sorts': 'sorts', 'query': 'query'},
        ('notes', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('notes', 'create'): {'properties': 'properties', 'associations': 'associations'},
        ('notes', 'get'): {'note_id': 'noteId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('notes', 'update'): {'properties': 'properties', 'note_id': 'noteId'},
        ('notes', 'delete'): {'note_id': 'noteId'},
        ('calls', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('calls', 'create'): {'properties': 'properties', 'associations': 'associations'},
        ('calls', 'get'): {'call_id': 'callId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('calls', 'update'): {'properties': 'properties', 'call_id': 'callId'},
        ('calls', 'delete'): {'call_id': 'callId'},
        ('emails', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('emails', 'create'): {'properties': 'properties', 'associations': 'associations'},
        ('emails', 'get'): {'email_id': 'emailId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('emails', 'update'): {'properties': 'properties', 'email_id': 'emailId'},
        ('emails', 'delete'): {'email_id': 'emailId'},
        ('meetings', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('meetings', 'create'): {'properties': 'properties', 'associations': 'associations'},
        ('meetings', 'get'): {'meeting_id': 'meetingId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('meetings', 'update'): {'properties': 'properties', 'meeting_id': 'meetingId'},
        ('meetings', 'delete'): {'meeting_id': 'meetingId'},
        ('tasks', 'list'): {'limit': 'limit', 'after': 'after', 'associations': 'associations', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'archived': 'archived'},
        ('tasks', 'create'): {'properties': 'properties', 'associations': 'associations'},
        ('tasks', 'get'): {'task_id': 'taskId', 'properties': 'properties', 'properties_with_history': 'propertiesWithHistory', 'associations': 'associations', 'id_property': 'idProperty', 'archived': 'archived'},
        ('tasks', 'update'): {'properties': 'properties', 'task_id': 'taskId'},
        ('tasks', 'delete'): {'task_id': 'taskId'},
        ('schemas', 'list'): {'archived': 'archived'},
        ('schemas', 'get'): {'object_type': 'objectType'},
        ('objects', 'list'): {'object_type': 'objectType', 'limit': 'limit', 'after': 'after', 'properties': 'properties', 'archived': 'archived', 'associations': 'associations', 'properties_with_history': 'propertiesWithHistory'},
        ('objects', 'get'): {'object_type': 'objectType', 'object_id': 'objectId', 'properties': 'properties', 'archived': 'archived', 'associations': 'associations', 'id_property': 'idProperty', 'properties_with_history': 'propertiesWithHistory'},
        ('associations', 'list'): {'from_object_type': 'fromObjectType', 'from_object_id': 'fromObjectId', 'to_object_type': 'toObjectType', 'after': 'after', 'limit': 'limit'},
        ('associations', 'create'): {'association_category': 'associationCategory', 'association_type_id': 'associationTypeId', 'from_object_type': 'fromObjectType', 'from_object_id': 'fromObjectId', 'to_object_type': 'toObjectType', 'to_object_id': 'toObjectId'},
        ('associations', 'delete'): {'from_object_type': 'fromObjectType', 'from_object_id': 'fromObjectId', 'to_object_type': 'toObjectType', 'to_object_id': 'toObjectId'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (HubspotOauth2AuthConfig, HubspotPrivateAppAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: HubspotAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new hubspot connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., HubspotAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = HubspotConnector(auth_config=HubspotAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = HubspotConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = HubspotConnector(
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
                connector_definition_id=str(HubspotConnectorModel.id),
                model=HubspotConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or HubspotAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, HubspotOauth2AuthConfig):
                    auth_scheme = "oauth2"
                if isinstance(auth_config, HubspotPrivateAppAuthConfig):
                    auth_scheme = "hubspotPrivateApp"

            self._executor = LocalExecutor(
                model=HubspotConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.contacts = ContactsQuery(self)
        self.companies = CompaniesQuery(self)
        self.deals = DealsQuery(self)
        self.tickets = TicketsQuery(self)
        self.notes = NotesQuery(self)
        self.calls = CallsQuery(self)
        self.emails = EmailsQuery(self)
        self.meetings = MeetingsQuery(self)
        self.tasks = TasksQuery(self)
        self.schemas = SchemasQuery(self)
        self.objects = ObjectsQuery(self)
        self.associations = AssociationsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
    ) -> "Contact": ...

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
    ) -> "Contact": ...

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
        entity: Literal["companies"],
        action: Literal["list"],
        params: "CompaniesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CompaniesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["create"],
        params: "CompaniesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Company": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["get"],
        params: "CompaniesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Company": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["update"],
        params: "CompaniesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Company": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["api_search"],
        params: "CompaniesApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CompaniesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["list"],
        params: "DealsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DealsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["create"],
        params: "DealsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Deal": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["get"],
        params: "DealsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Deal": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["update"],
        params: "DealsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Deal": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["api_search"],
        params: "DealsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DealsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["list"],
        params: "TicketsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TicketsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["create"],
        params: "TicketsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Ticket": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["get"],
        params: "TicketsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Ticket": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["update"],
        params: "TicketsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Ticket": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["api_search"],
        params: "TicketsApiSearchParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TicketsApiSearchResult": ...

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
    ) -> "Note": ...

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
    ) -> "Note": ...

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
        entity: Literal["calls"],
        action: Literal["list"],
        params: "CallsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CallsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["create"],
        params: "CallsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Call": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["get"],
        params: "CallsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Call": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["update"],
        params: "CallsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Call": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["delete"],
        params: "CallsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["emails"],
        action: Literal["list"],
        params: "EmailsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "EmailsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["emails"],
        action: Literal["create"],
        params: "EmailsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Email": ...

    @overload
    async def execute(
        self,
        entity: Literal["emails"],
        action: Literal["get"],
        params: "EmailsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Email": ...

    @overload
    async def execute(
        self,
        entity: Literal["emails"],
        action: Literal["update"],
        params: "EmailsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Email": ...

    @overload
    async def execute(
        self,
        entity: Literal["emails"],
        action: Literal["delete"],
        params: "EmailsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["meetings"],
        action: Literal["list"],
        params: "MeetingsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MeetingsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["meetings"],
        action: Literal["create"],
        params: "MeetingsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Meeting": ...

    @overload
    async def execute(
        self,
        entity: Literal["meetings"],
        action: Literal["get"],
        params: "MeetingsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Meeting": ...

    @overload
    async def execute(
        self,
        entity: Literal["meetings"],
        action: Literal["update"],
        params: "MeetingsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Meeting": ...

    @overload
    async def execute(
        self,
        entity: Literal["meetings"],
        action: Literal["delete"],
        params: "MeetingsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...

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
    ) -> "Task": ...

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
    ) -> "Task": ...

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
        entity: Literal["schemas"],
        action: Literal["list"],
        params: "SchemasListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SchemasListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["schemas"],
        action: Literal["get"],
        params: "SchemasGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Schema": ...

    @overload
    async def execute(
        self,
        entity: Literal["objects"],
        action: Literal["list"],
        params: "ObjectsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ObjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["objects"],
        action: Literal["get"],
        params: "ObjectsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CRMObject": ...

    @overload
    async def execute(
        self,
        entity: Literal["associations"],
        action: Literal["list"],
        params: "AssociationsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AssociationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["associations"],
        action: Literal["create"],
        params: "AssociationsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AssociationResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["associations"],
        action: Literal["delete"],
        params: "AssociationsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "dict[str, Any]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "api_search", "delete", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> HubspotExecuteResult[Any] | HubspotExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update", "api_search", "delete", "context_store_search"],
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
                return HubspotExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return HubspotExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> HubspotCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            HubspotCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return HubspotCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return HubspotCheckResult(
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

        connector = HubspotConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @HubspotConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @HubspotConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @HubspotConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
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
                    HubspotConnectorModel,
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
        return describe_entities(HubspotConnectorModel)

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
            (e for e in HubspotConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in HubspotConnectorModel.entities]}"
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



class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a paginated list of contacts

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
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
        properties: ContactsCreateParamsProperties,
        **kwargs
    ) -> Contact:
        """
        Create a new contact in HubSpot CRM with the provided properties.

        Args:
            properties: Contact properties to set
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "create", params)
        return result



    async def get(
        self,
        contact_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID

        Args:
            contact_id: Contact ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "contactId": contact_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



    async def update(
        self,
        properties: ContactsUpdateParamsProperties,
        contact_id: str,
        **kwargs
    ) -> Contact:
        """
        Update an existing contact's properties by ID. Only the specified properties will be updated.

        Args:
            properties: Contact properties to update
            contact_id: Contact ID
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "properties": properties,
            "contactId": contact_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "update", params)
        return result



    async def api_search(
        self,
        filter_groups: list[ContactsApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[ContactsApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> ContactsApiSearchResult:
        """
        Search for contacts by filtering on properties, searching through associations, and sorting results.

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            ContactsApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ContactsApiSearchResult(
            data=result.data,
            meta=getattr(result, "meta", None)
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
        - archived: Boolean flag indicating whether the contact has been archived or deleted
        - companies: Associated company records linked to this contact
        - created_at: Timestamp indicating when the contact was first created in the system
        - id: Unique identifier for the contact record
        - properties: Key-value object storing all contact properties and their values.
        - properties_associatedcompanyid: ID of the associated company
        - properties_createdate: Date the contact was created
        - properties_email: Contact email address
        - properties_firstname: Contact first name
        - properties_hs_object_id: HubSpot object ID
        - properties_hubspot_owner_id: ID of the HubSpot owner assigned to this contact
        - properties_lastmodifieddate: Last modified date of the contact
        - properties_lastname: Contact last name
        - updated_at: Timestamp indicating when the contact record was last modified

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

class CompaniesQuery:
    """
    Query class for Companies entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> CompaniesListResult:
        """
        Retrieve all companies, using query parameters to control the information that gets returned.

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            CompaniesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "list", params)
        # Cast generic envelope to concrete typed result
        return CompaniesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        properties: CompaniesCreateParamsProperties,
        **kwargs
    ) -> Company:
        """
        Create a new company in HubSpot CRM with the provided properties.

        Args:
            properties: Company properties to set
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "create", params)
        return result



    async def get(
        self,
        company_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Company:
        """
        Get a single company by ID

        Args:
            company_id: Company ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "companyId": company_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "get", params)
        return result



    async def update(
        self,
        properties: CompaniesUpdateParamsProperties,
        company_id: str,
        **kwargs
    ) -> Company:
        """
        Update an existing company's properties by ID. Only the specified properties will be updated.

        Args:
            properties: Company properties to update
            company_id: Company ID
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "properties": properties,
            "companyId": company_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "update", params)
        return result



    async def api_search(
        self,
        filter_groups: list[CompaniesApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[CompaniesApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> CompaniesApiSearchResult:
        """
        Search for companies by filtering on properties, searching through associations, and sorting results.

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            CompaniesApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CompaniesApiSearchResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: CompaniesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CompaniesSearchResult:
        """
        Search companies records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CompaniesSearchFilter):
        - archived: Indicates whether the company has been deleted and moved to the recycling bin
        - contacts: Associated contact records linked to this company
        - created_at: Timestamp when the company record was created
        - id: Unique identifier for the company record
        - properties: Object containing all property values for the company
        - properties_createdate: Date the company was created
        - properties_domain: Company domain name
        - properties_hs_lastmodifieddate: Last modified date of the company
        - properties_hs_object_id: HubSpot object ID
        - properties_hubspot_owner_id: ID of the HubSpot owner assigned to this company
        - properties_name: Company name
        - updated_at: Timestamp when the company record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CompaniesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("companies", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CompaniesSearchResult(
            data=[
                CompaniesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DealsQuery:
    """
    Query class for Deals entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> DealsListResult:
        """
        Returns a paginated list of deals

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            DealsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "list", params)
        # Cast generic envelope to concrete typed result
        return DealsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        properties: DealsCreateParamsProperties,
        **kwargs
    ) -> Deal:
        """
        Create a new deal in HubSpot CRM with the provided properties.

        Args:
            properties: Deal properties to set
            **kwargs: Additional parameters

        Returns:
            Deal
        """
        params = {k: v for k, v in {
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "create", params)
        return result



    async def get(
        self,
        deal_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Deal:
        """
        Get a single deal by ID

        Args:
            deal_id: Deal ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Deal
        """
        params = {k: v for k, v in {
            "dealId": deal_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "get", params)
        return result



    async def update(
        self,
        properties: DealsUpdateParamsProperties,
        deal_id: str,
        **kwargs
    ) -> Deal:
        """
        Update an existing deal's properties by ID. Only the specified properties will be updated.

        Args:
            properties: Deal properties to update
            deal_id: Deal ID
            **kwargs: Additional parameters

        Returns:
            Deal
        """
        params = {k: v for k, v in {
            "properties": properties,
            "dealId": deal_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "update", params)
        return result



    async def api_search(
        self,
        filter_groups: list[DealsApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[DealsApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> DealsApiSearchResult:
        """
        Search deals with filters and sorting

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            DealsApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "api_search", params)
        # Cast generic envelope to concrete typed result
        return DealsApiSearchResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: DealsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DealsSearchResult:
        """
        Search deals records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DealsSearchFilter):
        - archived: Indicates whether the deal has been deleted and moved to the recycling bin
        - companies: Collection of company records associated with the deal
        - contacts: Collection of contact records associated with the deal
        - created_at: Timestamp when the deal record was originally created
        - id: Unique identifier for the deal record
        - line_items: Collection of product line items associated with the deal
        - properties: Key-value object containing all deal properties and custom fields
        - properties_amount: Deal amount
        - properties_closedate: Expected close date of the deal
        - properties_createdate: Date the deal was created
        - properties_dealname: Deal name
        - properties_dealstage: Current deal stage
        - properties_hs_lastmodifieddate: Last modified date of the deal
        - properties_hs_object_id: HubSpot object ID
        - properties_hubspot_owner_id: ID of the HubSpot owner assigned to this deal
        - properties_pipeline: Deal pipeline
        - updated_at: Timestamp when the deal record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DealsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("deals", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DealsSearchResult(
            data=[
                DealsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TicketsQuery:
    """
    Query class for Tickets entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> TicketsListResult:
        """
        Returns a paginated list of tickets

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, deals, tickets, and custom object type IDs or fully qualified names (e.g., "p12345_cars").
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of companies that can be read by a single request.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            TicketsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        properties: TicketsCreateParamsProperties,
        **kwargs
    ) -> Ticket:
        """
        Create a new support ticket in HubSpot CRM with the provided properties.

        Args:
            properties: Ticket properties to set
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "create", params)
        return result



    async def get(
        self,
        ticket_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Ticket:
        """
        Get a single ticket by ID

        Args:
            ticket_id: Ticket ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "ticketId": ticket_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "get", params)
        return result



    async def update(
        self,
        properties: TicketsUpdateParamsProperties,
        ticket_id: str,
        **kwargs
    ) -> Ticket:
        """
        Update an existing ticket's properties by ID. Only the specified properties will be updated.

        Args:
            properties: Ticket properties to update
            ticket_id: Ticket ID
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "properties": properties,
            "ticketId": ticket_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "update", params)
        return result



    async def api_search(
        self,
        filter_groups: list[TicketsApiSearchParamsFiltergroupsItem] | None = None,
        properties: list[str] | None = None,
        limit: int | None = None,
        after: str | None = None,
        sorts: list[TicketsApiSearchParamsSortsItem] | None = None,
        query: str | None = None,
        **kwargs
    ) -> TicketsApiSearchResult:
        """
        Search for tickets by filtering on properties, searching through associations, and sorting results.

        Args:
            filter_groups: Up to 6 groups of filters defining additional query criteria.
            properties: A list of property names to include in the response.
            limit: Maximum number of results to return
            after: A paging cursor token for retrieving subsequent pages.
            sorts: Sort criteria
            query: The search query string, up to 3000 characters.
            **kwargs: Additional parameters

        Returns:
            TicketsApiSearchResult
        """
        params = {k: v for k, v in {
            "filterGroups": filter_groups,
            "properties": properties,
            "limit": limit,
            "after": after,
            "sorts": sorts,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "api_search", params)
        # Cast generic envelope to concrete typed result
        return TicketsApiSearchResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: TicketsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TicketsSearchResult:
        """
        Search tickets records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TicketsSearchFilter):
        - archived: Indicates whether the ticket has been deleted and moved to the recycling bin
        - companies: Collection of company records associated with the ticket
        - contacts: Collection of contact records associated with the ticket
        - created_at: Timestamp when the ticket record was originally created
        - id: Unique identifier for the ticket record
        - properties: Object containing all property values for the ticket
        - properties_content: Ticket content/description
        - properties_createdate: Date the ticket was created
        - properties_hs_lastmodifieddate: Last modified date of the ticket
        - properties_hs_object_id: HubSpot object ID
        - properties_hs_pipeline: Ticket pipeline
        - properties_hs_pipeline_stage: Current pipeline stage of the ticket
        - properties_hs_ticket_category: Ticket category
        - properties_hs_ticket_priority: Ticket priority level
        - properties_subject: Ticket subject line
        - updated_at: Timestamp when the ticket record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TicketsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tickets", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TicketsSearchResult(
            data=[
                TicketsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class NotesQuery:
    """
    Query class for Notes entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> NotesListResult:
        """
        Returns a paginated list of notes

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, companies, deals, tickets, and custom object type IDs or fully qualified names.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            NotesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
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
        properties: NotesCreateParamsProperties,
        associations: list[NotesCreateParamsAssociationsItem] | None = None,
        **kwargs
    ) -> Note:
        """
        Create a new note in HubSpot CRM. Notes can be associated with contacts,
companies, deals, or tickets by using the associations parameter.
The hs_timestamp property sets when the note activity occurred.


        Args:
            properties: Note properties to set
            associations: Associate the note with other CRM records (contacts, companies, deals, tickets)
            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "properties": properties,
            "associations": associations,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "create", params)
        return result



    async def get(
        self,
        note_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Note:
        """
        Get a single note by ID

        Args:
            note_id: Note ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "noteId": note_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "get", params)
        return result



    async def update(
        self,
        properties: NotesUpdateParamsProperties,
        note_id: str,
        **kwargs
    ) -> Note:
        """
        Update an existing note's properties by ID.

        Args:
            properties: Note properties to update
            note_id: Note ID
            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "properties": properties,
            "noteId": note_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "update", params)
        return result



    async def delete(
        self,
        note_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Archive a note by ID. This is a soft delete — the note is moved to the
recycle bin and can be restored for approximately 90 days. No public
hard-delete endpoint exists.


        Args:
            note_id: Note ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "noteId": note_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "delete", params)
        return result



    async def context_store_search(
        self,
        query: NotesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> NotesSearchResult:
        """
        Search notes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (NotesSearchFilter):
        - archived: Indicates whether the note has been archived
        - created_at: Timestamp when the note was created
        - id: Unique identifier for the note record
        - properties: Object containing all property values for the note
        - properties_hs_createdate: Date the note was created
        - properties_hs_lastmodifieddate: Last modified date of the note
        - properties_hs_note_body: The body content of the note (supports HTML)
        - properties_hs_object_id: HubSpot object ID
        - properties_hs_timestamp: Timestamp when the note activity occurred
        - properties_hubspot_owner_id: ID of the note owner
        - updated_at: Timestamp when the note record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            NotesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("notes", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return NotesSearchResult(
            data=[
                NotesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CallsQuery:
    """
    Query class for Calls entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> CallsListResult:
        """
        Returns a paginated list of calls

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, companies, deals, tickets, and custom object type IDs or fully qualified names.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            CallsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "list", params)
        # Cast generic envelope to concrete typed result
        return CallsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        properties: CallsCreateParamsProperties,
        associations: list[CallsCreateParamsAssociationsItem] | None = None,
        **kwargs
    ) -> Call:
        """
        Create a new call engagement in HubSpot CRM. Calls can be associated with contacts,
companies, deals, or tickets by using the associations parameter.
The hs_timestamp property sets when the call activity occurred.


        Args:
            properties: Call properties to set
            associations: Associate the call with other CRM records (contacts, companies, deals, tickets)
            **kwargs: Additional parameters

        Returns:
            Call
        """
        params = {k: v for k, v in {
            "properties": properties,
            "associations": associations,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "create", params)
        return result



    async def get(
        self,
        call_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Call:
        """
        Get a single call by ID

        Args:
            call_id: Call ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Call
        """
        params = {k: v for k, v in {
            "callId": call_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "get", params)
        return result



    async def update(
        self,
        properties: CallsUpdateParamsProperties,
        call_id: str,
        **kwargs
    ) -> Call:
        """
        Update an existing call's properties by ID.

        Args:
            properties: Call properties to update
            call_id: Call ID
            **kwargs: Additional parameters

        Returns:
            Call
        """
        params = {k: v for k, v in {
            "properties": properties,
            "callId": call_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "update", params)
        return result



    async def delete(
        self,
        call_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Archive a call by ID. This is a soft delete — the call is moved to the
recycle bin and can be restored for approximately 90 days. No public
hard-delete endpoint exists.


        Args:
            call_id: Call ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "callId": call_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "delete", params)
        return result



    async def context_store_search(
        self,
        query: CallsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CallsSearchResult:
        """
        Search calls records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CallsSearchFilter):
        - archived: Indicates whether the call has been archived
        - created_at: Timestamp when the call was created
        - id: Unique identifier for the call record
        - properties: Object containing all property values for the call
        - properties_hs_call_body: Description or notes about the call
        - properties_hs_call_direction: Direction of the call (INBOUND or OUTBOUND)
        - properties_hs_call_duration: Duration of the call in milliseconds
        - properties_hs_call_status: Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)
        - properties_hs_call_title: Title or subject of the call
        - properties_hs_createdate: Date the call was created
        - properties_hs_lastmodifieddate: Last modified date of the call
        - properties_hs_object_id: HubSpot object ID
        - properties_hs_timestamp: Timestamp when the call activity occurred
        - properties_hubspot_owner_id: ID of the call owner
        - updated_at: Timestamp when the call record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CallsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("calls", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CallsSearchResult(
            data=[
                CallsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class EmailsQuery:
    """
    Query class for Emails entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> EmailsListResult:
        """
        Returns a paginated list of emails

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, companies, deals, tickets, and custom object type IDs or fully qualified names.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            EmailsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("emails", "list", params)
        # Cast generic envelope to concrete typed result
        return EmailsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        properties: EmailsCreateParamsProperties,
        associations: list[EmailsCreateParamsAssociationsItem] | None = None,
        **kwargs
    ) -> Email:
        """
        Create a new email engagement in HubSpot CRM. Emails can be associated with contacts,
companies, deals, or tickets by using the associations parameter.
The hs_timestamp property sets when the email activity occurred.


        Args:
            properties: Email properties to set
            associations: Associate the email with other CRM records (contacts, companies, deals, tickets)
            **kwargs: Additional parameters

        Returns:
            Email
        """
        params = {k: v for k, v in {
            "properties": properties,
            "associations": associations,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("emails", "create", params)
        return result



    async def get(
        self,
        email_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Email:
        """
        Get a single email by ID

        Args:
            email_id: Email ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Email
        """
        params = {k: v for k, v in {
            "emailId": email_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("emails", "get", params)
        return result



    async def update(
        self,
        properties: EmailsUpdateParamsProperties,
        email_id: str,
        **kwargs
    ) -> Email:
        """
        Update an existing email's properties by ID.

        Args:
            properties: Email properties to update
            email_id: Email ID
            **kwargs: Additional parameters

        Returns:
            Email
        """
        params = {k: v for k, v in {
            "properties": properties,
            "emailId": email_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("emails", "update", params)
        return result



    async def delete(
        self,
        email_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Archive an email by ID. This is a soft delete — the email is moved to the
recycle bin and can be restored for approximately 90 days. No public
hard-delete endpoint exists.


        Args:
            email_id: Email ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "emailId": email_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("emails", "delete", params)
        return result



    async def context_store_search(
        self,
        query: EmailsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EmailsSearchResult:
        """
        Search emails records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EmailsSearchFilter):
        - archived: Indicates whether the email has been archived
        - created_at: Timestamp when the email was created
        - id: Unique identifier for the email record
        - properties: Object containing all property values for the email
        - properties_hs_createdate: Date the email was created
        - properties_hs_email_direction: Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)
        - properties_hs_email_status: Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)
        - properties_hs_email_subject: Subject line of the email
        - properties_hs_email_text: Plain text body of the email
        - properties_hs_lastmodifieddate: Last modified date of the email
        - properties_hs_object_id: HubSpot object ID
        - properties_hs_timestamp: Timestamp when the email activity occurred
        - properties_hubspot_owner_id: ID of the email owner
        - updated_at: Timestamp when the email record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EmailsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("emails", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EmailsSearchResult(
            data=[
                EmailsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MeetingsQuery:
    """
    Query class for Meetings entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> MeetingsListResult:
        """
        Returns a paginated list of meetings

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, companies, deals, tickets, and custom object type IDs or fully qualified names.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            MeetingsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("meetings", "list", params)
        # Cast generic envelope to concrete typed result
        return MeetingsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        properties: MeetingsCreateParamsProperties,
        associations: list[MeetingsCreateParamsAssociationsItem] | None = None,
        **kwargs
    ) -> Meeting:
        """
        Create a new meeting engagement in HubSpot CRM. Meetings can be associated with contacts,
companies, deals, or tickets by using the associations parameter.
The hs_timestamp property sets when the meeting activity occurred.


        Args:
            properties: Meeting properties to set
            associations: Associate the meeting with other CRM records (contacts, companies, deals, tickets)
            **kwargs: Additional parameters

        Returns:
            Meeting
        """
        params = {k: v for k, v in {
            "properties": properties,
            "associations": associations,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("meetings", "create", params)
        return result



    async def get(
        self,
        meeting_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Meeting:
        """
        Get a single meeting by ID

        Args:
            meeting_id: Meeting ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Meeting
        """
        params = {k: v for k, v in {
            "meetingId": meeting_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("meetings", "get", params)
        return result



    async def update(
        self,
        properties: MeetingsUpdateParamsProperties,
        meeting_id: str,
        **kwargs
    ) -> Meeting:
        """
        Update an existing meeting's properties by ID.

        Args:
            properties: Meeting properties to update
            meeting_id: Meeting ID
            **kwargs: Additional parameters

        Returns:
            Meeting
        """
        params = {k: v for k, v in {
            "properties": properties,
            "meetingId": meeting_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("meetings", "update", params)
        return result



    async def delete(
        self,
        meeting_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Archive a meeting by ID. This is a soft delete — the meeting is moved to the
recycle bin and can be restored for approximately 90 days. No public
hard-delete endpoint exists.


        Args:
            meeting_id: Meeting ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "meetingId": meeting_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("meetings", "delete", params)
        return result



    async def context_store_search(
        self,
        query: MeetingsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MeetingsSearchResult:
        """
        Search meetings records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MeetingsSearchFilter):
        - archived: Indicates whether the meeting has been archived
        - created_at: Timestamp when the meeting was created
        - id: Unique identifier for the meeting record
        - properties: Object containing all property values for the meeting
        - properties_hs_createdate: Date the meeting was created
        - properties_hs_lastmodifieddate: Last modified date of the meeting
        - properties_hs_meeting_body: Description or notes about the meeting
        - properties_hs_meeting_end_time: End time of the meeting
        - properties_hs_meeting_location: Location of the meeting
        - properties_hs_meeting_outcome: Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)
        - properties_hs_meeting_start_time: Start time of the meeting
        - properties_hs_meeting_title: Title of the meeting
        - properties_hs_object_id: HubSpot object ID
        - properties_hs_timestamp: Timestamp when the meeting activity occurred
        - properties_hubspot_owner_id: ID of the meeting owner
        - updated_at: Timestamp when the meeting record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MeetingsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("meetings", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MeetingsSearchResult(
            data=[
                MeetingsSearchData(**row)
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

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        after: str | None = None,
        associations: str | None = None,
        properties: str | None = None,
        properties_with_history: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> TasksListResult:
        """
        Returns a paginated list of tasks

        Args:
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the paging.next.after JSON property of a paged response containing more results.
            associations: A comma separated list of associated object types to include in the response. Valid values are contacts, companies, deals, tickets, and custom object type IDs or fully qualified names.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "associations": associations,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "archived": archived,
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
        properties: TasksCreateParamsProperties,
        associations: list[TasksCreateParamsAssociationsItem] | None = None,
        **kwargs
    ) -> Task:
        """
        Create a new task in HubSpot CRM. Tasks can be associated with contacts,
companies, deals, or tickets by using the associations parameter.
The hs_timestamp property sets when the task activity occurred.


        Args:
            properties: Task properties to set
            associations: Associate the task with other CRM records (contacts, companies, deals, tickets)
            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "properties": properties,
            "associations": associations,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "create", params)
        return result



    async def get(
        self,
        task_id: str,
        properties: str | None = None,
        properties_with_history: str | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Task:
        """
        Get a single task by ID

        Args:
            task_id: Task ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "taskId": task_id,
            "properties": properties,
            "propertiesWithHistory": properties_with_history,
            "associations": associations,
            "idProperty": id_property,
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def update(
        self,
        properties: TasksUpdateParamsProperties,
        task_id: str,
        **kwargs
    ) -> Task:
        """
        Update an existing task's properties by ID.

        Args:
            properties: Task properties to update
            task_id: Task ID
            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "properties": properties,
            "taskId": task_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "update", params)
        return result



    async def delete(
        self,
        task_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Archive a task by ID. This is a soft delete — the task is moved to the
recycle bin and can be restored for approximately 90 days. No public
hard-delete endpoint exists.


        Args:
            task_id: Task ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "taskId": task_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "delete", params)
        return result



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
        - archived: Indicates whether the task has been archived
        - created_at: Timestamp when the task was created
        - id: Unique identifier for the task record
        - properties: Object containing all property values for the task
        - properties_hs_createdate: Date the task was created
        - properties_hs_lastmodifieddate: Last modified date of the task
        - properties_hs_object_id: HubSpot object ID
        - properties_hs_task_body: Description or notes for the task
        - properties_hs_task_priority: Priority of the task (LOW, MEDIUM, HIGH)
        - properties_hs_task_status: Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)
        - properties_hs_task_subject: Subject or title of the task
        - properties_hs_task_type: Type of the task (TODO, CALL, EMAIL)
        - properties_hs_timestamp: Due date / timestamp for the task
        - properties_hubspot_owner_id: ID of the task owner
        - updated_at: Timestamp when the task record was last modified

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

class SchemasQuery:
    """
    Query class for Schemas entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        archived: bool | None = None,
        **kwargs
    ) -> SchemasListResult:
        """
        Returns all custom object schemas to discover available custom objects

        Args:
            archived: Whether to return only results that have been archived.
            **kwargs: Additional parameters

        Returns:
            SchemasListResult
        """
        params = {k: v for k, v in {
            "archived": archived,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schemas", "list", params)
        # Cast generic envelope to concrete typed result
        return SchemasListResult(
            data=result.data
        )



    async def get(
        self,
        object_type: str,
        **kwargs
    ) -> Schema:
        """
        Get the schema for a specific custom object type

        Args:
            object_type: Fully qualified name or object type ID of your schema.
            **kwargs: Additional parameters

        Returns:
            Schema
        """
        params = {k: v for k, v in {
            "objectType": object_type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schemas", "get", params)
        return result



class ObjectsQuery:
    """
    Query class for Objects entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        object_type: str,
        limit: int | None = None,
        after: str | None = None,
        properties: str | None = None,
        archived: bool | None = None,
        associations: str | None = None,
        properties_with_history: str | None = None,
        **kwargs
    ) -> ObjectsListResult:
        """
        Read a page of objects. Control what is returned via the properties query param.

        Args:
            object_type: Object type ID or fully qualified name (e.g., "cars" or "p12345_cars")
            limit: The maximum number of results to display per page.
            after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            **kwargs: Additional parameters

        Returns:
            ObjectsListResult
        """
        params = {k: v for k, v in {
            "objectType": object_type,
            "limit": limit,
            "after": after,
            "properties": properties,
            "archived": archived,
            "associations": associations,
            "propertiesWithHistory": properties_with_history,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("objects", "list", params)
        # Cast generic envelope to concrete typed result
        return ObjectsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        object_type: str,
        object_id: str,
        properties: str | None = None,
        archived: bool | None = None,
        associations: str | None = None,
        id_property: str | None = None,
        properties_with_history: str | None = None,
        **kwargs
    ) -> CRMObject:
        """
        Read an Object identified by {objectId}. {objectId} refers to the internal object ID by default, or optionally any unique property value as specified by the idProperty query param. Control what is returned via the properties query param.

        Args:
            object_type: Object type ID or fully qualified name
            object_id: Object record ID
            properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
            archived: Whether to return only results that have been archived.
            associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
            id_property: The name of a property whose values are unique for this object.
            properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
            **kwargs: Additional parameters

        Returns:
            CRMObject
        """
        params = {k: v for k, v in {
            "objectType": object_type,
            "objectId": object_id,
            "properties": properties,
            "archived": archived,
            "associations": associations,
            "idProperty": id_property,
            "propertiesWithHistory": properties_with_history,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("objects", "get", params)
        return result



class AssociationsQuery:
    """
    Query class for Associations entity operations.
    """

    def __init__(self, connector: HubspotConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        after: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> AssociationsListResult:
        """
        Retrieve all associations between a specific CRM record and a target object type using
the v4 associations API. Returns up to 500 associations per call. Use the `after` cursor
for pagination when there are more results. For example, retrieve all companies associated
with a contact, or all deals associated with a company.


        Args:
            from_object_type: Object type of the source record (e.g., contacts, companies, deals, tickets, or a custom object type ID)
            from_object_id: ID of the source record to retrieve associations for
            to_object_type: Object type of the target records to retrieve (e.g., contacts, companies, deals, tickets, or a custom object type ID)
            after: Paging cursor token from a previous response for retrieving subsequent pages of results
            limit: Maximum number of results to return per page (default 500, max 500)
            **kwargs: Additional parameters

        Returns:
            AssociationsListResult
        """
        params = {k: v for k, v in {
            "fromObjectType": from_object_type,
            "fromObjectId": from_object_id,
            "toObjectType": to_object_type,
            "after": after,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("associations", "list", params)
        # Cast generic envelope to concrete typed result
        return AssociationsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        association_category: str,
        association_type_id: int,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        to_object_id: str,
        **kwargs
    ) -> AssociationResult:
        """
        Create a labeled association between two CRM records using the v4 associations API.
Labeled associations carry an association type ID and category that describe the relationship
(e.g., "Primary Company", "Billing Contact"). This is idempotent — calling it again with the same
IDs and label has no effect. Use the association type ID and category from the HubSpot association
definitions for the relevant object pair. Common association type IDs include:
- Contact to Company: 279 (HUBSPOT_DEFINED) for default, 1 (HUBSPOT_DEFINED) for Primary
- Company to Contact: 280 (HUBSPOT_DEFINED) for default, 2 (HUBSPOT_DEFINED) for Primary
- Contact to Deal: 4 (HUBSPOT_DEFINED) for default
- Deal to Contact: 3 (HUBSPOT_DEFINED) for default
- Deal to Company: 341 (HUBSPOT_DEFINED) for default, 5 (HUBSPOT_DEFINED) for Primary
- Company to Deal: 342 (HUBSPOT_DEFINED) for default, 6 (HUBSPOT_DEFINED) for Primary
- Contact to Ticket: 15 (HUBSPOT_DEFINED) for default
- Ticket to Contact: 16 (HUBSPOT_DEFINED) for default
- Ticket to Company: 339 (HUBSPOT_DEFINED) for default, 26 (HUBSPOT_DEFINED) for Primary
- Company to Ticket: 340 (HUBSPOT_DEFINED) for default, 25 (HUBSPOT_DEFINED) for Primary


        Args:
            association_category: Category of the association type. Use HUBSPOT_DEFINED for standard HubSpot association
types (e.g., primary company, default contact-to-deal) or USER_DEFINED for custom
association labels created in your HubSpot portal.

            association_type_id: Numeric identifier for the association type. Common IDs include:
279 = Contact to Company (default), 280 = Company to Contact (default),
4 = Contact to Deal (default), 3 = Deal to Contact (default),
341 = Deal to Company (default), 342 = Company to Deal (default),
1 = Contact to Primary Company, 2 = Company to Primary Contact,
5 = Deal to Primary Company, 6 = Primary Company to Deal,
15 = Contact to Ticket (default), 16 = Ticket to Contact (default),
339 = Ticket to Company (default), 340 = Company to Ticket (default),
26 = Ticket to Primary Company, 25 = Primary Company to Ticket.
Use the association definitions API to discover additional type IDs.

            from_object_type: Object type of the source record (e.g., contacts, companies, deals, tickets, or a custom object type ID)
            from_object_id: ID of the source record to associate from
            to_object_type: Object type of the target record (e.g., contacts, companies, deals, tickets, or a custom object type ID)
            to_object_id: ID of the target record to associate to
            **kwargs: Additional parameters

        Returns:
            AssociationResult
        """
        params = {k: v for k, v in {
            "associationCategory": association_category,
            "associationTypeId": association_type_id,
            "fromObjectType": from_object_type,
            "fromObjectId": from_object_id,
            "toObjectType": to_object_type,
            "toObjectId": to_object_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("associations", "create", params)
        return result



    async def delete(
        self,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        to_object_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Delete all associations between two specific CRM records using the v4 associations API.
This removes every association (both default and labeled) between the two specified records.
This operation is irreversible — deleted associations must be recreated manually.


        Args:
            from_object_type: Object type of the source record (e.g., contacts, companies, deals, tickets, or a custom object type ID)
            from_object_id: ID of the source record
            to_object_type: Object type of the target record (e.g., contacts, companies, deals, tickets, or a custom object type ID)
            to_object_id: ID of the target record
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "fromObjectType": from_object_type,
            "fromObjectId": from_object_id,
            "toObjectType": to_object_type,
            "toObjectId": to_object_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("associations", "delete", params)
        return result


