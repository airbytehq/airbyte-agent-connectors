"""
Pydantic models for monday connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

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

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    birthday: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    join_date: str | None = Field(default=None)
    is_admin: bool | None = Field(default=None)
    is_guest: bool | None = Field(default=None)
    is_pending: bool | None = Field(default=None)
    is_view_only: bool | None = Field(default=None)
    is_verified: bool | None = Field(default=None)
    location: str | None = Field(default=None)
    mobile_phone: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    photo_original: str | None = Field(default=None)
    photo_small: str | None = Field(default=None)
    photo_thumb: str | None = Field(default=None)
    photo_thumb_small: str | None = Field(default=None)
    photo_tiny: str | None = Field(default=None)
    time_zone_identifier: str | None = Field(default=None)
    title: str | None = Field(default=None)
    url: str | None = Field(default=None)
    utc_hours_diff: int | None = Field(default=None)

class BoardSubscribersItem(BaseModel):
    """Nested schema for Board.subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class BoardTagsItem(BaseModel):
    """Nested schema for Board.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class BoardWorkspace(BaseModel):
    """Workspace the board belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    kind: str | None | None = Field(default=None)
    description: str | None | None = Field(default=None)

class BoardCreator(BaseModel):
    """Board creator"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class BoardTopGroup(BaseModel):
    """Top group on the board"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class BoardOwnersItem(BaseModel):
    """Nested schema for Board.owners_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class BoardViewsItem(BaseModel):
    """Nested schema for Board.views_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    settings_str: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    view_specific_data_str: str | None | None = Field(default=None)

class BoardColumnsItem(BaseModel):
    """Nested schema for Board.columns_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archived: bool | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    id: str | None | None = Field(default=None)
    settings_str: str | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    width: int | None | None = Field(default=None)

class BoardGroupsItem(BaseModel):
    """Nested schema for Board.groups_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archived: bool | None | None = Field(default=None)
    color: str | None | None = Field(default=None)
    deleted: bool | None | None = Field(default=None)
    id: str | None | None = Field(default=None)
    position: str | None | None = Field(default=None)
    title: str | None | None = Field(default=None)

class Board(BaseModel):
    """Monday.com board object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    board_kind: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    description: str | None = Field(default=None)
    permissions: str | None = Field(default=None)
    state: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    columns: list[BoardColumnsItem | None] | None = Field(default=None)
    groups: list[BoardGroupsItem | None] | None = Field(default=None)
    owners: list[BoardOwnersItem | None] | None = Field(default=None)
    creator: BoardCreator | None = Field(default=None)
    subscribers: list[BoardSubscribersItem | None] | None = Field(default=None)
    tags: list[BoardTagsItem | None] | None = Field(default=None)
    top_group: BoardTopGroup | None = Field(default=None)
    views: list[BoardViewsItem | None] | None = Field(default=None)
    workspace: BoardWorkspace | None = Field(default=None)

class ItemParentItem(BaseModel):
    """Parent item (for subitems)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class ItemColumnValuesItem(BaseModel):
    """Nested schema for Item.column_values_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    text: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class ItemSubscribersItem(BaseModel):
    """Nested schema for Item.subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class ItemBoard(BaseModel):
    """Board the item belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)

class ItemGroup(BaseModel):
    """Group the item belongs to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class Item(BaseModel):
    """Monday.com item object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    creator_id: str | None = Field(default=None)
    state: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    board: ItemBoard | None = Field(default=None)
    group: ItemGroup | None = Field(default=None)
    parent_item: ItemParentItem | None = Field(default=None)
    column_values: list[ItemColumnValuesItem | None] | None = Field(default=None)
    subscribers: list[ItemSubscribersItem | None] | None = Field(default=None)

class TeamUsersItem(BaseModel):
    """Nested schema for Team.users_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class Team(BaseModel):
    """Monday.com team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    picture_url: str | None = Field(default=None)
    users: list[TeamUsersItem | None] | None = Field(default=None)

class Tag(BaseModel):
    """Monday.com tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    color: str | None = Field(default=None)

