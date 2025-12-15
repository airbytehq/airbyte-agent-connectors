"""
Pydantic models for jira connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class JiraAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    username: str
    """Authentication username"""
    password: str
    """Authentication password"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ProjectLeadAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class ProjectLead(BaseModel):
    """Project lead user (available with expand=lead)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")
    avatar_urls: Union[ProjectLeadAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)

class ProjectIssuetypesItem(BaseModel):
    """Nested schema for Project.issueTypes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    icon_url: Union[str, Any] = Field(default=None, alias="iconUrl")
    name: Union[str, Any] = Field(default=None)
    subtask: Union[bool, Any] = Field(default=None)
    avatar_id: Union[int | None, Any] = Field(default=None, alias="avatarId")
    hierarchy_level: Union[int | None, Any] = Field(default=None, alias="hierarchyLevel")

class ProjectProjectcategory(BaseModel):
    """Project category information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)

class ProjectVersionsItem(BaseModel):
    """Nested schema for Project.versions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    released: Union[bool, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None, alias="startDate")
    release_date: Union[str | None, Any] = Field(default=None, alias="releaseDate")
    overdue: Union[bool | None, Any] = Field(default=None)
    user_start_date: Union[str | None, Any] = Field(default=None, alias="userStartDate")
    user_release_date: Union[str | None, Any] = Field(default=None, alias="userReleaseDate")
    project_id: Union[int, Any] = Field(default=None, alias="projectId")

class ProjectComponentsItem(BaseModel):
    """Nested schema for Project.components_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    is_assignee_type_valid: Union[bool, Any] = Field(default=None, alias="isAssigneeTypeValid")

class ProjectAvatarurls(BaseModel):
    """URLs for project avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class Project(BaseModel):
    """Jira project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    key: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    self: Union[str, Any] = Field(default=None)
    expand: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    lead: Union[ProjectLead | None, Any] = Field(default=None)
    avatar_urls: Union[ProjectAvatarurls, Any] = Field(default=None, alias="avatarUrls")
    project_type_key: Union[str, Any] = Field(default=None, alias="projectTypeKey")
    simplified: Union[bool, Any] = Field(default=None)
    style: Union[str, Any] = Field(default=None)
    is_private: Union[bool, Any] = Field(default=None, alias="isPrivate")
    properties: Union[dict[str, Any], Any] = Field(default=None)
    project_category: Union[ProjectProjectcategory | None, Any] = Field(default=None, alias="projectCategory")
    entity_id: Union[str | None, Any] = Field(default=None, alias="entityId")
    uuid: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    assignee_type: Union[str | None, Any] = Field(default=None, alias="assigneeType")
    components: Union[list[ProjectComponentsItem] | None, Any] = Field(default=None)
    issue_types: Union[list[ProjectIssuetypesItem] | None, Any] = Field(default=None, alias="issueTypes")
    versions: Union[list[ProjectVersionsItem] | None, Any] = Field(default=None)
    roles: Union[dict[str, str] | None, Any] = Field(default=None)

class ProjectsList(BaseModel):
    """Paginated list of projects from search results"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None, alias="nextPage")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    total: Union[int, Any] = Field(default=None)
    is_last: Union[bool, Any] = Field(default=None, alias="isLast")
    values: Union[list[Project], Any] = Field(default=None)

class IssueFieldsReporterAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class IssueFieldsReporter(BaseModel):
    """Issue reporter user information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    avatar_urls: Union[IssueFieldsReporterAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")

class IssueFieldsProjectAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class IssueFieldsProjectProjectcategory(BaseModel):
    """Nested schema for IssueFieldsProject.projectCategory"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)

