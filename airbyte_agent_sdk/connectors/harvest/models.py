"""
Pydantic models for harvest connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration - multiple options available

class HarvestOauth20AuthConfig(BaseModel):
    """OAuth 2.0"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Client ID"""
    client_secret: str
    """Client Secret"""
    refresh_token: str
    """Your Harvest OAuth2 refresh token"""
    account_id: str
    """Your Harvest account ID"""

class HarvestPersonalAccessTokenAuthConfig(BaseModel):
    """Personal Access Token"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """Your Harvest personal access token"""
    account_id: str
    """Your Harvest account ID"""

HarvestAuthConfig = HarvestOauth20AuthConfig | HarvestPersonalAccessTokenAuthConfig

# Replication configuration

class HarvestReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Harvest."""

    model_config = ConfigDict(extra="forbid")

    account_id: str
    """Your Harvest account ID. Required for all API requests."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PaginationLinks(BaseModel):
    """Pagination links for navigating result pages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first: str | None = Field(default=None)
    previous: str | None = Field(default=None)
    next: str | None = Field(default=None)
    last: str | None = Field(default=None)

class User(BaseModel):
    """A Harvest user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    telephone: str | None = Field(default=None)
    timezone: str | None = Field(default=None)
    has_access_to_all_future_projects: bool | None = Field(default=None)
    is_contractor: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    weekly_capacity: int | None = Field(default=None)
    default_hourly_rate: float | None = Field(default=None)
    cost_rate: float | None = Field(default=None)
    roles: list[str] | None = Field(default=None)
    access_roles: list[str] | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    employee_id: str | None = Field(default=None)
    calendar_integration_enabled: bool | None = Field(default=None)
    calendar_integration_source: str | None = Field(default=None)
    can_create_projects: bool | None = Field(default=None)
    permissions_claims: list[str] | None = Field(default=None)

class UsersList(BaseModel):
    """Paginated list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    users: list[User] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Client(BaseModel):
    """A Harvest client"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    address: str | None = Field(default=None)
    statement_key: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class ClientsList(BaseModel):
    """Paginated list of clients"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    clients: list[Client] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class ContactClient(BaseModel):
    """The client associated with this contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Client ID")
    """Client ID"""
    name: str | None | None = Field(default=None, description="Client name")
    """Client name"""

class Contact(BaseModel):
    """A Harvest contact associated with a client"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    title: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone_office: str | None = Field(default=None)
    phone_mobile: str | None = Field(default=None)
    fax: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    client: ContactClient | None = Field(default=None)

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    contacts: list[Contact] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Company(BaseModel):
    """The Harvest company/account information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base_uri: str | None = Field(default=None)
    full_domain: str | None = Field(default=None)
    name: str | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    week_start_day: str | None = Field(default=None)
    wants_timestamp_timers: bool | None = Field(default=None)
    time_format: str | None = Field(default=None)
    date_format: str | None = Field(default=None)
    plan_type: str | None = Field(default=None)
    clock: str | None = Field(default=None)
    currency_code_display: str | None = Field(default=None)
    currency_symbol_display: str | None = Field(default=None)
    decimal_symbol: str | None = Field(default=None)
    thousands_separator: str | None = Field(default=None)
    color_scheme: str | None = Field(default=None)
    weekly_capacity: int | None = Field(default=None)
    expense_feature: bool | None = Field(default=None)
    invoice_feature: bool | None = Field(default=None)
    estimate_feature: bool | None = Field(default=None)
    approval_feature: bool | None = Field(default=None)
    team_feature: bool | None = Field(default=None)
    currency: str | None = Field(default=None)
    saml_sign_in_required: bool | None = Field(default=None)
    day_entry_notes_required: bool | None = Field(default=None)

class ProjectClient(BaseModel):
    """The client associated with the project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Client ID")
    """Client ID"""
    name: str | None | None = Field(default=None, description="Client name")
    """Client name"""
    currency: str | None | None = Field(default=None, description="Client currency")
    """Client currency"""

