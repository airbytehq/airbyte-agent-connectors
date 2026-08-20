"""
Pydantic models for confluence connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class ConfluenceAuthConfig(BaseModel):
    """Confluence API Token Authentication - Authenticate using your Atlassian account email and API token"""

    model_config = ConfigDict(extra="forbid")

    username: str
    """Your Atlassian account email address"""
    password: str
    """Your Confluence API token from https://id.atlassian.com/manage-profile/security/api-tokens"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class SpaceLinks(BaseModel):
    """Links related to the space"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    webui: str | None = Field(default=None, description="Web UI link")
    """Web UI link"""
    base: str | None = Field(default=None, description="Base URL")
    """Base URL"""

class Space(BaseModel):
    """Confluence space object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    key: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    status: str | None = Field(default=None)
    author_id: str | None = Field(default=None, alias="authorId")
    created_at: str | None = Field(default=None, alias="createdAt")
    homepage_id: str | None = Field(default=None, alias="homepageId")
    space_owner_id: str | None = Field(default=None, alias="spaceOwnerId")
    current_active_alias: str | None = Field(default=None, alias="currentActiveAlias")
    description: Any | None = Field(default=None)
    icon: Any | None = Field(default=None)
    links: SpaceLinks | None = Field(default=None, alias="_links")

class SpacesListLinks(BaseModel):
    """Nested schema for SpacesList._links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None, description="URL for the next page of results")
    """URL for the next page of results"""
    base: str | None = Field(default=None, description="Base URL")
    """Base URL"""

class SpacesList(BaseModel):
    """Paginated list of spaces"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Space] | None = Field(default=None)
    links: SpacesListLinks | None = Field(default=None, alias="_links")

class PageBody(BaseModel):
    """Page body content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    storage: dict[str, Any] | None = Field(default=None, description="Storage format body")
    """Storage format body"""
    atlas_doc_format: dict[str, Any] | None = Field(default=None, description="Atlas doc format body")
    """Atlas doc format body"""

class PageLinks(BaseModel):
    """Links related to the page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    webui: str | None = Field(default=None, description="Web UI link")
    """Web UI link"""
    editui: str | None = Field(default=None, description="Edit UI link")
    """Edit UI link"""
    edituiv2: str | None = Field(default=None, description="Edit UI v2 link")
    """Edit UI v2 link"""
    tinyui: str | None = Field(default=None, description="Tiny UI link")
    """Tiny UI link"""
    base: str | None = Field(default=None, description="Base URL")
    """Base URL"""

class PageVersion(BaseModel):
    """Version information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str | None = Field(default=None, alias="createdAt", description="Version creation timestamp")
    """Version creation timestamp"""
    message: str | None = Field(default=None, description="Version message")
    """Version message"""
    number: int | None = Field(default=None, description="Version number")
    """Version number"""
    minor_edit: bool | None = Field(default=None, alias="minorEdit", description="Whether this was a minor edit")
    """Whether this was a minor edit"""
    author_id: str | None = Field(default=None, alias="authorId", description="ID of the version author")
    """ID of the version author"""
    ncs_step_version: Any | None = Field(default=None, alias="ncsStepVersion", description="NCS step version")
    """NCS step version"""

class Page(BaseModel):
    """Confluence page object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    status: str | None = Field(default=None)
    title: str | None = Field(default=None)
    space_id: str | None = Field(default=None, alias="spaceId")
    parent_id: Any | None = Field(default=None, alias="parentId")
    parent_type: Any | None = Field(default=None, alias="parentType")
    position: int | None = Field(default=None)
    author_id: str | None = Field(default=None, alias="authorId")
    owner_id: str | None = Field(default=None, alias="ownerId")
    last_owner_id: Any | None = Field(default=None, alias="lastOwnerId")
    created_at: str | None = Field(default=None, alias="createdAt")
    version: PageVersion | None = Field(default=None)
    body: PageBody | None = Field(default=None)
    links: PageLinks | None = Field(default=None, alias="_links")

