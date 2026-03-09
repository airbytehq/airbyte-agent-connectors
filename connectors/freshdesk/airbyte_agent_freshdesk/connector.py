"""
Freshdesk connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import FreshdeskConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AgentsGetParams,
    AgentsListParams,
    CompaniesGetParams,
    CompaniesListParams,
    ContactsGetParams,
    ContactsListParams,
    GroupsGetParams,
    GroupsListParams,
    RolesGetParams,
    RolesListParams,
    SatisfactionRatingsListParams,
    SurveysListParams,
    TicketFieldsListParams,
    TicketsGetParams,
    TicketsListParams,
    TimeEntriesListParams,
    AirbyteSearchParams,
    TicketsSearchFilter,
    TicketsSearchQuery,
    AgentsSearchFilter,
    AgentsSearchQuery,
    GroupsSearchFilter,
    GroupsSearchQuery,
)
from .models import FreshdeskAuthConfig

# Import response models and envelope models at runtime
from .models import (
    FreshdeskCheckResult,
    FreshdeskExecuteResult,
    FreshdeskExecuteResultWithMeta,
    TicketsListResult,
    ContactsListResult,
    AgentsListResult,
    GroupsListResult,
    CompaniesListResult,
    RolesListResult,
    SatisfactionRatingsListResult,
    SurveysListResult,
    TimeEntriesListResult,
    TicketFieldsListResult,
    Agent,
    Company,
    Contact,
    Group,
    Role,
    SatisfactionRating,
    Survey,
    Ticket,
    TicketField,
    TimeEntry,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    TicketsSearchData,
    TicketsSearchResult,
    AgentsSearchData,
    AgentsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 50_000  # ~50KB default, configurable per-tool


def _raise_output_too_large(message: str) -> None:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except Exception as exc:
        raise RuntimeError(message) from exc
    raise ModelRetry(message)


def _check_output_size(result: Any, max_chars: int | None, tool_name: str) -> Any:
    if max_chars is None or max_chars <= 0:
        return result

    try:
        serialized = json.dumps(result, default=str)
    except (TypeError, ValueError):
        return result

    if len(serialized) > max_chars:
        truncated_preview = serialized[:500] + "..." if len(serialized) > 500 else serialized
        _raise_output_too_large(
            f"Tool '{tool_name}' output too large ({len(serialized):,} chars, limit {max_chars:,}). "
            "Please narrow your query by: using the 'fields' parameter to select only needed fields, "
            "adding filters, or reducing the 'limit'. "
            f"Preview: {truncated_preview}"
        )

    return result




class FreshdeskConnector:
    """
    Type-safe Freshdesk API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "freshdesk"
    connector_version = "1.0.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("tickets", "list"): True,
        ("tickets", "get"): None,
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("agents", "list"): True,
        ("agents", "get"): None,
        ("groups", "list"): True,
        ("groups", "get"): None,
        ("companies", "list"): True,
        ("companies", "get"): None,
        ("roles", "list"): True,
        ("roles", "get"): None,
        ("satisfaction_ratings", "list"): True,
        ("surveys", "list"): True,
        ("time_entries", "list"): True,
        ("ticket_fields", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('tickets', 'list'): {'per_page': 'per_page', 'page': 'page', 'updated_since': 'updated_since', 'order_by': 'order_by', 'order_type': 'order_type'},
        ('tickets', 'get'): {'id': 'id'},
        ('contacts', 'list'): {'per_page': 'per_page', 'page': 'page', 'updated_since': 'updated_since'},
        ('contacts', 'get'): {'id': 'id'},
        ('agents', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('agents', 'get'): {'id': 'id'},
        ('groups', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('groups', 'get'): {'id': 'id'},
        ('companies', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('companies', 'get'): {'id': 'id'},
        ('roles', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('roles', 'get'): {'id': 'id'},
        ('satisfaction_ratings', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_since': 'created_since'},
        ('surveys', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('time_entries', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('ticket_fields', 'list'): {'per_page': 'per_page', 'page': 'page'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (FreshdeskAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: FreshdeskAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new freshdesk connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., FreshdeskAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Freshdesk subdomain (e.g., "acme" for acme.freshdesk.com)
        Examples:
            # Local mode (direct API calls)
            connector = FreshdeskConnector(auth_config=FreshdeskAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = FreshdeskConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = FreshdeskConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="user-123",
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
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                customer_name=auth_config.customer_name,
                organization_id=auth_config.organization_id,
                connector_definition_id=str(FreshdeskConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or FreshdeskAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            self._executor = LocalExecutor(
                model=FreshdeskConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if subdomain:
                base_url = base_url.replace("{subdomain}", subdomain)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.tickets = TicketsQuery(self)
        self.contacts = ContactsQuery(self)
        self.agents = AgentsQuery(self)
        self.groups = GroupsQuery(self)
        self.companies = CompaniesQuery(self)
        self.roles = RolesQuery(self)
        self.satisfaction_ratings = SatisfactionRatingsQuery(self)
        self.surveys = SurveysQuery(self)
        self.time_entries = TimeEntriesQuery(self)
        self.ticket_fields = TicketFieldsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["list"],
        params: "TicketsListParams"
    ) -> "TicketsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tickets"],
        action: Literal["get"],
        params: "TicketsGetParams"
    ) -> "Ticket": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["list"],
        params: "ContactsListParams"
    ) -> "ContactsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["get"],
        params: "ContactsGetParams"
    ) -> "Contact": ...

    @overload
    async def execute(
        self,
        entity: Literal["agents"],
        action: Literal["list"],
        params: "AgentsListParams"
    ) -> "AgentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["agents"],
        action: Literal["get"],
        params: "AgentsGetParams"
    ) -> "Agent": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["list"],
        params: "GroupsListParams"
    ) -> "GroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["get"],
        params: "GroupsGetParams"
    ) -> "Group": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["list"],
        params: "CompaniesListParams"
    ) -> "CompaniesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["get"],
        params: "CompaniesGetParams"
    ) -> "Company": ...

    @overload
    async def execute(
        self,
        entity: Literal["roles"],
        action: Literal["list"],
        params: "RolesListParams"
    ) -> "RolesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["roles"],
        action: Literal["get"],
        params: "RolesGetParams"
    ) -> "Role": ...

    @overload
    async def execute(
        self,
        entity: Literal["satisfaction_ratings"],
        action: Literal["list"],
        params: "SatisfactionRatingsListParams"
    ) -> "SatisfactionRatingsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["surveys"],
        action: Literal["list"],
        params: "SurveysListParams"
    ) -> "SurveysListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_entries"],
        action: Literal["list"],
        params: "TimeEntriesListParams"
    ) -> "TimeEntriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_fields"],
        action: Literal["list"],
        params: "TicketFieldsListParams"
    ) -> "TicketFieldsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> FreshdeskExecuteResult[Any] | FreshdeskExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any] | None = None
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

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

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
            params=resolved_params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return FreshdeskExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return FreshdeskExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> FreshdeskCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            FreshdeskCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return FreshdeskCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return FreshdeskCheckResult(
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
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @FreshdeskConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @FreshdeskConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    FreshdeskConnectorModel,
                    enable_hosted_mode_features=enable_hosted_mode_features,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            if inspect.iscoroutinefunction(inner):

                @wraps(inner)
                async def aw(*args: Any, **kwargs: Any) -> Any:
                    result = await inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = aw
            else:

                @wraps(inner)
                def sw(*args: Any, **kwargs: Any) -> Any:
                    result = inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = sw

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
        return describe_entities(FreshdeskConnectorModel)

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
            (e for e in FreshdeskConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in FreshdeskConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await FreshdeskConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "FreshdeskAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "FreshdeskConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A FreshdeskConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await FreshdeskConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=FreshdeskAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(FreshdeskConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )




class TicketsQuery:
    """
    Query class for Tickets entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        updated_since: str | None = None,
        order_by: str | None = None,
        order_type: str | None = None,
        **kwargs
    ) -> TicketsListResult:
        """
        Returns a paginated list of tickets. By default returns tickets created in the past 30 days. Use updated_since to get older tickets.

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            updated_since: Return tickets updated since this timestamp (ISO 8601)
            order_by: Sort field
            order_type: Sort order
            **kwargs: Additional parameters

        Returns:
            TicketsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "updated_since": updated_since,
            "order_by": order_by,
            "order_type": order_type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Ticket:
        """
        Get a single ticket by ID

        Args:
            id: Ticket ID
            **kwargs: Additional parameters

        Returns:
            Ticket
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tickets", "get", params)
        return result



    async def search(
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
        - id: Unique ticket ID
        - subject: Subject of the ticket
        - description: HTML content of the ticket
        - description_text: Plain text content of the ticket
        - status: Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed
        - priority: Priority: 1=Low, 2=Medium, 3=High, 4=Urgent
        - source: Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email
        - type_: Ticket type
        - requester_id: ID of the requester
        - requester: Requester details including name, email, and contact info
        - responder_id: ID of the agent to whom the ticket is assigned
        - group_id: ID of the group to which the ticket is assigned
        - company_id: Company ID of the requester
        - product_id: ID of the product associated with the ticket
        - email_config_id: ID of the email config used for the ticket
        - cc_emails: CC email addresses
        - ticket_cc_emails: Ticket CC email addresses
        - to_emails: To email addresses
        - fwd_emails: Forwarded email addresses
        - reply_cc_emails: Reply CC email addresses
        - tags: Tags associated with the ticket
        - custom_fields: Custom fields associated with the ticket
        - due_by: Resolution due by timestamp
        - fr_due_by: First response due by timestamp
        - fr_escalated: Whether the first response time was breached
        - is_escalated: Whether the ticket is escalated
        - nr_due_by: Next response due by timestamp
        - nr_escalated: Whether the next response time was breached
        - spam: Whether the ticket is marked as spam
        - association_type: Association type for parent/child tickets
        - associated_tickets_count: Number of associated tickets
        - stats: Ticket statistics including response and resolution times
        - created_at: Ticket creation timestamp
        - updated_at: Ticket last update timestamp

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

        result = await self._connector.execute("tickets", "search", params)

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

class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        updated_since: str | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a paginated list of contacts

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            updated_since: Return contacts updated since this timestamp (ISO 8601)
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "updated_since": updated_since,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID

        Args:
            id: Contact ID
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



class AgentsQuery:
    """
    Query class for Agents entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> AgentsListResult:
        """
        Returns a paginated list of agents

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            AgentsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agents", "list", params)
        # Cast generic envelope to concrete typed result
        return AgentsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Agent:
        """
        Get a single agent by ID

        Args:
            id: Agent ID
            **kwargs: Additional parameters

        Returns:
            Agent
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agents", "get", params)
        return result



    async def search(
        self,
        query: AgentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AgentsSearchResult:
        """
        Search agents records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AgentsSearchFilter):
        - id: Unique agent ID
        - available: Whether the agent is available
        - available_since: Timestamp since the agent has been available
        - contact: Contact details of the agent including name, email, phone, and job title
        - occasional: Whether the agent is an occasional agent
        - signature: Signature of the agent (HTML)
        - ticket_scope: Ticket scope: 1=Global, 2=Group, 3=Restricted
        - type_: Agent type: support_agent, field_agent, collaborator
        - last_active_at: Timestamp of last agent activity
        - created_at: Agent creation timestamp
        - updated_at: Agent last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AgentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("agents", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AgentsSearchResult(
            data=[
                AgentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GroupsQuery:
    """
    Query class for Groups entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> GroupsListResult:
        """
        Returns a paginated list of groups

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            GroupsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "list", params)
        # Cast generic envelope to concrete typed result
        return GroupsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Group:
        """
        Get a single group by ID

        Args:
            id: Group ID
            **kwargs: Additional parameters

        Returns:
            Group
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "get", params)
        return result



    async def search(
        self,
        query: GroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GroupsSearchResult:
        """
        Search groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GroupsSearchFilter):
        - id: Unique group ID
        - name: Name of the group
        - description: Description of the group
        - auto_ticket_assign: Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based
        - business_hour_id: ID of the associated business hour
        - escalate_to: User ID for escalation
        - group_type: Type of the group (e.g., support_agent_group)
        - unassigned_for: Time after which escalation triggers
        - created_at: Group creation timestamp
        - updated_at: Group last update timestamp

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GroupsSearchResult(
            data=[
                GroupsSearchData(**row)
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

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> CompaniesListResult:
        """
        Returns a paginated list of companies

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            CompaniesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "list", params)
        # Cast generic envelope to concrete typed result
        return CompaniesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Company:
        """
        Get a single company by ID

        Args:
            id: Company ID
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "get", params)
        return result



class RolesQuery:
    """
    Query class for Roles entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> RolesListResult:
        """
        Returns a paginated list of roles

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            RolesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("roles", "list", params)
        # Cast generic envelope to concrete typed result
        return RolesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Role:
        """
        Get a single role by ID

        Args:
            id: Role ID
            **kwargs: Additional parameters

        Returns:
            Role
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("roles", "get", params)
        return result



class SatisfactionRatingsQuery:
    """
    Query class for SatisfactionRatings entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_since: str | None = None,
        **kwargs
    ) -> SatisfactionRatingsListResult:
        """
        Returns a paginated list of satisfaction ratings

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            created_since: Return ratings created since this timestamp (ISO 8601)
            **kwargs: Additional parameters

        Returns:
            SatisfactionRatingsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_since": created_since,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("satisfaction_ratings", "list", params)
        # Cast generic envelope to concrete typed result
        return SatisfactionRatingsListResult(
            data=result.data
        )



class SurveysQuery:
    """
    Query class for Surveys entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> SurveysListResult:
        """
        Returns a paginated list of surveys

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            SurveysListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("surveys", "list", params)
        # Cast generic envelope to concrete typed result
        return SurveysListResult(
            data=result.data
        )



class TimeEntriesQuery:
    """
    Query class for TimeEntries entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> TimeEntriesListResult:
        """
        Returns a paginated list of time entries

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            TimeEntriesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_entries", "list", params)
        # Cast generic envelope to concrete typed result
        return TimeEntriesListResult(
            data=result.data
        )



class TicketFieldsQuery:
    """
    Query class for TicketFields entity operations.
    """

    def __init__(self, connector: FreshdeskConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> TicketFieldsListResult:
        """
        Returns a list of all ticket fields

        Args:
            per_page: Number of items per page (max 100)
            page: Page number (starts at 1)
            **kwargs: Additional parameters

        Returns:
            TicketFieldsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketFieldsListResult(
            data=result.data
        )


