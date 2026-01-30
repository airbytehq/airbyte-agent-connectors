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
    """Jira API Token Authentication - Authenticate using your Atlassian account email and API token"""

    model_config = ConfigDict(extra="forbid")

    username: str
    """Your Atlassian account email address"""
    password: str
    """Your Jira API token from https://id.atlassian.com/manage-profile/security/api-tokens"""

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

class ProjectAvatarurls(BaseModel):
    """URLs for project avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class ProjectComponentsItem(BaseModel):
    """Nested schema for Project.components_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    is_assignee_type_valid: Union[bool, Any] = Field(default=None, alias="isAssigneeTypeValid")

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

class IssueFieldsPriority(BaseModel):
    """Issue priority information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str, Any] = Field(default=None)
    icon_url: Union[str, Any] = Field(default=None, alias="iconUrl")
    name: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)

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

class UserAvatarurls(BaseModel):
    """URLs for user avatars in different sizes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field_16x16: Union[str, Any] = Field(default=None, alias="16x16")
    field_24x24: Union[str, Any] = Field(default=None, alias="24x24")
    field_32x32: Union[str, Any] = Field(default=None, alias="32x32")
    field_48x48: Union[str, Any] = Field(default=None, alias="48x48")

class UserApplicationrolesItemsItemDefaultgroupsdetailsItem(BaseModel):
    """Nested schema for UserApplicationrolesItemsItem.defaultGroupsDetails_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    group_id: Union[str, Any] = Field(default=None, alias="groupId")
    self: Union[str, Any] = Field(default=None)

class UserApplicationrolesItemsItemGroupdetailsItem(BaseModel):
    """Nested schema for UserApplicationrolesItemsItem.groupDetails_item"""
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
    schema_: Union[IssueFieldSchema | None, Any] = Field(default=None, alias="schema")
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

class IssueCommentVisibility(BaseModel):
    """Visibility restrictions for the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    value: Union[str, Any] = Field(default=None)
    identifier: Union[str | None, Any] = Field(default=None)

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

class IssueAssigneeParams(BaseModel):
    """Parameters for assigning an issue to a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: Union[str, Any] = Field(default=None, alias="accountId")

class EmptyResponse(BaseModel):
    """Empty response object (returned for 204 No Content responses)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pass

class IssueCreateParamsFieldsIssuetype(BaseModel):
    """The type of issue (e.g., Bug, Task, Story)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Issue type ID")
    """Issue type ID"""
    name: Union[str, Any] = Field(default=None, description="Issue type name (e.g., 'Bug', 'Task', 'Story')")
    """Issue type name (e.g., 'Bug', 'Task', 'Story')"""

class IssueCreateParamsFieldsDescriptionContentItemContentItem(BaseModel):
    """Nested schema for IssueCreateParamsFieldsDescriptionContentItem.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Content type (e.g., 'text')")
    """Content type (e.g., 'text')"""
    text: Union[str, Any] = Field(default=None, description="Text content")
    """Text content"""

class IssueCreateParamsFieldsDescriptionContentItem(BaseModel):
    """Nested schema for IssueCreateParamsFieldsDescription.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Block type (e.g., 'paragraph')")
    """Block type (e.g., 'paragraph')"""
    content: Union[list[IssueCreateParamsFieldsDescriptionContentItemContentItem], Any] = Field(default=None)

class IssueCreateParamsFieldsDescription(BaseModel):
    """Issue description in Atlassian Document Format (ADF)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Document type (always 'doc')")
    """Document type (always 'doc')"""
    version: Union[int, Any] = Field(default=None, description="ADF version")
    """ADF version"""
    content: Union[list[IssueCreateParamsFieldsDescriptionContentItem], Any] = Field(default=None, description="Array of content blocks")
    """Array of content blocks"""

