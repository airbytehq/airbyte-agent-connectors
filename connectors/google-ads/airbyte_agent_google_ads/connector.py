"""
Google-Ads connector.
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

from .connector_model import GoogleAdsConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AccessibleCustomersListParams,
    AccountsListParams,
    AdGroupAdLabelsListParams,
    AdGroupAdsListParams,
    AdGroupLabelsCreateParams,
    AdGroupLabelsCreateParamsOperationsItem,
    AdGroupLabelsListParams,
    AdGroupsListParams,
    AdGroupsUpdateParams,
    AdGroupsUpdateParamsOperationsItem,
    CampaignLabelsCreateParams,
    CampaignLabelsCreateParamsOperationsItem,
    CampaignLabelsListParams,
    CampaignsListParams,
    CampaignsUpdateParams,
    CampaignsUpdateParamsOperationsItem,
    LabelsCreateParams,
    LabelsCreateParamsOperationsItem,
    AirbyteSearchParams,
    AccountsSearchFilter,
    AccountsSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    AdGroupsSearchFilter,
    AdGroupsSearchQuery,
    AdGroupAdsSearchFilter,
    AdGroupAdsSearchQuery,
    CampaignLabelsSearchFilter,
    CampaignLabelsSearchQuery,
    AdGroupLabelsSearchFilter,
    AdGroupLabelsSearchQuery,
    AdGroupAdLabelsSearchFilter,
    AdGroupAdLabelsSearchQuery,
)
from .models import GoogleAdsAuthConfig
if TYPE_CHECKING:
    from .models import GoogleAdsReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    GoogleAdsCheckResult,
    GoogleAdsExecuteResult,
    GoogleAdsExecuteResultWithMeta,
    AccessibleCustomersListResult,
    AccountsListResult,
    CampaignsListResult,
    AdGroupsListResult,
    AdGroupAdsListResult,
    CampaignLabelsListResult,
    AdGroupLabelsListResult,
    AdGroupAdLabelsListResult,
    AccessibleCustomersList,
    Account,
    AdGroup,
    AdGroupAd,
    AdGroupAdLabel,
    AdGroupLabel,
    AdGroupLabelMutateResponse,
    AdGroupMutateResponse,
    Campaign,
    CampaignLabel,
    CampaignLabelMutateResponse,
    CampaignMutateResponse,
    LabelMutateResponse,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdGroupsSearchData,
    AdGroupsSearchResult,
    AdGroupAdsSearchData,
    AdGroupAdsSearchResult,
    CampaignLabelsSearchData,
    CampaignLabelsSearchResult,
    AdGroupLabelsSearchData,
    AdGroupLabelsSearchResult,
    AdGroupAdLabelsSearchData,
    AdGroupAdLabelsSearchResult,
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




class GoogleAdsConnector:
    """
    Type-safe Google-Ads API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "google-ads"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("accessible_customers", "list"): True,
        ("accounts", "list"): True,
        ("campaigns", "list"): True,
        ("ad_groups", "list"): True,
        ("ad_group_ads", "list"): True,
        ("campaign_labels", "list"): True,
        ("ad_group_labels", "list"): True,
        ("ad_group_ad_labels", "list"): True,
        ("campaigns", "update"): None,
        ("ad_groups", "update"): None,
        ("labels", "create"): None,
        ("campaign_labels", "create"): None,
        ("ad_group_labels", "create"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('accounts', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('campaigns', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('ad_groups', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('ad_group_ads', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('campaign_labels', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('ad_group_labels', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('ad_group_ad_labels', 'list'): {'query': 'query', 'page_token': 'pageToken', 'page_size': 'pageSize', 'customer_id': 'customer_id'},
        ('campaigns', 'update'): {'operations': 'operations', 'customer_id': 'customer_id'},
        ('ad_groups', 'update'): {'operations': 'operations', 'customer_id': 'customer_id'},
        ('labels', 'create'): {'operations': 'operations', 'customer_id': 'customer_id'},
        ('campaign_labels', 'create'): {'operations': 'operations', 'customer_id': 'customer_id'},
        ('ad_group_labels', 'create'): {'operations': 'operations', 'customer_id': 'customer_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GoogleAdsAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GoogleAdsAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new google-ads connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GoogleAdsAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GoogleAdsConnector(auth_config=GoogleAdsAuthConfig(client_id="...", client_secret="...", refresh_token="...", developer_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GoogleAdsConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = GoogleAdsConnector(
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
                connector_definition_id=str(GoogleAdsConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GoogleAdsAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GoogleAdsConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.accessible_customers = AccessibleCustomersQuery(self)
        self.accounts = AccountsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.ad_groups = AdGroupsQuery(self)
        self.ad_group_ads = AdGroupAdsQuery(self)
        self.campaign_labels = CampaignLabelsQuery(self)
        self.ad_group_labels = AdGroupLabelsQuery(self)
        self.ad_group_ad_labels = AdGroupAdLabelsQuery(self)
        self.labels = LabelsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["accessible_customers"],
        action: Literal["list"],
        params: "AccessibleCustomersListParams"
    ) -> "AccessibleCustomersListResult": ...

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
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams"
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups"],
        action: Literal["list"],
        params: "AdGroupsListParams"
    ) -> "AdGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_group_ads"],
        action: Literal["list"],
        params: "AdGroupAdsListParams"
    ) -> "AdGroupAdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_labels"],
        action: Literal["list"],
        params: "CampaignLabelsListParams"
    ) -> "CampaignLabelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_group_labels"],
        action: Literal["list"],
        params: "AdGroupLabelsListParams"
    ) -> "AdGroupLabelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_group_ad_labels"],
        action: Literal["list"],
        params: "AdGroupAdLabelsListParams"
    ) -> "AdGroupAdLabelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["update"],
        params: "CampaignsUpdateParams"
    ) -> "CampaignMutateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_groups"],
        action: Literal["update"],
        params: "AdGroupsUpdateParams"
    ) -> "AdGroupMutateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["labels"],
        action: Literal["create"],
        params: "LabelsCreateParams"
    ) -> "LabelMutateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaign_labels"],
        action: Literal["create"],
        params: "CampaignLabelsCreateParams"
    ) -> "CampaignLabelMutateResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_group_labels"],
        action: Literal["create"],
        params: "AdGroupLabelsCreateParams"
    ) -> "AdGroupLabelMutateResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "update", "create", "search"],
        params: Mapping[str, Any]
    ) -> GoogleAdsExecuteResult[Any] | GoogleAdsExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "update", "create", "search"],
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
                return GoogleAdsExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GoogleAdsExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GoogleAdsCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GoogleAdsCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GoogleAdsCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GoogleAdsCheckResult(
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
            @GoogleAdsConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GoogleAdsConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GoogleAdsConnectorModel,
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
        return describe_entities(GoogleAdsConnectorModel)

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
            (e for e in GoogleAdsConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GoogleAdsConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GoogleAdsConnector.create(...)
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
        replication_config: "GoogleAdsReplicationConfig" | None = None,
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
            consent_url = await GoogleAdsConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Google-Ads Source",
                replication_config=GoogleAdsReplicationConfig(customer_id="...", start_date="...", conversion_window_days="..."),
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
                definition_id=str(GoogleAdsConnectorModel.id),
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
        auth_config: "GoogleAdsAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GoogleAdsReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GoogleAdsConnector":
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
            A GoogleAdsConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GoogleAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleAdsAuthConfig(client_id="...", client_secret="...", refresh_token="...", developer_token="..."),
            )

            # With replication config (required for this connector):
            connector = await GoogleAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleAdsAuthConfig(client_id="...", client_secret="...", refresh_token="...", developer_token="..."),
                replication_config=GoogleAdsReplicationConfig(customer_id="...", start_date="...", conversion_window_days="..."),
            )

            # With server-side OAuth:
            connector = await GoogleAdsConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GoogleAdsReplicationConfig(customer_id="...", start_date="...", conversion_window_days="..."),
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
                connector_definition_id=str(GoogleAdsConnectorModel.id),
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




