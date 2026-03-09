"""
Pylon connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import PylonConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AccountsCreateParams,
    AccountsGetParams,
    AccountsListParams,
    AccountsUpdateParams,
    ArticlesCreateParams,
    ArticlesUpdateParams,
    CollectionsCreateParams,
    ContactsCreateParams,
    ContactsGetParams,
    ContactsListParams,
    ContactsUpdateParams,
    CustomFieldsGetParams,
    CustomFieldsListParams,
    IssueNotesCreateParams,
    IssueThreadsCreateParams,
    IssuesCreateParams,
    IssuesGetParams,
    IssuesListParams,
    IssuesUpdateParams,
    MeGetParams,
    MessagesListParams,
    MilestonesCreateParams,
    MilestonesUpdateParams,
    ProjectsCreateParams,
    ProjectsUpdateParams,
    TagsCreateParams,
    TagsGetParams,
    TagsListParams,
    TagsUpdateParams,
    TasksCreateParams,
    TasksUpdateParams,
    TeamsCreateParams,
    TeamsGetParams,
    TeamsListParams,
    TeamsUpdateParams,
    TicketFormsListParams,
    UserRolesListParams,
    UsersGetParams,
    UsersListParams,
)
from .models import PylonAuthConfig

# Import response models and envelope models at runtime
from .models import (
    PylonCheckResult,
    PylonExecuteResult,
    PylonExecuteResultWithMeta,
    IssuesListResult,
    MessagesListResult,
    AccountsListResult,
    ContactsListResult,
    TeamsListResult,
    TagsListResult,
    UsersListResult,
    CustomFieldsListResult,
    TicketFormsListResult,
    UserRolesListResult,
    Account,
    AccountResponse,
    ArticleResponse,
    CollectionResponse,
    Contact,
    ContactResponse,
    CustomField,
    Issue,
    IssueNoteResponse,
    IssueResponse,
    IssueThreadResponse,
    Message,
    MilestoneResponse,
    ProjectResponse,
    Tag,
    TagResponse,
    TaskResponse,
    Team,
    TeamResponse,
    TicketForm,
    User,
    UserRole,
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




class PylonConnector:
    """
    Type-safe Pylon API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "pylon"
    connector_version = "0.1.4"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("issues", "list"): True,
        ("issues", "create"): None,
        ("issues", "get"): None,
        ("issues", "update"): None,
        ("messages", "list"): True,
        ("issue_notes", "create"): None,
        ("issue_threads", "create"): None,
        ("accounts", "list"): True,
        ("accounts", "create"): None,
        ("accounts", "get"): None,
        ("accounts", "update"): None,
        ("contacts", "list"): True,
        ("contacts", "create"): None,
        ("contacts", "get"): None,
        ("contacts", "update"): None,
        ("teams", "list"): True,
        ("teams", "create"): None,
        ("teams", "get"): None,
        ("teams", "update"): None,
        ("tags", "list"): True,
        ("tags", "create"): None,
        ("tags", "get"): None,
        ("tags", "update"): None,
        ("users", "list"): True,
        ("users", "get"): None,
        ("custom_fields", "list"): True,
        ("custom_fields", "get"): None,
        ("ticket_forms", "list"): True,
        ("user_roles", "list"): True,
        ("tasks", "create"): None,
        ("tasks", "update"): None,
        ("projects", "create"): None,
        ("projects", "update"): None,
        ("milestones", "create"): None,
        ("milestones", "update"): None,
        ("articles", "create"): None,
        ("articles", "update"): None,
        ("collections", "create"): None,
        ("me", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('issues', 'list'): {'start_time': 'start_time', 'end_time': 'end_time', 'cursor': 'cursor'},
        ('issues', 'create'): {'title': 'title', 'body_html': 'body_html', 'priority': 'priority', 'requester_email': 'requester_email', 'requester_name': 'requester_name', 'account_id': 'account_id', 'assignee_id': 'assignee_id', 'team_id': 'team_id', 'tags': 'tags'},
        ('issues', 'get'): {'id': 'id'},
        ('issues', 'update'): {'state': 'state', 'assignee_id': 'assignee_id', 'team_id': 'team_id', 'account_id': 'account_id', 'tags': 'tags', 'id': 'id'},
        ('messages', 'list'): {'id': 'id', 'cursor': 'cursor'},
        ('issue_notes', 'create'): {'body_html': 'body_html', 'thread_id': 'thread_id', 'message_id': 'message_id', 'id': 'id'},
        ('issue_threads', 'create'): {'name': 'name', 'id': 'id'},
        ('accounts', 'list'): {'cursor': 'cursor'},
        ('accounts', 'create'): {'name': 'name', 'domains': 'domains', 'primary_domain': 'primary_domain', 'owner_id': 'owner_id', 'logo_url': 'logo_url', 'tags': 'tags'},
        ('accounts', 'get'): {'id': 'id'},
        ('accounts', 'update'): {'name': 'name', 'domains': 'domains', 'primary_domain': 'primary_domain', 'owner_id': 'owner_id', 'logo_url': 'logo_url', 'is_disabled': 'is_disabled', 'tags': 'tags', 'id': 'id'},
        ('contacts', 'list'): {'cursor': 'cursor'},
        ('contacts', 'create'): {'name': 'name', 'email': 'email', 'account_id': 'account_id', 'avatar_url': 'avatar_url'},
        ('contacts', 'get'): {'id': 'id'},
        ('contacts', 'update'): {'name': 'name', 'email': 'email', 'account_id': 'account_id', 'id': 'id'},
        ('teams', 'list'): {'cursor': 'cursor'},
        ('teams', 'create'): {'name': 'name'},
        ('teams', 'get'): {'id': 'id'},
        ('teams', 'update'): {'name': 'name', 'id': 'id'},
        ('tags', 'list'): {'cursor': 'cursor'},
        ('tags', 'create'): {'value': 'value', 'object_type': 'object_type', 'hex_color': 'hex_color'},
        ('tags', 'get'): {'id': 'id'},
        ('tags', 'update'): {'value': 'value', 'hex_color': 'hex_color', 'id': 'id'},
        ('users', 'list'): {'cursor': 'cursor'},
        ('users', 'get'): {'id': 'id'},
        ('custom_fields', 'list'): {'object_type': 'object_type', 'cursor': 'cursor'},
        ('custom_fields', 'get'): {'id': 'id'},
        ('ticket_forms', 'list'): {'cursor': 'cursor'},
        ('user_roles', 'list'): {'cursor': 'cursor'},
        ('tasks', 'create'): {'title': 'title', 'body_html': 'body_html', 'status': 'status', 'assignee_id': 'assignee_id', 'project_id': 'project_id', 'milestone_id': 'milestone_id', 'due_date': 'due_date'},
        ('tasks', 'update'): {'title': 'title', 'body_html': 'body_html', 'status': 'status', 'assignee_id': 'assignee_id', 'id': 'id'},
        ('projects', 'create'): {'name': 'name', 'account_id': 'account_id', 'description_html': 'description_html', 'start_date': 'start_date', 'end_date': 'end_date'},
        ('projects', 'update'): {'name': 'name', 'description_html': 'description_html', 'is_archived': 'is_archived', 'id': 'id'},
        ('milestones', 'create'): {'name': 'name', 'project_id': 'project_id', 'due_date': 'due_date'},
        ('milestones', 'update'): {'name': 'name', 'due_date': 'due_date', 'id': 'id'},
        ('articles', 'create'): {'title': 'title', 'body_html': 'body_html', 'author_user_id': 'author_user_id', 'slug': 'slug', 'is_published': 'is_published', 'kb_id': 'kb_id'},
        ('articles', 'update'): {'title': 'title', 'body_html': 'body_html', 'kb_id': 'kb_id', 'article_id': 'article_id'},
        ('collections', 'create'): {'title': 'title', 'description': 'description', 'slug': 'slug', 'kb_id': 'kb_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (PylonAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: PylonAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new pylon connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., PylonAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = PylonConnector(auth_config=PylonAuthConfig(api_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = PylonConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = PylonConnector(
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
                connector_definition_id=str(PylonConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or PylonAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=PylonConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.issues = IssuesQuery(self)
        self.messages = MessagesQuery(self)
        self.issue_notes = IssueNotesQuery(self)
        self.issue_threads = IssueThreadsQuery(self)
        self.accounts = AccountsQuery(self)
        self.contacts = ContactsQuery(self)
        self.teams = TeamsQuery(self)
        self.tags = TagsQuery(self)
        self.users = UsersQuery(self)
        self.custom_fields = CustomFieldsQuery(self)
        self.ticket_forms = TicketFormsQuery(self)
        self.user_roles = UserRolesQuery(self)
        self.tasks = TasksQuery(self)
        self.projects = ProjectsQuery(self)
        self.milestones = MilestonesQuery(self)
        self.articles = ArticlesQuery(self)
        self.collections = CollectionsQuery(self)
        self.me = MeQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        action: Literal["create"],
        params: "IssuesCreateParams"
    ) -> "IssueResponse": ...

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
    ) -> "IssueResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["list"],
        params: "MessagesListParams"
    ) -> "MessagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_notes"],
        action: Literal["create"],
        params: "IssueNotesCreateParams"
    ) -> "IssueNoteResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["issue_threads"],
        action: Literal["create"],
        params: "IssueThreadsCreateParams"
    ) -> "IssueThreadResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["list"],
        params: "AccountsListParams"
    ) -> "AccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["create"],
        params: "AccountsCreateParams"
    ) -> "AccountResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams"
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["update"],
        params: "AccountsUpdateParams"
    ) -> "AccountResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["list"],
        params: "ContactsListParams"
    ) -> "ContactsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["create"],
        params: "ContactsCreateParams"
    ) -> "ContactResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["get"],
        params: "ContactsGetParams"
    ) -> "Contact": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["update"],
        params: "ContactsUpdateParams"
    ) -> "ContactResponse": ...

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
        action: Literal["create"],
        params: "TeamsCreateParams"
    ) -> "TeamResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "Team": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["update"],
        params: "TeamsUpdateParams"
    ) -> "TeamResponse": ...

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
        action: Literal["create"],
        params: "TagsCreateParams"
    ) -> "TagResponse": ...

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
        entity: Literal["tags"],
        action: Literal["update"],
        params: "TagsUpdateParams"
    ) -> "TagResponse": ...

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
        entity: Literal["custom_fields"],
        action: Literal["list"],
        params: "CustomFieldsListParams"
    ) -> "CustomFieldsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_fields"],
        action: Literal["get"],
        params: "CustomFieldsGetParams"
    ) -> "CustomField": ...

    @overload
    async def execute(
        self,
        entity: Literal["ticket_forms"],
        action: Literal["list"],
        params: "TicketFormsListParams"
    ) -> "TicketFormsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["user_roles"],
        action: Literal["list"],
        params: "UserRolesListParams"
    ) -> "UserRolesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["create"],
        params: "TasksCreateParams"
    ) -> "TaskResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["update"],
        params: "TasksUpdateParams"
    ) -> "TaskResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["create"],
        params: "ProjectsCreateParams"
    ) -> "ProjectResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["update"],
        params: "ProjectsUpdateParams"
    ) -> "ProjectResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["milestones"],
        action: Literal["create"],
        params: "MilestonesCreateParams"
    ) -> "MilestoneResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["milestones"],
        action: Literal["update"],
        params: "MilestonesUpdateParams"
    ) -> "MilestoneResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["create"],
        params: "ArticlesCreateParams"
    ) -> "ArticleResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["update"],
        params: "ArticlesUpdateParams"
    ) -> "ArticleResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["collections"],
        action: Literal["create"],
        params: "CollectionsCreateParams"
    ) -> "CollectionResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["me"],
        action: Literal["get"],
        params: "MeGetParams"
    ) -> "User": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update"],
        params: Mapping[str, Any]
    ) -> PylonExecuteResult[Any] | PylonExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "create", "get", "update"],
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
                return PylonExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return PylonExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> PylonCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            PylonCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return PylonCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return PylonCheckResult(
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
            @PylonConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @PylonConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    PylonConnectorModel,
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
        return describe_entities(PylonConnectorModel)

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
            (e for e in PylonConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in PylonConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await PylonConnector.create(...)
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
        auth_config: "PylonAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "PylonConnector":
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
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A PylonConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await PylonConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=PylonAuthConfig(api_token="..."),
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
                connector_definition_id=str(PylonConnectorModel.id),
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




class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_time: str,
        end_time: str,
        cursor: str | None = None,
        **kwargs
    ) -> IssuesListResult:
        """
        Get a list of issues within a time range

        Args:
            start_time: The start time (RFC3339) of the time range to get issues for.
            end_time: The end time (RFC3339) of the time range to get issues for.
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            IssuesListResult
        """
        params = {k: v for k, v in {
            "start_time": start_time,
            "end_time": end_time,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        # Cast generic envelope to concrete typed result
        return IssuesListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        title: str,
        body_html: str,
        priority: str | None = None,
        requester_email: str | None = None,
        requester_name: str | None = None,
        account_id: str | None = None,
        assignee_id: str | None = None,
        team_id: str | None = None,
        tags: list[str] | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Create a new issue

        Args:
            title: The title of the issue
            body_html: The HTML content of the body of the issue
            priority: The priority of the issue (urgent, high, medium, low)
            requester_email: The email of the requester
            requester_name: The full name of the requester
            account_id: The account that this issue belongs to
            assignee_id: The user the issue should be assigned to
            team_id: The ID of the team this issue should be assigned to
            tags: Tags to associate with the issue
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body_html": body_html,
            "priority": priority,
            "requester_email": requester_email,
            "requester_name": requester_name,
            "account_id": account_id,
            "assignee_id": assignee_id,
            "team_id": team_id,
            "tags": tags,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Issue:
        """
        Get a single issue by ID

        Args:
            id: The ID of the issue
            **kwargs: Additional parameters

        Returns:
            Issue
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result



    async def update(
        self,
        state: str | None = None,
        assignee_id: str | None = None,
        team_id: str | None = None,
        account_id: str | None = None,
        tags: list[str] | None = None,
        id: str | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Update an existing issue by ID

        Args:
            state: The state of the issue (open, snoozed, closed)
            assignee_id: The user the issue should be assigned to
            team_id: The ID of the team this issue should be assigned to
            account_id: The account that this issue belongs to
            tags: Tags to associate with the issue
            id: The ID of the issue to update
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "state": state,
            "assignee_id": assignee_id,
            "team_id": team_id,
            "account_id": account_id,
            "tags": tags,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "update", params)
        return result



class MessagesQuery:
    """
    Query class for Messages entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        id: str | None = None,
        cursor: str | None = None,
        **kwargs
    ) -> MessagesListResult:
        """
        Returns all messages on an issue (customer-facing replies and internal notes)

        Args:
            id: The ID of the issue to fetch messages for
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            MessagesListResult
        """
        params = {k: v for k, v in {
            "id": id,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "list", params)
        # Cast generic envelope to concrete typed result
        return MessagesListResult(
            data=result.data,
            meta=result.meta
        )



class IssueNotesQuery:
    """
    Query class for IssueNotes entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        body_html: str,
        thread_id: str | None = None,
        message_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> IssueNoteResponse:
        """
        Create an internal note on an issue

        Args:
            body_html: The HTML content of the note
            thread_id: The ID of the thread to add the note to
            message_id: The ID of the message to add the note to
            id: The ID of the issue to add a note to
            **kwargs: Additional parameters

        Returns:
            IssueNoteResponse
        """
        params = {k: v for k, v in {
            "body_html": body_html,
            "thread_id": thread_id,
            "message_id": message_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_notes", "create", params)
        return result



class IssueThreadsQuery:
    """
    Query class for IssueThreads entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        name: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> IssueThreadResponse:
        """
        Create a new thread on an issue

        Args:
            name: The name of the thread
            id: The ID of the issue to create a thread on
            **kwargs: Additional parameters

        Returns:
            IssueThreadResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issue_threads", "create", params)
        return result



class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> AccountsListResult:
        """
        Get a list of accounts

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        name: str,
        domains: list[str] | None = None,
        primary_domain: str | None = None,
        owner_id: str | None = None,
        logo_url: str | None = None,
        tags: list[str] | None = None,
        **kwargs
    ) -> AccountResponse:
        """
        Create a new account

        Args:
            name: The name of the account
            domains: The domains of the account (e.g. stripe.com)
            primary_domain: Must be in the list of domains. If there are any domains, there must be exactly one primary domain.
            owner_id: The ID of the owner of the account
            logo_url: The logo URL of the account. Must be a square .png, .jpg or .jpeg.
            tags: Tags to associate with the account
            **kwargs: Additional parameters

        Returns:
            AccountResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "domains": domains,
            "primary_domain": primary_domain,
            "owner_id": owner_id,
            "logo_url": logo_url,
            "tags": tags,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Account:
        """
        Get a single account by ID

        Args:
            id: The ID of the account
            **kwargs: Additional parameters

        Returns:
            Account
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def update(
        self,
        name: str | None = None,
        domains: list[str] | None = None,
        primary_domain: str | None = None,
        owner_id: str | None = None,
        logo_url: str | None = None,
        is_disabled: bool | None = None,
        tags: list[str] | None = None,
        id: str | None = None,
        **kwargs
    ) -> AccountResponse:
        """
        Update an existing account by ID

        Args:
            name: The name of the account
            domains: Domains of the account. Must specify one domain as primary.
            primary_domain: Must be in the list of domains. If there are any domains, there must be exactly one primary domain.
            owner_id: The ID of the owner of the account. If empty string is passed in, the owner will be removed.
            logo_url: Logo URL of the account
            is_disabled: Whether the account is disabled
            tags: Tags to associate with the account
            id: The ID of the account to update
            **kwargs: Additional parameters

        Returns:
            AccountResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "domains": domains,
            "primary_domain": primary_domain,
            "owner_id": owner_id,
            "logo_url": logo_url,
            "is_disabled": is_disabled,
            "tags": tags,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "update", params)
        return result



class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Get a list of contacts

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        name: str,
        email: str | None = None,
        account_id: str | None = None,
        avatar_url: str | None = None,
        **kwargs
    ) -> ContactResponse:
        """
        Create a new contact

        Args:
            name: The name of the contact
            email: The email address of the contact
            account_id: The ID of the account to associate this contact with
            avatar_url: The URL of the contact's avatar
            **kwargs: Additional parameters

        Returns:
            ContactResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "email": email,
            "account_id": account_id,
            "avatar_url": avatar_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID

        Args:
            id: The ID of the contact
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



    async def update(
        self,
        name: str | None = None,
        email: str | None = None,
        account_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> ContactResponse:
        """
        Update an existing contact by ID

        Args:
            name: The name of the contact
            email: The email address of the contact
            account_id: The ID of the account to associate this contact with
            id: The ID of the contact to update
            **kwargs: Additional parameters

        Returns:
            ContactResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "email": email,
            "account_id": account_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "update", params)
        return result



class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> TeamsListResult:
        """
        Get a list of teams

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            TeamsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        name: str | None = None,
        **kwargs
    ) -> TeamResponse:
        """
        Create a new team

        Args:
            name: The name of the team
            **kwargs: Additional parameters

        Returns:
            TeamResponse
        """
        params = {k: v for k, v in {
            "name": name,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Team:
        """
        Get a single team by ID

        Args:
            id: The ID of the team
            **kwargs: Additional parameters

        Returns:
            Team
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        return result



    async def update(
        self,
        name: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> TeamResponse:
        """
        Update an existing team by ID

        Args:
            name: The name of the team
            id: The ID of the team to update
            **kwargs: Additional parameters

        Returns:
            TeamResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "update", params)
        return result



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> TagsListResult:
        """
        Get all tags

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            TagsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to concrete typed result
        return TagsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        value: str,
        object_type: str,
        hex_color: str | None = None,
        **kwargs
    ) -> TagResponse:
        """
        Create a new tag

        Args:
            value: The tag value
            object_type: The object type (issue, account, contact)
            hex_color: The hex color code of the tag
            **kwargs: Additional parameters

        Returns:
            TagResponse
        """
        params = {k: v for k, v in {
            "value": value,
            "object_type": object_type,
            "hex_color": hex_color,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "create", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Tag:
        """
        Get a tag by its ID

        Args:
            id: The ID of the tag
            **kwargs: Additional parameters

        Returns:
            Tag
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "get", params)
        return result



    async def update(
        self,
        value: str | None = None,
        hex_color: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> TagResponse:
        """
        Update an existing tag by ID

        Args:
            value: The tag value
            hex_color: The hex color code of the tag
            id: The ID of the tag to update
            **kwargs: Additional parameters

        Returns:
            TagResponse
        """
        params = {k: v for k, v in {
            "value": value,
            "hex_color": hex_color,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "update", params)
        return result



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Get a list of users

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
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
        id: str | None = None,
        **kwargs
    ) -> User:
        """
        Get a single user by ID

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



class CustomFieldsQuery:
    """
    Query class for CustomFields entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        object_type: str,
        cursor: str | None = None,
        **kwargs
    ) -> CustomFieldsListResult:
        """
        Get all custom fields for a given object type

        Args:
            object_type: The object type of the custom fields. Can be "account", "issue", or "contact".
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CustomFieldsListResult
        """
        params = {k: v for k, v in {
            "object_type": object_type,
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomFieldsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> CustomField:
        """
        Get a custom field by its ID

        Args:
            id: The ID of the custom field
            **kwargs: Additional parameters

        Returns:
            CustomField
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_fields", "get", params)
        return result



class TicketFormsQuery:
    """
    Query class for TicketForms entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> TicketFormsListResult:
        """
        Get a list of ticket forms

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            TicketFormsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ticket_forms", "list", params)
        # Cast generic envelope to concrete typed result
        return TicketFormsListResult(
            data=result.data,
            meta=result.meta
        )



class UserRolesQuery:
    """
    Query class for UserRoles entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        **kwargs
    ) -> UserRolesListResult:
        """
        Get a list of all user roles

        Args:
            cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            UserRolesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("user_roles", "list", params)
        # Cast generic envelope to concrete typed result
        return UserRolesListResult(
            data=result.data,
            meta=result.meta
        )



class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        title: str,
        body_html: str | None = None,
        status: str | None = None,
        assignee_id: str | None = None,
        project_id: str | None = None,
        milestone_id: str | None = None,
        due_date: str | None = None,
        **kwargs
    ) -> TaskResponse:
        """
        Create a new task

        Args:
            title: The title of the task
            body_html: The body HTML of the task
            status: The status of the task (not_started, in_progress, completed)
            assignee_id: The assignee ID for the task
            project_id: The project ID for the task
            milestone_id: The milestone ID for the task
            due_date: The due date for the task (RFC3339)
            **kwargs: Additional parameters

        Returns:
            TaskResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body_html": body_html,
            "status": status,
            "assignee_id": assignee_id,
            "project_id": project_id,
            "milestone_id": milestone_id,
            "due_date": due_date,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "create", params)
        return result



    async def update(
        self,
        title: str | None = None,
        body_html: str | None = None,
        status: str | None = None,
        assignee_id: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> TaskResponse:
        """
        Update an existing task by ID

        Args:
            title: The title of the task
            body_html: The body HTML of the task
            status: The status of the task (not_started, in_progress, completed)
            assignee_id: The assignee ID for the task
            id: The ID of the task to update
            **kwargs: Additional parameters

        Returns:
            TaskResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body_html": body_html,
            "status": status,
            "assignee_id": assignee_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "update", params)
        return result



class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        name: str,
        account_id: str,
        description_html: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        **kwargs
    ) -> ProjectResponse:
        """
        Create a new project

        Args:
            name: The name of the project
            account_id: The account ID for the project
            description_html: The HTML description of the project
            start_date: The start date of the project (RFC3339)
            end_date: The end date of the project (RFC3339)
            **kwargs: Additional parameters

        Returns:
            ProjectResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "account_id": account_id,
            "description_html": description_html,
            "start_date": start_date,
            "end_date": end_date,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "create", params)
        return result



    async def update(
        self,
        name: str | None = None,
        description_html: str | None = None,
        is_archived: bool | None = None,
        id: str | None = None,
        **kwargs
    ) -> ProjectResponse:
        """
        Update an existing project by ID

        Args:
            name: The name of the project
            description_html: The HTML description of the project
            is_archived: Whether the project is archived
            id: The ID of the project to update
            **kwargs: Additional parameters

        Returns:
            ProjectResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "description_html": description_html,
            "is_archived": is_archived,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "update", params)
        return result



class MilestonesQuery:
    """
    Query class for Milestones entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        name: str,
        project_id: str,
        due_date: str | None = None,
        **kwargs
    ) -> MilestoneResponse:
        """
        Create a new milestone

        Args:
            name: The name of the milestone
            project_id: The project ID for the milestone
            due_date: The due date of the milestone (RFC3339)
            **kwargs: Additional parameters

        Returns:
            MilestoneResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "project_id": project_id,
            "due_date": due_date,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("milestones", "create", params)
        return result



    async def update(
        self,
        name: str | None = None,
        due_date: str | None = None,
        id: str | None = None,
        **kwargs
    ) -> MilestoneResponse:
        """
        Update an existing milestone by ID

        Args:
            name: The name of the milestone
            due_date: The due date of the milestone (RFC3339)
            id: The ID of the milestone to update
            **kwargs: Additional parameters

        Returns:
            MilestoneResponse
        """
        params = {k: v for k, v in {
            "name": name,
            "due_date": due_date,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("milestones", "update", params)
        return result



class ArticlesQuery:
    """
    Query class for Articles entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        title: str,
        body_html: str,
        author_user_id: str,
        kb_id: str,
        slug: str | None = None,
        is_published: bool | None = None,
        **kwargs
    ) -> ArticleResponse:
        """
        Create a new article in a knowledge base

        Args:
            title: The title of the article
            body_html: The HTML body of the article
            author_user_id: The ID of the user attributed as the author
            slug: The slug of the article
            is_published: Whether the article should be published
            kb_id: The ID of the knowledge base
            **kwargs: Additional parameters

        Returns:
            ArticleResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body_html": body_html,
            "author_user_id": author_user_id,
            "slug": slug,
            "is_published": is_published,
            "kb_id": kb_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "create", params)
        return result



    async def update(
        self,
        kb_id: str,
        article_id: str,
        title: str | None = None,
        body_html: str | None = None,
        **kwargs
    ) -> ArticleResponse:
        """
        Update an existing article in a knowledge base

        Args:
            title: The title of the article
            body_html: The HTML body of the article
            kb_id: The ID of the knowledge base
            article_id: The ID of the article to update
            **kwargs: Additional parameters

        Returns:
            ArticleResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "body_html": body_html,
            "kb_id": kb_id,
            "article_id": article_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "update", params)
        return result



class CollectionsQuery:
    """
    Query class for Collections entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        title: str,
        kb_id: str,
        description: str | None = None,
        slug: str | None = None,
        **kwargs
    ) -> CollectionResponse:
        """
        Create a new collection in a knowledge base

        Args:
            title: The title of the collection
            description: The description of the collection
            slug: The slug of the collection
            kb_id: The ID of the knowledge base
            **kwargs: Additional parameters

        Returns:
            CollectionResponse
        """
        params = {k: v for k, v in {
            "title": title,
            "description": description,
            "slug": slug,
            "kb_id": kb_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collections", "create", params)
        return result



class MeQuery:
    """
    Query class for Me entity operations.
    """

    def __init__(self, connector: PylonConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> User:
        """
        Get the currently authenticated user

        Returns:
            User
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("me", "get", params)
        return result