class IssueCreateParamsFieldsAssignee(BaseModel):
    """The user to assign the issue to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: Union[str, Any] = Field(default=None, alias="accountId", description="The account ID of the user")
    """The account ID of the user"""

class IssueCreateParamsFieldsProject(BaseModel):
    """The project to create the issue in"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Project ID")
    """Project ID"""
    key: Union[str, Any] = Field(default=None, description="Project key (e.g., 'PROJ')")
    """Project key (e.g., 'PROJ')"""

class IssueCreateParamsFieldsParent(BaseModel):
    """Parent issue for subtasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: Union[str, Any] = Field(default=None, description="Parent issue key")
    """Parent issue key"""

class IssueCreateParamsFieldsPriority(BaseModel):
    """Issue priority"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Priority ID")
    """Priority ID"""
    name: Union[str, Any] = Field(default=None, description="Priority name (e.g., 'Highest', 'High', 'Medium', 'Low', 'Lowest')")
    """Priority name (e.g., 'Highest', 'High', 'Medium', 'Low', 'Lowest')"""

class IssueCreateParamsFields(BaseModel):
    """The issue fields to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project: Union[IssueCreateParamsFieldsProject, Any] = Field(default=None, description="The project to create the issue in")
    """The project to create the issue in"""
    issuetype: Union[IssueCreateParamsFieldsIssuetype, Any] = Field(default=None, description="The type of issue (e.g., Bug, Task, Story)")
    """The type of issue (e.g., Bug, Task, Story)"""
    summary: Union[str, Any] = Field(default=None, description="A brief summary of the issue (title)")
    """A brief summary of the issue (title)"""
    description: Union[IssueCreateParamsFieldsDescription, Any] = Field(default=None, description="Issue description in Atlassian Document Format (ADF)")
    """Issue description in Atlassian Document Format (ADF)"""
    priority: Union[IssueCreateParamsFieldsPriority, Any] = Field(default=None, description="Issue priority")
    """Issue priority"""
    assignee: Union[IssueCreateParamsFieldsAssignee, Any] = Field(default=None, description="The user to assign the issue to")
    """The user to assign the issue to"""
    labels: Union[list[str], Any] = Field(default=None, description="Labels to add to the issue")
    """Labels to add to the issue"""
    parent: Union[IssueCreateParamsFieldsParent, Any] = Field(default=None, description="Parent issue for subtasks")
    """Parent issue for subtasks"""

class IssueCreateParams(BaseModel):
    """Parameters for creating a new issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fields: Union[IssueCreateParamsFields, Any] = Field(default=None)
    update: Union[dict[str, Any], Any] = Field(default=None)

class IssueCreateResponse(BaseModel):
    """Response from creating an issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    key: Union[str, Any] = Field(default=None)
    self: Union[str, Any] = Field(default=None)

class IssueUpdateParamsTransition(BaseModel):
    """Transition the issue to a new status"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="The ID of the transition to perform")
    """The ID of the transition to perform"""

class IssueUpdateParamsFieldsAssignee(BaseModel):
    """The user to assign the issue to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: Union[str, Any] = Field(default=None, alias="accountId", description="The account ID of the user (use null to unassign)")
    """The account ID of the user (use null to unassign)"""

class IssueUpdateParamsFieldsDescriptionContentItemContentItem(BaseModel):
    """Nested schema for IssueUpdateParamsFieldsDescriptionContentItem.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Content type (e.g., 'text')")
    """Content type (e.g., 'text')"""
    text: Union[str, Any] = Field(default=None, description="Text content")
    """Text content"""

class IssueUpdateParamsFieldsDescriptionContentItem(BaseModel):
    """Nested schema for IssueUpdateParamsFieldsDescription.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Block type (e.g., 'paragraph')")
    """Block type (e.g., 'paragraph')"""
    content: Union[list[IssueUpdateParamsFieldsDescriptionContentItemContentItem], Any] = Field(default=None)

class IssueUpdateParamsFieldsDescription(BaseModel):
    """Issue description in Atlassian Document Format (ADF)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Document type (always 'doc')")
    """Document type (always 'doc')"""
    version: Union[int, Any] = Field(default=None, description="ADF version")
    """ADF version"""
    content: Union[list[IssueUpdateParamsFieldsDescriptionContentItem], Any] = Field(default=None, description="Array of content blocks")
    """Array of content blocks"""

