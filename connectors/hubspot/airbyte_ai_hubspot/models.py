"""
Pydantic models for hubspot connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class HubspotAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Your HubSpot Private App Access Token or OAuth Access Token"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Contact(BaseModel):
    """HubSpot contact object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)

class PagingNext(BaseModel):
    """Nested schema for Paging.next"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""
    link: Union[str, Any] = Field(default=None, description="URL for next page")
    """URL for next page"""

class Paging(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: Union[PagingNext, Any] = Field(default=None)

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Contact], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class Company(BaseModel):
    """HubSpot company object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)

class CompaniesList(BaseModel):
    """Paginated list of companies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Company], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class Deal(BaseModel):
    """HubSpot deal object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)

class DealsList(BaseModel):
    """Paginated list of deals"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Deal], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class Ticket(BaseModel):
    """HubSpot ticket object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)

class TicketsList(BaseModel):
    """Paginated list of tickets"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Ticket], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

class SchemaLabels(BaseModel):
    """Display labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    singular: Union[str, Any] = Field(default=None)
    plural: Union[str, Any] = Field(default=None)

class Schema(BaseModel):
    """Custom object schema definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    labels: Union[SchemaLabels, Any] = Field(default=None)
    object_type_id: Union[str, Any] = Field(default=None, alias="objectTypeId")
    fully_qualified_name: Union[str, Any] = Field(default=None, alias="fullyQualifiedName")
    properties: Union[list[dict[str, Any]], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")

class SchemasList(BaseModel):
    """List of custom object schemas"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Schema], Any] = Field(default=None)

class CRMObject(BaseModel):
    """Generic HubSpot CRM object (for custom objects)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)

class ObjectsList(BaseModel):
    """Paginated list of generic CRM objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[CRMObject], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class HubspotExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class HubspotExecuteResultWithMeta(HubspotExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

