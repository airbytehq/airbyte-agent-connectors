"""
Sentry connector.
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

from .connector_model import SentryConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    EventsGetParams,
    EventsListParams,
    IssuesGetParams,
    IssuesListParams,
    ProjectDetailGetParams,
    ProjectsGetParams,
    ProjectsListParams,
    ReleasesGetParams,
    ReleasesListParams,
    AirbyteSearchParams,
    EventsSearchFilter,
    EventsSearchQuery,
    IssuesSearchFilter,
    IssuesSearchQuery,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    ReleasesSearchFilter,
    ReleasesSearchQuery,
)
from .models import SentryAuthConfig
if TYPE_CHECKING:
    from .models import SentryReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    SentryCheckResult,
    SentryExecuteResult,
    SentryExecuteResultWithMeta,
    ProjectsListResult,
    IssuesListResult,
    EventsListResult,
    ReleasesListResult,
    Event,
    Issue,
    Project,
    ProjectDetail,
    Release,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    EventsSearchData,
    EventsSearchResult,
    IssuesSearchData,
    IssuesSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    ReleasesSearchData,
    ReleasesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 100_000  # ~100KB default, configurable per-tool


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




class SentryConnector:
    """
    Type-safe Sentry API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "sentry"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("projects", "list"): True,
        ("projects", "get"): None,
        ("issues", "list"): True,
        ("issues", "get"): None,
        ("events", "list"): True,
        ("events", "get"): None,
        ("releases", "list"): True,
        ("releases", "get"): None,
        ("project_detail", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('projects', 'list'): {'cursor': 'cursor'},
        ('projects', 'get'): {'organization_slug': 'organization_slug', 'project_slug': 'project_slug'},
        ('issues', 'list'): {'organization_slug': 'organization_slug', 'project_slug': 'project_slug', 'query': 'query', 'stats_period': 'statsPeriod', 'cursor': 'cursor'},
        ('issues', 'get'): {'organization_slug': 'organization_slug', 'issue_id': 'issue_id'},
        ('events', 'list'): {'organization_slug': 'organization_slug', 'project_slug': 'project_slug', 'full': 'full', 'cursor': 'cursor'},
        ('events', 'get'): {'organization_slug': 'organization_slug', 'project_slug': 'project_slug', 'event_id': 'event_id'},
        ('releases', 'list'): {'organization_slug': 'organization_slug', 'query': 'query', 'cursor': 'cursor'},
        ('releases', 'get'): {'organization_slug': 'organization_slug', 'version': 'version'},
        ('project_detail', 'get'): {'organization_slug': 'organization_slug', 'project_slug': 'project_slug'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (SentryAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: SentryAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        hostname: str | None = None    ):
        """
        Initialize a new sentry connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., SentryAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            hostname: Host name of Sentry API server. For self-hosted instances, specify your host name here. Otherwise, leave as sentry.io.
        Examples:
            # Local mode (direct API calls)
            connector = SentryConnector(auth_config=SentryAuthConfig(auth_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = SentryConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = SentryConnector(
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
                connector_definition_id=str(SentryConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or SentryAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if hostname:
                config_values["hostname"] = hostname

            self._executor = LocalExecutor(
                model=SentryConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if hostname:
                base_url = base_url.replace("{hostname}", hostname)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.projects = ProjectsQuery(self)
        self.issues = IssuesQuery(self)
        self.events = EventsQuery(self)
        self.releases = ReleasesQuery(self)
        self.project_detail = ProjectDetailQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["get"],
        params: "ProjectsGetParams"
    ) -> "ProjectDetail": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["list"],
        params: "IssuesListParams"
    ) -> "IssuesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["get"],
        params: "IssuesGetParams"
    ) -> "Issue": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["list"],
        params: "EventsListParams"
    ) -> "EventsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["get"],
        params: "EventsGetParams"
    ) -> "Event": ...

    @overload
    async def execute(
        self,
        entity: Literal["releases"],
        action: Literal["list"],
        params: "ReleasesListParams"
    ) -> "ReleasesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["releases"],
        action: Literal["get"],
        params: "ReleasesGetParams"
    ) -> "Release": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_detail"],
        action: Literal["get"],
        params: "ProjectDetailGetParams"
    ) -> "ProjectDetail": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> SentryExecuteResult[Any] | SentryExecuteResultWithMeta[Any, Any] | Any: ...

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
                return SentryExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SentryExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SentryCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SentryCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SentryCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SentryCheckResult(
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
            @SentryConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @SentryConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    SentryConnectorModel,
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
        return describe_entities(SentryConnectorModel)

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
            (e for e in SentryConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SentryConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await SentryConnector.create(...)
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
        auth_config: "SentryAuthConfig",
        name: str | None = None,
        replication_config: "SentryReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "SentryConnector":
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
            A SentryConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await SentryConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=SentryAuthConfig(auth_token="..."),
            )

            # With replication config (required for this connector):
            connector = await SentryConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=SentryAuthConfig(auth_token="..."),
                replication_config=SentryReplicationConfig(organization="...", project="..."),
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
                connector_definition_id=str(SentryConnectorModel.id),
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




class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: SentryConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> ProjectsListResult:
        """
        Return a list of projects available to the authenticated user.

        Args:
            cursor: Pagination cursor for next page of results.
            **kwargs: Additional parameters

        Returns:
            ProjectsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectsListResult(
            data=result.data
        )



    async def get(
        self,
        organization_slug: str,
        project_slug: str,
        **kwargs
    ) -> ProjectDetail:
        """
        Return details on an individual project.

        Args:
            organization_slug: The slug of the organization the project belongs to.
            project_slug: The slug of the project to retrieve.
            **kwargs: Additional parameters

        Returns:
            ProjectDetail
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "project_slug": project_slug,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        return result



    async def search(
        self,
        query: ProjectsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProjectsSearchResult:
        """
        Search projects records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProjectsSearchFilter):
        - access: List of access permissions for the authenticated user.
        - avatar: Project avatar information.
        - color: Project color code.
        - date_created: Date the project was created.
        - features: List of enabled features.
        - first_event: Timestamp of the first event.
        - first_transaction_event: Whether a transaction event has been received.
        - has_access: Whether the user has access to this project.
        - has_custom_metrics: Whether the project has custom metrics.
        - has_feedbacks: Whether the project has user feedback.
        - has_minified_stack_trace: Whether the project has minified stack traces.
        - has_monitors: Whether the project has cron monitors.
        - has_new_feedbacks: Whether the project has new user feedback.
        - has_profiles: Whether the project has profiling data.
        - has_replays: Whether the project has session replays.
        - has_sessions: Whether the project has session data.
        - id: Unique project identifier.
        - is_bookmarked: Whether the project is bookmarked.
        - is_internal: Whether the project is internal.
        - is_member: Whether the authenticated user is a member.
        - is_public: Whether the project is public.
        - name: Human-readable project name.
        - organization: Organization this project belongs to.
        - platform: The platform for this project.
        - slug: URL-friendly project identifier.
        - status: Project status.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProjectsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("projects", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProjectsSearchResult(
            data=[
                ProjectsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: SentryConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        organization_slug: str,
        project_slug: str,
        query: str | None = None,
        stats_period: str | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> IssuesListResult:
        """
        Return a list of issues (groups) bound to a project. A default query of is:unresolved is applied. To return results with other statuses send a new query value (i.e. ?query= for all results).

        Args:
            organization_slug: The slug of the organization the issues belong to.
            project_slug: The slug of the project the issues belong to.
            query: An optional Sentry structured search query. If not provided an implied "is:unresolved" is assumed.
            stats_period: An optional stat period (can be one of "24h", "14d", and "").
            cursor: Pagination cursor for next page of results.
            **kwargs: Additional parameters

        Returns:
            IssuesListResult
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "project_slug": project_slug,
            "query": query,
            "statsPeriod": stats_period,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        # Cast generic envelope to concrete typed result
        return IssuesListResult(
            data=result.data
        )



    async def get(
        self,
        organization_slug: str,
        issue_id: str,
        **kwargs
    ) -> Issue:
        """
        Return details on an individual issue. This returns the basic stats for the issue (title, last seen, first seen), some overall numbers (number of comments, user reports) as well as the summarized event data.

        Args:
            organization_slug: The slug of the organization the issue belongs to.
            issue_id: The ID of the issue to retrieve.
            **kwargs: Additional parameters

        Returns:
            Issue
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "issue_id": issue_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result



    async def search(
        self,
        query: IssuesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IssuesSearchResult:
        """
        Search issues records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IssuesSearchFilter):
        - annotations: Annotations on the issue.
        - assigned_to: User or team assigned to this issue.
        - count: Number of events for this issue.
        - culprit: The culprit (source) of the issue.
        - first_seen: When the issue was first seen.
        - has_seen: Whether the authenticated user has seen the issue.
        - id: Unique issue identifier.
        - is_bookmarked: Whether the issue is bookmarked.
        - is_public: Whether the issue is public.
        - is_subscribed: Whether the user is subscribed to the issue.
        - is_unhandled: Whether the issue is from an unhandled error.
        - issue_category: The category classification of the issue.
        - issue_type: The type classification of the issue.
        - last_seen: When the issue was last seen.
        - level: Issue severity level.
        - logger: Logger that generated the issue.
        - metadata: Issue metadata.
        - num_comments: Number of comments on the issue.
        - permalink: Permalink to the issue in the Sentry UI.
        - platform: Platform for this issue.
        - project: Project this issue belongs to.
        - share_id: Share ID if the issue is shared.
        - short_id: Short human-readable identifier.
        - stats: Issue event statistics.
        - status: Issue status (resolved, unresolved, ignored).
        - status_details: Status detail information.
        - subscription_details: Subscription details.
        - substatus: Issue substatus.
        - title: Issue title.
        - type_: Issue type.
        - user_count: Number of users affected.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IssuesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("issues", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IssuesSearchResult(
            data=[
                IssuesSearchData(**row)
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

    def __init__(self, connector: SentryConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        organization_slug: str,
        project_slug: str,
        full: str | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> EventsListResult:
        """
        Return a list of events bound to a project.

        Args:
            organization_slug: The slug of the organization the events belong to.
            project_slug: The slug of the project the events belong to.
            full: If set to true, the event payload will include the full event body.
            cursor: Pagination cursor for next page of results.
            **kwargs: Additional parameters

        Returns:
            EventsListResult
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "project_slug": project_slug,
            "full": full,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "list", params)
        # Cast generic envelope to concrete typed result
        return EventsListResult(
            data=result.data
        )



    async def get(
        self,
        organization_slug: str,
        project_slug: str,
        event_id: str,
        **kwargs
    ) -> Event:
        """
        Return details on an individual event.

        Args:
            organization_slug: The slug of the organization the event belongs to.
            project_slug: The slug of the project the event belongs to.
            event_id: The ID of the event to retrieve (hexadecimal).
            **kwargs: Additional parameters

        Returns:
            Event
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "project_slug": project_slug,
            "event_id": event_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "get", params)
        return result



    async def search(
        self,
        query: EventsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EventsSearchResult:
        """
        Search events records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EventsSearchFilter):
        - meta: Meta information for data scrubbing.
        - context: Additional context data.
        - contexts: Structured context information.
        - crash_file: Crash file reference.
        - culprit: The culprit (source) of the event.
        - date_created: When the event was created.
        - date_received: When the event was received by Sentry.
        - dist: Distribution information.
        - entries: Event entries (exception, breadcrumbs, request, etc.).
        - errors: Processing errors.
        - event_type: The type of the event.
        - event_id: Event ID as reported by the client.
        - fingerprints: Fingerprints used for grouping.
        - group_id: ID of the issue group this event belongs to.
        - grouping_config: Grouping configuration.
        - id: Unique event identifier.
        - location: Location in source code.
        - message: Event message.
        - metadata: Event metadata.
        - occurrence: Occurrence information for the event.
        - packages: Package information.
        - platform: Platform the event was generated on.
        - project_id: Project ID this event belongs to.
        - sdk: SDK information.
        - size: Event payload size in bytes.
        - tags: Tags associated with the event.
        - title: Event title.
        - type_: Event type.
        - user: User associated with the event.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EventsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("events", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EventsSearchResult(
            data=[
                EventsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ReleasesQuery:
    """
    Query class for Releases entity operations.
    """

    def __init__(self, connector: SentryConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        organization_slug: str,
        query: str | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> ReleasesListResult:
        """
        Return a list of releases for a given organization.

        Args:
            organization_slug: The slug of the organization.
            query: This parameter can be used to create a "starts with" filter for the version.
            cursor: Pagination cursor for next page of results.
            **kwargs: Additional parameters

        Returns:
            ReleasesListResult
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "query": query,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("releases", "list", params)
        # Cast generic envelope to concrete typed result
        return ReleasesListResult(
            data=result.data
        )



    async def get(
        self,
        organization_slug: str,
        version: str,
        **kwargs
    ) -> Release:
        """
        Return a release for a given organization.

        Args:
            organization_slug: The slug of the organization.
            version: The version identifier of the release.
            **kwargs: Additional parameters

        Returns:
            Release
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "version": version,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("releases", "get", params)
        return result



    async def search(
        self,
        query: ReleasesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ReleasesSearchResult:
        """
        Search releases records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ReleasesSearchFilter):
        - authors: Authors of commits in this release.
        - commit_count: Number of commits in this release.
        - current_project_meta: Metadata for the current project context.
        - data: Additional release data.
        - date_created: When the release was created.
        - date_released: When the release was deployed.
        - deploy_count: Number of deploys for this release.
        - first_event: Timestamp of the first event in this release.
        - id: Unique release identifier.
        - last_commit: Last commit in this release.
        - last_deploy: Last deploy of this release.
        - last_event: Timestamp of the last event in this release.
        - new_groups: Number of new issue groups in this release.
        - owner: Owner of the release.
        - projects: Projects associated with this release.
        - ref: Git reference (commit SHA, tag, etc.).
        - short_version: Short version string.
        - status: Release status.
        - url: URL associated with the release.
        - user_agent: User agent that created the release.
        - version: Release version string.
        - version_info: Parsed version information.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ReleasesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("releases", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ReleasesSearchResult(
            data=[
                ReleasesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProjectDetailQuery:
    """
    Query class for ProjectDetail entity operations.
    """

    def __init__(self, connector: SentryConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        organization_slug: str,
        project_slug: str,
        **kwargs
    ) -> ProjectDetail:
        """
        Return detailed information about a specific project.

        Args:
            organization_slug: The slug of the organization the project belongs to.
            project_slug: The slug of the project.
            **kwargs: Additional parameters

        Returns:
            ProjectDetail
        """
        params = {k: v for k, v in {
            "organization_slug": organization_slug,
            "project_slug": project_slug,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_detail", "get", params)
        return result


