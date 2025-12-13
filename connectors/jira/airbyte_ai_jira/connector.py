"""
jira connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    IssueCommentsGetParams,
    IssueCommentsListParams,
    IssueFieldsListParams,
    IssueFieldsSearchParams,
    IssueWorklogsGetParams,
    IssueWorklogsListParams,
    IssuesGetParams,
    IssuesSearchParams,
    ProjectsGetParams,
    ProjectsSearchParams,
    UsersGetParams,
    UsersListParams,
    UsersSearchParams,
)

if TYPE_CHECKING:
    from .models import JiraAuthConfig
# Import response models and envelope models at runtime
from .models import (
    JiraExecuteResult,
    JiraExecuteResultWithMeta,
    IssuesSearchResult,
    ProjectsSearchResult,
    IssueCommentsListResult,
    IssueWorklogsListResult,
    Issue,
    IssueComment,
    IssueFieldSearchResults,
    Project,
    User,
    Worklog,
)


class JiraConnector:
    """
    Type-safe Jira API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "jira"
    connector_version = "1.0.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("issues", "search"): True,
        ("issues", "get"): False,
        ("projects", "search"): True,
        ("projects", "get"): False,
        ("users", "get"): False,
        ("users", "list"): False,
        ("users", "search"): False,
        ("issue_fields", "list"): False,
        ("issue_fields", "search"): False,
        ("issue_comments", "list"): True,
        ("issue_comments", "get"): False,
        ("issue_worklogs", "list"): True,
        ("issue_worklogs", "get"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('issues', 'search'): {'jql': 'jql', 'next_page_token': 'nextPageToken', 'max_results': 'maxResults', 'fields': 'fields', 'expand': 'expand', 'properties': 'properties', 'fields_by_keys': 'fieldsByKeys', 'fail_fast': 'failFast'},
        ('issues', 'get'): {'issue_id_or_key': 'issueIdOrKey', 'fields': 'fields', 'expand': 'expand', 'properties': 'properties', 'fields_by_keys': 'fieldsByKeys', 'update_history': 'updateHistory', 'fail_fast': 'failFast'},
        ('projects', 'search'): {'start_at': 'startAt', 'max_results': 'maxResults', 'order_by': 'orderBy', 'id': 'id', 'keys': 'keys', 'query': 'query', 'type_key': 'typeKey', 'category_id': 'categoryId', 'action': 'action', 'expand': 'expand', 'status': 'status'},
        ('projects', 'get'): {'project_id_or_key': 'projectIdOrKey', 'expand': 'expand', 'properties': 'properties'},
        ('users', 'get'): {'account_id': 'accountId', 'expand': 'expand'},
        ('users', 'list'): {'start_at': 'startAt', 'max_results': 'maxResults'},
        ('users', 'search'): {'query': 'query', 'start_at': 'startAt', 'max_results': 'maxResults', 'account_id': 'accountId', 'property': 'property'},
        ('issue_fields', 'search'): {'start_at': 'startAt', 'max_results': 'maxResults', 'type': 'type', 'id': 'id', 'query': 'query', 'order_by': 'orderBy', 'expand': 'expand'},
        ('issue_comments', 'list'): {'issue_id_or_key': 'issueIdOrKey', 'start_at': 'startAt', 'max_results': 'maxResults', 'order_by': 'orderBy', 'expand': 'expand'},
        ('issue_comments', 'get'): {'issue_id_or_key': 'issueIdOrKey', 'comment_id': 'commentId', 'expand': 'expand'},
        ('issue_worklogs', 'list'): {'issue_id_or_key': 'issueIdOrKey', 'start_at': 'startAt', 'max_results': 'maxResults', 'expand': 'expand'},
        ('issue_worklogs', 'get'): {'issue_id_or_key': 'issueIdOrKey', 'worklog_id': 'worklogId', 'expand': 'expand'},
    }

    def __init__(
        self,
        auth_config: JiraAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new jira connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Jira Cloud subdomain
        Examples:
            # Local mode (direct API calls)
            connector = JiraConnector(auth_config=JiraAuthConfig(username="...", password="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = JiraConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = JiraConnector(
                auth_config=JiraAuthConfig(access_token="...", refresh_token="..."),
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
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            self._executor = LocalExecutor(
                config_path=config_path,
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
        self.issues = IssuesQuery(self)
        self.projects = ProjectsQuery(self)
        self.users = UsersQuery(self)
        self.issue_fields = IssueFieldsQuery(self)
        self.issue_comments = IssueCommentsQuery(self)
        self.issue_worklogs = IssueWorklogsQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["issues"],
        action: Literal["get"],
        params: "IssuesGetParams"
    ) -> "Issue": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["search"],
        params: "ProjectsSearchParams"
    ) -> "ProjectsSearchResult": ...

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
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["search"],
        params: "UsersSearchParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_fields"],
        action: Literal["list"],
        params: "IssueFieldsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_fields"],
        action: Literal["search"],
        params: "IssueFieldsSearchParams"
    ) -> "IssueFieldSearchResults": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_comments"],
        action: Literal["list"],
        params: "IssueCommentsListParams"
    ) -> "IssueCommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_comments"],
        action: Literal["get"],
        params: "IssueCommentsGetParams"
    ) -> "IssueComment": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_worklogs"],
        action: Literal["list"],
        params: "IssueWorklogsListParams"
    ) -> "IssueWorklogsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_worklogs"],
        action: Literal["get"],
        params: "IssueWorklogsGetParams"
    ) -> "Worklog": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> JiraExecuteResult[Any] | JiraExecuteResultWithMeta[Any, Any] | Any: ...

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
                return JiraExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return JiraExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def search(
        self,
        jql: str | None = None,
        next_page_token: str | None = None,
        max_results: int | None = None,
        fields: str | None = None,
        expand: str | None = None,
        properties: str | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        **kwargs
    ) -> IssuesSearchResult:
        """
        Retrieve issues based on JQL query with pagination support

        Args:
            jql: JQL query string to filter issues
            next_page_token: The token for a page to fetch that is not the first page. The first page has a nextPageToken of null. Use the `nextPageToken` to fetch the next page of issues. The `nextPageToken` field is not included in the response for the last page, indicating there is no next page.
            max_results: The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields or properties are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only. It returns max 5000 issues.
            fields: A comma-separated list of fields to return for each issue. By default, all navigable fields are returned. To get a list of all fields, use the Get fields operation.
            expand: A comma-separated list of parameters to expand. This parameter accepts multiple values, including `renderedFields`, `names`, `schema`, `transitions`, `operations`, `editmeta`, `changelog`, and `versionedRepresentations`.
            properties: A comma-separated list of issue property keys. To get a list of all issue property keys, use the Get issue operation. A maximum of 5 properties can be requested.
            fields_by_keys: Whether the fields parameter contains field keys (true) or field IDs (false). Default is false.
            fail_fast: Fail the request early if all field data cannot be retrieved. Default is false.
            **kwargs: Additional parameters

        Returns:
            IssuesSearchResult
        """
        params = {k: v for k, v in {
            "jql": jql,
            "nextPageToken": next_page_token,
            "maxResults": max_results,
            "fields": fields,
            "expand": expand,
            "properties": properties,
            "fieldsByKeys": fields_by_keys,
            "failFast": fail_fast,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "search", params)
        # Cast generic envelope to concrete typed result
        return IssuesSearchResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        issue_id_or_key: str,
        fields: str | None = None,
        expand: str | None = None,
        properties: str | None = None,
        fields_by_keys: bool | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
        **kwargs
    ) -> Issue:
        """
        Retrieve a single issue by its ID or key

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            fields: A comma-separated list of fields to return for the issue. By default, all navigable and Jira default fields are returned. Use it to retrieve a subset of fields.
            expand: A comma-separated list of parameters to expand. This parameter accepts multiple values, including `renderedFields`, `names`, `schema`, `transitions`, `operations`, `editmeta`, `changelog`, and `versionedRepresentations`.
            properties: A comma-separated list of issue property keys. To get a list of all issue property keys, use the Get issue operation. A maximum of 5 properties can be requested.
            fields_by_keys: Whether the fields parameter contains field keys (true) or field IDs (false). Default is false.
            update_history: Whether the action taken is added to the user's Recent history. Default is false.
            fail_fast: Fail the request early if all field data cannot be retrieved. Default is false.
            **kwargs: Additional parameters

        Returns:
            Issue
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "fields": fields,
            "expand": expand,
            "properties": properties,
            "fieldsByKeys": fields_by_keys,
            "updateHistory": update_history,
            "failFast": fail_fast,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result



class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def search(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        id: list[int] | None = None,
        keys: list[str] | None = None,
        query: str | None = None,
        type_key: str | None = None,
        category_id: int | None = None,
        action: str | None = None,
        expand: str | None = None,
        status: list[str] | None = None,
        **kwargs
    ) -> ProjectsSearchResult:
        """
        Search and filter projects with advanced query parameters

        Args:
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page (max 100)
            order_by: Order the results by a field (prefix with + for ascending, - for descending)
            id: Filter by project IDs (up to 50)
            keys: Filter by project keys (up to 50)
            query: Filter using a literal string (matches project key or name, case insensitive)
            type_key: Filter by project type (comma-separated)
            category_id: Filter by project category ID
            action: Filter by user permission (view, browse, edit, create)
            expand: Comma-separated list of additional fields (description, projectKeys, lead, issueTypes, url, insight)
            status: EXPERIMENTAL - Filter by project status
            **kwargs: Additional parameters

        Returns:
            ProjectsSearchResult
        """
        params = {k: v for k, v in {
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "id": id,
            "keys": keys,
            "query": query,
            "typeKey": type_key,
            "categoryId": category_id,
            "action": action,
            "expand": expand,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "search", params)
        # Cast generic envelope to concrete typed result
        return ProjectsSearchResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        project_id_or_key: str,
        expand: str | None = None,
        properties: str | None = None,
        **kwargs
    ) -> Project:
        """
        Retrieve a single project by its ID or key

        Args:
            project_id_or_key: The project ID or key (e.g., "PROJ" or "10000")
            expand: Comma-separated list of additional fields to include (description, projectKeys, lead, issueTypes, url, insight)
            properties: A comma-separated list of project property keys to return. To get a list of all project property keys, use Get project property keys.
            **kwargs: Additional parameters

        Returns:
            Project
        """
        params = {k: v for k, v in {
            "projectIdOrKey": project_id_or_key,
            "expand": expand,
            "properties": properties,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        return result



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        account_id: str,
        expand: str | None = None,
        **kwargs
    ) -> User:
        """
        Retrieve a single user by their account ID

        Args:
            account_id: The account ID of the user
            expand: Comma-separated list of additional fields to include (groups, applicationRoles)
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "accountId": account_id,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



    async def list(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of users

        Args:
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page (max 1000)
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "startAt": start_at,
            "maxResults": max_results,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        return result



    async def search(
        self,
        query: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        account_id: str | None = None,
        property: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Search for users using a query string

        Args:
            query: A query string to search for users (matches display name, email, account ID)
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page (max 1000)
            account_id: Filter by account IDs (supports multiple values)
            property: Property key to filter users
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "query": query,
            "startAt": start_at,
            "maxResults": max_results,
            "accountId": account_id,
            "property": property,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "search", params)
        return result



class IssueFieldsQuery:
    """
    Query class for IssueFields entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a list of all custom and system fields

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_fields", "list", params)
        return result



    async def search(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        type: list[str] | None = None,
        id: list[str] | None = None,
        query: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        **kwargs
    ) -> IssueFieldSearchResults:
        """
        Search and filter issue fields with query parameters

        Args:
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page (max 100)
            type: The type of fields to search for (custom, system, or both)
            id: List of field IDs to search for
            query: String to match against field names, descriptions, and field IDs (case insensitive)
            order_by: Order the results by a field (contextsCount, lastUsed, name, screensCount)
            expand: Comma-separated list of additional fields to include (searcherKey, screensCount, contextsCount, isLocked, lastUsed)
            **kwargs: Additional parameters

        Returns:
            IssueFieldSearchResults
        """
        params = {k: v for k, v in {
            "startAt": start_at,
            "maxResults": max_results,
            "type": type,
            "id": id,
            "query": query,
            "orderBy": order_by,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_fields", "search", params)
        return result



class IssueCommentsQuery:
    """
    Query class for IssueComments entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        issue_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        **kwargs
    ) -> IssueCommentsListResult:
        """
        Retrieve all comments for a specific issue

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page
            order_by: Order the results by created date (+ for ascending, - for descending)
            expand: Comma-separated list of additional fields to include (renderedBody, properties)
            **kwargs: Additional parameters

        Returns:
            IssueCommentsListResult
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "startAt": start_at,
            "maxResults": max_results,
            "orderBy": order_by,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_comments", "list", params)
        # Cast generic envelope to concrete typed result
        return IssueCommentsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        issue_id_or_key: str,
        comment_id: str,
        expand: str | None = None,
        **kwargs
    ) -> IssueComment:
        """
        Retrieve a single comment by its ID

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            comment_id: The comment ID
            expand: Comma-separated list of additional fields to include (renderedBody, properties)
            **kwargs: Additional parameters

        Returns:
            IssueComment
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "commentId": comment_id,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_comments", "get", params)
        return result



class IssueWorklogsQuery:
    """
    Query class for IssueWorklogs entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        issue_id_or_key: str,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        **kwargs
    ) -> IssueWorklogsListResult:
        """
        Retrieve all worklogs for a specific issue

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page
            expand: Comma-separated list of additional fields to include (properties)
            **kwargs: Additional parameters

        Returns:
            IssueWorklogsListResult
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "startAt": start_at,
            "maxResults": max_results,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_worklogs", "list", params)
        # Cast generic envelope to concrete typed result
        return IssueWorklogsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        expand: str | None = None,
        **kwargs
    ) -> Worklog:
        """
        Retrieve a single worklog by its ID

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            worklog_id: The worklog ID
            expand: Comma-separated list of additional fields to include (properties)
            **kwargs: Additional parameters

        Returns:
            Worklog
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "worklogId": worklog_id,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_worklogs", "get", params)
        return result


