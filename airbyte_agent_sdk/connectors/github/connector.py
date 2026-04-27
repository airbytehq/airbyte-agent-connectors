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

from pydantic import BaseModel

from .connector_model import GithubConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    BranchesGetParams,
    BranchesListParams,
    CommentsCreateParams,
    CommentsGetParams,
    CommentsListParams,
    CommitsGetParams,
    CommitsListParams,
    DirectoryContentListParams,
    DiscussionsApiSearchParams,
    DiscussionsGetParams,
    DiscussionsListParams,
    FileContentGetParams,
    IssuesApiSearchParams,
    IssuesCreateParams,
    IssuesGetParams,
    IssuesListParams,
    IssuesUpdateParams,
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
    PullRequestsCreateParams,
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
    AirbyteSearchParams,
    BranchesSearchFilter,
    BranchesSearchQuery,
    CommentsSearchFilter,
    CommentsSearchQuery,
    CommitsSearchFilter,
    CommitsSearchQuery,
    DirectoryContentSearchFilter,
    DirectoryContentSearchQuery,
    DiscussionsSearchFilter,
    DiscussionsSearchQuery,
    FileContentSearchFilter,
    FileContentSearchQuery,
    IssuesSearchFilter,
    IssuesSearchQuery,
    LabelsSearchFilter,
    LabelsSearchQuery,
    MilestonesSearchFilter,
    MilestonesSearchQuery,
    OrganizationsSearchFilter,
    OrganizationsSearchQuery,
    OrgRepositoriesSearchFilter,
    OrgRepositoriesSearchQuery,
    PrCommentsSearchFilter,
    PrCommentsSearchQuery,
    ProjectItemsSearchFilter,
    ProjectItemsSearchQuery,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    PullRequestsSearchFilter,
    PullRequestsSearchQuery,
    ReleasesSearchFilter,
    ReleasesSearchQuery,
    RepositoriesSearchFilter,
    RepositoriesSearchQuery,
    ReviewsSearchFilter,
    ReviewsSearchQuery,
    StargazersSearchFilter,
    StargazersSearchQuery,
    TagsSearchFilter,
    TagsSearchQuery,
    TeamsSearchFilter,
    TeamsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    ViewerSearchFilter,
    ViewerSearchQuery,
    ViewerRepositoriesSearchFilter,
    ViewerRepositoriesSearchQuery,
)
from .models import GithubOauth2AuthConfig, GithubPersonalAccessTokenAuthConfig
from .models import GithubAuthConfig
if TYPE_CHECKING:
    from .models import GithubReplicationConfig

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
    DiscussionsListResult,
    DiscussionsApiSearchResult,
    DirectoryContentListResult,
    CommentResponse,
    IssueResponse,
    PullRequestResponse,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    BranchesSearchData,
    BranchesSearchResult,
    CommentsSearchData,
    CommentsSearchResult,
    CommitsSearchData,
    CommitsSearchResult,
    DirectoryContentSearchData,
    DirectoryContentSearchResult,
    DiscussionsSearchData,
    DiscussionsSearchResult,
    FileContentSearchData,
    FileContentSearchResult,
    IssuesSearchData,
    IssuesSearchResult,
    LabelsSearchData,
    LabelsSearchResult,
    MilestonesSearchData,
    MilestonesSearchResult,
    OrganizationsSearchData,
    OrganizationsSearchResult,
    OrgRepositoriesSearchData,
    OrgRepositoriesSearchResult,
    PrCommentsSearchData,
    PrCommentsSearchResult,
    ProjectItemsSearchData,
    ProjectItemsSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    PullRequestsSearchData,
    PullRequestsSearchResult,
    ReleasesSearchData,
    ReleasesSearchResult,
    RepositoriesSearchData,
    RepositoriesSearchResult,
    ReviewsSearchData,
    ReviewsSearchResult,
    StargazersSearchData,
    StargazersSearchResult,
    TagsSearchData,
    TagsSearchResult,
    TeamsSearchData,
    TeamsSearchResult,
    UsersSearchData,
    UsersSearchResult,
    ViewerSearchData,
    ViewerSearchResult,
    ViewerRepositoriesSearchData,
    ViewerRepositoriesSearchResult,
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




