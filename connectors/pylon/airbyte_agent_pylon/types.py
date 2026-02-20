"""
Type definitions for pylon connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



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

