"""
Harvest connector.
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

from .connector_model import HarvestConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    ClientsGetParams,
    ClientsListParams,
    CompanyGetParams,
    ContactsGetParams,
    ContactsListParams,
    EstimateItemCategoriesGetParams,
    EstimateItemCategoriesListParams,
    EstimatesGetParams,
    EstimatesListParams,
    ExpenseCategoriesGetParams,
    ExpenseCategoriesListParams,
    ExpensesGetParams,
    ExpensesListParams,
    InvoiceItemCategoriesGetParams,
    InvoiceItemCategoriesListParams,
    InvoicesGetParams,
    InvoicesListParams,
    ProjectsGetParams,
    ProjectsListParams,
    RolesGetParams,
    RolesListParams,
    TaskAssignmentsListParams,
    TasksGetParams,
    TasksListParams,
    TimeEntriesGetParams,
    TimeEntriesListParams,
    TimeProjectsListParams,
    TimeTasksListParams,
    UserAssignmentsListParams,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    ClientsSearchFilter,
    ClientsSearchQuery,
    CompanySearchFilter,
    CompanySearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    EstimateItemCategoriesSearchFilter,
    EstimateItemCategoriesSearchQuery,
    EstimatesSearchFilter,
    EstimatesSearchQuery,
    ExpenseCategoriesSearchFilter,
    ExpenseCategoriesSearchQuery,
    ExpensesSearchFilter,
    ExpensesSearchQuery,
    InvoiceItemCategoriesSearchFilter,
    InvoiceItemCategoriesSearchQuery,
    InvoicesSearchFilter,
    InvoicesSearchQuery,
    ProjectsSearchFilter,
    ProjectsSearchQuery,
    RolesSearchFilter,
    RolesSearchQuery,
    TaskAssignmentsSearchFilter,
    TaskAssignmentsSearchQuery,
    TasksSearchFilter,
    TasksSearchQuery,
    TimeEntriesSearchFilter,
    TimeEntriesSearchQuery,
    TimeProjectsSearchFilter,
    TimeProjectsSearchQuery,
    TimeTasksSearchFilter,
    TimeTasksSearchQuery,
    UserAssignmentsSearchFilter,
    UserAssignmentsSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
)
from .models import HarvestOauth20AuthConfig, HarvestPersonalAccessTokenAuthConfig
from .models import HarvestAuthConfig
if TYPE_CHECKING:
    from .models import HarvestReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    HarvestCheckResult,
    HarvestExecuteResult,
    HarvestExecuteResultWithMeta,
    UsersListResult,
    ClientsListResult,
    ContactsListResult,
    ProjectsListResult,
    TasksListResult,
    TimeEntriesListResult,
    InvoicesListResult,
    InvoiceItemCategoriesListResult,
    EstimatesListResult,
    EstimateItemCategoriesListResult,
    ExpensesListResult,
    ExpenseCategoriesListResult,
    RolesListResult,
    UserAssignmentsListResult,
    TaskAssignmentsListResult,
    TimeProjectsListResult,
    TimeTasksListResult,
    Client,
    Company,
    Contact,
    Estimate,
    EstimateItemCategory,
    Expense,
    ExpenseCategory,
    Invoice,
    InvoiceItemCategory,
    Project,
    Role,
    Task,
    TaskAssignment,
    TimeEntry,
    TimeProject,
    TimeTask,
    User,
    UserAssignment,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ClientsSearchData,
    ClientsSearchResult,
    CompanySearchData,
    CompanySearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    EstimateItemCategoriesSearchData,
    EstimateItemCategoriesSearchResult,
    EstimatesSearchData,
    EstimatesSearchResult,
    ExpenseCategoriesSearchData,
    ExpenseCategoriesSearchResult,
    ExpensesSearchData,
    ExpensesSearchResult,
    InvoiceItemCategoriesSearchData,
    InvoiceItemCategoriesSearchResult,
    InvoicesSearchData,
    InvoicesSearchResult,
    ProjectsSearchData,
    ProjectsSearchResult,
    RolesSearchData,
    RolesSearchResult,
    TaskAssignmentsSearchData,
    TaskAssignmentsSearchResult,
    TasksSearchData,
    TasksSearchResult,
    TimeEntriesSearchData,
    TimeEntriesSearchResult,
    TimeProjectsSearchData,
    TimeProjectsSearchResult,
    TimeTasksSearchData,
    TimeTasksSearchResult,
    UserAssignmentsSearchData,
    UserAssignmentsSearchResult,
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




class HarvestConnector:
    """
    Type-safe Harvest API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "harvest"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("users", "list"): True,
        ("users", "get"): None,
        ("clients", "list"): True,
        ("clients", "get"): None,
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("company", "get"): None,
        ("projects", "list"): True,
        ("projects", "get"): None,
        ("tasks", "list"): True,
        ("tasks", "get"): None,
        ("time_entries", "list"): True,
        ("time_entries", "get"): None,
        ("invoices", "list"): True,
        ("invoices", "get"): None,
        ("invoice_item_categories", "list"): True,
        ("invoice_item_categories", "get"): None,
        ("estimates", "list"): True,
        ("estimates", "get"): None,
        ("estimate_item_categories", "list"): True,
        ("estimate_item_categories", "get"): None,
        ("expenses", "list"): True,
        ("expenses", "get"): None,
        ("expense_categories", "list"): True,
        ("expense_categories", "get"): None,
        ("roles", "list"): True,
        ("roles", "get"): None,
        ("user_assignments", "list"): True,
        ("task_assignments", "list"): True,
        ("time_projects", "list"): True,
        ("time_tasks", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('users', 'list'): {'per_page': 'per_page'},
        ('users', 'get'): {'id': 'id'},
        ('clients', 'list'): {'per_page': 'per_page'},
        ('clients', 'get'): {'id': 'id'},
        ('contacts', 'list'): {'per_page': 'per_page'},
        ('contacts', 'get'): {'id': 'id'},
        ('projects', 'list'): {'per_page': 'per_page'},
        ('projects', 'get'): {'id': 'id'},
        ('tasks', 'list'): {'per_page': 'per_page'},
        ('tasks', 'get'): {'id': 'id'},
        ('time_entries', 'list'): {'per_page': 'per_page'},
        ('time_entries', 'get'): {'id': 'id'},
        ('invoices', 'list'): {'per_page': 'per_page'},
        ('invoices', 'get'): {'id': 'id'},
        ('invoice_item_categories', 'list'): {'per_page': 'per_page'},
        ('invoice_item_categories', 'get'): {'id': 'id'},
        ('estimates', 'list'): {'per_page': 'per_page'},
        ('estimates', 'get'): {'id': 'id'},
        ('estimate_item_categories', 'list'): {'per_page': 'per_page'},
        ('estimate_item_categories', 'get'): {'id': 'id'},
        ('expenses', 'list'): {'per_page': 'per_page'},
        ('expenses', 'get'): {'id': 'id'},
        ('expense_categories', 'list'): {'per_page': 'per_page'},
        ('expense_categories', 'get'): {'id': 'id'},
        ('roles', 'list'): {'per_page': 'per_page'},
        ('roles', 'get'): {'id': 'id'},
        ('user_assignments', 'list'): {'per_page': 'per_page'},
        ('task_assignments', 'list'): {'per_page': 'per_page'},
        ('time_projects', 'list'): {'from_': 'from', 'to': 'to', 'per_page': 'per_page'},
        ('time_tasks', 'list'): {'from_': 'from', 'to': 'to', 'per_page': 'per_page'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (HarvestOauth20AuthConfig, HarvestPersonalAccessTokenAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: HarvestAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new harvest connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., HarvestAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = HarvestConnector(auth_config=HarvestAuthConfig(access_token="...", account_id="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = HarvestConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = HarvestConnector(
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
                connector_definition_id=str(HarvestConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or HarvestAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, HarvestOauth20AuthConfig):
                    auth_scheme = "oauth2"
                if isinstance(auth_config, HarvestPersonalAccessTokenAuthConfig):
                    auth_scheme = "bearer"

            self._executor = LocalExecutor(
                model=HarvestConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.users = UsersQuery(self)
        self.clients = ClientsQuery(self)
        self.contacts = ContactsQuery(self)
        self.company = CompanyQuery(self)
        self.projects = ProjectsQuery(self)
        self.tasks = TasksQuery(self)
        self.time_entries = TimeEntriesQuery(self)
        self.invoices = InvoicesQuery(self)
        self.invoice_item_categories = InvoiceItemCategoriesQuery(self)
        self.estimates = EstimatesQuery(self)
        self.estimate_item_categories = EstimateItemCategoriesQuery(self)
        self.expenses = ExpensesQuery(self)
        self.expense_categories = ExpenseCategoriesQuery(self)
        self.roles = RolesQuery(self)
        self.user_assignments = UserAssignmentsQuery(self)
        self.task_assignments = TaskAssignmentsQuery(self)
        self.time_projects = TimeProjectsQuery(self)
        self.time_tasks = TimeTasksQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["clients"],
        action: Literal["list"],
        params: "ClientsListParams"
    ) -> "ClientsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["clients"],
        action: Literal["get"],
        params: "ClientsGetParams"
    ) -> "Client": ...

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
        action: Literal["get"],
        params: "ContactsGetParams"
    ) -> "Contact": ...

    @overload
    async def execute(
        self,
        entity: Literal["company"],
        action: Literal["get"],
        params: "CompanyGetParams"
    ) -> "Company": ...

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
        entity: Literal["tasks"],
        action: Literal["list"],
        params: "TasksListParams"
    ) -> "TasksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["get"],
        params: "TasksGetParams"
    ) -> "Task": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_entries"],
        action: Literal["list"],
        params: "TimeEntriesListParams"
    ) -> "TimeEntriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_entries"],
        action: Literal["get"],
        params: "TimeEntriesGetParams"
    ) -> "TimeEntry": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoices"],
        action: Literal["list"],
        params: "InvoicesListParams"
    ) -> "InvoicesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoices"],
        action: Literal["get"],
        params: "InvoicesGetParams"
    ) -> "Invoice": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoice_item_categories"],
        action: Literal["list"],
        params: "InvoiceItemCategoriesListParams"
    ) -> "InvoiceItemCategoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["invoice_item_categories"],
        action: Literal["get"],
        params: "InvoiceItemCategoriesGetParams"
    ) -> "InvoiceItemCategory": ...

    @overload
    async def execute(
        self,
        entity: Literal["estimates"],
        action: Literal["list"],
        params: "EstimatesListParams"
    ) -> "EstimatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["estimates"],
        action: Literal["get"],
        params: "EstimatesGetParams"
    ) -> "Estimate": ...

    @overload
    async def execute(
        self,
        entity: Literal["estimate_item_categories"],
        action: Literal["list"],
        params: "EstimateItemCategoriesListParams"
    ) -> "EstimateItemCategoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["estimate_item_categories"],
        action: Literal["get"],
        params: "EstimateItemCategoriesGetParams"
    ) -> "EstimateItemCategory": ...

    @overload
    async def execute(
        self,
        entity: Literal["expenses"],
        action: Literal["list"],
        params: "ExpensesListParams"
    ) -> "ExpensesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["expenses"],
        action: Literal["get"],
        params: "ExpensesGetParams"
    ) -> "Expense": ...

    @overload
    async def execute(
        self,
        entity: Literal["expense_categories"],
        action: Literal["list"],
        params: "ExpenseCategoriesListParams"
    ) -> "ExpenseCategoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["expense_categories"],
        action: Literal["get"],
        params: "ExpenseCategoriesGetParams"
    ) -> "ExpenseCategory": ...

    @overload
    async def execute(
        self,
        entity: Literal["roles"],
        action: Literal["list"],
        params: "RolesListParams"
    ) -> "RolesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["roles"],
        action: Literal["get"],
        params: "RolesGetParams"
    ) -> "Role": ...

    @overload
    async def execute(
        self,
        entity: Literal["user_assignments"],
        action: Literal["list"],
        params: "UserAssignmentsListParams"
    ) -> "UserAssignmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["task_assignments"],
        action: Literal["list"],
        params: "TaskAssignmentsListParams"
    ) -> "TaskAssignmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_projects"],
        action: Literal["list"],
        params: "TimeProjectsListParams"
    ) -> "TimeProjectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["time_tasks"],
        action: Literal["list"],
        params: "TimeTasksListParams"
    ) -> "TimeTasksListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> HarvestExecuteResult[Any] | HarvestExecuteResultWithMeta[Any, Any] | Any: ...

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
                return HarvestExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return HarvestExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> HarvestCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            HarvestCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return HarvestCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return HarvestCheckResult(
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
            @HarvestConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @HarvestConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    HarvestConnectorModel,
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
        return describe_entities(HarvestConnectorModel)

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
            (e for e in HarvestConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in HarvestConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await HarvestConnector.create(...)
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
        replication_config: "HarvestReplicationConfig" | None = None,
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
            consent_url = await HarvestConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Harvest Source",
                replication_config=HarvestReplicationConfig(replication_start_date="..."),
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
                definition_id=str(HarvestConnectorModel.id),
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
        auth_config: "HarvestAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "HarvestReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "HarvestConnector":
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
            A HarvestConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await HarvestConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=HarvestAuthConfig(access_token="...", account_id="..."),
            )

            # With replication config (required for this connector):
            connector = await HarvestConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=HarvestAuthConfig(access_token="...", account_id="..."),
                replication_config=HarvestReplicationConfig(replication_start_date="..."),
            )

            # With server-side OAuth:
            connector = await HarvestConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=HarvestReplicationConfig(replication_start_date="..."),
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
                connector_definition_id=str(HarvestConnectorModel.id),
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