class UpdateAssetsItemUploadedBy(BaseModel):
    """Nested schema for UpdateAssetsItem.uploaded_by"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class UpdateAssetsItem(BaseModel):
    """Nested schema for Update.assets_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    url: str | None | None = Field(default=None)
    url_thumbnail: str | None | None = Field(default=None)
    public_url: str | None | None = Field(default=None)
    file_extension: str | None | None = Field(default=None)
    file_size: int | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None)
    original_geometry: str | None | None = Field(default=None)
    uploaded_by: UpdateAssetsItemUploadedBy | None | None = Field(default=None)

class UpdateRepliesItem(BaseModel):
    """Nested schema for Update.replies_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    creator_id: str | None | None = Field(default=None)
    created_at: str | None | None = Field(default=None)
    text_body: str | None | None = Field(default=None)
    updated_at: str | None | None = Field(default=None)
    body: str | None | None = Field(default=None)

class Update(BaseModel):
    """Monday.com update (comment/post) object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    body: str | None = Field(default=None)
    text_body: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    creator_id: str | None = Field(default=None)
    item_id: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    replies: list[UpdateRepliesItem | None] | None = Field(default=None)
    assets: list[UpdateAssetsItem | None] | None = Field(default=None)

class WorkspaceTeamOwnersSubscribersItem(BaseModel):
    """Nested schema for Workspace.team_owners_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)

class WorkspaceTeamsSubscribersItem(BaseModel):
    """Nested schema for Workspace.teams_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)

class WorkspaceSettingsIcon(BaseModel):
    """Nested schema for WorkspaceSettings.icon"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None | None = Field(default=None)
    image: str | None | None = Field(default=None)

class WorkspaceSettings(BaseModel):
    """Workspace settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    icon: WorkspaceSettingsIcon | None | None = Field(default=None)

class WorkspaceOwnersSubscribersItem(BaseModel):
    """Nested schema for Workspace.owners_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class WorkspaceUsersSubscribersItem(BaseModel):
    """Nested schema for Workspace.users_subscribers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)

class WorkspaceAccountProduct(BaseModel):
    """Account product info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    kind: str | None | None = Field(default=None)

class Workspace(BaseModel):
    """Monday.com workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    kind: str | None = Field(default=None)
    description: str | None = Field(default=None)
    state: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    account_product: WorkspaceAccountProduct | None = Field(default=None)
    owners_subscribers: list[WorkspaceOwnersSubscribersItem | None] | None = Field(default=None)
    settings: WorkspaceSettings | None = Field(default=None)
    team_owners_subscribers: list[WorkspaceTeamOwnersSubscribersItem | None] | None = Field(default=None)
    teams_subscribers: list[WorkspaceTeamsSubscribersItem | None] | None = Field(default=None)
    users_subscribers: list[WorkspaceUsersSubscribersItem | None] | None = Field(default=None)

class ActivityLog(BaseModel):
    """Monday.com activity log entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    event: str | None = Field(default=None)
    data: str | None = Field(default=None)
    entity: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    user_id: str | None = Field(default=None)

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
    type_: str | None = None
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

UsersListResult = MondayExecuteResult[list[User]]
"""Result type for users.list operation."""

BoardsListResult = MondayExecuteResult[list[Board]]
"""Result type for boards.list operation."""

ItemsListResult = MondayExecuteResult[list[Item]]
"""Result type for items.list operation."""

TeamsListResult = MondayExecuteResult[list[Team]]
"""Result type for teams.list operation."""

TagsListResult = MondayExecuteResult[list[Tag]]
"""Result type for tags.list operation."""

UpdatesListResult = MondayExecuteResult[list[Update]]
"""Result type for updates.list operation."""

WorkspacesListResult = MondayExecuteResult[list[Workspace]]
"""Result type for workspaces.list operation."""

ActivityLogsListResult = MondayExecuteResult[list[ActivityLog]]
"""Result type for activity_logs.list operation."""

