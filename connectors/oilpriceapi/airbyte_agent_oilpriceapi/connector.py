"""
OilPriceAPI connector.
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

from .connector_model import OilPriceApiConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    LatestPricesGetParams,
    HistoricalPricesListParams,
)
from .models import OilPriceApiAuthConfig
if TYPE_CHECKING:
    pass

# Import response models and envelope models at runtime
from .models import (
    OilPriceApiCheckResult,
    OilPriceApiExecuteResult,
    OilPriceApiExecuteResultWithMeta,
    LatestPrice,
    HistoricalPrice,
    HistoricalPricesListResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 50_000


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


class OilPriceApiConnector:
    """
    Type-safe OilPriceAPI connector.

    Provides access to WTI and Brent crude oil spot prices from OilPriceAPI.
    """

    connector_name = "oilpriceapi"
    connector_version = "0.1.0"
    vendored_sdk_version = "0.1.0"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("latest_prices", "get"): None,
        ("historical_prices", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    _PARAM_MAP = {
        ('latest_prices', 'get'): {'by_code': 'by_code'},
        ('historical_prices', 'list'): {'by_code': 'by_code'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (OilPriceApiAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: OilPriceApiAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
    ):
        """
        Initialize a new OilPriceAPI connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., OilPriceApiAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.

        Examples:
            # Local mode (direct API calls)
            connector = OilPriceApiConnector(auth_config=OilPriceApiAuthConfig(api_key="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = OilPriceApiConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="my-customer",
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
                connector_definition_id=str(OilPriceApiConnectorModel.id),
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or OilPriceApiAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            config_values = None

            self._executor = LocalExecutor(
                model=OilPriceApiConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh,
            )

        # Initialize entity query objects
        self.latest_prices = LatestPricesQuery(self)
        self.historical_prices = HistoricalPricesQuery(self)

    # ===== TYPED EXECUTE METHOD =====

    @overload
    async def execute(
        self,
        entity: Literal["latest_prices"],
        action: Literal["get"],
        params: "LatestPricesGetParams"
    ) -> "LatestPrice": ...

    @overload
    async def execute(
        self,
        entity: Literal["historical_prices"],
        action: Literal["list"],
        params: "HistoricalPricesListParams"
    ) -> "HistoricalPricesListResult": ...

    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get"],
        params: Mapping[str, Any]
    ) -> OilPriceApiExecuteResult[Any] | OilPriceApiExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get"],
        params: Mapping[str, Any] | None = None
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        Args:
            entity: Entity name (e.g., "latest_prices", "historical_prices")
            action: Operation action (e.g., "get", "list")
            params: Operation parameters (typed based on entity+action)

        Returns:
            Typed response based on the operation

        Example:
            price = await connector.execute(
                entity="latest_prices",
                action="get",
                params={"by_code": "WTI_USD"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Remap parameter names
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            if result.meta is not None:
                return OilPriceApiExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return OilPriceApiExecuteResult[Any](data=result.data)
        else:
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> OilPriceApiCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Returns:
            OilPriceApiCheckResult with status ("healthy" or "unhealthy") and optional error message
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return OilPriceApiCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return OilPriceApiCheckResult(
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
        """Decorator that adds tool utilities like docstring augmentation and output limits."""

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    OilPriceApiConnectorModel,
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

            if full_doc:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate  # type: ignore[return-value]

    def list_entities(self) -> list[dict[str, Any]]:
        """Get structured data about available entities, actions, and parameters."""
        return describe_entities(OilPriceApiConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """Get the JSON schema for an entity."""
        entity_def = next(
            (e for e in OilPriceApiConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in OilPriceApiConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode)."""
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "OilPriceApiAuthConfig",
        name: str | None = None,
    ) -> "OilPriceApiConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name

        Returns:
            An OilPriceApiConnector instance configured in hosted mode
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
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None

            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(OilPriceApiConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
            )
        finally:
            await client.close()

        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )


class LatestPricesQuery:
    """Query class for LatestPrices entity operations."""

    def __init__(self, connector: OilPriceApiConnector):
        self._connector = connector

    async def get(
        self,
        by_code: str,
        **kwargs
    ) -> LatestPrice:
        """
        Returns the latest spot price for a commodity.

        Args:
            by_code: Commodity code (WTI_USD or BRENT_USD)
            **kwargs: Additional parameters

        Returns:
            LatestPrice
        """
        params = {k: v for k, v in {
            "by_code": by_code,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("latest_prices", "get", params)
        return result


class HistoricalPricesQuery:
    """Query class for HistoricalPrices entity operations."""

    def __init__(self, connector: OilPriceApiConnector):
        self._connector = connector

    async def list(
        self,
        by_code: str,
        **kwargs
    ) -> HistoricalPricesListResult:
        """
        Returns historical price data for a commodity.

        Args:
            by_code: Commodity code (WTI_USD or BRENT_USD)
            **kwargs: Additional parameters

        Returns:
            HistoricalPricesListResult
        """
        params = {k: v for k, v in {
            "by_code": by_code,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("historical_prices", "list", params)
        return result
