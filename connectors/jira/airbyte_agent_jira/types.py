"""
Type definitions for jira connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class IssuesCreateParamsFieldsProject(TypedDict):
    """The project to create the issue in"""
    id: NotRequired[str]
    key: NotRequired[str]

class IssuesCreateParamsFieldsIssuetype(TypedDict):
    """The type of issue (e.g., Bug, Task, Story)"""
    id: NotRequired[str]
    name: NotRequired[str]

class IssuesCreateParamsFieldsDescriptionContentItemContentItem(TypedDict):
    """Nested schema for IssuesCreateParamsFieldsDescriptionContentItem.content_item"""
    type: NotRequired[str]
    text: NotRequired[str]

class IssuesCreateParamsFieldsDescriptionContentItem(TypedDict):
    """Nested schema for IssuesCreateParamsFieldsDescription.content_item"""
    type: NotRequired[str]
    content: NotRequired[list[IssuesCreateParamsFieldsDescriptionContentItemContentItem]]

class IssuesCreateParamsFieldsDescription(TypedDict):
    """Issue description in Atlassian Document Format (ADF)"""
    type: NotRequired[str]
    version: NotRequired[int]
    content: NotRequired[list[IssuesCreateParamsFieldsDescriptionContentItem]]

class IssuesCreateParamsFieldsPriority(TypedDict):
    """Issue priority"""
    id: NotRequired[str]
    name: NotRequired[str]

class IssuesCreateParamsFieldsAssignee(TypedDict):
    """The user to assign the issue to"""
    accountId: NotRequired[str]

class IssuesCreateParamsFieldsParent(TypedDict):
    """Parent issue for subtasks"""
    key: NotRequired[str]

class IssuesCreateParamsFields(TypedDict):
    """The issue fields to set"""
    project: IssuesCreateParamsFieldsProject
    issuetype: IssuesCreateParamsFieldsIssuetype
    summary: str
    description: NotRequired[IssuesCreateParamsFieldsDescription]
    priority: NotRequired[IssuesCreateParamsFieldsPriority]
    assignee: NotRequired[IssuesCreateParamsFieldsAssignee]
    labels: NotRequired[list[str]]
    parent: NotRequired[IssuesCreateParamsFieldsParent]

class IssuesUpdateParamsFieldsDescriptionContentItemContentItem(TypedDict):
    """Nested schema for IssuesUpdateParamsFieldsDescriptionContentItem.content_item"""
    type: NotRequired[str]
    text: NotRequired[str]

class IssuesUpdateParamsFieldsDescriptionContentItem(TypedDict):
    """Nested schema for IssuesUpdateParamsFieldsDescription.content_item"""
    type: NotRequired[str]
    content: NotRequired[list[IssuesUpdateParamsFieldsDescriptionContentItemContentItem]]

class IssuesUpdateParamsFieldsDescription(TypedDict):
    """Issue description in Atlassian Document Format (ADF)"""
    type: NotRequired[str]
    version: NotRequired[int]
    content: NotRequired[list[IssuesUpdateParamsFieldsDescriptionContentItem]]

class IssuesUpdateParamsFieldsPriority(TypedDict):
    """Issue priority"""
    id: NotRequired[str]
    name: NotRequired[str]

class IssuesUpdateParamsFieldsAssignee(TypedDict):
    """The user to assign the issue to"""
    accountId: NotRequired[str]

class IssuesUpdateParamsFields(TypedDict):
    """The issue fields to update"""
    summary: NotRequired[str]
    description: NotRequired[IssuesUpdateParamsFieldsDescription]
    priority: NotRequired[IssuesUpdateParamsFieldsPriority]
    assignee: NotRequired[IssuesUpdateParamsFieldsAssignee]
    labels: NotRequired[list[str]]

class IssuesUpdateParamsTransition(TypedDict):
    """Transition the issue to a new status"""
    id: NotRequired[str]

class IssueCommentsCreateParamsBodyContentItemContentItem(TypedDict):
    """Nested schema for IssueCommentsCreateParamsBodyContentItem.content_item"""
    type: NotRequired[str]
    text: NotRequired[str]

class IssueCommentsCreateParamsBodyContentItem(TypedDict):
    """Nested schema for IssueCommentsCreateParamsBody.content_item"""
    type: NotRequired[str]
    content: NotRequired[list[IssueCommentsCreateParamsBodyContentItemContentItem]]

class IssueCommentsCreateParamsBody(TypedDict):
    """Comment content in Atlassian Document Format (ADF)"""
    type: str
    version: int
    content: list[IssueCommentsCreateParamsBodyContentItem]

class IssueCommentsCreateParamsVisibility(TypedDict):
    """Restrict comment visibility to a group or role"""
    type: NotRequired[str]
    value: NotRequired[str]
    identifier: NotRequired[str]

class IssueCommentsUpdateParamsBodyContentItemContentItem(TypedDict):
    """Nested schema for IssueCommentsUpdateParamsBodyContentItem.content_item"""
    type: NotRequired[str]
    text: NotRequired[str]

class IssueCommentsUpdateParamsBodyContentItem(TypedDict):
    """Nested schema for IssueCommentsUpdateParamsBody.content_item"""
    type: NotRequired[str]
    content: NotRequired[list[IssueCommentsUpdateParamsBodyContentItemContentItem]]

class IssueCommentsUpdateParamsBody(TypedDict):
    """Updated comment content in Atlassian Document Format (ADF)"""
    type: str
    version: int
    content: list[IssueCommentsUpdateParamsBodyContentItem]

class IssueCommentsUpdateParamsVisibility(TypedDict):
    """Restrict comment visibility to a group or role"""
    type: NotRequired[str]
    value: NotRequired[str]
    identifier: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class IssuesApiSearchParams(TypedDict):
    """Parameters for issues.api_search operation"""
    jql: NotRequired[str]
    next_page_token: NotRequired[str]
    max_results: NotRequired[int]
    fields: NotRequired[str]
    expand: NotRequired[str]
    properties: NotRequired[str]
    fields_by_keys: NotRequired[bool]
    fail_fast: NotRequired[bool]

class IssuesCreateParams(TypedDict):
    """Parameters for issues.create operation"""
    fields: IssuesCreateParamsFields
    update: NotRequired[dict[str, Any]]
    update_history: NotRequired[bool]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    issue_id_or_key: str
    fields: NotRequired[str]
    expand: NotRequired[str]
    properties: NotRequired[str]
    fields_by_keys: NotRequired[bool]
    update_history: NotRequired[bool]
    fail_fast: NotRequired[bool]

class IssuesUpdateParams(TypedDict):
    """Parameters for issues.update operation"""
    fields: NotRequired[IssuesUpdateParamsFields]
    update: NotRequired[dict[str, Any]]
    transition: NotRequired[IssuesUpdateParamsTransition]
    issue_id_or_key: str
    notify_users: NotRequired[bool]
    override_screen_security: NotRequired[bool]
    override_editable_flag: NotRequired[bool]
    return_issue: NotRequired[bool]
    expand: NotRequired[str]

class IssuesDeleteParams(TypedDict):
    """Parameters for issues.delete operation"""
    issue_id_or_key: str
    delete_subtasks: NotRequired[bool]

class ProjectsApiSearchParams(TypedDict):
    """Parameters for projects.api_search operation"""
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    order_by: NotRequired[str]
    id: NotRequired[list[int]]
    keys: NotRequired[list[str]]
    query: NotRequired[str]
    type_key: NotRequired[str]
    category_id: NotRequired[int]
    action: NotRequired[str]
    expand: NotRequired[str]
    status: NotRequired[list[str]]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    project_id_or_key: str
    expand: NotRequired[str]
    properties: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    account_id: str
    expand: NotRequired[str]

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    start_at: NotRequired[int]
    max_results: NotRequired[int]

class UsersApiSearchParams(TypedDict):
    """Parameters for users.api_search operation"""
    query: NotRequired[str]
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    account_id: NotRequired[str]
    property: NotRequired[str]

class IssueFieldsListParams(TypedDict):
    """Parameters for issue_fields.list operation"""
    pass

class IssueFieldsApiSearchParams(TypedDict):
    """Parameters for issue_fields.api_search operation"""
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    type: NotRequired[list[str]]
    id: NotRequired[list[str]]
    query: NotRequired[str]
    order_by: NotRequired[str]
    expand: NotRequired[str]

class IssueCommentsListParams(TypedDict):
    """Parameters for issue_comments.list operation"""
    issue_id_or_key: str
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    order_by: NotRequired[str]
    expand: NotRequired[str]

class IssueCommentsCreateParams(TypedDict):
    """Parameters for issue_comments.create operation"""
    body: IssueCommentsCreateParamsBody
    visibility: NotRequired[IssueCommentsCreateParamsVisibility]
    properties: NotRequired[list[dict[str, Any]]]
    issue_id_or_key: str
    expand: NotRequired[str]

class IssueCommentsGetParams(TypedDict):
    """Parameters for issue_comments.get operation"""
    issue_id_or_key: str
    comment_id: str
    expand: NotRequired[str]

class IssueCommentsUpdateParams(TypedDict):
    """Parameters for issue_comments.update operation"""
    body: IssueCommentsUpdateParamsBody
    visibility: NotRequired[IssueCommentsUpdateParamsVisibility]
    issue_id_or_key: str
    comment_id: str
    notify_users: NotRequired[bool]
    expand: NotRequired[str]

class IssueCommentsDeleteParams(TypedDict):
    """Parameters for issue_comments.delete operation"""
    issue_id_or_key: str
    comment_id: str

class IssueWorklogsListParams(TypedDict):
    """Parameters for issue_worklogs.list operation"""
    issue_id_or_key: str
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    expand: NotRequired[str]

class IssueWorklogsGetParams(TypedDict):
    """Parameters for issue_worklogs.get operation"""
    issue_id_or_key: str
    worklog_id: str
    expand: NotRequired[str]

class IssuesAssigneeUpdateParams(TypedDict):
    """Parameters for issues_assignee.update operation"""
    account_id: NotRequired[str]
    issue_id_or_key: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    changelog: dict[str, Any] | None
    """Details of changelogs associated with the issue"""
    created: str | None
    """The timestamp when the issue was created"""
    editmeta: dict[str, Any] | None
    """The metadata for the fields on the issue that can be amended"""
    expand: str
    """Expand options that include additional issue details in the response"""
    fields: dict[str, Any]
    """Details of various fields associated with the issue"""
    fields_to_include: dict[str, Any]
    """Specify the fields to include in the fetched issues data"""
    id: str
    """The unique ID of the issue"""
    key: str
    """The unique key of the issue"""
    names: dict[str, Any]
    """The ID and name of each field present on the issue"""
    operations: dict[str, Any] | None
    """The operations that can be performed on the issue"""
    project_id: str
    """The ID of the project containing the issue"""
    project_key: str
    """The key of the project containing the issue"""
    properties: dict[str, Any]
    """Details of the issue properties identified in the request"""
    rendered_fields: dict[str, Any]
    """The rendered value of each field present on the issue"""
    schema_: dict[str, Any]
    """The schema describing each field present on the issue"""
    self: str
    """The URL of the issue details"""
    transitions: list[Any]
    """The transitions that can be performed on the issue"""
    updated: str | None
    """The timestamp when the issue was last updated"""
    versioned_representations: dict[str, Any]
    """The versions of each field on the issue"""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    changelog: list[dict[str, Any]]
    """Details of changelogs associated with the issue"""
    created: list[str]
    """The timestamp when the issue was created"""
    editmeta: list[dict[str, Any]]
    """The metadata for the fields on the issue that can be amended"""
    expand: list[str]
    """Expand options that include additional issue details in the response"""
    fields: list[dict[str, Any]]
    """Details of various fields associated with the issue"""
    fields_to_include: list[dict[str, Any]]
    """Specify the fields to include in the fetched issues data"""
    id: list[str]
    """The unique ID of the issue"""
    key: list[str]
    """The unique key of the issue"""
    names: list[dict[str, Any]]
    """The ID and name of each field present on the issue"""
    operations: list[dict[str, Any]]
    """The operations that can be performed on the issue"""
    project_id: list[str]
    """The ID of the project containing the issue"""
    project_key: list[str]
    """The key of the project containing the issue"""
    properties: list[dict[str, Any]]
    """Details of the issue properties identified in the request"""
    rendered_fields: list[dict[str, Any]]
    """The rendered value of each field present on the issue"""
    schema_: list[dict[str, Any]]
    """The schema describing each field present on the issue"""
    self: list[str]
    """The URL of the issue details"""
    transitions: list[list[Any]]
    """The transitions that can be performed on the issue"""
    updated: list[str]
    """The timestamp when the issue was last updated"""
    versioned_representations: list[dict[str, Any]]
    """The versions of each field on the issue"""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    changelog: Any
    """Details of changelogs associated with the issue"""
    created: Any
    """The timestamp when the issue was created"""
    editmeta: Any
    """The metadata for the fields on the issue that can be amended"""
    expand: Any
    """Expand options that include additional issue details in the response"""
    fields: Any
    """Details of various fields associated with the issue"""
    fields_to_include: Any
    """Specify the fields to include in the fetched issues data"""
    id: Any
    """The unique ID of the issue"""
    key: Any
    """The unique key of the issue"""
    names: Any
    """The ID and name of each field present on the issue"""
    operations: Any
    """The operations that can be performed on the issue"""
    project_id: Any
    """The ID of the project containing the issue"""
    project_key: Any
    """The key of the project containing the issue"""
    properties: Any
    """Details of the issue properties identified in the request"""
    rendered_fields: Any
    """The rendered value of each field present on the issue"""
    schema_: Any
    """The schema describing each field present on the issue"""
    self: Any
    """The URL of the issue details"""
    transitions: Any
    """The transitions that can be performed on the issue"""
    updated: Any
    """The timestamp when the issue was last updated"""
    versioned_representations: Any
    """The versions of each field on the issue"""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    changelog: str
    """Details of changelogs associated with the issue"""
    created: str
    """The timestamp when the issue was created"""
    editmeta: str
    """The metadata for the fields on the issue that can be amended"""
    expand: str
    """Expand options that include additional issue details in the response"""
    fields: str
    """Details of various fields associated with the issue"""
    fields_to_include: str
    """Specify the fields to include in the fetched issues data"""
    id: str
    """The unique ID of the issue"""
    key: str
    """The unique key of the issue"""
    names: str
    """The ID and name of each field present on the issue"""
    operations: str
    """The operations that can be performed on the issue"""
    project_id: str
    """The ID of the project containing the issue"""
    project_key: str
    """The key of the project containing the issue"""
    properties: str
    """Details of the issue properties identified in the request"""
    rendered_fields: str
    """The rendered value of each field present on the issue"""
    schema_: str
    """The schema describing each field present on the issue"""
    self: str
    """The URL of the issue details"""
    transitions: str
    """The transitions that can be performed on the issue"""
    updated: str
    """The timestamp when the issue was last updated"""
    versioned_representations: str
    """The versions of each field on the issue"""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    changelog: AirbyteSortOrder
    """Details of changelogs associated with the issue"""
    created: AirbyteSortOrder
    """The timestamp when the issue was created"""
    editmeta: AirbyteSortOrder
    """The metadata for the fields on the issue that can be amended"""
    expand: AirbyteSortOrder
    """Expand options that include additional issue details in the response"""
    fields: AirbyteSortOrder
    """Details of various fields associated with the issue"""
    fields_to_include: AirbyteSortOrder
    """Specify the fields to include in the fetched issues data"""
    id: AirbyteSortOrder
    """The unique ID of the issue"""
    key: AirbyteSortOrder
    """The unique key of the issue"""
    names: AirbyteSortOrder
    """The ID and name of each field present on the issue"""
    operations: AirbyteSortOrder
    """The operations that can be performed on the issue"""
    project_id: AirbyteSortOrder
    """The ID of the project containing the issue"""
    project_key: AirbyteSortOrder
    """The key of the project containing the issue"""
    properties: AirbyteSortOrder
    """Details of the issue properties identified in the request"""
    rendered_fields: AirbyteSortOrder
    """The rendered value of each field present on the issue"""
    schema_: AirbyteSortOrder
    """The schema describing each field present on the issue"""
    self: AirbyteSortOrder
    """The URL of the issue details"""
    transitions: AirbyteSortOrder
    """The transitions that can be performed on the issue"""
    updated: AirbyteSortOrder
    """The timestamp when the issue was last updated"""
    versioned_representations: AirbyteSortOrder
    """The versions of each field on the issue"""


# Entity-specific condition types for issues
class IssuesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssuesSearchFilter


class IssuesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssuesSearchFilter


class IssuesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssuesSearchFilter


class IssuesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssuesSearchFilter


class IssuesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssuesSearchFilter


class IssuesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssuesSearchFilter


class IssuesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssuesStringFilter


class IssuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssuesStringFilter


class IssuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssuesStringFilter


class IssuesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssuesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssuesInCondition = TypedDict("IssuesInCondition", {"in": IssuesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssuesNotCondition = TypedDict("IssuesNotCondition", {"not": "IssuesCondition"}, total=False)
"""Negates the nested condition."""

IssuesAndCondition = TypedDict("IssuesAndCondition", {"and": "list[IssuesCondition]"}, total=False)
"""True if all nested conditions are true."""

IssuesOrCondition = TypedDict("IssuesOrCondition", {"or": "list[IssuesCondition]"}, total=False)
"""True if any nested condition is true."""

IssuesAnyCondition = TypedDict("IssuesAnyCondition", {"any": IssuesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issues condition types
IssuesCondition = (
    IssuesEqCondition
    | IssuesNeqCondition
    | IssuesGtCondition
    | IssuesGteCondition
    | IssuesLtCondition
    | IssuesLteCondition
    | IssuesInCondition
    | IssuesLikeCondition
    | IssuesFuzzyCondition
    | IssuesKeywordCondition
    | IssuesContainsCondition
    | IssuesNotCondition
    | IssuesAndCondition
    | IssuesOrCondition
    | IssuesAnyCondition
)


class IssuesSearchQuery(TypedDict, total=False):
    """Search query for issues entity."""
    filter: IssuesCondition
    sort: list[IssuesSortFilter]


# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    archived: bool
    """Whether the project is archived"""
    archived_by: dict[str, Any] | None
    """The user who archived the project"""
    archived_date: str | None
    """The date when the project was archived"""
    assignee_type: str | None
    """The default assignee when creating issues for this project"""
    avatar_urls: dict[str, Any]
    """The URLs of the project's avatars"""
    components: list[Any]
    """List of the components contained in the project"""
    deleted: bool
    """Whether the project is marked as deleted"""
    deleted_by: dict[str, Any] | None
    """The user who marked the project as deleted"""
    deleted_date: str | None
    """The date when the project was marked as deleted"""
    description: str | None
    """A brief description of the project"""
    email: str | None
    """An email address associated with the project"""
    entity_id: str | None
    """The unique identifier of the project entity"""
    expand: str | None
    """Expand options that include additional project details in the response"""
    favourite: bool
    """Whether the project is selected as a favorite"""
    id: str
    """The ID of the project"""
    insight: dict[str, Any] | None
    """Insights about the project"""
    is_private: bool
    """Whether the project is private"""
    issue_type_hierarchy: dict[str, Any] | None
    """The issue type hierarchy for the project"""
    issue_types: list[Any]
    """List of the issue types available in the project"""
    key: str
    """The key of the project"""
    lead: dict[str, Any] | None
    """The username of the project lead"""
    name: str
    """The name of the project"""
    permissions: dict[str, Any] | None
    """User permissions on the project"""
    project_category: dict[str, Any] | None
    """The category the project belongs to"""
    project_type_key: str | None
    """The project type of the project"""
    properties: dict[str, Any]
    """Map of project properties"""
    retention_till_date: str | None
    """The date when the project is deleted permanently"""
    roles: dict[str, Any]
    """The name and self URL for each role defined in the project"""
    self: str
    """The URL of the project details"""
    simplified: bool
    """Whether the project is simplified"""
    style: str | None
    """The type of the project"""
    url: str | None
    """A link to information about this project"""
    uuid: str | None
    """Unique ID for next-gen projects"""
    versions: list[Any]
    """The versions defined in the project"""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Whether the project is archived"""
    archived_by: list[dict[str, Any]]
    """The user who archived the project"""
    archived_date: list[str]
    """The date when the project was archived"""
    assignee_type: list[str]
    """The default assignee when creating issues for this project"""
    avatar_urls: list[dict[str, Any]]
    """The URLs of the project's avatars"""
    components: list[list[Any]]
    """List of the components contained in the project"""
    deleted: list[bool]
    """Whether the project is marked as deleted"""
    deleted_by: list[dict[str, Any]]
    """The user who marked the project as deleted"""
    deleted_date: list[str]
    """The date when the project was marked as deleted"""
    description: list[str]
    """A brief description of the project"""
    email: list[str]
    """An email address associated with the project"""
    entity_id: list[str]
    """The unique identifier of the project entity"""
    expand: list[str]
    """Expand options that include additional project details in the response"""
    favourite: list[bool]
    """Whether the project is selected as a favorite"""
    id: list[str]
    """The ID of the project"""
    insight: list[dict[str, Any]]
    """Insights about the project"""
    is_private: list[bool]
    """Whether the project is private"""
    issue_type_hierarchy: list[dict[str, Any]]
    """The issue type hierarchy for the project"""
    issue_types: list[list[Any]]
    """List of the issue types available in the project"""
    key: list[str]
    """The key of the project"""
    lead: list[dict[str, Any]]
    """The username of the project lead"""
    name: list[str]
    """The name of the project"""
    permissions: list[dict[str, Any]]
    """User permissions on the project"""
    project_category: list[dict[str, Any]]
    """The category the project belongs to"""
    project_type_key: list[str]
    """The project type of the project"""
    properties: list[dict[str, Any]]
    """Map of project properties"""
    retention_till_date: list[str]
    """The date when the project is deleted permanently"""
    roles: list[dict[str, Any]]
    """The name and self URL for each role defined in the project"""
    self: list[str]
    """The URL of the project details"""
    simplified: list[bool]
    """Whether the project is simplified"""
    style: list[str]
    """The type of the project"""
    url: list[str]
    """A link to information about this project"""
    uuid: list[str]
    """Unique ID for next-gen projects"""
    versions: list[list[Any]]
    """The versions defined in the project"""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Whether the project is archived"""
    archived_by: Any
    """The user who archived the project"""
    archived_date: Any
    """The date when the project was archived"""
    assignee_type: Any
    """The default assignee when creating issues for this project"""
    avatar_urls: Any
    """The URLs of the project's avatars"""
    components: Any
    """List of the components contained in the project"""
    deleted: Any
    """Whether the project is marked as deleted"""
    deleted_by: Any
    """The user who marked the project as deleted"""
    deleted_date: Any
    """The date when the project was marked as deleted"""
    description: Any
    """A brief description of the project"""
    email: Any
    """An email address associated with the project"""
    entity_id: Any
    """The unique identifier of the project entity"""
    expand: Any
    """Expand options that include additional project details in the response"""
    favourite: Any
    """Whether the project is selected as a favorite"""
    id: Any
    """The ID of the project"""
    insight: Any
    """Insights about the project"""
    is_private: Any
    """Whether the project is private"""
    issue_type_hierarchy: Any
    """The issue type hierarchy for the project"""
    issue_types: Any
    """List of the issue types available in the project"""
    key: Any
    """The key of the project"""
    lead: Any
    """The username of the project lead"""
    name: Any
    """The name of the project"""
    permissions: Any
    """User permissions on the project"""
    project_category: Any
    """The category the project belongs to"""
    project_type_key: Any
    """The project type of the project"""
    properties: Any
    """Map of project properties"""
    retention_till_date: Any
    """The date when the project is deleted permanently"""
    roles: Any
    """The name and self URL for each role defined in the project"""
    self: Any
    """The URL of the project details"""
    simplified: Any
    """Whether the project is simplified"""
    style: Any
    """The type of the project"""
    url: Any
    """A link to information about this project"""
    uuid: Any
    """Unique ID for next-gen projects"""
    versions: Any
    """The versions defined in the project"""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Whether the project is archived"""
    archived_by: str
    """The user who archived the project"""
    archived_date: str
    """The date when the project was archived"""
    assignee_type: str
    """The default assignee when creating issues for this project"""
    avatar_urls: str
    """The URLs of the project's avatars"""
    components: str
    """List of the components contained in the project"""
    deleted: str
    """Whether the project is marked as deleted"""
    deleted_by: str
    """The user who marked the project as deleted"""
    deleted_date: str
    """The date when the project was marked as deleted"""
    description: str
    """A brief description of the project"""
    email: str
    """An email address associated with the project"""
    entity_id: str
    """The unique identifier of the project entity"""
    expand: str
    """Expand options that include additional project details in the response"""
    favourite: str
    """Whether the project is selected as a favorite"""
    id: str
    """The ID of the project"""
    insight: str
    """Insights about the project"""
    is_private: str
    """Whether the project is private"""
    issue_type_hierarchy: str
    """The issue type hierarchy for the project"""
    issue_types: str
    """List of the issue types available in the project"""
    key: str
    """The key of the project"""
    lead: str
    """The username of the project lead"""
    name: str
    """The name of the project"""
    permissions: str
    """User permissions on the project"""
    project_category: str
    """The category the project belongs to"""
    project_type_key: str
    """The project type of the project"""
    properties: str
    """Map of project properties"""
    retention_till_date: str
    """The date when the project is deleted permanently"""
    roles: str
    """The name and self URL for each role defined in the project"""
    self: str
    """The URL of the project details"""
    simplified: str
    """Whether the project is simplified"""
    style: str
    """The type of the project"""
    url: str
    """A link to information about this project"""
    uuid: str
    """Unique ID for next-gen projects"""
    versions: str
    """The versions defined in the project"""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    archived: AirbyteSortOrder
    """Whether the project is archived"""
    archived_by: AirbyteSortOrder
    """The user who archived the project"""
    archived_date: AirbyteSortOrder
    """The date when the project was archived"""
    assignee_type: AirbyteSortOrder
    """The default assignee when creating issues for this project"""
    avatar_urls: AirbyteSortOrder
    """The URLs of the project's avatars"""
    components: AirbyteSortOrder
    """List of the components contained in the project"""
    deleted: AirbyteSortOrder
    """Whether the project is marked as deleted"""
    deleted_by: AirbyteSortOrder
    """The user who marked the project as deleted"""
    deleted_date: AirbyteSortOrder
    """The date when the project was marked as deleted"""
    description: AirbyteSortOrder
    """A brief description of the project"""
    email: AirbyteSortOrder
    """An email address associated with the project"""
    entity_id: AirbyteSortOrder
    """The unique identifier of the project entity"""
    expand: AirbyteSortOrder
    """Expand options that include additional project details in the response"""
    favourite: AirbyteSortOrder
    """Whether the project is selected as a favorite"""
    id: AirbyteSortOrder
    """The ID of the project"""
    insight: AirbyteSortOrder
    """Insights about the project"""
    is_private: AirbyteSortOrder
    """Whether the project is private"""
    issue_type_hierarchy: AirbyteSortOrder
    """The issue type hierarchy for the project"""
    issue_types: AirbyteSortOrder
    """List of the issue types available in the project"""
    key: AirbyteSortOrder
    """The key of the project"""
    lead: AirbyteSortOrder
    """The username of the project lead"""
    name: AirbyteSortOrder
    """The name of the project"""
    permissions: AirbyteSortOrder
    """User permissions on the project"""
    project_category: AirbyteSortOrder
    """The category the project belongs to"""
    project_type_key: AirbyteSortOrder
    """The project type of the project"""
    properties: AirbyteSortOrder
    """Map of project properties"""
    retention_till_date: AirbyteSortOrder
    """The date when the project is deleted permanently"""
    roles: AirbyteSortOrder
    """The name and self URL for each role defined in the project"""
    self: AirbyteSortOrder
    """The URL of the project details"""
    simplified: AirbyteSortOrder
    """Whether the project is simplified"""
    style: AirbyteSortOrder
    """The type of the project"""
    url: AirbyteSortOrder
    """A link to information about this project"""
    uuid: AirbyteSortOrder
    """Unique ID for next-gen projects"""
    versions: AirbyteSortOrder
    """The versions defined in the project"""


