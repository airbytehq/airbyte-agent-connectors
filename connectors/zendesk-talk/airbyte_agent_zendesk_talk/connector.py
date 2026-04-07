"""
Zendesk-Talk connector.
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

from .connector_model import ZendeskTalkConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AccountOverviewListParams,
    AddressesGetParams,
    AddressesListParams,
    AgentsActivityListParams,
    AgentsOverviewListParams,
    CallLegsListParams,
    CallsListParams,
    CurrentQueueActivityListParams,
    GreetingCategoriesGetParams,
    GreetingCategoriesListParams,
    GreetingsGetParams,
    GreetingsListParams,
    IvrsGetParams,
    IvrsListParams,
    PhoneNumbersGetParams,
    PhoneNumbersListParams,
    AirbyteSearchParams,
    AddressesSearchFilter,
    AddressesSearchQuery,
    AgentsActivitySearchFilter,
    AgentsActivitySearchQuery,
    AgentsOverviewSearchFilter,
    AgentsOverviewSearchQuery,
    GreetingCategoriesSearchFilter,
    GreetingCategoriesSearchQuery,
    GreetingsSearchFilter,
    GreetingsSearchQuery,
    PhoneNumbersSearchFilter,
    PhoneNumbersSearchQuery,
    CallLegsSearchFilter,
    CallLegsSearchQuery,
    CallsSearchFilter,
    CallsSearchQuery,
    CurrentQueueActivitySearchFilter,
    CurrentQueueActivitySearchQuery,
    AccountOverviewSearchFilter,
    AccountOverviewSearchQuery,
    IvrsSearchFilter,
    IvrsSearchQuery,
)
from .models import ZendeskTalkOauth20AuthConfig, ZendeskTalkApiTokenAuthConfig
from .models import ZendeskTalkAuthConfig
if TYPE_CHECKING:
    from .models import ZendeskTalkReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    ZendeskTalkCheckResult,
    ZendeskTalkExecuteResult,
    ZendeskTalkExecuteResultWithMeta,
    PhoneNumbersListResult,
    AddressesListResult,
    GreetingsListResult,
    GreetingCategoriesListResult,
    IvrsListResult,
    AgentsActivityListResult,
    AgentsOverviewListResult,
    AccountOverviewListResult,
    CurrentQueueActivityListResult,
    CallsListResult,
    CallLegsListResult,
    AccountOverview,
    Address,
    AgentActivity,
    AgentsOverview,
    Call,
    CallLeg,
    CurrentQueueActivity,
    Greeting,
    GreetingCategory,
    Ivr,
    PhoneNumber,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AddressesSearchData,
    AddressesSearchResult,
    AgentsActivitySearchData,
    AgentsActivitySearchResult,
    AgentsOverviewSearchData,
    AgentsOverviewSearchResult,
    GreetingCategoriesSearchData,
    GreetingCategoriesSearchResult,
    GreetingsSearchData,
    GreetingsSearchResult,
    PhoneNumbersSearchData,
    PhoneNumbersSearchResult,
    CallLegsSearchData,
    CallLegsSearchResult,
    CallsSearchData,
    CallsSearchResult,
    CurrentQueueActivitySearchData,
    CurrentQueueActivitySearchResult,
    AccountOverviewSearchData,
    AccountOverviewSearchResult,
    IvrsSearchData,
    IvrsSearchResult,
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




class ZendeskTalkConnector:
    """
    Type-safe Zendesk-Talk API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-talk"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("phone_numbers", "list"): True,
        ("phone_numbers", "get"): None,
        ("addresses", "list"): True,
        ("addresses", "get"): None,
        ("greetings", "list"): True,
        ("greetings", "get"): None,
        ("greeting_categories", "list"): True,
        ("greeting_categories", "get"): None,
        ("ivrs", "list"): True,
        ("ivrs", "get"): None,
        ("agents_activity", "list"): True,
        ("agents_overview", "list"): True,
        ("account_overview", "list"): True,
        ("current_queue_activity", "list"): True,
        ("calls", "list"): True,
        ("call_legs", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('phone_numbers', 'get'): {'phone_number_id': 'phone_number_id'},
        ('addresses', 'get'): {'address_id': 'address_id'},
        ('greetings', 'get'): {'greeting_id': 'greeting_id'},
        ('greeting_categories', 'get'): {'greeting_category_id': 'greeting_category_id'},
        ('ivrs', 'get'): {'ivr_id': 'ivr_id'},
        ('calls', 'list'): {'start_time': 'start_time'},
        ('call_legs', 'list'): {'start_time': 'start_time'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ZendeskTalkOauth20AuthConfig, ZendeskTalkApiTokenAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ZendeskTalkAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new zendesk-talk connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ZendeskTalkAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Zendesk subdomain (the part before .zendesk.com in your Zendesk URL)
        Examples:
            # Local mode (direct API calls)
            connector = ZendeskTalkConnector(auth_config=ZendeskTalkAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ZendeskTalkConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = ZendeskTalkConnector(
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
                connector_definition_id=str(ZendeskTalkConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ZendeskTalkAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, ZendeskTalkOauth20AuthConfig):
                    auth_scheme = "zendeskOAuth"
                if isinstance(auth_config, ZendeskTalkApiTokenAuthConfig):
                    auth_scheme = "zendeskAPIToken"

            self._executor = LocalExecutor(
                model=ZendeskTalkConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if subdomain:
                base_url = base_url.replace("{subdomain}", subdomain)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.phone_numbers = PhoneNumbersQuery(self)
        self.addresses = AddressesQuery(self)
        self.greetings = GreetingsQuery(self)
        self.greeting_categories = GreetingCategoriesQuery(self)
        self.ivrs = IvrsQuery(self)
        self.agents_activity = AgentsActivityQuery(self)
        self.agents_overview = AgentsOverviewQuery(self)
        self.account_overview = AccountOverviewQuery(self)
        self.current_queue_activity = CurrentQueueActivityQuery(self)
        self.calls = CallsQuery(self)
        self.call_legs = CallLegsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["phone_numbers"],
        action: Literal["list"],
        params: "PhoneNumbersListParams"
    ) -> "PhoneNumbersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["phone_numbers"],
        action: Literal["get"],
        params: "PhoneNumbersGetParams"
    ) -> "PhoneNumber": ...

    @overload
    async def execute(
        self,
        entity: Literal["addresses"],
        action: Literal["list"],
        params: "AddressesListParams"
    ) -> "AddressesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["addresses"],
        action: Literal["get"],
        params: "AddressesGetParams"
    ) -> "Address": ...

    @overload
    async def execute(
        self,
        entity: Literal["greetings"],
        action: Literal["list"],
        params: "GreetingsListParams"
    ) -> "GreetingsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["greetings"],
        action: Literal["get"],
        params: "GreetingsGetParams"
    ) -> "Greeting": ...

    @overload
    async def execute(
        self,
        entity: Literal["greeting_categories"],
        action: Literal["list"],
        params: "GreetingCategoriesListParams"
    ) -> "GreetingCategoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["greeting_categories"],
        action: Literal["get"],
        params: "GreetingCategoriesGetParams"
    ) -> "GreetingCategory": ...

    @overload
    async def execute(
        self,
        entity: Literal["ivrs"],
        action: Literal["list"],
        params: "IvrsListParams"
    ) -> "IvrsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ivrs"],
        action: Literal["get"],
        params: "IvrsGetParams"
    ) -> "Ivr": ...

    @overload
    async def execute(
        self,
        entity: Literal["agents_activity"],
        action: Literal["list"],
        params: "AgentsActivityListParams"
    ) -> "AgentsActivityListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["agents_overview"],
        action: Literal["list"],
        params: "AgentsOverviewListParams"
    ) -> "AgentsOverviewListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["account_overview"],
        action: Literal["list"],
        params: "AccountOverviewListParams"
    ) -> "AccountOverviewListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["current_queue_activity"],
        action: Literal["list"],
        params: "CurrentQueueActivityListParams"
    ) -> "CurrentQueueActivityListResult": ...

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
        entity: Literal["call_legs"],
        action: Literal["list"],
        params: "CallLegsListParams"
    ) -> "CallLegsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> ZendeskTalkExecuteResult[Any] | ZendeskTalkExecuteResultWithMeta[Any, Any] | Any: ...

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
                return ZendeskTalkExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ZendeskTalkExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ZendeskTalkCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ZendeskTalkCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ZendeskTalkCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ZendeskTalkCheckResult(
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
            @ZendeskTalkConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @ZendeskTalkConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    ZendeskTalkConnectorModel,
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
        return describe_entities(ZendeskTalkConnectorModel)

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
            (e for e in ZendeskTalkConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ZendeskTalkConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await ZendeskTalkConnector.create(...)
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
        replication_config: "ZendeskTalkReplicationConfig" | None = None,
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
            consent_url = await ZendeskTalkConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Zendesk-Talk Source",
                replication_config=ZendeskTalkReplicationConfig(start_date="..."),
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
                definition_id=str(ZendeskTalkConnectorModel.id),
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
        auth_config: "ZendeskTalkAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "ZendeskTalkReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "ZendeskTalkConnector":
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
            A ZendeskTalkConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await ZendeskTalkConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=ZendeskTalkAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
            )

            # With replication config (required for this connector):
            connector = await ZendeskTalkConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=ZendeskTalkAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."),
                replication_config=ZendeskTalkReplicationConfig(start_date="..."),
            )

            # With server-side OAuth:
            connector = await ZendeskTalkConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=ZendeskTalkReplicationConfig(start_date="..."),
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
                connector_definition_id=str(ZendeskTalkConnectorModel.id),
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




