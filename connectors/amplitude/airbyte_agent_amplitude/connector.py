"""
Amplitude connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import AmplitudeConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    ActiveUsersListParams,
    AnnotationsGetParams,
    AnnotationsListParams,
    AverageSessionLengthListParams,
    CohortsGetParams,
    CohortsListParams,
    EventsListListParams,
    AirbyteSearchParams,
    AnnotationsSearchFilter,
    AnnotationsSearchQuery,
    CohortsSearchFilter,
    CohortsSearchQuery,
    EventsListSearchFilter,
    EventsListSearchQuery,
    ActiveUsersSearchFilter,
    ActiveUsersSearchQuery,
    AverageSessionLengthSearchFilter,
    AverageSessionLengthSearchQuery,
)
from .models import AmplitudeAuthConfig
if TYPE_CHECKING:
    from .models import AmplitudeReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    AmplitudeCheckResult,
    AmplitudeExecuteResult,
    AmplitudeExecuteResultWithMeta,
    AnnotationsListResult,
    CohortsListResult,
    EventsListListResult,
    ActiveUsersListResult,
    AverageSessionLengthListResult,
    ActiveUsersData,
    Annotation,
    AnnotationV3,
    AverageSessionLengthData,
    Cohort,
    EventType,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AnnotationsSearchData,
    AnnotationsSearchResult,
    CohortsSearchData,
    CohortsSearchResult,
    EventsListSearchData,
    EventsListSearchResult,
    ActiveUsersSearchData,
    ActiveUsersSearchResult,
    AverageSessionLengthSearchData,
    AverageSessionLengthSearchResult,
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




class AmplitudeConnector:
    """
    Type-safe Amplitude API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "amplitude"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("annotations", "list"): True,
        ("annotations", "get"): None,
        ("cohorts", "list"): True,
        ("cohorts", "get"): None,
        ("events_list", "list"): True,
        ("active_users", "list"): True,
        ("average_session_length", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('annotations', 'get'): {'annotation_id': 'annotation_id'},
        ('cohorts', 'get'): {'cohort_id': 'cohort_id'},
        ('active_users', 'list'): {'start': 'start', 'end': 'end', 'm': 'm', 'i': 'i', 'g': 'g'},
        ('average_session_length', 'list'): {'start': 'start', 'end': 'end'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (AmplitudeAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: AmplitudeAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new amplitude connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., AmplitudeAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = AmplitudeConnector(auth_config=AmplitudeAuthConfig(api_key="...", secret_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = AmplitudeConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = AmplitudeConnector(
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
                connector_definition_id=str(AmplitudeConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or AmplitudeAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=AmplitudeConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.annotations = AnnotationsQuery(self)
        self.cohorts = CohortsQuery(self)
        self.events_list = EventsListQuery(self)
        self.active_users = ActiveUsersQuery(self)
        self.average_session_length = AverageSessionLengthQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["annotations"],
        action: Literal["list"],
        params: "AnnotationsListParams"
    ) -> "AnnotationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["annotations"],
        action: Literal["get"],
        params: "AnnotationsGetParams"
    ) -> "AnnotationV3": ...

    @overload
    async def execute(
        self,
        entity: Literal["cohorts"],
        action: Literal["list"],
        params: "CohortsListParams"
    ) -> "CohortsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cohorts"],
        action: Literal["get"],
        params: "CohortsGetParams"
    ) -> "Cohort": ...

    @overload
    async def execute(
        self,
        entity: Literal["events_list"],
        action: Literal["list"],
        params: "EventsListListParams"
    ) -> "EventsListListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["active_users"],
        action: Literal["list"],
        params: "ActiveUsersListParams"
    ) -> "ActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["average_session_length"],
        action: Literal["list"],
        params: "AverageSessionLengthListParams"
    ) -> "AverageSessionLengthListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> AmplitudeExecuteResult[Any] | AmplitudeExecuteResultWithMeta[Any, Any] | Any: ...

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
                return AmplitudeExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return AmplitudeExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> AmplitudeCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            AmplitudeCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return AmplitudeCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return AmplitudeCheckResult(
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
            @AmplitudeConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @AmplitudeConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    AmplitudeConnectorModel,
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
        return describe_entities(AmplitudeConnectorModel)

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
            (e for e in AmplitudeConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in AmplitudeConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await AmplitudeConnector.create(...)
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
        auth_config: "AmplitudeAuthConfig",
        name: str | None = None,
        replication_config: "AmplitudeReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "AmplitudeConnector":
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
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A AmplitudeConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await AmplitudeConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AmplitudeAuthConfig(api_key="...", secret_key="..."),
            )

            # With replication config (required for this connector):
            connector = await AmplitudeConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AmplitudeAuthConfig(api_key="...", secret_key="..."),
                replication_config=AmplitudeReplicationConfig(start_date="..."),
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
                connector_definition_id=str(AmplitudeConnectorModel.id),
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




class AnnotationsQuery:
    """
    Query class for Annotations entity operations.
    """

    def __init__(self, connector: AmplitudeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AnnotationsListResult:
        """
        Returns all chart annotations for the project.

        Returns:
            AnnotationsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("annotations", "list", params)
        # Cast generic envelope to concrete typed result
        return AnnotationsListResult(
            data=result.data
        )



    async def get(
        self,
        annotation_id: str,
        **kwargs
    ) -> AnnotationV3:
        """
        Retrieves a single chart annotation by ID.

        Args:
            annotation_id: The ID of the annotation to retrieve
            **kwargs: Additional parameters

        Returns:
            AnnotationV3
        """
        params = {k: v for k, v in {
            "annotation_id": annotation_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("annotations", "get", params)
        return result



    async def search(
        self,
        query: AnnotationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AnnotationsSearchResult:
        """
        Search annotations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AnnotationsSearchFilter):
        - date: The date when the annotation was made
        - details: Additional details or information related to the annotation
        - id: The unique identifier for the annotation
        - label: The label assigned to the annotation

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AnnotationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("annotations", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AnnotationsSearchResult(
            data=[
                AnnotationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CohortsQuery:
    """
    Query class for Cohorts entity operations.
    """

    def __init__(self, connector: AmplitudeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> CohortsListResult:
        """
        Returns all cohorts for the project.

        Returns:
            CohortsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cohorts", "list", params)
        # Cast generic envelope to concrete typed result
        return CohortsListResult(
            data=result.data
        )



    async def get(
        self,
        cohort_id: str,
        **kwargs
    ) -> Cohort:
        """
        Retrieves a single cohort by ID.

        Args:
            cohort_id: The ID of the cohort to retrieve
            **kwargs: Additional parameters

        Returns:
            Cohort
        """
        params = {k: v for k, v in {
            "cohort_id": cohort_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cohorts", "get", params)
        return result



    async def search(
        self,
        query: CohortsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CohortsSearchResult:
        """
        Search cohorts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CohortsSearchFilter):
        - app_id: The unique identifier of the application
        - archived: Indicates if the cohort data is archived
        - chart_id: The identifier of the chart associated with the cohort
        - created_at: The timestamp when the cohort was created
        - definition: The specific definition or criteria for the cohort
        - description: A brief explanation or summary of the cohort
        - edit_id: The ID for editing purposes or version control
        - finished: Indicates if the cohort data has been finalized
        - hidden: Flag to determine if the cohort is hidden from view
        - id: The unique identifier for the cohort
        - is_official_content: Indicates if the cohort data is official content
        - is_predictive: Flag to indicate if the cohort is predictive
        - last_computed: Timestamp of the last computation of cohort data
        - last_mod: Timestamp of the last modification made to the cohort
        - last_viewed: Timestamp when the cohort was last viewed
        - location_id: Identifier of the location associated with the cohort
        - metadata: Additional information or data related to the cohort
        - name: The name or title of the cohort
        - owners: The owners or administrators of the cohort
        - popularity: Popularity rank or score of the cohort
        - published: Status indicating if the cohort data is published
        - shortcut_ids: Identifiers of any shortcuts associated with the cohort
        - size: Size or scale of the cohort data
        - type: The type or category of the cohort
        - view_count: The total count of views on the cohort data
        - viewers: Users or viewers who have access to the cohort data

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CohortsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("cohorts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CohortsSearchResult(
            data=[
                CohortsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class EventsListQuery:
    """
    Query class for EventsList entity operations.
    """

    def __init__(self, connector: AmplitudeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> EventsListListResult:
        """
        Returns the list of event types with the current week's totals, unique users, and percentage of DAU.


        Returns:
            EventsListListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events_list", "list", params)
        # Cast generic envelope to concrete typed result
        return EventsListListResult(
            data=result.data
        )



    async def search(
        self,
        query: EventsListSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EventsListSearchResult:
        """
        Search events_list records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EventsListSearchFilter):
        - autohidden: Whether the event is auto-hidden
        - clusters_hidden: Whether the event is hidden from clusters
        - deleted: Whether the event is deleted
        - display: Display name of the event
        - flow_hidden: Whether the event is hidden from Pathfinder
        - hidden: Whether the event is hidden
        - id: Unique identifier for the event type
        - in_waitroom: Whether the event is in the waitroom
        - name: Name of the event type
        - non_active: Whether the event is marked as inactive
        - timeline_hidden: Whether the event is hidden from the timeline
        - totals: Total number of times the event occurred this week
        - totals_delta: Change in totals from the previous period
        - value: Raw event name in the data

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EventsListSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("events_list", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EventsListSearchResult(
            data=[
                EventsListSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ActiveUsersQuery:
    """
    Query class for ActiveUsers entity operations.
    """

    def __init__(self, connector: AmplitudeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: str,
        end: str,
        m: str | None = None,
        i: int | None = None,
        g: str | None = None,
        **kwargs
    ) -> ActiveUsersListResult:
        """
        Returns the number of active or new users for each day in the specified date range.


        Args:
            start: First date included in data series, formatted YYYYMMDD (e.g. 20220101)
            end: Last date included in data series, formatted YYYYMMDD (e.g. 20220131)
            m: Either 'new' or 'active' to get the desired count. Defaults to 'active'.
            i: Either 1, 7, or 30 for daily, weekly, and monthly counts. Defaults to 1.
            g: The property to group by (e.g. country, city, platform).
            **kwargs: Additional parameters

        Returns:
            ActiveUsersListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "end": end,
            "m": m,
            "i": i,
            "g": g,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("active_users", "list", params)
        # Cast generic envelope to concrete typed result
        return ActiveUsersListResult(
            data=result.data
        )



    async def search(
        self,
        query: ActiveUsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ActiveUsersSearchResult:
        """
        Search active_users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ActiveUsersSearchFilter):
        - date: The date for which the active user data is reported
        - statistics: The statistics related to the active users for the given date

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ActiveUsersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("active_users", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ActiveUsersSearchResult(
            data=[
                ActiveUsersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AverageSessionLengthQuery:
    """
    Query class for AverageSessionLength entity operations.
    """

    def __init__(self, connector: AmplitudeConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: str,
        end: str,
        **kwargs
    ) -> AverageSessionLengthListResult:
        """
        Returns the average session length (in seconds) for each day in the specified date range.


        Args:
            start: First date included in data series, formatted YYYYMMDD (e.g. 20220101)
            end: Last date included in data series, formatted YYYYMMDD (e.g. 20220131)
            **kwargs: Additional parameters

        Returns:
            AverageSessionLengthListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "end": end,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("average_session_length", "list", params)
        # Cast generic envelope to concrete typed result
        return AverageSessionLengthListResult(
            data=result.data
        )



    async def search(
        self,
        query: AverageSessionLengthSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AverageSessionLengthSearchResult:
        """
        Search average_session_length records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AverageSessionLengthSearchFilter):
        - date: The date on which the session occurred
        - length: The duration of the session in seconds

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AverageSessionLengthSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("average_session_length", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AverageSessionLengthSearchResult(
            data=[
                AverageSessionLengthSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
