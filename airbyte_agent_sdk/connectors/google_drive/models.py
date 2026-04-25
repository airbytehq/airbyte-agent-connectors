"""
Pydantic models for google-drive connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration

class GoogleDriveAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """Your Google OAuth2 Access Token (optional, will be obtained via refresh)"""
    refresh_token: str
    """Your Google OAuth2 Refresh Token"""
    client_id: Optional[str] = None
    """Your Google OAuth2 Client ID"""
    client_secret: Optional[str] = None
    """Your Google OAuth2 Client Secret"""

# Replication configuration

class GoogleDriveReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Google Drive."""

    model_config = ConfigDict(extra="forbid")

    folder_url: str
    """URL for the Google Drive folder you want to sync (e.g., https://drive.google.com/drive/folders/YOUR-FOLDER-ID)"""
    streams: str
    """Configuration for file streams to sync from Google Drive"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class User(BaseModel):
    """Information about a Drive user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    display_name: str | None = Field(default=None, alias="displayName")
    photo_link: str | None = Field(default=None, alias="photoLink")
    me: bool | None = Field(default=None)
    permission_id: str | None = Field(default=None, alias="permissionId")
    email_address: str | None = Field(default=None, alias="emailAddress")

class FileLinksharemetadata(BaseModel):
    """Contains details about the link URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    security_update_eligible: bool | None | None = Field(default=None, alias="securityUpdateEligible")
    security_update_enabled: bool | None | None = Field(default=None, alias="securityUpdateEnabled")

class FileCapabilities(BaseModel):
    """Capabilities the current user has on this file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_edit: bool | None | None = Field(default=None, alias="canEdit")
    can_comment: bool | None | None = Field(default=None, alias="canComment")
    can_share: bool | None | None = Field(default=None, alias="canShare")
    can_copy: bool | None | None = Field(default=None, alias="canCopy")
    can_download: bool | None | None = Field(default=None, alias="canDownload")
    can_delete: bool | None | None = Field(default=None, alias="canDelete")
    can_rename: bool | None | None = Field(default=None, alias="canRename")
    can_trash: bool | None | None = Field(default=None, alias="canTrash")
    can_read_revisions: bool | None | None = Field(default=None, alias="canReadRevisions")
    can_add_children: bool | None | None = Field(default=None, alias="canAddChildren")
    can_list_children: bool | None | None = Field(default=None, alias="canListChildren")
    can_remove_children: bool | None | None = Field(default=None, alias="canRemoveChildren")

class FileContentrestrictionsItem(BaseModel):
    """Nested schema for File.contentRestrictions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    read_only: bool | None | None = Field(default=None, alias="readOnly")
    reason: str | None | None = Field(default=None)
    restricting_user: Any | None = Field(default=None, alias="restrictingUser")
    restriction_time: str | None | None = Field(default=None, alias="restrictionTime")
    type_: str | None | None = Field(default=None, alias="type")

class FileLabelinfo(BaseModel):
    """An overview of the labels on the file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    labels: list[dict[str, Any]] | None | None = Field(default=None)

class FileVideomediametadata(BaseModel):
    """Additional metadata about video media"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    width: int | None | None = Field(default=None)
    height: int | None | None = Field(default=None)
    duration_millis: str | None | None = Field(default=None, alias="durationMillis")

class FileShortcutdetails(BaseModel):
    """Shortcut file details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target_id: str | None | None = Field(default=None, alias="targetId")
    target_mime_type: str | None | None = Field(default=None, alias="targetMimeType")
    target_resource_key: str | None | None = Field(default=None, alias="targetResourceKey")