class IssueFieldsProject(BaseModel):
    """Project information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    key: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    project_type_key: Union[str, Any] = Field(default=None, alias="projectTypeKey")
    simplified: Union[bool, Any] = Field(default=None)
    avatar_urls: Union[IssueFieldsProjectAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""
    project_category: Union[IssueFieldsProjectProjectcategory | None, Any] = Field(default=None, alias="projectCategory")

class IssueFieldsAssigneeAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class IssueFieldsAssignee(BaseModel):
    """Issue assignee user information (null if unassigned)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    avatar_urls: Union[IssueFieldsAssigneeAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")

class IssueFieldsPriority(BaseModel):
    """Issue priority information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    icon_url: Union[str, Any] = Field(default=None, alias="iconUrl")
    name: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)

class IssueFieldsStatusStatuscategory(BaseModel):
    """Nested schema for IssueFieldsStatus.statusCategory"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    key: Union[str, Any] = Field(default=None)
    color_name: Union[str, Any] = Field(default=None, alias="colorName")
    name: Union[str, Any] = Field(default=None)

class IssueFieldsStatus(BaseModel):
    """Issue status information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    icon_url: Union[str, Any] = Field(default=None, alias="iconUrl")
    name: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    status_category: Union[IssueFieldsStatusStatuscategory, Any] = Field(default=None, alias="statusCategory")

class IssueFieldsIssuetype(BaseModel):
    """Issue type information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    icon_url: Union[str, Any] = Field(default=None, alias="iconUrl")
    name: Union[str, Any] = Field(default=None)
    subtask: Union[bool, Any] = Field(default=None)
    avatar_id: Union[int | None, Any] = Field(default=None, alias="avatarId")
    hierarchy_level: Union[int | None, Any] = Field(default=None, alias="hierarchyLevel")

class IssueFields(BaseModel):
    """Issue fields (actual fields depend on 'fields' parameter in request)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    summary: Union[str, Any] = Field(default=None, description="Issue summary/title")
    """Issue summary/title"""
    issuetype: Union[IssueFieldsIssuetype, Any] = Field(default=None, description="Issue type information")
    """Issue type information"""
    created: Union[str, Any] = Field(default=None, description="Issue creation timestamp")
    """Issue creation timestamp"""
    updated: Union[str, Any] = Field(default=None, description="Issue last update timestamp")
    """Issue last update timestamp"""
    project: Union[IssueFieldsProject, Any] = Field(default=None, description="Project information")
    """Project information"""
    reporter: Union[IssueFieldsReporter | None, Any] = Field(default=None, description="Issue reporter user information")
    """Issue reporter user information"""
    assignee: Union[IssueFieldsAssignee | None, Any] = Field(default=None, description="Issue assignee user information (null if unassigned)")
    """Issue assignee user information (null if unassigned)"""
    priority: Union[IssueFieldsPriority | None, Any] = Field(default=None, description="Issue priority information")
    """Issue priority information"""
    status: Union[IssueFieldsStatus, Any] = Field(default=None, description="Issue status information")
    """Issue status information"""

class Issue(BaseModel):
    """Jira issue object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    key: Union[str, Any] = Field(default=None)
    self: Union[str, Any] = Field(default=None)
    expand: Union[str | None, Any] = Field(default=None)
    fields: Union[IssueFields, Any] = Field(default=None)

class IssuesList(BaseModel):
    """Paginated list of issues from JQL search"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issues: Union[list[Issue], Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)
    max_results: Union[int | None, Any] = Field(default=None, alias="maxResults")
    start_at: Union[int | None, Any] = Field(default=None, alias="startAt")
    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    is_last: Union[bool | None, Any] = Field(default=None, alias="isLast")

class UserGroupsItemsItem(BaseModel):
    """Nested schema for UserGroups.items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    group_id: Union[str, Any] = Field(default=None, alias="groupId")
    self: Union[str, Any] = Field(default=None)

class UserGroups(BaseModel):
    """User groups (available with expand=groups)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    size: Union[int, Any] = Field(default=None, description="Number of groups")
    """Number of groups"""
    items: Union[list[UserGroupsItemsItem], Any] = Field(default=None, description="Array of group objects")
    """Array of group objects"""

class UserApplicationrolesItemsItemGroupdetailsItem(BaseModel):
    """Nested schema for UserApplicationrolesItemsItem.groupDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    group_id: Union[str, Any] = Field(default=None, alias="groupId")
    self: Union[str, Any] = Field(default=None)

class UserApplicationrolesItemsItemDefaultgroupsdetailsItem(BaseModel):
    """Nested schema for UserApplicationrolesItemsItem.defaultGroupsDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    group_id: Union[str, Any] = Field(default=None, alias="groupId")
    self: Union[str, Any] = Field(default=None)

class UserApplicationrolesItemsItem(BaseModel):
    """Nested schema for UserApplicationroles.items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    groups: Union[list[str], Any] = Field(default=None)
    group_details: Union[list[UserApplicationrolesItemsItemGroupdetailsItem], Any] = Field(default=None, alias="groupDetails")
    default_groups: Union[list[str], Any] = Field(default=None, alias="defaultGroups")
    default_groups_details: Union[list[UserApplicationrolesItemsItemDefaultgroupsdetailsItem], Any] = Field(default=None, alias="defaultGroupsDetails")
    selected_by_default: Union[bool, Any] = Field(default=None, alias="selectedByDefault")
    defined: Union[bool, Any] = Field(default=None)
    number_of_seats: Union[int, Any] = Field(default=None, alias="numberOfSeats")
    remaining_seats: Union[int, Any] = Field(default=None, alias="remainingSeats")
    user_count: Union[int, Any] = Field(default=None, alias="userCount")
    user_count_description: Union[str, Any] = Field(default=None, alias="userCountDescription")
    has_unlimited_seats: Union[bool, Any] = Field(default=None, alias="hasUnlimitedSeats")
    platform: Union[bool, Any] = Field(default=None)

class UserApplicationroles(BaseModel):
    """User application roles (available with expand=applicationRoles)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    size: Union[int, Any] = Field(default=None, description="Number of application roles")
    """Number of application roles"""
    items: Union[list[UserApplicationrolesItemsItem], Any] = Field(default=None, description="Array of application role objects")
    """Array of application role objects"""

class UserAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class User(BaseModel):
    """Jira user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")
    email_address: Union[str | None, Any] = Field(default=None, alias="emailAddress")
    avatar_urls: Union[UserAvatarurls, Any] = Field(default=None, alias="avatarUrls")
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str | None, Any] = Field(default=None, alias="timeZone")
    locale: Union[str | None, Any] = Field(default=None)
    expand: Union[str | None, Any] = Field(default=None)
    groups: Union[UserGroups | None, Any] = Field(default=None)
    application_roles: Union[UserApplicationroles | None, Any] = Field(default=None, alias="applicationRoles")

