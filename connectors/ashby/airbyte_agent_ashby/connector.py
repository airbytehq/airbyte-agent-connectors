"""
Ashby connector.
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

from .connector_model import AshbyConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    ApplicationsGetParams,
    ApplicationsListParams,
    ArchiveReasonsListParams,
    CandidateTagsListParams,
    CandidatesGetParams,
    CandidatesListParams,
    CustomFieldsListParams,
    DepartmentsGetParams,
    DepartmentsListParams,
    FeedbackFormDefinitionsListParams,
    JobPostingsGetParams,
    JobPostingsListParams,
    JobsGetParams,
    JobsListParams,
    LocationsGetParams,
    LocationsListParams,
    SourcesListParams,
    UsersGetParams,
    UsersListParams,
)
from .models import AshbyAuthConfig
if TYPE_CHECKING:
    from .models import AshbyReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    AshbyCheckResult,
    AshbyExecuteResult,
    AshbyExecuteResultWithMeta,
    CandidatesListResult,
    ApplicationsListResult,
    JobsListResult,
    DepartmentsListResult,
    LocationsListResult,
    UsersListResult,
    JobPostingsListResult,
    SourcesListResult,
    ArchiveReasonsListResult,
    CandidateTagsListResult,
    CustomFieldsListResult,
    FeedbackFormDefinitionsListResult,
    Application,
    ArchiveReason,
    Candidate,
    CandidateTag,
    CustomField,
    Department,
    FeedbackFormDefinition,
    Job,
    JobPosting,
    Location,
    Source,
    User,
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




class AshbyConnector:
    """
    Type-safe Ashby API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "ashby"
    connector_version = "0.1.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("candidates", "list"): True,
        ("candidates", "get"): None,
        ("applications", "list"): True,
        ("applications", "get"): None,
        ("jobs", "list"): True,
        ("jobs", "get"): None,
        ("departments", "list"): True,
        ("departments", "get"): None,
        ("locations", "list"): True,
        ("locations", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("job_postings", "list"): True,
        ("job_postings", "get"): None,
        ("sources", "list"): True,
        ("archive_reasons", "list"): True,
        ("candidate_tags", "list"): True,
        ("custom_fields", "list"): True,
        ("feedback_form_definitions", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('candidates', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('candidates', 'get'): {'id': 'id'},
        ('applications', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('applications', 'get'): {'application_id': 'applicationId'},
        ('jobs', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('jobs', 'get'): {'id': 'id'},
        ('departments', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('departments', 'get'): {'department_id': 'departmentId'},
        ('locations', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('locations', 'get'): {'location_id': 'locationId'},
        ('users', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('users', 'get'): {'user_id': 'userId'},
        ('job_postings', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('job_postings', 'get'): {'job_posting_id': 'jobPostingId'},
        ('sources', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('archive_reasons', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('candidate_tags', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('custom_fields', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
        ('feedback_form_definitions', 'list'): {'cursor': 'cursor', 'limit': 'limit'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (AshbyAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: AshbyAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new ashby connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., AshbyAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `external_user_id`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = AshbyConnector(auth_config=AshbyAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = AshbyConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by external_user_id
            connector = AshbyConnector(
                auth_config=AirbyteAuthConfig(
                    external_user_id="user-123",
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
                external_user_id=auth_config.external_user_id,
                connector_definition_id=str(AshbyConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or AshbyAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=AshbyConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.candidates = CandidatesQuery(self)
        self.applications = ApplicationsQuery(self)
        self.jobs = JobsQuery(self)
        self.departments = DepartmentsQuery(self)
        self.locations = LocationsQuery(self)
        self.users = UsersQuery(self)
        self.job_postings = JobPostingsQuery(self)
        self.sources = SourcesQuery(self)
        self.archive_reasons = ArchiveReasonsQuery(self)
        self.candidate_tags = CandidateTagsQuery(self)
        self.custom_fields = CustomFieldsQuery(self)
        self.feedback_form_definitions = FeedbackFormDefinitionsQuery(self)

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
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["locations"],
        action: Literal["list"],
        params: "LocationsListParams"
    ) -> "LocationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["locations"],
        action: Literal["get"],
        params: "LocationsGetParams"
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_postings"],
        action: Literal["list"],
        params: "JobPostingsListParams"
    ) -> "JobPostingsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_postings"],
        action: Literal["get"],
        params: "JobPostingsGetParams"
    ) -> "dict[str, Any]": ...

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
        entity: Literal["archive_reasons"],
        action: Literal["list"],
        params: "ArchiveReasonsListParams"
    ) -> "ArchiveReasonsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidate_tags"],
        action: Literal["list"],
        params: "CandidateTagsListParams"
    ) -> "CandidateTagsListResult": ...

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
        entity: Literal["feedback_form_definitions"],
        action: Literal["list"],
        params: "FeedbackFormDefinitionsListParams"
    ) -> "FeedbackFormDefinitionsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get"],
        params: Mapping[str, Any]
    ) -> AshbyExecuteResult[Any] | AshbyExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get"],
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
                return AshbyExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return AshbyExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> AshbyCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            AshbyCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return AshbyCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return AshbyCheckResult(
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
            @AshbyConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @AshbyConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    AshbyConnectorModel,
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
        return describe_entities(AshbyConnectorModel)

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
            (e for e in AshbyConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in AshbyConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await AshbyConnector.create(...)
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
        auth_config: "AshbyAuthConfig",
        name: str | None = None,
        replication_config: "AshbyReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "AshbyConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and external_user_id.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A AshbyConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await AshbyConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AshbyAuthConfig(api_key="..."),
            )

            # With replication config (required for this connector):
            connector = await AshbyConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AshbyAuthConfig(api_key="..."),
                replication_config=AshbyReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.external_user_id:
            raise ValueError("airbyte_config.external_user_id is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(AshbyConnectorModel.id),
                external_user_id=airbyte_config.external_user_id,
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
                connector_id=source_id,
            ),
        )




class CandidatesQuery:
    """
    Query class for Candidates entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> CandidatesListResult:
        """
        Lists all candidates in the organization

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            CandidatesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "list", params)
        # Cast generic envelope to concrete typed result
        return CandidatesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single candidate by ID

        Args:
            id: Candidate ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "get", params)
        return result



class ApplicationsQuery:
    """
    Query class for Applications entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> ApplicationsListResult:
        """
        Gets all applications in the organization

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            ApplicationsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "list", params)
        # Cast generic envelope to concrete typed result
        return ApplicationsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        application_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single application by ID

        Args:
            application_id: Application ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "applicationId": application_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "get", params)
        return result



class JobsQuery:
    """
    Query class for Jobs entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> JobsListResult:
        """
        List all open, closed, and archived jobs

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            JobsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "list", params)
        # Cast generic envelope to concrete typed result
        return JobsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single job by ID

        Args:
            id: Job ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "get", params)
        return result



class DepartmentsQuery:
    """
    Query class for Departments entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> DepartmentsListResult:
        """
        List all departments

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            DepartmentsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "list", params)
        # Cast generic envelope to concrete typed result
        return DepartmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        department_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single department by ID

        Args:
            department_id: Department ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "departmentId": department_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "get", params)
        return result



class LocationsQuery:
    """
    Query class for Locations entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> LocationsListResult:
        """
        List all locations

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            LocationsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("locations", "list", params)
        # Cast generic envelope to concrete typed result
        return LocationsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        location_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single location by ID

        Args:
            location_id: Location ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "locationId": location_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("locations", "get", params)
        return result



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        List all users in the organization

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
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
        user_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single user by ID

        Args:
            user_id: User ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "userId": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



class JobPostingsQuery:
    """
    Query class for JobPostings entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> JobPostingsListResult:
        """
        List all job postings

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            JobPostingsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_postings", "list", params)
        # Cast generic envelope to concrete typed result
        return JobPostingsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        job_posting_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single job posting by ID

        Args:
            job_posting_id: Job posting ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "jobPostingId": job_posting_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_postings", "get", params)
        return result



class SourcesQuery:
    """
    Query class for Sources entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> SourcesListResult:
        """
        List all candidate sources

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            SourcesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sources", "list", params)
        # Cast generic envelope to concrete typed result
        return SourcesListResult(
            data=result.data,
            meta=result.meta
        )



class ArchiveReasonsQuery:
    """
    Query class for ArchiveReasons entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> ArchiveReasonsListResult:
        """
        List all archive reasons

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            ArchiveReasonsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("archive_reasons", "list", params)
        # Cast generic envelope to concrete typed result
        return ArchiveReasonsListResult(
            data=result.data,
            meta=result.meta
        )



class CandidateTagsQuery:
    """
    Query class for CandidateTags entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> CandidateTagsListResult:
        """
        List all candidate tags

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            CandidateTagsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidate_tags", "list", params)
        # Cast generic envelope to concrete typed result
        return CandidateTagsListResult(
            data=result.data,
            meta=result.meta
        )



class CustomFieldsQuery:
    """
    Query class for CustomFields entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> CustomFieldsListResult:
        """
        List all custom fields

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            CustomFieldsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomFieldsListResult(
            data=result.data,
            meta=result.meta
        )



class FeedbackFormDefinitionsQuery:
    """
    Query class for FeedbackFormDefinitions entity operations.
    """

    def __init__(self, connector: AshbyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        **kwargs
    ) -> FeedbackFormDefinitionsListResult:
        """
        List all feedback form definitions

        Args:
            cursor: Pagination cursor for next page
            limit: Maximum number of records to return per page
            **kwargs: Additional parameters

        Returns:
            FeedbackFormDefinitionsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("feedback_form_definitions", "list", params)
        # Cast generic envelope to concrete typed result
        return FeedbackFormDefinitionsListResult(
            data=result.data,
            meta=result.meta
        )