class Project(BaseModel):
    """A Harvest project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    code: str | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    is_billable: bool | None = Field(default=None)
    is_fixed_fee: bool | None = Field(default=None)
    bill_by: str | None = Field(default=None)
    hourly_rate: float | None = Field(default=None)
    budget_by: str | None = Field(default=None)
    budget_is_monthly: bool | None = Field(default=None)
    budget: float | None = Field(default=None)
    cost_budget: float | None = Field(default=None)
    cost_budget_include_expenses: bool | None = Field(default=None)
    notify_when_over_budget: bool | None = Field(default=None)
    over_budget_notification_percentage: float | None = Field(default=None)
    over_budget_notification_date: str | None = Field(default=None)
    show_budget_to_all: bool | None = Field(default=None)
    fee: float | None = Field(default=None)
    notes: str | None = Field(default=None)
    starts_on: str | None = Field(default=None)
    ends_on: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    client: ProjectClient | None = Field(default=None)

class ProjectsList(BaseModel):
    """Paginated list of projects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    projects: list[Project] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Task(BaseModel):
    """A Harvest task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    billable_by_default: bool | None = Field(default=None)
    default_hourly_rate: float | None = Field(default=None)
    is_default: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class TasksList(BaseModel):
    """Paginated list of tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tasks: list[Task] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class TimeEntryClient(BaseModel):
    """The client associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Client ID")
    """Client ID"""
    name: str | None | None = Field(default=None, description="Client name")
    """Client name"""

class TimeEntryInvoice(BaseModel):
    """The invoice associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Invoice ID")
    """Invoice ID"""
    number: str | None | None = Field(default=None, description="Invoice number")
    """Invoice number"""

class TimeEntryTask(BaseModel):
    """The task associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Task ID")
    """Task ID"""
    name: str | None | None = Field(default=None, description="Task name")
    """Task name"""

class TimeEntryProject(BaseModel):
    """The project associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Project ID")
    """Project ID"""
    name: str | None | None = Field(default=None, description="Project name")
    """Project name"""

class TimeEntryUser(BaseModel):
    """The user associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="User ID")
    """User ID"""
    name: str | None | None = Field(default=None, description="User name")
    """User name"""

class TimeEntry(BaseModel):
    """A Harvest time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    spent_date: str | None = Field(default=None)
    hours: float | None = Field(default=None)
    hours_without_timer: float | None = Field(default=None)
    rounded_hours: float | None = Field(default=None)
    notes: str | None = Field(default=None)
    is_locked: bool | None = Field(default=None)
    locked_reason: str | None = Field(default=None)
    is_closed: bool | None = Field(default=None)
    is_billed: bool | None = Field(default=None)
    timer_started_at: str | None = Field(default=None)
    started_time: str | None = Field(default=None)
    ended_time: str | None = Field(default=None)
    is_running: bool | None = Field(default=None)
    billable: bool | None = Field(default=None)
    budgeted: bool | None = Field(default=None)
    billable_rate: float | None = Field(default=None)
    cost_rate: float | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    approval_status: str | None = Field(default=None)
    is_explicitly_locked: bool | None = Field(default=None)
    user: TimeEntryUser | None = Field(default=None)
    client: TimeEntryClient | None = Field(default=None)
    project: TimeEntryProject | None = Field(default=None)
    task: TimeEntryTask | None = Field(default=None)
    user_assignment: dict[str, Any] | None = Field(default=None)
    task_assignment: dict[str, Any] | None = Field(default=None)
    external_reference: dict[str, Any] | None = Field(default=None)
    invoice: TimeEntryInvoice | None = Field(default=None)

class TimeEntriesList(BaseModel):
    """Paginated list of time entries"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    time_entries: list[TimeEntry] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Invoice(BaseModel):
    """A Harvest invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    client_key: str | None = Field(default=None)
    number: str | None = Field(default=None)
    purchase_order: str | None = Field(default=None)
    amount: float | None = Field(default=None)
    due_amount: float | None = Field(default=None)
    tax: float | None = Field(default=None)
    tax_amount: float | None = Field(default=None)
    tax2: float | None = Field(default=None)
    tax2_amount: float | None = Field(default=None)
    discount: float | None = Field(default=None)
    discount_amount: float | None = Field(default=None)
    subject: str | None = Field(default=None)
    notes: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    state: str | None = Field(default=None)
    period_start: str | None = Field(default=None)
    period_end: str | None = Field(default=None)
    issue_date: str | None = Field(default=None)
    due_date: str | None = Field(default=None)
    payment_term: str | None = Field(default=None)
    payment_options: list[str] | None = Field(default=None)
    sent_at: str | None = Field(default=None)
    paid_at: str | None = Field(default=None)
    paid_date: str | None = Field(default=None)
    closed_at: str | None = Field(default=None)
    recurring_invoice_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    client: dict[str, Any] | None = Field(default=None)
    estimate: dict[str, Any] | None = Field(default=None)
    retainer: dict[str, Any] | None = Field(default=None)
    creator: dict[str, Any] | None = Field(default=None)
    line_items: list[dict[str, Any]] | None = Field(default=None)

