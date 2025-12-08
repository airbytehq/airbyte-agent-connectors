"""
Pydantic models for linear connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class LinearAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """API authentication key"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Issue(BaseModel):
    """Linear issue object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    description: Union[Any, Any] = Field(default=None)
    state: Union[Any, Any] = Field(default=None)
    priority: Union[Any, Any] = Field(default=None)
    assignee: Union[Any, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")

class IssuesListResponseDataIssuesPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: Union[str | None, Any] = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class IssuesListResponseDataIssues(BaseModel):
    """Nested schema for IssuesListResponseData.issues"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: Union[list[Issue], Any] = Field(default=None)
    page_info: Union[IssuesListResponseDataIssuesPageinfo, Any] = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class IssuesListResponseData(BaseModel):
    """Nested schema for IssuesListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issues: Union[IssuesListResponseDataIssues, Any] = Field(default=None)

class IssuesListResponse(BaseModel):
    """GraphQL response for issues list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[IssuesListResponseData, Any] = Field(default=None)

class IssueResponseData(BaseModel):
    """Nested schema for IssueResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue: Union[Issue, Any] = Field(default=None)

class IssueResponse(BaseModel):
    """GraphQL response for single issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[IssueResponseData, Any] = Field(default=None)

class Project(BaseModel):
    """Linear project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[Any, Any] = Field(default=None)
    state: Union[Any, Any] = Field(default=None)
    start_date: Union[Any, Any] = Field(default=None, alias="startDate")
    target_date: Union[Any, Any] = Field(default=None, alias="targetDate")
    lead: Union[Any, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")

class ProjectsListResponseDataProjectsPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: Union[str | None, Any] = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class ProjectsListResponseDataProjects(BaseModel):
    """Nested schema for ProjectsListResponseData.projects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: Union[list[Project], Any] = Field(default=None)
    page_info: Union[ProjectsListResponseDataProjectsPageinfo, Any] = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class ProjectsListResponseData(BaseModel):
    """Nested schema for ProjectsListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    projects: Union[ProjectsListResponseDataProjects, Any] = Field(default=None)

class ProjectsListResponse(BaseModel):
    """GraphQL response for projects list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[ProjectsListResponseData, Any] = Field(default=None)

class ProjectResponseData(BaseModel):
    """Nested schema for ProjectResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project: Union[Project, Any] = Field(default=None)

class ProjectResponse(BaseModel):
    """GraphQL response for single project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[ProjectResponseData, Any] = Field(default=None)

class Team(BaseModel):
    """Linear team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    key: Union[str, Any] = Field(default=None)
    description: Union[Any, Any] = Field(default=None)
    timezone: Union[Any, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")

class TeamsListResponseDataTeamsPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: Union[str | None, Any] = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class TeamsListResponseDataTeams(BaseModel):
    """Nested schema for TeamsListResponseData.teams"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: Union[list[Team], Any] = Field(default=None)
    page_info: Union[TeamsListResponseDataTeamsPageinfo, Any] = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class TeamsListResponseData(BaseModel):
    """Nested schema for TeamsListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    teams: Union[TeamsListResponseDataTeams, Any] = Field(default=None)

class TeamsListResponse(BaseModel):
    """GraphQL response for teams list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[TeamsListResponseData, Any] = Field(default=None)

class TeamResponseData(BaseModel):
    """Nested schema for TeamResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    team: Union[Team, Any] = Field(default=None)

class TeamResponse(BaseModel):
    """GraphQL response for single team"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[TeamResponseData, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class LinearExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class LinearExecuteResultWithMeta(LinearExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

