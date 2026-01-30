"""
Greenhouse connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import GreenhouseConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    ApplicationAttachmentDownloadParams,
    ApplicationsGetParams,
    ApplicationsListParams,
    CandidateAttachmentDownloadParams,
    CandidatesGetParams,
    CandidatesListParams,
    DepartmentsGetParams,
    DepartmentsListParams,
    JobPostsGetParams,
    JobPostsListParams,
    JobsGetParams,
    JobsListParams,
    OffersGetParams,
    OffersListParams,
    OfficesGetParams,
    OfficesListParams,
    ScheduledInterviewsGetParams,
    ScheduledInterviewsListParams,
    SourcesListParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    ApplicationsSearchFilter,
    ApplicationsSearchQuery,
    CandidatesSearchFilter,
    CandidatesSearchQuery,
    DepartmentsSearchFilter,
    DepartmentsSearchQuery,
    JobPostsSearchFilter,
    JobPostsSearchQuery,
    JobsSearchFilter,
    JobsSearchQuery,
    OffersSearchFilter,
    OffersSearchQuery,
    OfficesSearchFilter,
    OfficesSearchQuery,
    SourcesSearchFilter,
    SourcesSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
)
if TYPE_CHECKING:
    from .models import GreenhouseAuthConfig

# Import response models and envelope models at runtime
from .models import (
    GreenhouseCheckResult,
    GreenhouseExecuteResult,
    GreenhouseExecuteResultWithMeta,
    CandidatesListResult,
    ApplicationsListResult,
    JobsListResult,
    OffersListResult,
    UsersListResult,
    DepartmentsListResult,
    OfficesListResult,
    JobPostsListResult,
    SourcesListResult,
    ScheduledInterviewsListResult,
    Application,
    Candidate,
    Department,
    Job,
    JobPost,
    Offer,
    Office,
    ScheduledInterview,
    Source,
    User,
    AirbyteSearchHit,
    AirbyteSearchResult,
    ApplicationsSearchData,
    ApplicationsSearchResult,
    CandidatesSearchData,
    CandidatesSearchResult,
    DepartmentsSearchData,
    DepartmentsSearchResult,
    JobPostsSearchData,
    JobPostsSearchResult,
    JobsSearchData,
    JobsSearchResult,
    OffersSearchData,
    OffersSearchResult,
    OfficesSearchData,
    OfficesSearchResult,
    SourcesSearchData,
    SourcesSearchResult,
    UsersSearchData,
    UsersSearchResult,
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




class GreenhouseConnector:
    """
    Type-safe Greenhouse API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "greenhouse"
    connector_version = "0.1.4"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("candidates", "list"): True,
        ("candidates", "get"): None,
        ("applications", "list"): True,
        ("applications", "get"): None,
        ("jobs", "list"): True,
        ("jobs", "get"): None,
        ("offers", "list"): True,
        ("offers", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("departments", "list"): True,
        ("departments", "get"): None,
        ("offices", "list"): True,
        ("offices", "get"): None,
        ("job_posts", "list"): True,
        ("job_posts", "get"): None,
        ("sources", "list"): True,
        ("scheduled_interviews", "list"): True,
        ("scheduled_interviews", "get"): None,
        ("application_attachment", "download"): None,
        ("candidate_attachment", "download"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('candidates', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('candidates', 'get'): {'id': 'id'},
        ('applications', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'last_activity_after': 'last_activity_after', 'job_id': 'job_id', 'status': 'status'},
        ('applications', 'get'): {'id': 'id'},
        ('jobs', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('jobs', 'get'): {'id': 'id'},
        ('offers', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'resolved_after': 'resolved_after'},
        ('offers', 'get'): {'id': 'id'},
        ('users', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'updated_before': 'updated_before', 'updated_after': 'updated_after'},
        ('users', 'get'): {'id': 'id'},
        ('departments', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('departments', 'get'): {'id': 'id'},
        ('offices', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('offices', 'get'): {'id': 'id'},
        ('job_posts', 'list'): {'per_page': 'per_page', 'page': 'page', 'live': 'live', 'active': 'active'},
        ('job_posts', 'get'): {'id': 'id'},
        ('sources', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('scheduled_interviews', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'updated_before': 'updated_before', 'updated_after': 'updated_after', 'starts_after': 'starts_after', 'ends_before': 'ends_before'},
        ('scheduled_interviews', 'get'): {'id': 'id'},
        ('application_attachment', 'download'): {'id': 'id', 'attachment_index': 'attachment_index', 'range_header': 'range_header'},
        ('candidate_attachment', 'download'): {'id': 'id', 'attachment_index': 'attachment_index', 'range_header': 'range_header'},
    }

    def __init__(
        self,
        auth_config: GreenhouseAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new greenhouse connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide Airbyte credentials with either `connector_id` or `external_user_id`

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (for hosted mode lookup)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            connector_id: Specific connector/source ID (for hosted mode, skips lookup)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GreenhouseConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = GreenhouseConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GreenhouseConnector(
                auth_config=GreenhouseAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: Airbyte credentials + either connector_id OR external_user_id
        is_hosted = airbyte_client_id and airbyte_client_secret and (connector_id or external_user_id)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_id=connector_id,
                external_user_id=external_user_id,
                connector_definition_id=str(GreenhouseConnectorModel.id) if not connector_id else None,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide Airbyte credentials (airbyte_client_id, airbyte_client_secret) with "
                    "connector_id or external_user_id for hosted mode, or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GreenhouseConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.candidates = CandidatesQuery(self)
        self.applications = ApplicationsQuery(self)
        self.jobs = JobsQuery(self)
        self.offers = OffersQuery(self)
        self.users = UsersQuery(self)
        self.departments = DepartmentsQuery(self)
        self.offices = OfficesQuery(self)
        self.job_posts = JobPostsQuery(self)
        self.sources = SourcesQuery(self)
        self.scheduled_interviews = ScheduledInterviewsQuery(self)
        self.application_attachment = ApplicationAttachmentQuery(self)
        self.candidate_attachment = CandidateAttachmentQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["list"],
        params: "CandidatesListParams"
    ) -> "CandidatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["get"],
        params: "CandidatesGetParams"
    ) -> "Candidate": ...

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["list"],
        params: "ApplicationsListParams"
    ) -> "ApplicationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["get"],
        params: "ApplicationsGetParams"
    ) -> "Application": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["list"],
        params: "JobsListParams"
    ) -> "JobsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["get"],
        params: "JobsGetParams"
    ) -> "Job": ...

    @overload
    async def execute(
        self,
        entity: Literal["offers"],
        action: Literal["list"],
        params: "OffersListParams"
    ) -> "OffersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["offers"],
        action: Literal["get"],
        params: "OffersGetParams"
    ) -> "Offer": ...

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
        entity: Literal["departments"],
        action: Literal["list"],
        params: "DepartmentsListParams"
    ) -> "DepartmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["departments"],
        action: Literal["get"],
        params: "DepartmentsGetParams"
    ) -> "Department": ...

    @overload
    async def execute(
        self,
        entity: Literal["offices"],
        action: Literal["list"],
        params: "OfficesListParams"
    ) -> "OfficesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["offices"],
        action: Literal["get"],
        params: "OfficesGetParams"
    ) -> "Office": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_posts"],
        action: Literal["list"],
        params: "JobPostsListParams"
    ) -> "JobPostsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_posts"],
        action: Literal["get"],
        params: "JobPostsGetParams"
    ) -> "JobPost": ...

    @overload
    async def execute(
        self,
        entity: Literal["sources"],
        action: Literal["list"],
        params: "SourcesListParams"
    ) -> "SourcesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["scheduled_interviews"],
        action: Literal["list"],
        params: "ScheduledInterviewsListParams"
    ) -> "ScheduledInterviewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["scheduled_interviews"],
        action: Literal["get"],
        params: "ScheduledInterviewsGetParams"
    ) -> "ScheduledInterview": ...

    @overload
    async def execute(
        self,
        entity: Literal["application_attachment"],
        action: Literal["download"],
        params: "ApplicationAttachmentDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidate_attachment"],
        action: Literal["download"],
        params: "CandidateAttachmentDownloadParams"
    ) -> "AsyncIterator[bytes]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download", "search"],
        params: Mapping[str, Any]
    ) -> GreenhouseExecuteResult[Any] | GreenhouseExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "download", "search"],
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
                return GreenhouseExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GreenhouseExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GreenhouseCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GreenhouseCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GreenhouseCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GreenhouseCheckResult(
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
            @GreenhouseConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GreenhouseConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GreenhouseConnectorModel,
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
        return describe_entities(GreenhouseConnectorModel)

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
            (e for e in GreenhouseConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GreenhouseConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GreenhouseConnector.create_hosted(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create_hosted(
        cls,
        *,
        external_user_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        auth_config: "GreenhouseAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "GreenhouseConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            external_user_id: Workspace identifier in Airbyte Cloud
            airbyte_client_id: Airbyte OAuth client ID
            airbyte_client_secret: Airbyte OAuth client secret
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).

        Returns:
            A GreenhouseConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await GreenhouseConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=GreenhouseAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config
            credentials = auth_config.model_dump(exclude_none=True)
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(GreenhouseConnectorModel.id),
                external_user_id=external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            airbyte_client_id=airbyte_client_id,
            airbyte_client_secret=airbyte_client_secret,
            connector_id=source_id,
        )



class CandidatesQuery:
    """
    Query class for Candidates entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> CandidatesListResult:
        """
        Returns a paginated list of all candidates in the organization

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            CandidatesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "list", params)
        # Cast generic envelope to concrete typed result
        return CandidatesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Candidate:
        """
        Get a single candidate by ID

        Args:
            id: Candidate ID
            **kwargs: Additional parameters

        Returns:
            Candidate
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "get", params)
        return result



    async def search(
        self,
        query: CandidatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CandidatesSearchResult:
        """
        Search candidates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CandidatesSearchFilter):
        - addresses: Candidate's addresses
        - application_ids: List of application IDs
        - applications: An array of all applications made by candidates.
        - attachments: Attachments related to the candidate
        - can_email: Indicates if candidate can be emailed
        - company: Company where the candidate is associated
        - coordinator: Coordinator assigned to the candidate
        - created_at: Date and time of creation
        - custom_fields: Custom fields associated with the candidate
        - educations: List of candidate's educations
        - email_addresses: Candidate's email addresses
        - employments: List of candidate's employments
        - first_name: Candidate's first name
        - id: Candidate's ID
        - is_private: Indicates if the candidate's data is private
        - keyed_custom_fields: Keyed custom fields associated with the candidate
        - last_activity: Details of the last activity related to the candidate
        - last_name: Candidate's last name
        - phone_numbers: Candidate's phone numbers
        - photo_url: URL of the candidate's profile photo
        - recruiter: Recruiter assigned to the candidate
        - social_media_addresses: Candidate's social media addresses
        - tags: Tags associated with the candidate
        - title: Candidate's title (e.g., Mr., Mrs., Dr.)
        - updated_at: Date and time of last update
        - website_addresses: List of candidate's website addresses

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CandidatesSearchResult with hits (list of AirbyteSearchHit[CandidatesSearchData]) and pagination info

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

        result = await self._connector.execute("candidates", "search", params)

        # Parse response into typed result
        return CandidatesSearchResult(
            hits=[
                AirbyteSearchHit[CandidatesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CandidatesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ApplicationsQuery:
    """
    Query class for Applications entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        last_activity_after: str | None = None,
        job_id: int | None = None,
        status: str | None = None,
        **kwargs
    ) -> ApplicationsListResult:
        """
        Returns a paginated list of all applications

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by applications created before this timestamp
            created_after: Filter by applications created after this timestamp
            last_activity_after: Filter by applications with activity after this timestamp
            job_id: Filter by job ID
            status: Filter by application status
            **kwargs: Additional parameters

        Returns:
            ApplicationsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "last_activity_after": last_activity_after,
            "job_id": job_id,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "list", params)
        # Cast generic envelope to concrete typed result
        return ApplicationsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Application:
        """
        Get a single application by ID

        Args:
            id: Application ID
            **kwargs: Additional parameters

        Returns:
            Application
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "get", params)
        return result



    async def search(
        self,
        query: ApplicationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ApplicationsSearchResult:
        """
        Search applications records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ApplicationsSearchFilter):
        - answers: Answers provided in the application.
        - applied_at: Timestamp when the candidate applied.
        - attachments: Attachments uploaded with the application.
        - candidate_id: Unique identifier for the candidate.
        - credited_to: Information about the employee who credited the application.
        - current_stage: Current stage of the application process.
        - id: Unique identifier for the application.
        - job_post_id: 
        - jobs: Jobs applied for by the candidate.
        - last_activity_at: Timestamp of the last activity on the application.
        - location: Location related to the application.
        - prospect: Status of the application prospect.
        - prospect_detail: Details related to the application prospect.
        - prospective_department: Prospective department for the candidate.
        - prospective_office: Prospective office for the candidate.
        - rejected_at: Timestamp when the application was rejected.
        - rejection_details: Details related to the application rejection.
        - rejection_reason: Reason for the application rejection.
        - source: Source of the application.
        - status: Status of the application.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ApplicationsSearchResult with hits (list of AirbyteSearchHit[ApplicationsSearchData]) and pagination info

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

        result = await self._connector.execute("applications", "search", params)

        # Parse response into typed result
        return ApplicationsSearchResult(
            hits=[
                AirbyteSearchHit[ApplicationsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ApplicationsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class JobsQuery:
    """
    Query class for Jobs entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> JobsListResult:
        """
        Returns a paginated list of all jobs in the organization

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            JobsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "list", params)
        # Cast generic envelope to concrete typed result
        return JobsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Job:
        """
        Get a single job by ID

        Args:
            id: Job ID
            **kwargs: Additional parameters

        Returns:
            Job
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "get", params)
        return result



    async def search(
        self,
        query: JobsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> JobsSearchResult:
        """
        Search jobs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (JobsSearchFilter):
        - closed_at: The date and time the job was closed
        - confidential: Indicates if the job details are confidential
        - copied_from_id: The ID of the job from which this job was copied
        - created_at: The date and time the job was created
        - custom_fields: Custom fields related to the job
        - departments: Departments associated with the job
        - hiring_team: Members of the hiring team for the job
        - id: Unique ID of the job
        - is_template: Indicates if the job is a template
        - keyed_custom_fields: Keyed custom fields related to the job
        - name: Name of the job
        - notes: Additional notes or comments about the job
        - offices: Offices associated with the job
        - opened_at: The date and time the job was opened
        - openings: Openings associated with the job
        - requisition_id: ID associated with the job requisition
        - status: Current status of the job
        - updated_at: The date and time the job was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            JobsSearchResult with hits (list of AirbyteSearchHit[JobsSearchData]) and pagination info

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

        result = await self._connector.execute("jobs", "search", params)

        # Parse response into typed result
        return JobsSearchResult(
            hits=[
                AirbyteSearchHit[JobsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=JobsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class OffersQuery:
    """
    Query class for Offers entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        resolved_after: str | None = None,
        **kwargs
    ) -> OffersListResult:
        """
        Returns a paginated list of all offers

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by offers created before this timestamp
            created_after: Filter by offers created after this timestamp
            resolved_after: Filter by offers resolved after this timestamp
            **kwargs: Additional parameters

        Returns:
            OffersListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "resolved_after": resolved_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offers", "list", params)
        # Cast generic envelope to concrete typed result
        return OffersListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Offer:
        """
        Get a single offer by ID

        Args:
            id: Offer ID
            **kwargs: Additional parameters

        Returns:
            Offer
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offers", "get", params)
        return result



    async def search(
        self,
        query: OffersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OffersSearchResult:
        """
        Search offers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OffersSearchFilter):
        - application_id: Unique identifier for the application associated with the offer
        - candidate_id: Unique identifier for the candidate associated with the offer
        - created_at: Timestamp indicating when the offer was created
        - custom_fields: Additional custom fields related to the offer
        - id: Unique identifier for the offer
        - job_id: Unique identifier for the job associated with the offer
        - keyed_custom_fields: Keyed custom fields associated with the offer
        - opening: Details about the job opening
        - resolved_at: Timestamp indicating when the offer was resolved
        - sent_at: Timestamp indicating when the offer was sent
        - starts_at: Timestamp indicating when the offer starts
        - status: Status of the offer
        - updated_at: Timestamp indicating when the offer was last updated
        - version: Version of the offer data

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OffersSearchResult with hits (list of AirbyteSearchHit[OffersSearchData]) and pagination info

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

        result = await self._connector.execute("offers", "search", params)

        # Parse response into typed result
        return OffersSearchResult(
            hits=[
                AirbyteSearchHit[OffersSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=OffersSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        updated_before: str | None = None,
        updated_after: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a paginated list of all users

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by users created before this timestamp
            created_after: Filter by users created after this timestamp
            updated_before: Filter by users updated before this timestamp
            updated_after: Filter by users updated after this timestamp
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "updated_before": updated_before,
            "updated_after": updated_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> User:
        """
        Get a single user by ID

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
        - created_at: The date and time when the user account was created.
        - departments: List of departments associated with users
        - disabled: Indicates whether the user account is disabled.
        - emails: Email addresses of the users
        - employee_id: Employee identifier for the user.
        - first_name: The first name of the user.
        - id: Unique identifier for the user.
        - last_name: The last name of the user.
        - linked_candidate_ids: IDs of candidates linked to the user.
        - name: The full name of the user.
        - offices: List of office locations where users are based
        - primary_email_address: The primary email address of the user.
        - site_admin: Indicates whether the user is a site administrator.
        - updated_at: The date and time when the user account was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UsersSearchResult with hits (list of AirbyteSearchHit[UsersSearchData]) and pagination info

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
        return UsersSearchResult(
            hits=[
                AirbyteSearchHit[UsersSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=UsersSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class DepartmentsQuery:
    """
    Query class for Departments entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> DepartmentsListResult:
        """
        Returns a paginated list of all departments

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            DepartmentsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "list", params)
        # Cast generic envelope to concrete typed result
        return DepartmentsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Department:
        """
        Get a single department by ID

        Args:
            id: Department ID
            **kwargs: Additional parameters

        Returns:
            Department
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "get", params)
        return result



    async def search(
        self,
        query: DepartmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DepartmentsSearchResult:
        """
        Search departments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DepartmentsSearchFilter):
        - child_department_external_ids: External IDs of child departments associated with this department.
        - child_ids: Unique IDs of child departments associated with this department.
        - external_id: External ID of this department.
        - id: Unique ID of this department.
        - name: Name of the department.
        - parent_department_external_id: External ID of the parent department of this department.
        - parent_id: Unique ID of the parent department of this department.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DepartmentsSearchResult with hits (list of AirbyteSearchHit[DepartmentsSearchData]) and pagination info

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

        result = await self._connector.execute("departments", "search", params)

        # Parse response into typed result
        return DepartmentsSearchResult(
            hits=[
                AirbyteSearchHit[DepartmentsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=DepartmentsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class OfficesQuery:
    """
    Query class for Offices entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> OfficesListResult:
        """
        Returns a paginated list of all offices

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            OfficesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offices", "list", params)
        # Cast generic envelope to concrete typed result
        return OfficesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Office:
        """
        Get a single office by ID

        Args:
            id: Office ID
            **kwargs: Additional parameters

        Returns:
            Office
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offices", "get", params)
        return result



    async def search(
        self,
        query: OfficesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OfficesSearchResult:
        """
        Search offices records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OfficesSearchFilter):
        - child_ids: IDs of child offices associated with this office
        - child_office_external_ids: External IDs of child offices associated with this office
        - external_id: Unique identifier for this office in the external system
        - id: Unique identifier for this office in the API system
        - location: Location details of this office
        - name: Name of the office
        - parent_id: ID of the parent office, if this office is a branch office
        - parent_office_external_id: External ID of the parent office in the external system
        - primary_contact_user_id: User ID of the primary contact person for this office

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OfficesSearchResult with hits (list of AirbyteSearchHit[OfficesSearchData]) and pagination info

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

        result = await self._connector.execute("offices", "search", params)

        # Parse response into typed result
        return OfficesSearchResult(
            hits=[
                AirbyteSearchHit[OfficesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=OfficesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class JobPostsQuery:
    """
    Query class for JobPosts entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        live: bool | None = None,
        active: bool | None = None,
        **kwargs
    ) -> JobPostsListResult:
        """
        Returns a paginated list of all job posts

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            live: Filter by live status
            active: Filter by active status
            **kwargs: Additional parameters

        Returns:
            JobPostsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "live": live,
            "active": active,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_posts", "list", params)
        # Cast generic envelope to concrete typed result
        return JobPostsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> JobPost:
        """
        Get a single job post by ID

        Args:
            id: Job Post ID
            **kwargs: Additional parameters

        Returns:
            JobPost
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_posts", "get", params)
        return result



    async def search(
        self,
        query: JobPostsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> JobPostsSearchResult:
        """
        Search job_posts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (JobPostsSearchFilter):
        - active: Flag indicating if the job post is active or not.
        - content: Content or description of the job post.
        - created_at: Date and time when the job post was created.
        - demographic_question_set_id: ID of the demographic question set associated with the job post.
        - external: Flag indicating if the job post is external or not.
        - first_published_at: Date and time when the job post was first published.
        - id: Unique identifier of the job post.
        - internal: Flag indicating if the job post is internal or not.
        - internal_content: Internal content or description of the job post.
        - job_id: ID of the job associated with the job post.
        - live: Flag indicating if the job post is live or not.
        - location: Details about the job post location.
        - questions: List of questions related to the job post.
        - title: Title or headline of the job post.
        - updated_at: Date and time when the job post was last updated.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            JobPostsSearchResult with hits (list of AirbyteSearchHit[JobPostsSearchData]) and pagination info

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

        result = await self._connector.execute("job_posts", "search", params)

        # Parse response into typed result
        return JobPostsSearchResult(
            hits=[
                AirbyteSearchHit[JobPostsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=JobPostsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class SourcesQuery:
    """
    Query class for Sources entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> SourcesListResult:
        """
        Returns a paginated list of all sources

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            SourcesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sources", "list", params)
        # Cast generic envelope to concrete typed result
        return SourcesListResult(
            data=result.data
        )



    async def search(
        self,
        query: SourcesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SourcesSearchResult:
        """
        Search sources records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SourcesSearchFilter):
        - id: The unique identifier for the source.
        - name: The name of the source.
        - type: Type of the data source

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SourcesSearchResult with hits (list of AirbyteSearchHit[SourcesSearchData]) and pagination info

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

        result = await self._connector.execute("sources", "search", params)

        # Parse response into typed result
        return SourcesSearchResult(
            hits=[
                AirbyteSearchHit[SourcesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=SourcesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ScheduledInterviewsQuery:
    """
    Query class for ScheduledInterviews entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        updated_before: str | None = None,
        updated_after: str | None = None,
        starts_after: str | None = None,
        ends_before: str | None = None,
        **kwargs
    ) -> ScheduledInterviewsListResult:
        """
        Returns a paginated list of all scheduled interviews

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by interviews created before this timestamp
            created_after: Filter by interviews created after this timestamp
            updated_before: Filter by interviews updated before this timestamp
            updated_after: Filter by interviews updated after this timestamp
            starts_after: Filter by interviews starting after this timestamp
            ends_before: Filter by interviews ending before this timestamp
            **kwargs: Additional parameters

        Returns:
            ScheduledInterviewsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "updated_before": updated_before,
            "updated_after": updated_after,
            "starts_after": starts_after,
            "ends_before": ends_before,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("scheduled_interviews", "list", params)
        # Cast generic envelope to concrete typed result
        return ScheduledInterviewsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ScheduledInterview:
        """
        Get a single scheduled interview by ID

        Args:
            id: Scheduled Interview ID
            **kwargs: Additional parameters

        Returns:
            ScheduledInterview
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("scheduled_interviews", "get", params)
        return result



class ApplicationAttachmentQuery:
    """
    Query class for ApplicationAttachment entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        attachment_index: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads an attachment (resume, cover letter, etc.) for an application by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.


        Args:
            id: Application ID
            attachment_index: Index of the attachment to download (0-based)
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "attachment_index": attachment_index,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("application_attachment", "download", params)
        return result


    async def download_local(
        self,
        attachment_index: str,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads an attachment (resume, cover letter, etc.) for an application by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.
 and save to file.

        Args:
            id: Application ID
            attachment_index: Index of the attachment to download (0-based)
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            attachment_index=attachment_index,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class CandidateAttachmentQuery:
    """
    Query class for CandidateAttachment entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        attachment_index: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads an attachment (resume, cover letter, etc.) for a candidate by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.


        Args:
            id: Candidate ID
            attachment_index: Index of the attachment to download (0-based)
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "attachment_index": attachment_index,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidate_attachment", "download", params)
        return result


    async def download_local(
        self,
        attachment_index: str,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads an attachment (resume, cover letter, etc.) for a candidate by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.
 and save to file.

        Args:
            id: Candidate ID
            attachment_index: Index of the attachment to download (0-based)
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            attachment_index=attachment_index,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)