class FileImagemediametadataLocation(BaseModel):
    """Nested schema for FileImagemediametadata.location"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    latitude: float | None | None = Field(default=None)
    longitude: float | None | None = Field(default=None)
    altitude: float | None | None = Field(default=None)

class FileImagemediametadata(BaseModel):
    """Additional metadata about image media"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    width: int | None | None = Field(default=None)
    height: int | None | None = Field(default=None)
    rotation: int | None | None = Field(default=None)
    time: str | None | None = Field(default=None)
    camera_make: str | None | None = Field(default=None, alias="cameraMake")
    camera_model: str | None | None = Field(default=None, alias="cameraModel")
    exposure_time: float | None | None = Field(default=None, alias="exposureTime")
    aperture: float | None | None = Field(default=None)
    flash_used: bool | None | None = Field(default=None, alias="flashUsed")
    focal_length: float | None | None = Field(default=None, alias="focalLength")
    iso_speed: int | None | None = Field(default=None, alias="isoSpeed")
    metering_mode: str | None | None = Field(default=None, alias="meteringMode")
    sensor: str | None | None = Field(default=None)
    exposure_mode: str | None | None = Field(default=None, alias="exposureMode")
    color_space: str | None | None = Field(default=None, alias="colorSpace")
    white_balance: str | None | None = Field(default=None, alias="whiteBalance")
    exposure_bias: float | None | None = Field(default=None, alias="exposureBias")
    max_aperture_value: float | None | None = Field(default=None, alias="maxApertureValue")
    subject_distance: int | None | None = Field(default=None, alias="subjectDistance")
    lens: str | None | None = Field(default=None)
    location: FileImagemediametadataLocation | None | None = Field(default=None)

class File(BaseModel):
    """The metadata for a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    mime_type: str | None = Field(default=None, alias="mimeType")
    description: str | None = Field(default=None)
    starred: bool | None = Field(default=None)
    trashed: bool | None = Field(default=None)
    explicitly_trashed: bool | None = Field(default=None, alias="explicitlyTrashed")
    parents: list[str] | None = Field(default=None)
    properties: dict[str, str] | None = Field(default=None)
    app_properties: dict[str, str] | None = Field(default=None, alias="appProperties")
    spaces: list[str] | None = Field(default=None)
    version: str | None = Field(default=None)
    web_content_link: str | None = Field(default=None, alias="webContentLink")
    web_view_link: str | None = Field(default=None, alias="webViewLink")
    icon_link: str | None = Field(default=None, alias="iconLink")
    has_thumbnail: bool | None = Field(default=None, alias="hasThumbnail")
    thumbnail_link: str | None = Field(default=None, alias="thumbnailLink")
    thumbnail_version: str | None = Field(default=None, alias="thumbnailVersion")
    viewed_by_me: bool | None = Field(default=None, alias="viewedByMe")
    viewed_by_me_time: str | None = Field(default=None, alias="viewedByMeTime")
    created_time: str | None = Field(default=None, alias="createdTime")
    modified_time: str | None = Field(default=None, alias="modifiedTime")
    modified_by_me_time: str | None = Field(default=None, alias="modifiedByMeTime")
    modified_by_me: bool | None = Field(default=None, alias="modifiedByMe")
    shared_with_me_time: str | None = Field(default=None, alias="sharedWithMeTime")
    sharing_user: Any | None = Field(default=None, alias="sharingUser")
    owners: list[User] | None = Field(default=None)
    drive_id: str | None = Field(default=None, alias="driveId")
    last_modifying_user: Any | None = Field(default=None, alias="lastModifyingUser")
    shared: bool | None = Field(default=None)
    owned_by_me: bool | None = Field(default=None, alias="ownedByMe")
    capabilities: FileCapabilities | None = Field(default=None)
    viewers_can_copy_content: bool | None = Field(default=None, alias="viewersCanCopyContent")
    copy_requires_writer_permission: bool | None = Field(default=None, alias="copyRequiresWriterPermission")
    writers_can_share: bool | None = Field(default=None, alias="writersCanShare")
    permission_ids: list[str] | None = Field(default=None, alias="permissionIds")
    folder_color_rgb: str | None = Field(default=None, alias="folderColorRgb")
    original_filename: str | None = Field(default=None, alias="originalFilename")
    full_file_extension: str | None = Field(default=None, alias="fullFileExtension")
    file_extension: str | None = Field(default=None, alias="fileExtension")
    md5_checksum: str | None = Field(default=None, alias="md5Checksum")
    sha1_checksum: str | None = Field(default=None, alias="sha1Checksum")
    sha256_checksum: str | None = Field(default=None, alias="sha256Checksum")
    size: str | None = Field(default=None)
    quota_bytes_used: str | None = Field(default=None, alias="quotaBytesUsed")
    head_revision_id: str | None = Field(default=None, alias="headRevisionId")
    is_app_authorized: bool | None = Field(default=None, alias="isAppAuthorized")
    export_links: dict[str, str] | None = Field(default=None, alias="exportLinks")
    shortcut_details: FileShortcutdetails | None = Field(default=None, alias="shortcutDetails")
    content_restrictions: list[FileContentrestrictionsItem] | None = Field(default=None, alias="contentRestrictions")
    resource_key: str | None = Field(default=None, alias="resourceKey")
    link_share_metadata: FileLinksharemetadata | None = Field(default=None, alias="linkShareMetadata")
    label_info: FileLabelinfo | None = Field(default=None, alias="labelInfo")
    trashed_time: str | None = Field(default=None, alias="trashedTime")
    trashing_user: Any | None = Field(default=None, alias="trashingUser")
    image_media_metadata: FileImagemediametadata | None = Field(default=None, alias="imageMediaMetadata")
    video_media_metadata: FileVideomediametadata | None = Field(default=None, alias="videoMediaMetadata")

class FilesListResponse(BaseModel):
    """A list of files"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    incomplete_search: bool | None = Field(default=None, alias="incompleteSearch")
    files: list[File] | None = Field(default=None)

