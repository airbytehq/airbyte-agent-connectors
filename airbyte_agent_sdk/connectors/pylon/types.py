"""
Type definitions for pylon connector.
"""
# ruff: noqa: E501
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    start_time: str
    end_time: str
    cursor: NotRequired[str]

class IssuesCreateParams(TypedDict):
    """Parameters for issues.create operation"""
    title: str
    body_html: str
    priority: NotRequired[str]
    requester_email: NotRequired[str]
    requester_name: NotRequired[str]
    account_id: NotRequired[str]
    assignee_id: NotRequired[str]
    team_id: NotRequired[str]
    tags: NotRequired[list[str]]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    id: str

class IssuesUpdateParams(TypedDict):
    """Parameters for issues.update operation"""
    state: NotRequired[str]
    assignee_id: NotRequired[str]
    team_id: NotRequired[str]
    account_id: NotRequired[str]
    tags: NotRequired[list[str]]
    id: str

class IssueRepliesCreateParams(TypedDict):
    """Parameters for issue_replies.create operation"""
    body_html: str
    message_id: str
    user_id: NotRequired[str]
    contact_id: NotRequired[str]
    attachment_urls: NotRequired[list[str]]
    id: str

class IssueAssignmentsUpdateParams(TypedDict):
    """Parameters for issue_assignments.update operation"""
    assignee_id: NotRequired[str]
    team_id: NotRequired[str]
    id: str

class IssueStatusesUpdateParams(TypedDict):
    """Parameters for issue_statuses.update operation"""
    state: str
    id: str

class IssuesDeleteParams(TypedDict):
    """Parameters for issues.delete operation"""
    id: str

class MessagesListParams(TypedDict):
    """Parameters for messages.list operation"""
    id: str
    cursor: NotRequired[str]

class IssueNotesCreateParams(TypedDict):
    """Parameters for issue_notes.create operation"""
    body_html: str
    thread_id: NotRequired[str]
    message_id: NotRequired[str]
    id: str

class IssueThreadsCreateParams(TypedDict):
    """Parameters for issue_threads.create operation"""
    name: NotRequired[str]
    id: str

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    cursor: NotRequired[str]

class AccountsCreateParams(TypedDict):
    """Parameters for accounts.create operation"""
    name: str
    domains: NotRequired[list[str]]
    primary_domain: NotRequired[str]
    owner_id: NotRequired[str]
    logo_url: NotRequired[str]
    tags: NotRequired[list[str]]

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str

class AccountsUpdateParams(TypedDict):
    """Parameters for accounts.update operation"""
    name: NotRequired[str]
    domains: NotRequired[list[str]]
    primary_domain: NotRequired[str]
    owner_id: NotRequired[str]
    logo_url: NotRequired[str]
    is_disabled: NotRequired[bool]
    tags: NotRequired[list[str]]
    id: str

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    cursor: NotRequired[str]

class ContactsCreateParams(TypedDict):
    """Parameters for contacts.create operation"""
    name: str
    email: NotRequired[str]
    account_id: NotRequired[str]
    avatar_url: NotRequired[str]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class ContactsUpdateParams(TypedDict):
    """Parameters for contacts.update operation"""
    name: NotRequired[str]
    email: NotRequired[str]
    account_id: NotRequired[str]
    id: str

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    cursor: NotRequired[str]

class TeamsCreateParams(TypedDict):
    """Parameters for teams.create operation"""
    name: NotRequired[str]

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    id: str

class TeamsUpdateParams(TypedDict):
    """Parameters for teams.update operation"""
    name: NotRequired[str]
    id: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    cursor: NotRequired[str]

class TagsCreateParams(TypedDict):
    """Parameters for tags.create operation"""
    value: str
    object_type: str
    hex_color: NotRequired[str]

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    id: str

class TagsUpdateParams(TypedDict):
    """Parameters for tags.update operation"""
    value: NotRequired[str]
    hex_color: NotRequired[str]
    id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CustomFieldsListParams(TypedDict):
    """Parameters for custom_fields.list operation"""
    object_type: str
    cursor: NotRequired[str]

class CustomFieldsGetParams(TypedDict):
    """Parameters for custom_fields.get operation"""
    id: str

class TicketFormsListParams(TypedDict):
    """Parameters for ticket_forms.list operation"""
    cursor: NotRequired[str]

class UserRolesListParams(TypedDict):
    """Parameters for user_roles.list operation"""
    cursor: NotRequired[str]

