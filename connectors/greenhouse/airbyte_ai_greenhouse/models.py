"""
Pydantic models for greenhouse connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from pydantic import BaseModel, ConfigDict, SkipValidation
from typing import TypeVar, Generic

# Authentication configuration

class GreenhouseAuthConfig(BaseModel):
    """Harvest API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Greenhouse Harvest API Key from the Dev Center"""

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class GreenhouseExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: SkipValidation[T]
    """Response data containing the result of the action."""


class GreenhouseExecuteResultWithMeta(GreenhouseExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: SkipValidation[S]
    """Metadata about the response (e.g., pagination cursors, record counts)."""