class FileCreateParams(BaseModel):
    """Parameters for creating a new file or folder"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    mime_type: str | None = Field(default=None, alias="mimeType")
    parents: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)

class FileUpdateParams(BaseModel):
    """Parameters for updating file metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    mime_type: str | None = Field(default=None, alias="mimeType")

class FileUploadParams(BaseModel):
    """Parameters for uploading a file with content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    file_content: str
    mime_type: str | None = Field(default=None, alias="mimeType")
    parents: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)
    file_mime_type: str | None = Field(default=None)

class DriveBackgroundimagefile(BaseModel):
    """An image file and cropping parameters for the background image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    x_coordinate: float | None | None = Field(default=None, alias="xCoordinate")
    y_coordinate: float | None | None = Field(default=None, alias="yCoordinate")
    width: float | None | None = Field(default=None)

class DriveRestrictions(BaseModel):
    """A set of restrictions that apply to this shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    copy_requires_writer_permission: bool | None | None = Field(default=None, alias="copyRequiresWriterPermission")
    domain_users_only: bool | None | None = Field(default=None, alias="domainUsersOnly")
    drive_members_only: bool | None | None = Field(default=None, alias="driveMembersOnly")
    admin_managed_restrictions: bool | None | None = Field(default=None, alias="adminManagedRestrictions")
    sharing_folders_requires_organizer_permission: bool | None | None = Field(default=None, alias="sharingFoldersRequiresOrganizerPermission")

class DriveCapabilities(BaseModel):
    """Capabilities the current user has on this shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_add_children: bool | None | None = Field(default=None, alias="canAddChildren")
    can_comment: bool | None | None = Field(default=None, alias="canComment")
    can_copy: bool | None | None = Field(default=None, alias="canCopy")
    can_delete_drive: bool | None | None = Field(default=None, alias="canDeleteDrive")
    can_download: bool | None | None = Field(default=None, alias="canDownload")
    can_edit: bool | None | None = Field(default=None, alias="canEdit")
    can_list_children: bool | None | None = Field(default=None, alias="canListChildren")
    can_manage_members: bool | None | None = Field(default=None, alias="canManageMembers")
    can_read_revisions: bool | None | None = Field(default=None, alias="canReadRevisions")
    can_rename: bool | None | None = Field(default=None, alias="canRename")
    can_rename_drive: bool | None | None = Field(default=None, alias="canRenameDrive")
    can_change_drive_background: bool | None | None = Field(default=None, alias="canChangeDriveBackground")
    can_share: bool | None | None = Field(default=None, alias="canShare")
    can_change_copy_requires_writer_permission_restriction: bool | None | None = Field(default=None, alias="canChangeCopyRequiresWriterPermissionRestriction")
    can_change_domain_users_only_restriction: bool | None | None = Field(default=None, alias="canChangeDomainUsersOnlyRestriction")
    can_change_drive_members_only_restriction: bool | None | None = Field(default=None, alias="canChangeDriveMembersOnlyRestriction")
    can_change_sharing_folders_requires_organizer_permission_restriction: bool | None | None = Field(default=None, alias="canChangeSharingFoldersRequiresOrganizerPermissionRestriction")
    can_reset_drive_restrictions: bool | None | None = Field(default=None, alias="canResetDriveRestrictions")
    can_delete_children: bool | None | None = Field(default=None, alias="canDeleteChildren")
    can_trash_children: bool | None | None = Field(default=None, alias="canTrashChildren")