class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a paginated list of users in the Harvest account

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
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
        - avatar_url: Avatar URL
        - cost_rate: Cost rate
        - created_at: When created
        - default_hourly_rate: Default hourly rate
        - email: Email address
        - first_name: First name
        - id: Unique identifier
        - is_active: Whether active
        - is_contractor: Whether contractor
        - last_name: Last name
        - roles: Assigned roles
        - telephone: Phone number
        - timezone: Timezone
        - updated_at: When last updated
        - weekly_capacity: Weekly capacity in seconds

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

class ClientsQuery:
    """
    Query class for Clients entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> ClientsListResult:
        """
        Returns a paginated list of clients

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            ClientsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("clients", "list", params)
        # Cast generic envelope to concrete typed result
        return ClientsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Client:
        """
        Get a single client by ID

        Args:
            id: Client ID
            **kwargs: Additional parameters

        Returns:
            Client
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("clients", "get", params)
        return result



    async def search(
        self,
        query: ClientsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ClientsSearchResult:
        """
        Search clients records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ClientsSearchFilter):
        - address: The client's postal address
        - created_at: When the client record was created
        - currency: The currency used by the client
        - id: Unique identifier for the client
        - is_active: Whether the client is active
        - name: The client's name
        - updated_at: When the client record was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ClientsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("clients", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ClientsSearchResult(
            data=[
                ClientsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a paginated list of contacts

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID

        Args:
            id: Contact ID
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



    async def search(
        self,
        query: ContactsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ContactsSearchResult:
        """
        Search contacts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ContactsSearchFilter):
        - client: Client associated with the contact
        - created_at: When created
        - email: Email address
        - first_name: First name
        - id: Unique identifier
        - last_name: Last name
        - title: Job title
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ContactsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("contacts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ContactsSearchResult(
            data=[
                ContactsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CompanyQuery:
    """
    Query class for Company entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> Company:
        """
        Returns the company information for the authenticated account

        Returns:
            Company
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("company", "get", params)
        return result



    async def search(
        self,
        query: CompanySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CompanySearchResult:
        """
        Search company records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CompanySearchFilter):
        - base_uri: The base URI
        - currency: Currency used by the company
        - full_domain: The full domain name
        - is_active: Whether the company is active
        - name: The name of the company
        - plan_type: The plan type
        - weekly_capacity: Weekly capacity in seconds

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CompanySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("company", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CompanySearchResult(
            data=[
                CompanySearchData(**row)
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

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> ProjectsListResult:
        """
        Returns a paginated list of projects

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            ProjectsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
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
        id: str | None = None,
        **kwargs
    ) -> Project:
        """
        Get a single project by ID

        Args:
            id: Project ID
            **kwargs: Additional parameters

        Returns:
            Project
        """
        params = {k: v for k, v in {
            "id": id,
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
        - budget: Budget amount
        - client: Client details
        - code: Project code
        - created_at: When created
        - hourly_rate: Hourly rate
        - id: Unique identifier
        - is_active: Whether active
        - is_billable: Whether billable
        - name: Project name
        - starts_on: Start date
        - updated_at: When last updated

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

class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> TasksListResult:
        """
        Returns a paginated list of tasks

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TasksListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Task:
        """
        Get a single task by ID

        Args:
            id: Task ID
            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def search(
        self,
        query: TasksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TasksSearchResult:
        """
        Search tasks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TasksSearchFilter):
        - billable_by_default: Whether billable by default
        - created_at: When created
        - default_hourly_rate: Default hourly rate
        - id: Unique identifier
        - is_active: Whether active
        - name: Task name
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TasksSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tasks", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TasksSearchResult(
            data=[
                TasksSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TimeEntriesQuery:
    """
    Query class for TimeEntries entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> TimeEntriesListResult:
        """
        Returns a paginated list of time entries

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            TimeEntriesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_entries", "list", params)
        # Cast generic envelope to concrete typed result
        return TimeEntriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> TimeEntry:
        """
        Get a single time entry by ID

        Args:
            id: Time entry ID
            **kwargs: Additional parameters

        Returns:
            TimeEntry
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_entries", "get", params)
        return result



    async def search(
        self,
        query: TimeEntriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TimeEntriesSearchResult:
        """
        Search time_entries records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TimeEntriesSearchFilter):
        - billable: Whether billable
        - client: Associated client
        - created_at: When created
        - hours: Hours logged
        - id: Unique identifier
        - is_billed: Whether billed
        - notes: Notes
        - project: Associated project
        - spent_date: Date time was spent
        - task: Associated task
        - updated_at: When last updated
        - user: Associated user

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TimeEntriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("time_entries", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TimeEntriesSearchResult(
            data=[
                TimeEntriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class InvoicesQuery:
    """
    Query class for Invoices entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> InvoicesListResult:
        """
        Returns a paginated list of invoices

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            InvoicesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "list", params)
        # Cast generic envelope to concrete typed result
        return InvoicesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Invoice:
        """
        Get a single invoice by ID

        Args:
            id: Invoice ID
            **kwargs: Additional parameters

        Returns:
            Invoice
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoices", "get", params)
        return result



    async def search(
        self,
        query: InvoicesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InvoicesSearchResult:
        """
        Search invoices records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InvoicesSearchFilter):
        - amount: Total amount
        - client: Client details
        - created_at: When created
        - currency: Currency
        - due_amount: Amount due
        - due_date: Due date
        - id: Unique identifier
        - issue_date: Issue date
        - number: Invoice number
        - state: Current state
        - subject: Subject
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InvoicesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("invoices", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InvoicesSearchResult(
            data=[
                InvoicesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class InvoiceItemCategoriesQuery:
    """
    Query class for InvoiceItemCategories entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> InvoiceItemCategoriesListResult:
        """
        Returns a paginated list of invoice item categories

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            InvoiceItemCategoriesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoice_item_categories", "list", params)
        # Cast generic envelope to concrete typed result
        return InvoiceItemCategoriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> InvoiceItemCategory:
        """
        Get a single invoice item category by ID

        Args:
            id: Invoice item category ID
            **kwargs: Additional parameters

        Returns:
            InvoiceItemCategory
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invoice_item_categories", "get", params)
        return result



    async def search(
        self,
        query: InvoiceItemCategoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InvoiceItemCategoriesSearchResult:
        """
        Search invoice_item_categories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InvoiceItemCategoriesSearchFilter):
        - created_at: When created
        - id: Unique identifier
        - name: Category name
        - updated_at: When last updated
        - use_as_expense: Whether used as expense type
        - use_as_service: Whether used as service type

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InvoiceItemCategoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("invoice_item_categories", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InvoiceItemCategoriesSearchResult(
            data=[
                InvoiceItemCategoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class EstimatesQuery:
    """
    Query class for Estimates entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> EstimatesListResult:
        """
        Returns a paginated list of estimates

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            EstimatesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("estimates", "list", params)
        # Cast generic envelope to concrete typed result
        return EstimatesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Estimate:
        """
        Get a single estimate by ID

        Args:
            id: Estimate ID
            **kwargs: Additional parameters

        Returns:
            Estimate
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("estimates", "get", params)
        return result



    async def search(
        self,
        query: EstimatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EstimatesSearchResult:
        """
        Search estimates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EstimatesSearchFilter):
        - amount: Total amount
        - client: Client details
        - created_at: When created
        - currency: Currency
        - id: Unique identifier
        - issue_date: Issue date
        - number: Estimate number
        - state: Current state
        - subject: Subject
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EstimatesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("estimates", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EstimatesSearchResult(
            data=[
                EstimatesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class EstimateItemCategoriesQuery:
    """
    Query class for EstimateItemCategories entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> EstimateItemCategoriesListResult:
        """
        Returns a paginated list of estimate item categories

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            EstimateItemCategoriesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("estimate_item_categories", "list", params)
        # Cast generic envelope to concrete typed result
        return EstimateItemCategoriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> EstimateItemCategory:
        """
        Get a single estimate item category by ID

        Args:
            id: Estimate item category ID
            **kwargs: Additional parameters

        Returns:
            EstimateItemCategory
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("estimate_item_categories", "get", params)
        return result



    async def search(
        self,
        query: EstimateItemCategoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EstimateItemCategoriesSearchResult:
        """
        Search estimate_item_categories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EstimateItemCategoriesSearchFilter):
        - created_at: When created
        - id: Unique identifier
        - name: Category name
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EstimateItemCategoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("estimate_item_categories", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EstimateItemCategoriesSearchResult(
            data=[
                EstimateItemCategoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ExpensesQuery:
    """
    Query class for Expenses entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> ExpensesListResult:
        """
        Returns a paginated list of expenses

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            ExpensesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("expenses", "list", params)
        # Cast generic envelope to concrete typed result
        return ExpensesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Expense:
        """
        Get a single expense by ID

        Args:
            id: Expense ID
            **kwargs: Additional parameters

        Returns:
            Expense
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("expenses", "get", params)
        return result



    async def search(
        self,
        query: ExpensesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ExpensesSearchResult:
        """
        Search expenses records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ExpensesSearchFilter):
        - billable: Whether billable
        - client: Associated client
        - created_at: When created
        - expense_category: Expense category
        - id: Unique identifier
        - is_billed: Whether billed
        - notes: Notes
        - project: Associated project
        - spent_date: Date spent
        - total_cost: Total cost
        - updated_at: When last updated
        - user: Associated user

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ExpensesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("expenses", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ExpensesSearchResult(
            data=[
                ExpensesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ExpenseCategoriesQuery:
    """
    Query class for ExpenseCategories entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> ExpenseCategoriesListResult:
        """
        Returns a paginated list of expense categories

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            ExpenseCategoriesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("expense_categories", "list", params)
        # Cast generic envelope to concrete typed result
        return ExpenseCategoriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ExpenseCategory:
        """
        Get a single expense category by ID

        Args:
            id: Expense category ID
            **kwargs: Additional parameters

        Returns:
            ExpenseCategory
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("expense_categories", "get", params)
        return result



    async def search(
        self,
        query: ExpenseCategoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ExpenseCategoriesSearchResult:
        """
        Search expense_categories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ExpenseCategoriesSearchFilter):
        - created_at: When created
        - id: Unique identifier
        - is_active: Whether active
        - name: Category name
        - unit_name: Unit name
        - unit_price: Unit price
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ExpenseCategoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("expense_categories", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ExpenseCategoriesSearchResult(
            data=[
                ExpenseCategoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class RolesQuery:
    """
    Query class for Roles entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> RolesListResult:
        """
        Returns a paginated list of roles

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            RolesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("roles", "list", params)
        # Cast generic envelope to concrete typed result
        return RolesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Role:
        """
        Get a single role by ID

        Args:
            id: Role ID
            **kwargs: Additional parameters

        Returns:
            Role
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("roles", "get", params)
        return result



    async def search(
        self,
        query: RolesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> RolesSearchResult:
        """
        Search roles records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (RolesSearchFilter):
        - created_at: When created
        - id: Unique identifier
        - name: Role name
        - updated_at: When last updated
        - user_ids: User IDs with this role

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            RolesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("roles", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return RolesSearchResult(
            data=[
                RolesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class UserAssignmentsQuery:
    """
    Query class for UserAssignments entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> UserAssignmentsListResult:
        """
        Returns a paginated list of user assignments across all projects

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            UserAssignmentsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("user_assignments", "list", params)
        # Cast generic envelope to concrete typed result
        return UserAssignmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: UserAssignmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> UserAssignmentsSearchResult:
        """
        Search user_assignments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (UserAssignmentsSearchFilter):
        - budget: Budget
        - created_at: When created
        - hourly_rate: Hourly rate
        - id: Unique identifier
        - is_active: Whether active
        - is_project_manager: Whether project manager
        - project: Associated project
        - updated_at: When last updated
        - user: Associated user

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UserAssignmentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("user_assignments", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return UserAssignmentsSearchResult(
            data=[
                UserAssignmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TaskAssignmentsQuery:
    """
    Query class for TaskAssignments entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        **kwargs
    ) -> TaskAssignmentsListResult:
        """
        Returns a paginated list of task assignments across all projects

        Args:
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            TaskAssignmentsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("task_assignments", "list", params)
        # Cast generic envelope to concrete typed result
        return TaskAssignmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: TaskAssignmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TaskAssignmentsSearchResult:
        """
        Search task_assignments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TaskAssignmentsSearchFilter):
        - billable: Whether billable
        - created_at: When created
        - hourly_rate: Hourly rate
        - id: Unique identifier
        - is_active: Whether active
        - project: Associated project
        - task: Associated task
        - updated_at: When last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TaskAssignmentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("task_assignments", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TaskAssignmentsSearchResult(
            data=[
                TaskAssignmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TimeProjectsQuery:
    """
    Query class for TimeProjects entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        from_: str,
        to: str,
        per_page: int | None = None,
        **kwargs
    ) -> TimeProjectsListResult:
        """
        Returns time report data grouped by project for a given date range

        Args:
            from_: Start date for the report in YYYYMMDD format
            to: End date for the report in YYYYMMDD format
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            TimeProjectsListResult
        """
        params = {k: v for k, v in {
            "from": from_,
            "to": to,
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_projects", "list", params)
        # Cast generic envelope to concrete typed result
        return TimeProjectsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: TimeProjectsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TimeProjectsSearchResult:
        """
        Search time_projects records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TimeProjectsSearchFilter):
        - billable_amount: Total billable amount
        - billable_hours: Number of billable hours
        - client_id: Client identifier
        - client_name: Client name
        - currency: Currency code
        - project_id: Project identifier
        - project_name: Project name
        - total_hours: Total hours spent

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TimeProjectsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("time_projects", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TimeProjectsSearchResult(
            data=[
                TimeProjectsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TimeTasksQuery:
    """
    Query class for TimeTasks entity operations.
    """

    def __init__(self, connector: HarvestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        from_: str,
        to: str,
        per_page: int | None = None,
        **kwargs
    ) -> TimeTasksListResult:
        """
        Returns time report data grouped by task for a given date range

        Args:
            from_: Start date for the report in YYYYMMDD format
            to: End date for the report in YYYYMMDD format
            per_page: Number of records per page (max 2000)
            **kwargs: Additional parameters

        Returns:
            TimeTasksListResult
        """
        params = {k: v for k, v in {
            "from": from_,
            "to": to,
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("time_tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TimeTasksListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: TimeTasksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TimeTasksSearchResult:
        """
        Search time_tasks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TimeTasksSearchFilter):
        - billable_amount: Total billable amount
        - billable_hours: Number of billable hours
        - currency: Currency code
        - task_id: Task identifier
        - task_name: Task name
        - total_hours: Total hours spent

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TimeTasksSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("time_tasks", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TimeTasksSearchResult(
            data=[
                TimeTasksSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