# Entity-specific condition types for projects
class ProjectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectsSearchFilter


class ProjectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectsSearchFilter


class ProjectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectsSearchFilter


class ProjectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectsSearchFilter


class ProjectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectsSearchFilter


class ProjectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectsSearchFilter


class ProjectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectsStringFilter


class ProjectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectsStringFilter


class ProjectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectsStringFilter


class ProjectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectsInCondition = TypedDict("ProjectsInCondition", {"in": ProjectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectsNotCondition = TypedDict("ProjectsNotCondition", {"not": "ProjectsCondition"}, total=False)
"""Negates the nested condition."""

ProjectsAndCondition = TypedDict("ProjectsAndCondition", {"and": "list[ProjectsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectsOrCondition = TypedDict("ProjectsOrCondition", {"or": "list[ProjectsCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectsAnyCondition = TypedDict("ProjectsAnyCondition", {"any": ProjectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all projects condition types
ProjectsCondition = (
    ProjectsEqCondition
    | ProjectsNeqCondition
    | ProjectsGtCondition
    | ProjectsGteCondition
    | ProjectsLtCondition
    | ProjectsLteCondition
    | ProjectsInCondition
    | ProjectsLikeCondition
    | ProjectsFuzzyCondition
    | ProjectsKeywordCondition
    | ProjectsContainsCondition
    | ProjectsNotCondition
    | ProjectsAndCondition
    | ProjectsOrCondition
    | ProjectsAnyCondition
)


class ProjectsSearchQuery(TypedDict, total=False):
    """Search query for projects entity."""
    filter: ProjectsCondition
    sort: list[ProjectsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    account_id: str
    """The account ID of the user, uniquely identifying the user across all Atlassian products"""
    account_type: str | None
    """The user account type (atlassian, app, or customer)"""
    active: bool
    """Indicates whether the user is active"""
    application_roles: dict[str, Any] | None
    """The application roles assigned to the user"""
    avatar_urls: dict[str, Any]
    """The avatars of the user"""
    display_name: str | None
    """The display name of the user"""
    email_address: str | None
    """The email address of the user"""
    expand: str | None
    """Options to include additional user details in the response"""
    groups: dict[str, Any] | None
    """The groups to which the user belongs"""
    key: str | None
    """Deprecated property"""
    locale: str | None
    """The locale of the user"""
    name: str | None
    """Deprecated property"""
    self: str
    """The URL of the user"""
    time_zone: str | None
    """The time zone specified in the user's profile"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_id: list[str]
    """The account ID of the user, uniquely identifying the user across all Atlassian products"""
    account_type: list[str]
    """The user account type (atlassian, app, or customer)"""
    active: list[bool]
    """Indicates whether the user is active"""
    application_roles: list[dict[str, Any]]
    """The application roles assigned to the user"""
    avatar_urls: list[dict[str, Any]]
    """The avatars of the user"""
    display_name: list[str]
    """The display name of the user"""
    email_address: list[str]
    """The email address of the user"""
    expand: list[str]
    """Options to include additional user details in the response"""
    groups: list[dict[str, Any]]
    """The groups to which the user belongs"""
    key: list[str]
    """Deprecated property"""
    locale: list[str]
    """The locale of the user"""
    name: list[str]
    """Deprecated property"""
    self: list[str]
    """The URL of the user"""
    time_zone: list[str]
    """The time zone specified in the user's profile"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_id: Any
    """The account ID of the user, uniquely identifying the user across all Atlassian products"""
    account_type: Any
    """The user account type (atlassian, app, or customer)"""
    active: Any
    """Indicates whether the user is active"""
    application_roles: Any
    """The application roles assigned to the user"""
    avatar_urls: Any
    """The avatars of the user"""
    display_name: Any
    """The display name of the user"""
    email_address: Any
    """The email address of the user"""
    expand: Any
    """Options to include additional user details in the response"""
    groups: Any
    """The groups to which the user belongs"""
    key: Any
    """Deprecated property"""
    locale: Any
    """The locale of the user"""
    name: Any
    """Deprecated property"""
    self: Any
    """The URL of the user"""
    time_zone: Any
    """The time zone specified in the user's profile"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_id: str
    """The account ID of the user, uniquely identifying the user across all Atlassian products"""
    account_type: str
    """The user account type (atlassian, app, or customer)"""
    active: str
    """Indicates whether the user is active"""
    application_roles: str
    """The application roles assigned to the user"""
    avatar_urls: str
    """The avatars of the user"""
    display_name: str
    """The display name of the user"""
    email_address: str
    """The email address of the user"""
    expand: str
    """Options to include additional user details in the response"""
    groups: str
    """The groups to which the user belongs"""
    key: str
    """Deprecated property"""
    locale: str
    """The locale of the user"""
    name: str
    """Deprecated property"""
    self: str
    """The URL of the user"""
    time_zone: str
    """The time zone specified in the user's profile"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    account_id: AirbyteSortOrder
    """The account ID of the user, uniquely identifying the user across all Atlassian products"""
    account_type: AirbyteSortOrder
    """The user account type (atlassian, app, or customer)"""
    active: AirbyteSortOrder
    """Indicates whether the user is active"""
    application_roles: AirbyteSortOrder
    """The application roles assigned to the user"""
    avatar_urls: AirbyteSortOrder
    """The avatars of the user"""
    display_name: AirbyteSortOrder
    """The display name of the user"""
    email_address: AirbyteSortOrder
    """The email address of the user"""
    expand: AirbyteSortOrder
    """Options to include additional user details in the response"""
    groups: AirbyteSortOrder
    """The groups to which the user belongs"""
    key: AirbyteSortOrder
    """Deprecated property"""
    locale: AirbyteSortOrder
    """The locale of the user"""
    name: AirbyteSortOrder
    """Deprecated property"""
    self: AirbyteSortOrder
    """The URL of the user"""
    time_zone: AirbyteSortOrder
    """The time zone specified in the user's profile"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]


# ===== ISSUE_COMMENTS SEARCH TYPES =====

class IssueCommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering issue_comments search queries."""
    author: dict[str, Any] | None
    """The ID of the user who created the comment"""
    body: dict[str, Any]
    """The comment text in Atlassian Document Format"""
    created: str
    """The date and time at which the comment was created"""
    id: str
    """The ID of the comment"""
    issue_id: str | None
    """Id of the related issue"""
    jsd_public: bool
    """Whether the comment is visible in Jira Service Desk"""
    properties: list[Any]
    """A list of comment properties"""
    rendered_body: str | None
    """The rendered version of the comment"""
    self: str
    """The URL of the comment"""
    update_author: dict[str, Any] | None
    """The ID of the user who updated the comment last"""
    updated: str
    """The date and time at which the comment was updated last"""
    visibility: dict[str, Any] | None
    """The group or role to which this item is visible"""


class IssueCommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    author: list[dict[str, Any]]
    """The ID of the user who created the comment"""
    body: list[dict[str, Any]]
    """The comment text in Atlassian Document Format"""
    created: list[str]
    """The date and time at which the comment was created"""
    id: list[str]
    """The ID of the comment"""
    issue_id: list[str]
    """Id of the related issue"""
    jsd_public: list[bool]
    """Whether the comment is visible in Jira Service Desk"""
    properties: list[list[Any]]
    """A list of comment properties"""
    rendered_body: list[str]
    """The rendered version of the comment"""
    self: list[str]
    """The URL of the comment"""
    update_author: list[dict[str, Any]]
    """The ID of the user who updated the comment last"""
    updated: list[str]
    """The date and time at which the comment was updated last"""
    visibility: list[dict[str, Any]]
    """The group or role to which this item is visible"""


class IssueCommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    author: Any
    """The ID of the user who created the comment"""
    body: Any
    """The comment text in Atlassian Document Format"""
    created: Any
    """The date and time at which the comment was created"""
    id: Any
    """The ID of the comment"""
    issue_id: Any
    """Id of the related issue"""
    jsd_public: Any
    """Whether the comment is visible in Jira Service Desk"""
    properties: Any
    """A list of comment properties"""
    rendered_body: Any
    """The rendered version of the comment"""
    self: Any
    """The URL of the comment"""
    update_author: Any
    """The ID of the user who updated the comment last"""
    updated: Any
    """The date and time at which the comment was updated last"""
    visibility: Any
    """The group or role to which this item is visible"""


class IssueCommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    author: str
    """The ID of the user who created the comment"""
    body: str
    """The comment text in Atlassian Document Format"""
    created: str
    """The date and time at which the comment was created"""
    id: str
    """The ID of the comment"""
    issue_id: str
    """Id of the related issue"""
    jsd_public: str
    """Whether the comment is visible in Jira Service Desk"""
    properties: str
    """A list of comment properties"""
    rendered_body: str
    """The rendered version of the comment"""
    self: str
    """The URL of the comment"""
    update_author: str
    """The ID of the user who updated the comment last"""
    updated: str
    """The date and time at which the comment was updated last"""
    visibility: str
    """The group or role to which this item is visible"""


class IssueCommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting issue_comments search results."""
    author: AirbyteSortOrder
    """The ID of the user who created the comment"""
    body: AirbyteSortOrder
    """The comment text in Atlassian Document Format"""
    created: AirbyteSortOrder
    """The date and time at which the comment was created"""
    id: AirbyteSortOrder
    """The ID of the comment"""
    issue_id: AirbyteSortOrder
    """Id of the related issue"""
    jsd_public: AirbyteSortOrder
    """Whether the comment is visible in Jira Service Desk"""
    properties: AirbyteSortOrder
    """A list of comment properties"""
    rendered_body: AirbyteSortOrder
    """The rendered version of the comment"""
    self: AirbyteSortOrder
    """The URL of the comment"""
    update_author: AirbyteSortOrder
    """The ID of the user who updated the comment last"""
    updated: AirbyteSortOrder
    """The date and time at which the comment was updated last"""
    visibility: AirbyteSortOrder
    """The group or role to which this item is visible"""


# Entity-specific condition types for issue_comments
class IssueCommentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssueCommentsSearchFilter


class IssueCommentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssueCommentsSearchFilter


class IssueCommentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssueCommentsSearchFilter


class IssueCommentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssueCommentsSearchFilter


class IssueCommentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssueCommentsSearchFilter


class IssueCommentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssueCommentsSearchFilter


class IssueCommentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssueCommentsStringFilter


class IssueCommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssueCommentsStringFilter


class IssueCommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssueCommentsStringFilter


class IssueCommentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssueCommentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssueCommentsInCondition = TypedDict("IssueCommentsInCondition", {"in": IssueCommentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssueCommentsNotCondition = TypedDict("IssueCommentsNotCondition", {"not": "IssueCommentsCondition"}, total=False)
"""Negates the nested condition."""

IssueCommentsAndCondition = TypedDict("IssueCommentsAndCondition", {"and": "list[IssueCommentsCondition]"}, total=False)
"""True if all nested conditions are true."""

IssueCommentsOrCondition = TypedDict("IssueCommentsOrCondition", {"or": "list[IssueCommentsCondition]"}, total=False)
"""True if any nested condition is true."""

IssueCommentsAnyCondition = TypedDict("IssueCommentsAnyCondition", {"any": IssueCommentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issue_comments condition types
IssueCommentsCondition = (
    IssueCommentsEqCondition
    | IssueCommentsNeqCondition
    | IssueCommentsGtCondition
    | IssueCommentsGteCondition
    | IssueCommentsLtCondition
    | IssueCommentsLteCondition
    | IssueCommentsInCondition
    | IssueCommentsLikeCondition
    | IssueCommentsFuzzyCondition
    | IssueCommentsKeywordCondition
    | IssueCommentsContainsCondition
    | IssueCommentsNotCondition
    | IssueCommentsAndCondition
    | IssueCommentsOrCondition
    | IssueCommentsAnyCondition
)


class IssueCommentsSearchQuery(TypedDict, total=False):
    """Search query for issue_comments entity."""
    filter: IssueCommentsCondition
    sort: list[IssueCommentsSortFilter]


# ===== ISSUE_FIELDS SEARCH TYPES =====

class IssueFieldsSearchFilter(TypedDict, total=False):
    """Available fields for filtering issue_fields search queries."""
    clause_names: list[Any]
    """The names that can be used to reference the field in an advanced search"""
    custom: bool
    """Whether the field is a custom field"""
    id: str
    """The ID of the field"""
    key: str | None
    """The key of the field"""
    name: str
    """The name of the field"""
    navigable: bool
    """Whether the field can be used as a column on the issue navigator"""
    orderable: bool
    """Whether the content of the field can be used to order lists"""
    schema_: dict[str, Any] | None
    """The data schema for the field"""
    scope: dict[str, Any] | None
    """The scope of the field"""
    searchable: bool
    """Whether the content of the field can be searched"""
    untranslated_name: str | None
    """The untranslated name of the field"""


class IssueFieldsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clause_names: list[list[Any]]
    """The names that can be used to reference the field in an advanced search"""
    custom: list[bool]
    """Whether the field is a custom field"""
    id: list[str]
    """The ID of the field"""
    key: list[str]
    """The key of the field"""
    name: list[str]
    """The name of the field"""
    navigable: list[bool]
    """Whether the field can be used as a column on the issue navigator"""
    orderable: list[bool]
    """Whether the content of the field can be used to order lists"""
    schema_: list[dict[str, Any]]
    """The data schema for the field"""
    scope: list[dict[str, Any]]
    """The scope of the field"""
    searchable: list[bool]
    """Whether the content of the field can be searched"""
    untranslated_name: list[str]
    """The untranslated name of the field"""


class IssueFieldsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clause_names: Any
    """The names that can be used to reference the field in an advanced search"""
    custom: Any
    """Whether the field is a custom field"""
    id: Any
    """The ID of the field"""
    key: Any
    """The key of the field"""
    name: Any
    """The name of the field"""
    navigable: Any
    """Whether the field can be used as a column on the issue navigator"""
    orderable: Any
    """Whether the content of the field can be used to order lists"""
    schema_: Any
    """The data schema for the field"""
    scope: Any
    """The scope of the field"""
    searchable: Any
    """Whether the content of the field can be searched"""
    untranslated_name: Any
    """The untranslated name of the field"""


class IssueFieldsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clause_names: str
    """The names that can be used to reference the field in an advanced search"""
    custom: str
    """Whether the field is a custom field"""
    id: str
    """The ID of the field"""
    key: str
    """The key of the field"""
    name: str
    """The name of the field"""
    navigable: str
    """Whether the field can be used as a column on the issue navigator"""
    orderable: str
    """Whether the content of the field can be used to order lists"""
    schema_: str
    """The data schema for the field"""
    scope: str
    """The scope of the field"""
    searchable: str
    """Whether the content of the field can be searched"""
    untranslated_name: str
    """The untranslated name of the field"""


class IssueFieldsSortFilter(TypedDict, total=False):
    """Available fields for sorting issue_fields search results."""
    clause_names: AirbyteSortOrder
    """The names that can be used to reference the field in an advanced search"""
    custom: AirbyteSortOrder
    """Whether the field is a custom field"""
    id: AirbyteSortOrder
    """The ID of the field"""
    key: AirbyteSortOrder
    """The key of the field"""
    name: AirbyteSortOrder
    """The name of the field"""
    navigable: AirbyteSortOrder
    """Whether the field can be used as a column on the issue navigator"""
    orderable: AirbyteSortOrder
    """Whether the content of the field can be used to order lists"""
    schema_: AirbyteSortOrder
    """The data schema for the field"""
    scope: AirbyteSortOrder
    """The scope of the field"""
    searchable: AirbyteSortOrder
    """Whether the content of the field can be searched"""
    untranslated_name: AirbyteSortOrder
    """The untranslated name of the field"""


# Entity-specific condition types for issue_fields
class IssueFieldsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssueFieldsSearchFilter


class IssueFieldsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssueFieldsSearchFilter


class IssueFieldsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssueFieldsSearchFilter


class IssueFieldsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssueFieldsSearchFilter


class IssueFieldsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssueFieldsSearchFilter


class IssueFieldsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssueFieldsSearchFilter


class IssueFieldsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssueFieldsStringFilter


class IssueFieldsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssueFieldsStringFilter


class IssueFieldsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssueFieldsStringFilter


class IssueFieldsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssueFieldsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssueFieldsInCondition = TypedDict("IssueFieldsInCondition", {"in": IssueFieldsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssueFieldsNotCondition = TypedDict("IssueFieldsNotCondition", {"not": "IssueFieldsCondition"}, total=False)
"""Negates the nested condition."""

IssueFieldsAndCondition = TypedDict("IssueFieldsAndCondition", {"and": "list[IssueFieldsCondition]"}, total=False)
"""True if all nested conditions are true."""

IssueFieldsOrCondition = TypedDict("IssueFieldsOrCondition", {"or": "list[IssueFieldsCondition]"}, total=False)
"""True if any nested condition is true."""

IssueFieldsAnyCondition = TypedDict("IssueFieldsAnyCondition", {"any": IssueFieldsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issue_fields condition types
IssueFieldsCondition = (
    IssueFieldsEqCondition
    | IssueFieldsNeqCondition
    | IssueFieldsGtCondition
    | IssueFieldsGteCondition
    | IssueFieldsLtCondition
    | IssueFieldsLteCondition
    | IssueFieldsInCondition
    | IssueFieldsLikeCondition
    | IssueFieldsFuzzyCondition
    | IssueFieldsKeywordCondition
    | IssueFieldsContainsCondition
    | IssueFieldsNotCondition
    | IssueFieldsAndCondition
    | IssueFieldsOrCondition
    | IssueFieldsAnyCondition
)


class IssueFieldsSearchQuery(TypedDict, total=False):
    """Search query for issue_fields entity."""
    filter: IssueFieldsCondition
    sort: list[IssueFieldsSortFilter]


# ===== ISSUE_WORKLOGS SEARCH TYPES =====

class IssueWorklogsSearchFilter(TypedDict, total=False):
    """Available fields for filtering issue_worklogs search queries."""
    author: dict[str, Any]
    """Details of the user who created the worklog"""
    comment: dict[str, Any] | None
    """A comment about the worklog in Atlassian Document Format"""
    created: str
    """The datetime on which the worklog was created"""
    id: str
    """The ID of the worklog record"""
    issue_id: str
    """The ID of the issue this worklog is for"""
    properties: list[Any]
    """Details of properties for the worklog"""
    self: str
    """The URL of the worklog item"""
    started: str
    """The datetime on which the worklog effort was started"""
    time_spent: str | None
    """The time spent working on the issue as days, hours, or minutes"""
    time_spent_seconds: int
    """The time in seconds spent working on the issue"""
    update_author: dict[str, Any] | None
    """Details of the user who last updated the worklog"""
    updated: str
    """The datetime on which the worklog was last updated"""
    visibility: dict[str, Any] | None
    """Details about any restrictions in the visibility of the worklog"""


class IssueWorklogsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    author: list[dict[str, Any]]
    """Details of the user who created the worklog"""
    comment: list[dict[str, Any]]
    """A comment about the worklog in Atlassian Document Format"""
    created: list[str]
    """The datetime on which the worklog was created"""
    id: list[str]
    """The ID of the worklog record"""
    issue_id: list[str]
    """The ID of the issue this worklog is for"""
    properties: list[list[Any]]
    """Details of properties for the worklog"""
    self: list[str]
    """The URL of the worklog item"""
    started: list[str]
    """The datetime on which the worklog effort was started"""
    time_spent: list[str]
    """The time spent working on the issue as days, hours, or minutes"""
    time_spent_seconds: list[int]
    """The time in seconds spent working on the issue"""
    update_author: list[dict[str, Any]]
    """Details of the user who last updated the worklog"""
    updated: list[str]
    """The datetime on which the worklog was last updated"""
    visibility: list[dict[str, Any]]
    """Details about any restrictions in the visibility of the worklog"""


class IssueWorklogsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    author: Any
    """Details of the user who created the worklog"""
    comment: Any
    """A comment about the worklog in Atlassian Document Format"""
    created: Any
    """The datetime on which the worklog was created"""
    id: Any
    """The ID of the worklog record"""
    issue_id: Any
    """The ID of the issue this worklog is for"""
    properties: Any
    """Details of properties for the worklog"""
    self: Any
    """The URL of the worklog item"""
    started: Any
    """The datetime on which the worklog effort was started"""
    time_spent: Any
    """The time spent working on the issue as days, hours, or minutes"""
    time_spent_seconds: Any
    """The time in seconds spent working on the issue"""
    update_author: Any
    """Details of the user who last updated the worklog"""
    updated: Any
    """The datetime on which the worklog was last updated"""
    visibility: Any
    """Details about any restrictions in the visibility of the worklog"""


class IssueWorklogsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    author: str
    """Details of the user who created the worklog"""
    comment: str
    """A comment about the worklog in Atlassian Document Format"""
    created: str
    """The datetime on which the worklog was created"""
    id: str
    """The ID of the worklog record"""
    issue_id: str
    """The ID of the issue this worklog is for"""
    properties: str
    """Details of properties for the worklog"""
    self: str
    """The URL of the worklog item"""
    started: str
    """The datetime on which the worklog effort was started"""
    time_spent: str
    """The time spent working on the issue as days, hours, or minutes"""
    time_spent_seconds: str
    """The time in seconds spent working on the issue"""
    update_author: str
    """Details of the user who last updated the worklog"""
    updated: str
    """The datetime on which the worklog was last updated"""
    visibility: str
    """Details about any restrictions in the visibility of the worklog"""


class IssueWorklogsSortFilter(TypedDict, total=False):
    """Available fields for sorting issue_worklogs search results."""
    author: AirbyteSortOrder
    """Details of the user who created the worklog"""
    comment: AirbyteSortOrder
    """A comment about the worklog in Atlassian Document Format"""
    created: AirbyteSortOrder
    """The datetime on which the worklog was created"""
    id: AirbyteSortOrder
    """The ID of the worklog record"""
    issue_id: AirbyteSortOrder
    """The ID of the issue this worklog is for"""
    properties: AirbyteSortOrder
    """Details of properties for the worklog"""
    self: AirbyteSortOrder
    """The URL of the worklog item"""
    started: AirbyteSortOrder
    """The datetime on which the worklog effort was started"""
    time_spent: AirbyteSortOrder
    """The time spent working on the issue as days, hours, or minutes"""
    time_spent_seconds: AirbyteSortOrder
    """The time in seconds spent working on the issue"""
    update_author: AirbyteSortOrder
    """Details of the user who last updated the worklog"""
    updated: AirbyteSortOrder
    """The datetime on which the worklog was last updated"""
    visibility: AirbyteSortOrder
    """Details about any restrictions in the visibility of the worklog"""


# Entity-specific condition types for issue_worklogs
class IssueWorklogsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssueWorklogsSearchFilter


class IssueWorklogsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssueWorklogsSearchFilter


class IssueWorklogsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssueWorklogsSearchFilter


class IssueWorklogsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssueWorklogsSearchFilter


class IssueWorklogsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssueWorklogsSearchFilter


class IssueWorklogsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssueWorklogsSearchFilter


class IssueWorklogsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssueWorklogsStringFilter


class IssueWorklogsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssueWorklogsStringFilter


class IssueWorklogsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssueWorklogsStringFilter


class IssueWorklogsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssueWorklogsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssueWorklogsInCondition = TypedDict("IssueWorklogsInCondition", {"in": IssueWorklogsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssueWorklogsNotCondition = TypedDict("IssueWorklogsNotCondition", {"not": "IssueWorklogsCondition"}, total=False)
"""Negates the nested condition."""

IssueWorklogsAndCondition = TypedDict("IssueWorklogsAndCondition", {"and": "list[IssueWorklogsCondition]"}, total=False)
"""True if all nested conditions are true."""

IssueWorklogsOrCondition = TypedDict("IssueWorklogsOrCondition", {"or": "list[IssueWorklogsCondition]"}, total=False)
"""True if any nested condition is true."""

IssueWorklogsAnyCondition = TypedDict("IssueWorklogsAnyCondition", {"any": IssueWorklogsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issue_worklogs condition types
IssueWorklogsCondition = (
    IssueWorklogsEqCondition
    | IssueWorklogsNeqCondition
    | IssueWorklogsGtCondition
    | IssueWorklogsGteCondition
    | IssueWorklogsLtCondition
    | IssueWorklogsLteCondition
    | IssueWorklogsInCondition
    | IssueWorklogsLikeCondition
    | IssueWorklogsFuzzyCondition
    | IssueWorklogsKeywordCondition
    | IssueWorklogsContainsCondition
    | IssueWorklogsNotCondition
    | IssueWorklogsAndCondition
    | IssueWorklogsOrCondition
    | IssueWorklogsAnyCondition
)


class IssueWorklogsSearchQuery(TypedDict, total=False):
    """Search query for issue_worklogs entity."""
    filter: IssueWorklogsCondition
    sort: list[IssueWorklogsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
