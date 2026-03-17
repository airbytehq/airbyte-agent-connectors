"""
Zoho-Crm connector.
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

from .connector_model import ZohoCrmConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AccountsGetParams,
    AccountsListParams,
    CallsGetParams,
    CallsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    ContactsGetParams,
    ContactsListParams,
    DealsGetParams,
    DealsListParams,
    EventsGetParams,
    EventsListParams,
    InvoicesGetParams,
    InvoicesListParams,
    LeadsGetParams,
    LeadsListParams,
    ProductsGetParams,
    ProductsListParams,
    QuotesGetParams,
    QuotesListParams,
    TasksGetParams,
    TasksListParams,
    AirbyteSearchParams,
    LeadsSearchFilter,
    LeadsSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    AccountsSearchFilter,
    AccountsSearchQuery,
    DealsSearchFilter,
    DealsSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    TasksSearchFilter,
    TasksSearchQuery,
    EventsSearchFilter,
    EventsSearchQuery,
    CallsSearchFilter,
    CallsSearchQuery,
    ProductsSearchFilter,
    ProductsSearchQuery,
    QuotesSearchFilter,
    QuotesSearchQuery,
    InvoicesSearchFilter,
    InvoicesSearchQuery,
)
from .models import ZohoCrmAuthConfig

# Import response models and envelope models at runtime
from .models import (
    ZohoCrmCheckResult,
    ZohoCrmExecuteResult,
    ZohoCrmExecuteResultWithMeta,
    LeadsListResult,
    ContactsListResult,
    AccountsListResult,
    DealsListResult,
    CampaignsListResult,
    TasksListResult,
    EventsListResult,
    CallsListResult,
    ProductsListResult,
    QuotesListResult,
    InvoicesListResult,
    Account,
    Call,
    Campaign,
    Contact,
    Deal,
    Event,
    Invoice,
    Lead,
    Product,
    Quote,
    Task,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    LeadsSearchData,
    LeadsSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    DealsSearchData,
    DealsSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    TasksSearchData,
    TasksSearchResult,
    EventsSearchData,
    EventsSearchResult,
    CallsSearchData,
    CallsSearchResult,
    ProductsSearchData,
    ProductsSearchResult,
    QuotesSearchData,
    QuotesSearchResult,
    InvoicesSearchData,
    InvoicesSearchResult,
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




class ZohoCrmConnector:
    """
    Type-safe Zoho-Crm API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zoho-crm"
    connector_version = "1.0.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("leads", "list"): True,
        ("leads", "get"): None,
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("accounts", "list"): True,
        ("accounts", "get"): None,
        ("deals", "list"): True,
        ("deals", "get"): None,
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("tasks", "list"): True,
        ("tasks", "get"): None,
        ("events", "list"): True,
        ("events", "get"): None,
        ("calls", "list"): True,
        ("calls", "get"): None,
        ("products", "list"): True,
        ("products", "get"): None,
        ("quotes", "list"): True,
        ("quotes", "get"): None,
        ("invoices", "list"): True,
        ("invoices", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('leads', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('leads', 'get'): {'id': 'id'},
        ('contacts', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('contacts', 'get'): {'id': 'id'},
        ('accounts', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('accounts', 'get'): {'id': 'id'},
        ('deals', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('deals', 'get'): {'id': 'id'},
        ('campaigns', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('campaigns', 'get'): {'id': 'id'},
        ('tasks', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('tasks', 'get'): {'id': 'id'},
        ('events', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('events', 'get'): {'id': 'id'},
        ('calls', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('calls', 'get'): {'id': 'id'},
        ('products', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('products', 'get'): {'id': 'id'},
        ('quotes', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('quotes', 'get'): {'id': 'id'},
        ('invoices', 'list'): {'page': 'page', 'per_page': 'per_page', 'page_token': 'page_token', 'sort_by': 'sort_by', 'sort_order': 'sort_order'},
        ('invoices', 'get'): {'id': 'id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ZohoCrmAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ZohoCrmAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        dc_region: str | None = None    ):
        """
        Initialize a new zoho-crm connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ZohoCrmAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            dc_region: The Zoho data center region domain suffix: - com (US) - com.au (AU) - eu (EU) - in (IN) - com.cn (CN) - jp (JP)

        Examples:
            # Local mode (direct API calls)
            connector = ZohoCrmConnector(auth_config=ZohoCrmAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ZohoCrmConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = ZohoCrmConnector(
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
                connector_definition_id=str(ZohoCrmConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ZohoCrmAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if dc_region:
                config_values["dc_region"] = dc_region

            self._executor = LocalExecutor(
                model=ZohoCrmConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if dc_region:
                base_url = base_url.replace("{dc_region}", dc_region)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.leads = LeadsQuery(self)
        self.contacts = ContactsQuery(self)
        self.accounts = AccountsQuery(self)
        self.deals = DealsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.tasks = TasksQuery(self)
        self.events = EventsQuery(self)
        self.calls = CallsQuery(self)
        self.products = ProductsQuery(self)
        self.quotes = QuotesQuery(self)
        self.invoices = InvoicesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["list"],
        params: "LeadsListParams"
    ) -> "LeadsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["get"],
        params: "LeadsGetParams"
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

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
        action: Literal["get"],
        params: "AccountsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["list"],
        params: "DealsListParams"
    ) -> "DealsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["deals"],
        action: Literal["get"],
        params: "DealsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams"
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams"
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["list"],
        params: "EventsListParams"
    ) -> "EventsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["get"],
        params: "EventsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["list"],
        params: "CallsListParams"
    ) -> "CallsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["get"],
        params: "CallsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["list"],
        params: "ProductsListParams"
    ) -> "ProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["get"],
        params: "ProductsGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["quotes"],
        action: Literal["list"],
        params: "QuotesListParams"
    ) -> "QuotesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["quotes"],
        action: Literal["get"],
        params: "QuotesGetParams"
    ) -> "dict[str, Any]": ...

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
    ) -> "dict[str, Any]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> ZohoCrmExecuteResult[Any] | ZohoCrmExecuteResultWithMeta[Any, Any] | Any: ...

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
                return ZohoCrmExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ZohoCrmExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ZohoCrmCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ZohoCrmCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ZohoCrmCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ZohoCrmCheckResult(
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
            @ZohoCrmConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @ZohoCrmConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    ZohoCrmConnectorModel,
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
        return describe_entities(ZohoCrmConnectorModel)

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
            (e for e in ZohoCrmConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ZohoCrmConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await ZohoCrmConnector.create(...)
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
        replication_config: dict[str, Any] | None = None,
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
            replication_config: Optional replication settings dict. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await ZohoCrmConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Zoho-Crm Source",
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
                definition_id=str(ZohoCrmConnectorModel.id),
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
        auth_config: "ZohoCrmAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "ZohoCrmConnector":
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
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A ZohoCrmConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await ZohoCrmConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=ZohoCrmAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
            )

            # With server-side OAuth:
            connector = await ZohoCrmConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
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
                connector_definition_id=str(ZohoCrmConnectorModel.id),
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




class LeadsQuery:
    """
    Query class for Leads entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> LeadsListResult:
        """
        Returns a paginated list of leads

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            LeadsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "list", params)
        # Cast generic envelope to concrete typed result
        return LeadsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single lead by ID

        Args:
            id: Lead ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "get", params)
        return result



    async def search(
        self,
        query: LeadsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LeadsSearchResult:
        """
        Search leads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LeadsSearchFilter):
        - id: Unique record identifier
        - first_name: Lead's first name
        - last_name: Lead's last name
        - full_name: Lead's full name
        - email: Lead's email address
        - phone: Lead's phone number
        - mobile: Lead's mobile number
        - company: Company the lead is associated with
        - title: Lead's job title
        - lead_source: Source from which the lead was generated
        - industry: Industry the lead belongs to
        - annual_revenue: Annual revenue of the lead's company
        - no_of_employees: Number of employees in the lead's company
        - rating: Lead rating
        - lead_status: Current status of the lead
        - website: Lead's website URL
        - city: Lead's city
        - state: Lead's state or province
        - country: Lead's country
        - description: Description or notes about the lead
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LeadsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("leads", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LeadsSearchResult(
            data=[
                LeadsSearchData(**row)
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

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a paginated list of contacts

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
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
    ) -> dict[str, Any]:
        """
        Get a single contact by ID

        Args:
            id: Contact ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
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
        - id: Unique record identifier
        - first_name: Contact's first name
        - last_name: Contact's last name
        - full_name: Contact's full name
        - email: Contact's email address
        - phone: Contact's phone number
        - mobile: Contact's mobile number
        - title: Contact's job title
        - department: Department the contact belongs to
        - lead_source: Source from which the contact was generated
        - date_of_birth: Contact's date of birth
        - mailing_city: Mailing address city
        - mailing_state: Mailing address state or province
        - mailing_country: Mailing address country
        - description: Description or notes about the contact
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

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

class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> AccountsListResult:
        """
        Returns a paginated list of accounts

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single account by ID

        Args:
            id: Account ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def search(
        self,
        query: AccountsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AccountsSearchResult:
        """
        Search accounts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AccountsSearchFilter):
        - id: Unique record identifier
        - account_name: Name of the account or company
        - account_number: Account number
        - account_type: Type of account (e.g., Analyst, Competitor, Customer)
        - industry: Industry the account belongs to
        - annual_revenue: Annual revenue of the account
        - employees: Number of employees
        - phone: Account phone number
        - website: Account website URL
        - ownership: Ownership type (e.g., Public, Private)
        - rating: Account rating
        - billing_city: Billing address city
        - billing_state: Billing address state or province
        - billing_country: Billing address country
        - description: Description or notes about the account
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("accounts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AccountsSearchResult(
            data=[
                AccountsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DealsQuery:
    """
    Query class for Deals entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> DealsListResult:
        """
        Returns a paginated list of deals

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            DealsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "list", params)
        # Cast generic envelope to concrete typed result
        return DealsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single deal by ID

        Args:
            id: Deal ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("deals", "get", params)
        return result



    async def search(
        self,
        query: DealsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DealsSearchResult:
        """
        Search deals records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DealsSearchFilter):
        - id: Unique record identifier
        - deal_name: Name of the deal
        - amount: Monetary value of the deal
        - stage: Current stage of the deal in the pipeline
        - probability: Probability of closing the deal (percentage)
        - closing_date: Expected closing date
        - type_: Type of deal (e.g., New Business, Existing Business)
        - next_step: Next step in the deal process
        - lead_source: Source from which the deal originated
        - description: Description or notes about the deal
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DealsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("deals", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DealsSearchResult(
            data=[
                DealsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a paginated list of campaigns

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single campaign by ID

        Args:
            id: Campaign ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def search(
        self,
        query: CampaignsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsSearchResult:
        """
        Search campaigns records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsSearchFilter):
        - id: Unique record identifier
        - campaign_name: Name of the campaign
        - type_: Type of campaign (e.g., Email, Webinar, Conference)
        - status: Current status of the campaign
        - start_date: Campaign start date
        - end_date: Campaign end date
        - expected_revenue: Expected revenue from the campaign
        - budgeted_cost: Budget allocated for the campaign
        - actual_cost: Actual cost incurred
        - num_sent: Number of campaign messages sent
        - expected_response: Expected response count
        - description: Description or notes about the campaign
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaigns", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignsSearchResult(
            data=[
                CampaignsSearchData(**row)
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

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> TasksListResult:
        """
        Returns a paginated list of tasks

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
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
    ) -> dict[str, Any]:
        """
        Get a single task by ID

        Args:
            id: Task ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
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
        - id: Unique record identifier
        - subject: Subject or title of the task
        - due_date: Due date for the task
        - status: Current status (e.g., Not Started, In Progress, Completed)
        - priority: Priority level (e.g., High, Highest, Low, Lowest, Normal)
        - send_notification_email: Whether to send a notification email
        - description: Description or notes about the task
        - created_time: Time the record was created
        - modified_time: Time the record was last modified
        - closed_time: Time the task was closed

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

class EventsQuery:
    """
    Query class for Events entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> EventsListResult:
        """
        Returns a paginated list of events (meetings/calendar events)

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            EventsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "list", params)
        # Cast generic envelope to concrete typed result
        return EventsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single event by ID

        Args:
            id: Event ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "get", params)
        return result



    async def search(
        self,
        query: EventsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EventsSearchResult:
        """
        Search events records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EventsSearchFilter):
        - id: Unique record identifier
        - event_title: Title of the event
        - start_date_time: Event start date and time
        - end_date_time: Event end date and time
        - all_day: Whether this is an all-day event
        - location: Event location
        - description: Description or notes about the event
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EventsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("events", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return EventsSearchResult(
            data=[
                EventsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CallsQuery:
    """
    Query class for Calls entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> CallsListResult:
        """
        Returns a paginated list of calls

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            CallsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "list", params)
        # Cast generic envelope to concrete typed result
        return CallsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single call by ID

        Args:
            id: Call ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "get", params)
        return result



    async def search(
        self,
        query: CallsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CallsSearchResult:
        """
        Search calls records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CallsSearchFilter):
        - id: Unique record identifier
        - subject: Subject of the call
        - call_type: Type of call (Inbound or Outbound)
        - call_start_time: Start time of the call
        - call_duration: Duration of the call as a formatted string
        - call_duration_in_seconds: Duration of the call in seconds
        - call_purpose: Purpose of the call
        - call_result: Result or outcome of the call
        - caller_id: Caller ID number
        - outgoing_call_status: Status of outgoing calls
        - description: Description or notes about the call
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CallsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("calls", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CallsSearchResult(
            data=[
                CallsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductsQuery:
    """
    Query class for Products entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> ProductsListResult:
        """
        Returns a paginated list of products

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            ProductsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single product by ID

        Args:
            id: Product ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "get", params)
        return result



    async def search(
        self,
        query: ProductsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductsSearchResult:
        """
        Search products records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductsSearchFilter):
        - id: Unique record identifier
        - product_name: Name of the product
        - product_code: Product code or SKU
        - product_category: Category of the product
        - product_active: Whether the product is active
        - unit_price: Unit price of the product
        - commission_rate: Commission rate for the product
        - manufacturer: Product manufacturer
        - sales_start_date: Date when sales begin
        - sales_end_date: Date when sales end
        - qty_in_stock: Quantity currently in stock
        - qty_in_demand: Quantity in demand
        - qty_ordered: Quantity on order
        - description: Description of the product
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("products", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductsSearchResult(
            data=[
                ProductsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class QuotesQuery:
    """
    Query class for Quotes entity operations.
    """

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> QuotesListResult:
        """
        Returns a paginated list of quotes

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            QuotesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("quotes", "list", params)
        # Cast generic envelope to concrete typed result
        return QuotesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get a single quote by ID

        Args:
            id: Quote ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("quotes", "get", params)
        return result



    async def search(
        self,
        query: QuotesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> QuotesSearchResult:
        """
        Search quotes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (QuotesSearchFilter):
        - id: Unique record identifier
        - subject: Subject or title of the quote
        - quote_stage: Current stage of the quote
        - valid_till: Date until which the quote is valid
        - carrier: Shipping carrier
        - sub_total: Subtotal before tax and adjustments
        - tax: Tax amount
        - adjustment: Adjustment amount
        - grand_total: Total amount including tax and adjustments
        - discount: Discount amount
        - terms_and_conditions: Terms and conditions text
        - description: Description or notes about the quote
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            QuotesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("quotes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return QuotesSearchResult(
            data=[
                QuotesSearchData(**row)
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

    def __init__(self, connector: ZohoCrmConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        page_token: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        **kwargs
    ) -> InvoicesListResult:
        """
        Returns a paginated list of invoices

        Args:
            page: Page number
            per_page: Number of records per page
            page_token: Page token for fetching beyond 2000 records
            sort_by: Field to sort by
            sort_order: Sort order
            **kwargs: Additional parameters

        Returns:
            InvoicesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "page_token": page_token,
            "sort_by": sort_by,
            "sort_order": sort_order,
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
    ) -> dict[str, Any]:
        """
        Get a single invoice by ID

        Args:
            id: Invoice ID
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
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
        - id: Unique record identifier
        - subject: Subject or title of the invoice
        - invoice_number: Invoice number
        - invoice_date: Date the invoice was issued
        - due_date: Payment due date
        - status: Current status of the invoice
        - purchase_order: Associated purchase order number
        - sub_total: Subtotal before tax and adjustments
        - tax: Tax amount
        - adjustment: Adjustment amount
        - grand_total: Total amount including tax and adjustments
        - discount: Discount amount
        - excise_duty: Excise duty amount
        - terms_and_conditions: Terms and conditions text
        - description: Description or notes about the invoice
        - created_time: Time the record was created
        - modified_time: Time the record was last modified

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