class IssueFieldSchema(BaseModel):
    """Schema information for the field"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Field type (e.g., string, number, array)")
    """Field type (e.g., string, number, array)"""
    system: Union[str | None, Any] = Field(default=None, description="System field identifier")
    """System field identifier"""
    items: Union[str | None, Any] = Field(default=None, description="Type of items in array fields")
    """Type of items in array fields"""
    custom: Union[str | None, Any] = Field(default=None, description="Custom field type identifier")
    """Custom field type identifier"""
    custom_id: Union[int | None, Any] = Field(default=None, alias="customId", description="Custom field ID")
    """Custom field ID"""
    configuration: Union[dict[str, Any] | None, Any] = Field(default=None, description="Field configuration")
    """Field configuration"""

class IssueField(BaseModel):
    """Jira issue field object (custom or system field)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    custom: Union[bool | None, Any] = Field(default=None)
    orderable: Union[bool | None, Any] = Field(default=None)
    navigable: Union[bool | None, Any] = Field(default=None)
    searchable: Union[bool | None, Any] = Field(default=None)
    clause_names: Union[list[str] | None, Any] = Field(default=None, alias="clauseNames")
    schema: Union[IssueFieldSchema | None, Any] = Field(default=None)
    untranslated_name: Union[str | None, Any] = Field(default=None, alias="untranslatedName")
    type_display_name: Union[str | None, Any] = Field(default=None, alias="typeDisplayName")
    description: Union[str | None, Any] = Field(default=None)
    searcher_key: Union[str | None, Any] = Field(default=None, alias="searcherKey")
    screens_count: Union[int | None, Any] = Field(default=None, alias="screensCount")
    contexts_count: Union[int | None, Any] = Field(default=None, alias="contextsCount")
    is_locked: Union[bool | None, Any] = Field(default=None, alias="isLocked")
    last_used: Union[str | None, Any] = Field(default=None, alias="lastUsed")