class InvoicesList(BaseModel):
    """Paginated list of invoices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invoices: list[Invoice] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class InvoiceItemCategory(BaseModel):
    """A Harvest invoice item category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    use_as_service: bool | None = Field(default=None)
    use_as_expense: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class InvoiceItemCategoriesList(BaseModel):
    """Paginated list of invoice item categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invoice_item_categories: list[InvoiceItemCategory] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Estimate(BaseModel):
    """A Harvest estimate"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    client_key: str | None = Field(default=None)
    number: str | None = Field(default=None)
    purchase_order: str | None = Field(default=None)
    amount: float | None = Field(default=None)
    tax: float | None = Field(default=None)
    tax_amount: float | None = Field(default=None)
    tax2: float | None = Field(default=None)
    tax2_amount: float | None = Field(default=None)
    discount: float | None = Field(default=None)
    discount_amount: float | None = Field(default=None)
    subject: str | None = Field(default=None)
    notes: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    state: str | None = Field(default=None)
    issue_date: str | None = Field(default=None)
    sent_at: str | None = Field(default=None)
    accepted_at: str | None = Field(default=None)
    declined_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    client: dict[str, Any] | None = Field(default=None)
    creator: dict[str, Any] | None = Field(default=None)
    line_items: list[dict[str, Any]] | None = Field(default=None)

class EstimatesList(BaseModel):
    """Paginated list of estimates"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    estimates: list[Estimate] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class EstimateItemCategory(BaseModel):
    """A Harvest estimate item category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class EstimateItemCategoriesList(BaseModel):
    """Paginated list of estimate item categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    estimate_item_categories: list[EstimateItemCategory] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Expense(BaseModel):
    """A Harvest expense"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    notes: str | None = Field(default=None)
    total_cost: float | None = Field(default=None)
    units: float | None = Field(default=None)
    is_closed: bool | None = Field(default=None)
    is_locked: bool | None = Field(default=None)
    is_billed: bool | None = Field(default=None)
    locked_reason: str | None = Field(default=None)
    spent_date: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    billable: bool | None = Field(default=None)
    approval_status: str | None = Field(default=None)
    is_explicitly_locked: bool | None = Field(default=None)
    receipt: dict[str, Any] | None = Field(default=None)
    user: dict[str, Any] | None = Field(default=None)
    user_assignment: dict[str, Any] | None = Field(default=None)
    project: dict[str, Any] | None = Field(default=None)
    expense_category: dict[str, Any] | None = Field(default=None)
    client: dict[str, Any] | None = Field(default=None)
    invoice: dict[str, Any] | None = Field(default=None)

class ExpensesList(BaseModel):
    """Paginated list of expenses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expenses: list[Expense] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class ExpenseCategory(BaseModel):
    """A Harvest expense category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    unit_name: str | None = Field(default=None)
    unit_price: float | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class ExpenseCategoriesList(BaseModel):
    """Paginated list of expense categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expense_categories: list[ExpenseCategory] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class Role(BaseModel):
    """A Harvest role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    user_ids: list[int] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class RolesList(BaseModel):
    """Paginated list of roles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    roles: list[Role] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class UserAssignmentProject(BaseModel):
    """The project associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Project ID")
    """Project ID"""
    name: str | None | None = Field(default=None, description="Project name")
    """Project name"""
    code: str | None | None = Field(default=None, description="Project code")
    """Project code"""

class UserAssignmentUser(BaseModel):
    """The user associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="User ID")
    """User ID"""
    name: str | None | None = Field(default=None, description="User name")
    """User name"""

class UserAssignment(BaseModel):
    """A Harvest user assignment linking a user to a project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    is_project_manager: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    budget: float | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    hourly_rate: float | None = Field(default=None)
    use_default_rates: bool | None = Field(default=None)
    project: UserAssignmentProject | None = Field(default=None)
    user: UserAssignmentUser | None = Field(default=None)

