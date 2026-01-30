"""
Github connector.
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

from .connector_model import GithubConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    BranchesGetParams,
    BranchesListParams,
    CommentsGetParams,
    CommentsListParams,
    CommitsGetParams,
    CommitsListParams,
    IssuesApiSearchParams,
    IssuesGetParams,
    IssuesListParams,
    LabelsGetParams,
    LabelsListParams,
    MilestonesGetParams,
    MilestonesListParams,
    OrgRepositoriesListParams,
    OrganizationsGetParams,
    OrganizationsListParams,
    PrCommentsGetParams,
    PrCommentsListParams,
    ProjectItemsListParams,
    ProjectsGetParams,
    ProjectsListParams,
    PullRequestsApiSearchParams,
    PullRequestsGetParams,
    PullRequestsListParams,
    ReleasesGetParams,
    ReleasesListParams,
    RepositoriesApiSearchParams,
    RepositoriesGetParams,
    RepositoriesListParams,
    ReviewsListParams,
    StargazersListParams,
    TagsGetParams,
    TagsListParams,
    TeamsGetParams,
    TeamsListParams,
    UsersApiSearchParams,
    UsersGetParams,
    UsersListParams,
    ViewerGetParams,
    ViewerRepositoriesListParams,
)
if TYPE_CHECKING:
    from .models import GithubAuthConfig

# Import specific auth config classes for multi-auth isinstance checks
from .models import GithubOauth2AuthConfig, GithubPersonalAccessTokenAuthConfig
# Import response models and envelope models at runtime
from .models import (
    GithubCheckResult,
    GithubExecuteResult,
    GithubExecuteResultWithMeta,
    RepositoriesListResult,
    RepositoriesApiSearchResult,
    OrgRepositoriesListResult,
    BranchesListResult,
    CommitsListResult,
    ReleasesListResult,
    IssuesListResult,
    IssuesApiSearchResult,
    PullRequestsListResult,
    PullRequestsApiSearchResult,
    ReviewsListResult,
    CommentsListResult,
    PrCommentsListResult,
    LabelsListResult,
    MilestonesListResult,
    OrganizationsListResult,
    UsersListResult,
    UsersApiSearchResult,
    TeamsListResult,
    TagsListResult,
    StargazersListResult,
    ViewerRepositoriesListResult,
    ProjectsListResult,
    ProjectItemsListResult,
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




class GithubConnector:
    """
    Type-safe Github API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "github"
    connector_version = "0.1.9"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("repositories", "get"): None,
        ("repositories", "list"): True,
        ("repositories", "api_search"): True,
        ("org_repositories", "list"): True,
        ("branches", "list"): True,
        ("branches", "get"): None,
        ("commits", "list"): True,
        ("commits", "get"): None,
        ("releases", "list"): True,
        ("releases", "get"): None,
        ("issues", "list"): True,
        ("issues", "get"): None,
        ("issues", "api_search"): True,
        ("pull_requests", "list"): True,
        ("pull_requests", "get"): None,
        ("pull_requests", "api_search"): True,
        ("reviews", "list"): True,
        ("comments", "list"): True,
        ("comments", "get"): None,
        ("pr_comments", "list"): True,
        ("pr_comments", "get"): None,
        ("labels", "list"): True,
        ("labels", "get"): None,
        ("milestones", "list"): True,
        ("milestones", "get"): None,
        ("organizations", "get"): None,
        ("organizations", "list"): True,
        ("users", "get"): None,
        ("users", "list"): True,
        ("users", "api_search"): True,
        ("teams", "list"): True,
        ("teams", "get"): None,
        ("tags", "list"): True,
        ("tags", "get"): None,
        ("stargazers", "list"): True,
        ("viewer", "get"): None,
        ("viewer_repositories", "list"): True,
        ("projects", "list"): True,
        ("projects", "get"): None,
        ("project_items", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('repositories', 'get'): {'owner': 'owner', 'repo': 'repo', 'fields': 'fields'},
        ('repositories', 'list'): {'username': 'username', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('repositories', 'api_search'): {'query': 'query', 'limit': 'limit', 'after': 'after', 'fields': 'fields'},
        ('org_repositories', 'list'): {'org': 'org', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('branches', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('branches', 'get'): {'owner': 'owner', 'repo': 'repo', 'branch': 'branch', 'fields': 'fields'},
        ('commits', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('commits', 'get'): {'owner': 'owner', 'repo': 'repo', 'sha': 'sha', 'fields': 'fields'},
        ('releases', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('releases', 'get'): {'owner': 'owner', 'repo': 'repo', 'tag': 'tag', 'fields': 'fields'},
        ('issues', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('issues', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('issues', 'api_search'): {'query': 'query', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('pull_requests', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('pull_requests', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('pull_requests', 'api_search'): {'query': 'query', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('reviews', 'list'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('comments', 'list'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('comments', 'get'): {'id': 'id', 'fields': 'fields'},
        ('pr_comments', 'list'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('pr_comments', 'get'): {'id': 'id', 'fields': 'fields'},
        ('labels', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('labels', 'get'): {'owner': 'owner', 'repo': 'repo', 'name': 'name', 'fields': 'fields'},
        ('milestones', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('milestones', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('organizations', 'get'): {'org': 'org', 'fields': 'fields'},
        ('organizations', 'list'): {'username': 'username', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('users', 'get'): {'username': 'username', 'fields': 'fields'},
        ('users', 'list'): {'org': 'org', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('users', 'api_search'): {'query': 'query', 'limit': 'limit', 'after': 'after', 'fields': 'fields'},
        ('teams', 'list'): {'org': 'org', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('teams', 'get'): {'org': 'org', 'team_slug': 'team_slug', 'fields': 'fields'},
        ('tags', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('tags', 'get'): {'owner': 'owner', 'repo': 'repo', 'tag': 'tag', 'fields': 'fields'},
        ('stargazers', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('viewer', 'get'): {'fields': 'fields'},
        ('viewer_repositories', 'list'): {'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('projects', 'list'): {'org': 'org', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('projects', 'get'): {'org': 'org', 'project_number': 'project_number', 'fields': 'fields'},
        ('project_items', 'list'): {'org': 'org', 'project_number': 'project_number', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
    }

    def __init__(
        self,
        auth_config: GithubAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new github connector instance.

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
            connector = GithubConnector(auth_config=GithubAuthConfig(access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GithubConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = GithubConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GithubConnector(
                auth_config=GithubAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(GithubConnectorModel.id) if not connector_id else None,
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

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, GithubOauth2AuthConfig):
                    auth_scheme = "githubOAuth"
                if isinstance(auth_config, GithubPersonalAccessTokenAuthConfig):
                    auth_scheme = "githubPAT"

            self._executor = LocalExecutor(
                model=GithubConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.repositories = RepositoriesQuery(self)
        self.org_repositories = OrgRepositoriesQuery(self)
        self.branches = BranchesQuery(self)
        self.commits = CommitsQuery(self)
        self.releases = ReleasesQuery(self)
        self.issues = IssuesQuery(self)
        self.pull_requests = PullRequestsQuery(self)
        self.reviews = ReviewsQuery(self)
        self.comments = CommentsQuery(self)
        self.pr_comments = PrCommentsQuery(self)
        self.labels = LabelsQuery(self)
        self.milestones = MilestonesQuery(self)
        self.organizations = OrganizationsQuery(self)
        self.users = UsersQuery(self)
        self.teams = TeamsQuery(self)
        self.tags = TagsQuery(self)
        self.stargazers = StargazersQuery(self)
        self.viewer = ViewerQuery(self)
        self.viewer_repositories = ViewerRepositoriesQuery(self)
        self.projects = ProjectsQuery(self)
        self.project_items = ProjectItemsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["get"],
        params: "RepositoriesGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["list"],
        params: "RepositoriesListParams"
    ) -> "RepositoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["api_search"],
        params: "RepositoriesApiSearchParams"
    ) -> "RepositoriesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["org_repositories"],
        action: Literal["list"],
        params: "OrgRepositoriesListParams"
    ) -> "OrgRepositoriesListResult": ...

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
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["api_search"],
        params: "IssuesApiSearchParams"
    ) -> "IssuesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pull_requests"],
        action: Literal["list"],
        params: "PullRequestsListParams"
    ) -> "PullRequestsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pull_requests"],
        action: Literal["get"],
        params: "PullRequestsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["pull_requests"],
        action: Literal["api_search"],
        params: "PullRequestsApiSearchParams"
    ) -> "PullRequestsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["reviews"],
        action: Literal["list"],
        params: "ReviewsListParams"
    ) -> "ReviewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["list"],
        params: "CommentsListParams"
    ) -> "CommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["get"],
        params: "CommentsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["pr_comments"],
        action: Literal["list"],
        params: "PrCommentsListParams"
    ) -> "PrCommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pr_comments"],
        action: Literal["get"],
        params: "PrCommentsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["list"],
        params: "LabelsListParams"
    ) -> "LabelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["get"],
        params: "LabelsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["milestones"],
        action: Literal["list"],
        params: "MilestonesListParams"
    ) -> "MilestonesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["milestones"],
        action: Literal["get"],
        params: "MilestonesGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["get"],
        params: "OrganizationsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["list"],
        params: "OrganizationsListParams"
    ) -> "OrganizationsListResult": ...

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
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["api_search"],
        params: "UsersApiSearchParams"
    ) -> "UsersApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["list"],
        params: "TeamsListParams"
    ) -> "TeamsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["stargazers"],
        action: Literal["list"],
        params: "StargazersListParams"
    ) -> "StargazersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["viewer"],
        action: Literal["get"],
        params: "ViewerGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["viewer_repositories"],
        action: Literal["list"],
        params: "ViewerRepositoriesListParams"
    ) -> "ViewerRepositoriesListResult": ...

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
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["project_items"],
        action: Literal["list"],
        params: "ProjectItemsListParams"
    ) -> "ProjectItemsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "api_search"],
        params: Mapping[str, Any]
    ) -> GithubExecuteResult[Any] | GithubExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "api_search"],
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
                return GithubExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GithubExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GithubCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GithubCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GithubCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GithubCheckResult(
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
            @GithubConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GithubConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GithubConnectorModel,
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
        return describe_entities(GithubConnectorModel)

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
            (e for e in GithubConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GithubConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GithubConnector.create_hosted(...)
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
        auth_config: "GithubAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "GithubConnector":
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
            A GithubConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await GithubConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=GithubAuthConfig(access_token="..."),
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
                connector_definition_id=str(GithubConnectorModel.id),
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



class RepositoriesQuery:
    """
    Query class for Repositories entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        owner: str,
        repo: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific GitHub repository using GraphQL

        Args:
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "get", params)
        return result



    async def list(
        self,
        username: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> RepositoriesListResult:
        """
        Returns a list of repositories for the specified user using GraphQL

        Args:
            username: The username of the user whose repositories to list
            per_page: The number of results per page
            after: Cursor for pagination (from previous response's endCursor)
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            RepositoriesListResult
        """
        params = {k: v for k, v in {
            "username": username,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "list", params)
        # Cast generic envelope to concrete typed result
        return RepositoriesListResult(
            data=result.data
        )



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> RepositoriesApiSearchResult:
        """
        Search for GitHub repositories using GitHub's powerful search syntax.
Examples: "language:python stars:>1000", "topic:machine-learning", "org:facebook is:public"


        Args:
            query: GitHub repository search query using GitHub's search syntax
            limit: Number of results to return
            after: Cursor for pagination (from previous response's endCursor)
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            RepositoriesApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "api_search", params)
        # Cast generic envelope to concrete typed result
        return RepositoriesApiSearchResult(
            data=result.data
        )



class OrgRepositoriesQuery:
    """
    Query class for OrgRepositories entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        org: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> OrgRepositoriesListResult:
        """
        Returns a list of repositories for the specified organization using GraphQL

        Args:
            org: The organization login/username
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            OrgRepositoriesListResult
        """
        params = {k: v for k, v in {
            "org": org,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("org_repositories", "list", params)
        # Cast generic envelope to concrete typed result
        return OrgRepositoriesListResult(
            data=result.data
        )



class BranchesQuery:
    """
    Query class for Branches entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> BranchesListResult:
        """
        Returns a list of branches for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            BranchesListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("branches", "list", params)
        # Cast generic envelope to concrete typed result
        return BranchesListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        branch: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific branch using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            branch: The branch name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("branches", "get", params)
        return result



class CommitsQuery:
    """
    Query class for Commits entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> CommitsListResult:
        """
        Returns a list of commits for the default branch using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            CommitsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("commits", "list", params)
        # Cast generic envelope to concrete typed result
        return CommitsListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific commit by SHA using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            sha: The commit SHA
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "sha": sha,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("commits", "get", params)
        return result



class ReleasesQuery:
    """
    Query class for Releases entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> ReleasesListResult:
        """
        Returns a list of releases for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ReleasesListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("releases", "list", params)
        # Cast generic envelope to concrete typed result
        return ReleasesListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        tag: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific release by tag name using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            tag: The release tag name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "tag": tag,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("releases", "get", params)
        return result



class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        states: list[str] | None = None,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> IssuesListResult:
        """
        Returns a list of issues for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            states: Filter by issue state
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            IssuesListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "states": states,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        # Cast generic envelope to concrete typed result
        return IssuesListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific issue using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The issue number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result



    async def api_search(
        self,
        query: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> IssuesApiSearchResult:
        """
        Search for issues using GitHub's search syntax

        Args:
            query: GitHub issue search query using GitHub's search syntax
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            IssuesApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "api_search", params)
        # Cast generic envelope to concrete typed result
        return IssuesApiSearchResult(
            data=result.data
        )



class PullRequestsQuery:
    """
    Query class for PullRequests entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        states: list[str] | None = None,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> PullRequestsListResult:
        """
        Returns a list of pull requests for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            states: Filter by pull request state
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            PullRequestsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "states": states,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pull_requests", "list", params)
        # Cast generic envelope to concrete typed result
        return PullRequestsListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific pull request using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The pull request number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pull_requests", "get", params)
        return result



    async def api_search(
        self,
        query: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> PullRequestsApiSearchResult:
        """
        Search for pull requests using GitHub's search syntax

        Args:
            query: GitHub pull request search query using GitHub's search syntax
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            PullRequestsApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pull_requests", "api_search", params)
        # Cast generic envelope to concrete typed result
        return PullRequestsApiSearchResult(
            data=result.data
        )



class ReviewsQuery:
    """
    Query class for Reviews entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        number: int,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> ReviewsListResult:
        """
        Returns a list of reviews for the specified pull request using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The pull request number
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ReviewsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reviews", "list", params)
        # Cast generic envelope to concrete typed result
        return ReviewsListResult(
            data=result.data
        )



class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        number: int,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> CommentsListResult:
        """
        Returns a list of comments for the specified issue using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The issue number
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            CommentsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "list", params)
        # Cast generic envelope to concrete typed result
        return CommentsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific issue comment by its GraphQL node ID.

Note: This endpoint requires a GraphQL node ID (e.g., 'IC_kwDOBZtLds6YWTMj'),
not a numeric database ID. You can obtain node IDs from the Comments_List response,
where each comment includes both 'id' (node ID) and 'databaseId' (numeric ID).


        Args:
            id: The GraphQL node ID of the comment
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "get", params)
        return result



class PrCommentsQuery:
    """
    Query class for PrComments entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        number: int,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> PrCommentsListResult:
        """
        Returns a list of comments for the specified pull request using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The pull request number
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            PrCommentsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pr_comments", "list", params)
        # Cast generic envelope to concrete typed result
        return PrCommentsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific pull request comment by its GraphQL node ID.

Note: This endpoint requires a GraphQL node ID (e.g., 'IC_kwDOBZtLds6YWTMj'),
not a numeric database ID. You can obtain node IDs from the PRComments_List response,
where each comment includes both 'id' (node ID) and 'databaseId' (numeric ID).


        Args:
            id: The GraphQL node ID of the comment
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pr_comments", "get", params)
        return result



class LabelsQuery:
    """
    Query class for Labels entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> LabelsListResult:
        """
        Returns a list of labels for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            LabelsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "list", params)
        # Cast generic envelope to concrete typed result
        return LabelsListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        name: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific label by name using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            name: The label name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "name": name,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "get", params)
        return result



class MilestonesQuery:
    """
    Query class for Milestones entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        states: list[str] | None = None,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> MilestonesListResult:
        """
        Returns a list of milestones for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            states: Filter by milestone state
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            MilestonesListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "states": states,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("milestones", "list", params)
        # Cast generic envelope to concrete typed result
        return MilestonesListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific milestone by number using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The milestone number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("milestones", "get", params)
        return result



class OrganizationsQuery:
    """
    Query class for Organizations entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        org: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific organization using GraphQL

        Args:
            org: The organization login/username
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "org": org,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "get", params)
        return result



    async def list(
        self,
        username: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> OrganizationsListResult:
        """
        Returns a list of organizations the user belongs to using GraphQL

        Args:
            username: The username of the user
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            OrganizationsListResult
        """
        params = {k: v for k, v in {
            "username": username,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "list", params)
        # Cast generic envelope to concrete typed result
        return OrganizationsListResult(
            data=result.data
        )



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        username: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific user using GraphQL

        Args:
            username: The username of the user
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "username": username,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



    async def list(
        self,
        org: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a list of members for the specified organization using GraphQL

        Args:
            org: The organization login/username
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "org": org,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data
        )



    async def api_search(
        self,
        query: str,
        limit: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> UsersApiSearchResult:
        """
        Search for GitHub users using search syntax

        Args:
            query: GitHub user search query using GitHub's search syntax
            limit: Number of results to return
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            UsersApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "api_search", params)
        # Cast generic envelope to concrete typed result
        return UsersApiSearchResult(
            data=result.data
        )



class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        org: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> TeamsListResult:
        """
        Returns a list of teams for the specified organization using GraphQL

        Args:
            org: The organization login/username
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            TeamsListResult
        """
        params = {k: v for k, v in {
            "org": org,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamsListResult(
            data=result.data
        )



    async def get(
        self,
        org: str,
        team_slug: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific team using GraphQL

        Args:
            org: The organization login/username
            team_slug: The team slug
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "org": org,
            "team_slug": team_slug,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        return result



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> TagsListResult:
        """
        Returns a list of tags for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            TagsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to concrete typed result
        return TagsListResult(
            data=result.data
        )



    async def get(
        self,
        owner: str,
        repo: str,
        tag: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific tag by name using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            tag: The tag name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "tag": tag,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "get", params)
        return result



class StargazersQuery:
    """
    Query class for Stargazers entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> StargazersListResult:
        """
        Returns a list of users who have starred the repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            StargazersListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("stargazers", "list", params)
        # Cast generic envelope to concrete typed result
        return StargazersListResult(
            data=result.data
        )



class ViewerQuery:
    """
    Query class for Viewer entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about the currently authenticated user.
This is useful when you don't know the username but need to access
the current user's profile, permissions, or associated resources.


        Args:
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("viewer", "get", params)
        return result



class ViewerRepositoriesQuery:
    """
    Query class for ViewerRepositories entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> ViewerRepositoriesListResult:
        """
        Returns a list of repositories owned by the authenticated user.
Unlike Repositories_List which requires a username, this endpoint
automatically lists repositories for the current authenticated user.


        Args:
            per_page: The number of results per page
            after: Cursor for pagination (from previous response's endCursor)
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ViewerRepositoriesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("viewer_repositories", "list", params)
        # Cast generic envelope to concrete typed result
        return ViewerRepositoriesListResult(
            data=result.data
        )



class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        org: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> ProjectsListResult:
        """
        Returns a list of GitHub Projects V2 for the specified organization.
Projects V2 are the new project boards that replaced classic projects.


        Args:
            org: The organization login/username
            per_page: The number of results per page
            after: Cursor for pagination (from previous response's endCursor)
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ProjectsListResult
        """
        params = {k: v for k, v in {
            "org": org,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectsListResult(
            data=result.data
        )



    async def get(
        self,
        org: str,
        project_number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific GitHub Project V2 by number

        Args:
            org: The organization login/username
            project_number: The project number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "org": org,
            "project_number": project_number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        return result



class ProjectItemsQuery:
    """
    Query class for ProjectItems entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        org: str,
        project_number: int,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> ProjectItemsListResult:
        """
        Returns a list of items (issues, pull requests, draft issues) in a GitHub Project V2.
Each item includes its field values like Status, Priority, etc.


        Args:
            org: The organization login/username
            project_number: The project number
            per_page: The number of results per page
            after: Cursor for pagination (from previous response's endCursor)
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ProjectItemsListResult
        """
        params = {k: v for k, v in {
            "org": org,
            "project_number": project_number,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("project_items", "list", params)
        # Cast generic envelope to concrete typed result
        return ProjectItemsListResult(
            data=result.data
        )