class IssueUpdateParamsFieldsPriority(BaseModel):
    """Issue priority"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Priority ID")
    """Priority ID"""
    name: Union[str, Any] = Field(default=None, description="Priority name (e.g., 'Highest', 'High', 'Medium', 'Low', 'Lowest')")
    """Priority name (e.g., 'Highest', 'High', 'Medium', 'Low', 'Lowest')"""

class IssueUpdateParamsFields(BaseModel):
    """The issue fields to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    summary: Union[str, Any] = Field(default=None, description="A brief summary of the issue (title)")
    """A brief summary of the issue (title)"""
    description: Union[IssueUpdateParamsFieldsDescription, Any] = Field(default=None, description="Issue description in Atlassian Document Format (ADF)")
    """Issue description in Atlassian Document Format (ADF)"""
    priority: Union[IssueUpdateParamsFieldsPriority, Any] = Field(default=None, description="Issue priority")
    """Issue priority"""
    assignee: Union[IssueUpdateParamsFieldsAssignee, Any] = Field(default=None, description="The user to assign the issue to")
    """The user to assign the issue to"""
    labels: Union[list[str], Any] = Field(default=None, description="Labels for the issue")
    """Labels for the issue"""

class IssueUpdateParams(BaseModel):
    """Parameters for updating an issue. Only fields included are updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fields: Union[IssueUpdateParamsFields, Any] = Field(default=None)
    update: Union[dict[str, Any], Any] = Field(default=None)
    transition: Union[IssueUpdateParamsTransition, Any] = Field(default=None)

class CommentCreateParamsBodyContentItemContentItem(BaseModel):
    """Nested schema for CommentCreateParamsBodyContentItem.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Content type (e.g., 'text')")
    """Content type (e.g., 'text')"""
    text: Union[str, Any] = Field(default=None, description="Text content")
    """Text content"""

class CommentCreateParamsBodyContentItem(BaseModel):
    """Nested schema for CommentCreateParamsBody.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Block type (e.g., 'paragraph')")
    """Block type (e.g., 'paragraph')"""
    content: Union[list[CommentCreateParamsBodyContentItemContentItem], Any] = Field(default=None)

class CommentCreateParamsBody(BaseModel):
    """Comment content in Atlassian Document Format (ADF)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Document type (always 'doc')")
    """Document type (always 'doc')"""
    version: Union[int, Any] = Field(default=None, description="ADF version")
    """ADF version"""
    content: Union[list[CommentCreateParamsBodyContentItem], Any] = Field(default=None, description="Array of content blocks")
    """Array of content blocks"""

class CommentCreateParamsVisibility(BaseModel):
    """Restrict comment visibility to a group or role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="The type of visibility restriction")
    """The type of visibility restriction"""
    value: Union[str, Any] = Field(default=None, description="The name of the group or role")
    """The name of the group or role"""
    identifier: Union[str, Any] = Field(default=None, description="The ID of the group or role")
    """The ID of the group or role"""

class CommentCreateParams(BaseModel):
    """Parameters for creating a comment on an issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: Union[CommentCreateParamsBody, Any] = Field(default=None)
    visibility: Union[CommentCreateParamsVisibility, Any] = Field(default=None)
    properties: Union[list[dict[str, Any]], Any] = Field(default=None)

class CommentUpdateParamsBodyContentItemContentItem(BaseModel):
    """Nested schema for CommentUpdateParamsBodyContentItem.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Content type (e.g., 'text')")
    """Content type (e.g., 'text')"""
    text: Union[str, Any] = Field(default=None, description="Text content")
    """Text content"""

class CommentUpdateParamsBodyContentItem(BaseModel):
    """Nested schema for CommentUpdateParamsBody.content_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Block type (e.g., 'paragraph')")
    """Block type (e.g., 'paragraph')"""
    content: Union[list[CommentUpdateParamsBodyContentItemContentItem], Any] = Field(default=None)

