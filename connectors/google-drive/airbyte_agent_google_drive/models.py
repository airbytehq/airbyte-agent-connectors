"""
Pydantic models for google-drive connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class GoogleDriveAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """Your Google OAuth2 Access Token (optional, will be obtained via refresh)"""
    refresh_token: str
    """Your Google OAuth2 Refresh Token"""
    client_id: str
    """Your Google OAuth2 Client ID"""
    client_secret: str
    """Your Google OAuth2 Client Secret"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class User(BaseModel):
    """Information about a Drive user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    display_name: Union[str | None, Any] = Field(default=None, alias="displayName")
    photo_link: Union[str | None, Any] = Field(default=None, alias="photoLink")
    me: Union[bool | None, Any] = Field(default=None)
    permission_id: Union[str | None, Any] = Field(default=None, alias="permissionId")
    email_address: Union[str | None, Any] = Field(default=None, alias="emailAddress")

class FileCapabilities(BaseModel):
    """Capabilities the current user has on this file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_edit: Union[bool | None, Any] = Field(default=None, alias="canEdit")
    can_comment: Union[bool | None, Any] = Field(default=None, alias="canComment")
    can_share: Union[bool | None, Any] = Field(default=None, alias="canShare")
    can_copy: Union[bool | None, Any] = Field(default=None, alias="canCopy")
    can_download: Union[bool | None, Any] = Field(default=None, alias="canDownload")
    can_delete: Union[bool | None, Any] = Field(default=None, alias="canDelete")
    can_rename: Union[bool | None, Any] = Field(default=None, alias="canRename")
    can_trash: Union[bool | None, Any] = Field(default=None, alias="canTrash")
    can_read_revisions: Union[bool | None, Any] = Field(default=None, alias="canReadRevisions")
    can_add_children: Union[bool | None, Any] = Field(default=None, alias="canAddChildren")
    can_list_children: Union[bool | None, Any] = Field(default=None, alias="canListChildren")
    can_remove_children: Union[bool | None, Any] = Field(default=None, alias="canRemoveChildren")

class FileImagemediametadataLocation(BaseModel):
    """Nested schema for FileImagemediametadata.location"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    latitude: Union[float | None, Any] = Field(default=None)
    longitude: Union[float | None, Any] = Field(default=None)
    altitude: Union[float | None, Any] = Field(default=None)

class FileImagemediametadata(BaseModel):
    """Additional metadata about image media"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    width: Union[int | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    rotation: Union[int | None, Any] = Field(default=None)
    time: Union[str | None, Any] = Field(default=None)
    camera_make: Union[str | None, Any] = Field(default=None, alias="cameraMake")
    camera_model: Union[str | None, Any] = Field(default=None, alias="cameraModel")
    exposure_time: Union[float | None, Any] = Field(default=None, alias="exposureTime")
    aperture: Union[float | None, Any] = Field(default=None)
    flash_used: Union[bool | None, Any] = Field(default=None, alias="flashUsed")
    focal_length: Union[float | None, Any] = Field(default=None, alias="focalLength")
    iso_speed: Union[int | None, Any] = Field(default=None, alias="isoSpeed")
    metering_mode: Union[str | None, Any] = Field(default=None, alias="meteringMode")
    sensor: Union[str | None, Any] = Field(default=None)
    exposure_mode: Union[str | None, Any] = Field(default=None, alias="exposureMode")
    color_space: Union[str | None, Any] = Field(default=None, alias="colorSpace")
    white_balance: Union[str | None, Any] = Field(default=None, alias="whiteBalance")
    exposure_bias: Union[float | None, Any] = Field(default=None, alias="exposureBias")
    max_aperture_value: Union[float | None, Any] = Field(default=None, alias="maxApertureValue")
    subject_distance: Union[int | None, Any] = Field(default=None, alias="subjectDistance")
    lens: Union[str | None, Any] = Field(default=None)
    location: Union[FileImagemediametadataLocation | None, Any] = Field(default=None)