class GithubConnector:
    """
    Type-safe Github API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "github"
    connector_version = "0.1.18"
    sdk_version = "0.1.94"

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
        ("issues", "create"): None,
        ("issues", "update"): None,
        ("comments", "create"): None,
        ("pull_requests", "create"): None,
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
        ("discussions", "list"): True,
        ("discussions", "get"): None,
        ("discussions", "api_search"): True,
        ("file_content", "get"): None,
        ("directory_content", "list"): True,
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
        ('commits', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'path': 'path', 'fields': 'fields'},
        ('commits', 'get'): {'owner': 'owner', 'repo': 'repo', 'sha': 'sha', 'fields': 'fields'},
        ('releases', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('releases', 'get'): {'owner': 'owner', 'repo': 'repo', 'tag': 'tag', 'fields': 'fields'},
        ('issues', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('issues', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('issues', 'api_search'): {'query': 'query', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('issues', 'create'): {'title': 'title', 'body': 'body', 'labels': 'labels', 'assignees': 'assignees', 'milestone': 'milestone', 'owner': 'owner', 'repo': 'repo'},
        ('issues', 'update'): {'title': 'title', 'body': 'body', 'state': 'state', 'state_reason': 'state_reason', 'labels': 'labels', 'assignees': 'assignees', 'milestone': 'milestone', 'owner': 'owner', 'repo': 'repo', 'issue_number': 'issue_number'},
        ('comments', 'create'): {'body': 'body', 'owner': 'owner', 'repo': 'repo', 'issue_number': 'issue_number'},
        ('pull_requests', 'create'): {'title': 'title', 'head': 'head', 'base': 'base', 'body': 'body', 'draft': 'draft', 'maintainer_can_modify': 'maintainer_can_modify', 'owner': 'owner', 'repo': 'repo'},
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
        ('discussions', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'answered': 'answered', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('discussions', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('discussions', 'api_search'): {'query': 'query', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('file_content', 'get'): {'owner': 'owner', 'repo': 'repo', 'path': 'path', 'ref': 'ref', 'fields': 'fields'},
        ('directory_content', 'list'): {'owner': 'owner', 'repo': 'repo', 'path': 'path', 'ref': 'ref', 'fields': 'fields'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GithubOauth2AuthConfig, GithubPersonalAccessTokenAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GithubAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new github connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GithubAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GithubConnector(auth_config=GithubAuthConfig(access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GithubConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = GithubConnector(
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
                connector_definition_id=str(GithubConnectorModel.id),
                model=GithubConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GithubAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

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
        self.comments = CommentsQuery(self)
        self.pull_requests = PullRequestsQuery(self)
        self.reviews = ReviewsQuery(self)
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
        self.discussions = DiscussionsQuery(self)
        self.file_content = FileContentQuery(self)
        self.directory_content = DirectoryContentQuery(self)

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
        entity: Literal["issues"],
        action: Literal["create"],
        params: "IssuesCreateParams"
    ) -> "IssueResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["update"],
        params: "IssuesUpdateParams"
    ) -> "IssueResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["create"],
        params: "CommentsCreateParams"
    ) -> "CommentResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["pull_requests"],
        action: Literal["create"],
        params: "PullRequestsCreateParams"
    ) -> "PullRequestResponse": ...

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
        entity: Literal["discussions"],
        action: Literal["list"],
        params: "DiscussionsListParams"
    ) -> "DiscussionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["discussions"],
        action: Literal["get"],
        params: "DiscussionsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["discussions"],
        action: Literal["api_search"],
        params: "DiscussionsApiSearchParams"
    ) -> "DiscussionsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["file_content"],
        action: Literal["get"],
        params: "FileContentGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["directory_content"],
        action: Literal["list"],
        params: "DirectoryContentListParams"
    ) -> "DirectoryContentListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "api_search", "create", "update", "context_store_search"],
        params: Mapping[str, Any]
    ) -> GithubExecuteResult[Any] | GithubExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "api_search", "create", "update", "context_store_search"],
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
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    GithubConnectorModel,
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
            connector = await GithubConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
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

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def get_consent_url(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        redirect_url: str,
        name: str | None = None,
        replication_config: "GithubReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and workspace_name.
                Optionally include organization_id for multi-org request routing.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + workspace_name.
            replication_config: Typed replication settings. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await GithubConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Github Source",
                replication_config=GithubReplicationConfig(repositories="..."),
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.workspace_name:
            raise ValueError("airbyte_config.workspace_name is required for get_consent_url()")

        from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(GithubConnectorModel.id),
                workspace_name=airbyte_config.workspace_name,
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
        auth_config: "GithubAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GithubReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GithubConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and workspace_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + workspace_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A GithubConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GithubConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GithubAuthConfig(access_token="..."),
            )

            # With replication config (required for this connector):
            connector = await GithubConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GithubAuthConfig(access_token="..."),
                replication_config=GithubReplicationConfig(repositories="..."),
            )

            # With server-side OAuth:
            connector = await GithubConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GithubReplicationConfig(repositories="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.workspace_name:
            raise ValueError("airbyte_config.workspace_name is required for create()")

        # Validate: exactly one of auth_config or server_side_oauth_secret_id required
        if auth_config is None and server_side_oauth_secret_id is None:
            raise ValueError(
                "Either auth_config or server_side_oauth_secret_id must be provided"
            )
        if auth_config is not None and server_side_oauth_secret_id is not None:
            raise ValueError(
                "Cannot provide both auth_config and server_side_oauth_secret_id"
            )

        from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
        from airbyte_agent_sdk.types import AirbyteAuthConfig as _AirbyteAuthConfig

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
            source_name = name or f"{cls.connector_name} - {airbyte_config.workspace_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(GithubConnectorModel.id),
                workspace_name=airbyte_config.workspace_name,
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
            data=result.data,
            meta=result.meta
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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: RepositoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> RepositoriesSearchResult:
        """
        Search repositories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (RepositoriesSearchFilter):
        - id: GraphQL node ID of the repository
        - name: Short repository name (without owner)
        - name_with_owner: Fully-qualified `owner/name` identifier for the repository
        - description: Short description of the repository
        - url: Canonical GitHub URL for the repository
        - created_at: ISO 8601 timestamp when the repository was created
        - updated_at: ISO 8601 timestamp when the repository was last updated
        - pushed_at: ISO 8601 timestamp of the most recent push to the repository
        - fork_count: Number of forks of the repository
        - stargazer_count: Number of users who have starred the repository
        - is_private: Whether the repository is private
        - is_fork: Whether the repository is a fork of another repository
        - is_archived: Whether the repository has been archived

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            RepositoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("repositories", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return RepositoriesSearchResult(
            data=[
                RepositoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: OrgRepositoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrgRepositoriesSearchResult:
        """
        Search org_repositories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrgRepositoriesSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrgRepositoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("org_repositories", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrgRepositoriesSearchResult(
            data=[
                OrgRepositoriesSearchData(**row)
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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
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
        - name: Branch name (e.g. `main`, `feature/foo`)
        - prefix: Git ref prefix for the branch (typically `refs/heads/`)

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

        result = await self._connector.execute("branches", "context_store_search", params)

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
        path: str | None = None,
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
            path: Only include commits that modified this file path (e.g. "airbyte-integrations/connectors/source-stripe/")
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
            "path": path,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("commits", "list", params)
        # Cast generic envelope to concrete typed result
        return CommitsListResult(
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
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
        - oid: Full Git commit SHA
        - abbreviated_oid: Abbreviated Git commit SHA (typically 7 characters)
        - message_headline: First line of the commit message
        - message: Full commit message
        - committed_date: ISO 8601 timestamp when the commit was applied to its tree
        - authored_date: ISO 8601 timestamp when the commit was originally authored
        - additions: Number of lines added across all files in the commit
        - deletions: Number of lines deleted across all files in the commit
        - changed_files: Number of files changed in the commit
        - url: Permalink to the commit on GitHub

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

        result = await self._connector.execute("commits", "context_store_search", params)

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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
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
        - id: GraphQL node ID of the release
        - database_id: REST API numeric identifier for the release
        - name: Display name of the release
        - tag_name: Git tag the release points at (e.g. `v1.2.3`)
        - description: Markdown body / release notes
        - published_at: ISO 8601 timestamp when the release was published
        - created_at: ISO 8601 timestamp when the release was created
        - is_prerelease: Whether the release is marked as a pre-release
        - is_draft: Whether the release is still a draft and not published
        - url: Permalink to the release on GitHub

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

        result = await self._connector.execute("releases", "context_store_search", params)

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
            data=result.data,
            meta=result.meta
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
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        title: str,
        owner: str,
        repo: str,
        body: str | None = None,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
        milestone: int | None | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Creates a new issue in the specified repository.
Any user with pull access to a repository can create an issue.
Labels and assignees are silently dropped if the authenticated user does not have push access.


        Args:
            title: The title of the issue
            body: The contents of the issue (supports Markdown)
            labels: Labels to associate with this issue (requires push access)
            assignees: Logins for users to assign to this issue (requires push access)
            milestone: The number of the milestone to associate this issue with (requires push access)
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body": body,
            "labels": labels,
            "assignees": assignees,
            "milestone": milestone,
            "owner": owner,
            "repo": repo,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "create", params)
        return result



    async def update(
        self,
        owner: str,
        repo: str,
        issue_number: str,
        title: str | None = None,
        body: str | None = None,
        state: str | None = None,
        state_reason: str | None | None = None,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
        milestone: int | None | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Updates an existing issue in the specified repository.
Use this to close/reopen issues, change title/body, add/remove labels, assign users, or set milestones.
Any user with push access can update an issue.


        Args:
            title: The title of the issue
            body: The contents of the issue (supports Markdown)
            state: State of the issue: open or closed
            state_reason: Reason for the state change: completed, not_planned, reopened, or null
            labels: Labels to set on this issue (replaces all existing labels; requires push access)
            assignees: Logins for users to assign to this issue (replaces all existing assignees; requires push access)
            milestone: The number of the milestone to associate this issue with, or null to remove the milestone (requires push access)
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            issue_number: The number that identifies the issue
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body": body,
            "state": state,
            "state_reason": state_reason,
            "labels": labels,
            "assignees": assignees,
            "milestone": milestone,
            "owner": owner,
            "repo": repo,
            "issue_number": issue_number,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "update", params)
        return result



    async def context_store_search(
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
        - id: GraphQL node ID of the issue
        - database_id: REST API numeric identifier for the issue
        - number: Repository-scoped issue number
        - title: Issue title
        - state: Issue state: `OPEN` or `CLOSED`
        - state_reason: Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)
        - created_at: ISO 8601 timestamp when the issue was created
        - updated_at: ISO 8601 timestamp when the issue was last updated
        - closed_at: ISO 8601 timestamp when the issue was closed, if applicable
        - locked: Whether the conversation on the issue is locked
        - url: Permalink to the issue on GitHub

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

        result = await self._connector.execute("issues", "context_store_search", params)

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

class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        body: str,
        owner: str,
        repo: str,
        issue_number: str,
        **kwargs
    ) -> CommentResponse:
        """
        Creates a comment on the specified issue.
This endpoint works for both issues and pull requests, since pull requests are issues.
Any user with read access can create a comment.


        Args:
            body: The contents of the comment (supports Markdown)
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            issue_number: The number that identifies the issue or pull request
            **kwargs: Additional parameters

        Returns:
            CommentResponse
        """
        params = {k: v for k, v in {
            "body": body,
            "owner": owner,
            "repo": repo,
            "issue_number": issue_number,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "create", params)
        return result



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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
        self,
        query: CommentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CommentsSearchResult:
        """
        Search comments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CommentsSearchFilter):
        - id: GraphQL node ID of the comment
        - database_id: REST API numeric identifier for the comment
        - body: Markdown body of the comment
        - created_at: ISO 8601 timestamp when the comment was created
        - updated_at: ISO 8601 timestamp when the comment was last updated
        - url: Permalink to the comment on GitHub
        - is_minimized: Whether the comment has been hidden/collapsed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CommentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("comments", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CommentsSearchResult(
            data=[
                CommentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class PullRequestsQuery:
    """
    Query class for PullRequests entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        title: str,
        head: str,
        base: str,
        owner: str,
        repo: str,
        body: str | None = None,
        draft: bool | None = None,
        maintainer_can_modify: bool | None = None,
        **kwargs
    ) -> PullRequestResponse:
        """
        Creates a new pull request in the specified repository.
To open or update a pull request in a public repository, you must have write access to the head or the source branch.


        Args:
            title: The title of the new pull request
            head: The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace head with a user like this: username:branch
            base: The name of the branch you want the changes pulled into (e.g. main)
            body: The contents of the pull request (supports Markdown)
            draft: Indicates whether the pull request is a draft
            maintainer_can_modify: Indicates whether maintainers can modify the pull request
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            **kwargs: Additional parameters

        Returns:
            PullRequestResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "head": head,
            "base": base,
            "body": body,
            "draft": draft,
            "maintainer_can_modify": maintainer_can_modify,
            "owner": owner,
            "repo": repo,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pull_requests", "create", params)
        return result



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
            data=result.data,
            meta=result.meta
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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: PullRequestsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PullRequestsSearchResult:
        """
        Search pull_requests records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PullRequestsSearchFilter):
        - id: GraphQL node ID of the pull request
        - database_id: REST API numeric identifier for the pull request
        - number: Repository-scoped pull request number
        - title: Pull request title
        - state: Pull request state: `OPEN`, `CLOSED`, or `MERGED`
        - is_draft: Whether the pull request is still a draft
        - merged: Whether the pull request has been merged
        - created_at: ISO 8601 timestamp when the pull request was created
        - updated_at: ISO 8601 timestamp when the pull request was last updated
        - closed_at: ISO 8601 timestamp when the pull request was closed, if applicable
        - merged_at: ISO 8601 timestamp when the pull request was merged, if applicable
        - base_ref_name: Name of the branch being merged into
        - head_ref_name: Name of the branch with the proposed changes
        - url: Permalink to the pull request on GitHub

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PullRequestsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("pull_requests", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PullRequestsSearchResult(
            data=[
                PullRequestsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: ReviewsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ReviewsSearchResult:
        """
        Search reviews records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ReviewsSearchFilter):
        - id: GraphQL node ID of the review
        - database_id: REST API numeric identifier for the review
        - state: Review state: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`
        - body: Review body text
        - submitted_at: ISO 8601 timestamp when the review was submitted
        - created_at: ISO 8601 timestamp when the review was created
        - updated_at: ISO 8601 timestamp when the review was last updated
        - url: Permalink to the review on GitHub

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ReviewsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("reviews", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ReviewsSearchResult(
            data=[
                ReviewsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
        self,
        query: PrCommentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PrCommentsSearchResult:
        """
        Search pr_comments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PrCommentsSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PrCommentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("pr_comments", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PrCommentsSearchResult(
            data=[
                PrCommentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
        self,
        query: LabelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LabelsSearchResult:
        """
        Search labels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LabelsSearchFilter):
        - id: GraphQL node ID of the label
        - name: Label name
        - color: Label color as a 6-character hex string without a leading `#`
        - description: Short description of what the label is used for
        - created_at: ISO 8601 timestamp when the label was created
        - url: Permalink to the label on GitHub

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LabelsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("labels", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LabelsSearchResult(
            data=[
                LabelsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
        self,
        query: MilestonesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MilestonesSearchResult:
        """
        Search milestones records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MilestonesSearchFilter):
        - id: GraphQL node ID of the milestone
        - number: Repository-scoped milestone number
        - title: Milestone title
        - description: Milestone description
        - state: Milestone state: `OPEN` or `CLOSED`
        - due_on: ISO 8601 timestamp for the milestone's due date, if set
        - closed_at: ISO 8601 timestamp when the milestone was closed, if applicable
        - created_at: ISO 8601 timestamp when the milestone was created
        - updated_at: ISO 8601 timestamp when the milestone was last updated
        - progress_percentage: Percentage of associated issues/PRs that are closed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MilestonesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("milestones", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MilestonesSearchResult(
            data=[
                MilestonesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: OrganizationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrganizationsSearchResult:
        """
        Search organizations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrganizationsSearchFilter):
        - id: GraphQL node ID of the organization
        - database_id: REST API numeric identifier for the organization
        - login: Organization login/handle (unique URL slug)
        - name: Display name of the organization
        - description: Short public description of the organization
        - email: Public contact email for the organization, if set
        - location: Public location of the organization, if set
        - is_verified: Whether the organization has a verified domain
        - created_at: ISO 8601 timestamp when the organization was created

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrganizationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("organizations", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrganizationsSearchResult(
            data=[
                OrganizationsSearchData(**row)
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
            data=result.data,
            meta=result.meta
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
            data=result.data,
            meta=result.meta
        )



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
        - id: GraphQL node ID of the user
        - database_id: REST API numeric identifier for the user
        - login: User login/handle
        - name: Public display name of the user, if set
        - email: Public email address of the user, if set
        - company: Public company affiliation of the user, if set
        - location: Public location of the user, if set
        - twitter_username: Public Twitter/X username of the user, if set
        - url: Permalink to the user's profile on GitHub
        - created_at: ISO 8601 timestamp when the user account was created
        - is_hireable: Whether the user has marked themselves as available for hire

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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
        self,
        query: TeamsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TeamsSearchResult:
        """
        Search teams records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TeamsSearchFilter):
        - id: GraphQL node ID of the team
        - database_id: REST API numeric identifier for the team
        - slug: URL-friendly slug for the team within its organization
        - name: Display name of the team
        - description: Short description of the team
        - privacy: Team visibility: `SECRET` or `VISIBLE`
        - url: Permalink to the team on GitHub
        - created_at: ISO 8601 timestamp when the team was created
        - updated_at: ISO 8601 timestamp when the team was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TeamsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("teams", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TeamsSearchResult(
            data=[
                TeamsSearchData(**row)
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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
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
        - name: Tag name (e.g. `v1.2.3`)
        - prefix: Git ref prefix for the tag (typically `refs/tags/`)

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

        result = await self._connector.execute("tags", "context_store_search", params)

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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: StargazersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> StargazersSearchResult:
        """
        Search stargazers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (StargazersSearchFilter):
        - starred_at: ISO 8601 timestamp when the user starred the repository

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            StargazersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("stargazers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return StargazersSearchResult(
            data=[
                StargazersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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



    async def context_store_search(
        self,
        query: ViewerSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ViewerSearchResult:
        """
        Search viewer records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ViewerSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ViewerSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("viewer", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ViewerSearchResult(
            data=[
                ViewerSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: ViewerRepositoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ViewerRepositoriesSearchResult:
        """
        Search viewer_repositories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ViewerRepositoriesSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ViewerRepositoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("viewer_repositories", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ViewerRepositoriesSearchResult(
            data=[
                ViewerRepositoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            data=result.data,
            meta=result.meta
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



    async def context_store_search(
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
        - id: GraphQL node ID of the project
        - number: Organization- or user-scoped project number
        - title: Project title
        - short_description: Short description displayed on the project summary
        - url: Permalink to the project on GitHub
        - closed: Whether the project has been closed
        - public: Whether the project is publicly visible
        - created_at: ISO 8601 timestamp when the project was created
        - updated_at: ISO 8601 timestamp when the project was last updated

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

        result = await self._connector.execute("projects", "context_store_search", params)

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
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: ProjectItemsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProjectItemsSearchResult:
        """
        Search project_items records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProjectItemsSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProjectItemsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("project_items", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProjectItemsSearchResult(
            data=[
                ProjectItemsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DiscussionsQuery:
    """
    Query class for Discussions entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        states: list[str] | None = None,
        answered: bool | None = None,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> DiscussionsListResult:
        """
        Returns a list of discussions for the specified repository using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            states: Filter by discussion state
            answered: Filter by answered/unanswered status
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            DiscussionsListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "states": states,
            "answered": answered,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discussions", "list", params)
        # Cast generic envelope to concrete typed result
        return DiscussionsListResult(
            data=result.data,
            meta=result.meta
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
        Gets information about a specific discussion by number using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The discussion number
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

        result = await self._connector.execute("discussions", "get", params)
        return result



    async def api_search(
        self,
        query: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> DiscussionsApiSearchResult:
        """
        Search for discussions using GitHub's search syntax

        Args:
            query: GitHub discussion search query using GitHub's search syntax
            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            DiscussionsApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discussions", "api_search", params)
        # Cast generic envelope to concrete typed result
        return DiscussionsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: DiscussionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DiscussionsSearchResult:
        """
        Search discussions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DiscussionsSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DiscussionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("discussions", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DiscussionsSearchResult(
            data=[
                DiscussionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class FileContentQuery:
    """
    Query class for FileContent entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        owner: str,
        repo: str,
        path: str,
        ref: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns the text content of a file at a specific path and git ref (branch, tag, or commit SHA).
Only works for text files. Binary files will have text as null and isBinary as true.


        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            path: The file path within the repository (e.g. 'README.md' or 'src/main.py')
            ref: The git ref to read from — branch name, tag, or commit SHA. Defaults to 'HEAD' (default branch)
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "path": path,
            "ref": ref,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("file_content", "get", params)
        return result



    async def context_store_search(
        self,
        query: FileContentSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FileContentSearchResult:
        """
        Search file_content records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FileContentSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FileContentSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("file_content", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FileContentSearchResult(
            data=[
                FileContentSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DirectoryContentQuery:
    """
    Query class for DirectoryContent entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        owner: str,
        repo: str,
        path: str,
        ref: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> DirectoryContentListResult:
        """
        Returns a list of files and subdirectories at a specific path in the repository.
Each entry includes the name, type (blob for files, tree for directories), and object ID.
Use this to explore repository structure before reading specific files.


        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            path: The directory path within the repository (e.g. 'src' or 'airbyte-integrations/connectors/source-stripe')
            ref: The git ref — branch name, tag, or commit SHA. Defaults to 'HEAD' (default branch)
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            DirectoryContentListResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "path": path,
            "ref": ref,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("directory_content", "list", params)
        # Cast generic envelope to concrete typed result
        return DirectoryContentListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: DirectoryContentSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DirectoryContentSearchResult:
        """
        Search directory_content records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DirectoryContentSearchFilter):

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DirectoryContentSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("directory_content", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DirectoryContentSearchResult(
            data=[
                DirectoryContentSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