class CommentUpdateParamsBody(BaseModel):
    """Updated comment content in Atlassian Document Format (ADF)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="Document type (always 'doc')")
    """Document type (always 'doc')"""
    version: Union[int, Any] = Field(default=None, description="ADF version")
    """ADF version"""
    content: Union[list[CommentUpdateParamsBodyContentItem], Any] = Field(default=None, description="Array of content blocks")
    """Array of content blocks"""

class CommentUpdateParamsVisibility(BaseModel):
    """Restrict comment visibility to a group or role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None, description="The type of visibility restriction")
    """The type of visibility restriction"""
    value: Union[str, Any] = Field(default=None, description="The name of the group or role")
    """The name of the group or role"""
    identifier: Union[str, Any] = Field(default=None, description="The ID of the group or role")
    """The ID of the group or role"""

class CommentUpdateParams(BaseModel):
    """Parameters for updating a comment. Only fields included are updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: Union[CommentUpdateParamsBody, Any] = Field(default=None)
    visibility: Union[CommentUpdateParamsVisibility, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class IssuesApiSearchResultMeta(BaseModel):
    """Metadata for issues.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_token: Union[str | None, Any] = Field(default=None, alias="nextPageToken")
    is_last: Union[bool | None, Any] = Field(default=None, alias="isLast")
    total: Union[int, Any] = Field(default=None)

class ProjectsApiSearchResultMeta(BaseModel):
    """Metadata for projects.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None, alias="nextPage")
    total: Union[int, Any] = Field(default=None)

class IssueCommentsListResultMeta(BaseModel):
    """Metadata for issue_comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    total: Union[int, Any] = Field(default=None)

