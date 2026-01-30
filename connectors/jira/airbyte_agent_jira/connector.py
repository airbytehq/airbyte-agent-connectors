"""
Jira connector.
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

from .connector_model import JiraConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    IssueCommentsCreateParams,
    IssueCommentsCreateParamsBody,
    IssueCommentsCreateParamsVisibility,
    IssueCommentsDeleteParams,
    IssueCommentsGetParams,
    IssueCommentsListParams,
    IssueCommentsUpdateParams,
    IssueCommentsUpdateParamsBody,
    IssueCommentsUpdateParamsVisibility,
    IssueFieldsApiSearchParams,
    IssueFieldsListParams,
    IssueWorklogsGetParams,
    IssueWorklogsListParams,
    IssuesApiSearchParams,
    IssuesAssigneeUpdateParams,
    IssuesCreateParams,
    IssuesCreateParamsFields,
    IssuesDeleteParams,
    IssuesGetParams,
    IssuesUpdateParams,
    IssuesUpdateParamsFields,
    IssuesUpdateParamsTransition,
    ProjectsApiSearchParams,
    ProjectsGetParams,
    UsersApiSearchParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    IssuesSearchFilter,
    IssuesSearchQuery,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    IssueCommentsSearchFilter,
    IssueCommentsSearchQuery,
    IssueFieldsSearchFilter,
    IssueFieldsSearchQuery,
    IssueWorklogsSearchFilter,
    IssueWorklogsSearchQuery,
)
if TYPE_CHECKING:
    from .models import JiraAuthConfig
# Import response models and envelope models at runtime
from .models import (
    JiraCheckResult,
    JiraExecuteResult,
    JiraExecuteResultWithMeta,
    IssuesApiSearchResult,
    ProjectsApiSearchResult,
    UsersListResult,
    UsersApiSearchResult,
    IssueFieldsListResult,
    IssueFieldsApiSearchResult,
    IssueCommentsListResult,
    IssueWorklogsListResult,
    Issue,
    IssueComment,
    IssueCreateResponse,
    IssueField,
    IssueFieldSearchResults,
    Project,
    User,
    Worklog,
    AirbyteSearchHit,
    AirbyteSearchResult,
    IssuesSearchData,
    IssuesSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    UsersSearchData,
    UsersSearchResult,
    IssueCommentsSearchData,
    IssueCommentsSearchResult,
    IssueFieldsSearchData,
    IssueFieldsSearchResult,
    IssueWorklogsSearchData,
    IssueWorklogsSearchResult,
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




class JiraConnector:
    """
    Type-safe Jira API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "jira"
    connector_version = "1.1.4"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("issues", "api_search"): True,
        ("issues", "create"): None,
        ("issues", "get"): None,
        ("issues", "update"): None,
        ("issues", "delete"): None,
        ("projects", "api_search"): True,
        ("projects", "get"): None,
        ("users", "get"): None,
        ("users", "list"): True,
        ("users", "api_search"): True,
        ("issue_fields", "list"): True,
        ("issue_fields", "api_search"): True,
        ("issue_comments", "list"): True,
        ("issue_comments", "create"): None,
        ("issue_comments", "get"): None,
        ("issue_comments", "update"): None,
        ("issue_comments", "delete"): None,
        ("issue_worklogs", "list"): True,
        ("issue_worklogs", "get"): None,
        ("issues_assignee", "update"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('issues', 'api_search'): {'jql': 'jql', 'next_page_token': 'nextPageToken', 'max_results': 'maxResults', 'fields': 'fields', 'expand': 'expand', 'properties': 'properties', 'fields_by_keys': 'fieldsByKeys', 'fail_fast': 'failFast'},
        ('issues', 'create'): {'fields': 'fields', 'update': 'update', 'update_history': 'updateHistory'},
        ('issues', 'get'): {'issue_id_or_key': 'issueIdOrKey', 'fields': 'fields', 'expand': 'expand', 'properties': 'properties', 'fields_by_keys': 'fieldsByKeys', 'update_history': 'updateHistory', 'fail_fast': 'failFast'},
        ('issues', 'update'): {'fields': 'fields', 'update': 'update', 'transition': 'transition', 'issue_id_or_key': 'issueIdOrKey', 'notify_users': 'notifyUsers', 'override_screen_security': 'overrideScreenSecurity', 'override_editable_flag': 'overrideEditableFlag', 'return_issue': 'returnIssue', 'expand': 'expand'},
        ('issues', 'delete'): {'issue_id_or_key': 'issueIdOrKey', 'delete_subtasks': 'deleteSubtasks'},
        ('projects', 'api_search'): {'start_at': 'startAt', 'max_results': 'maxResults', 'order_by': 'orderBy', 'id': 'id', 'keys': 'keys', 'query': 'query', 'type_key': 'typeKey', 'category_id': 'categoryId', 'action': 'action', 'expand': 'expand', 'status': 'status'},
        ('projects', 'get'): {'project_id_or_key': 'projectIdOrKey', 'expand': 'expand', 'properties': 'properties'},
        ('users', 'get'): {'account_id': 'accountId', 'expand': 'expand'},
        ('users', 'list'): {'start_at': 'startAt', 'max_results': 'maxResults'},
        ('users', 'api_search'): {'query': 'query', 'start_at': 'startAt', 'max_results': 'maxResults', 'account_id': 'accountId', 'property': 'property'},
        ('issue_fields', 'api_search'): {'start_at': 'startAt', 'max_results': 'maxResults', 'type': 'type', 'id': 'id', 'query': 'query', 'order_by': 'orderBy', 'expand': 'expand'},
        ('issue_comments', 'list'): {'issue_id_or_key': 'issueIdOrKey', 'start_at': 'startAt', 'max_results': 'maxResults', 'order_by': 'orderBy', 'expand': 'expand'},
        ('issue_comments', 'create'): {'body': 'body', 'visibility': 'visibility', 'properties': 'properties', 'issue_id_or_key': 'issueIdOrKey', 'expand': 'expand'},
        ('issue_comments', 'get'): {'issue_id_or_key': 'issueIdOrKey', 'comment_id': 'commentId', 'expand': 'expand'},
        ('issue_comments', 'update'): {'body': 'body', 'visibility': 'visibility', 'issue_id_or_key': 'issueIdOrKey', 'comment_id': 'commentId', 'notify_users': 'notifyUsers', 'expand': 'expand'},
        ('issue_comments', 'delete'): {'issue_id_or_key': 'issueIdOrKey', 'comment_id': 'commentId'},
        ('issue_worklogs', 'list'): {'issue_id_or_key': 'issueIdOrKey', 'start_at': 'startAt', 'max_results': 'maxResults', 'expand': 'expand'},
        ('issue_worklogs', 'get'): {'issue_id_or_key': 'issueIdOrKey', 'worklog_id': 'worklogId', 'expand': 'expand'},
        ('issues_assignee', 'update'): {'account_id': 'accountId', 'issue_id_or_key': 'issueIdOrKey'},
    }

    def __init__(
        self,
        auth_config: JiraAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new jira connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `external_user_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Jira Cloud subdomain
        Examples:
            # Local mode (direct API calls)
            connector = JiraConnector(auth_config=JiraAuthConfig(username="...", password="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = JiraConnector(
                external_user_id="user-123",
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
        # Hosted mode: external_user_id, airbyte_client_id, and airbyte_client_secret provided
        if external_user_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                external_user_id=external_user_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_definition_id=str(JiraConnectorModel.id),
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (external_user_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            self._executor = LocalExecutor(
                model=JiraConnectorModel,
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
        self.issues_assignee = IssuesAssigneeQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
    ) -> "IssueCreateResponse": ...

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
        entity: Literal["issues"],
        action: Literal["update"],
        params: "IssuesUpdateParams"
    ) -> "Issue": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["delete"],
        params: "IssuesDeleteParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["api_search"],
        params: "ProjectsApiSearchParams"
    ) -> "ProjectsApiSearchResult": ...

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
        entity: Literal["issue_fields"],
        action: Literal["list"],
        params: "IssueFieldsListParams"
    ) -> "IssueFieldsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_fields"],
        action: Literal["api_search"],
        params: "IssueFieldsApiSearchParams"
    ) -> "IssueFieldsApiSearchResult": ...

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
        action: Literal["create"],
        params: "IssueCommentsCreateParams"
    ) -> "IssueComment": ...

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
        entity: Literal["issue_comments"],
        action: Literal["update"],
        params: "IssueCommentsUpdateParams"
    ) -> "IssueComment": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_comments"],
        action: Literal["delete"],
        params: "IssueCommentsDeleteParams"
    ) -> "dict[str, Any]": ...

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
        entity: Literal["issues_assignee"],
        action: Literal["update"],
        params: "IssuesAssigneeUpdateParams"
    ) -> "dict[str, Any]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["api_search", "create", "get", "update", "delete", "list", "search"],
        params: Mapping[str, Any]
    ) -> JiraExecuteResult[Any] | JiraExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["api_search", "create", "get", "update", "delete", "list", "search"],
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
                return JiraExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return JiraExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> JiraCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            JiraCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return JiraCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return JiraCheckResult(
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
            @JiraConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @JiraConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    JiraConnectorModel,
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
        return describe_entities(JiraConnectorModel)

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
            (e for e in JiraConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in JiraConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def api_search(
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
    ) -> IssuesApiSearchResult:
        """
        Retrieve issues based on JQL query with pagination support.

IMPORTANT: This endpoint requires a bounded JQL query. A bounded query must include a search restriction that limits the scope of the search. Examples of valid restrictions include: project (e.g., "project = MYPROJECT"), assignee (e.g., "assignee = currentUser()"), reporter, issue key, sprint, or date-based filters combined with a project restriction. An unbounded query like "order by key desc" will be rejected with a 400 error. Example bounded query: "project = MYPROJECT AND updated >= -7d ORDER BY created DESC".


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
            IssuesApiSearchResult
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

        result = await self._connector.execute("issues", "api_search", params)
        # Cast generic envelope to concrete typed result
        return IssuesApiSearchResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        fields: IssuesCreateParamsFields,
        update: dict[str, Any] | None = None,
        update_history: bool | None = None,
        **kwargs
    ) -> IssueCreateResponse:
        """
        Creates an issue or a sub-task from a JSON representation

        Args:
            fields: The issue fields to set
            update: Additional update operations to perform
            update_history: Whether the action taken is added to the user's Recent history
            **kwargs: Additional parameters

        Returns:
            IssueCreateResponse
        """
        params = {k: v for k, v in {
            "fields": fields,
            "update": update,
            "updateHistory": update_history,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "create", params)
        return result



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



    async def update(
        self,
        issue_id_or_key: str,
        fields: IssuesUpdateParamsFields | None = None,
        update: dict[str, Any] | None = None,
        transition: IssuesUpdateParamsTransition | None = None,
        notify_users: bool | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        return_issue: bool | None = None,
        expand: str | None = None,
        **kwargs
    ) -> Issue:
        """
        Edits an issue. Issue properties may be updated as part of the edit. Only fields included in the request body are updated.

        Args:
            fields: The issue fields to update
            update: Additional update operations to perform
            transition: Transition the issue to a new status
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            notify_users: Whether a notification email about the issue update is sent to all watchers. Default is true.
            override_screen_security: Whether screen security is overridden to enable hidden fields to be edited.
            override_editable_flag: Whether the issue's edit metadata is overridden.
            return_issue: Whether the updated issue is returned.
            expand: Expand options when returning the updated issue.
            **kwargs: Additional parameters

        Returns:
            Issue
        """
        params = {k: v for k, v in {
            "fields": fields,
            "update": update,
            "transition": transition,
            "issueIdOrKey": issue_id_or_key,
            "notifyUsers": notify_users,
            "overrideScreenSecurity": override_screen_security,
            "overrideEditableFlag": override_editable_flag,
            "returnIssue": return_issue,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "update", params)
        return result



    async def delete(
        self,
        issue_id_or_key: str,
        delete_subtasks: bool | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Deletes an issue. An issue cannot be deleted if it has one or more subtasks unless deleteSubtasks is true.

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            delete_subtasks: Whether to delete the issue's subtasks. Default is false.
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "deleteSubtasks": delete_subtasks,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "delete", params)
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
        - changelog: Details of changelogs associated with the issue
        - created: The timestamp when the issue was created
        - editmeta: The metadata for the fields on the issue that can be amended
        - expand: Expand options that include additional issue details in the response
        - fields: Details of various fields associated with the issue
        - fields_to_include: Specify the fields to include in the fetched issues data
        - id: The unique ID of the issue
        - key: The unique key of the issue
        - names: The ID and name of each field present on the issue
        - operations: The operations that can be performed on the issue
        - project_id: The ID of the project containing the issue
        - project_key: The key of the project containing the issue
        - properties: Details of the issue properties identified in the request
        - rendered_fields: The rendered value of each field present on the issue
        - schema_: The schema describing each field present on the issue
        - self: The URL of the issue details
        - transitions: The transitions that can be performed on the issue
        - updated: The timestamp when the issue was last updated
        - versioned_representations: The versions of each field on the issue

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IssuesSearchResult with hits (list of AirbyteSearchHit[IssuesSearchData]) and pagination info

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
        return IssuesSearchResult(
            hits=[
                AirbyteSearchHit[IssuesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=IssuesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def api_search(
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
    ) -> ProjectsApiSearchResult:
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
            ProjectsApiSearchResult
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

        result = await self._connector.execute("projects", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ProjectsApiSearchResult(
            data=result.data,
            meta=result.meta
        )



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
        - archived: Whether the project is archived
        - archived_by: The user who archived the project
        - archived_date: The date when the project was archived
        - assignee_type: The default assignee when creating issues for this project
        - avatar_urls: The URLs of the project's avatars
        - components: List of the components contained in the project
        - deleted: Whether the project is marked as deleted
        - deleted_by: The user who marked the project as deleted
        - deleted_date: The date when the project was marked as deleted
        - description: A brief description of the project
        - email: An email address associated with the project
        - entity_id: The unique identifier of the project entity
        - expand: Expand options that include additional project details in the response
        - favourite: Whether the project is selected as a favorite
        - id: The ID of the project
        - insight: Insights about the project
        - is_private: Whether the project is private
        - issue_type_hierarchy: The issue type hierarchy for the project
        - issue_types: List of the issue types available in the project
        - key: The key of the project
        - lead: The username of the project lead
        - name: The name of the project
        - permissions: User permissions on the project
        - project_category: The category the project belongs to
        - project_type_key: The project type of the project
        - properties: Map of project properties
        - retention_till_date: The date when the project is deleted permanently
        - roles: The name and self URL for each role defined in the project
        - self: The URL of the project details
        - simplified: Whether the project is simplified
        - style: The type of the project
        - url: A link to information about this project
        - uuid: Unique ID for next-gen projects
        - versions: The versions defined in the project

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProjectsSearchResult with hits (list of AirbyteSearchHit[ProjectsSearchData]) and pagination info

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
        return ProjectsSearchResult(
            hits=[
                AirbyteSearchHit[ProjectsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ProjectsSearchData(**hit.get("data", {}))
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
    ) -> UsersListResult:
        """
        Returns a paginated list of users

        Args:
            start_at: The index of the first item to return in a page of results (page offset)
            max_results: The maximum number of items to return per page (max 1000)
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "startAt": start_at,
            "maxResults": max_results,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data
        )



    async def api_search(
        self,
        query: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        account_id: str | None = None,
        property: str | None = None,
        **kwargs
    ) -> UsersApiSearchResult:
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
            UsersApiSearchResult
        """
        params = {k: v for k, v in {
            "query": query,
            "startAt": start_at,
            "maxResults": max_results,
            "accountId": account_id,
            "property": property,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "api_search", params)
        # Cast generic envelope to concrete typed result
        return UsersApiSearchResult(
            data=result.data
        )



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
        - account_id: The account ID of the user, uniquely identifying the user across all Atlassian products
        - account_type: The user account type (atlassian, app, or customer)
        - active: Indicates whether the user is active
        - application_roles: The application roles assigned to the user
        - avatar_urls: The avatars of the user
        - display_name: The display name of the user
        - email_address: The email address of the user
        - expand: Options to include additional user details in the response
        - groups: The groups to which the user belongs
        - key: Deprecated property
        - locale: The locale of the user
        - name: Deprecated property
        - self: The URL of the user
        - time_zone: The time zone specified in the user's profile

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
    ) -> IssueFieldsListResult:
        """
        Returns a list of all custom and system fields

        Returns:
            IssueFieldsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return IssueFieldsListResult(
            data=result.data
        )



    async def api_search(
        self,
        start_at: int | None = None,
        max_results: int | None = None,
        type: list[str] | None = None,
        id: list[str] | None = None,
        query: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        **kwargs
    ) -> IssueFieldsApiSearchResult:
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
            IssueFieldsApiSearchResult
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

        result = await self._connector.execute("issue_fields", "api_search", params)
        # Cast generic envelope to concrete typed result
        return IssueFieldsApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: IssueFieldsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IssueFieldsSearchResult:
        """
        Search issue_fields records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IssueFieldsSearchFilter):
        - clause_names: The names that can be used to reference the field in an advanced search
        - custom: Whether the field is a custom field
        - id: The ID of the field
        - key: The key of the field
        - name: The name of the field
        - navigable: Whether the field can be used as a column on the issue navigator
        - orderable: Whether the content of the field can be used to order lists
        - schema_: The data schema for the field
        - scope: The scope of the field
        - searchable: Whether the content of the field can be searched
        - untranslated_name: The untranslated name of the field

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IssueFieldsSearchResult with hits (list of AirbyteSearchHit[IssueFieldsSearchData]) and pagination info

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

        result = await self._connector.execute("issue_fields", "search", params)

        # Parse response into typed result
        return IssueFieldsSearchResult(
            hits=[
                AirbyteSearchHit[IssueFieldsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=IssueFieldsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



    async def create(
        self,
        body: IssueCommentsCreateParamsBody,
        issue_id_or_key: str,
        visibility: IssueCommentsCreateParamsVisibility | None = None,
        properties: list[dict[str, Any]] | None = None,
        expand: str | None = None,
        **kwargs
    ) -> IssueComment:
        """
        Adds a comment to an issue

        Args:
            body: Comment content in Atlassian Document Format (ADF)
            visibility: Restrict comment visibility to a group or role
            properties: Custom properties for the comment
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            expand: Expand options for the returned comment
            **kwargs: Additional parameters

        Returns:
            IssueComment
        """
        params = {k: v for k, v in {
            "body": body,
            "visibility": visibility,
            "properties": properties,
            "issueIdOrKey": issue_id_or_key,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_comments", "create", params)
        return result



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



    async def update(
        self,
        body: IssueCommentsUpdateParamsBody,
        issue_id_or_key: str,
        comment_id: str,
        visibility: IssueCommentsUpdateParamsVisibility | None = None,
        notify_users: bool | None = None,
        expand: str | None = None,
        **kwargs
    ) -> IssueComment:
        """
        Updates a comment on an issue

        Args:
            body: Updated comment content in Atlassian Document Format (ADF)
            visibility: Restrict comment visibility to a group or role
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            comment_id: The comment ID
            notify_users: Whether a notification email about the comment update is sent. Default is true.
            expand: Expand options for the returned comment
            **kwargs: Additional parameters

        Returns:
            IssueComment
        """
        params = {k: v for k, v in {
            "body": body,
            "visibility": visibility,
            "issueIdOrKey": issue_id_or_key,
            "commentId": comment_id,
            "notifyUsers": notify_users,
            "expand": expand,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_comments", "update", params)
        return result



    async def delete(
        self,
        issue_id_or_key: str,
        comment_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Deletes a comment from an issue

        Args:
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            comment_id: The comment ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "issueIdOrKey": issue_id_or_key,
            "commentId": comment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_comments", "delete", params)
        return result



    async def search(
        self,
        query: IssueCommentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IssueCommentsSearchResult:
        """
        Search issue_comments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IssueCommentsSearchFilter):
        - author: The ID of the user who created the comment
        - body: The comment text in Atlassian Document Format
        - created: The date and time at which the comment was created
        - id: The ID of the comment
        - issue_id: Id of the related issue
        - jsd_public: Whether the comment is visible in Jira Service Desk
        - properties: A list of comment properties
        - rendered_body: The rendered version of the comment
        - self: The URL of the comment
        - update_author: The ID of the user who updated the comment last
        - updated: The date and time at which the comment was updated last
        - visibility: The group or role to which this item is visible

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IssueCommentsSearchResult with hits (list of AirbyteSearchHit[IssueCommentsSearchData]) and pagination info

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

        result = await self._connector.execute("issue_comments", "search", params)

        # Parse response into typed result
        return IssueCommentsSearchResult(
            hits=[
                AirbyteSearchHit[IssueCommentsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=IssueCommentsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



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



    async def search(
        self,
        query: IssueWorklogsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IssueWorklogsSearchResult:
        """
        Search issue_worklogs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IssueWorklogsSearchFilter):
        - author: Details of the user who created the worklog
        - comment: A comment about the worklog in Atlassian Document Format
        - created: The datetime on which the worklog was created
        - id: The ID of the worklog record
        - issue_id: The ID of the issue this worklog is for
        - properties: Details of properties for the worklog
        - self: The URL of the worklog item
        - started: The datetime on which the worklog effort was started
        - time_spent: The time spent working on the issue as days, hours, or minutes
        - time_spent_seconds: The time in seconds spent working on the issue
        - update_author: Details of the user who last updated the worklog
        - updated: The datetime on which the worklog was last updated
        - visibility: Details about any restrictions in the visibility of the worklog

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IssueWorklogsSearchResult with hits (list of AirbyteSearchHit[IssueWorklogsSearchData]) and pagination info

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

        result = await self._connector.execute("issue_worklogs", "search", params)

        # Parse response into typed result
        return IssueWorklogsSearchResult(
            hits=[
                AirbyteSearchHit[IssueWorklogsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=IssueWorklogsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class IssuesAssigneeQuery:
    """
    Query class for IssuesAssignee entity operations.
    """

    def __init__(self, connector: JiraConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def update(
        self,
        issue_id_or_key: str,
        account_id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Assigns an issue to a user. Use accountId to specify the assignee. Use null to unassign the issue. Use "-1" to set to automatic (project default).

        Args:
            account_id: The account ID of the user to assign the issue to. Use null to unassign the issue. Use "-1" to set to automatic (project default assignee).
            issue_id_or_key: The issue ID or key (e.g., "PROJ-123" or "10000")
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "accountId": account_id,
            "issueIdOrKey": issue_id_or_key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues_assignee", "update", params)
        return result