class FileLabelinfo(BaseModel):
    """An overview of the labels on the file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    labels: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class FileShortcutdetails(BaseModel):
    """Shortcut file details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target_id: Union[str | None, Any] = Field(default=None, alias="targetId")
    target_mime_type: Union[str | None, Any] = Field(default=None, alias="targetMimeType")
    target_resource_key: Union[str | None, Any] = Field(default=None, alias="targetResourceKey")

class FileContentrestrictionsItem(BaseModel):
    """Nested schema for File.contentRestrictions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    read_only: Union[bool | None, Any] = Field(default=None, alias="readOnly")
    reason: Union[str | None, Any] = Field(default=None)
    restricting_user: Union[Any, Any] = Field(default=None, alias="restrictingUser")
    restriction_time: Union[str | None, Any] = Field(default=None, alias="restrictionTime")
    type: Union[str | None, Any] = Field(default=None)

class FileLinksharemetadata(BaseModel):
    """Contains details about the link URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    security_update_eligible: Union[bool | None, Any] = Field(default=None, alias="securityUpdateEligible")
    security_update_enabled: Union[bool | None, Any] = Field(default=None, alias="securityUpdateEnabled")

class FileVideomediametadata(BaseModel):
    """Additional metadata about video media"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    width: Union[int | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    duration_millis: Union[str | None, Any] = Field(default=None, alias="durationMillis")

class File(BaseModel):
    """The metadata for a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    mime_type: Union[str | None, Any] = Field(default=None, alias="mimeType")
    description: Union[str | None, Any] = Field(default=None)
    starred: Union[bool | None, Any] = Field(default=None)
    trashed: Union[bool | None, Any] = Field(default=None)
    explicitly_trashed: Union[bool | None, Any] = Field(default=None, alias="explicitlyTrashed")
    parents: Union[list[str] | None, Any] = Field(default=None)
    properties: Union[dict[str, str] | None, Any] = Field(default=None)
    app_properties: Union[dict[str, str] | None, Any] = Field(default=None, alias="appProperties")
    spaces: Union[list[str] | None, Any] = Field(default=None)
    version: Union[str | None, Any] = Field(default=None)
    web_content_link: Union[str | None, Any] = Field(default=None, alias="webContentLink")
    web_view_link: Union[str | None, Any] = Field(default=None, alias="webViewLink")
    icon_link: Union[str | None, Any] = Field(default=None, alias="iconLink")
    has_thumbnail: Union[bool | None, Any] = Field(default=None, alias="hasThumbnail")
    thumbnail_link: Union[str | None, Any] = Field(default=None, alias="thumbnailLink")
    thumbnail_version: Union[str | None, Any] = Field(default=None, alias="thumbnailVersion")
    viewed_by_me: Union[bool | None, Any] = Field(default=None, alias="viewedByMe")
    viewed_by_me_time: Union[str | None, Any] = Field(default=None, alias="viewedByMeTime")
    created_time: Union[str | None, Any] = Field(default=None, alias="createdTime")
    modified_time: Union[str | None, Any] = Field(default=None, alias="modifiedTime")
    modified_by_me_time: Union[str | None, Any] = Field(default=None, alias="modifiedByMeTime")
    modified_by_me: Union[bool | None, Any] = Field(default=None, alias="modifiedByMe")
    shared_with_me_time: Union[str | None, Any] = Field(default=None, alias="sharedWithMeTime")
    sharing_user: Union[Any, Any] = Field(default=None, alias="sharingUser")
    owners: Union[list[User] | None, Any] = Field(default=None)
    drive_id: Union[str | None, Any] = Field(default=None, alias="driveId")
    last_modifying_user: Union[Any, Any] = Field(default=None, alias="lastModifyingUser")
    shared: Union[bool | None, Any] = Field(default=None)
    owned_by_me: Union[bool | None, Any] = Field(default=None, alias="ownedByMe")
    capabilities: Union[FileCapabilities | None, Any] = Field(default=None)
    viewers_can_copy_content: Union[bool | None, Any] = Field(default=None, alias="viewersCanCopyContent")
    copy_requires_writer_permission: Union[bool | None, Any] = Field(default=None, alias="copyRequiresWriterPermission")
    writers_can_share: Union[bool | None, Any] = Field(default=None, alias="writersCanShare")
    permission_ids: Union[list[str] | None, Any] = Field(default=None, alias="permissionIds")
    folder_color_rgb: Union[str | None, Any] = Field(default=None, alias="folderColorRgb")
    original_filename: Union[str | None, Any] = Field(default=None, alias="originalFilename")
    full_file_extension: Union[str | None, Any] = Field(default=None, alias="fullFileExtension")
    file_extension: Union[str | None, Any] = Field(default=None, alias="fileExtension")
    md5_checksum: Union[str | None, Any] = Field(default=None, alias="md5Checksum")
    sha1_checksum: Union[str | None, Any] = Field(default=None, alias="sha1Checksum")
    sha256_checksum: Union[str | None, Any] = Field(default=None, alias="sha256Checksum")
    size: Union[str | None, Any] = Field(default=None)
    quota_bytes_used: Union[str | None, Any] = Field(default=None, alias="quotaBytesUsed")
    head_revision_id: Union[str | None, Any] = Field(default=None, alias="headRevisionId")
    is_app_authorized: Union[bool | None, Any] = Field(default=None, alias="isAppAuthorized")
    export_links: Union[dict[str, str] | None, Any] = Field(default=None, alias="exportLinks")
    shortcut_details: Union[FileShortcutdetails | None, Any] = Field(default=None, alias="shortcutDetails")
    content_restrictions: Union[list[FileContentrestrictionsItem] | None, Any] = Field(default=None, alias="contentRestrictions")
    resource_key: Union[str | None, Any] = Field(default=None, alias="resourceKey")
    link_share_metadata: Union[FileLinksharemetadata | None, Any] = Field(default=None, alias="linkShareMetadata")
    label_info: Union[FileLabelinfo | None, Any] = Field(default=None, alias="labelInfo")
    trashed_time: Union[str | None, Any] = Field(default=None, alias="trashedTime")
    trashing_user: Union[Any, Any] = Field(default=None, alias="trashingUser")
    image_media_metadata: Union[FileImagemediametadata | None, Any] = Field(default=None, alias="imageMediaMetadata")
    video_media_metadata: Union[FileVideomediametadata | None, Any] = Field(default=None, alias="videoMediaMetadata")

