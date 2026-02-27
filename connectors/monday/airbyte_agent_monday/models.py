"""
Pydantic models for monday connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration - multiple options available

class MondayOauth20AuthenticationAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Access token obtained via OAuth 2.0 flow"""
    client_id: str
    """The Client ID of your Monday.com OAuth application"""
    client_secret: str
    """The Client Secret of your Monday.com OAuth application"""

class MondayApiTokenAuthenticationAuthConfig(BaseModel):
    """API Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Monday.com personal API token"""

MondayAuthConfig = MondayOauth20AuthenticationAuthConfig | MondayApiTokenAuthenticationAuthConfig

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class User(BaseModel):
    """Monday.com user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    birthday: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    join_date: Union[str | None, Any] = Field(default=None)
    is_admin: Union[bool | None, Any] = Field(default=None)
    is_guest: Union[bool | None, Any] = Field(default=None)
    is_pending: Union[bool | None, Any] = Field(default=None)
    is_view_only: Union[bool | None, Any] = Field(default=None)
    is_verified: Union[bool | None, Any] = Field(default=None)
    location: Union[str | None, Any] = Field(default=None)
    mobile_phone: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    photo_original: Union[str | None, Any] = Field(default=None)
    photo_small: Union[str | None, Any] = Field(default=None)
    photo_thumb: Union[str | None, Any] = Field(default=None)
    photo_thumb_small: Union[str | None, Any] = Field(default=None)
    photo_tiny: Union[str | None, Any] = Field(default=None)
    time_zone_identifier: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    utc_hours_diff: Union[int | None, Any] = Field(default=None)

class BoardCreator(BaseModel):
    """Board creator"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class BoardViewsItem(BaseModel):
    """Nested schema for Board.views_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    settings_str: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    view_specific_data_str: Union[str | None, Any] = Field(default=None)

class BoardTagsItem(BaseModel):
    """Nested schema for Board.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class BoardOwnersItem(BaseModel):
    """Nested schema for Board.owners_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class BoardWorkspace(BaseModel):
    """Workspace the board belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    kind: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)

class BoardTopGroup(BaseModel):
    """Top group on the board"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class BoardGroupsItem(BaseModel):
    """Nested schema for Board.groups_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archived: Union[bool | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    position: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)

class BoardSubscribersItem(BaseModel):
    """Nested schema for Board.subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class BoardColumnsItem(BaseModel):
    """Nested schema for Board.columns_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archived: Union[bool | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    settings_str: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)

class Board(BaseModel):
    """Monday.com board object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    board_kind: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    permissions: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    columns: Union[list[BoardColumnsItem | None] | None, Any] = Field(default=None)
    groups: Union[list[BoardGroupsItem | None] | None, Any] = Field(default=None)
    owners: Union[list[BoardOwnersItem | None] | None, Any] = Field(default=None)
    creator: Union[BoardCreator | None, Any] = Field(default=None)
    subscribers: Union[list[BoardSubscribersItem | None] | None, Any] = Field(default=None)
    tags: Union[list[BoardTagsItem | None] | None, Any] = Field(default=None)
    top_group: Union[BoardTopGroup | None, Any] = Field(default=None)
    views: Union[list[BoardViewsItem | None] | None, Any] = Field(default=None)
    workspace: Union[BoardWorkspace | None, Any] = Field(default=None)

class ItemColumnValuesItem(BaseModel):
    """Nested schema for Item.column_values_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)

class ItemGroup(BaseModel):
    """Group the item belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class ItemBoard(BaseModel):
    """Board the item belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class ItemParentItem(BaseModel):
    """Parent item (for subitems)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class ItemSubscribersItem(BaseModel):
    """Nested schema for Item.subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class Item(BaseModel):
    """Monday.com item object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    creator_id: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    board: Union[ItemBoard | None, Any] = Field(default=None)
    group: Union[ItemGroup | None, Any] = Field(default=None)
    parent_item: Union[ItemParentItem | None, Any] = Field(default=None)
    column_values: Union[list[ItemColumnValuesItem | None] | None, Any] = Field(default=None)
    subscribers: Union[list[ItemSubscribersItem | None] | None, Any] = Field(default=None)

class TeamUsersItem(BaseModel):
    """Nested schema for Team.users_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class Team(BaseModel):
    """Monday.com team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    picture_url: Union[str | None, Any] = Field(default=None)
    users: Union[list[TeamUsersItem | None] | None, Any] = Field(default=None)

class Tag(BaseModel):
    """Monday.com tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class UpdateAssetsItemUploadedBy(BaseModel):
    """Nested schema for UpdateAssetsItem.uploaded_by"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class UpdateAssetsItem(BaseModel):
    """Nested schema for Update.assets_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    url_thumbnail: Union[str | None, Any] = Field(default=None)
    public_url: Union[str | None, Any] = Field(default=None)
    file_extension: Union[str | None, Any] = Field(default=None)
    file_size: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    original_geometry: Union[str | None, Any] = Field(default=None)
    uploaded_by: Union[UpdateAssetsItemUploadedBy | None, Any] = Field(default=None)