class IssueFieldSearchResults(BaseModel):
    """Paginated search results for issue fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    total: Union[int, Any] = Field(default=None)
    is_last: Union[bool, Any] = Field(default=None, alias="isLast")
    values: Union[list[IssueField], Any] = Field(default=None)

class IssueCommentUpdateauthorAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class IssueCommentUpdateauthor(BaseModel):
    """User who last updated the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")
    avatar_urls: Union[IssueCommentUpdateauthorAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""

class IssueCommentVisibility(BaseModel):
    """Visibility restrictions for the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    value: Union[str, Any] = Field(default=None)
    identifier: Union[str | None, Any] = Field(default=None)

class IssueCommentBodyContentItemContentItem(BaseModel):
    """Nested schema for IssueCommentBodyContentItem.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Content type (e.g., 'text')")
    """Content type (e.g., 'text')"""
    text: Union[str, Any] = Field(default=None, description="Text content")
    """Text content"""

class IssueCommentBodyContentItem(BaseModel):
    """Nested schema for IssueCommentBody.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Block type (e.g., 'paragraph')")
    """Block type (e.g., 'paragraph')"""
    content: Union[list[IssueCommentBodyContentItemContentItem], Any] = Field(default=None, description="Nested content items")
    """Nested content items"""

class IssueCommentBody(BaseModel):
    """Comment content in ADF (Atlassian Document Format)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Document type (always 'doc')")
    """Document type (always 'doc')"""
    version: Union[int, Any] = Field(default=None, description="ADF version")
    """ADF version"""
    content: Union[list[IssueCommentBodyContentItem], Any] = Field(default=None, description="Array of content blocks")
    """Array of content blocks"""

class IssueCommentAuthorAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class IssueCommentAuthor(BaseModel):
    """Comment author user information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")
    avatar_urls: Union[IssueCommentAuthorAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""

class IssueComment(BaseModel):
    """Jira issue comment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    self: Union[str, Any] = Field(default=None)
    body: Union[IssueCommentBody, Any] = Field(default=None)
    author: Union[IssueCommentAuthor, Any] = Field(default=None)
    update_author: Union[IssueCommentUpdateauthor, Any] = Field(default=None, alias="updateAuthor")
    created: Union[str, Any] = Field(default=None)
    updated: Union[str, Any] = Field(default=None)
    jsd_public: Union[bool, Any] = Field(default=None, alias="jsdPublic")
    visibility: Union[IssueCommentVisibility | None, Any] = Field(default=None)
    rendered_body: Union[str | None, Any] = Field(default=None, alias="renderedBody")
    properties: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class IssueCommentsList(BaseModel):
    """Paginated list of issue comments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    total: Union[int, Any] = Field(default=None)
    comments: Union[list[IssueComment], Any] = Field(default=None)

class WorklogUpdateauthorAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class WorklogUpdateauthor(BaseModel):
    """User who last updated the worklog"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")
    avatar_urls: Union[WorklogUpdateauthorAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""

class WorklogVisibility(BaseModel):
    """Visibility restrictions for the worklog"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    value: Union[str, Any] = Field(default=None)
    identifier: Union[str | None, Any] = Field(default=None)

class WorklogAuthorAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class WorklogAuthor(BaseModel):
    """Worklog author user information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None, alias="accountId")
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    display_name: Union[str, Any] = Field(default=None, alias="displayName")
    active: Union[bool, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")
    account_type: Union[str, Any] = Field(default=None, alias="accountType")
    avatar_urls: Union[WorklogAuthorAvatarurls, Any] = Field(default=None, alias="avatarUrls", description="URLs for user avatars in different sizes")
    """URLs for user avatars in different sizes"""

class WorklogCommentContentItemContentItem(BaseModel):
    """Nested schema for WorklogCommentContentItem.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Content type (e.g., 'text')")
    """Content type (e.g., 'text')"""
    text: Union[str, Any] = Field(default=None, description="Text content")
    """Text content"""

class WorklogCommentContentItem(BaseModel):
    """Nested schema for WorklogComment.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Block type (e.g., 'paragraph')")
    """Block type (e.g., 'paragraph')"""
    content: Union[list[WorklogCommentContentItemContentItem], Any] = Field(default=None, description="Nested content items")
    """Nested content items"""

class WorklogComment(BaseModel):
    """Comment associated with the worklog (ADF format)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Document type (always 'doc')")
    """Document type (always 'doc')"""
    version: Union[int, Any] = Field(default=None, description="ADF version")
    """ADF version"""
    content: Union[list[WorklogCommentContentItem], Any] = Field(default=None, description="Array of content blocks")
    """Array of content blocks"""

class Worklog(BaseModel):
    """Jira worklog object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    self: Union[str, Any] = Field(default=None)
    author: Union[WorklogAuthor, Any] = Field(default=None)
    update_author: Union[WorklogUpdateauthor, Any] = Field(default=None, alias="updateAuthor")
    comment: Union[WorklogComment, Any] = Field(default=None)
    created: Union[str, Any] = Field(default=None)
    updated: Union[str, Any] = Field(default=None)
    started: Union[str, Any] = Field(default=None)
    time_spent: Union[str, Any] = Field(default=None, alias="timeSpent")
    time_spent_seconds: Union[int, Any] = Field(default=None, alias="timeSpentSeconds")
    issue_id: Union[str, Any] = Field(default=None, alias="issueId")
    visibility: Union[WorklogVisibility | None, Any] = Field(default=None)
    properties: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class WorklogsList(BaseModel):
    """Paginated list of issue worklogs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    total: Union[int, Any] = Field(default=None)
    worklogs: Union[list[Worklog], Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class IssuesSearchResultMeta(BaseModel):
    """Metadata for issues.search operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    is_last: Union[bool | None, Any] = Field(default=None, alias="isLast")
    total: Union[int, Any] = Field(default=None)

class ProjectsSearchResultMeta(BaseModel):
    """Metadata for projects.search operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None, alias="nextPage")
    total: Union[int, Any] = Field(default=None)

class IssueCommentsListResultMeta(BaseModel):
    """Metadata for issue_comments.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    total: Union[int, Any] = Field(default=None)

class IssueWorklogsListResultMeta(BaseModel):
    """Metadata for issue_worklogs.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    total: Union[int, Any] = Field(default=None)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class JiraExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class JiraExecuteResultWithMeta(JiraExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

IssuesSearchResult = JiraExecuteResultWithMeta[list[Issue], IssuesSearchResultMeta]
"""Result type for issues.search operation with data and metadata."""

ProjectsSearchResult = JiraExecuteResultWithMeta[list[Project], ProjectsSearchResultMeta]
"""Result type for projects.search operation with data and metadata."""

IssueCommentsListResult = JiraExecuteResultWithMeta[list[IssueComment], IssueCommentsListResultMeta]
"""Result type for issue_comments.list operation with data and metadata."""

IssueWorklogsListResult = JiraExecuteResultWithMeta[list[Worklog], IssueWorklogsListResultMeta]
"""Result type for issue_worklogs.list operation with data and metadata."""

