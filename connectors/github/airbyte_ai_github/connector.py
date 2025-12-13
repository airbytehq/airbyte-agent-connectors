"""
github connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    BranchesGetParams,
    BranchesListParams,
    CommentsGetParams,
    CommentsListParams,
    CommitsGetParams,
    CommitsListParams,
    IssuesGetParams,
    IssuesListParams,
    IssuesSearchParams,
    LabelsGetParams,
    LabelsListParams,
    MilestonesGetParams,
    MilestonesListParams,
    OrgRepositoriesListParams,
    OrganizationsGetParams,
    OrganizationsListParams,
    PrCommentsGetParams,
    PrCommentsListParams,
    PullRequestsGetParams,
    PullRequestsListParams,
    PullRequestsSearchParams,
    ReleasesGetParams,
    ReleasesListParams,
    RepositoriesGetParams,
    RepositoriesListParams,
    RepositoriesSearchParams,
    ReviewsListParams,
    StargazersListParams,
    TagsGetParams,
    TagsListParams,
    TeamsGetParams,
    TeamsListParams,
    UsersGetParams,
    UsersListParams,
    UsersSearchParams,
    ViewerGetParams,
    ViewerRepositoriesListParams,
)

if TYPE_CHECKING:
    from .models import GithubAuthConfig
# Import response models and envelope models at runtime
from .models import (
    GithubExecuteResult,
    GithubExecuteResultWithMeta,
    RepositoriesGetResult,
    RepositoriesListResult,
    RepositoriesSearchResult,
    OrgRepositoriesListResult,
    BranchesListResult,
    BranchesGetResult,
    CommitsListResult,
    CommitsGetResult,
    ReleasesListResult,
    ReleasesGetResult,
    IssuesListResult,
    IssuesGetResult,
    IssuesSearchResult,
    PullRequestsListResult,
    PullRequestsGetResult,
    PullRequestsSearchResult,
    ReviewsListResult,
    CommentsListResult,
    CommentsGetResult,
    PrCommentsListResult,
    PrCommentsGetResult,
    LabelsListResult,
    LabelsGetResult,
    MilestonesListResult,
    MilestonesGetResult,
    OrganizationsGetResult,
    OrganizationsListResult,
    UsersGetResult,
    UsersListResult,
    UsersSearchResult,
    TeamsListResult,
    TeamsGetResult,
    TagsListResult,
    TagsGetResult,
    StargazersListResult,
    ViewerGetResult,
    ViewerRepositoriesListResult,
)


class GithubConnector:
    """
    Type-safe Github API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "github"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("repositories", "get"): True,
        ("repositories", "list"): True,
        ("repositories", "search"): True,
        ("org_repositories", "list"): True,
        ("branches", "list"): True,
        ("branches", "get"): True,
        ("commits", "list"): True,
        ("commits", "get"): True,
        ("releases", "list"): True,
        ("releases", "get"): True,
        ("issues", "list"): True,
        ("issues", "get"): True,
        ("issues", "search"): True,
        ("pull_requests", "list"): True,
        ("pull_requests", "get"): True,
        ("pull_requests", "search"): True,
        ("reviews", "list"): True,
        ("comments", "list"): True,
        ("comments", "get"): True,
        ("pr_comments", "list"): True,
        ("pr_comments", "get"): True,
        ("labels", "list"): True,
        ("labels", "get"): True,
        ("milestones", "list"): True,
        ("milestones", "get"): True,
        ("organizations", "get"): True,
        ("organizations", "list"): True,
        ("users", "get"): True,
        ("users", "list"): True,
        ("users", "search"): True,
        ("teams", "list"): True,
        ("teams", "get"): True,
        ("tags", "list"): True,
        ("tags", "get"): True,
        ("stargazers", "list"): True,
        ("viewer", "get"): True,
        ("viewer_repositories", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('repositories', 'get'): {'owner': 'owner', 'repo': 'repo', 'fields': 'fields'},
        ('repositories', 'list'): {'username': 'username', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('repositories', 'search'): {'query': 'query', 'limit': 'limit', 'after': 'after', 'fields': 'fields'},
        ('org_repositories', 'list'): {'org': 'org', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('branches', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('branches', 'get'): {'owner': 'owner', 'repo': 'repo', 'branch': 'branch', 'fields': 'fields'},
        ('commits', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('commits', 'get'): {'owner': 'owner', 'repo': 'repo', 'sha': 'sha', 'fields': 'fields'},
        ('releases', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('releases', 'get'): {'owner': 'owner', 'repo': 'repo', 'tag': 'tag', 'fields': 'fields'},
        ('issues', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('issues', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('issues', 'search'): {'query': 'query', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('pull_requests', 'list'): {'owner': 'owner', 'repo': 'repo', 'states': 'states', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('pull_requests', 'get'): {'owner': 'owner', 'repo': 'repo', 'number': 'number', 'fields': 'fields'},
        ('pull_requests', 'search'): {'query': 'query', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
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
        ('users', 'search'): {'query': 'query', 'limit': 'limit', 'after': 'after', 'fields': 'fields'},
        ('teams', 'list'): {'org': 'org', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('teams', 'get'): {'org': 'org', 'team_slug': 'team_slug', 'fields': 'fields'},
        ('tags', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('tags', 'get'): {'owner': 'owner', 'repo': 'repo', 'tag': 'tag', 'fields': 'fields'},
        ('stargazers', 'list'): {'owner': 'owner', 'repo': 'repo', 'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
        ('viewer', 'get'): {'fields': 'fields'},
        ('viewer_repositories', 'list'): {'per_page': 'per_page', 'after': 'after', 'fields': 'fields'},
    }

    def __init__(
        self,
        auth_config: GithubAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new github connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            airbyte_connector_api_url: Airbyte connector API URL (defaults to Airbyte Cloud API URL)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = GithubConnector(
                connector_id="connector-456",
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
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            if not config_path:
                config_path = str(self.get_default_config_path())

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
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

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["get"],
        params: "RepositoriesGetParams"
    ) -> "RepositoriesGetResult": ...

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
        action: Literal["search"],
        params: "RepositoriesSearchParams"
    ) -> "RepositoriesSearchResult": ...

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
    ) -> "BranchesGetResult": ...

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
    ) -> "CommitsGetResult": ...

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
    ) -> "ReleasesGetResult": ...

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
    ) -> "IssuesGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["search"],
        params: "IssuesSearchParams"
    ) -> "IssuesSearchResult": ...

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
    ) -> "PullRequestsGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pull_requests"],
        action: Literal["search"],
        params: "PullRequestsSearchParams"
    ) -> "PullRequestsSearchResult": ...

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
    ) -> "CommentsGetResult": ...

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
    ) -> "PrCommentsGetResult": ...

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
    ) -> "LabelsGetResult": ...

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
    ) -> "MilestonesGetResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["organizations"],
        action: Literal["get"],
        params: "OrganizationsGetParams"
    ) -> "OrganizationsGetResult": ...

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
    ) -> "UsersGetResult": ...

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
        action: Literal["search"],
        params: "UsersSearchParams"
    ) -> "UsersSearchResult": ...

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
    ) -> "TeamsGetResult": ...

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
    ) -> "TagsGetResult": ...

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
    ) -> "ViewerGetResult": ...

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
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> GithubExecuteResult[Any] | GithubExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None
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
        if params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                params = {param_map.get(k, k): v for k, v in params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._EXTRACTOR_MAP.get((entity, action), False)

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
    ) -> RepositoriesGetResult:
        """
        Gets information about a specific GitHub repository using GraphQL

        Args:
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            RepositoriesGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "get", params)
        # Cast generic envelope to concrete typed result
        return RepositoriesGetResult(
            data=result.data        )



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
            data=result.data        )



    async def search(
        self,
        query: str,
        limit: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> RepositoriesSearchResult:
        """
        Search for GitHub repositories using GitHub's powerful search syntax.