class TasksCreateParams(TypedDict):
    """Parameters for tasks.create operation"""
    title: str
    body_html: NotRequired[str]
    status: NotRequired[str]
    assignee_id: NotRequired[str]
    project_id: NotRequired[str]
    milestone_id: NotRequired[str]
    due_date: NotRequired[str]

class TasksUpdateParams(TypedDict):
    """Parameters for tasks.update operation"""
    title: NotRequired[str]
    body_html: NotRequired[str]
    status: NotRequired[str]
    assignee_id: NotRequired[str]
    id: str

class ProjectsCreateParams(TypedDict):
    """Parameters for projects.create operation"""
    name: str
    account_id: str
    description_html: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]

class ProjectsUpdateParams(TypedDict):
    """Parameters for projects.update operation"""
    name: NotRequired[str]
    description_html: NotRequired[str]
    is_archived: NotRequired[bool]
    id: str

class MilestonesCreateParams(TypedDict):
    """Parameters for milestones.create operation"""
    name: str
    project_id: str
    due_date: NotRequired[str]

class MilestonesUpdateParams(TypedDict):
    """Parameters for milestones.update operation"""
    name: NotRequired[str]
    due_date: NotRequired[str]
    id: str

class ArticlesCreateParams(TypedDict):
    """Parameters for articles.create operation"""
    title: str
    body_html: str
    author_user_id: str
    slug: NotRequired[str]
    is_published: NotRequired[bool]
    kb_id: str

class ArticlesUpdateParams(TypedDict):
    """Parameters for articles.update operation"""
    title: NotRequired[str]
    body_html: NotRequired[str]
    kb_id: str
    article_id: str

class CollectionsCreateParams(TypedDict):
    """Parameters for collections.create operation"""
    title: str
    description: NotRequired[str]
    slug: NotRequired[str]
    kb_id: str