class PhoneNumbersQuery:
    """
    Query class for PhoneNumbers entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> PhoneNumbersListResult:
        """
        Returns a list of all phone numbers in the Zendesk Talk account

        Returns:
            PhoneNumbersListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("phone_numbers", "list", params)
        # Cast generic envelope to concrete typed result
        return PhoneNumbersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        phone_number_id: str,
        **kwargs
    ) -> PhoneNumber:
        """
        Retrieves a single phone number by ID

        Args:
            phone_number_id: ID of the phone number
            **kwargs: Additional parameters

        Returns:
            PhoneNumber
        """
        params = {k: v for k, v in {
            "phone_number_id": phone_number_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("phone_numbers", "get", params)
        return result



    async def search(
        self,
        query: PhoneNumbersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PhoneNumbersSearchResult:
        """
        Search phone_numbers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PhoneNumbersSearchFilter):
        - call_recording_consent: What call recording consent is set to
        - capabilities: Phone number capabilities (sms, mms, voice)
        - categorised_greetings: Greeting category IDs and names
        - categorised_greetings_with_sub_settings: Greeting categories with associated settings
        - country_code: ISO country code for the number
        - created_at: Date and time the phone number was created
        - default_greeting_ids: Names of default system greetings
        - default_group_id: Default group ID
        - display_number: Formatted phone number
        - external: Whether this is an external caller ID number
        - failover_number: Failover number associated with the phone number
        - greeting_ids: Custom greeting IDs associated with the phone number
        - group_ids: Array of associated group IDs
        - id: Unique phone number identifier
        - ivr_id: ID of IVR associated with the phone number
        - line_type: Type of line (phone or digital)
        - location: Geographical location of the number
        - name: Nickname if set, otherwise the display number
        - nickname: Nickname of the phone number
        - number: Phone number digits
        - outbound_enabled: Whether outbound calls are enabled
        - priority: Priority level of the phone number
        - recorded: Whether calls are recorded
        - schedule_id: ID of schedule associated with the phone number
        - sms_enabled: Whether SMS is enabled
        - sms_group_id: Group associated with SMS
        - token: Generated token unique for the phone number
        - toll_free: Whether the number is toll-free
        - transcription: Whether voicemail transcription is enabled
        - voice_enabled: Whether voice is enabled

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PhoneNumbersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("phone_numbers", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PhoneNumbersSearchResult(
            data=[
                PhoneNumbersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AddressesQuery:
    """
    Query class for Addresses entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AddressesListResult:
        """
        Returns a list of all addresses in the Zendesk Talk account

        Returns:
            AddressesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("addresses", "list", params)
        # Cast generic envelope to concrete typed result
        return AddressesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        address_id: str,
        **kwargs
    ) -> Address:
        """
        Retrieves a single address by ID

        Args:
            address_id: ID of the address
            **kwargs: Additional parameters

        Returns:
            Address
        """
        params = {k: v for k, v in {
            "address_id": address_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("addresses", "get", params)
        return result



    async def search(
        self,
        query: AddressesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AddressesSearchResult:
        """
        Search addresses records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AddressesSearchFilter):
        - city: City of the address
        - country_code: ISO country code
        - id: Unique address identifier
        - name: Name of the address
        - provider_reference: Provider reference of the address
        - province: Province of the address
        - state: State of the address
        - street: Street of the address
        - zip: Zip code of the address

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AddressesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("addresses", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AddressesSearchResult(
            data=[
                AddressesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GreetingsQuery:
    """
    Query class for Greetings entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> GreetingsListResult:
        """
        Returns a list of all greetings in the Zendesk Talk account

        Returns:
            GreetingsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("greetings", "list", params)
        # Cast generic envelope to concrete typed result
        return GreetingsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        greeting_id: str,
        **kwargs
    ) -> Greeting:
        """
        Retrieves a single greeting by ID

        Args:
            greeting_id: ID of the greeting
            **kwargs: Additional parameters

        Returns:
            Greeting
        """
        params = {k: v for k, v in {
            "greeting_id": greeting_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("greetings", "get", params)
        return result



    async def search(
        self,
        query: GreetingsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GreetingsSearchResult:
        """
        Search greetings records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GreetingsSearchFilter):
        - active: Whether the greeting is associated with phone numbers
        - audio_name: Audio file name
        - audio_url: Path to the greeting sound file
        - category_id: ID of the greeting category
        - default: Whether this is a system default greeting
        - default_lang: Whether the greeting has a default language
        - has_sub_settings: Sub-settings for categorized greetings
        - id: Greeting ID
        - ivr_ids: IDs of IVRs associated with the greeting
        - name: Name of the greeting
        - pending: Whether the greeting is pending
        - phone_number_ids: IDs of phone numbers associated with the greeting
        - upload_id: Upload ID associated with the greeting

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GreetingsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("greetings", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GreetingsSearchResult(
            data=[
                GreetingsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GreetingCategoriesQuery:
    """
    Query class for GreetingCategories entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> GreetingCategoriesListResult:
        """
        Returns a list of all greeting categories

        Returns:
            GreetingCategoriesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("greeting_categories", "list", params)
        # Cast generic envelope to concrete typed result
        return GreetingCategoriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        greeting_category_id: str,
        **kwargs
    ) -> GreetingCategory:
        """
        Retrieves a single greeting category by ID

        Args:
            greeting_category_id: ID of the greeting category
            **kwargs: Additional parameters

        Returns:
            GreetingCategory
        """
        params = {k: v for k, v in {
            "greeting_category_id": greeting_category_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("greeting_categories", "get", params)
        return result



    async def search(
        self,
        query: GreetingCategoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GreetingCategoriesSearchResult:
        """
        Search greeting_categories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GreetingCategoriesSearchFilter):
        - id: Greeting category ID
        - name: Name of the greeting category

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GreetingCategoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("greeting_categories", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GreetingCategoriesSearchResult(
            data=[
                GreetingCategoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class IvrsQuery:
    """
    Query class for Ivrs entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> IvrsListResult:
        """
        Returns a list of all IVR configurations

        Returns:
            IvrsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ivrs", "list", params)
        # Cast generic envelope to concrete typed result
        return IvrsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        ivr_id: str,
        **kwargs
    ) -> Ivr:
        """
        Retrieves a single IVR configuration by ID

        Args:
            ivr_id: ID of the IVR
            **kwargs: Additional parameters

        Returns:
            Ivr
        """
        params = {k: v for k, v in {
            "ivr_id": ivr_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ivrs", "get", params)
        return result



    async def search(
        self,
        query: IvrsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IvrsSearchResult:
        """
        Search ivrs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IvrsSearchFilter):
        - id: IVR ID
        - menus: List of IVR menus
        - name: Name of the IVR
        - phone_number_ids: IDs of phone numbers configured with this IVR
        - phone_number_names: Names of phone numbers configured with this IVR

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IvrsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ivrs", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IvrsSearchResult(
            data=[
                IvrsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AgentsActivityQuery:
    """
    Query class for AgentsActivity entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AgentsActivityListResult:
        """
        Returns activity statistics for all agents for the current day

        Returns:
            AgentsActivityListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agents_activity", "list", params)
        # Cast generic envelope to concrete typed result
        return AgentsActivityListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AgentsActivitySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AgentsActivitySearchResult:
        """
        Search agents_activity records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AgentsActivitySearchFilter):
        - accepted_third_party_conferences: Accepted third party conferences
        - accepted_transfers: Total transfers accepted
        - agent_id: Agent ID
        - agent_state: Agent state: online, offline, away, or transfers_only
        - available_time: Total time agent was available to answer calls
        - avatar_url: URL to agent avatar
        - average_hold_time: Average hold time per call
        - average_talk_time: Average talk time per call
        - average_wrap_up_time: Average wrap-up time per call
        - away_time: Total time agent was set to away
        - call_status: Agent call status: on_call, wrap_up, or null
        - calls_accepted: Total calls accepted
        - calls_denied: Total calls denied
        - calls_missed: Total calls missed
        - calls_put_on_hold: Total calls placed on hold
        - forwarding_number: Forwarding number set by the agent
        - name: Agent name
        - online_time: Total online time
        - started_third_party_conferences: Started third party conferences
        - started_transfers: Total transfers started
        - total_call_duration: Total call duration
        - total_hold_time: Total hold time across all calls
        - total_talk_time: Total talk time (excludes hold)
        - total_wrap_up_time: Total wrap-up time
        - transfers_only_time: Total time in transfers-only mode
        - via: Channel the agent is registered on

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AgentsActivitySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("agents_activity", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AgentsActivitySearchResult(
            data=[
                AgentsActivitySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AgentsOverviewQuery:
    """
    Query class for AgentsOverview entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AgentsOverviewListResult:
        """
        Returns overview statistics for all agents for the current day

        Returns:
            AgentsOverviewListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agents_overview", "list", params)
        # Cast generic envelope to concrete typed result
        return AgentsOverviewListResult(
            data=result.data
        )



    async def search(
        self,
        query: AgentsOverviewSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AgentsOverviewSearchResult:
        """
        Search agents_overview records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AgentsOverviewSearchFilter):
        - average_accepted_transfers: Average accepted transfers
        - average_available_time: Average available time
        - average_away_time: Average away time
        - average_calls_accepted: Average calls accepted
        - average_calls_denied: Average calls denied
        - average_calls_missed: Average calls missed
        - average_calls_put_on_hold: Average calls put on hold
        - average_hold_time: Average hold time
        - average_online_time: Average online time
        - average_started_transfers: Average started transfers
        - average_talk_time: Average talk time
        - average_transfers_only_time: Average transfers-only time
        - average_wrap_up_time: Average wrap-up time
        - current_timestamp: Current timestamp
        - total_accepted_transfers: Total accepted transfers
        - total_calls_accepted: Total calls accepted
        - total_calls_denied: Total calls denied
        - total_calls_missed: Total calls missed
        - total_calls_put_on_hold: Total calls put on hold
        - total_hold_time: Total hold time
        - total_started_transfers: Total started transfers
        - total_talk_time: Total talk time
        - total_wrap_up_time: Total wrap-up time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AgentsOverviewSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("agents_overview", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AgentsOverviewSearchResult(
            data=[
                AgentsOverviewSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AccountOverviewQuery:
    """
    Query class for AccountOverview entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AccountOverviewListResult:
        """
        Returns overview statistics for the account for the current day

        Returns:
            AccountOverviewListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("account_overview", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountOverviewListResult(
            data=result.data
        )



    async def search(
        self,
        query: AccountOverviewSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AccountOverviewSearchResult:
        """
        Search account_overview records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AccountOverviewSearchFilter):
        - average_call_duration: Average call duration
        - average_callback_wait_time: Average callback wait time
        - average_hold_time: Average hold time per call
        - average_queue_wait_time: Average queue wait time
        - average_time_to_answer: Average time to answer
        - average_wrap_up_time: Average wrap-up time
        - current_timestamp: Current timestamp
        - max_calls_waiting: Max calls waiting in queue
        - max_queue_wait_time: Max queue wait time
        - total_call_duration: Total call duration
        - total_callback_calls: Total callback calls
        - total_calls: Total calls
        - total_calls_abandoned_in_queue: Total calls abandoned in queue
        - total_calls_outside_business_hours: Total calls outside business hours
        - total_calls_with_exceeded_queue_wait_time: Total calls exceeding max queue wait time
        - total_calls_with_requested_voicemail: Total calls requesting voicemail
        - total_embeddable_callback_calls: Total embeddable callback calls
        - total_hold_time: Total hold time
        - total_inbound_calls: Total inbound calls
        - total_outbound_calls: Total outbound calls
        - total_textback_requests: Total textback requests
        - total_voicemails: Total voicemails
        - total_wrap_up_time: Total wrap-up time

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountOverviewSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("account_overview", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AccountOverviewSearchResult(
            data=[
                AccountOverviewSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CurrentQueueActivityQuery:
    """
    Query class for CurrentQueueActivity entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> CurrentQueueActivityListResult:
        """
        Returns current queue activity statistics

        Returns:
            CurrentQueueActivityListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("current_queue_activity", "list", params)
        # Cast generic envelope to concrete typed result
        return CurrentQueueActivityListResult(
            data=result.data
        )



    async def search(
        self,
        query: CurrentQueueActivitySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CurrentQueueActivitySearchResult:
        """
        Search current_queue_activity records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CurrentQueueActivitySearchFilter):
        - agents_online: Current number of agents online
        - average_wait_time: Average wait time for callers in queue (seconds)
        - callbacks_waiting: Number of callers in callback queue
        - calls_waiting: Number of callers waiting in queue
        - current_timestamp: Current timestamp
        - embeddable_callbacks_waiting: Number of Web Widget callback requests waiting
        - longest_wait_time: Longest wait time for any caller (seconds)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CurrentQueueActivitySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("current_queue_activity", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CurrentQueueActivitySearchResult(
            data=[
                CurrentQueueActivitySearchData(**row)
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

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_time: int,
        **kwargs
    ) -> CallsListResult:
        """
        Returns incremental call data. Requires a start_time parameter (Unix epoch timestamp).

        Args:
            start_time: Unix epoch time to start from (e.g. 1704067200 for 2024-01-01)
            **kwargs: Additional parameters

        Returns:
            CallsListResult
        """
        params = {k: v for k, v in {
            "start_time": start_time,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "list", params)
        # Cast generic envelope to concrete typed result
        return CallsListResult(
            data=result.data,
            meta=result.meta
        )



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
        - agent_id: Agent ID
        - call_charge: Call charge amount
        - call_group_id: Call group ID
        - call_recording_consent: Call recording consent status
        - call_recording_consent_action: Recording consent action
        - call_recording_consent_keypress: Recording consent keypress
        - callback: Whether this was a callback
        - callback_source: Source of the callback
        - completion_status: Call completion status
        - consultation_time: Consultation time
        - created_at: Creation timestamp
        - customer_requested_voicemail: Whether customer requested voicemail
        - default_group: Whether default group was used
        - direction: Call direction (inbound/outbound)
        - duration: Call duration in seconds
        - exceeded_queue_time: Whether queue time was exceeded
        - exceeded_queue_wait_time: Whether max queue wait time was exceeded
        - hold_time: Hold time in seconds
        - id: Call ID
        - ivr_action: IVR action taken
        - ivr_destination_group_name: IVR destination group name
        - ivr_hops: Number of IVR hops
        - ivr_routed_to: Where IVR routed the call
        - ivr_time_spent: Time spent in IVR
        - minutes_billed: Minutes billed
        - not_recording_time: Time not recording
        - outside_business_hours: Whether call was outside business hours
        - overflowed: Whether call overflowed
        - overflowed_to: Where call overflowed to
        - phone_number: Phone number used
        - phone_number_id: Phone number ID
        - quality_issues: Quality issues detected
        - recording_control_interactions: Recording control interactions count
        - recording_time: Recording time
        - talk_time: Talk time in seconds
        - ticket_id: Associated ticket ID
        - time_to_answer: Time to answer in seconds
        - updated_at: Last update timestamp
        - voicemail: Whether it was a voicemail
        - wait_time: Wait time in seconds
        - wrap_up_time: Wrap-up time in seconds

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

class CallLegsQuery:
    """
    Query class for CallLegs entity operations.
    """

    def __init__(self, connector: ZendeskTalkConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_time: int,
        **kwargs
    ) -> CallLegsListResult:
        """
        Returns incremental call leg data. Requires a start_time parameter (Unix epoch timestamp).

        Args:
            start_time: Unix epoch time to start from (e.g. 1704067200 for 2024-01-01)
            **kwargs: Additional parameters

        Returns:
            CallLegsListResult
        """
        params = {k: v for k, v in {
            "start_time": start_time,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("call_legs", "list", params)
        # Cast generic envelope to concrete typed result
        return CallLegsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CallLegsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CallLegsSearchResult:
        """
        Search call_legs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CallLegsSearchFilter):
        - agent_id: Agent ID
        - available_via: Channel agent was available through
        - call_charge: Call charge amount
        - call_id: Associated call ID
        - completion_status: Completion status
        - conference_from: Conference from time
        - conference_time: Conference duration
        - conference_to: Conference to time
        - consultation_from: Consultation from time
        - consultation_time: Consultation duration
        - consultation_to: Consultation to time
        - created_at: Creation timestamp
        - duration: Duration in seconds
        - forwarded_to: Number forwarded to
        - hold_time: Hold time in seconds
        - id: Call leg ID
        - minutes_billed: Minutes billed
        - quality_issues: Quality issues detected
        - talk_time: Talk time in seconds
        - transferred_from: Transferred from agent ID
        - transferred_to: Transferred to agent ID
        - type_: Type of call leg
        - updated_at: Last update timestamp
        - user_id: User ID
        - wrap_up_time: Wrap-up time in seconds

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CallLegsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("call_legs", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CallLegsSearchResult(
            data=[
                CallLegsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
