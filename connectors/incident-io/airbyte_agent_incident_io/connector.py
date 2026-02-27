"""
Incident-Io connector.
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

from .connector_model import IncidentIoConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AlertsGetParams,
    AlertsListParams,
    CatalogTypesGetParams,
    CatalogTypesListParams,
    CustomFieldsGetParams,
    CustomFieldsListParams,
    EscalationsGetParams,
    EscalationsListParams,
    IncidentRolesGetParams,
    IncidentRolesListParams,
    IncidentStatusesGetParams,
    IncidentStatusesListParams,
    IncidentTimestampsGetParams,
    IncidentTimestampsListParams,
    IncidentUpdatesListParams,
    IncidentsGetParams,
    IncidentsListParams,
    SchedulesGetParams,
    SchedulesListParams,
    SeveritiesGetParams,
    SeveritiesListParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    IncidentsSearchFilter,
    IncidentsSearchQuery,
    AlertsSearchFilter,
    AlertsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    IncidentUpdatesSearchFilter,
    IncidentUpdatesSearchQuery,
    IncidentRolesSearchFilter,
    IncidentRolesSearchQuery,
    IncidentStatusesSearchFilter,
    IncidentStatusesSearchQuery,
    IncidentTimestampsSearchFilter,
    IncidentTimestampsSearchQuery,
    SeveritiesSearchFilter,
    SeveritiesSearchQuery,
    CustomFieldsSearchFilter,
    CustomFieldsSearchQuery,
    CatalogTypesSearchFilter,
    CatalogTypesSearchQuery,
    SchedulesSearchFilter,
    SchedulesSearchQuery,
    EscalationsSearchFilter,
    EscalationsSearchQuery,
)
from .models import IncidentIoAuthConfig

# Import response models and envelope models at runtime
from .models import (
    IncidentIoCheckResult,
    IncidentIoExecuteResult,
    IncidentIoExecuteResultWithMeta,
    IncidentsListResult,
    AlertsListResult,
    EscalationsListResult,
    UsersListResult,
    IncidentUpdatesListResult,
    IncidentRolesListResult,
    IncidentStatusesListResult,
    IncidentTimestampsListResult,
    SeveritiesListResult,
    CustomFieldsListResult,
    CatalogTypesListResult,
    SchedulesListResult,
    Alert,
    CatalogType,
    CustomField,
    Escalation,
    Incident,
    IncidentRole,
    IncidentStatus,
    IncidentTimestamp,
    IncidentUpdate,
    Schedule,
    Severity,
    User,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    IncidentsSearchData,
    IncidentsSearchResult,
    AlertsSearchData,
    AlertsSearchResult,
    UsersSearchData,
    UsersSearchResult,
    IncidentUpdatesSearchData,
    IncidentUpdatesSearchResult,
    IncidentRolesSearchData,
    IncidentRolesSearchResult,
    IncidentStatusesSearchData,
    IncidentStatusesSearchResult,
    IncidentTimestampsSearchData,
    IncidentTimestampsSearchResult,
    SeveritiesSearchData,
    SeveritiesSearchResult,
    CustomFieldsSearchData,
    CustomFieldsSearchResult,
    CatalogTypesSearchData,
    CatalogTypesSearchResult,
    SchedulesSearchData,
    SchedulesSearchResult,
    EscalationsSearchData,
    EscalationsSearchResult,
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




class IncidentIoConnector:
    """
    Type-safe Incident-Io API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "incident-io"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("incidents", "list"): True,
        ("incidents", "get"): None,
        ("alerts", "list"): True,
        ("alerts", "get"): None,
        ("escalations", "list"): True,
        ("escalations", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("incident_updates", "list"): True,
        ("incident_roles", "list"): True,
        ("incident_roles", "get"): None,
        ("incident_statuses", "list"): True,
        ("incident_statuses", "get"): None,
        ("incident_timestamps", "list"): True,
        ("incident_timestamps", "get"): None,
        ("severities", "list"): True,
        ("severities", "get"): None,
        ("custom_fields", "list"): True,
        ("custom_fields", "get"): None,
        ("catalog_types", "list"): True,
        ("catalog_types", "get"): None,
        ("schedules", "list"): True,
        ("schedules", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('incidents', 'list'): {'page_size': 'page_size', 'after': 'after'},
        ('incidents', 'get'): {'id': 'id'},
        ('alerts', 'list'): {'page_size': 'page_size', 'after': 'after'},
        ('alerts', 'get'): {'id': 'id'},
        ('escalations', 'list'): {'page_size': 'page_size', 'after': 'after'},
        ('escalations', 'get'): {'id': 'id'},
        ('users', 'list'): {'page_size': 'page_size', 'after': 'after'},
        ('users', 'get'): {'id': 'id'},
        ('incident_updates', 'list'): {'page_size': 'page_size', 'after': 'after'},
        ('incident_roles', 'get'): {'id': 'id'},
        ('incident_statuses', 'get'): {'id': 'id'},
        ('incident_timestamps', 'get'): {'id': 'id'},
        ('severities', 'get'): {'id': 'id'},
        ('custom_fields', 'get'): {'id': 'id'},
        ('catalog_types', 'get'): {'id': 'id'},
        ('schedules', 'list'): {'page_size': 'page_size', 'after': 'after'},
        ('schedules', 'get'): {'id': 'id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (IncidentIoAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: IncidentIoAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new incident-io connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., IncidentIoAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = IncidentIoConnector(auth_config=IncidentIoAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = IncidentIoConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = IncidentIoConnector(
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
                connector_definition_id=str(IncidentIoConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or IncidentIoAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=IncidentIoConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.incidents = IncidentsQuery(self)
        self.alerts = AlertsQuery(self)
        self.escalations = EscalationsQuery(self)
        self.users = UsersQuery(self)
        self.incident_updates = IncidentUpdatesQuery(self)
        self.incident_roles = IncidentRolesQuery(self)
        self.incident_statuses = IncidentStatusesQuery(self)
        self.incident_timestamps = IncidentTimestampsQuery(self)
        self.severities = SeveritiesQuery(self)
        self.custom_fields = CustomFieldsQuery(self)
        self.catalog_types = CatalogTypesQuery(self)
        self.schedules = SchedulesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["incidents"],
        action: Literal["list"],
        params: "IncidentsListParams"
    ) -> "IncidentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["incidents"],
        action: Literal["get"],
        params: "IncidentsGetParams"
    ) -> "Incident": ...

    @overload
    async def execute(
        self,
        entity: Literal["alerts"],
        action: Literal["list"],
        params: "AlertsListParams"
    ) -> "AlertsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["alerts"],
        action: Literal["get"],
        params: "AlertsGetParams"
    ) -> "Alert": ...

    @overload
    async def execute(
        self,
        entity: Literal["escalations"],
        action: Literal["list"],
        params: "EscalationsListParams"
    ) -> "EscalationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["escalations"],
        action: Literal["get"],
        params: "EscalationsGetParams"
    ) -> "Escalation": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_updates"],
        action: Literal["list"],
        params: "IncidentUpdatesListParams"
    ) -> "IncidentUpdatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_roles"],
        action: Literal["list"],
        params: "IncidentRolesListParams"
    ) -> "IncidentRolesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_roles"],
        action: Literal["get"],
        params: "IncidentRolesGetParams"
    ) -> "IncidentRole": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_statuses"],
        action: Literal["list"],
        params: "IncidentStatusesListParams"
    ) -> "IncidentStatusesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_statuses"],
        action: Literal["get"],
        params: "IncidentStatusesGetParams"
    ) -> "IncidentStatus": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_timestamps"],
        action: Literal["list"],
        params: "IncidentTimestampsListParams"
    ) -> "IncidentTimestampsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["incident_timestamps"],
        action: Literal["get"],
        params: "IncidentTimestampsGetParams"
    ) -> "IncidentTimestamp": ...

    @overload
    async def execute(
        self,
        entity: Literal["severities"],
        action: Literal["list"],
        params: "SeveritiesListParams"
    ) -> "SeveritiesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["severities"],
        action: Literal["get"],
        params: "SeveritiesGetParams"
    ) -> "Severity": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_fields"],
        action: Literal["list"],
        params: "CustomFieldsListParams"
    ) -> "CustomFieldsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_fields"],
        action: Literal["get"],
        params: "CustomFieldsGetParams"
    ) -> "CustomField": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalog_types"],
        action: Literal["list"],
        params: "CatalogTypesListParams"
    ) -> "CatalogTypesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalog_types"],
        action: Literal["get"],
        params: "CatalogTypesGetParams"
    ) -> "CatalogType": ...

    @overload
    async def execute(
        self,
        entity: Literal["schedules"],
        action: Literal["list"],
        params: "SchedulesListParams"
    ) -> "SchedulesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["schedules"],
        action: Literal["get"],
        params: "SchedulesGetParams"
    ) -> "Schedule": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> IncidentIoExecuteResult[Any] | IncidentIoExecuteResultWithMeta[Any, Any] | Any: ...

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
                return IncidentIoExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return IncidentIoExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> IncidentIoCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            IncidentIoCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return IncidentIoCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return IncidentIoCheckResult(
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
            @IncidentIoConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @IncidentIoConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    IncidentIoConnectorModel,
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
        return describe_entities(IncidentIoConnectorModel)

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
            (e for e in IncidentIoConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in IncidentIoConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await IncidentIoConnector.create(...)
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
        auth_config: "IncidentIoAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "IncidentIoConnector":
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
            A IncidentIoConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await IncidentIoConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=IncidentIoAuthConfig(api_key="..."),
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
                connector_definition_id=str(IncidentIoConnectorModel.id),
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




class IncidentsQuery:
    """
    Query class for Incidents entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> IncidentsListResult:
        """
        List all incidents for the organisation with cursor-based pagination.

        Args:
            page_size: Number of incidents per page
            after: Cursor for the next page of results
            **kwargs: Additional parameters

        Returns:
            IncidentsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incidents", "list", params)
        # Cast generic envelope to concrete typed result
        return IncidentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Incident:
        """
        Get a single incident by ID or numeric reference.

        Args:
            id: Incident ID or numeric reference
            **kwargs: Additional parameters

        Returns:
            Incident
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incidents", "get", params)
        return result



    async def search(
        self,
        query: IncidentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IncidentsSearchResult:
        """
        Search incidents records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IncidentsSearchFilter):
        - call_url: URL of the call associated with the incident
        - created_at: When the incident was created
        - creator: The user who created the incident
        - custom_field_entries: Custom field values for the incident
        - duration_metrics: Duration metrics associated with the incident
        - has_debrief: Whether the incident has had a debrief
        - id: Unique identifier for the incident
        - incident_role_assignments: Role assignments for the incident
        - incident_status: Current status of the incident
        - incident_timestamp_values: Timestamp values for the incident
        - incident_type: Type of the incident
        - mode: Mode of the incident: standard, retrospective, test, or tutorial
        - name: Name/title of the incident
        - permalink: Link to the incident in the dashboard
        - reference: Human-readable reference (e.g. INC-123)
        - severity: Severity of the incident
        - slack_channel_id: Slack channel ID for the incident
        - slack_channel_name: Slack channel name for the incident
        - slack_team_id: Slack team/workspace ID
        - summary: Detailed summary of the incident
        - updated_at: When the incident was last updated
        - visibility: Whether the incident is public or private
        - workload_minutes_late: Minutes of workload classified as late
        - workload_minutes_sleeping: Minutes of workload classified as sleeping
        - workload_minutes_total: Total workload minutes
        - workload_minutes_working: Minutes of workload classified as working

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IncidentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("incidents", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IncidentsSearchResult(
            data=[
                IncidentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AlertsQuery:
    """
    Query class for Alerts entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> AlertsListResult:
        """
        List all alerts for the account with cursor-based pagination.

        Args:
            page_size: Number of alerts per page
            after: Cursor for the next page of results
            **kwargs: Additional parameters

        Returns:
            AlertsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("alerts", "list", params)
        # Cast generic envelope to concrete typed result
        return AlertsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Alert:
        """
        Show a single alert by ID.

        Args:
            id: Alert ID
            **kwargs: Additional parameters

        Returns:
            Alert
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("alerts", "get", params)
        return result



    async def search(
        self,
        query: AlertsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AlertsSearchResult:
        """
        Search alerts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AlertsSearchFilter):
        - alert_source_id: ID of the alert source that generated this alert
        - attributes: Structured alert attributes
        - created_at: When the alert was created
        - deduplication_key: Deduplication key uniquely referencing this alert
        - description: Description of the alert
        - id: Unique identifier for the alert
        - resolved_at: When the alert was resolved
        - source_url: Link to the alert in the upstream system
        - status: Status of the alert: firing or resolved
        - title: Title of the alert
        - updated_at: When the alert was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AlertsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("alerts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AlertsSearchResult(
            data=[
                AlertsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class EscalationsQuery:
    """
    Query class for Escalations entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> EscalationsListResult:
        """
        List all escalations for the account with cursor-based pagination.

        Args:
            page_size: Number of escalations per page
            after: Cursor for the next page of results
            **kwargs: Additional parameters

        Returns:
            EscalationsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("escalations", "list", params)
        # Cast generic envelope to concrete typed result
        return EscalationsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Escalation:
        """
        Show a specific escalation by ID.

        Args:
            id: Escalation ID
            **kwargs: Additional parameters

        Returns:
            Escalation
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("escalations", "get", params)
        return result



    async def search(
        self,
        query: EscalationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EscalationsSearchResult:
        """
        Search escalations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EscalationsSearchFilter):
        - created_at: When the escalation was created
        - creator: The creator of this escalation
        - escalation_path_id: ID of the escalation path used
        - events: History of escalation events
        - id: Unique identifier for the escalation
        - priority: Priority of the escalation
        - related_alerts: Alerts related to this escalation
        - related_incidents: Incidents related to this escalation
        - status: Status: pending, triggered, acked, resolved, expired, cancelled
        - title: Title of the escalation
        - updated_at: When the escalation was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EscalationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("escalations", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EscalationsSearchResult(
            data=[
                EscalationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        List all users for the organisation with cursor-based pagination.

        Args:
            page_size: Number of users per page
            after: Cursor for the next page of results
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> User:
        """
        Get a single user by ID.

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



    async def search(
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
        - base_role: Base role assigned to the user
        - custom_roles: Custom roles assigned to the user
        - email: Email address of the user
        - id: Unique identifier for the user
        - name: Full name of the user
        - role: Deprecated role field
        - slack_user_id: Slack user ID

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

        result = await self._connector.execute("users", "search", params)

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

class IncidentUpdatesQuery:
    """
    Query class for IncidentUpdates entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> IncidentUpdatesListResult:
        """
        List all incident updates for the organisation with cursor-based pagination.

        Args:
            page_size: Number of incident updates per page
            after: Cursor for the next page of results
            **kwargs: Additional parameters

        Returns:
            IncidentUpdatesListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_updates", "list", params)
        # Cast generic envelope to concrete typed result
        return IncidentUpdatesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: IncidentUpdatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IncidentUpdatesSearchResult:
        """
        Search incident_updates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IncidentUpdatesSearchFilter):
        - created_at: When the update was created
        - id: Unique identifier for the incident update
        - incident_id: ID of the incident this update belongs to
        - message: Update message content
        - new_incident_status: New incident status set by this update
        - new_severity: New severity set by this update
        - updater: Who made this update

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IncidentUpdatesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("incident_updates", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IncidentUpdatesSearchResult(
            data=[
                IncidentUpdatesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class IncidentRolesQuery:
    """
    Query class for IncidentRoles entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> IncidentRolesListResult:
        """
        List all incident roles for the organisation.

        Returns:
            IncidentRolesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_roles", "list", params)
        # Cast generic envelope to concrete typed result
        return IncidentRolesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> IncidentRole:
        """
        Get a single incident role by ID.

        Args:
            id: Incident role ID
            **kwargs: Additional parameters

        Returns:
            IncidentRole
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_roles", "get", params)
        return result



    async def search(
        self,
        query: IncidentRolesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IncidentRolesSearchResult:
        """
        Search incident_roles records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IncidentRolesSearchFilter):
        - created_at: When the role was created
        - description: Description of the role
        - id: Unique identifier for the incident role
        - instructions: Instructions for the role holder
        - name: Name of the role
        - required: Whether this role must be assigned
        - role_type: Type of role
        - shortform: Short form label for the role
        - updated_at: When the role was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IncidentRolesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("incident_roles", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IncidentRolesSearchResult(
            data=[
                IncidentRolesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class IncidentStatusesQuery:
    """
    Query class for IncidentStatuses entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> IncidentStatusesListResult:
        """
        List all incident statuses for the organisation.

        Returns:
            IncidentStatusesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_statuses", "list", params)
        # Cast generic envelope to concrete typed result
        return IncidentStatusesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> IncidentStatus:
        """
        Get a single incident status by ID.

        Args:
            id: Incident status ID
            **kwargs: Additional parameters

        Returns:
            IncidentStatus
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_statuses", "get", params)
        return result



    async def search(
        self,
        query: IncidentStatusesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IncidentStatusesSearchResult:
        """
        Search incident_statuses records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IncidentStatusesSearchFilter):
        - category: Category: triage, active, post-incident, closed, etc.
        - created_at: When the status was created
        - description: Description of the status
        - id: Unique identifier for the status
        - name: Name of the status
        - rank: Rank for ordering
        - updated_at: When the status was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IncidentStatusesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("incident_statuses", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IncidentStatusesSearchResult(
            data=[
                IncidentStatusesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class IncidentTimestampsQuery:
    """
    Query class for IncidentTimestamps entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> IncidentTimestampsListResult:
        """
        List all incident timestamps for the organisation.

        Returns:
            IncidentTimestampsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_timestamps", "list", params)
        # Cast generic envelope to concrete typed result
        return IncidentTimestampsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> IncidentTimestamp:
        """
        Get a single incident timestamp by ID.

        Args:
            id: Incident timestamp ID
            **kwargs: Additional parameters

        Returns:
            IncidentTimestamp
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incident_timestamps", "get", params)
        return result



    async def search(
        self,
        query: IncidentTimestampsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IncidentTimestampsSearchResult:
        """
        Search incident_timestamps records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IncidentTimestampsSearchFilter):
        - id: Unique identifier for the timestamp
        - name: Name of the timestamp
        - rank: Rank for ordering

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IncidentTimestampsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("incident_timestamps", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IncidentTimestampsSearchResult(
            data=[
                IncidentTimestampsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SeveritiesQuery:
    """
    Query class for Severities entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SeveritiesListResult:
        """
        List all severities for the organisation.

        Returns:
            SeveritiesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("severities", "list", params)
        # Cast generic envelope to concrete typed result
        return SeveritiesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Severity:
        """
        Get a single severity by ID.

        Args:
            id: Severity ID
            **kwargs: Additional parameters

        Returns:
            Severity
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("severities", "get", params)
        return result



    async def search(
        self,
        query: SeveritiesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SeveritiesSearchResult:
        """
        Search severities records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SeveritiesSearchFilter):
        - created_at: When the severity was created
        - description: Description of the severity
        - id: Unique identifier for the severity
        - name: Name of the severity
        - rank: Rank for ordering
        - updated_at: When the severity was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SeveritiesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("severities", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SeveritiesSearchResult(
            data=[
                SeveritiesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CustomFieldsQuery:
    """
    Query class for CustomFields entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> CustomFieldsListResult:
        """
        List all custom fields for the organisation.

        Returns:
            CustomFieldsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomFieldsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> CustomField:
        """
        Get a single custom field by ID.

        Args:
            id: Custom field ID
            **kwargs: Additional parameters

        Returns:
            CustomField
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_fields", "get", params)
        return result



    async def search(
        self,
        query: CustomFieldsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomFieldsSearchResult:
        """
        Search custom_fields records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomFieldsSearchFilter):
        - catalog_type_id: ID of the catalog type associated with this custom field
        - created_at: When the custom field was created
        - description: Description of the custom field
        - field_type: Type of field
        - id: Unique identifier for the custom field
        - name: Name of the custom field
        - updated_at: When the custom field was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomFieldsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("custom_fields", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CustomFieldsSearchResult(
            data=[
                CustomFieldsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CatalogTypesQuery:
    """
    Query class for CatalogTypes entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> CatalogTypesListResult:
        """
        List all catalog types for the organisation.

        Returns:
            CatalogTypesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalog_types", "list", params)
        # Cast generic envelope to concrete typed result
        return CatalogTypesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> CatalogType:
        """
        Show a single catalog type by ID.

        Args:
            id: Catalog type ID
            **kwargs: Additional parameters

        Returns:
            CatalogType
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalog_types", "get", params)
        return result



    async def search(
        self,
        query: CatalogTypesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CatalogTypesSearchResult:
        """
        Search catalog_types records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CatalogTypesSearchFilter):
        - annotations: Annotations metadata
        - categories: Categories this type belongs to
        - color: Display color
        - created_at: When the catalog type was created
        - description: Description of the catalog type
        - icon: Display icon
        - id: Unique identifier for the catalog type
        - is_editable: Whether entries can be edited
        - last_synced_at: When the catalog type was last synced
        - name: Name of the catalog type
        - ranked: Whether entries are ranked
        - registry_type: Registry type if synced from an integration
        - required_integrations: Integrations required for this type
        - schema_: Schema definition for the catalog type
        - semantic_type: Semantic type for special behavior
        - type_name: Programmatic type name
        - updated_at: When the catalog type was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CatalogTypesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("catalog_types", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CatalogTypesSearchResult(
            data=[
                CatalogTypesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SchedulesQuery:
    """
    Query class for Schedules entity operations.
    """

    def __init__(self, connector: IncidentIoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> SchedulesListResult:
        """
        List all on-call schedules with cursor-based pagination.

        Args:
            page_size: Number of schedules per page
            after: Cursor for the next page of results
            **kwargs: Additional parameters

        Returns:
            SchedulesListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schedules", "list", params)
        # Cast generic envelope to concrete typed result
        return SchedulesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Schedule:
        """
        Get a single on-call schedule by ID.

        Args:
            id: Schedule ID
            **kwargs: Additional parameters

        Returns:
            Schedule
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("schedules", "get", params)
        return result



    async def search(
        self,
        query: SchedulesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SchedulesSearchResult:
        """
        Search schedules records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SchedulesSearchFilter):
        - annotations: Annotations metadata
        - config: Schedule configuration with rotations
        - created_at: When the schedule was created
        - current_shifts: Currently active shifts
        - holidays_public_config: Public holiday configuration for the schedule
        - id: Unique identifier for the schedule
        - name: Name of the schedule
        - team_ids: IDs of teams associated with this schedule
        - timezone: Timezone for the schedule
        - updated_at: When the schedule was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SchedulesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("schedules", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SchedulesSearchResult(
            data=[
                SchedulesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
