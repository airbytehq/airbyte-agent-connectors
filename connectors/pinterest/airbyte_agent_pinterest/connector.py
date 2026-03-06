"""
Pinterest connector.
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

from .connector_model import PinterestConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AdAccountsGetParams,
    AdAccountsListParams,
    AdGroupsListParams,
    AdsListParams,
    AudiencesListParams,
    BoardPinsListParams,
    BoardSectionsListParams,
    BoardsGetParams,
    BoardsListParams,
    CampaignsListParams,
    CatalogsFeedsListParams,
    CatalogsListParams,
    CatalogsProductGroupsListParams,
    ConversionTagsListParams,
    CustomerListsListParams,
    KeywordsListParams,
    AirbyteSearchParams,
    AdAccountsSearchFilter,
    AdAccountsSearchQuery,
    BoardsSearchFilter,
    BoardsSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    AdGroupsSearchFilter,
    AdGroupsSearchQuery,
    AdsSearchFilter,
    AdsSearchQuery,
    BoardSectionsSearchFilter,
    BoardSectionsSearchQuery,
    BoardPinsSearchFilter,
    BoardPinsSearchQuery,
    CatalogsSearchFilter,
    CatalogsSearchQuery,
    CatalogsFeedsSearchFilter,
    CatalogsFeedsSearchQuery,
    CatalogsProductGroupsSearchFilter,
    CatalogsProductGroupsSearchQuery,
    AudiencesSearchFilter,
    AudiencesSearchQuery,
    ConversionTagsSearchFilter,
    ConversionTagsSearchQuery,
    CustomerListsSearchFilter,
    CustomerListsSearchQuery,
    KeywordsSearchFilter,
    KeywordsSearchQuery,
)
from .models import PinterestAuthConfig
if TYPE_CHECKING:
    from .models import PinterestReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    PinterestCheckResult,
    PinterestExecuteResult,
    PinterestExecuteResultWithMeta,
    AdAccountsListResult,
    BoardsListResult,
    CampaignsListResult,
    AdGroupsListResult,
    AdsListResult,
    BoardSectionsListResult,
    BoardPinsListResult,
    CatalogsListResult,
    CatalogsFeedsListResult,
    CatalogsProductGroupsListResult,
    AudiencesListResult,
    ConversionTagsListResult,
    CustomerListsListResult,
    KeywordsListResult,
    Ad,
    AdAccount,
    AdGroup,
    Audience,
    Board,
    BoardPin,
    BoardSection,
    Campaign,
    Catalog,
    CatalogsFeed,
    CatalogsProductGroup,
    ConversionTag,
    CustomerList,
    Keyword,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AdAccountsSearchData,
    AdAccountsSearchResult,
    BoardsSearchData,
    BoardsSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    AdGroupsSearchData,
    AdGroupsSearchResult,
    AdsSearchData,
    AdsSearchResult,
    BoardSectionsSearchData,
    BoardSectionsSearchResult,
    BoardPinsSearchData,
    BoardPinsSearchResult,
    CatalogsSearchData,
    CatalogsSearchResult,
    CatalogsFeedsSearchData,
    CatalogsFeedsSearchResult,
    CatalogsProductGroupsSearchData,
    CatalogsProductGroupsSearchResult,
    AudiencesSearchData,
    AudiencesSearchResult,
    ConversionTagsSearchData,
    ConversionTagsSearchResult,
    CustomerListsSearchData,
    CustomerListsSearchResult,
    KeywordsSearchData,
    KeywordsSearchResult,
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




class PinterestConnector:
    """
    Type-safe Pinterest API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "pinterest"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("ad_accounts", "list"): True,
        ("ad_accounts", "get"): None,
        ("boards", "list"): True,
        ("boards", "get"): None,
        ("campaigns", "list"): True,
        ("ad_groups", "list"): True,
        ("ads", "list"): True,
        ("board_sections", "list"): True,
        ("board_pins", "list"): True,
        ("catalogs", "list"): True,
        ("catalogs_feeds", "list"): True,
        ("catalogs_product_groups", "list"): True,
        ("audiences", "list"): True,
        ("conversion_tags", "list"): True,
        ("customer_lists", "list"): True,
        ("keywords", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('ad_accounts', 'list'): {'page_size': 'page_size', 'bookmark': 'bookmark', 'include_shared_accounts': 'include_shared_accounts'},
        ('ad_accounts', 'get'): {'ad_account_id': 'ad_account_id'},
        ('boards', 'list'): {'page_size': 'page_size', 'bookmark': 'bookmark', 'privacy': 'privacy'},
        ('boards', 'get'): {'board_id': 'board_id'},
        ('campaigns', 'list'): {'ad_account_id': 'ad_account_id', 'page_size': 'page_size', 'bookmark': 'bookmark', 'entity_statuses': 'entity_statuses', 'order': 'order'},
        ('ad_groups', 'list'): {'ad_account_id': 'ad_account_id', 'page_size': 'page_size', 'bookmark': 'bookmark', 'entity_statuses': 'entity_statuses', 'order': 'order'},
        ('ads', 'list'): {'ad_account_id': 'ad_account_id', 'page_size': 'page_size', 'bookmark': 'bookmark', 'entity_statuses': 'entity_statuses', 'order': 'order'},
        ('board_sections', 'list'): {'board_id': 'board_id', 'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('board_pins', 'list'): {'board_id': 'board_id', 'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('catalogs', 'list'): {'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('catalogs_feeds', 'list'): {'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('catalogs_product_groups', 'list'): {'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('audiences', 'list'): {'ad_account_id': 'ad_account_id', 'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('conversion_tags', 'list'): {'ad_account_id': 'ad_account_id', 'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('customer_lists', 'list'): {'ad_account_id': 'ad_account_id', 'page_size': 'page_size', 'bookmark': 'bookmark'},
        ('keywords', 'list'): {'ad_account_id': 'ad_account_id', 'ad_group_id': 'ad_group_id', 'page_size': 'page_size', 'bookmark': 'bookmark'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (PinterestAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: PinterestAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new pinterest connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., PinterestAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = PinterestConnector(auth_config=PinterestAuthConfig(refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = PinterestConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = PinterestConnector(
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
                connector_definition_id=str(PinterestConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or PinterestAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=PinterestConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.ad_accounts = AdAccountsQuery(self)
        self.boards = BoardsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.ad_groups = AdGroupsQuery(self)
        self.ads = AdsQuery(self)
        self.board_sections = BoardSectionsQuery(self)
        self.board_pins = BoardPinsQuery(self)
        self.catalogs = CatalogsQuery(self)
        self.catalogs_feeds = CatalogsFeedsQuery(self)
        self.catalogs_product_groups = CatalogsProductGroupsQuery(self)
        self.audiences = AudiencesQuery(self)
        self.conversion_tags = ConversionTagsQuery(self)
        self.customer_lists = CustomerListsQuery(self)
        self.keywords = KeywordsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["ad_accounts"],
        action: Literal["list"],
        params: "AdAccountsListParams"
    ) -> "AdAccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["ad_accounts"],
        action: Literal["get"],
        params: "AdAccountsGetParams"
    ) -> "AdAccount": ...

    @overload
    async def execute(
        self,
        entity: Literal["boards"],
        action: Literal["list"],
        params: "BoardsListParams"
    ) -> "BoardsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["boards"],
        action: Literal["get"],
        params: "BoardsGetParams"
    ) -> "Board": ...

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
        entity: Literal["ads"],
        action: Literal["list"],
        params: "AdsListParams"
    ) -> "AdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["board_sections"],
        action: Literal["list"],
        params: "BoardSectionsListParams"
    ) -> "BoardSectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["board_pins"],
        action: Literal["list"],
        params: "BoardPinsListParams"
    ) -> "BoardPinsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalogs"],
        action: Literal["list"],
        params: "CatalogsListParams"
    ) -> "CatalogsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalogs_feeds"],
        action: Literal["list"],
        params: "CatalogsFeedsListParams"
    ) -> "CatalogsFeedsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalogs_product_groups"],
        action: Literal["list"],
        params: "CatalogsProductGroupsListParams"
    ) -> "CatalogsProductGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["audiences"],
        action: Literal["list"],
        params: "AudiencesListParams"
    ) -> "AudiencesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversion_tags"],
        action: Literal["list"],
        params: "ConversionTagsListParams"
    ) -> "ConversionTagsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customer_lists"],
        action: Literal["list"],
        params: "CustomerListsListParams"
    ) -> "CustomerListsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["keywords"],
        action: Literal["list"],
        params: "KeywordsListParams"
    ) -> "KeywordsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> PinterestExecuteResult[Any] | PinterestExecuteResultWithMeta[Any, Any] | Any: ...

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
                return PinterestExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return PinterestExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> PinterestCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            PinterestCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return PinterestCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return PinterestCheckResult(
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
            @PinterestConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @PinterestConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    PinterestConnectorModel,
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
        return describe_entities(PinterestConnectorModel)

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
            (e for e in PinterestConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in PinterestConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await PinterestConnector.create(...)
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
        replication_config: "PinterestReplicationConfig" | None = None,
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
            consent_url = await PinterestConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Pinterest Source",
                replication_config=PinterestReplicationConfig(start_date="..."),
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
                definition_id=str(PinterestConnectorModel.id),
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
        auth_config: "PinterestAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "PinterestReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "PinterestConnector":
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
            A PinterestConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await PinterestConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=PinterestAuthConfig(refresh_token="...", client_id="...", client_secret="..."),
            )

            # With replication config (required for this connector):
            connector = await PinterestConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=PinterestAuthConfig(refresh_token="...", client_id="...", client_secret="..."),
                replication_config=PinterestReplicationConfig(start_date="..."),
            )

            # With server-side OAuth:
            connector = await PinterestConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=PinterestReplicationConfig(start_date="..."),
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
                connector_definition_id=str(PinterestConnectorModel.id),
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