class FilesListResponse(BaseModel):
    """A list of files"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    incomplete_search: Union[bool | None, Any] = Field(default=None, alias="incompleteSearch")
    files: Union[list[File], Any] = Field(default=None)

class DriveBackgroundimagefile(BaseModel):
    """An image file and cropping parameters for the background image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    x_coordinate: Union[float | None, Any] = Field(default=None, alias="xCoordinate")
    y_coordinate: Union[float | None, Any] = Field(default=None, alias="yCoordinate")
    width: Union[float | None, Any] = Field(default=None)

class DriveCapabilities(BaseModel):
    """Capabilities the current user has on this shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_add_children: Union[bool | None, Any] = Field(default=None, alias="canAddChildren")
    can_comment: Union[bool | None, Any] = Field(default=None, alias="canComment")
    can_copy: Union[bool | None, Any] = Field(default=None, alias="canCopy")
    can_delete_drive: Union[bool | None, Any] = Field(default=None, alias="canDeleteDrive")
    can_download: Union[bool | None, Any] = Field(default=None, alias="canDownload")
    can_edit: Union[bool | None, Any] = Field(default=None, alias="canEdit")
    can_list_children: Union[bool | None, Any] = Field(default=None, alias="canListChildren")
    can_manage_members: Union[bool | None, Any] = Field(default=None, alias="canManageMembers")
    can_read_revisions: Union[bool | None, Any] = Field(default=None, alias="canReadRevisions")
    can_rename: Union[bool | None, Any] = Field(default=None, alias="canRename")
    can_rename_drive: Union[bool | None, Any] = Field(default=None, alias="canRenameDrive")
    can_change_drive_background: Union[bool | None, Any] = Field(default=None, alias="canChangeDriveBackground")
    can_share: Union[bool | None, Any] = Field(default=None, alias="canShare")
    can_change_copy_requires_writer_permission_restriction: Union[bool | None, Any] = Field(default=None, alias="canChangeCopyRequiresWriterPermissionRestriction")
    can_change_domain_users_only_restriction: Union[bool | None, Any] = Field(default=None, alias="canChangeDomainUsersOnlyRestriction")
    can_change_drive_members_only_restriction: Union[bool | None, Any] = Field(default=None, alias="canChangeDriveMembersOnlyRestriction")
    can_change_sharing_folders_requires_organizer_permission_restriction: Union[bool | None, Any] = Field(default=None, alias="canChangeSharingFoldersRequiresOrganizerPermissionRestriction")
    can_reset_drive_restrictions: Union[bool | None, Any] = Field(default=None, alias="canResetDriveRestrictions")
    can_delete_children: Union[bool | None, Any] = Field(default=None, alias="canDeleteChildren")
    can_trash_children: Union[bool | None, Any] = Field(default=None, alias="canTrashChildren")

class DriveRestrictions(BaseModel):
    """A set of restrictions that apply to this shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    copy_requires_writer_permission: Union[bool | None, Any] = Field(default=None, alias="copyRequiresWriterPermission")
    domain_users_only: Union[bool | None, Any] = Field(default=None, alias="domainUsersOnly")
    drive_members_only: Union[bool | None, Any] = Field(default=None, alias="driveMembersOnly")
    admin_managed_restrictions: Union[bool | None, Any] = Field(default=None, alias="adminManagedRestrictions")
    sharing_folders_requires_organizer_permission: Union[bool | None, Any] = Field(default=None, alias="sharingFoldersRequiresOrganizerPermission")