class PagesListLinks(BaseModel):
    """Nested schema for PagesList._links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None, description="URL for the next page of results")
    """URL for the next page of results"""
    base: str | None = Field(default=None, description="Base URL")
    """Base URL"""

class PagesList(BaseModel):
    """Paginated list of pages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Page] | None = Field(default=None)
    links: PagesListLinks | None = Field(default=None, alias="_links")

class BlogPostVersion(BaseModel):
    """Version information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str | None = Field(default=None, alias="createdAt", description="Version creation timestamp")
    """Version creation timestamp"""
    message: str | None = Field(default=None, description="Version message")
    """Version message"""
    number: int | None = Field(default=None, description="Version number")
    """Version number"""
    minor_edit: bool | None = Field(default=None, alias="minorEdit", description="Whether this was a minor edit")
    """Whether this was a minor edit"""
    author_id: str | None = Field(default=None, alias="authorId", description="ID of the version author")
    """ID of the version author"""
    ncs_step_version: Any | None = Field(default=None, alias="ncsStepVersion", description="NCS step version")
    """NCS step version"""

class BlogPostLinks(BaseModel):
    """Links related to the blog post"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    webui: str | None = Field(default=None, description="Web UI link")
    """Web UI link"""
    editui: str | None = Field(default=None, description="Edit UI link")
    """Edit UI link"""
    edituiv2: str | None = Field(default=None, description="Edit UI v2 link")
    """Edit UI v2 link"""
    tinyui: str | None = Field(default=None, description="Tiny UI link")
    """Tiny UI link"""
    base: str | None = Field(default=None, description="Base URL")
    """Base URL"""

class BlogPostBody(BaseModel):
    """Blog post body content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    storage: dict[str, Any] | None = Field(default=None, description="Storage format body")
    """Storage format body"""
    atlas_doc_format: dict[str, Any] | None = Field(default=None, description="Atlas doc format body")
    """Atlas doc format body"""

class BlogPost(BaseModel):
    """Confluence blog post object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    status: str | None = Field(default=None)
    title: str | None = Field(default=None)
    space_id: str | None = Field(default=None, alias="spaceId")
    author_id: str | None = Field(default=None, alias="authorId")
    created_at: str | None = Field(default=None, alias="createdAt")
    version: BlogPostVersion | None = Field(default=None)
    body: BlogPostBody | None = Field(default=None)
    links: BlogPostLinks | None = Field(default=None, alias="_links")

class BlogPostsListLinks(BaseModel):
    """Nested schema for BlogPostsList._links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None, description="URL for the next page of results")
    """URL for the next page of results"""
    base: str | None = Field(default=None, description="Base URL")
    """Base URL"""

class BlogPostsList(BaseModel):
    """Paginated list of blog posts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[BlogPost] | None = Field(default=None)
    links: BlogPostsListLinks | None = Field(default=None, alias="_links")

class GroupLinks(BaseModel):
    """Links related to the group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="Self link")
    """Self link"""

class Group(BaseModel):
    """Confluence group object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    managed_by: str | None = Field(default=None, alias="managedBy")
    usage_type: str | None = Field(default=None, alias="usageType")
    resource_ari: str | None = Field(default=None, alias="resourceAri")
    links: GroupLinks | None = Field(default=None, alias="_links")

class GroupsListLinks(BaseModel):
    """Nested schema for GroupsList._links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: str | None = Field(default=None)
    context: str | None = Field(default=None)
    next: str | None = Field(default=None)
    self: str | None = Field(default=None)

class GroupsList(BaseModel):
    """Paginated list of groups"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Group] | None = Field(default=None)
    start: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    size: int | None = Field(default=None)
    links: GroupsListLinks | None = Field(default=None, alias="_links")

