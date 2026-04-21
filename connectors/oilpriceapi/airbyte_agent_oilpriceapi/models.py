"""
Pydantic models for oilpriceapi connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any


# Authentication configuration

class OilPriceApiAuthConfig(BaseModel):
    """Authentication configuration for OilPriceAPI."""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """API key from oilpriceapi.com. Used as Token {api_key} in Authorization header."""


# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PriceChanges24h(BaseModel):
    """24-hour price changes."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[float, None] = Field(default=None)
    percent: Union[float, None] = Field(default=None)
    previous_price: Union[float, None] = Field(default=None)


class PriceChanges(BaseModel):
    """Price change data."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PriceMetadata(BaseModel):
    """Price metadata."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    source: Union[str, None] = Field(default=None)
    source_description: Union[str, None] = Field(default=None)


class LatestPrice(BaseModel):
    """Latest price for a commodity."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price: Union[float, None] = Field(default=None)
    formatted: Union[str, None] = Field(default=None)
    currency: Union[str, None] = Field(default=None)
    code: str = Field(description="Commodity code (e.g. WTI_USD, BRENT_USD)")
    created_at: Union[str, None] = Field(default=None)
    updated_at: Union[str, None] = Field(default=None)
    type: Union[str, None] = Field(default=None)
    unit: Union[str, None] = Field(default=None)
    source: Union[str, None] = Field(default=None)
    changes: Union[PriceChanges, None] = Field(default=None)
    metadata: Union[PriceMetadata, None] = Field(default=None)


class HistoricalPrice(BaseModel):
    """Historical price record for a commodity."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, None] = Field(default=None)
    price: Union[float, None] = Field(default=None)
    currency: Union[str, None] = Field(default=None)
    code: str = Field(description="Commodity code (e.g. WTI_USD, BRENT_USD)")
    created_at: str = Field(description="Price record timestamp")
    source: Union[str, None] = Field(default=None)
    type: Union[str, None] = Field(default=None)


# ===== RESPONSE ENVELOPE MODELS =====

T = TypeVar('T')
S = TypeVar('S')


class OilPriceApiCheckResult(BaseModel):
    """Result of a health check."""
    model_config = ConfigDict(extra="forbid")

    status: str = "unhealthy"
    error: str | None = None
    checked_entity: str | None = None
    checked_action: str | None = None


class OilPriceApiExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only."""
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class OilPriceApiExecuteResultWithMeta(OilPriceApiExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata."""
    meta: S
    """Metadata about the response."""


# ===== OPERATION RESULT TYPE ALIASES =====

class HistoricalPricesListResultMeta(BaseModel):
    """Metadata for historical_prices.list result."""
    model_config = ConfigDict(extra="allow")


HistoricalPricesListResult = OilPriceApiExecuteResultWithMeta[list[HistoricalPrice], HistoricalPricesListResultMeta]
