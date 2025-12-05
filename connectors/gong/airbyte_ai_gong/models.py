"""
Pydantic models for gong connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from pydantic import BaseModel, ConfigDict, SkipValidation
from typing import TypeVar, Generic

# Authentication configuration

class GongAuthConfig(BaseModel):
    """Access Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_key: str
    """Your Gong API Access Key"""
    access_key_secret: str
    """Your Gong API Access Key Secret"""

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class GongExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: SkipValidation[T]
    """Response data containing the result of the action."""


class GongExecuteResultWithMeta(GongExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: SkipValidation[S]
    """Metadata about the response (e.g., pagination cursors, record counts)."""