class Drive(BaseModel):
    """Representation of a shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    color_rgb: Union[str | None, Any] = Field(default=None, alias="colorRgb")
    background_image_link: Union[str | None, Any] = Field(default=None, alias="backgroundImageLink")
    background_image_file: Union[DriveBackgroundimagefile | None, Any] = Field(default=None, alias="backgroundImageFile")
    capabilities: Union[DriveCapabilities | None, Any] = Field(default=None)
    theme_id: Union[str | None, Any] = Field(default=None, alias="themeId")
    created_time: Union[str | None, Any] = Field(default=None, alias="createdTime")
    hidden: Union[bool | None, Any] = Field(default=None)
    restrictions: Union[DriveRestrictions | None, Any] = Field(default=None)
    org_unit_id: Union[str | None, Any] = Field(default=None, alias="orgUnitId")

class DrivesListResponse(BaseModel):
    """A list of shared drives"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    drives: Union[list[Drive], Any] = Field(default=None)

class PermissionTeamdrivepermissiondetailsItem(BaseModel):
    """Nested schema for Permission.teamDrivePermissionDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    team_drive_permission_type: Union[str | None, Any] = Field(default=None, alias="teamDrivePermissionType")
    role: Union[str | None, Any] = Field(default=None)
    inherited_from: Union[str | None, Any] = Field(default=None, alias="inheritedFrom")
    inherited: Union[bool | None, Any] = Field(default=None)

class PermissionPermissiondetailsItem(BaseModel):
    """Nested schema for Permission.permissionDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    permission_type: Union[str | None, Any] = Field(default=None, alias="permissionType")
    role: Union[str | None, Any] = Field(default=None)
    inherited_from: Union[str | None, Any] = Field(default=None, alias="inheritedFrom")
    inherited: Union[bool | None, Any] = Field(default=None)