class UserAssignmentsList(BaseModel):
    """Paginated list of user assignments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_assignments: list[UserAssignment] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class TaskAssignmentTask(BaseModel):
    """The task associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Task ID")
    """Task ID"""
    name: str | None | None = Field(default=None, description="Task name")
    """Task name"""

class TaskAssignmentProject(BaseModel):
    """The project associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Project ID")
    """Project ID"""
    name: str | None | None = Field(default=None, description="Project name")
    """Project name"""
    code: str | None | None = Field(default=None, description="Project code")
    """Project code"""

class TaskAssignment(BaseModel):
    """A Harvest task assignment linking a task to a project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    billable: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    hourly_rate: float | None = Field(default=None)
    budget: float | None = Field(default=None)
    project: TaskAssignmentProject | None = Field(default=None)
    task: TaskAssignmentTask | None = Field(default=None)

class TaskAssignmentsList(BaseModel):
    """Paginated list of task assignments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    task_assignments: list[TaskAssignment] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class TimeProject(BaseModel):
    """A time report entry grouped by project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project_id: int | None = Field(default=None)
    project_name: str | None = Field(default=None)
    client_id: int | None = Field(default=None)
    client_name: str | None = Field(default=None)
    total_hours: float | None = Field(default=None)
    billable_hours: float | None = Field(default=None)
    currency: str | None = Field(default=None)
    billable_amount: float | None = Field(default=None)

class TimeProjectsList(BaseModel):
    """Paginated list of time report entries by project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[TimeProject] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

class TimeTask(BaseModel):
    """A time report entry grouped by task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    task_id: int | None = Field(default=None)
    task_name: str | None = Field(default=None)
    total_hours: float | None = Field(default=None)
    billable_hours: float | None = Field(default=None)
    currency: str | None = Field(default=None)
    billable_amount: float | None = Field(default=None)

class TimeTasksList(BaseModel):
    """Paginated list of time report entries by task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[TimeTask] | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_entries: int | None = Field(default=None)
    page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    links: PaginationLinks | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class ClientsListResultMeta(BaseModel):
    """Metadata for clients.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TimeEntriesListResultMeta(BaseModel):
    """Metadata for time_entries.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class InvoicesListResultMeta(BaseModel):
    """Metadata for invoices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class InvoiceItemCategoriesListResultMeta(BaseModel):
    """Metadata for invoice_item_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class EstimatesListResultMeta(BaseModel):
    """Metadata for estimates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class EstimateItemCategoriesListResultMeta(BaseModel):
    """Metadata for estimate_item_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class ExpensesListResultMeta(BaseModel):
    """Metadata for expenses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class ExpenseCategoriesListResultMeta(BaseModel):
    """Metadata for expense_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class RolesListResultMeta(BaseModel):
    """Metadata for roles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class UserAssignmentsListResultMeta(BaseModel):
    """Metadata for user_assignments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TaskAssignmentsListResultMeta(BaseModel):
    """Metadata for task_assignments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TimeProjectsListResultMeta(BaseModel):
    """Metadata for time_projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

class TimeTasksListResultMeta(BaseModel):
    """Metadata for time_tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class HarvestCheckResult(BaseModel):
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


class HarvestExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class HarvestExecuteResultWithMeta(HarvestExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ClientsSearchData(BaseModel):
    """Search result data for clients entity."""
    model_config = ConfigDict(extra="allow")

    address: str | None = None
    """The client's postal address"""
    created_at: str | None = None
    """When the client record was created"""
    currency: str | None = None
    """The currency used by the client"""
    id: int | None = None
    """Unique identifier for the client"""
    is_active: bool | None = None
    """Whether the client is active"""
    name: str | None = None
    """The client's name"""
    updated_at: str | None = None
    """When the client record was last updated"""


class CompanySearchData(BaseModel):
    """Search result data for company entity."""
    model_config = ConfigDict(extra="allow")

    base_uri: str | None = None
    """The base URI"""
    currency: str | None = None
    """Currency used by the company"""
    full_domain: str | None = None
    """The full domain name"""
    is_active: bool | None = None
    """Whether the company is active"""
    name: str | None = None
    """The name of the company"""
    plan_type: str | None = None
    """The plan type"""
    weekly_capacity: int | None = None
    """Weekly capacity in seconds"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    client: dict[str, Any] | None = None
    """Client associated with the contact"""
    created_at: str | None = None
    """When created"""
    email: str | None = None
    """Email address"""
    first_name: str | None = None
    """First name"""
    id: int | None = None
    """Unique identifier"""
    last_name: str | None = None
    """Last name"""
    title: str | None = None
    """Job title"""
    updated_at: str | None = None
    """When last updated"""


class EstimateItemCategoriesSearchData(BaseModel):
    """Search result data for estimate_item_categories entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When created"""
    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Category name"""
    updated_at: str | None = None
    """When last updated"""


class EstimatesSearchData(BaseModel):
    """Search result data for estimates entity."""
    model_config = ConfigDict(extra="allow")

    amount: float | None = None
    """Total amount"""
    client: dict[str, Any] | None = None
    """Client details"""
    created_at: str | None = None
    """When created"""
    currency: str | None = None
    """Currency"""
    id: int | None = None
    """Unique identifier"""
    issue_date: str | None = None
    """Issue date"""
    number: str | None = None
    """Estimate number"""
    state: str | None = None
    """Current state"""
    subject: str | None = None
    """Subject"""
    updated_at: str | None = None
    """When last updated"""


class ExpenseCategoriesSearchData(BaseModel):
    """Search result data for expense_categories entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When created"""
    id: int | None = None
    """Unique identifier"""
    is_active: bool | None = None
    """Whether active"""
    name: str | None = None
    """Category name"""
    unit_name: str | None = None
    """Unit name"""
    unit_price: float | None = None
    """Unit price"""
    updated_at: str | None = None
    """When last updated"""


class ExpensesSearchData(BaseModel):
    """Search result data for expenses entity."""
    model_config = ConfigDict(extra="allow")

    billable: bool | None = None
    """Whether billable"""
    client: dict[str, Any] | None = None
    """Associated client"""
    created_at: str | None = None
    """When created"""
    expense_category: dict[str, Any] | None = None
    """Expense category"""
    id: int | None = None
    """Unique identifier"""
    is_billed: bool | None = None
    """Whether billed"""
    notes: str | None = None
    """Notes"""
    project: dict[str, Any] | None = None
    """Associated project"""
    spent_date: str | None = None
    """Date spent"""
    total_cost: float | None = None
    """Total cost"""
    updated_at: str | None = None
    """When last updated"""
    user: dict[str, Any] | None = None
    """Associated user"""


class InvoiceItemCategoriesSearchData(BaseModel):
    """Search result data for invoice_item_categories entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When created"""
    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Category name"""
    updated_at: str | None = None
    """When last updated"""
    use_as_expense: bool | None = None
    """Whether used as expense type"""
    use_as_service: bool | None = None
    """Whether used as service type"""


class InvoicesSearchData(BaseModel):
    """Search result data for invoices entity."""
    model_config = ConfigDict(extra="allow")

    amount: float | None = None
    """Total amount"""
    client: dict[str, Any] | None = None
    """Client details"""
    created_at: str | None = None
    """When created"""
    currency: str | None = None
    """Currency"""
    due_amount: float | None = None
    """Amount due"""
    due_date: str | None = None
    """Due date"""
    id: int | None = None
    """Unique identifier"""
    issue_date: str | None = None
    """Issue date"""
    number: str | None = None
    """Invoice number"""
    state: str | None = None
    """Current state"""
    subject: str | None = None
    """Subject"""
    updated_at: str | None = None
    """When last updated"""


class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    budget: float | None = None
    """Budget amount"""
    client: dict[str, Any] | None = None
    """Client details"""
    code: str | None = None
    """Project code"""
    created_at: str | None = None
    """When created"""
    hourly_rate: float | None = None
    """Hourly rate"""
    id: int | None = None
    """Unique identifier"""
    is_active: bool | None = None
    """Whether active"""
    is_billable: bool | None = None
    """Whether billable"""
    name: str | None = None
    """Project name"""
    starts_on: str | None = None
    """Start date"""
    updated_at: str | None = None
    """When last updated"""


class RolesSearchData(BaseModel):
    """Search result data for roles entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When created"""
    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Role name"""
    updated_at: str | None = None
    """When last updated"""
    user_ids: list[Any] | None = None
    """User IDs with this role"""


class TaskAssignmentsSearchData(BaseModel):
    """Search result data for task_assignments entity."""
    model_config = ConfigDict(extra="allow")

    billable: bool | None = None
    """Whether billable"""
    created_at: str | None = None
    """When created"""
    hourly_rate: float | None = None
    """Hourly rate"""
    id: int | None = None
    """Unique identifier"""
    is_active: bool | None = None
    """Whether active"""
    project: dict[str, Any] | None = None
    """Associated project"""
    task: dict[str, Any] | None = None
    """Associated task"""
    updated_at: str | None = None
    """When last updated"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    billable_by_default: bool | None = None
    """Whether billable by default"""
    created_at: str | None = None
    """When created"""
    default_hourly_rate: float | None = None
    """Default hourly rate"""
    id: int | None = None
    """Unique identifier"""
    is_active: bool | None = None
    """Whether active"""
    name: str | None = None
    """Task name"""
    updated_at: str | None = None
    """When last updated"""


class TimeEntriesSearchData(BaseModel):
    """Search result data for time_entries entity."""
    model_config = ConfigDict(extra="allow")

    billable: bool | None = None
    """Whether billable"""
    client: dict[str, Any] | None = None
    """Associated client"""
    created_at: str | None = None
    """When created"""
    hours: float | None = None
    """Hours logged"""
    id: int | None = None
    """Unique identifier"""
    is_billed: bool | None = None
    """Whether billed"""
    notes: str | None = None
    """Notes"""
    project: dict[str, Any] | None = None
    """Associated project"""
    spent_date: str | None = None
    """Date time was spent"""
    task: dict[str, Any] | None = None
    """Associated task"""
    updated_at: str | None = None
    """When last updated"""
    user: dict[str, Any] | None = None
    """Associated user"""


class TimeProjectsSearchData(BaseModel):
    """Search result data for time_projects entity."""
    model_config = ConfigDict(extra="allow")

    billable_amount: float | None = None
    """Total billable amount"""
    billable_hours: float | None = None
    """Number of billable hours"""
    client_id: int | None = None
    """Client identifier"""
    client_name: str | None = None
    """Client name"""
    currency: str | None = None
    """Currency code"""
    project_id: int | None = None
    """Project identifier"""
    project_name: str | None = None
    """Project name"""
    total_hours: float | None = None
    """Total hours spent"""


class TimeTasksSearchData(BaseModel):
    """Search result data for time_tasks entity."""
    model_config = ConfigDict(extra="allow")

    billable_amount: float | None = None
    """Total billable amount"""
    billable_hours: float | None = None
    """Number of billable hours"""
    currency: str | None = None
    """Currency code"""
    task_id: int | None = None
    """Task identifier"""
    task_name: str | None = None
    """Task name"""
    total_hours: float | None = None
    """Total hours spent"""


class UserAssignmentsSearchData(BaseModel):
    """Search result data for user_assignments entity."""
    model_config = ConfigDict(extra="allow")

    budget: float | None = None
    """Budget"""
    created_at: str | None = None
    """When created"""
    hourly_rate: float | None = None
    """Hourly rate"""
    id: int | None = None
    """Unique identifier"""
    is_active: bool | None = None
    """Whether active"""
    is_project_manager: bool | None = None
    """Whether project manager"""
    project: dict[str, Any] | None = None
    """Associated project"""
    updated_at: str | None = None
    """When last updated"""
    user: dict[str, Any] | None = None
    """Associated user"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    avatar_url: str | None = None
    """Avatar URL"""
    cost_rate: float | None = None
    """Cost rate"""
    created_at: str | None = None
    """When created"""
    default_hourly_rate: float | None = None
    """Default hourly rate"""
    email: str | None = None
    """Email address"""
    first_name: str | None = None
    """First name"""
    id: int | None = None
    """Unique identifier"""
    is_active: bool | None = None
    """Whether active"""
    is_contractor: bool | None = None
    """Whether contractor"""
    last_name: str | None = None
    """Last name"""
    roles: list[Any] | None = None
    """Assigned roles"""
    telephone: str | None = None
    """Phone number"""
    timezone: str | None = None
    """Timezone"""
    updated_at: str | None = None
    """When last updated"""
    weekly_capacity: int | None = None
    """Weekly capacity in seconds"""


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

ClientsSearchResult = AirbyteSearchResult[ClientsSearchData]
"""Search result type for clients entity."""

CompanySearchResult = AirbyteSearchResult[CompanySearchData]
"""Search result type for company entity."""

ContactsSearchResult = AirbyteSearchResult[ContactsSearchData]
"""Search result type for contacts entity."""

EstimateItemCategoriesSearchResult = AirbyteSearchResult[EstimateItemCategoriesSearchData]
"""Search result type for estimate_item_categories entity."""

EstimatesSearchResult = AirbyteSearchResult[EstimatesSearchData]
"""Search result type for estimates entity."""

ExpenseCategoriesSearchResult = AirbyteSearchResult[ExpenseCategoriesSearchData]
"""Search result type for expense_categories entity."""

ExpensesSearchResult = AirbyteSearchResult[ExpensesSearchData]
"""Search result type for expenses entity."""

InvoiceItemCategoriesSearchResult = AirbyteSearchResult[InvoiceItemCategoriesSearchData]
"""Search result type for invoice_item_categories entity."""

InvoicesSearchResult = AirbyteSearchResult[InvoicesSearchData]
"""Search result type for invoices entity."""

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

RolesSearchResult = AirbyteSearchResult[RolesSearchData]
"""Search result type for roles entity."""

TaskAssignmentsSearchResult = AirbyteSearchResult[TaskAssignmentsSearchData]
"""Search result type for task_assignments entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""

TimeEntriesSearchResult = AirbyteSearchResult[TimeEntriesSearchData]
"""Search result type for time_entries entity."""

TimeProjectsSearchResult = AirbyteSearchResult[TimeProjectsSearchData]
"""Search result type for time_projects entity."""

TimeTasksSearchResult = AirbyteSearchResult[TimeTasksSearchData]
"""Search result type for time_tasks entity."""

UserAssignmentsSearchResult = AirbyteSearchResult[UserAssignmentsSearchData]
"""Search result type for user_assignments entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = HarvestExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

ClientsListResult = HarvestExecuteResultWithMeta[list[Client], ClientsListResultMeta]
"""Result type for clients.list operation with data and metadata."""

ContactsListResult = HarvestExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

ProjectsListResult = HarvestExecuteResultWithMeta[list[Project], ProjectsListResultMeta]
"""Result type for projects.list operation with data and metadata."""

TasksListResult = HarvestExecuteResultWithMeta[list[Task], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

TimeEntriesListResult = HarvestExecuteResultWithMeta[list[TimeEntry], TimeEntriesListResultMeta]
"""Result type for time_entries.list operation with data and metadata."""

InvoicesListResult = HarvestExecuteResultWithMeta[list[Invoice], InvoicesListResultMeta]
"""Result type for invoices.list operation with data and metadata."""

InvoiceItemCategoriesListResult = HarvestExecuteResultWithMeta[list[InvoiceItemCategory], InvoiceItemCategoriesListResultMeta]
"""Result type for invoice_item_categories.list operation with data and metadata."""

EstimatesListResult = HarvestExecuteResultWithMeta[list[Estimate], EstimatesListResultMeta]
"""Result type for estimates.list operation with data and metadata."""

EstimateItemCategoriesListResult = HarvestExecuteResultWithMeta[list[EstimateItemCategory], EstimateItemCategoriesListResultMeta]
"""Result type for estimate_item_categories.list operation with data and metadata."""

ExpensesListResult = HarvestExecuteResultWithMeta[list[Expense], ExpensesListResultMeta]
"""Result type for expenses.list operation with data and metadata."""

ExpenseCategoriesListResult = HarvestExecuteResultWithMeta[list[ExpenseCategory], ExpenseCategoriesListResultMeta]
"""Result type for expense_categories.list operation with data and metadata."""

RolesListResult = HarvestExecuteResultWithMeta[list[Role], RolesListResultMeta]
"""Result type for roles.list operation with data and metadata."""

UserAssignmentsListResult = HarvestExecuteResultWithMeta[list[UserAssignment], UserAssignmentsListResultMeta]
"""Result type for user_assignments.list operation with data and metadata."""

TaskAssignmentsListResult = HarvestExecuteResultWithMeta[list[TaskAssignment], TaskAssignmentsListResultMeta]
"""Result type for task_assignments.list operation with data and metadata."""

TimeProjectsListResult = HarvestExecuteResultWithMeta[list[TimeProject], TimeProjectsListResultMeta]
"""Result type for time_projects.list operation with data and metadata."""

TimeTasksListResult = HarvestExecuteResultWithMeta[list[TimeTask], TimeTasksListResultMeta]
"""Result type for time_tasks.list operation with data and metadata."""