class AdAccountsQuery:
    """
    Query class for AdAccounts entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        bookmark: str | None = None,
        include_shared_accounts: bool | None = None,
        **kwargs
    ) -> AdAccountsListResult:
        """
        Get a list of the ad accounts that the authenticated user has access to.

        Args:
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            include_shared_accounts: Include shared ad accounts.
            **kwargs: Additional parameters

        Returns:
            AdAccountsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "bookmark": bookmark,
            "include_shared_accounts": include_shared_accounts,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AdAccountsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        ad_account_id: str,
        **kwargs
    ) -> AdAccount:
        """
        Get an ad account by ID.

        Args:
            ad_account_id: Unique identifier of the ad account.
            **kwargs: Additional parameters

        Returns:
            AdAccount
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_accounts", "get", params)
        return result



    async def search(
        self,
        query: AdAccountsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdAccountsSearchResult:
        """
        Search ad_accounts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdAccountsSearchFilter):
        - country: Country associated with the ad account
        - created_time: Timestamp when the ad account was created (Unix seconds)
        - currency: Currency used for billing
        - id: Unique identifier for the ad account
        - name: Name of the ad account
        - owner: Owner details of the ad account
        - permissions: Permissions assigned to the ad account
        - updated_time: Timestamp when the ad account was last updated (Unix seconds)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdAccountsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ad_accounts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdAccountsSearchResult(
            data=[
                AdAccountsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BoardsQuery:
    """
    Query class for Boards entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        bookmark: str | None = None,
        privacy: str | None = None,
        **kwargs
    ) -> BoardsListResult:
        """
        Get a list of the boards owned by the authenticated user.

        Args:
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            privacy: Filter by board privacy setting.
            **kwargs: Additional parameters

        Returns:
            BoardsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "bookmark": bookmark,
            "privacy": privacy,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("boards", "list", params)
        # Cast generic envelope to concrete typed result
        return BoardsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        board_id: str,
        **kwargs
    ) -> Board:
        """
        Get a board by ID.

        Args:
            board_id: Unique identifier of the board.
            **kwargs: Additional parameters

        Returns:
            Board
        """
        params = {k: v for k, v in {
            "board_id": board_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("boards", "get", params)
        return result



    async def search(
        self,
        query: BoardsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BoardsSearchResult:
        """
        Search boards records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BoardsSearchFilter):
        - board_pins_modified_at: Timestamp when pins on the board were last modified
        - collaborator_count: Number of collaborators
        - created_at: Timestamp when the board was created
        - description: Board description
        - follower_count: Number of followers
        - id: Unique identifier for the board
        - media: Media content for the board
        - name: Board name
        - owner: Board owner details
        - pin_count: Number of pins on the board
        - privacy: Board privacy setting

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BoardsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("boards", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BoardsSearchResult(
            data=[
                BoardsSearchData(**row)
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

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        entity_statuses: list[str] | None = None,
        order: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Get a list of campaigns in the specified ad account.

        Args:
            ad_account_id: Unique identifier of the ad account.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            entity_statuses: Filter by entity status.
            order: Sort order.
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "page_size": page_size,
            "bookmark": bookmark,
            "entity_statuses": entity_statuses,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=result.meta
        )



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
        - ad_account_id: Ad account ID
        - created_time: Creation timestamp (Unix seconds)
        - daily_spend_cap: Maximum daily spend in microcurrency
        - end_time: End timestamp (Unix seconds)
        - id: Campaign ID
        - is_campaign_budget_optimization: Whether CBO is enabled
        - is_flexible_daily_budgets: Whether flexible daily budgets are enabled
        - lifetime_spend_cap: Maximum lifetime spend in microcurrency
        - name: Campaign name
        - objective_type: Campaign objective type
        - order_line_id: Order line ID on invoice
        - start_time: Start timestamp (Unix seconds)
        - status: Entity status
        - summary_status: Summary status
        - tracking_urls: Third-party tracking URLs
        - type_: Always 'campaign'
        - updated_time: Last update timestamp (Unix seconds)

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

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        entity_statuses: list[str] | None = None,
        order: str | None = None,
        **kwargs
    ) -> AdGroupsListResult:
        """
        Get a list of ad groups in the specified ad account.

        Args:
            ad_account_id: Unique identifier of the ad account.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            entity_statuses: Filter by entity status.
            order: Sort order.
            **kwargs: Additional parameters

        Returns:
            AdGroupsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "page_size": page_size,
            "bookmark": bookmark,
            "entity_statuses": entity_statuses,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ad_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return AdGroupsListResult(
            data=result.data,
            meta=result.meta
        )



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
        - ad_account_id: Ad account ID
        - auto_targeting_enabled: Whether auto targeting is enabled
        - bid_in_micro_currency: Bid in microcurrency
        - bid_strategy_type: Bid strategy type
        - billable_event: Billable event type
        - budget_in_micro_currency: Budget in microcurrency
        - budget_type: Budget type
        - campaign_id: Parent campaign ID
        - conversion_learning_mode_type: oCPM learn mode type
        - created_time: Creation timestamp (Unix seconds)
        - end_time: End time (Unix seconds)
        - feed_profile_id: Feed profile ID
        - id: Ad group ID
        - lifetime_frequency_cap: Max impressions per user in 30 days
        - name: Ad group name
        - optimization_goal_metadata: Optimization goal metadata
        - pacing_delivery_type: Pacing delivery type
        - placement_group: Placement group
        - start_time: Start time (Unix seconds)
        - status: Entity status
        - summary_status: Summary status
        - targeting_spec: Targeting specifications
        - tracking_urls: Third-party tracking URLs
        - type_: Always 'adgroup'
        - updated_time: Last update timestamp (Unix seconds)

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

class AdsQuery:
    """
    Query class for Ads entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        entity_statuses: list[str] | None = None,
        order: str | None = None,
        **kwargs
    ) -> AdsListResult:
        """
        Get a list of ads in the specified ad account.

        Args:
            ad_account_id: Unique identifier of the ad account.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            entity_statuses: Filter by entity status.
            order: Sort order.
            **kwargs: Additional parameters

        Returns:
            AdsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "page_size": page_size,
            "bookmark": bookmark,
            "entity_statuses": entity_statuses,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("ads", "list", params)
        # Cast generic envelope to concrete typed result
        return AdsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AdsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AdsSearchResult:
        """
        Search ads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AdsSearchFilter):
        - ad_account_id: Ad account ID
        - ad_group_id: Ad group ID
        - android_deep_link: Android deep link
        - campaign_id: Campaign ID
        - carousel_android_deep_links: Carousel Android deep links
        - carousel_destination_urls: Carousel destination URLs
        - carousel_ios_deep_links: Carousel iOS deep links
        - click_tracking_url: Click tracking URL
        - collection_items_destination_url_template: Template URL for collection items
        - created_time: Creation timestamp (Unix seconds)
        - creative_type: Creative type
        - destination_url: Main destination URL
        - id: Unique ad ID
        - ios_deep_link: iOS deep link
        - is_pin_deleted: Whether the original pin is deleted
        - is_removable: Whether the ad is removable
        - lead_form_id: Lead form ID
        - name: Ad name
        - pin_id: Associated pin ID
        - rejected_reasons: Rejection reasons
        - rejection_labels: Rejection text labels
        - review_status: Review status
        - status: Entity status
        - summary_status: Summary status
        - tracking_urls: Third-party tracking URLs
        - type_: Always 'pinpromotion'
        - updated_time: Last update timestamp (Unix seconds)
        - view_tracking_url: View tracking URL

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AdsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("ads", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AdsSearchResult(
            data=[
                AdsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BoardSectionsQuery:
    """
    Query class for BoardSections entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        board_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> BoardSectionsListResult:
        """
        Get a list of sections for a specific board.

        Args:
            board_id: Unique identifier of the board.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            BoardSectionsListResult
        """
        params = {k: v for k, v in {
            "board_id": board_id,
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("board_sections", "list", params)
        # Cast generic envelope to concrete typed result
        return BoardSectionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: BoardSectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BoardSectionsSearchResult:
        """
        Search board_sections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BoardSectionsSearchFilter):
        - id: Unique identifier for the board section
        - name: Name of the board section

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BoardSectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("board_sections", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BoardSectionsSearchResult(
            data=[
                BoardSectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BoardPinsQuery:
    """
    Query class for BoardPins entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        board_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> BoardPinsListResult:
        """
        Get a list of pins on a specific board.

        Args:
            board_id: Unique identifier of the board.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            BoardPinsListResult
        """
        params = {k: v for k, v in {
            "board_id": board_id,
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("board_pins", "list", params)
        # Cast generic envelope to concrete typed result
        return BoardPinsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: BoardPinsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BoardPinsSearchResult:
        """
        Search board_pins records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BoardPinsSearchFilter):
        - alt_text: Alternate text for accessibility
        - board_id: Board the pin belongs to
        - board_owner: Board owner info
        - board_section_id: Section within the board
        - created_at: Timestamp when the pin was created
        - creative_type: Creative type
        - description: Pin description
        - dominant_color: Dominant color from the pin image
        - has_been_promoted: Whether the pin has been promoted
        - id: Unique pin identifier
        - is_owner: Whether the current user is the owner
        - is_standard: Whether the pin is a standard pin
        - link: URL link associated with the pin
        - media: Media content
        - parent_pin_id: Parent pin ID if this is a repin
        - pin_metrics: Pin metrics data
        - title: Pin title

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BoardPinsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("board_pins", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BoardPinsSearchResult(
            data=[
                BoardPinsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CatalogsQuery:
    """
    Query class for Catalogs entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> CatalogsListResult:
        """
        Get a list of catalogs for the authenticated user.

        Args:
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            CatalogsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalogs", "list", params)
        # Cast generic envelope to concrete typed result
        return CatalogsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CatalogsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CatalogsSearchResult:
        """
        Search catalogs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CatalogsSearchFilter):
        - catalog_type: Type of catalog
        - created_at: Timestamp when the catalog was created
        - id: Unique catalog identifier
        - name: Catalog name
        - updated_at: Timestamp when the catalog was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CatalogsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("catalogs", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CatalogsSearchResult(
            data=[
                CatalogsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CatalogsFeedsQuery:
    """
    Query class for CatalogsFeeds entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> CatalogsFeedsListResult:
        """
        Get a list of catalog feeds for the authenticated user.

        Args:
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            CatalogsFeedsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalogs_feeds", "list", params)
        # Cast generic envelope to concrete typed result
        return CatalogsFeedsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CatalogsFeedsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CatalogsFeedsSearchResult:
        """
        Search catalogs_feeds records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CatalogsFeedsSearchFilter):
        - catalog_type: Type of catalog
        - created_at: Timestamp when the feed was created
        - default_availability: Default availability status
        - default_country: Default country
        - default_currency: Default currency for pricing
        - default_locale: Default locale
        - format: Feed format
        - id: Unique feed identifier
        - location: URL where the feed is available
        - name: Feed name
        - preferred_processing_schedule: Preferred processing schedule
        - status: Feed status
        - updated_at: Timestamp when the feed was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CatalogsFeedsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("catalogs_feeds", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CatalogsFeedsSearchResult(
            data=[
                CatalogsFeedsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CatalogsProductGroupsQuery:
    """
    Query class for CatalogsProductGroups entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> CatalogsProductGroupsListResult:
        """
        Get a list of catalog product groups for the authenticated user.

        Args:
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            CatalogsProductGroupsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalogs_product_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return CatalogsProductGroupsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CatalogsProductGroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CatalogsProductGroupsSearchResult:
        """
        Search catalogs_product_groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CatalogsProductGroupsSearchFilter):
        - created_at: Creation timestamp (Unix seconds)
        - description: Product group description
        - feed_id: Associated feed ID
        - id: Unique product group identifier
        - is_featured: Whether the product group is featured
        - name: Product group name
        - status: Product group status
        - type_: Product group type
        - updated_at: Last update timestamp (Unix seconds)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CatalogsProductGroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("catalogs_product_groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CatalogsProductGroupsSearchResult(
            data=[
                CatalogsProductGroupsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AudiencesQuery:
    """
    Query class for Audiences entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> AudiencesListResult:
        """
        Get a list of audiences for the specified ad account.

        Args:
            ad_account_id: Unique identifier of the ad account.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            AudiencesListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("audiences", "list", params)
        # Cast generic envelope to concrete typed result
        return AudiencesListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AudiencesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AudiencesSearchResult:
        """
        Search audiences records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AudiencesSearchFilter):
        - ad_account_id: Ad account ID
        - audience_type: Audience type
        - created_timestamp: Creation time (Unix seconds)
        - description: Audience description
        - id: Unique audience identifier
        - name: Audience name
        - rule: Audience targeting rules
        - size: Estimated audience size
        - status: Audience status
        - type_: Always 'audience'
        - updated_timestamp: Last update time (Unix seconds)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AudiencesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("audiences", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AudiencesSearchResult(
            data=[
                AudiencesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ConversionTagsQuery:
    """
    Query class for ConversionTags entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> ConversionTagsListResult:
        """
        Get a list of conversion tags for the specified ad account.

        Args:
            ad_account_id: Unique identifier of the ad account.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            ConversionTagsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversion_tags", "list", params)
        # Cast generic envelope to concrete typed result
        return ConversionTagsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ConversionTagsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ConversionTagsSearchResult:
        """
        Search conversion_tags records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ConversionTagsSearchFilter):
        - ad_account_id: Ad account ID
        - code_snippet: JavaScript code snippet for tracking
        - configs: Tag configurations
        - enhanced_match_status: Enhanced match status
        - id: Unique conversion tag identifier
        - last_fired_time_ms: Timestamp of last event fired (milliseconds)
        - name: Conversion tag name
        - status: Status
        - version: Version number

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ConversionTagsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("conversion_tags", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ConversionTagsSearchResult(
            data=[
                ConversionTagsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CustomerListsQuery:
    """
    Query class for CustomerLists entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> CustomerListsListResult:
        """
        Get a list of customer lists for the specified ad account.

        Args:
            ad_account_id: Unique identifier of the ad account.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            CustomerListsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customer_lists", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomerListsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CustomerListsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomerListsSearchResult:
        """
        Search customer_lists records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomerListsSearchFilter):
        - ad_account_id: Associated ad account ID
        - created_time: Creation time (Unix seconds)
        - id: Unique customer list identifier
        - name: Customer list name
        - num_batches: Total number of list updates
        - num_removed_user_records: Count of removed user records
        - num_uploaded_user_records: Count of uploaded user records
        - status: Status
        - type_: Always 'customerlist'
        - updated_time: Last update time (Unix seconds)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomerListsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("customer_lists", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CustomerListsSearchResult(
            data=[
                CustomerListsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class KeywordsQuery:
    """
    Query class for Keywords entity operations.
    """

    def __init__(self, connector: PinterestConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ad_account_id: str,
        ad_group_id: str,
        page_size: int | None = None,
        bookmark: str | None = None,
        **kwargs
    ) -> KeywordsListResult:
        """
        Get a list of keywords for the specified ad account. Requires an ad_group_id filter.

        Args:
            ad_account_id: Unique identifier of the ad account.
            ad_group_id: Ad group ID to filter keywords by.
            page_size: Maximum number of items to include in a single page of the response.
            bookmark: Cursor value for paginating through results.
            **kwargs: Additional parameters

        Returns:
            KeywordsListResult
        """
        params = {k: v for k, v in {
            "ad_account_id": ad_account_id,
            "ad_group_id": ad_group_id,
            "page_size": page_size,
            "bookmark": bookmark,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("keywords", "list", params)
        # Cast generic envelope to concrete typed result
        return KeywordsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: KeywordsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> KeywordsSearchResult:
        """
        Search keywords records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (KeywordsSearchFilter):
        - archived: Whether the keyword is archived
        - bid: Bid value in microcurrency
        - id: Unique keyword identifier
        - match_type: Match type
        - parent_id: Parent entity ID
        - parent_type: Parent entity type
        - type_: Always 'keyword'
        - value: Keyword text value

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            KeywordsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("keywords", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return KeywordsSearchResult(
            data=[
                KeywordsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
