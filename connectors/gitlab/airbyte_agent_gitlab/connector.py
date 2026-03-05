"""
Gitlab connector.
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

from .connector_model import GitlabConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    BranchesGetParams,
    BranchesListParams,
    CommitsGetParams,
    CommitsListParams,
    GroupMembersGetParams,
    GroupMembersListParams,
    GroupMilestonesGetParams,
    GroupMilestonesListParams,
    GroupsGetParams,
    GroupsListParams,
    IssuesGetParams,
    IssuesListParams,
    MergeRequestsGetParams,
    MergeRequestsListParams,
    PipelinesGetParams,
    PipelinesListParams,
    ProjectMembersGetParams,
    ProjectMembersListParams,
    ProjectMilestonesGetParams,
    ProjectMilestonesListParams,
    ProjectsGetParams,
    ProjectsListParams,
    ReleasesGetParams,
    ReleasesListParams,
    TagsGetParams,
    TagsListParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    IssuesSearchFilter,
    IssuesSearchQuery,
    MergeRequestsSearchFilter,
    MergeRequestsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    CommitsSearchFilter,
    CommitsSearchQuery,
    GroupsSearchFilter,
    GroupsSearchQuery,
    BranchesSearchFilter,
    BranchesSearchQuery,
    PipelinesSearchFilter,
    PipelinesSearchQuery,
    GroupMembersSearchFilter,
    GroupMembersSearchQuery,
    ProjectMembersSearchFilter,
    ProjectMembersSearchQuery,
    ReleasesSearchFilter,
    ReleasesSearchQuery,
    TagsSearchFilter,
    TagsSearchQuery,
    GroupMilestonesSearchFilter,
    GroupMilestonesSearchQuery,
    ProjectMilestonesSearchFilter,
    ProjectMilestonesSearchQuery,
)
from .models import GitlabPersonalAccessTokenAuthConfig, GitlabOauth20AuthConfig
from .models import GitlabAuthConfig
if TYPE_CHECKING:
    from .models import GitlabReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    GitlabCheckResult,
    GitlabExecuteResult,
    GitlabExecuteResultWithMeta,
    ProjectsListResult,
    IssuesListResult,
    MergeRequestsListResult,
    UsersListResult,
    CommitsListResult,
    GroupsListResult,
    BranchesListResult,
    PipelinesListResult,
    GroupMembersListResult,
    ProjectMembersListResult,
    ReleasesListResult,
    TagsListResult,
    GroupMilestonesListResult,
    ProjectMilestonesListResult,
    Branch,
    Commit,
    Group,
    Issue,
    Member,
    MergeRequest,
    Milestone,
    Pipeline,
    Project,
    Release,
    Tag,
    User,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    IssuesSearchData,
    IssuesSearchResult,
    MergeRequestsSearchData,
    MergeRequestsSearchResult,
    UsersSearchData,
    UsersSearchResult,
    CommitsSearchData,
    CommitsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
    BranchesSearchData,
    BranchesSearchResult,
    PipelinesSearchData,
    PipelinesSearchResult,
    GroupMembersSearchData,
    GroupMembersSearchResult,
    ProjectMembersSearchData,
    ProjectMembersSearchResult,
    ReleasesSearchData,
    ReleasesSearchResult,
    TagsSearchData,
    TagsSearchResult,
    GroupMilestonesSearchData,
    GroupMilestonesSearchResult,
    ProjectMilestonesSearchData,
    ProjectMilestonesSearchResult,
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




class GitlabConnector:
    """
    Type-safe Gitlab API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "gitlab"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("projects", "list"): True,
        ("projects", "get"): None,
        ("issues", "list"): True,
        ("issues", "get"): None,
        ("merge_requests", "list"): True,
        ("merge_requests", "get"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("commits", "list"): True,
        ("commits", "get"): None,
        ("groups", "list"): True,
        ("groups", "get"): None,
        ("branches", "list"): True,
        ("branches", "get"): None,
        ("pipelines", "list"): True,
        ("pipelines", "get"): None,
        ("group_members", "list"): True,
        ("group_members", "get"): None,
        ("project_members", "list"): True,
        ("project_members", "get"): None,
        ("releases", "list"): True,
        ("releases", "get"): None,
        ("tags", "list"): True,
        ("tags", "get"): None,
        ("group_milestones", "list"): True,
        ("group_milestones", "get"): None,
        ("project_milestones", "list"): True,
        ("project_milestones", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('projects', 'list'): {'page': 'page', 'per_page': 'per_page', 'membership': 'membership', 'owned': 'owned', 'search': 'search', 'order_by': 'order_by', 'sort': 'sort'},
        ('projects', 'get'): {'id': 'id', 'statistics': 'statistics'},
        ('issues', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'state': 'state', 'scope': 'scope', 'order_by': 'order_by', 'sort': 'sort', 'created_after': 'created_after', 'created_before': 'created_before', 'updated_after': 'updated_after', 'updated_before': 'updated_before'},
        ('issues', 'get'): {'project_id': 'project_id', 'issue_iid': 'issue_iid'},
        ('merge_requests', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'state': 'state', 'scope': 'scope', 'order_by': 'order_by', 'sort': 'sort', 'created_after': 'created_after', 'created_before': 'created_before', 'updated_after': 'updated_after', 'updated_before': 'updated_before'},
        ('merge_requests', 'get'): {'project_id': 'project_id', 'merge_request_iid': 'merge_request_iid'},
        ('users', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'active': 'active'},
        ('users', 'get'): {'id': 'id'},
        ('commits', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'ref_name': 'ref_name', 'since': 'since', 'until': 'until', 'with_stats': 'with_stats'},
        ('commits', 'get'): {'project_id': 'project_id', 'sha': 'sha', 'stats': 'stats'},
        ('groups', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'owned': 'owned', 'order_by': 'order_by', 'sort': 'sort'},
        ('groups', 'get'): {'id': 'id'},
        ('branches', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'search': 'search'},
        ('branches', 'get'): {'project_id': 'project_id', 'branch': 'branch'},
        ('pipelines', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'status': 'status', 'ref': 'ref', 'order_by': 'order_by', 'sort': 'sort'},
        ('pipelines', 'get'): {'project_id': 'project_id', 'pipeline_id': 'pipeline_id'},
        ('group_members', 'list'): {'group_id': 'group_id', 'page': 'page', 'per_page': 'per_page', 'query': 'query'},
        ('group_members', 'get'): {'group_id': 'group_id', 'user_id': 'user_id'},
        ('project_members', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'query': 'query'},
        ('project_members', 'get'): {'project_id': 'project_id', 'user_id': 'user_id'},
        ('releases', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'order_by': 'order_by', 'sort': 'sort'},
        ('releases', 'get'): {'project_id': 'project_id', 'tag_name': 'tag_name'},
        ('tags', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'search': 'search', 'order_by': 'order_by', 'sort': 'sort'},
        ('tags', 'get'): {'project_id': 'project_id', 'tag_name': 'tag_name'},
        ('group_milestones', 'list'): {'group_id': 'group_id', 'page': 'page', 'per_page': 'per_page', 'state': 'state', 'search': 'search'},
        ('group_milestones', 'get'): {'group_id': 'group_id', 'milestone_id': 'milestone_id'},
        ('project_milestones', 'list'): {'project_id': 'project_id', 'page': 'page', 'per_page': 'per_page', 'state': 'state', 'search': 'search'},
        ('project_milestones', 'get'): {'project_id': 'project_id', 'milestone_id': 'milestone_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GitlabPersonalAccessTokenAuthConfig, GitlabOauth20AuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GitlabAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        api_url: str | None = None    ):
        """
        Initialize a new gitlab connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GitlabAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            api_url: GitLab instance hostname
        Examples:
            # Local mode (direct API calls)
            connector = GitlabConnector(auth_config=GitlabAuthConfig(access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GitlabConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = GitlabConnector(
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
                connector_definition_id=str(GitlabConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GitlabAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if api_url:
                config_values["api_url"] = api_url

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, GitlabPersonalAccessTokenAuthConfig):
                    auth_scheme = "gitlabPAT"
                if isinstance(auth_config, GitlabOauth20AuthConfig):
                    auth_scheme = "gitlabOAuth"

            self._executor = LocalExecutor(
                model=GitlabConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if api_url:
                base_url = base_url.replace("{api_url}", api_url)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.projects = ProjectsQuery(self)
        self.issues = IssuesQuery(self)
        self.merge_requests = MergeRequestsQuery(self)
        self.users = UsersQuery(self)
        self.commits = CommitsQuery(self)
        self.groups = GroupsQuery(self)
        self.branches = BranchesQuery(self)
        self.pipelines = PipelinesQuery(self)
        self.group_members = GroupMembersQuery(self)
        self.project_members = ProjectMembersQuery(self)
        self.releases = ReleasesQuery(self)
        self.tags = TagsQuery(self)
        self.group_milestones = GroupMilestonesQuery(self)
        self.project_milestones = ProjectMilestonesQuery(self)

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
    ) -> "Project": ...

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
        entity: Literal["merge_requests"],
        action: Literal["list"],
        params: "MergeRequestsListParams"
    ) -> "MergeRequestsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["merge_requests"],
        action: Literal["get"],
        params: "MergeRequestsGetParams"
    ) -> "MergeRequest": ...

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
        entity: Literal["commits"],
        action: Literal["list"],
        params: "CommitsListParams"
    ) -> "CommitsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["commits"],
        action: Literal["get"],
        params: "CommitsGetParams"
    ) -> "Commit": ...

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
        entity: Literal["branches"],
        action: Literal["list"],
        params: "BranchesListParams"
    ) -> "BranchesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["branches"],
        action: Literal["get"],
        params: "BranchesGetParams"
    ) -> "Branch": ...

    @overload
    async def execute(
        self,
        entity: Literal["pipelines"],
        action: Literal["list"],
        params: "PipelinesListParams"
    ) -> "PipelinesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pipelines"],
        action: Literal["get"],
        params: "PipelinesGetParams"
    ) -> "Pipeline": ...

    @overload
    async def execute(
        self,
        entity: Literal["group_members"],
        action: Literal["list"],
        params: "GroupMembersListParams"
    ) -> "GroupMembersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["group_members"],
        action: Literal["get"],
        params: "GroupMembersGetParams"
    ) -> "Member": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_members"],
        action: Literal["list"],
        params: "ProjectMembersListParams"
    ) -> "ProjectMembersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_members"],
        action: Literal["get"],
        params: "ProjectMembersGetParams"
    ) -> "Member": ...

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
        entity: Literal["tags"],
        action: Literal["list"],
        params: "TagsListParams"
    ) -> "TagsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tags"],
        action: Literal["get"],
        params: "TagsGetParams"
    ) -> "Tag": ...

    @overload
    async def execute(
        self,
        entity: Literal["group_milestones"],
        action: Literal["list"],
        params: "GroupMilestonesListParams"
    ) -> "GroupMilestonesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["group_milestones"],
        action: Literal["get"],
        params: "GroupMilestonesGetParams"
    ) -> "Milestone": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_milestones"],
        action: Literal["list"],
        params: "ProjectMilestonesListParams"
    ) -> "ProjectMilestonesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_milestones"],
        action: Literal["get"],
        params: "ProjectMilestonesGetParams"
    ) -> "Milestone": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> GitlabExecuteResult[Any] | GitlabExecuteResultWithMeta[Any, Any] | Any: ...

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
                return GitlabExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GitlabExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GitlabCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GitlabCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GitlabCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GitlabCheckResult(
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
            @GitlabConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GitlabConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GitlabConnectorModel,
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
        return describe_entities(GitlabConnectorModel)

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
            (e for e in GitlabConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GitlabConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GitlabConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def get_consent_url(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        redirect_url: str,
        name: str | None = None,
        replication_config: "GitlabReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + customer_name.
            replication_config: Typed replication settings. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await GitlabConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Gitlab Source",
                replication_config=GitlabReplicationConfig(start_date="..."),
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for get_consent_url()")

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(GitlabConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                redirect_url=redirect_url,
                name=name,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        return consent_url

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "GitlabAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GitlabReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GitlabConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A GitlabConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GitlabConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GitlabAuthConfig(access_token="..."),
            )

            # With replication config (required for this connector):
            connector = await GitlabConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GitlabAuthConfig(access_token="..."),
                replication_config=GitlabReplicationConfig(start_date="..."),
            )

            # With server-side OAuth:
            connector = await GitlabConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GitlabReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")

        # Validate: exactly one of auth_config or server_side_oauth_secret_id required
        if auth_config is None and server_side_oauth_secret_id is None:
            raise ValueError(
                "Either auth_config or server_side_oauth_secret_id must be provided"
            )
        if auth_config is not None and server_side_oauth_secret_id is not None:
            raise ValueError(
                "Cannot provide both auth_config and server_side_oauth_secret_id"
            )

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
                connector_definition_id=str(GitlabConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
                replication_config=replication_config_dict,
                server_side_oauth_secret_id=server_side_oauth_secret_id,
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

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        membership: bool | None = None,
        owned: bool | None = None,
        search: str | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> ProjectsListResult:
        """
        Get a list of all visible projects across GitLab for the authenticated user.

        Args:
            page: Page number (1-indexed)
            per_page: Number of items per page (max 100)
            membership: Limit by projects that the current user is a member of
            owned: Limit by projects explicitly owned by the current user
            search: Return list of projects matching the search criteria
            order_by: Return projects ordered by field
            sort: Return projects sorted in asc or desc order
            **kwargs: Additional parameters

        Returns:
            ProjectsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "membership": membership,
            "owned": owned,
            "search": search,
            "order_by": order_by,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        statistics: bool | None = None,
        **kwargs
    ) -> Project:
        """
        Get a specific project by ID.

        Args:
            id: The ID or URL-encoded path of the project
            statistics: Include project statistics
            **kwargs: Additional parameters

        Returns:
            Project
        """
        params = {k: v for k, v in {
            "id": id,
            "statistics": statistics,
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
        - id: ID of the project
        - description: Description of the project
        - description_html: HTML-rendered description of the project
        - name: Name of the project
        - name_with_namespace: Full name including namespace
        - path: URL path of the project
        - path_with_namespace: Full path including namespace
        - created_at: Timestamp when the project was created
        - updated_at: Timestamp when the project was last updated
        - default_branch: Default branch of the project
        - tag_list: List of tags for the project
        - topics: List of topics for the project
        - ssh_url_to_repo: SSH URL to the repository
        - http_url_to_repo: HTTP URL to the repository
        - web_url: Web URL of the project
        - readme_url: URL to the project README
        - avatar_url: URL of the project avatar
        - forks_count: Number of forks
        - star_count: Number of stars
        - last_activity_at: Timestamp of last activity
        - namespace: Namespace the project belongs to
        - container_registry_image_prefix: Prefix for container registry images
        - links: Related resource links
        - packages_enabled: Whether packages are enabled
        - empty_repo: Whether the repository is empty
        - archived: Whether the project is archived
        - visibility: Visibility level of the project
        - resolve_outdated_diff_discussions: Whether outdated diff discussions are auto-resolved
        - container_registry_enabled: Whether container registry is enabled
        - container_expiration_policy: Container expiration policy settings
        - issues_enabled: Whether issues are enabled
        - merge_requests_enabled: Whether merge requests are enabled
        - wiki_enabled: Whether wiki is enabled
        - jobs_enabled: Whether jobs are enabled
        - snippets_enabled: Whether snippets are enabled
        - service_desk_enabled: Whether service desk is enabled
        - service_desk_address: Email address for the service desk
        - can_create_merge_request_in: Whether user can create merge requests
        - issues_access_level: Access level for issues
        - repository_access_level: Access level for the repository
        - merge_requests_access_level: Access level for merge requests
        - forking_access_level: Access level for forking
        - wiki_access_level: Access level for the wiki
        - builds_access_level: Access level for builds
        - snippets_access_level: Access level for snippets
        - pages_access_level: Access level for pages
        - operations_access_level: Access level for operations
        - analytics_access_level: Access level for analytics
        - emails_disabled: Whether emails are disabled
        - shared_runners_enabled: Whether shared runners are enabled
        - lfs_enabled: Whether Git LFS is enabled
        - creator_id: ID of the project creator
        - import_status: Import status of the project
        - open_issues_count: Number of open issues
        - ci_default_git_depth: Default git depth for CI pipelines
        - ci_forward_deployment_enabled: Whether CI forward deployment is enabled
        - public_jobs: Whether jobs are public
        - build_timeout: Build timeout in seconds
        - auto_cancel_pending_pipelines: Auto-cancel pending pipelines setting
        - ci_config_path: Path to the CI configuration file
        - shared_with_groups: Groups the project is shared with
        - only_allow_merge_if_pipeline_succeeds: Whether merge requires pipeline success
        - allow_merge_on_skipped_pipeline: Whether merge is allowed on skipped pipeline
        - restrict_user_defined_variables: Whether user-defined variables are restricted
        - request_access_enabled: Whether access requests are enabled
        - only_allow_merge_if_all_discussions_are_resolved: Whether merge requires all discussions resolved
        - remove_source_branch_after_merge: Whether source branch is removed after merge
        - printing_merge_request_link_enabled: Whether MR link printing is enabled
        - merge_method: Merge method used for the project
        - statistics: Project statistics
        - auto_devops_enabled: Whether Auto DevOps is enabled
        - auto_devops_deploy_strategy: Auto DevOps deployment strategy
        - autoclose_referenced_issues: Whether referenced issues are auto-closed
        - external_authorization_classification_label: External authorization classification label
        - requirements_enabled: Whether requirements are enabled
        - security_and_compliance_enabled: Whether security and compliance is enabled
        - compliance_frameworks: Compliance frameworks for the project
        - permissions: User permissions for the project
        - keep_latest_artifact: Whether the latest artifact is kept

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

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        state: str | None = None,
        scope: str | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        updated_after: str | None = None,
        updated_before: str | None = None,
        **kwargs
    ) -> IssuesListResult:
        """
        Get a list of a project's issues.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            state: Filter issues by state
            scope: Filter issues by scope
            order_by: Return issues ordered by field
            sort: Return issues sorted in asc or desc order
            created_after: Return issues created on or after the given time (ISO 8601 format)
            created_before: Return issues created on or before the given time (ISO 8601 format)
            updated_after: Return issues updated on or after the given time (ISO 8601 format)
            updated_before: Return issues updated on or before the given time (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            IssuesListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "state": state,
            "scope": scope,
            "order_by": order_by,
            "sort": sort,
            "created_after": created_after,
            "created_before": created_before,
            "updated_after": updated_after,
            "updated_before": updated_before,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        # Cast generic envelope to concrete typed result
        return IssuesListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        issue_iid: str,
        **kwargs
    ) -> Issue:
        """
        Get a single project issue.

        Args:
            project_id: The ID or URL-encoded path of the project
            issue_iid: The internal ID of a project's issue
            **kwargs: Additional parameters

        Returns:
            Issue
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "issue_iid": issue_iid,
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
        - id: ID of the issue
        - iid: Internal ID of the issue within the project
        - project_id: ID of the project the issue belongs to
        - title: Title of the issue
        - description: Description of the issue
        - state: State of the issue
        - created_at: Timestamp when the issue was created
        - updated_at: Timestamp when the issue was last updated
        - closed_at: Timestamp when the issue was closed
        - labels: Labels assigned to the issue
        - assignees: Users assigned to the issue
        - type_: Type of the issue
        - user_notes_count: Number of user notes on the issue
        - merge_requests_count: Number of related merge requests
        - upvotes: Number of upvotes
        - downvotes: Number of downvotes
        - due_date: Due date for the issue
        - confidential: Whether the issue is confidential
        - discussion_locked: Whether discussion is locked
        - issue_type: Type classification of the issue
        - web_url: Web URL of the issue
        - time_stats: Time tracking statistics
        - task_completion_status: Task completion status
        - blocking_issues_count: Number of blocking issues
        - has_tasks: Whether the issue has tasks
        - links: Related resource links
        - references: Issue references
        - author: Author of the issue
        - author_id: ID of the author
        - assignee: Primary assignee of the issue
        - assignee_id: ID of the primary assignee
        - closed_by: User who closed the issue
        - closed_by_id: ID of the user who closed the issue
        - milestone: Milestone the issue belongs to
        - milestone_id: ID of the milestone
        - weight: Weight of the issue
        - severity: Severity level of the issue

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

class MergeRequestsQuery:
    """
    Query class for MergeRequests entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        state: str | None = None,
        scope: str | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        updated_after: str | None = None,
        updated_before: str | None = None,
        **kwargs
    ) -> MergeRequestsListResult:
        """
        Get all merge requests for a project.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            state: Filter merge requests by state
            scope: Filter merge requests by scope
            order_by: Return merge requests ordered by field
            sort: Return merge requests sorted in asc or desc order
            created_after: Return merge requests created on or after the given time (ISO 8601 format)
            created_before: Return merge requests created on or before the given time (ISO 8601 format)
            updated_after: Return merge requests updated on or after the given time (ISO 8601 format)
            updated_before: Return merge requests updated on or before the given time (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            MergeRequestsListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "state": state,
            "scope": scope,
            "order_by": order_by,
            "sort": sort,
            "created_after": created_after,
            "created_before": created_before,
            "updated_after": updated_after,
            "updated_before": updated_before,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("merge_requests", "list", params)
        # Cast generic envelope to concrete typed result
        return MergeRequestsListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        merge_request_iid: str,
        **kwargs
    ) -> MergeRequest:
        """
        Get information about a single merge request.

        Args:
            project_id: The ID or URL-encoded path of the project
            merge_request_iid: The internal ID of the merge request
            **kwargs: Additional parameters

        Returns:
            MergeRequest
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "merge_request_iid": merge_request_iid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("merge_requests", "get", params)
        return result



    async def search(
        self,
        query: MergeRequestsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MergeRequestsSearchResult:
        """
        Search merge_requests records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MergeRequestsSearchFilter):
        - id: ID of the merge request
        - iid: Internal ID of the merge request within the project
        - project_id: ID of the project
        - title: Title of the merge request
        - description: Description of the merge request
        - state: State of the merge request
        - created_at: Timestamp when the merge request was created
        - updated_at: Timestamp when the merge request was last updated
        - merged_at: Timestamp when the merge request was merged
        - closed_at: Timestamp when the merge request was closed
        - target_branch: Target branch for the merge request
        - source_branch: Source branch for the merge request
        - user_notes_count: Number of user notes
        - upvotes: Number of upvotes
        - downvotes: Number of downvotes
        - assignees: Users assigned to the merge request
        - reviewers: Users assigned as reviewers
        - source_project_id: ID of the source project
        - target_project_id: ID of the target project
        - labels: Labels assigned to the merge request
        - work_in_progress: Whether the merge request is a work in progress
        - merge_when_pipeline_succeeds: Whether to merge when pipeline succeeds
        - merge_status: Merge status of the merge request
        - sha: SHA of the head commit
        - merge_commit_sha: SHA of the merge commit
        - squash_commit_sha: SHA of the squash commit
        - discussion_locked: Whether discussion is locked
        - should_remove_source_branch: Whether source branch should be removed
        - force_remove_source_branch: Whether to force remove source branch
        - reference: Short reference for the merge request
        - references: Merge request references
        - web_url: Web URL of the merge request
        - time_stats: Time tracking statistics
        - squash: Whether to squash commits on merge
        - task_completion_status: Task completion status
        - has_conflicts: Whether the merge request has conflicts
        - blocking_discussions_resolved: Whether blocking discussions are resolved
        - author: Author of the merge request
        - author_id: ID of the author
        - assignee: Primary assignee of the merge request
        - assignee_id: ID of the primary assignee
        - closed_by: User who closed the merge request
        - closed_by_id: ID of the user who closed it
        - milestone: Milestone the merge request belongs to
        - milestone_id: ID of the milestone
        - merged_by: User who merged the merge request
        - merged_by_id: ID of the user who merged it
        - draft: Whether the merge request is a draft
        - detailed_merge_status: Detailed merge status
        - merge_user: User who performed the merge

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MergeRequestsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("merge_requests", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MergeRequestsSearchResult(
            data=[
                MergeRequestsSearchData(**row)
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

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        active: bool | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Get a list of users.

        Args:
            page: Page number
            per_page: Number of items per page
            search: Search for users by name, username, or email
            active: Filter users by active state
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "active": active,
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
        Get a single user by ID.

        Args:
            id: The ID of the user
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
        - id: ID of the user
        - name: Full name of the user
        - username: Username of the user
        - state: State of the user account
        - avatar_url: URL of the user avatar
        - web_url: Web URL of the user profile
        - locked: Whether the user account is locked

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

class CommitsQuery:
    """
    Query class for Commits entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        ref_name: str | None = None,
        since: str | None = None,
        until: str | None = None,
        with_stats: bool | None = None,
        **kwargs
    ) -> CommitsListResult:
        """
        Get a list of repository commits in a project.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            ref_name: The name of a repository branch, tag, or revision range
            since: Only commits after or on this date (ISO 8601)
            until: Only commits before or on this date (ISO 8601)
            with_stats: Include stats about each commit
            **kwargs: Additional parameters

        Returns:
            CommitsListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "ref_name": ref_name,
            "since": since,
            "until": until,
            "with_stats": with_stats,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("commits", "list", params)
        # Cast generic envelope to concrete typed result
        return CommitsListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        sha: str,
        stats: bool | None = None,
        **kwargs
    ) -> Commit:
        """
        Get a specific commit identified by the commit hash or name of a branch or tag.

        Args:
            project_id: The ID or URL-encoded path of the project
            sha: The commit hash or name of a repository branch or tag
            stats: Include commit stats
            **kwargs: Additional parameters

        Returns:
            Commit
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "sha": sha,
            "stats": stats,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("commits", "get", params)
        return result



    async def search(
        self,
        query: CommitsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CommitsSearchResult:
        """
        Search commits records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CommitsSearchFilter):
        - project_id: ID of the project the commit belongs to
        - id: SHA of the commit
        - short_id: Short SHA of the commit
        - created_at: Timestamp when the commit was created
        - parent_ids: SHAs of parent commits
        - title: Title of the commit
        - message: Full commit message
        - author_name: Name of the commit author
        - author_email: Email of the commit author
        - authored_date: Date the commit was authored
        - committer_name: Name of the committer
        - committer_email: Email of the committer
        - committed_date: Date the commit was committed
        - trailers: Git trailers for the commit
        - web_url: Web URL of the commit
        - stats: Commit statistics

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CommitsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("commits", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CommitsSearchResult(
            data=[
                CommitsSearchData(**row)
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

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        owned: bool | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> GroupsListResult:
        """
        Get a list of visible groups for the authenticated user.

        Args:
            page: Page number
            per_page: Number of items per page
            search: Search for groups by name or path
            owned: Limit to groups explicitly owned by the current user
            order_by: Order groups by field
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            GroupsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "owned": owned,
            "order_by": order_by,
            "sort": sort,
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
        Get all details of a group.

        Args:
            id: The ID or URL-encoded path of the group
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
        - id: ID of the group
        - web_url: Web URL of the group
        - name: Name of the group
        - path: URL path of the group
        - description: Description of the group
        - visibility: Visibility level of the group
        - share_with_group_lock: Whether sharing with other groups is locked
        - require_two_factor_authentication: Whether two-factor authentication is required
        - two_factor_grace_period: Grace period for two-factor authentication
        - project_creation_level: Level required to create projects
        - auto_devops_enabled: Whether Auto DevOps is enabled
        - subgroup_creation_level: Level required to create subgroups
        - emails_disabled: Whether emails are disabled
        - emails_enabled: Whether emails are enabled
        - mentions_disabled: Whether mentions are disabled
        - lfs_enabled: Whether Git LFS is enabled
        - default_branch_protection: Default branch protection level
        - avatar_url: URL of the group avatar
        - request_access_enabled: Whether access requests are enabled
        - full_name: Full name of the group
        - full_path: Full path of the group
        - created_at: Timestamp when the group was created
        - parent_id: ID of the parent group
        - shared_with_groups: Groups this group is shared with
        - projects: Projects in the group

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

class BranchesQuery:
    """
    Query class for Branches entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        **kwargs
    ) -> BranchesListResult:
        """
        Get a list of repository branches from a project.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            search: Return list of branches containing the search string
            **kwargs: Additional parameters

        Returns:
            BranchesListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "search": search,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("branches", "list", params)
        # Cast generic envelope to concrete typed result
        return BranchesListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        branch: str,
        **kwargs
    ) -> Branch:
        """
        Get a single project repository branch.

        Args:
            project_id: The ID or URL-encoded path of the project
            branch: The name of the branch (URL-encoded if it contains special characters)
            **kwargs: Additional parameters

        Returns:
            Branch
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "branch": branch,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("branches", "get", params)
        return result



    async def search(
        self,
        query: BranchesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BranchesSearchResult:
        """
        Search branches records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BranchesSearchFilter):
        - project_id: ID of the project the branch belongs to
        - name: Name of the branch
        - merged: Whether the branch is merged
        - protected: Whether the branch is protected
        - developers_can_push: Whether developers can push to the branch
        - developers_can_merge: Whether developers can merge into the branch
        - can_push: Whether the current user can push
        - default: Whether this is the default branch
        - web_url: Web URL of the branch
        - commit_id: SHA of the head commit
        - commit: Head commit details

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BranchesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("branches", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BranchesSearchResult(
            data=[
                BranchesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class PipelinesQuery:
    """
    Query class for Pipelines entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        status: str | None = None,
        ref: str | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> PipelinesListResult:
        """
        List pipelines in a project.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            status: Filter pipelines by status
            ref: Filter pipelines by ref
            order_by: Order pipelines by field
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            PipelinesListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "status": status,
            "ref": ref,
            "order_by": order_by,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pipelines", "list", params)
        # Cast generic envelope to concrete typed result
        return PipelinesListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        pipeline_id: str,
        **kwargs
    ) -> Pipeline:
        """
        Get one pipeline of a project.

        Args:
            project_id: The ID or URL-encoded path of the project
            pipeline_id: The ID of the pipeline
            **kwargs: Additional parameters

        Returns:
            Pipeline
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "pipeline_id": pipeline_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pipelines", "get", params)
        return result



    async def search(
        self,
        query: PipelinesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PipelinesSearchResult:
        """
        Search pipelines records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PipelinesSearchFilter):
        - id: ID of the pipeline
        - iid: Internal ID of the pipeline within the project
        - project_id: ID of the project
        - sha: SHA of the commit that triggered the pipeline
        - source: Source that triggered the pipeline
        - ref: Branch or tag that triggered the pipeline
        - status: Status of the pipeline
        - created_at: Timestamp when the pipeline was created
        - updated_at: Timestamp when the pipeline was last updated
        - web_url: Web URL of the pipeline
        - name: Name of the pipeline

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PipelinesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("pipelines", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PipelinesSearchResult(
            data=[
                PipelinesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GroupMembersQuery:
    """
    Query class for GroupMembers entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        group_id: str,
        page: int | None = None,
        per_page: int | None = None,
        query: str | None = None,
        **kwargs
    ) -> GroupMembersListResult:
        """
        Gets a list of group members viewable by the authenticated user.

        Args:
            group_id: The ID or URL-encoded path of the group
            page: Page number
            per_page: Number of items per page
            query: Filter members by name or username
            **kwargs: Additional parameters

        Returns:
            GroupMembersListResult
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            "page": page,
            "per_page": per_page,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("group_members", "list", params)
        # Cast generic envelope to concrete typed result
        return GroupMembersListResult(
            data=result.data
        )



    async def get(
        self,
        group_id: str,
        user_id: str,
        **kwargs
    ) -> Member:
        """
        Get a member of a group.

        Args:
            group_id: The ID or URL-encoded path of the group
            user_id: The user ID of the member
            **kwargs: Additional parameters

        Returns:
            Member
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            "user_id": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("group_members", "get", params)
        return result



    async def search(
        self,
        query: GroupMembersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GroupMembersSearchResult:
        """
        Search group_members records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GroupMembersSearchFilter):
        - group_id: ID of the group
        - id: ID of the member
        - name: Full name of the member
        - username: Username of the member
        - state: State of the member account
        - membership_state: State of the membership
        - avatar_url: URL of the member avatar
        - web_url: Web URL of the member profile
        - access_level: Access level of the member
        - created_at: Timestamp when the member was added
        - expires_at: Expiration date of the membership
        - created_by: User who added the member
        - locked: Whether the member account is locked

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GroupMembersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("group_members", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GroupMembersSearchResult(
            data=[
                GroupMembersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProjectMembersQuery:
    """
    Query class for ProjectMembers entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        query: str | None = None,
        **kwargs
    ) -> ProjectMembersListResult:
        """
        Gets a list of project members viewable by the authenticated user.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            query: Filter members by name or username
            **kwargs: Additional parameters

        Returns:
            ProjectMembersListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "query": query,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_members", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectMembersListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        user_id: str,
        **kwargs
    ) -> Member:
        """
        Get a member of a project.

        Args:
            project_id: The ID or URL-encoded path of the project
            user_id: The user ID of the member
            **kwargs: Additional parameters

        Returns:
            Member
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "user_id": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_members", "get", params)
        return result



    async def search(
        self,
        query: ProjectMembersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProjectMembersSearchResult:
        """
        Search project_members records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProjectMembersSearchFilter):
        - project_id: ID of the project
        - id: ID of the member
        - name: Full name of the member
        - username: Username of the member
        - state: State of the member account
        - membership_state: State of the membership
        - avatar_url: URL of the member avatar
        - web_url: Web URL of the member profile
        - access_level: Access level of the member
        - created_at: Timestamp when the member was added
        - expires_at: Expiration date of the membership
        - created_by: User who added the member
        - locked: Whether the member account is locked

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProjectMembersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("project_members", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProjectMembersSearchResult(
            data=[
                ProjectMembersSearchData(**row)
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

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> ReleasesListResult:
        """
        Paginated list of releases for a given project, sorted by released_at.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            order_by: Order by field
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            ReleasesListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "order_by": order_by,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("releases", "list", params)
        # Cast generic envelope to concrete typed result
        return ReleasesListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        tag_name: str,
        **kwargs
    ) -> Release:
        """
        Get a release for the given tag.

        Args:
            project_id: The ID or URL-encoded path of the project
            tag_name: The Git tag the release is associated with
            **kwargs: Additional parameters

        Returns:
            Release
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "tag_name": tag_name,
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
        - name: Name of the release
        - tag_name: Tag name associated with the release
        - description: Description of the release
        - created_at: Timestamp when the release was created
        - released_at: Timestamp when the release was published
        - upcoming_release: Whether this is an upcoming release
        - milestones: Milestones associated with the release
        - commit_path: Path to the release commit
        - tag_path: Path to the release tag
        - assets: Assets attached to the release
        - evidences: Evidences collected for the release
        - links: Related resource links
        - author: Author of the release
        - author_id: ID of the author
        - commit: Commit associated with the release
        - commit_id: SHA of the associated commit
        - project_id: ID of the project

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

class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> TagsListResult:
        """
        Get a list of repository tags from a project, sorted by update date and time in descending order.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            search: Return list of tags matching the search criteria
            order_by: Return tags ordered by field
            sort: Sort order
            **kwargs: Additional parameters

        Returns:
            TagsListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "search": search,
            "order_by": order_by,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to concrete typed result
        return TagsListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        tag_name: str,
        **kwargs
    ) -> Tag:
        """
        Get a specific repository tag determined by its name.

        Args:
            project_id: The ID or URL-encoded path of the project
            tag_name: The name of the tag
            **kwargs: Additional parameters

        Returns:
            Tag
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "tag_name": tag_name,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "get", params)
        return result



    async def search(
        self,
        query: TagsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TagsSearchResult:
        """
        Search tags records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TagsSearchFilter):
        - name: Name of the tag
        - message: Annotation message of the tag
        - target: SHA the tag points to
        - release: Release associated with the tag
        - protected: Whether the tag is protected
        - commit: Commit the tag points to
        - commit_id: SHA of the tagged commit
        - project_id: ID of the project

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TagsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tags", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TagsSearchResult(
            data=[
                TagsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GroupMilestonesQuery:
    """
    Query class for GroupMilestones entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        group_id: str,
        page: int | None = None,
        per_page: int | None = None,
        state: str | None = None,
        search: str | None = None,
        **kwargs
    ) -> GroupMilestonesListResult:
        """
        Returns a list of group milestones.

        Args:
            group_id: The ID or URL-encoded path of the group
            page: Page number
            per_page: Number of items per page
            state: Filter milestones by state
            search: Search for milestones by title or description
            **kwargs: Additional parameters

        Returns:
            GroupMilestonesListResult
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            "page": page,
            "per_page": per_page,
            "state": state,
            "search": search,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("group_milestones", "list", params)
        # Cast generic envelope to concrete typed result
        return GroupMilestonesListResult(
            data=result.data
        )



    async def get(
        self,
        group_id: str,
        milestone_id: str,
        **kwargs
    ) -> Milestone:
        """
        Get a single group milestone.

        Args:
            group_id: The ID or URL-encoded path of the group
            milestone_id: The ID of the milestone
            **kwargs: Additional parameters

        Returns:
            Milestone
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            "milestone_id": milestone_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("group_milestones", "get", params)
        return result



    async def search(
        self,
        query: GroupMilestonesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GroupMilestonesSearchResult:
        """
        Search group_milestones records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GroupMilestonesSearchFilter):
        - id: ID of the milestone
        - iid: Internal ID of the milestone within the group
        - group_id: ID of the group
        - title: Title of the milestone
        - description: Description of the milestone
        - state: State of the milestone
        - created_at: Timestamp when the milestone was created
        - updated_at: Timestamp when the milestone was last updated
        - due_date: Due date of the milestone
        - start_date: Start date of the milestone
        - expired: Whether the milestone is expired
        - web_url: Web URL of the milestone

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GroupMilestonesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("group_milestones", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GroupMilestonesSearchResult(
            data=[
                GroupMilestonesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProjectMilestonesQuery:
    """
    Query class for ProjectMilestones entity operations.
    """

    def __init__(self, connector: GitlabConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        project_id: str,
        page: int | None = None,
        per_page: int | None = None,
        state: str | None = None,
        search: str | None = None,
        **kwargs
    ) -> ProjectMilestonesListResult:
        """
        Returns a list of project milestones.

        Args:
            project_id: The ID or URL-encoded path of the project
            page: Page number
            per_page: Number of items per page
            state: Filter milestones by state
            search: Search for milestones by title or description
            **kwargs: Additional parameters

        Returns:
            ProjectMilestonesListResult
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "page": page,
            "per_page": per_page,
            "state": state,
            "search": search,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_milestones", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectMilestonesListResult(
            data=result.data
        )



    async def get(
        self,
        project_id: str,
        milestone_id: str,
        **kwargs
    ) -> Milestone:
        """
        Get a single project milestone.

        Args:
            project_id: The ID or URL-encoded path of the project
            milestone_id: The ID of the milestone
            **kwargs: Additional parameters

        Returns:
            Milestone
        """
        params = {k: v for k, v in {
            "project_id": project_id,
            "milestone_id": milestone_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_milestones", "get", params)
        return result



    async def search(
        self,
        query: ProjectMilestonesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProjectMilestonesSearchResult:
        """
        Search project_milestones records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProjectMilestonesSearchFilter):
        - id: ID of the milestone
        - iid: Internal ID of the milestone within the project
        - project_id: ID of the project
        - title: Title of the milestone
        - description: Description of the milestone
        - state: State of the milestone
        - created_at: Timestamp when the milestone was created
        - updated_at: Timestamp when the milestone was last updated
        - due_date: Due date of the milestone
        - start_date: Start date of the milestone
        - expired: Whether the milestone is expired
        - web_url: Web URL of the milestone

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProjectMilestonesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("project_milestones", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProjectMilestonesSearchResult(
            data=[
                ProjectMilestonesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