class IssueWorklogsListResultMeta(BaseModel):
    """Metadata for issue_worklogs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_at: Union[int, Any] = Field(default=None, alias="startAt")
    max_results: Union[int, Any] = Field(default=None, alias="maxResults")
    total: Union[int, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class JiraCheckResult(BaseModel):
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

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")

    changelog: dict[str, Any] | None = None
    """Details of changelogs associated with the issue"""
    created: str | None = None
    """The timestamp when the issue was created"""
    editmeta: dict[str, Any] | None = None
    """The metadata for the fields on the issue that can be amended"""
    expand: str = None
    """Expand options that include additional issue details in the response"""
    fields: dict[str, Any] = None
    """Details of various fields associated with the issue"""
    fields_to_include: dict[str, Any] = None
    """Specify the fields to include in the fetched issues data"""
    id: str = None
    """The unique ID of the issue"""
    key: str = None
    """The unique key of the issue"""
    names: dict[str, Any] = None
    """The ID and name of each field present on the issue"""
    operations: dict[str, Any] | None = None
    """The operations that can be performed on the issue"""
    project_id: str = None
    """The ID of the project containing the issue"""
    project_key: str = None
    """The key of the project containing the issue"""
    properties: dict[str, Any] = None
    """Details of the issue properties identified in the request"""
    rendered_fields: dict[str, Any] = None
    """The rendered value of each field present on the issue"""
    schema_: dict[str, Any] = None
    """The schema describing each field present on the issue"""
    self: str = None
    """The URL of the issue details"""
    transitions: list[Any] = None
    """The transitions that can be performed on the issue"""
    updated: str | None = None
    """The timestamp when the issue was last updated"""
    versioned_representations: dict[str, Any] = None
    """The versions of each field on the issue"""


class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool = None
    """Whether the project is archived"""
    archived_by: dict[str, Any] | None = None
    """The user who archived the project"""
    archived_date: str | None = None
    """The date when the project was archived"""
    assignee_type: str | None = None
    """The default assignee when creating issues for this project"""
    avatar_urls: dict[str, Any] = None
    """The URLs of the project's avatars"""
    components: list[Any] = None
    """List of the components contained in the project"""
    deleted: bool = None
    """Whether the project is marked as deleted"""
    deleted_by: dict[str, Any] | None = None
    """The user who marked the project as deleted"""
    deleted_date: str | None = None
    """The date when the project was marked as deleted"""
    description: str | None = None
    """A brief description of the project"""
    email: str | None = None
    """An email address associated with the project"""
    entity_id: str | None = None
    """The unique identifier of the project entity"""
    expand: str | None = None
    """Expand options that include additional project details in the response"""
    favourite: bool = None
    """Whether the project is selected as a favorite"""
    id: str = None
    """The ID of the project"""
    insight: dict[str, Any] | None = None
    """Insights about the project"""
    is_private: bool = None
    """Whether the project is private"""
    issue_type_hierarchy: dict[str, Any] | None = None
    """The issue type hierarchy for the project"""
    issue_types: list[Any] = None
    """List of the issue types available in the project"""
    key: str = None
    """The key of the project"""
    lead: dict[str, Any] | None = None
    """The username of the project lead"""
    name: str = None
    """The name of the project"""
    permissions: dict[str, Any] | None = None
    """User permissions on the project"""
    project_category: dict[str, Any] | None = None
    """The category the project belongs to"""
    project_type_key: str | None = None
    """The project type of the project"""
    properties: dict[str, Any] = None
    """Map of project properties"""
    retention_till_date: str | None = None
    """The date when the project is deleted permanently"""
    roles: dict[str, Any] = None
    """The name and self URL for each role defined in the project"""
    self: str = None
    """The URL of the project details"""
    simplified: bool = None
    """Whether the project is simplified"""
    style: str | None = None
    """The type of the project"""
    url: str | None = None
    """A link to information about this project"""
    uuid: str | None = None
    """Unique ID for next-gen projects"""
    versions: list[Any] = None
    """The versions defined in the project"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    account_id: str = None
    """The account ID of the user, uniquely identifying the user across all Atlassian products"""
    account_type: str | None = None
    """The user account type (atlassian, app, or customer)"""
    active: bool = None
    """Indicates whether the user is active"""
    application_roles: dict[str, Any] | None = None
    """The application roles assigned to the user"""
    avatar_urls: dict[str, Any] = None
    """The avatars of the user"""
    display_name: str | None = None
    """The display name of the user"""
    email_address: str | None = None
    """The email address of the user"""
    expand: str | None = None
    """Options to include additional user details in the response"""
    groups: dict[str, Any] | None = None
    """The groups to which the user belongs"""
    key: str | None = None
    """Deprecated property"""
    locale: str | None = None
    """The locale of the user"""
    name: str | None = None
    """Deprecated property"""
    self: str = None
    """The URL of the user"""
    time_zone: str | None = None
    """The time zone specified in the user's profile"""


class IssueCommentsSearchData(BaseModel):
    """Search result data for issue_comments entity."""
    model_config = ConfigDict(extra="allow")

    author: dict[str, Any] | None = None
    """The ID of the user who created the comment"""
    body: dict[str, Any] = None
    """The comment text in Atlassian Document Format"""
    created: str = None
    """The date and time at which the comment was created"""
    id: str = None
    """The ID of the comment"""
    issue_id: str | None = None
    """Id of the related issue"""
    jsd_public: bool = None
    """Whether the comment is visible in Jira Service Desk"""
    properties: list[Any] = None
    """A list of comment properties"""
    rendered_body: str | None = None
    """The rendered version of the comment"""
    self: str = None
    """The URL of the comment"""
    update_author: dict[str, Any] | None = None
    """The ID of the user who updated the comment last"""
    updated: str = None
    """The date and time at which the comment was updated last"""
    visibility: dict[str, Any] | None = None
    """The group or role to which this item is visible"""