class Drive(BaseModel):
    """Representation of a shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    color_rgb: str | None = Field(default=None, alias="colorRgb")
    background_image_link: str | None = Field(default=None, alias="backgroundImageLink")
    background_image_file: DriveBackgroundimagefile | None = Field(default=None, alias="backgroundImageFile")
    capabilities: DriveCapabilities | None = Field(default=None)
    theme_id: str | None = Field(default=None, alias="themeId")
    created_time: str | None = Field(default=None, alias="createdTime")
    hidden: bool | None = Field(default=None)
    restrictions: DriveRestrictions | None = Field(default=None)
    org_unit_id: str | None = Field(default=None, alias="orgUnitId")

class DrivesListResponse(BaseModel):
    """A list of shared drives"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    drives: list[Drive] | None = Field(default=None)

class PermissionPermissiondetailsItem(BaseModel):
    """Nested schema for Permission.permissionDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    permission_type: str | None | None = Field(default=None, alias="permissionType")
    role: str | None | None = Field(default=None)
    inherited_from: str | None | None = Field(default=None, alias="inheritedFrom")
    inherited: bool | None | None = Field(default=None)

class PermissionTeamdrivepermissiondetailsItem(BaseModel):
    """Nested schema for Permission.teamDrivePermissionDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    team_drive_permission_type: str | None | None = Field(default=None, alias="teamDrivePermissionType")
    role: str | None | None = Field(default=None)
    inherited_from: str | None | None = Field(default=None, alias="inheritedFrom")
    inherited: bool | None | None = Field(default=None)

class Permission(BaseModel):
    """A permission for a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    email_address: str | None = Field(default=None, alias="emailAddress")
    domain: str | None = Field(default=None)
    role: str | None = Field(default=None)
    view: str | None = Field(default=None)
    allow_file_discovery: bool | None = Field(default=None, alias="allowFileDiscovery")
    display_name: str | None = Field(default=None, alias="displayName")
    photo_link: str | None = Field(default=None, alias="photoLink")
    expiration_time: str | None = Field(default=None, alias="expirationTime")
    team_drive_permission_details: list[PermissionTeamdrivepermissiondetailsItem] | None = Field(default=None, alias="teamDrivePermissionDetails")
    permission_details: list[PermissionPermissiondetailsItem] | None = Field(default=None, alias="permissionDetails")
    deleted: bool | None = Field(default=None)
    pending_owner: bool | None = Field(default=None, alias="pendingOwner")

class PermissionsListResponse(BaseModel):
    """A list of permissions for a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    permissions: list[Permission] | None = Field(default=None)