class AuditRecordAuthor(BaseModel):
    """User who triggered the audit event"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Author type")
    """Author type"""
    display_name: str | None = Field(default=None, alias="displayName", description="Display name of the author")
    """Display name of the author"""
    public_name: str | None = Field(default=None, alias="publicName", description="Public name of the author")
    """Public name of the author"""
    account_type: str | None = Field(default=None, alias="accountType", description="Account type")
    """Account type"""
    is_external_collaborator: bool | None = Field(default=None, alias="isExternalCollaborator", description="Whether the author is an external collaborator")
    """Whether the author is an external collaborator"""
    external_collaborator: bool | None = Field(default=None, alias="externalCollaborator", description="Whether the author is an external collaborator")
    """Whether the author is an external collaborator"""
    operations: Any | None = Field(default=None, description="Operations available for the author")
    """Operations available for the author"""

class AuditRecordAssociatedobjectsItem(BaseModel):
    """Nested schema for AuditRecord.associatedObjects_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the associated object")
    """Name of the associated object"""
    object_type: str | None = Field(default=None, alias="objectType", description="Type of the associated object")
    """Type of the associated object"""

class AuditRecordAffectedobject(BaseModel):
    """Object affected by the audit event"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the affected object")
    """Name of the affected object"""
    object_type: str | None = Field(default=None, alias="objectType", description="Type of the affected object")
    """Type of the affected object"""

class AuditRecord(BaseModel):
    """Confluence audit record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: AuditRecordAuthor | None = Field(default=None)
    remote_address: str | None = Field(default=None, alias="remoteAddress")
    creation_date: int | None = Field(default=None, alias="creationDate")
    summary: str | None = Field(default=None)
    description: str | None = Field(default=None)
    category: str | None = Field(default=None)
    sys_admin: bool | None = Field(default=None, alias="sysAdmin")
    super_admin: bool | None = Field(default=None, alias="superAdmin")
    affected_object: AuditRecordAffectedobject | None = Field(default=None, alias="affectedObject")
    changed_values: list[Any] | None = Field(default=None, alias="changedValues")
    associated_objects: list[AuditRecordAssociatedobjectsItem] | None = Field(default=None, alias="associatedObjects")

class AuditRecordsListLinks(BaseModel):
    """Nested schema for AuditRecordsList._links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base: str | None = Field(default=None)
    context: str | None = Field(default=None)
    next: str | None = Field(default=None)
    self: str | None = Field(default=None)

class AuditRecordsList(BaseModel):
    """Paginated list of audit records"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AuditRecord] | None = Field(default=None)
    start: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    size: int | None = Field(default=None)
    links: AuditRecordsListLinks | None = Field(default=None, alias="_links")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class SpacesListResultMeta(BaseModel):
    """Metadata for spaces.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class PagesListResultMeta(BaseModel):
    """Metadata for pages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class BlogPostsListResultMeta(BaseModel):
    """Metadata for blog_posts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class GroupsListResultMeta(BaseModel):
    """Metadata for groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)
    start: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    size: int | None = Field(default=None)