class UpdateRepliesItem(BaseModel):
    """Nested schema for Update.replies_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    creator_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    text_body: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)

class Update(BaseModel):
    """Monday.com update (comment/post) object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    text_body: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    creator_id: Union[str | None, Any] = Field(default=None)
    item_id: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    replies: Union[list[UpdateRepliesItem | None] | None, Any] = Field(default=None)
    assets: Union[list[UpdateAssetsItem | None] | None, Any] = Field(default=None)

class WorkspaceUsersSubscribersItem(BaseModel):
    """Nested schema for Workspace.users_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class WorkspaceTeamOwnersSubscribersItem(BaseModel):
    """Nested schema for Workspace.team_owners_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class WorkspaceOwnersSubscribersItem(BaseModel):
    """Nested schema for Workspace.owners_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class WorkspaceSettingsIcon(BaseModel):
    """Nested schema for WorkspaceSettings.icon"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: Union[str | None, Any] = Field(default=None)
    image: Union[str | None, Any] = Field(default=None)

class WorkspaceSettings(BaseModel):
    """Workspace settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    icon: Union[WorkspaceSettingsIcon | None, Any] = Field(default=None)

class WorkspaceAccountProduct(BaseModel):
    """Account product info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    kind: Union[str | None, Any] = Field(default=None)

class WorkspaceTeamsSubscribersItem(BaseModel):
    """Nested schema for Workspace.teams_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class Workspace(BaseModel):
    """Monday.com workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    kind: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    account_product: Union[WorkspaceAccountProduct | None, Any] = Field(default=None)
    owners_subscribers: Union[list[WorkspaceOwnersSubscribersItem | None] | None, Any] = Field(default=None)
    settings: Union[WorkspaceSettings | None, Any] = Field(default=None)
    team_owners_subscribers: Union[list[WorkspaceTeamOwnersSubscribersItem | None] | None, Any] = Field(default=None)
    teams_subscribers: Union[list[WorkspaceTeamsSubscribersItem | None] | None, Any] = Field(default=None)
    users_subscribers: Union[list[WorkspaceUsersSubscribersItem | None] | None, Any] = Field(default=None)

class ActivityLog(BaseModel):
    """Monday.com activity log entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    event: Union[str | None, Any] = Field(default=None)
    data: Union[str | None, Any] = Field(default=None)
    entity: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    user_id: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class MondayCheckResult(BaseModel):
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


class MondayExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class MondayExecuteResultWithMeta(MondayExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ActivityLogsSearchData(BaseModel):
    """Search result data for activity_logs entity."""
    model_config = ConfigDict(extra="allow")

    board_id: int | None = None
    """Board ID the activity belongs to"""
    created_at: str | None = None
    """When the activity occurred"""
    created_at_int: int | None = None
    """When the activity occurred (Unix timestamp)"""
    data: str | None = None
    """Event data (JSON string)"""
    entity: str | None = None
    """Entity type that was affected"""
    event: str | None = None
    """Event type"""
    id: str | None = None
    """Unique activity log identifier"""
    pulse_id: int | None = None
    """Item (pulse) ID the activity belongs to"""
    user_id: str | None = None
    """ID of the user who performed the action"""


class BoardsSearchData(BaseModel):
    """Search result data for boards entity."""
    model_config = ConfigDict(extra="allow")

    board_kind: str | None = None
    """Board kind (public, private, share)"""
    columns: list[Any] | None = None
    """Board columns"""
    communication: str | None = None
    """Board communication value"""
    creator: dict[str, Any] | None = None
    """Board creator"""
    description: str | None = None
    """Board description"""
    groups: list[Any] | None = None
    """Board groups"""
    id: str | None = None
    """Unique board identifier"""
    name: str | None = None
    """Board name"""
    owners: list[Any] | None = None
    """Board owners"""
    permissions: str | None = None
    """Board permissions"""
    state: str | None = None
    """Board state (active, archived, deleted)"""
    subscribers: list[Any] | None = None
    """Board subscribers"""
    tags: list[Any] | None = None
    """Board tags"""
    top_group: dict[str, Any] | None = None
    """Top group on the board"""
    type: str | None = None
    """Board type"""
    updated_at: str | None = None
    """When the board was last updated"""
    updated_at_int: int | None = None
    """When the board was last updated (Unix timestamp)"""
    updates: list[Any] | None = None
    """Board updates"""
    views: list[Any] | None = None
    """Board views"""
    workspace: dict[str, Any] | None = None
    """Workspace the board belongs to"""


class ItemsSearchData(BaseModel):
    """Search result data for items entity."""
    model_config = ConfigDict(extra="allow")

    assets: list[Any] | None = None
    """Files attached to the item"""
    board: dict[str, Any] | None = None
    """Board the item belongs to"""
    column_values: list[Any] | None = None
    """Item column values"""
    created_at: str | None = None
    """When the item was created"""
    creator_id: str | None = None
    """ID of the user who created the item"""
    group: dict[str, Any] | None = None
    """Group the item belongs to"""
    id: str | None = None
    """Unique item identifier"""
    name: str | None = None
    """Item name"""
    parent_item: dict[str, Any] | None = None
    """Parent item (for subitems)"""
    state: str | None = None
    """Item state (active, archived, deleted)"""
    subscribers: list[Any] | None = None
    """Item subscribers"""
    updated_at: str | None = None
    """When the item was last updated"""
    updated_at_int: int | None = None
    """When the item was last updated (Unix timestamp)"""
    updates: list[Any] | None = None
    """Item updates"""


class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")

    color: str | None = None
    """Tag color"""
    id: str | None = None
    """Unique tag identifier"""
    name: str | None = None
    """Tag name"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique team identifier"""
    name: str | None = None
    """Team name"""
    picture_url: str | None = None
    """Team picture URL"""
    users: list[Any] | None = None
    """Team members"""