class CommentQuotedfilecontent(BaseModel):
    """The file content to which the comment refers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    mime_type: str | None | None = Field(default=None, alias="mimeType")
    value: str | None | None = Field(default=None)

class Reply(BaseModel):
    """A reply to a comment on a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    id: str | None = Field(default=None)
    created_time: str | None = Field(default=None, alias="createdTime")
    modified_time: str | None = Field(default=None, alias="modifiedTime")
    author: Any | None = Field(default=None)
    html_content: str | None = Field(default=None, alias="htmlContent")
    content: str | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    action: str | None = Field(default=None)

class Comment(BaseModel):
    """A comment on a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    id: str | None = Field(default=None)
    created_time: str | None = Field(default=None, alias="createdTime")
    modified_time: str | None = Field(default=None, alias="modifiedTime")
    author: Any | None = Field(default=None)
    html_content: str | None = Field(default=None, alias="htmlContent")
    content: str | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    resolved: bool | None = Field(default=None)
    quoted_file_content: CommentQuotedfilecontent | None = Field(default=None, alias="quotedFileContent")
    anchor: str | None = Field(default=None)
    replies: list[Reply] | None = Field(default=None)
    mentioned_email_addresses: list[str] | None = Field(default=None, alias="mentionedEmailAddresses")
    assignee_email_address: str | None = Field(default=None, alias="assigneeEmailAddress")

class CommentsListResponse(BaseModel):
    """A list of comments on a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    comments: list[Comment] | None = Field(default=None)

class RepliesListResponse(BaseModel):
    """A list of replies to a comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    replies: list[Reply] | None = Field(default=None)

class Revision(BaseModel):
    """The metadata for a revision to a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    id: str | None = Field(default=None)
    mime_type: str | None = Field(default=None, alias="mimeType")
    modified_time: str | None = Field(default=None, alias="modifiedTime")
    keep_forever: bool | None = Field(default=None, alias="keepForever")
    published: bool | None = Field(default=None)
    published_link: str | None = Field(default=None, alias="publishedLink")
    publish_auto: bool | None = Field(default=None, alias="publishAuto")
    published_outside_domain: bool | None = Field(default=None, alias="publishedOutsideDomain")
    last_modifying_user: Any | None = Field(default=None, alias="lastModifyingUser")
    original_filename: str | None = Field(default=None, alias="originalFilename")
    md5_checksum: str | None = Field(default=None, alias="md5Checksum")
    size: str | None = Field(default=None)
    export_links: dict[str, str] | None = Field(default=None, alias="exportLinks")

class RevisionsListResponse(BaseModel):
    """A list of revisions of a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    revisions: list[Revision] | None = Field(default=None)

class Change(BaseModel):
    """A change to a file or shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    removed: bool | None = Field(default=None)
    file: Any | None = Field(default=None)
    file_id: str | None = Field(default=None, alias="fileId")
    drive_id: str | None = Field(default=None, alias="driveId")
    drive: Any | None = Field(default=None)
    time: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    change_type: str | None = Field(default=None, alias="changeType")

class ChangesListResponse(BaseModel):
    """A list of changes for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    new_start_page_token: str | None = Field(default=None, alias="newStartPageToken")
    changes: list[Change] | None = Field(default=None)

class StartPageToken(BaseModel):
    """The starting page token for listing changes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    start_page_token: str | None = Field(default=None, alias="startPageToken")

class AboutTeamdrivethemesItem(BaseModel):
    """Nested schema for About.teamDriveThemes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    background_image_link: str | None | None = Field(default=None, alias="backgroundImageLink")
    color_rgb: str | None | None = Field(default=None, alias="colorRgb")

class AboutStoragequota(BaseModel):
    """The user's storage quota limits and usage"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    limit: str | None | None = Field(default=None, description="The usage limit, if applicable")
    """The usage limit, if applicable"""
    usage: str | None | None = Field(default=None, description="The total usage across all services")
    """The total usage across all services"""
    usage_in_drive: str | None | None = Field(default=None, alias="usageInDrive", description="The usage by all files in Google Drive")
    """The usage by all files in Google Drive"""
    usage_in_drive_trash: str | None | None = Field(default=None, alias="usageInDriveTrash", description="The usage by trashed files in Google Drive")
    """The usage by trashed files in Google Drive"""

