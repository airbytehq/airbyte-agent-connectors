"""
Pydantic models for harvest connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

    replication_start_date: str
    """UTC date and time in YYYY-MM-DDTHH:mm:ssZ format from which to start replicating data. Data before this date will not be replicated."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PaginationLinks(BaseModel):
    """Pagination links for navigating result pages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first: Union[str | None, Any] = Field(default=None)
    previous: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    last: Union[str | None, Any] = Field(default=None)

class User(BaseModel):
    """A Harvest user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    telephone: Union[str | None, Any] = Field(default=None)
    timezone: Union[str | None, Any] = Field(default=None)
    has_access_to_all_future_projects: Union[bool | None, Any] = Field(default=None)
    is_contractor: Union[bool | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    weekly_capacity: Union[int | None, Any] = Field(default=None)
    default_hourly_rate: Union[float | None, Any] = Field(default=None)
    cost_rate: Union[float | None, Any] = Field(default=None)
    roles: Union[list[str] | None, Any] = Field(default=None)
    access_roles: Union[list[str] | None, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    employee_id: Union[str | None, Any] = Field(default=None)
    calendar_integration_enabled: Union[bool | None, Any] = Field(default=None)
    calendar_integration_source: Union[str | None, Any] = Field(default=None)
    can_create_projects: Union[bool | None, Any] = Field(default=None)
    permissions_claims: Union[list[str] | None, Any] = Field(default=None)

class UsersList(BaseModel):
    """Paginated list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    users: Union[list[User], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Client(BaseModel):
    """A Harvest client"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    address: Union[str | None, Any] = Field(default=None)
    statement_key: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class ClientsList(BaseModel):
    """Paginated list of clients"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    clients: Union[list[Client], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class ContactClient(BaseModel):
    """The client associated with this contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Client ID")
    """Client ID"""
    name: Union[str | None, Any] = Field(default=None, description="Client name")
    """Client name"""

class Contact(BaseModel):
    """A Harvest contact associated with a client"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone_office: Union[str | None, Any] = Field(default=None)
    phone_mobile: Union[str | None, Any] = Field(default=None)
    fax: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    client: Union[ContactClient | None, Any] = Field(default=None)

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    contacts: Union[list[Contact], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Company(BaseModel):
    """The Harvest company/account information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    base_uri: Union[str | None, Any] = Field(default=None)
    full_domain: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    week_start_day: Union[str | None, Any] = Field(default=None)
    wants_timestamp_timers: Union[bool | None, Any] = Field(default=None)
    time_format: Union[str | None, Any] = Field(default=None)
    date_format: Union[str | None, Any] = Field(default=None)
    plan_type: Union[str | None, Any] = Field(default=None)
    clock: Union[str | None, Any] = Field(default=None)
    currency_code_display: Union[str | None, Any] = Field(default=None)
    currency_symbol_display: Union[str | None, Any] = Field(default=None)
    decimal_symbol: Union[str | None, Any] = Field(default=None)
    thousands_separator: Union[str | None, Any] = Field(default=None)
    color_scheme: Union[str | None, Any] = Field(default=None)
    weekly_capacity: Union[int | None, Any] = Field(default=None)
    expense_feature: Union[bool | None, Any] = Field(default=None)
    invoice_feature: Union[bool | None, Any] = Field(default=None)
    estimate_feature: Union[bool | None, Any] = Field(default=None)
    approval_feature: Union[bool | None, Any] = Field(default=None)
    team_feature: Union[bool | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    saml_sign_in_required: Union[bool | None, Any] = Field(default=None)
    day_entry_notes_required: Union[bool | None, Any] = Field(default=None)

class ProjectClient(BaseModel):
    """The client associated with the project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Client ID")
    """Client ID"""
    name: Union[str | None, Any] = Field(default=None, description="Client name")
    """Client name"""
    currency: Union[str | None, Any] = Field(default=None, description="Client currency")
    """Client currency"""

class Project(BaseModel):
    """A Harvest project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    code: Union[str | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    is_billable: Union[bool | None, Any] = Field(default=None)
    is_fixed_fee: Union[bool | None, Any] = Field(default=None)
    bill_by: Union[str | None, Any] = Field(default=None)
    hourly_rate: Union[float | None, Any] = Field(default=None)
    budget_by: Union[str | None, Any] = Field(default=None)
    budget_is_monthly: Union[bool | None, Any] = Field(default=None)
    budget: Union[float | None, Any] = Field(default=None)
    cost_budget: Union[float | None, Any] = Field(default=None)
    cost_budget_include_expenses: Union[bool | None, Any] = Field(default=None)
    notify_when_over_budget: Union[bool | None, Any] = Field(default=None)
    over_budget_notification_percentage: Union[float | None, Any] = Field(default=None)
    over_budget_notification_date: Union[str | None, Any] = Field(default=None)
    show_budget_to_all: Union[bool | None, Any] = Field(default=None)
    fee: Union[float | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    starts_on: Union[str | None, Any] = Field(default=None)
    ends_on: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    client: Union[ProjectClient | None, Any] = Field(default=None)

class ProjectsList(BaseModel):
    """Paginated list of projects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    projects: Union[list[Project], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Task(BaseModel):
    """A Harvest task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    billable_by_default: Union[bool | None, Any] = Field(default=None)
    default_hourly_rate: Union[float | None, Any] = Field(default=None)
    is_default: Union[bool | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class TasksList(BaseModel):
    """Paginated list of tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tasks: Union[list[Task], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class TimeEntryInvoice(BaseModel):
    """The invoice associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Invoice ID")
    """Invoice ID"""
    number: Union[str | None, Any] = Field(default=None, description="Invoice number")
    """Invoice number"""

class TimeEntryUser(BaseModel):
    """The user associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="User ID")
    """User ID"""
    name: Union[str | None, Any] = Field(default=None, description="User name")
    """User name"""

class TimeEntryTask(BaseModel):
    """The task associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Task ID")
    """Task ID"""
    name: Union[str | None, Any] = Field(default=None, description="Task name")
    """Task name"""

class TimeEntryClient(BaseModel):
    """The client associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Client ID")
    """Client ID"""
    name: Union[str | None, Any] = Field(default=None, description="Client name")
    """Client name"""

class TimeEntryProject(BaseModel):
    """The project associated with the time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Project ID")
    """Project ID"""
    name: Union[str | None, Any] = Field(default=None, description="Project name")
    """Project name"""

class TimeEntry(BaseModel):
    """A Harvest time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    spent_date: Union[str | None, Any] = Field(default=None)
    hours: Union[float | None, Any] = Field(default=None)
    hours_without_timer: Union[float | None, Any] = Field(default=None)
    rounded_hours: Union[float | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    is_locked: Union[bool | None, Any] = Field(default=None)
    locked_reason: Union[str | None, Any] = Field(default=None)
    is_closed: Union[bool | None, Any] = Field(default=None)
    is_billed: Union[bool | None, Any] = Field(default=None)
    timer_started_at: Union[str | None, Any] = Field(default=None)
    started_time: Union[str | None, Any] = Field(default=None)
    ended_time: Union[str | None, Any] = Field(default=None)
    is_running: Union[bool | None, Any] = Field(default=None)
    billable: Union[bool | None, Any] = Field(default=None)
    budgeted: Union[bool | None, Any] = Field(default=None)
    billable_rate: Union[float | None, Any] = Field(default=None)
    cost_rate: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    approval_status: Union[str | None, Any] = Field(default=None)
    is_explicitly_locked: Union[bool | None, Any] = Field(default=None)
    user: Union[TimeEntryUser | None, Any] = Field(default=None)
    client: Union[TimeEntryClient | None, Any] = Field(default=None)
    project: Union[TimeEntryProject | None, Any] = Field(default=None)
    task: Union[TimeEntryTask | None, Any] = Field(default=None)
    user_assignment: Union[dict[str, Any] | None, Any] = Field(default=None)
    task_assignment: Union[dict[str, Any] | None, Any] = Field(default=None)
    external_reference: Union[dict[str, Any] | None, Any] = Field(default=None)
    invoice: Union[TimeEntryInvoice | None, Any] = Field(default=None)

class TimeEntriesList(BaseModel):
    """Paginated list of time entries"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    time_entries: Union[list[TimeEntry], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Invoice(BaseModel):
    """A Harvest invoice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    client_key: Union[str | None, Any] = Field(default=None)
    number: Union[str | None, Any] = Field(default=None)
    purchase_order: Union[str | None, Any] = Field(default=None)
    amount: Union[float | None, Any] = Field(default=None)
    due_amount: Union[float | None, Any] = Field(default=None)
    tax: Union[float | None, Any] = Field(default=None)
    tax_amount: Union[float | None, Any] = Field(default=None)
    tax2: Union[float | None, Any] = Field(default=None)
    tax2_amount: Union[float | None, Any] = Field(default=None)
    discount: Union[float | None, Any] = Field(default=None)
    discount_amount: Union[float | None, Any] = Field(default=None)
    subject: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    period_start: Union[str | None, Any] = Field(default=None)
    period_end: Union[str | None, Any] = Field(default=None)
    issue_date: Union[str | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    payment_term: Union[str | None, Any] = Field(default=None)
    payment_options: Union[list[str] | None, Any] = Field(default=None)
    sent_at: Union[str | None, Any] = Field(default=None)
    paid_at: Union[str | None, Any] = Field(default=None)
    paid_date: Union[str | None, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    recurring_invoice_id: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    client: Union[dict[str, Any] | None, Any] = Field(default=None)
    estimate: Union[dict[str, Any] | None, Any] = Field(default=None)
    retainer: Union[dict[str, Any] | None, Any] = Field(default=None)
    creator: Union[dict[str, Any] | None, Any] = Field(default=None)
    line_items: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class InvoicesList(BaseModel):
    """Paginated list of invoices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invoices: Union[list[Invoice], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class InvoiceItemCategory(BaseModel):
    """A Harvest invoice item category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    use_as_service: Union[bool | None, Any] = Field(default=None)
    use_as_expense: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class InvoiceItemCategoriesList(BaseModel):
    """Paginated list of invoice item categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invoice_item_categories: Union[list[InvoiceItemCategory], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Estimate(BaseModel):
    """A Harvest estimate"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    client_key: Union[str | None, Any] = Field(default=None)
    number: Union[str | None, Any] = Field(default=None)
    purchase_order: Union[str | None, Any] = Field(default=None)
    amount: Union[float | None, Any] = Field(default=None)
    tax: Union[float | None, Any] = Field(default=None)
    tax_amount: Union[float | None, Any] = Field(default=None)
    tax2: Union[float | None, Any] = Field(default=None)
    tax2_amount: Union[float | None, Any] = Field(default=None)
    discount: Union[float | None, Any] = Field(default=None)
    discount_amount: Union[float | None, Any] = Field(default=None)
    subject: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    issue_date: Union[str | None, Any] = Field(default=None)
    sent_at: Union[str | None, Any] = Field(default=None)
    accepted_at: Union[str | None, Any] = Field(default=None)
    declined_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    client: Union[dict[str, Any] | None, Any] = Field(default=None)
    creator: Union[dict[str, Any] | None, Any] = Field(default=None)
    line_items: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class EstimatesList(BaseModel):
    """Paginated list of estimates"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    estimates: Union[list[Estimate], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class EstimateItemCategory(BaseModel):
    """A Harvest estimate item category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class EstimateItemCategoriesList(BaseModel):
    """Paginated list of estimate item categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    estimate_item_categories: Union[list[EstimateItemCategory], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Expense(BaseModel):
    """A Harvest expense"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    total_cost: Union[float | None, Any] = Field(default=None)
    units: Union[float | None, Any] = Field(default=None)
    is_closed: Union[bool | None, Any] = Field(default=None)
    is_locked: Union[bool | None, Any] = Field(default=None)
    is_billed: Union[bool | None, Any] = Field(default=None)
    locked_reason: Union[str | None, Any] = Field(default=None)
    spent_date: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    billable: Union[bool | None, Any] = Field(default=None)
    approval_status: Union[str | None, Any] = Field(default=None)
    is_explicitly_locked: Union[bool | None, Any] = Field(default=None)
    receipt: Union[dict[str, Any] | None, Any] = Field(default=None)
    user: Union[dict[str, Any] | None, Any] = Field(default=None)
    user_assignment: Union[dict[str, Any] | None, Any] = Field(default=None)
    project: Union[dict[str, Any] | None, Any] = Field(default=None)
    expense_category: Union[dict[str, Any] | None, Any] = Field(default=None)
    client: Union[dict[str, Any] | None, Any] = Field(default=None)
    invoice: Union[dict[str, Any] | None, Any] = Field(default=None)

class ExpensesList(BaseModel):
    """Paginated list of expenses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expenses: Union[list[Expense], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class ExpenseCategory(BaseModel):
    """A Harvest expense category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    unit_name: Union[str | None, Any] = Field(default=None)
    unit_price: Union[float | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class ExpenseCategoriesList(BaseModel):
    """Paginated list of expense categories"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expense_categories: Union[list[ExpenseCategory], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class Role(BaseModel):
    """A Harvest role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    user_ids: Union[list[int] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class RolesList(BaseModel):
    """Paginated list of roles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    roles: Union[list[Role], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class UserAssignmentProject(BaseModel):
    """The project associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Project ID")
    """Project ID"""
    name: Union[str | None, Any] = Field(default=None, description="Project name")
    """Project name"""
    code: Union[str | None, Any] = Field(default=None, description="Project code")
    """Project code"""

class UserAssignmentUser(BaseModel):
    """The user associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="User ID")
    """User ID"""
    name: Union[str | None, Any] = Field(default=None, description="User name")
    """User name"""

class UserAssignment(BaseModel):
    """A Harvest user assignment linking a user to a project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    is_project_manager: Union[bool | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    budget: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    hourly_rate: Union[float | None, Any] = Field(default=None)
    use_default_rates: Union[bool | None, Any] = Field(default=None)
    project: Union[UserAssignmentProject | None, Any] = Field(default=None)
    user: Union[UserAssignmentUser | None, Any] = Field(default=None)

class UserAssignmentsList(BaseModel):
    """Paginated list of user assignments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_assignments: Union[list[UserAssignment], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class TaskAssignmentTask(BaseModel):
    """The task associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Task ID")
    """Task ID"""
    name: Union[str | None, Any] = Field(default=None, description="Task name")
    """Task name"""

class TaskAssignmentProject(BaseModel):
    """The project associated with the assignment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None, description="Project ID")
    """Project ID"""
    name: Union[str | None, Any] = Field(default=None, description="Project name")
    """Project name"""
    code: Union[str | None, Any] = Field(default=None, description="Project code")
    """Project code"""

class TaskAssignment(BaseModel):
    """A Harvest task assignment linking a task to a project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    billable: Union[bool | None, Any] = Field(default=None)
    is_active: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    hourly_rate: Union[float | None, Any] = Field(default=None)
    budget: Union[float | None, Any] = Field(default=None)
    project: Union[TaskAssignmentProject | None, Any] = Field(default=None)
    task: Union[TaskAssignmentTask | None, Any] = Field(default=None)

class TaskAssignmentsList(BaseModel):
    """Paginated list of task assignments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    task_assignments: Union[list[TaskAssignment], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class TimeProject(BaseModel):
    """A time report entry grouped by project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project_id: Union[int | None, Any] = Field(default=None)
    project_name: Union[str | None, Any] = Field(default=None)
    client_id: Union[int | None, Any] = Field(default=None)
    client_name: Union[str | None, Any] = Field(default=None)
    total_hours: Union[float | None, Any] = Field(default=None)
    billable_hours: Union[float | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    billable_amount: Union[float | None, Any] = Field(default=None)

class TimeProjectsList(BaseModel):
    """Paginated list of time report entries by project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[TimeProject], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

class TimeTask(BaseModel):
    """A time report entry grouped by task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    task_id: Union[int | None, Any] = Field(default=None)
    task_name: Union[str | None, Any] = Field(default=None)
    total_hours: Union[float | None, Any] = Field(default=None)
    billable_hours: Union[float | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    billable_amount: Union[float | None, Any] = Field(default=None)

class TimeTasksList(BaseModel):
    """Paginated list of time report entries by task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[TimeTask], Any] = Field(default=None)
    per_page: Union[int, Any] = Field(default=None)
    total_pages: Union[int, Any] = Field(default=None)
    total_entries: Union[int, Any] = Field(default=None)
    page: Union[int, Any] = Field(default=None)
    next_page: Union[int | None, Any] = Field(default=None)
    previous_page: Union[int | None, Any] = Field(default=None)
    links: Union[PaginationLinks, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class ClientsListResultMeta(BaseModel):
    """Metadata for clients.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class TimeEntriesListResultMeta(BaseModel):
    """Metadata for time_entries.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class InvoicesListResultMeta(BaseModel):
    """Metadata for invoices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class InvoiceItemCategoriesListResultMeta(BaseModel):
    """Metadata for invoice_item_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class EstimatesListResultMeta(BaseModel):
    """Metadata for estimates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class EstimateItemCategoriesListResultMeta(BaseModel):
    """Metadata for estimate_item_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class ExpensesListResultMeta(BaseModel):
    """Metadata for expenses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class ExpenseCategoriesListResultMeta(BaseModel):
    """Metadata for expense_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class RolesListResultMeta(BaseModel):
    """Metadata for roles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class UserAssignmentsListResultMeta(BaseModel):
    """Metadata for user_assignments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class TaskAssignmentsListResultMeta(BaseModel):
    """Metadata for task_assignments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class TimeProjectsListResultMeta(BaseModel):
    """Metadata for time_projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

class TimeTasksListResultMeta(BaseModel):
    """Metadata for time_tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_link: Union[str | None, Any] = Field(default=None)

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
    meta: S
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

