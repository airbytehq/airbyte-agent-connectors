"""
Pydantic models for commonroom connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class CommonroomAuthConfig(BaseModel):
    """API Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_token: str
    """API token for authenticating with CommonRoom API. Create a token at https://app.commonroom.io/ under Settings | API tokens."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ApiTokenStatus(BaseModel):
    """API token status information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    jti: Union[str | None, Any] = Field(default=None)
    iat: Union[int | None, Any] = Field(default=None)
    exp: Union[int | None, Any] = Field(default=None)
    sub: Union[str | None, Any] = Field(default=None)

class ContactCustomField(BaseModel):
    """Custom field definition for contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    values: Union[list[str] | None, Any] = Field(default=None)
    multivalue: Union[bool | None, Any] = Field(default=None)

class ActivityType(BaseModel):
    """Activity type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    display_name: Union[str | None, Any] = Field(default=None, alias="displayName")

class Segment(BaseModel):
    """Segment definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class Tag(BaseModel):
    """Tag definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None, alias="createdAt")
    deleted_at: Union[str | None, Any] = Field(default=None, alias="deletedAt")
    entity_types: Union[list[str] | None, Any] = Field(default=None, alias="entityTypes")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class CommonroomExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class CommonroomExecuteResultWithMeta(CommonroomExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TagsListResult = CommonroomExecuteResult[list[Tag]]
"""Result type for tags.list operation."""