class Permission(BaseModel):
    """A permission for a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    email_address: Union[str | None, Any] = Field(default=None, alias="emailAddress")
    domain: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    view: Union[str | None, Any] = Field(default=None)
    allow_file_discovery: Union[bool | None, Any] = Field(default=None, alias="allowFileDiscovery")
    display_name: Union[str | None, Any] = Field(default=None, alias="displayName")
    photo_link: Union[str | None, Any] = Field(default=None, alias="photoLink")
    expiration_time: Union[str | None, Any] = Field(default=None, alias="expirationTime")
    team_drive_permission_details: Union[list[PermissionTeamdrivepermissiondetailsItem] | None, Any] = Field(default=None, alias="teamDrivePermissionDetails")
    permission_details: Union[list[PermissionPermissiondetailsItem] | None, Any] = Field(default=None, alias="permissionDetails")
    deleted: Union[bool | None, Any] = Field(default=None)
    pending_owner: Union[bool | None, Any] = Field(default=None, alias="pendingOwner")

class PermissionsListResponse(BaseModel):
    """A list of permissions for a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    permissions: Union[list[Permission], Any] = Field(default=None)

class Reply(BaseModel):
    """A reply to a comment on a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None, alias="createdTime")
    modified_time: Union[str | None, Any] = Field(default=None, alias="modifiedTime")
    author: Union[Any, Any] = Field(default=None)
    html_content: Union[str | None, Any] = Field(default=None, alias="htmlContent")
    content: Union[str | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    action: Union[str | None, Any] = Field(default=None)

class CommentQuotedfilecontent(BaseModel):
    """The file content to which the comment refers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    mime_type: Union[str | None, Any] = Field(default=None, alias="mimeType")
    value: Union[str | None, Any] = Field(default=None)

class Comment(BaseModel):
    """A comment on a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None, alias="createdTime")
    modified_time: Union[str | None, Any] = Field(default=None, alias="modifiedTime")
    author: Union[Any, Any] = Field(default=None)
    html_content: Union[str | None, Any] = Field(default=None, alias="htmlContent")
    content: Union[str | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    resolved: Union[bool | None, Any] = Field(default=None)
    quoted_file_content: Union[CommentQuotedfilecontent | None, Any] = Field(default=None, alias="quotedFileContent")
    anchor: Union[str | None, Any] = Field(default=None)
    replies: Union[list[Reply] | None, Any] = Field(default=None)
    mentioned_email_addresses: Union[list[str] | None, Any] = Field(default=None, alias="mentionedEmailAddresses")
    assignee_email_address: Union[str | None, Any] = Field(default=None, alias="assigneeEmailAddress")

class CommentsListResponse(BaseModel):
    """A list of comments on a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    comments: Union[list[Comment], Any] = Field(default=None)

class RepliesListResponse(BaseModel):
    """A list of replies to a comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    replies: Union[list[Reply], Any] = Field(default=None)

class Revision(BaseModel):
    """The metadata for a revision to a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    mime_type: Union[str | None, Any] = Field(default=None, alias="mimeType")
    modified_time: Union[str | None, Any] = Field(default=None, alias="modifiedTime")
    keep_forever: Union[bool | None, Any] = Field(default=None, alias="keepForever")
    published: Union[bool | None, Any] = Field(default=None)
    published_link: Union[str | None, Any] = Field(default=None, alias="publishedLink")
    publish_auto: Union[bool | None, Any] = Field(default=None, alias="publishAuto")
    published_outside_domain: Union[bool | None, Any] = Field(default=None, alias="publishedOutsideDomain")
    last_modifying_user: Union[Any, Any] = Field(default=None, alias="lastModifyingUser")
    original_filename: Union[str | None, Any] = Field(default=None, alias="originalFilename")
    md5_checksum: Union[str | None, Any] = Field(default=None, alias="md5Checksum")
    size: Union[str | None, Any] = Field(default=None)
    export_links: Union[dict[str, str] | None, Any] = Field(default=None, alias="exportLinks")

