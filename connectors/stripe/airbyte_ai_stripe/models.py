"""
Pydantic models for stripe connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class StripeAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """Authentication bearer token"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CustomerAddress(BaseModel):
    """Customer's address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line1: Union[str, Any] = Field(default=None)
    line2: Union[str, Any] = Field(default=None)
    city: Union[str, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    postal_code: Union[str, Any] = Field(default=None)
    country: Union[str, Any] = Field(default=None)

class Customer(BaseModel):
    """Customer type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    address: Union[CustomerAddress | None, Any] = Field(default=None)
    metadata: Union[dict[str, str], Any] = Field(default=None)
    created: Union[int, Any] = Field(default=None)
    balance: Union[int, Any] = Field(default=None)
    delinquent: Union[bool, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    default_currency: Union[str | None, Any] = Field(default=None)
    default_source: Union[str | None, Any] = Field(default=None)
    discount: Union[dict[str, Any] | None, Any] = Field(default=None)
    invoice_prefix: Union[str | None, Any] = Field(default=None)
    invoice_settings: Union[dict[str, Any] | None, Any] = Field(default=None)
    livemode: Union[bool, Any] = Field(default=None)
    next_invoice_sequence: Union[int | None, Any] = Field(default=None)
    preferred_locales: Union[list[str] | None, Any] = Field(default=None)
    shipping: Union[dict[str, Any] | None, Any] = Field(default=None)
    tax_exempt: Union[str | None, Any] = Field(default=None)
    test_clock: Union[str | None, Any] = Field(default=None)

class CustomerList(BaseModel):
    """CustomerList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str, Any] = Field(default=None)
    data: Union[list[Customer], Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class StripeExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class StripeExecuteResultWithMeta(StripeExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