class IssueFieldsSearchData(BaseModel):
    """Search result data for issue_fields entity."""
    model_config = ConfigDict(extra="allow")

    clause_names: list[Any] = None
    """The names that can be used to reference the field in an advanced search"""
    custom: bool = None
    """Whether the field is a custom field"""
    id: str = None
    """The ID of the field"""
    key: str | None = None
    """The key of the field"""
    name: str = None
    """The name of the field"""
    navigable: bool = None
    """Whether the field can be used as a column on the issue navigator"""
    orderable: bool = None
    """Whether the content of the field can be used to order lists"""
    schema_: dict[str, Any] | None = None
    """The data schema for the field"""
    scope: dict[str, Any] | None = None
    """The scope of the field"""
    searchable: bool = None
    """Whether the content of the field can be searched"""
    untranslated_name: str | None = None
    """The untranslated name of the field"""


class IssueWorklogsSearchData(BaseModel):
    """Search result data for issue_worklogs entity."""
    model_config = ConfigDict(extra="allow")

    author: dict[str, Any] = None
    """Details of the user who created the worklog"""
    comment: dict[str, Any] | None = None
    """A comment about the worklog in Atlassian Document Format"""
    created: str = None
    """The datetime on which the worklog was created"""
    id: str = None
    """The ID of the worklog record"""
    issue_id: str = None
    """The ID of the issue this worklog is for"""
    properties: list[Any] = None
    """Details of properties for the worklog"""
    self: str = None
    """The URL of the worklog item"""
    started: str = None
    """The datetime on which the worklog effort was started"""
    time_spent: str | None = None
    """The time spent working on the issue as days, hours, or minutes"""
    time_spent_seconds: int = None
    """The time in seconds spent working on the issue"""
    update_author: dict[str, Any] | None = None
    """Details of the user who last updated the worklog"""
    updated: str = None
    """The datetime on which the worklog was last updated"""
    visibility: dict[str, Any] | None = None
    """Details about any restrictions in the visibility of the worklog"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchHit(BaseModel, Generic[D]):
    """A single search result with typed data."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the record."""
    score: float | None = None
    """Relevance score for the match."""
    data: D
    """The matched record data."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed hits."""
    model_config = ConfigDict(extra="allow")

    hits: list[AirbyteSearchHit[D]] = Field(default_factory=list)
    """List of matching records."""
    next_cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

IssueCommentsSearchResult = AirbyteSearchResult[IssueCommentsSearchData]
"""Search result type for issue_comments entity."""

IssueFieldsSearchResult = AirbyteSearchResult[IssueFieldsSearchData]
"""Search result type for issue_fields entity."""

IssueWorklogsSearchResult = AirbyteSearchResult[IssueWorklogsSearchData]
"""Search result type for issue_worklogs entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

IssuesApiSearchResult = JiraExecuteResultWithMeta[list[Issue], IssuesApiSearchResultMeta]
"""Result type for issues.api_search operation with data and metadata."""

ProjectsApiSearchResult = JiraExecuteResultWithMeta[list[Project], ProjectsApiSearchResultMeta]
"""Result type for projects.api_search operation with data and metadata."""

UsersListResult = JiraExecuteResult[list[User]]
"""Result type for users.list operation."""

UsersApiSearchResult = JiraExecuteResult[list[User]]
"""Result type for users.api_search operation."""

IssueFieldsListResult = JiraExecuteResult[list[IssueField]]
"""Result type for issue_fields.list operation."""

IssueFieldsApiSearchResult = JiraExecuteResult[IssueFieldSearchResults]
"""Result type for issue_fields.api_search operation."""

IssueCommentsListResult = JiraExecuteResultWithMeta[list[IssueComment], IssueCommentsListResultMeta]
"""Result type for issue_comments.list operation with data and metadata."""

IssueWorklogsListResult = JiraExecuteResultWithMeta[list[Worklog], IssueWorklogsListResultMeta]
"""Result type for issue_worklogs.list operation with data and metadata."""