class AccessibleCustomersQuery:
    """
    Query class for AccessibleCustomers entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AccessibleCustomersListResult:
        """
        Returns resource names of customers directly accessible by the user authenticating the call. No customer_id is required for this endpoint.

        Returns:
            AccessibleCustomersListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accessible_customers", "list", params)
        # Cast generic envelope to concrete typed result
        return AccessibleCustomersListResult(
            data=result.data
        )



class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AccountsListResult:
        """
        Retrieves customer account details using GAQL query.

        Args:
            query: Google Ads Query Language (GAQL) query
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountsListResult(
            data=result.data,
            meta=result.meta
        )



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
        - customer_auto_tagging_enabled: Whether auto-tagging is enabled for the account
        - customer_call_reporting_setting_call_conversion_action: Call conversion action resource name
        - customer_call_reporting_setting_call_conversion_reporting_enabled: Whether call conversion reporting is enabled
        - customer_call_reporting_setting_call_reporting_enabled: Whether call reporting is enabled
        - customer_conversion_tracking_setting_conversion_tracking_id: Conversion tracking ID
        - customer_conversion_tracking_setting_cross_account_conversion_tracking_id: Cross-account conversion tracking ID
        - customer_currency_code: Currency code for the account (e.g., USD)
        - customer_descriptive_name: Descriptive name of the customer account
        - customer_final_url_suffix: URL suffix appended to final URLs
        - customer_has_partners_badge: Whether the account has a Google Partners badge
        - customer_id: Unique customer account ID
        - customer_manager: Whether this is a manager (MCC) account
        - customer_optimization_score: Optimization score for the account (0.0 to 1.0)
        - customer_optimization_score_weight: Weight of the optimization score
        - customer_pay_per_conversion_eligibility_failure_reasons: Reasons why pay-per-conversion is not eligible
        - customer_remarketing_setting_google_global_site_tag: Google global site tag snippet
        - customer_resource_name: Resource name of the customer
        - customer_test_account: Whether this is a test account
        - customer_time_zone: Time zone of the account
        - customer_tracking_url_template: Tracking URL template for the account
        - segments_date: Date segment for the report row

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

class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Retrieves campaign data using GAQL query.

        Args:
            query: GAQL query for campaigns
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=result.meta
        )



    async def update(
        self,
        operations: list[CampaignsUpdateParamsOperationsItem],
        customer_id: str,
        **kwargs
    ) -> CampaignMutateResponse:
        """
        Updates campaign properties such as status (enable/pause), name, or other mutable fields using the Google Ads CampaignService mutate endpoint.

        Args:
            operations: List of campaign operations to perform
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            CampaignMutateResponse
        """
        params = {k: v for k, v in {
            "operations": operations,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "update", params)
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
        - campaign_id: Campaign ID
        - campaign_name: Campaign name
        - campaign_status: Campaign status (ENABLED, PAUSED, REMOVED)
        - campaign_advertising_channel_type: Advertising channel type (SEARCH, DISPLAY, etc.)
        - campaign_advertising_channel_sub_type: Advertising channel sub-type
        - campaign_bidding_strategy: Bidding strategy resource name
        - campaign_bidding_strategy_type: Bidding strategy type
        - campaign_campaign_budget: Campaign budget resource name
        - campaign_budget_amount_micros: Campaign budget amount in micros
        - campaign_start_date: Campaign start date
        - campaign_end_date: Campaign end date
        - campaign_serving_status: Campaign serving status
        - campaign_resource_name: Resource name of the campaign
        - campaign_labels: Labels applied to the campaign
        - campaign_network_settings_target_google_search: Whether targeting Google Search
        - campaign_network_settings_target_search_network: Whether targeting search network
        - campaign_network_settings_target_content_network: Whether targeting content network
        - campaign_network_settings_target_partner_search_network: Whether targeting partner search network
        - metrics_clicks: Number of clicks
        - metrics_ctr: Click-through rate
        - metrics_conversions: Number of conversions
        - metrics_conversions_value: Total conversions value
        - metrics_cost_micros: Cost in micros
        - metrics_impressions: Number of impressions
        - metrics_average_cpc: Average cost per click
        - metrics_average_cpm: Average cost per thousand impressions
        - metrics_interactions: Number of interactions
        - segments_date: Date segment for the report row
        - segments_hour: Hour segment
        - segments_ad_network_type: Ad network type segment

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

class AdGroupsQuery:
    """
    Query class for AdGroups entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdGroupsListResult:
        """
        Retrieves ad group data using GAQL query.

        Args:
            query: GAQL query for ad groups
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AdGroupsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupsListResult(
            data=result.data,
            meta=result.meta
        )



    async def update(
        self,
        operations: list[AdGroupsUpdateParamsOperationsItem],
        customer_id: str,
        **kwargs
    ) -> AdGroupMutateResponse:
        """
        Updates ad group properties such as status (enable/pause), name, or bid amounts using the Google Ads AdGroupService mutate endpoint.

        Args:
            operations: List of ad group operations to perform
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AdGroupMutateResponse
        """
        params = {k: v for k, v in {
            "operations": operations,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups", "update", params)
        return result



    async def search(
        self,
        query: AdGroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdGroupsSearchResult:
        """
        Search ad_groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdGroupsSearchFilter):
        - campaign_id: Parent campaign ID
        - ad_group_id: Ad group ID
        - ad_group_name: Ad group name
        - ad_group_status: Ad group status (ENABLED, PAUSED, REMOVED)
        - ad_group_type: Ad group type
        - ad_group_ad_rotation_mode: Ad rotation mode
        - ad_group_base_ad_group: Base ad group resource name
        - ad_group_campaign: Parent campaign resource name
        - ad_group_cpc_bid_micros: CPC bid in micros
        - ad_group_cpm_bid_micros: CPM bid in micros
        - ad_group_cpv_bid_micros: CPV bid in micros
        - ad_group_effective_target_cpa_micros: Effective target CPA in micros
        - ad_group_effective_target_cpa_source: Source of the effective target CPA
        - ad_group_effective_target_roas: Effective target ROAS
        - ad_group_effective_target_roas_source: Source of the effective target ROAS
        - ad_group_labels: Labels applied to the ad group
        - ad_group_resource_name: Resource name of the ad group
        - ad_group_target_cpa_micros: Target CPA in micros
        - ad_group_target_roas: Target ROAS
        - ad_group_tracking_url_template: Tracking URL template
        - metrics_cost_micros: Cost in micros
        - segments_date: Date segment for the report row

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdGroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdGroupsSearchResult(
            data=[
                AdGroupsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdGroupAdsQuery:
    """
    Query class for AdGroupAds entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdGroupAdsListResult:
        """
        Retrieves ad group ad data using GAQL query.

        Args:
            query: GAQL query for ad group ads
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AdGroupAdsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_group_ads", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupAdsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AdGroupAdsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdGroupAdsSearchResult:
        """
        Search ad_group_ads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdGroupAdsSearchFilter):
        - ad_group_id: Parent ad group ID
        - ad_group_ad_ad_id: Ad ID
        - ad_group_ad_ad_name: Ad name
        - ad_group_ad_ad_type: Ad type
        - ad_group_ad_status: Ad group ad status (ENABLED, PAUSED, REMOVED)
        - ad_group_ad_ad_strength: Ad strength rating
        - ad_group_ad_ad_display_url: Display URL of the ad
        - ad_group_ad_ad_final_urls: Final URLs for the ad
        - ad_group_ad_ad_final_mobile_urls: Final mobile URLs for the ad
        - ad_group_ad_ad_final_url_suffix: Final URL suffix
        - ad_group_ad_ad_tracking_url_template: Tracking URL template
        - ad_group_ad_ad_resource_name: Resource name of the ad
        - ad_group_ad_ad_group: Ad group resource name
        - ad_group_ad_resource_name: Resource name of the ad group ad
        - ad_group_ad_labels: Labels applied to the ad group ad
        - ad_group_ad_policy_summary_approval_status: Policy approval status
        - ad_group_ad_policy_summary_review_status: Policy review status
        - segments_date: Date segment for the report row

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdGroupAdsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_group_ads", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdGroupAdsSearchResult(
            data=[
                AdGroupAdsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CampaignLabelsQuery:
    """
    Query class for CampaignLabels entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CampaignLabelsListResult:
        """
        Retrieves campaign label associations using GAQL query.

        Args:
            query: GAQL query for campaign labels
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            CampaignLabelsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_labels", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignLabelsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        operations: list[CampaignLabelsCreateParamsOperationsItem],
        customer_id: str,
        **kwargs
    ) -> CampaignLabelMutateResponse:
        """
        Creates a campaign-label association, applying an existing label to a campaign for organization and filtering.

        Args:
            operations: List of campaign label operations to perform
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            CampaignLabelMutateResponse
        """
        params = {k: v for k, v in {
            "operations": operations,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaign_labels", "create", params)
        return result



    async def search(
        self,
        query: CampaignLabelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignLabelsSearchResult:
        """
        Search campaign_labels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignLabelsSearchFilter):
        - campaign_id: Campaign ID
        - campaign_label_resource_name: Resource name of the campaign label
        - label_id: Label ID
        - label_name: Label name
        - label_resource_name: Resource name of the label

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignLabelsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("campaign_labels", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignLabelsSearchResult(
            data=[
                CampaignLabelsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdGroupLabelsQuery:
    """
    Query class for AdGroupLabels entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdGroupLabelsListResult:
        """
        Retrieves ad group label associations using GAQL query.

        Args:
            query: GAQL query for ad group labels
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AdGroupLabelsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_group_labels", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupLabelsListResult(
            data=result.data,
            meta=result.meta
        )



    async def create(
        self,
        operations: list[AdGroupLabelsCreateParamsOperationsItem],
        customer_id: str,
        **kwargs
    ) -> AdGroupLabelMutateResponse:
        """
        Creates an ad group-label association, applying an existing label to an ad group for organization and filtering.

        Args:
            operations: List of ad group label operations to perform
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AdGroupLabelMutateResponse
        """
        params = {k: v for k, v in {
            "operations": operations,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_group_labels", "create", params)
        return result



    async def search(
        self,
        query: AdGroupLabelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdGroupLabelsSearchResult:
        """
        Search ad_group_labels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdGroupLabelsSearchFilter):
        - ad_group_id: Ad group ID
        - ad_group_label_resource_name: Resource name of the ad group label
        - label_id: Label ID
        - label_name: Label name
        - label_resource_name: Resource name of the label

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdGroupLabelsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_group_labels", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdGroupLabelsSearchResult(
            data=[
                AdGroupLabelsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AdGroupAdLabelsQuery:
    """
    Query class for AdGroupAdLabels entity operations.
    """

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        query: str | None = None,
        page_token: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> AdGroupAdLabelsListResult:
        """
        Retrieves ad group ad label associations using GAQL query.

        Args:
            query: GAQL query for ad group ad labels
            page_token: Token for pagination
            page_size: Number of results per page (max 10000)
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            AdGroupAdLabelsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "pageToken": page_token,
            "pageSize": page_size,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_group_ad_labels", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupAdLabelsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AdGroupAdLabelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdGroupAdLabelsSearchResult:
        """
        Search ad_group_ad_labels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdGroupAdLabelsSearchFilter):
        - ad_group_ad_ad_id: Ad ID
        - ad_group_ad_label_resource_name: Resource name of the ad group ad label
        - label_id: Label ID
        - label_name: Label name
        - label_resource_name: Resource name of the label

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdGroupAdLabelsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_group_ad_labels", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdGroupAdLabelsSearchResult(
            data=[
                AdGroupAdLabelsSearchData(**row)
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

    def __init__(self, connector: GoogleAdsConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        operations: list[LabelsCreateParamsOperationsItem],
        customer_id: str,
        **kwargs
    ) -> LabelMutateResponse:
        """
        Creates a new label that can be applied to campaigns, ad groups, or ads for organization and reporting purposes.

        Args:
            operations: List of label operations to perform
            customer_id: Google Ads customer ID (10 digits, no dashes)
            **kwargs: Additional parameters

        Returns:
            LabelMutateResponse
        """
        params = {k: v for k, v in {
            "operations": operations,
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("labels", "create", params)
        return result