class MeGetParams(TypedDict):
    """Parameters for me.get operation"""
    pass

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    id: str
    """Unique identifier for the issue"""
    title: str | None
    """Title of the issue"""
    state: str | None
    """Current state of the issue (e.g. new, in_progress, closed)"""
    source: str | None
    """Channel the issue originated from (e.g. email, slack)"""
    type_: str | None
    """Type classification of the issue"""
    number: int | None
    """Human-readable issue number within the workspace"""
    created_at: str | None
    """Timestamp when the issue was created, in ISO 8601 format"""
    latest_message_time: str | None
    """Timestamp of the most recent message on the issue, in ISO 8601 format"""
    resolution_time: str | None
    """Timestamp when the issue was resolved, in ISO 8601 format"""
    snoozed_until_time: str | None
    """Timestamp the issue is snoozed until, in ISO 8601 format"""
    customer_portal_visible: bool | None
    """Whether the issue is visible in the customer portal"""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the issue"""
    title: list[str]
    """Title of the issue"""
    state: list[str]
    """Current state of the issue (e.g. new, in_progress, closed)"""
    source: list[str]
    """Channel the issue originated from (e.g. email, slack)"""
    type_: list[str]
    """Type classification of the issue"""
    number: list[int]
    """Human-readable issue number within the workspace"""
    created_at: list[str]
    """Timestamp when the issue was created, in ISO 8601 format"""
    latest_message_time: list[str]
    """Timestamp of the most recent message on the issue, in ISO 8601 format"""
    resolution_time: list[str]
    """Timestamp when the issue was resolved, in ISO 8601 format"""
    snoozed_until_time: list[str]
    """Timestamp the issue is snoozed until, in ISO 8601 format"""
    customer_portal_visible: list[bool]
    """Whether the issue is visible in the customer portal"""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the issue"""
    title: Any
    """Title of the issue"""
    state: Any
    """Current state of the issue (e.g. new, in_progress, closed)"""
    source: Any
    """Channel the issue originated from (e.g. email, slack)"""
    type_: Any
    """Type classification of the issue"""
    number: Any
    """Human-readable issue number within the workspace"""
    created_at: Any
    """Timestamp when the issue was created, in ISO 8601 format"""
    latest_message_time: Any
    """Timestamp of the most recent message on the issue, in ISO 8601 format"""
    resolution_time: Any
    """Timestamp when the issue was resolved, in ISO 8601 format"""
    snoozed_until_time: Any
    """Timestamp the issue is snoozed until, in ISO 8601 format"""
    customer_portal_visible: Any
    """Whether the issue is visible in the customer portal"""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the issue"""
    title: str
    """Title of the issue"""
    state: str
    """Current state of the issue (e.g. new, in_progress, closed)"""
    source: str
    """Channel the issue originated from (e.g. email, slack)"""
    type_: str
    """Type classification of the issue"""
    number: str
    """Human-readable issue number within the workspace"""
    created_at: str
    """Timestamp when the issue was created, in ISO 8601 format"""
    latest_message_time: str
    """Timestamp of the most recent message on the issue, in ISO 8601 format"""
    resolution_time: str
    """Timestamp when the issue was resolved, in ISO 8601 format"""
    snoozed_until_time: str
    """Timestamp the issue is snoozed until, in ISO 8601 format"""
    customer_portal_visible: str
    """Whether the issue is visible in the customer portal"""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    id: AirbyteSortOrder
    """Unique identifier for the issue"""
    title: AirbyteSortOrder
    """Title of the issue"""
    state: AirbyteSortOrder
    """Current state of the issue (e.g. new, in_progress, closed)"""
    source: AirbyteSortOrder
    """Channel the issue originated from (e.g. email, slack)"""
    type_: AirbyteSortOrder
    """Type classification of the issue"""
    number: AirbyteSortOrder
    """Human-readable issue number within the workspace"""
    created_at: AirbyteSortOrder
    """Timestamp when the issue was created, in ISO 8601 format"""
    latest_message_time: AirbyteSortOrder
    """Timestamp of the most recent message on the issue, in ISO 8601 format"""
    resolution_time: AirbyteSortOrder
    """Timestamp when the issue was resolved, in ISO 8601 format"""
    snoozed_until_time: AirbyteSortOrder
    """Timestamp the issue is snoozed until, in ISO 8601 format"""
    customer_portal_visible: AirbyteSortOrder
    """Whether the issue is visible in the customer portal"""


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


class IssuesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: IssuesStringFilter


class IssuesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: IssuesStringFilter


class IssuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssuesStringFilter


class IssuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssuesStringFilter


class IssuesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | IssuesStartswithCondition
    | IssuesEndswithCondition
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


# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    id: str
    """Unique identifier for the account"""
    name: str | None
    """Name of the account (customer organization)"""
    domain: str | None
    """Primary domain associated with the account"""
    primary_domain: str | None
    """Canonical primary domain for the account"""
    type_: str | None
    """Classification of the account (e.g. customer, prospect)"""
    is_disabled: bool | None
    """Whether the account has been disabled"""
    created_at: str | None
    """Timestamp when the account was created, in ISO 8601 format"""
    latest_customer_activity_time: str | None
    """Timestamp of the most recent activity from this account, in ISO 8601 format"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the account"""
    name: list[str]
    """Name of the account (customer organization)"""
    domain: list[str]
    """Primary domain associated with the account"""
    primary_domain: list[str]
    """Canonical primary domain for the account"""
    type_: list[str]
    """Classification of the account (e.g. customer, prospect)"""
    is_disabled: list[bool]
    """Whether the account has been disabled"""
    created_at: list[str]
    """Timestamp when the account was created, in ISO 8601 format"""
    latest_customer_activity_time: list[str]
    """Timestamp of the most recent activity from this account, in ISO 8601 format"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the account"""
    name: Any
    """Name of the account (customer organization)"""
    domain: Any
    """Primary domain associated with the account"""
    primary_domain: Any
    """Canonical primary domain for the account"""
    type_: Any
    """Classification of the account (e.g. customer, prospect)"""
    is_disabled: Any
    """Whether the account has been disabled"""
    created_at: Any
    """Timestamp when the account was created, in ISO 8601 format"""
    latest_customer_activity_time: Any
    """Timestamp of the most recent activity from this account, in ISO 8601 format"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the account"""
    name: str
    """Name of the account (customer organization)"""
    domain: str
    """Primary domain associated with the account"""
    primary_domain: str
    """Canonical primary domain for the account"""
    type_: str
    """Classification of the account (e.g. customer, prospect)"""
    is_disabled: str
    """Whether the account has been disabled"""
    created_at: str
    """Timestamp when the account was created, in ISO 8601 format"""
    latest_customer_activity_time: str
    """Timestamp of the most recent activity from this account, in ISO 8601 format"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    id: AirbyteSortOrder
    """Unique identifier for the account"""
    name: AirbyteSortOrder
    """Name of the account (customer organization)"""
    domain: AirbyteSortOrder
    """Primary domain associated with the account"""
    primary_domain: AirbyteSortOrder
    """Canonical primary domain for the account"""
    type_: AirbyteSortOrder
    """Classification of the account (e.g. customer, prospect)"""
    is_disabled: AirbyteSortOrder
    """Whether the account has been disabled"""
    created_at: AirbyteSortOrder
    """Timestamp when the account was created, in ISO 8601 format"""
    latest_customer_activity_time: AirbyteSortOrder
    """Timestamp of the most recent activity from this account, in ISO 8601 format"""


# Entity-specific condition types for accounts
class AccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountsSearchFilter


class AccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountsSearchFilter


class AccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountsSearchFilter


class AccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountsSearchFilter


class AccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountsSearchFilter


class AccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountsSearchFilter


class AccountsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AccountsStringFilter


class AccountsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AccountsStringFilter


class AccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountsStringFilter


class AccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountsStringFilter


class AccountsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountsInCondition = TypedDict("AccountsInCondition", {"in": AccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountsNotCondition = TypedDict("AccountsNotCondition", {"not": "AccountsCondition"}, total=False)
"""Negates the nested condition."""

AccountsAndCondition = TypedDict("AccountsAndCondition", {"and": "list[AccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountsOrCondition = TypedDict("AccountsOrCondition", {"or": "list[AccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AccountsAnyCondition = TypedDict("AccountsAnyCondition", {"any": AccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all accounts condition types
AccountsCondition = (
    AccountsEqCondition
    | AccountsNeqCondition
    | AccountsGtCondition
    | AccountsGteCondition
    | AccountsLtCondition
    | AccountsLteCondition
    | AccountsInCondition
    | AccountsStartswithCondition
    | AccountsEndswithCondition
    | AccountsFuzzyCondition
    | AccountsKeywordCondition
    | AccountsContainsCondition
    | AccountsNotCondition
    | AccountsAndCondition
    | AccountsOrCondition
    | AccountsAnyCondition
)


class AccountsSearchQuery(TypedDict, total=False):
    """Search query for accounts entity."""
    filter: AccountsCondition
    sort: list[AccountsSortFilter]


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    id: str
    """Unique identifier for the contact"""
    name: str | None
    """Full name of the contact"""
    email: str | None
    """Primary email address of the contact"""
    primary_phone_number: str | None
    """Primary phone number of the contact"""
    portal_role: str | None
    """Role the contact has in the customer portal"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the contact"""
    name: list[str]
    """Full name of the contact"""
    email: list[str]
    """Primary email address of the contact"""
    primary_phone_number: list[str]
    """Primary phone number of the contact"""
    portal_role: list[str]
    """Role the contact has in the customer portal"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the contact"""
    name: Any
    """Full name of the contact"""
    email: Any
    """Primary email address of the contact"""
    primary_phone_number: Any
    """Primary phone number of the contact"""
    portal_role: Any
    """Role the contact has in the customer portal"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the contact"""
    name: str
    """Full name of the contact"""
    email: str
    """Primary email address of the contact"""
    primary_phone_number: str
    """Primary phone number of the contact"""
    portal_role: str
    """Role the contact has in the customer portal"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    id: AirbyteSortOrder
    """Unique identifier for the contact"""
    name: AirbyteSortOrder
    """Full name of the contact"""
    email: AirbyteSortOrder
    """Primary email address of the contact"""
    primary_phone_number: AirbyteSortOrder
    """Primary phone number of the contact"""
    portal_role: AirbyteSortOrder
    """Role the contact has in the customer portal"""


# Entity-specific condition types for contacts
class ContactsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ContactsSearchFilter


class ContactsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ContactsSearchFilter


class ContactsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ContactsSearchFilter


class ContactsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ContactsSearchFilter


class ContactsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ContactsSearchFilter


class ContactsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ContactsSearchFilter


class ContactsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ContactsStringFilter


class ContactsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ContactsStringFilter


class ContactsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ContactsStringFilter


class ContactsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ContactsStringFilter


class ContactsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: ContactsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ContactsInCondition = TypedDict("ContactsInCondition", {"in": ContactsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ContactsNotCondition = TypedDict("ContactsNotCondition", {"not": "ContactsCondition"}, total=False)
"""Negates the nested condition."""

ContactsAndCondition = TypedDict("ContactsAndCondition", {"and": "list[ContactsCondition]"}, total=False)
"""True if all nested conditions are true."""

ContactsOrCondition = TypedDict("ContactsOrCondition", {"or": "list[ContactsCondition]"}, total=False)
"""True if any nested condition is true."""

ContactsAnyCondition = TypedDict("ContactsAnyCondition", {"any": ContactsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all contacts condition types
ContactsCondition = (
    ContactsEqCondition
    | ContactsNeqCondition
    | ContactsGtCondition
    | ContactsGteCondition
    | ContactsLtCondition
    | ContactsLteCondition
    | ContactsInCondition
    | ContactsStartswithCondition
    | ContactsEndswithCondition
    | ContactsFuzzyCondition
    | ContactsKeywordCondition
    | ContactsContainsCondition
    | ContactsNotCondition
    | ContactsAndCondition
    | ContactsOrCondition
    | ContactsAnyCondition
)


class ContactsSearchQuery(TypedDict, total=False):
    """Search query for contacts entity."""
    filter: ContactsCondition
    sort: list[ContactsSortFilter]


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    id: str
    """Unique identifier for the team"""
    name: str | None
    """Name of the team"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the team"""
    name: list[str]
    """Name of the team"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the team"""
    name: Any
    """Name of the team"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the team"""
    name: str
    """Name of the team"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    id: AirbyteSortOrder
    """Unique identifier for the team"""
    name: AirbyteSortOrder
    """Name of the team"""


# Entity-specific condition types for teams
class TeamsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TeamsSearchFilter


class TeamsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TeamsSearchFilter


class TeamsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TeamsSearchFilter


class TeamsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TeamsSearchFilter


class TeamsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TeamsSearchFilter


class TeamsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TeamsSearchFilter


class TeamsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TeamsStringFilter


class TeamsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TeamsStringFilter


class TeamsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TeamsStringFilter


class TeamsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TeamsStringFilter


class TeamsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: TeamsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TeamsInCondition = TypedDict("TeamsInCondition", {"in": TeamsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TeamsNotCondition = TypedDict("TeamsNotCondition", {"not": "TeamsCondition"}, total=False)
"""Negates the nested condition."""

TeamsAndCondition = TypedDict("TeamsAndCondition", {"and": "list[TeamsCondition]"}, total=False)
"""True if all nested conditions are true."""

TeamsOrCondition = TypedDict("TeamsOrCondition", {"or": "list[TeamsCondition]"}, total=False)
"""True if any nested condition is true."""

TeamsAnyCondition = TypedDict("TeamsAnyCondition", {"any": TeamsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all teams condition types
TeamsCondition = (
    TeamsEqCondition
    | TeamsNeqCondition
    | TeamsGtCondition
    | TeamsGteCondition
    | TeamsLtCondition
    | TeamsLteCondition
    | TeamsInCondition
    | TeamsStartswithCondition
    | TeamsEndswithCondition
    | TeamsFuzzyCondition
    | TeamsKeywordCondition
    | TeamsContainsCondition
    | TeamsNotCondition
    | TeamsAndCondition
    | TeamsOrCondition
    | TeamsAnyCondition
)


class TeamsSearchQuery(TypedDict, total=False):
    """Search query for teams entity."""
    filter: TeamsCondition
    sort: list[TeamsSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    id: str
    """Unique identifier for the tag"""
    value: str | None
    """Display value of the tag"""
    object_type: str | None
    """Type of object this tag applies to (e.g. issue, account)"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the tag"""
    value: list[str]
    """Display value of the tag"""
    object_type: list[str]
    """Type of object this tag applies to (e.g. issue, account)"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the tag"""
    value: Any
    """Display value of the tag"""
    object_type: Any
    """Type of object this tag applies to (e.g. issue, account)"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the tag"""
    value: str
    """Display value of the tag"""
    object_type: str
    """Type of object this tag applies to (e.g. issue, account)"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    id: AirbyteSortOrder
    """Unique identifier for the tag"""
    value: AirbyteSortOrder
    """Display value of the tag"""
    object_type: AirbyteSortOrder
    """Type of object this tag applies to (e.g. issue, account)"""


# Entity-specific condition types for tags
class TagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TagsSearchFilter


class TagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TagsSearchFilter


class TagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TagsSearchFilter


class TagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TagsSearchFilter


class TagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TagsSearchFilter


class TagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TagsSearchFilter


class TagsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TagsStringFilter


class TagsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TagsStringFilter


class TagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TagsStringFilter


class TagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TagsStringFilter


class TagsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: TagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TagsInCondition = TypedDict("TagsInCondition", {"in": TagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TagsNotCondition = TypedDict("TagsNotCondition", {"not": "TagsCondition"}, total=False)
"""Negates the nested condition."""

TagsAndCondition = TypedDict("TagsAndCondition", {"and": "list[TagsCondition]"}, total=False)
"""True if all nested conditions are true."""

TagsOrCondition = TypedDict("TagsOrCondition", {"or": "list[TagsCondition]"}, total=False)
"""True if any nested condition is true."""

TagsAnyCondition = TypedDict("TagsAnyCondition", {"any": TagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tags condition types
TagsCondition = (
    TagsEqCondition
    | TagsNeqCondition
    | TagsGtCondition
    | TagsGteCondition
    | TagsLtCondition
    | TagsLteCondition
    | TagsInCondition
    | TagsStartswithCondition
    | TagsEndswithCondition
    | TagsFuzzyCondition
    | TagsKeywordCondition
    | TagsContainsCondition
    | TagsNotCondition
    | TagsAndCondition
    | TagsOrCondition
    | TagsAnyCondition
)


class TagsSearchQuery(TypedDict, total=False):
    """Search query for tags entity."""
    filter: TagsCondition
    sort: list[TagsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    id: str
    """Unique identifier for the user"""
    name: str | None
    """Full name of the user"""
    email: str | None
    """Primary email address of the user"""
    role_id: str | None
    """Identifier of the user's role"""
    status: str | None
    """Current status of the user (e.g. active, disabled)"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the user"""
    name: list[str]
    """Full name of the user"""
    email: list[str]
    """Primary email address of the user"""
    role_id: list[str]
    """Identifier of the user's role"""
    status: list[str]
    """Current status of the user (e.g. active, disabled)"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the user"""
    name: Any
    """Full name of the user"""
    email: Any
    """Primary email address of the user"""
    role_id: Any
    """Identifier of the user's role"""
    status: Any
    """Current status of the user (e.g. active, disabled)"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the user"""
    name: str
    """Full name of the user"""
    email: str
    """Primary email address of the user"""
    role_id: str
    """Identifier of the user's role"""
    status: str
    """Current status of the user (e.g. active, disabled)"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    name: AirbyteSortOrder
    """Full name of the user"""
    email: AirbyteSortOrder
    """Primary email address of the user"""
    role_id: AirbyteSortOrder
    """Identifier of the user's role"""
    status: AirbyteSortOrder
    """Current status of the user (e.g. active, disabled)"""


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


class UsersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UsersStringFilter


class UsersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | UsersStartswithCondition
    | UsersEndswithCondition
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


# ===== CUSTOM_FIELDS SEARCH TYPES =====

class CustomFieldsSearchFilter(TypedDict, total=False):
    """Available fields for filtering custom_fields search queries."""
    id: str
    """Unique identifier for the custom field"""
    label: str | None
    """Display label of the custom field"""
    slug: str | None
    """URL-safe identifier for the custom field"""
    type_: str | None
    """Data type of the custom field (e.g. text, select)"""
    object_type: str | None
    """Type of object this custom field applies to (e.g. issue, account)"""
    is_read_only: bool | None
    """Whether the custom field is read-only"""
    created_at: str | None
    """Timestamp when the custom field was created, in ISO 8601 format"""


class CustomFieldsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the custom field"""
    label: list[str]
    """Display label of the custom field"""
    slug: list[str]
    """URL-safe identifier for the custom field"""
    type_: list[str]
    """Data type of the custom field (e.g. text, select)"""
    object_type: list[str]
    """Type of object this custom field applies to (e.g. issue, account)"""
    is_read_only: list[bool]
    """Whether the custom field is read-only"""
    created_at: list[str]
    """Timestamp when the custom field was created, in ISO 8601 format"""


class CustomFieldsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the custom field"""
    label: Any
    """Display label of the custom field"""
    slug: Any
    """URL-safe identifier for the custom field"""
    type_: Any
    """Data type of the custom field (e.g. text, select)"""
    object_type: Any
    """Type of object this custom field applies to (e.g. issue, account)"""
    is_read_only: Any
    """Whether the custom field is read-only"""
    created_at: Any
    """Timestamp when the custom field was created, in ISO 8601 format"""


class CustomFieldsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the custom field"""
    label: str
    """Display label of the custom field"""
    slug: str
    """URL-safe identifier for the custom field"""
    type_: str
    """Data type of the custom field (e.g. text, select)"""
    object_type: str
    """Type of object this custom field applies to (e.g. issue, account)"""
    is_read_only: str
    """Whether the custom field is read-only"""
    created_at: str
    """Timestamp when the custom field was created, in ISO 8601 format"""


class CustomFieldsSortFilter(TypedDict, total=False):
    """Available fields for sorting custom_fields search results."""
    id: AirbyteSortOrder
    """Unique identifier for the custom field"""
    label: AirbyteSortOrder
    """Display label of the custom field"""
    slug: AirbyteSortOrder
    """URL-safe identifier for the custom field"""
    type_: AirbyteSortOrder
    """Data type of the custom field (e.g. text, select)"""
    object_type: AirbyteSortOrder
    """Type of object this custom field applies to (e.g. issue, account)"""
    is_read_only: AirbyteSortOrder
    """Whether the custom field is read-only"""
    created_at: AirbyteSortOrder
    """Timestamp when the custom field was created, in ISO 8601 format"""


# Entity-specific condition types for custom_fields
class CustomFieldsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomFieldsSearchFilter


class CustomFieldsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomFieldsSearchFilter


class CustomFieldsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomFieldsSearchFilter


class CustomFieldsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomFieldsSearchFilter


class CustomFieldsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomFieldsSearchFilter


class CustomFieldsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomFieldsSearchFilter


class CustomFieldsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CustomFieldsStringFilter


class CustomFieldsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CustomFieldsStringFilter


class CustomFieldsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomFieldsStringFilter


class CustomFieldsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomFieldsStringFilter


class CustomFieldsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: CustomFieldsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomFieldsInCondition = TypedDict("CustomFieldsInCondition", {"in": CustomFieldsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomFieldsNotCondition = TypedDict("CustomFieldsNotCondition", {"not": "CustomFieldsCondition"}, total=False)
"""Negates the nested condition."""

CustomFieldsAndCondition = TypedDict("CustomFieldsAndCondition", {"and": "list[CustomFieldsCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomFieldsOrCondition = TypedDict("CustomFieldsOrCondition", {"or": "list[CustomFieldsCondition]"}, total=False)
"""True if any nested condition is true."""

CustomFieldsAnyCondition = TypedDict("CustomFieldsAnyCondition", {"any": CustomFieldsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all custom_fields condition types
CustomFieldsCondition = (
    CustomFieldsEqCondition
    | CustomFieldsNeqCondition
    | CustomFieldsGtCondition
    | CustomFieldsGteCondition
    | CustomFieldsLtCondition
    | CustomFieldsLteCondition
    | CustomFieldsInCondition
    | CustomFieldsStartswithCondition
    | CustomFieldsEndswithCondition
    | CustomFieldsFuzzyCondition
    | CustomFieldsKeywordCondition
    | CustomFieldsContainsCondition
    | CustomFieldsNotCondition
    | CustomFieldsAndCondition
    | CustomFieldsOrCondition
    | CustomFieldsAnyCondition
)


class CustomFieldsSearchQuery(TypedDict, total=False):
    """Search query for custom_fields entity."""
    filter: CustomFieldsCondition
    sort: list[CustomFieldsSortFilter]


# ===== TICKET_FORMS SEARCH TYPES =====

class TicketFormsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_forms search queries."""
    id: str
    """Unique identifier for the ticket form"""
    name: str | None
    """Display name of the ticket form"""
    slug: str | None
    """URL-safe identifier for the ticket form"""
    is_public: bool | None
    """Whether the ticket form is publicly accessible"""


class TicketFormsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the ticket form"""
    name: list[str]
    """Display name of the ticket form"""
    slug: list[str]
    """URL-safe identifier for the ticket form"""
    is_public: list[bool]
    """Whether the ticket form is publicly accessible"""


class TicketFormsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the ticket form"""
    name: Any
    """Display name of the ticket form"""
    slug: Any
    """URL-safe identifier for the ticket form"""
    is_public: Any
    """Whether the ticket form is publicly accessible"""


class TicketFormsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the ticket form"""
    name: str
    """Display name of the ticket form"""
    slug: str
    """URL-safe identifier for the ticket form"""
    is_public: str
    """Whether the ticket form is publicly accessible"""


class TicketFormsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_forms search results."""
    id: AirbyteSortOrder
    """Unique identifier for the ticket form"""
    name: AirbyteSortOrder
    """Display name of the ticket form"""
    slug: AirbyteSortOrder
    """URL-safe identifier for the ticket form"""
    is_public: AirbyteSortOrder
    """Whether the ticket form is publicly accessible"""


# Entity-specific condition types for ticket_forms
class TicketFormsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketFormsSearchFilter


class TicketFormsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketFormsSearchFilter


class TicketFormsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketFormsSearchFilter


class TicketFormsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketFormsSearchFilter


class TicketFormsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketFormsSearchFilter


class TicketFormsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketFormsSearchFilter


class TicketFormsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TicketFormsStringFilter


class TicketFormsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TicketFormsStringFilter


class TicketFormsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketFormsStringFilter


class TicketFormsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketFormsStringFilter


class TicketFormsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: TicketFormsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketFormsInCondition = TypedDict("TicketFormsInCondition", {"in": TicketFormsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketFormsNotCondition = TypedDict("TicketFormsNotCondition", {"not": "TicketFormsCondition"}, total=False)
"""Negates the nested condition."""

TicketFormsAndCondition = TypedDict("TicketFormsAndCondition", {"and": "list[TicketFormsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketFormsOrCondition = TypedDict("TicketFormsOrCondition", {"or": "list[TicketFormsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketFormsAnyCondition = TypedDict("TicketFormsAnyCondition", {"any": TicketFormsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_forms condition types
TicketFormsCondition = (
    TicketFormsEqCondition
    | TicketFormsNeqCondition
    | TicketFormsGtCondition
    | TicketFormsGteCondition
    | TicketFormsLtCondition
    | TicketFormsLteCondition
    | TicketFormsInCondition
    | TicketFormsStartswithCondition
    | TicketFormsEndswithCondition
    | TicketFormsFuzzyCondition
    | TicketFormsKeywordCondition
    | TicketFormsContainsCondition
    | TicketFormsNotCondition
    | TicketFormsAndCondition
    | TicketFormsOrCondition
    | TicketFormsAnyCondition
)


class TicketFormsSearchQuery(TypedDict, total=False):
    """Search query for ticket_forms entity."""
    filter: TicketFormsCondition
    sort: list[TicketFormsSortFilter]


# ===== USER_ROLES SEARCH TYPES =====

class UserRolesSearchFilter(TypedDict, total=False):
    """Available fields for filtering user_roles search queries."""
    id: str
    """Unique identifier for the user role"""
    name: str | None
    """Display name of the user role"""
    slug: str | None
    """URL-safe identifier for the user role"""


class UserRolesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the user role"""
    name: list[str]
    """Display name of the user role"""
    slug: list[str]
    """URL-safe identifier for the user role"""


class UserRolesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the user role"""
    name: Any
    """Display name of the user role"""
    slug: Any
    """URL-safe identifier for the user role"""


class UserRolesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the user role"""
    name: str
    """Display name of the user role"""
    slug: str
    """URL-safe identifier for the user role"""


class UserRolesSortFilter(TypedDict, total=False):
    """Available fields for sorting user_roles search results."""
    id: AirbyteSortOrder
    """Unique identifier for the user role"""
    name: AirbyteSortOrder
    """Display name of the user role"""
    slug: AirbyteSortOrder
    """URL-safe identifier for the user role"""


# Entity-specific condition types for user_roles
class UserRolesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UserRolesSearchFilter


class UserRolesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UserRolesSearchFilter


class UserRolesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UserRolesSearchFilter


class UserRolesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UserRolesSearchFilter


class UserRolesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UserRolesSearchFilter


class UserRolesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UserRolesSearchFilter


class UserRolesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UserRolesStringFilter


class UserRolesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UserRolesStringFilter


class UserRolesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UserRolesStringFilter


class UserRolesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UserRolesStringFilter


class UserRolesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: UserRolesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UserRolesInCondition = TypedDict("UserRolesInCondition", {"in": UserRolesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UserRolesNotCondition = TypedDict("UserRolesNotCondition", {"not": "UserRolesCondition"}, total=False)
"""Negates the nested condition."""

UserRolesAndCondition = TypedDict("UserRolesAndCondition", {"and": "list[UserRolesCondition]"}, total=False)
"""True if all nested conditions are true."""

UserRolesOrCondition = TypedDict("UserRolesOrCondition", {"or": "list[UserRolesCondition]"}, total=False)
"""True if any nested condition is true."""

UserRolesAnyCondition = TypedDict("UserRolesAnyCondition", {"any": UserRolesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all user_roles condition types
UserRolesCondition = (
    UserRolesEqCondition
    | UserRolesNeqCondition
    | UserRolesGtCondition
    | UserRolesGteCondition
    | UserRolesLtCondition
    | UserRolesLteCondition
    | UserRolesInCondition
    | UserRolesStartswithCondition
    | UserRolesEndswithCondition
    | UserRolesFuzzyCondition
    | UserRolesKeywordCondition
    | UserRolesContainsCondition
    | UserRolesNotCondition
    | UserRolesAndCondition
    | UserRolesOrCondition
    | UserRolesAnyCondition
)


class UserRolesSearchQuery(TypedDict, total=False):
    """Search query for user_roles entity."""
    filter: UserRolesCondition
    sort: list[UserRolesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