class UpdatesSearchData(BaseModel):
    """Search result data for updates entity."""
    model_config = ConfigDict(extra="allow")

    assets: list[Any] | None = None
    """Files attached to this update"""
    body: str | None = None
    """Update body (HTML)"""
    created_at: str | None = None
    """When the update was created"""
    creator_id: str | None = None
    """ID of the user who created the update"""
    id: str | None = None
    """Unique update identifier"""
    item_id: str | None = None
    """ID of the item this update belongs to"""
    replies: list[Any] | None = None
    """Replies to this update"""
    text_body: str | None = None
    """Update body (plain text)"""
    updated_at: str | None = None
    """When the update was last modified"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    birthday: str | None = None
    """User's birthday"""
    country_code: str | None = None
    """User's country code"""
    created_at: str | None = None
    """When the user was created"""
    email: str | None = None
    """User's email address"""
    enabled: bool | None = None
    """Whether the user account is enabled"""
    id: str | None = None
    """Unique user identifier"""
    is_admin: bool | None = None
    """Whether the user is an admin"""
    is_guest: bool | None = None
    """Whether the user is a guest"""
    is_pending: bool | None = None
    """Whether the user is pending"""
    is_view_only: bool | None = None
    """Whether the user is view-only"""
    is_verified: bool | None = None
    """Whether the user is verified"""
    join_date: str | None = None
    """When the user joined"""
    location: str | None = None
    """User's location"""
    mobile_phone: str | None = None
    """User's mobile phone number"""
    name: str | None = None
    """User's display name"""
    phone: str | None = None
    """User's phone number"""
    photo_original: str | None = None
    """URL to original size photo"""
    photo_small: str | None = None
    """URL to small photo"""
    photo_thumb: str | None = None
    """URL to thumbnail photo"""
    photo_thumb_small: str | None = None
    """URL to small thumbnail photo"""
    photo_tiny: str | None = None
    """URL to tiny photo"""
    time_zone_identifier: str | None = None
    """User's timezone identifier"""
    title: str | None = None
    """User's job title"""
    url: str | None = None
    """User's Monday.com profile URL"""
    utc_hours_diff: int | None = None
    """UTC hours difference for the user's timezone"""


class WorkspacesSearchData(BaseModel):
    """Search result data for workspaces entity."""
    model_config = ConfigDict(extra="allow")

    account_product: dict[str, Any] | None = None
    """Account product info"""
    created_at: str | None = None
    """When the workspace was created"""
    description: str | None = None
    """Workspace description"""
    id: str | None = None
    """Unique workspace identifier"""
    kind: str | None = None
    """Workspace kind (open, closed)"""
    name: str | None = None
    """Workspace name"""
    owners_subscribers: list[Any] | None = None
    """Owner subscribers"""
    settings: dict[str, Any] | None = None
    """Workspace settings"""
    state: str | None = None
    """Workspace state"""
    team_owners_subscribers: list[Any] | None = None
    """Team owner subscribers"""
    teams_subscribers: list[Any] | None = None
    """Team subscribers"""
    users_subscribers: list[Any] | None = None
    """User subscribers"""


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

ActivityLogsSearchResult = AirbyteSearchResult[ActivityLogsSearchData]
"""Search result type for activity_logs entity."""

BoardsSearchResult = AirbyteSearchResult[BoardsSearchData]
"""Search result type for boards entity."""

ItemsSearchResult = AirbyteSearchResult[ItemsSearchData]
"""Search result type for items entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

UpdatesSearchResult = AirbyteSearchResult[UpdatesSearchData]
"""Search result type for updates entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

WorkspacesSearchResult = AirbyteSearchResult[WorkspacesSearchData]
"""Search result type for workspaces entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for users.list operation."""

BoardsListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for boards.list operation."""

ItemsListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for items.list operation."""

TeamsListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for teams.list operation."""

TagsListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for tags.list operation."""

UpdatesListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for updates.list operation."""

WorkspacesListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for workspaces.list operation."""

ActivityLogsListResult = MondayExecuteResult[dict[str, Any]]
"""Result type for activity_logs.list operation."""

