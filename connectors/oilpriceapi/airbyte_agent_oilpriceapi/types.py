"""
Type definitions for oilpriceapi connector.
"""
from __future__ import annotations

try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]


# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class LatestPricesGetParams(TypedDict):
    """Parameters for latest_prices.get operation"""
    by_code: str


class HistoricalPricesListParams(TypedDict):
    """Parameters for historical_prices.list operation"""
    by_code: str