class AuditListResultMeta(BaseModel):
    """Metadata for audit.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)
    start: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    size: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ConfluenceCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class ConfluenceExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ConfluenceExecuteResultWithMeta(ConfluenceExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AuditSearchData(BaseModel):
    """Search result data for audit entity."""
    model_config = ConfigDict(extra="allow")

    affected_object: dict[str, Any] | None = None
    """The object that was affected by the audit event."""
    associated_objects: list[Any] | None = None
    """Any associated objects related to the audit event."""
    author: dict[str, Any] | None = None
    """The user who triggered the audit event."""
    category: str | None = None
    """The category under which the audit event falls."""
    changed_values: list[Any] | None = None
    """Details of the values that were changed during the audit event."""
    creation_date: int | None = None
    """The date and time when the audit event was created."""
    description: str | None = None
    """A detailed description of the audit event."""
    remote_address: str | None = None
    """The IP address from which the audit event originated."""
    summary: str | None = None
    """A brief summary or title describing the audit event."""
    super_admin: bool | None = None
    """Indicates if the user triggering the audit event is a super admin."""
    sys_admin: bool | None = None
    """Indicates if the user triggering the audit event is a system admin."""


class BlogPostsSearchData(BaseModel):
    """Search result data for blog_posts entity."""
    model_config = ConfigDict(extra="allow")

    links: dict[str, Any] | None = None
    """Links related to the blog post"""
    author_id: str | None = None
    """ID of the user who created the blog post"""
    body: dict[str, Any] | None = None
    """Blog post body content"""
    created_at: str | None = None
    """Timestamp when the blog post was created"""
    id: str | None = None
    """Unique blog post identifier"""
    space_id: str | None = None
    """ID of the space containing this blog post"""
    status: str | None = None
    """Blog post status (current, draft, trashed)"""
    title: str | None = None
    """Blog post title"""
    version: dict[str, Any] | None = None
    """Version information"""


class GroupsSearchData(BaseModel):
    """Search result data for groups entity."""
    model_config = ConfigDict(extra="allow")

    links: dict[str, Any] | None = None
    """Links related to the group"""
    id: str | None = None
    """The unique identifier of the group"""
    name: str | None = None
    """The name of the group"""
    type_: str | None = None
    """The type of group"""


class PagesSearchData(BaseModel):
    """Search result data for pages entity."""
    model_config = ConfigDict(extra="allow")

    links: dict[str, Any] | None = None
    """Links related to the page"""
    author_id: str | None = None
    """ID of the user who created the page"""
    body: dict[str, Any] | None = None
    """Page body content"""
    created_at: str | None = None
    """Timestamp when the page was created"""
    id: str | None = None
    """Unique page identifier"""
    last_owner_id: str | None = None
    """ID of the previous page owner"""
    owner_id: str | None = None
    """ID of the current page owner"""
    parent_id: str | None = None
    """ID of the parent page"""
    parent_type: str | None = None
    """Type of the parent (page or space)"""
    position: int | None = None
    """Position of the page among siblings"""
    space_id: str | None = None
    """ID of the space containing this page"""
    status: str | None = None
    """Page status (current, archived, trashed, draft)"""
    title: str | None = None
    """Page title"""
    version: dict[str, Any] | None = None
    """Version information"""


class SpacesSearchData(BaseModel):
    """Search result data for spaces entity."""
    model_config = ConfigDict(extra="allow")

    links: dict[str, Any] | None = None
    """Links related to the space"""
    author_id: str | None = None
    """ID of the user who created the space"""
    created_at: str | None = None
    """Timestamp when the space was created"""
    description: dict[str, Any] | None = None
    """Space description in various formats"""
    homepage_id: str | None = None
    """ID of the space homepage"""
    icon: dict[str, Any] | None = None
    """Space icon information"""
    id: str | None = None
    """Unique space identifier"""
    key: str | None = None
    """Space key"""
    name: str | None = None
    """Space name"""
    status: str | None = None
    """Space status (current or archived)"""
    type_: str | None = None
    """Space type (global or personal)"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

AuditSearchResult = AirbyteSearchResult[AuditSearchData]
"""Search result type for audit entity."""

BlogPostsSearchResult = AirbyteSearchResult[BlogPostsSearchData]
"""Search result type for blog_posts entity."""

GroupsSearchResult = AirbyteSearchResult[GroupsSearchData]
"""Search result type for groups entity."""

PagesSearchResult = AirbyteSearchResult[PagesSearchData]
"""Search result type for pages entity."""

SpacesSearchResult = AirbyteSearchResult[SpacesSearchData]
"""Search result type for spaces entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

SpacesListResult = ConfluenceExecuteResultWithMeta[list[Space], SpacesListResultMeta]
"""Result type for spaces.list operation with data and metadata."""

PagesListResult = ConfluenceExecuteResultWithMeta[list[Page], PagesListResultMeta]
"""Result type for pages.list operation with data and metadata."""

BlogPostsListResult = ConfluenceExecuteResultWithMeta[list[BlogPost], BlogPostsListResultMeta]
"""Result type for blog_posts.list operation with data and metadata."""

GroupsListResult = ConfluenceExecuteResultWithMeta[list[Group], GroupsListResultMeta]
"""Result type for groups.list operation with data and metadata."""

AuditListResult = ConfluenceExecuteResultWithMeta[list[AuditRecord], AuditListResultMeta]
"""Result type for audit.list operation with data and metadata."""