class RevisionsListResponse(BaseModel):
    """A list of revisions of a file"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    revisions: Union[list[Revision], Any] = Field(default=None)

class Change(BaseModel):
    """A change to a file or shared drive"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    removed: Union[bool | None, Any] = Field(default=None)
    file: Union[Any, Any] = Field(default=None)
    file_id: Union[str | None, Any] = Field(default=None, alias="fileId")
    drive_id: Union[str | None, Any] = Field(default=None, alias="driveId")
    drive: Union[Any, Any] = Field(default=None)
    time: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    change_type: Union[str | None, Any] = Field(default=None, alias="changeType")

class ChangesListResponse(BaseModel):
    """A list of changes for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    new_start_page_token: Union[str | None, Any] = Field(default=None, alias="newStartPageToken")
    changes: Union[list[Change], Any] = Field(default=None)

class StartPageToken(BaseModel):
    """The starting page token for listing changes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    start_page_token: Union[str, Any] = Field(default=None, alias="startPageToken")

class AboutDrivethemesItem(BaseModel):
    """Nested schema for About.driveThemes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    background_image_link: Union[str | None, Any] = Field(default=None, alias="backgroundImageLink")
    color_rgb: Union[str | None, Any] = Field(default=None, alias="colorRgb")

class AboutTeamdrivethemesItem(BaseModel):
    """Nested schema for About.teamDriveThemes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    background_image_link: Union[str | None, Any] = Field(default=None, alias="backgroundImageLink")
    color_rgb: Union[str | None, Any] = Field(default=None, alias="colorRgb")

class AboutStoragequota(BaseModel):
    """The user's storage quota limits and usage"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    limit: Union[str | None, Any] = Field(default=None, description="The usage limit, if applicable")
    """The usage limit, if applicable"""
    usage: Union[str | None, Any] = Field(default=None, description="The total usage across all services")
    """The total usage across all services"""
    usage_in_drive: Union[str | None, Any] = Field(default=None, alias="usageInDrive", description="The usage by all files in Google Drive")
    """The usage by all files in Google Drive"""
    usage_in_drive_trash: Union[str | None, Any] = Field(default=None, alias="usageInDriveTrash", description="The usage by trashed files in Google Drive")
    """The usage by trashed files in Google Drive"""

class About(BaseModel):
    """Information about the user, the user's Drive, and system capabilities"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    kind: Union[str | None, Any] = Field(default=None)
    user: Union[Any, Any] = Field(default=None)
    storage_quota: Union[AboutStoragequota | None, Any] = Field(default=None, alias="storageQuota")
    import_formats: Union[dict[str, list[str]] | None, Any] = Field(default=None, alias="importFormats")
    export_formats: Union[dict[str, list[str]] | None, Any] = Field(default=None, alias="exportFormats")
    max_import_sizes: Union[dict[str, str] | None, Any] = Field(default=None, alias="maxImportSizes")
    max_upload_size: Union[str | None, Any] = Field(default=None, alias="maxUploadSize")
    app_installed: Union[bool | None, Any] = Field(default=None, alias="appInstalled")
    folder_color_palette: Union[list[str] | None, Any] = Field(default=None, alias="folderColorPalette")
    drive_themes: Union[list[AboutDrivethemesItem] | None, Any] = Field(default=None, alias="driveThemes")
    can_create_drives: Union[bool | None, Any] = Field(default=None, alias="canCreateDrives")
    can_create_team_drives: Union[bool | None, Any] = Field(default=None, alias="canCreateTeamDrives")
    team_drive_themes: Union[list[AboutTeamdrivethemesItem] | None, Any] = Field(default=None, alias="teamDriveThemes")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class FilesListResultMeta(BaseModel):
    """Metadata for files.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    incomplete_search: Union[bool | None, Any] = Field(default=None, alias="incompleteSearch")

class DrivesListResultMeta(BaseModel):
    """Metadata for drives.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")

class PermissionsListResultMeta(BaseModel):
    """Metadata for permissions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")

class RepliesListResultMeta(BaseModel):
    """Metadata for replies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")

class RevisionsListResultMeta(BaseModel):
    """Metadata for revisions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")

class ChangesListResultMeta(BaseModel):
    """Metadata for changes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    new_start_page_token: Union[str | None, Any] = Field(default=None, alias="newStartPageToken")

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