Examples: "language:python stars:>1000", "topic:machine-learning", "org:facebook is:public"


        Args:
            query: GitHub repository search query. Examples:
- "language:python stars:>1000"
- "topic:machine-learning"
- "org:facebook is:public"

            limit: Number of results to return
            after: Cursor for pagination (from previous response's endCursor)
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            RepositoriesSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "search", params)
        # Cast generic envelope to concrete typed result
        return RepositoriesSearchResult(
            data=result.data        )



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
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        branch: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> BranchesGetResult:
        """
        Gets information about a specific branch using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            branch: The branch name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            BranchesGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("branches", "get", params)
        # Cast generic envelope to concrete typed result
        return BranchesGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> CommitsGetResult:
        """
        Gets information about a specific commit by SHA using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            sha: The commit SHA
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            CommitsGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "sha": sha,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("commits", "get", params)
        # Cast generic envelope to concrete typed result
        return CommitsGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        tag: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> ReleasesGetResult:
        """
        Gets information about a specific release by tag name using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            tag: The release tag name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ReleasesGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "tag": tag,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("releases", "get", params)
        # Cast generic envelope to concrete typed result
        return ReleasesGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> IssuesGetResult:
        """
        Gets information about a specific issue using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The issue number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            IssuesGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        # Cast generic envelope to concrete typed result
        return IssuesGetResult(
            data=result.data        )



    async def search(
        self,
        query: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> IssuesSearchResult:
        """
        Search for issues using GitHub's search syntax

        Args:
            query: GitHub issue search query. Examples:
- "repo:owner/name is:issue is:open"
- "repo:owner/name is:issue label:bug"

            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            IssuesSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "search", params)
        # Cast generic envelope to concrete typed result
        return IssuesSearchResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> PullRequestsGetResult:
        """
        Gets information about a specific pull request using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The pull request number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            PullRequestsGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pull_requests", "get", params)
        # Cast generic envelope to concrete typed result
        return PullRequestsGetResult(
            data=result.data        )



    async def search(
        self,
        query: str,
        per_page: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> PullRequestsSearchResult:
        """
        Search for pull requests using GitHub's search syntax

        Args:
            query: GitHub PR search query. Examples:
- "repo:owner/name type:pr is:open"
- "repo:owner/name type:pr author:username"

            per_page: The number of results per page
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            PullRequestsSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "per_page": per_page,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pull_requests", "search", params)
        # Cast generic envelope to concrete typed result
        return PullRequestsSearchResult(
            data=result.data        )



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
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        id: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> CommentsGetResult:
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
            CommentsGetResult
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "get", params)
        # Cast generic envelope to concrete typed result
        return CommentsGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        id: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> PrCommentsGetResult:
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
            PrCommentsGetResult
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pr_comments", "get", params)
        # Cast generic envelope to concrete typed result
        return PrCommentsGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        name: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> LabelsGetResult:
        """
        Gets information about a specific label by name using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            name: The label name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            LabelsGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "name": name,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "get", params)
        # Cast generic envelope to concrete typed result
        return LabelsGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        number: int,
        fields: list[str] | None = None,
        **kwargs
    ) -> MilestonesGetResult:
        """
        Gets information about a specific milestone by number using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            number: The milestone number
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            MilestonesGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "number": number,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("milestones", "get", params)
        # Cast generic envelope to concrete typed result
        return MilestonesGetResult(
            data=result.data        )



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
    ) -> OrganizationsGetResult:
        """
        Gets information about a specific organization using GraphQL

        Args:
            org: The organization login/username
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            OrganizationsGetResult
        """
        params = {k: v for k, v in {
            "org": org,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("organizations", "get", params)
        # Cast generic envelope to concrete typed result
        return OrganizationsGetResult(
            data=result.data        )



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
            data=result.data        )



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
    ) -> UsersGetResult:
        """
        Gets information about a specific user using GraphQL

        Args:
            username: The username of the user
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            UsersGetResult
        """
        params = {k: v for k, v in {
            "username": username,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        # Cast generic envelope to concrete typed result
        return UsersGetResult(
            data=result.data        )



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
            data=result.data        )



    async def search(
        self,
        query: str,
        limit: int | None = None,
        after: str | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> UsersSearchResult:
        """
        Search for GitHub users using search syntax

        Args:
            query: GitHub user search query. Examples:
- "location:san francisco"
- "followers:>1000"

            limit: Number of results to return
            after: Cursor for pagination
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            UsersSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "after": after,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "search", params)
        # Cast generic envelope to concrete typed result
        return UsersSearchResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        org: str,
        team_slug: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> TeamsGetResult:
        """
        Gets information about a specific team using GraphQL

        Args:
            org: The organization login/username
            team_slug: The team slug
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            TeamsGetResult
        """
        params = {k: v for k, v in {
            "org": org,
            "team_slug": team_slug,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        # Cast generic envelope to concrete typed result
        return TeamsGetResult(
            data=result.data        )



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
            data=result.data        )



    async def get(
        self,
        owner: str,
        repo: str,
        tag: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> TagsGetResult:
        """
        Gets information about a specific tag by name using GraphQL

        Args:
            owner: The account owner of the repository
            repo: The name of the repository
            tag: The tag name
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            TagsGetResult
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "tag": tag,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "get", params)
        # Cast generic envelope to concrete typed result
        return TagsGetResult(
            data=result.data        )



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
            data=result.data        )



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
    ) -> ViewerGetResult:
        """
        Gets information about the currently authenticated user.
This is useful when you don't know the username but need to access
the current user's profile, permissions, or associated resources.


        Args:
            fields: Optional array of field names to select
            **kwargs: Additional parameters

        Returns:
            ViewerGetResult
        """
        params = {k: v for k, v in {
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("viewer", "get", params)
        # Cast generic envelope to concrete typed result
        return ViewerGetResult(
            data=result.data        )



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
            data=result.data        )


