"""
Pydantic models for zendesk-support connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from pydantic import BaseModel, ConfigDict, SkipValidation
from typing import TypeVar, Generic
from typing import Optional

# Authentication configuration

class ZendeskSupportAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """OAuth2 access token"""
    refresh_token: Optional[str] = None
    """OAuth2 refresh token (optional)"""
    client_id: Optional[str] = None
    """OAuth2 client ID (optional)"""
    client_secret: Optional[str] = None
    """OAuth2 client secret (optional)"""

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class ZendeskSupportExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: SkipValidation[T]
    """Response data containing the result of the action."""


class ZendeskSupportExecuteResultWithMeta(ZendeskSupportExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: SkipValidation[S]
    """Metadata about the response (e.g., pagination cursors, record counts)."""