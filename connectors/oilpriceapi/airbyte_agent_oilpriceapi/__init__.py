"""
Airbyte Agent Connector for OilPriceAPI.

Provides access to WTI and Brent crude oil spot prices.
"""

from .connector import OilPriceApiConnector
from .models import (
    OilPriceApiAuthConfig,
    OilPriceApiCheckResult,
    OilPriceApiExecuteResult,
    OilPriceApiExecuteResultWithMeta,
    LatestPrice,
    HistoricalPrice,
    HistoricalPricesListResult,
)
from .types import (
    LatestPricesGetParams,
    HistoricalPricesListParams,
)
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig

__all__ = [
    "OilPriceApiConnector",
    "AirbyteAuthConfig",
    "OilPriceApiAuthConfig",
    "OilPriceApiCheckResult",
    "OilPriceApiExecuteResult",
    "OilPriceApiExecuteResultWithMeta",
    "LatestPrice",
    "HistoricalPrice",
    "HistoricalPricesListResult",
    "LatestPricesGetParams",
    "HistoricalPricesListParams",
]