class AboutDrivethemesItem(BaseModel):
    """Nested schema for About.driveThemes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    background_image_link: str | None | None = Field(default=None, alias="backgroundImageLink")
    color_rgb: str | None | None = Field(default=None, alias="colorRgb")

class About(BaseModel):
    """Information about the user, the user's Drive, and system capabilities"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: str | None = Field(default=None)
    user: Any | None = Field(default=None)
    storage_quota: AboutStoragequota | None = Field(default=None, alias="storageQuota")
    import_formats: dict[str, list[str]] | None = Field(default=None, alias="importFormats")
    export_formats: dict[str, list[str]] | None = Field(default=None, alias="exportFormats")
    max_import_sizes: dict[str, str] | None = Field(default=None, alias="maxImportSizes")
    max_upload_size: str | None = Field(default=None, alias="maxUploadSize")
    app_installed: bool | None = Field(default=None, alias="appInstalled")
    folder_color_palette: list[str] | None = Field(default=None, alias="folderColorPalette")
    drive_themes: list[AboutDrivethemesItem] | None = Field(default=None, alias="driveThemes")
    can_create_drives: bool | None = Field(default=None, alias="canCreateDrives")
    can_create_team_drives: bool | None = Field(default=None, alias="canCreateTeamDrives")
    team_drive_themes: list[AboutTeamdrivethemesItem] | None = Field(default=None, alias="teamDriveThemes")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class FilesListResultMeta(BaseModel):
    """Metadata for files.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    incomplete_search: bool | None = Field(default=None, alias="incompleteSearch")

class DrivesListResultMeta(BaseModel):
    """Metadata for drives.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class PermissionsListResultMeta(BaseModel):
    """Metadata for permissions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class RepliesListResultMeta(BaseModel):
    """Metadata for replies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class RevisionsListResultMeta(BaseModel):
    """Metadata for revisions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")

class ChangesListResultMeta(BaseModel):
    """Metadata for changes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: str | None = Field(default=None, alias="nextPageToken")
    new_start_page_token: str | None = Field(default=None, alias="newStartPageToken")

# ===== CHECK RESULT MODEL =====

class GoogleDriveCheckResult(BaseModel):
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


class GoogleDriveExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GoogleDriveExecuteResultWithMeta(GoogleDriveExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

FilesListResult = GoogleDriveExecuteResultWithMeta[list[File], FilesListResultMeta]
"""Result type for files.list operation with data and metadata."""

DrivesListResult = GoogleDriveExecuteResultWithMeta[list[Drive], DrivesListResultMeta]
"""Result type for drives.list operation with data and metadata."""

PermissionsListResult = GoogleDriveExecuteResultWithMeta[list[Permission], PermissionsListResultMeta]
"""Result type for permissions.list operation with data and metadata."""

CommentsListResult = GoogleDriveExecuteResultWithMeta[list[Comment], CommentsListResultMeta]
"""Result type for comments.list operation with data and metadata."""

RepliesListResult = GoogleDriveExecuteResultWithMeta[list[Reply], RepliesListResultMeta]
"""Result type for replies.list operation with data and metadata."""

RevisionsListResult = GoogleDriveExecuteResultWithMeta[list[Revision], RevisionsListResultMeta]
"""Result type for revisions.list operation with data and metadata."""

ChangesListResult = GoogleDriveExecuteResultWithMeta[list[Change], ChangesListResultMeta]
"""Result type for changes.list operation with data and metadata."""

