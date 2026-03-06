"""
Type definitions for typeform connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class FormsListParams(TypedDict):
    """Parameters for forms.list operation"""
    page: NotRequired[int]
    page_size: NotRequired[int]

class FormsGetParams(TypedDict):
    """Parameters for forms.get operation"""
    form_id: str

class ResponsesListParams(TypedDict):
    """Parameters for responses.list operation"""
    form_id: str
    page_size: NotRequired[int]
    since: NotRequired[str]
    until: NotRequired[str]
    after: NotRequired[str]
    before: NotRequired[str]
    sort: NotRequired[str]
    completed: NotRequired[bool]
    query: NotRequired[str]

class WebhooksListParams(TypedDict):
    """Parameters for webhooks.list operation"""
    form_id: str

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    page: NotRequired[int]
    page_size: NotRequired[int]

class ImagesListParams(TypedDict):
    """Parameters for images.list operation"""
    pass

class ThemesListParams(TypedDict):
    """Parameters for themes.list operation"""
    page: NotRequired[int]
    page_size: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== FORMS SEARCH TYPES =====

class FormsSearchFilter(TypedDict, total=False):
    """Available fields for filtering forms search queries."""
    links: dict[str, Any] | None
    """Links to related resources"""
    created_at: str | None
    """Date and time when the form was created"""
    fields: list[Any] | None
    """List of fields within the form"""
    id: str | None
    """Unique identifier of the form"""
    last_updated_at: str | None
    """Date and time when the form was last updated"""
    logic: list[Any] | None
    """Logic rules or conditions applied to the form fields"""
    published_at: str | None
    """Date and time when the form was published"""
    settings: dict[str, Any] | None
    """Settings and configurations for the form"""
    thankyou_screens: list[Any] | None
    """Thank you screen configurations"""
    theme: dict[str, Any] | None
    """Theme settings for the form"""
    title: str | None
    """Title of the form"""
    type_: str | None
    """Type of the form"""
    welcome_screens: list[Any] | None
    """Welcome screen configurations"""
    workspace: dict[str, Any] | None
    """Workspace details where the form belongs"""


class FormsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    links: list[dict[str, Any]]
    """Links to related resources"""
    created_at: list[str]
    """Date and time when the form was created"""
    fields: list[list[Any]]
    """List of fields within the form"""
    id: list[str]
    """Unique identifier of the form"""
    last_updated_at: list[str]
    """Date and time when the form was last updated"""
    logic: list[list[Any]]
    """Logic rules or conditions applied to the form fields"""
    published_at: list[str]
    """Date and time when the form was published"""
    settings: list[dict[str, Any]]
    """Settings and configurations for the form"""
    thankyou_screens: list[list[Any]]
    """Thank you screen configurations"""
    theme: list[dict[str, Any]]
    """Theme settings for the form"""
    title: list[str]
    """Title of the form"""
    type_: list[str]
    """Type of the form"""
    welcome_screens: list[list[Any]]
    """Welcome screen configurations"""
    workspace: list[dict[str, Any]]
    """Workspace details where the form belongs"""


class FormsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    links: Any
    """Links to related resources"""
    created_at: Any
    """Date and time when the form was created"""
    fields: Any
    """List of fields within the form"""
    id: Any
    """Unique identifier of the form"""
    last_updated_at: Any
    """Date and time when the form was last updated"""
    logic: Any
    """Logic rules or conditions applied to the form fields"""
    published_at: Any
    """Date and time when the form was published"""
    settings: Any
    """Settings and configurations for the form"""
    thankyou_screens: Any
    """Thank you screen configurations"""
    theme: Any
    """Theme settings for the form"""
    title: Any
    """Title of the form"""
    type_: Any
    """Type of the form"""
    welcome_screens: Any
    """Welcome screen configurations"""
    workspace: Any
    """Workspace details where the form belongs"""


class FormsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    links: str
    """Links to related resources"""
    created_at: str
    """Date and time when the form was created"""
    fields: str
    """List of fields within the form"""
    id: str
    """Unique identifier of the form"""
    last_updated_at: str
    """Date and time when the form was last updated"""
    logic: str
    """Logic rules or conditions applied to the form fields"""
    published_at: str
    """Date and time when the form was published"""
    settings: str
    """Settings and configurations for the form"""
    thankyou_screens: str
    """Thank you screen configurations"""
    theme: str
    """Theme settings for the form"""
    title: str
    """Title of the form"""
    type_: str
    """Type of the form"""
    welcome_screens: str
    """Welcome screen configurations"""
    workspace: str
    """Workspace details where the form belongs"""


class FormsSortFilter(TypedDict, total=False):
    """Available fields for sorting forms search results."""
    links: AirbyteSortOrder
    """Links to related resources"""
    created_at: AirbyteSortOrder
    """Date and time when the form was created"""
    fields: AirbyteSortOrder
    """List of fields within the form"""
    id: AirbyteSortOrder
    """Unique identifier of the form"""
    last_updated_at: AirbyteSortOrder
    """Date and time when the form was last updated"""
    logic: AirbyteSortOrder
    """Logic rules or conditions applied to the form fields"""
    published_at: AirbyteSortOrder
    """Date and time when the form was published"""
    settings: AirbyteSortOrder
    """Settings and configurations for the form"""
    thankyou_screens: AirbyteSortOrder
    """Thank you screen configurations"""
    theme: AirbyteSortOrder
    """Theme settings for the form"""
    title: AirbyteSortOrder
    """Title of the form"""
    type_: AirbyteSortOrder
    """Type of the form"""
    welcome_screens: AirbyteSortOrder
    """Welcome screen configurations"""
    workspace: AirbyteSortOrder
    """Workspace details where the form belongs"""


# Entity-specific condition types for forms
class FormsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FormsSearchFilter


class FormsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FormsSearchFilter


class FormsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FormsSearchFilter


class FormsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FormsSearchFilter


class FormsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FormsSearchFilter


class FormsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FormsSearchFilter


class FormsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FormsStringFilter


class FormsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FormsStringFilter


class FormsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FormsStringFilter


class FormsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FormsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FormsInCondition = TypedDict("FormsInCondition", {"in": FormsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FormsNotCondition = TypedDict("FormsNotCondition", {"not": "FormsCondition"}, total=False)
"""Negates the nested condition."""

FormsAndCondition = TypedDict("FormsAndCondition", {"and": "list[FormsCondition]"}, total=False)
"""True if all nested conditions are true."""

FormsOrCondition = TypedDict("FormsOrCondition", {"or": "list[FormsCondition]"}, total=False)
"""True if any nested condition is true."""

FormsAnyCondition = TypedDict("FormsAnyCondition", {"any": FormsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all forms condition types
FormsCondition = (
    FormsEqCondition
    | FormsNeqCondition
    | FormsGtCondition
    | FormsGteCondition
    | FormsLtCondition
    | FormsLteCondition
    | FormsInCondition
    | FormsLikeCondition
    | FormsFuzzyCondition
    | FormsKeywordCondition
    | FormsContainsCondition
    | FormsNotCondition
    | FormsAndCondition
    | FormsOrCondition
    | FormsAnyCondition
)


class FormsSearchQuery(TypedDict, total=False):
    """Search query for forms entity."""
    filter: FormsCondition
    sort: list[FormsSortFilter]


# ===== RESPONSES SEARCH TYPES =====

class ResponsesSearchFilter(TypedDict, total=False):
    """Available fields for filtering responses search queries."""
    answers: list[Any] | None
    """Response data for each question in the form"""
    calculated: dict[str, Any] | None
    """Calculated data related to the response"""
    form_id: str | None
    """ID of the form"""
    hidden: dict[str, Any] | None
    """Hidden fields in the response"""
    landed_at: str | None
    """Timestamp when the respondent landed on the form"""
    landing_id: str | None
    """ID of the landing page"""
    metadata: dict[str, Any] | None
    """Metadata related to the response"""
    response_id: str | None
    """ID of the response"""
    response_type: str | None
    """Type of the response"""
    submitted_at: str | None
    """Timestamp when the response was submitted"""
    token: str | None
    """Token associated with the response"""
    variables: list[Any] | None
    """Variables associated with the response"""


class ResponsesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    answers: list[list[Any]]
    """Response data for each question in the form"""
    calculated: list[dict[str, Any]]
    """Calculated data related to the response"""
    form_id: list[str]
    """ID of the form"""
    hidden: list[dict[str, Any]]
    """Hidden fields in the response"""
    landed_at: list[str]
    """Timestamp when the respondent landed on the form"""
    landing_id: list[str]
    """ID of the landing page"""
    metadata: list[dict[str, Any]]
    """Metadata related to the response"""
    response_id: list[str]
    """ID of the response"""
    response_type: list[str]
    """Type of the response"""
    submitted_at: list[str]
    """Timestamp when the response was submitted"""
    token: list[str]
    """Token associated with the response"""
    variables: list[list[Any]]
    """Variables associated with the response"""


class ResponsesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    answers: Any
    """Response data for each question in the form"""
    calculated: Any
    """Calculated data related to the response"""
    form_id: Any
    """ID of the form"""
    hidden: Any
    """Hidden fields in the response"""
    landed_at: Any
    """Timestamp when the respondent landed on the form"""
    landing_id: Any
    """ID of the landing page"""
    metadata: Any
    """Metadata related to the response"""
    response_id: Any
    """ID of the response"""
    response_type: Any
    """Type of the response"""
    submitted_at: Any
    """Timestamp when the response was submitted"""
    token: Any
    """Token associated with the response"""
    variables: Any
    """Variables associated with the response"""


class ResponsesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    answers: str
    """Response data for each question in the form"""
    calculated: str
    """Calculated data related to the response"""
    form_id: str
    """ID of the form"""
    hidden: str
    """Hidden fields in the response"""
    landed_at: str
    """Timestamp when the respondent landed on the form"""
    landing_id: str
    """ID of the landing page"""
    metadata: str
    """Metadata related to the response"""
    response_id: str
    """ID of the response"""
    response_type: str
    """Type of the response"""
    submitted_at: str
    """Timestamp when the response was submitted"""
    token: str
    """Token associated with the response"""
    variables: str
    """Variables associated with the response"""


class ResponsesSortFilter(TypedDict, total=False):
    """Available fields for sorting responses search results."""
    answers: AirbyteSortOrder
    """Response data for each question in the form"""
    calculated: AirbyteSortOrder
    """Calculated data related to the response"""
    form_id: AirbyteSortOrder
    """ID of the form"""
    hidden: AirbyteSortOrder
    """Hidden fields in the response"""
    landed_at: AirbyteSortOrder
    """Timestamp when the respondent landed on the form"""
    landing_id: AirbyteSortOrder
    """ID of the landing page"""
    metadata: AirbyteSortOrder
    """Metadata related to the response"""
    response_id: AirbyteSortOrder
    """ID of the response"""
    response_type: AirbyteSortOrder
    """Type of the response"""
    submitted_at: AirbyteSortOrder
    """Timestamp when the response was submitted"""
    token: AirbyteSortOrder
    """Token associated with the response"""
    variables: AirbyteSortOrder
    """Variables associated with the response"""


# Entity-specific condition types for responses
class ResponsesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ResponsesSearchFilter


class ResponsesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ResponsesSearchFilter


class ResponsesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ResponsesSearchFilter


class ResponsesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ResponsesSearchFilter


class ResponsesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ResponsesSearchFilter


class ResponsesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ResponsesSearchFilter


class ResponsesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ResponsesStringFilter


class ResponsesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ResponsesStringFilter


class ResponsesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ResponsesStringFilter


class ResponsesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ResponsesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ResponsesInCondition = TypedDict("ResponsesInCondition", {"in": ResponsesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ResponsesNotCondition = TypedDict("ResponsesNotCondition", {"not": "ResponsesCondition"}, total=False)
"""Negates the nested condition."""

ResponsesAndCondition = TypedDict("ResponsesAndCondition", {"and": "list[ResponsesCondition]"}, total=False)
"""True if all nested conditions are true."""

ResponsesOrCondition = TypedDict("ResponsesOrCondition", {"or": "list[ResponsesCondition]"}, total=False)
"""True if any nested condition is true."""

ResponsesAnyCondition = TypedDict("ResponsesAnyCondition", {"any": ResponsesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all responses condition types
ResponsesCondition = (
    ResponsesEqCondition
    | ResponsesNeqCondition
    | ResponsesGtCondition
    | ResponsesGteCondition
    | ResponsesLtCondition
    | ResponsesLteCondition
    | ResponsesInCondition
    | ResponsesLikeCondition
    | ResponsesFuzzyCondition
    | ResponsesKeywordCondition
    | ResponsesContainsCondition
    | ResponsesNotCondition
    | ResponsesAndCondition
    | ResponsesOrCondition
    | ResponsesAnyCondition
)


class ResponsesSearchQuery(TypedDict, total=False):
    """Search query for responses entity."""
    filter: ResponsesCondition
    sort: list[ResponsesSortFilter]


# ===== WEBHOOKS SEARCH TYPES =====

class WebhooksSearchFilter(TypedDict, total=False):
    """Available fields for filtering webhooks search queries."""
    created_at: str | None
    """Timestamp when the webhook was created"""
    enabled: bool | None
    """Whether the webhook is currently enabled"""
    form_id: str | None
    """ID of the form associated with the webhook"""
    id: str | None
    """Unique identifier of the webhook"""
    tag: str | None
    """Tag to categorize or label the webhook"""
    updated_at: str | None
    """Timestamp when the webhook was last updated"""
    url: str | None
    """URL where webhook data is sent"""
    verify_ssl: bool | None
    """Whether SSL verification is enforced"""


class WebhooksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Timestamp when the webhook was created"""
    enabled: list[bool]
    """Whether the webhook is currently enabled"""
    form_id: list[str]
    """ID of the form associated with the webhook"""
    id: list[str]
    """Unique identifier of the webhook"""
    tag: list[str]
    """Tag to categorize or label the webhook"""
    updated_at: list[str]
    """Timestamp when the webhook was last updated"""
    url: list[str]
    """URL where webhook data is sent"""
    verify_ssl: list[bool]
    """Whether SSL verification is enforced"""


class WebhooksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Timestamp when the webhook was created"""
    enabled: Any
    """Whether the webhook is currently enabled"""
    form_id: Any
    """ID of the form associated with the webhook"""
    id: Any
    """Unique identifier of the webhook"""
    tag: Any
    """Tag to categorize or label the webhook"""
    updated_at: Any
    """Timestamp when the webhook was last updated"""
    url: Any
    """URL where webhook data is sent"""
    verify_ssl: Any
    """Whether SSL verification is enforced"""


class WebhooksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """Timestamp when the webhook was created"""
    enabled: str
    """Whether the webhook is currently enabled"""
    form_id: str
    """ID of the form associated with the webhook"""
    id: str
    """Unique identifier of the webhook"""
    tag: str
    """Tag to categorize or label the webhook"""
    updated_at: str
    """Timestamp when the webhook was last updated"""
    url: str
    """URL where webhook data is sent"""
    verify_ssl: str
    """Whether SSL verification is enforced"""


class WebhooksSortFilter(TypedDict, total=False):
    """Available fields for sorting webhooks search results."""
    created_at: AirbyteSortOrder
    """Timestamp when the webhook was created"""
    enabled: AirbyteSortOrder
    """Whether the webhook is currently enabled"""
    form_id: AirbyteSortOrder
    """ID of the form associated with the webhook"""
    id: AirbyteSortOrder
    """Unique identifier of the webhook"""
    tag: AirbyteSortOrder
    """Tag to categorize or label the webhook"""
    updated_at: AirbyteSortOrder
    """Timestamp when the webhook was last updated"""
    url: AirbyteSortOrder
    """URL where webhook data is sent"""
    verify_ssl: AirbyteSortOrder
    """Whether SSL verification is enforced"""


# Entity-specific condition types for webhooks
class WebhooksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: WebhooksSearchFilter


class WebhooksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: WebhooksSearchFilter


class WebhooksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: WebhooksSearchFilter


class WebhooksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: WebhooksSearchFilter


class WebhooksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: WebhooksSearchFilter


class WebhooksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: WebhooksSearchFilter


class WebhooksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: WebhooksStringFilter


class WebhooksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: WebhooksStringFilter


class WebhooksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: WebhooksStringFilter


class WebhooksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: WebhooksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
WebhooksInCondition = TypedDict("WebhooksInCondition", {"in": WebhooksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

WebhooksNotCondition = TypedDict("WebhooksNotCondition", {"not": "WebhooksCondition"}, total=False)
"""Negates the nested condition."""

WebhooksAndCondition = TypedDict("WebhooksAndCondition", {"and": "list[WebhooksCondition]"}, total=False)
"""True if all nested conditions are true."""

WebhooksOrCondition = TypedDict("WebhooksOrCondition", {"or": "list[WebhooksCondition]"}, total=False)
"""True if any nested condition is true."""

WebhooksAnyCondition = TypedDict("WebhooksAnyCondition", {"any": WebhooksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all webhooks condition types
WebhooksCondition = (
    WebhooksEqCondition
    | WebhooksNeqCondition
    | WebhooksGtCondition
    | WebhooksGteCondition
    | WebhooksLtCondition
    | WebhooksLteCondition
    | WebhooksInCondition
    | WebhooksLikeCondition
    | WebhooksFuzzyCondition
    | WebhooksKeywordCondition
    | WebhooksContainsCondition
    | WebhooksNotCondition
    | WebhooksAndCondition
    | WebhooksOrCondition
    | WebhooksAnyCondition
)


class WebhooksSearchQuery(TypedDict, total=False):
    """Search query for webhooks entity."""
    filter: WebhooksCondition
    sort: list[WebhooksSortFilter]


# ===== WORKSPACES SEARCH TYPES =====

class WorkspacesSearchFilter(TypedDict, total=False):
    """Available fields for filtering workspaces search queries."""
    account_id: str | None
    """Account ID associated with the workspace"""
    default: bool | None
    """Whether this is the default workspace"""
    forms: dict[str, Any] | None
    """Information about forms in the workspace"""
    id: str | None
    """Unique identifier of the workspace"""
    name: str | None
    """Name of the workspace"""
    self: dict[str, Any] | None
    """Self-referential link"""
    shared: bool | None
    """Whether this workspace is shared"""


class WorkspacesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_id: list[str]
    """Account ID associated with the workspace"""
    default: list[bool]
    """Whether this is the default workspace"""
    forms: list[dict[str, Any]]
    """Information about forms in the workspace"""
    id: list[str]
    """Unique identifier of the workspace"""
    name: list[str]
    """Name of the workspace"""
    self: list[dict[str, Any]]
    """Self-referential link"""
    shared: list[bool]
    """Whether this workspace is shared"""


class WorkspacesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_id: Any
    """Account ID associated with the workspace"""
    default: Any
    """Whether this is the default workspace"""
    forms: Any
    """Information about forms in the workspace"""
    id: Any
    """Unique identifier of the workspace"""
    name: Any
    """Name of the workspace"""
    self: Any
    """Self-referential link"""
    shared: Any
    """Whether this workspace is shared"""


class WorkspacesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_id: str
    """Account ID associated with the workspace"""
    default: str
    """Whether this is the default workspace"""
    forms: str
    """Information about forms in the workspace"""
    id: str
    """Unique identifier of the workspace"""
    name: str
    """Name of the workspace"""
    self: str
    """Self-referential link"""
    shared: str
    """Whether this workspace is shared"""


class WorkspacesSortFilter(TypedDict, total=False):
    """Available fields for sorting workspaces search results."""
    account_id: AirbyteSortOrder
    """Account ID associated with the workspace"""
    default: AirbyteSortOrder
    """Whether this is the default workspace"""
    forms: AirbyteSortOrder
    """Information about forms in the workspace"""
    id: AirbyteSortOrder
    """Unique identifier of the workspace"""
    name: AirbyteSortOrder
    """Name of the workspace"""
    self: AirbyteSortOrder
    """Self-referential link"""
    shared: AirbyteSortOrder
    """Whether this workspace is shared"""


# Entity-specific condition types for workspaces
class WorkspacesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: WorkspacesSearchFilter


class WorkspacesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: WorkspacesSearchFilter


class WorkspacesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: WorkspacesSearchFilter


class WorkspacesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: WorkspacesSearchFilter


class WorkspacesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: WorkspacesSearchFilter


class WorkspacesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: WorkspacesSearchFilter


class WorkspacesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: WorkspacesStringFilter


class WorkspacesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: WorkspacesStringFilter


class WorkspacesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: WorkspacesStringFilter


class WorkspacesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: WorkspacesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
WorkspacesInCondition = TypedDict("WorkspacesInCondition", {"in": WorkspacesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

WorkspacesNotCondition = TypedDict("WorkspacesNotCondition", {"not": "WorkspacesCondition"}, total=False)
"""Negates the nested condition."""

WorkspacesAndCondition = TypedDict("WorkspacesAndCondition", {"and": "list[WorkspacesCondition]"}, total=False)
"""True if all nested conditions are true."""

WorkspacesOrCondition = TypedDict("WorkspacesOrCondition", {"or": "list[WorkspacesCondition]"}, total=False)
"""True if any nested condition is true."""

WorkspacesAnyCondition = TypedDict("WorkspacesAnyCondition", {"any": WorkspacesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all workspaces condition types
WorkspacesCondition = (
    WorkspacesEqCondition
    | WorkspacesNeqCondition
    | WorkspacesGtCondition
    | WorkspacesGteCondition
    | WorkspacesLtCondition
    | WorkspacesLteCondition
    | WorkspacesInCondition
    | WorkspacesLikeCondition
    | WorkspacesFuzzyCondition
    | WorkspacesKeywordCondition
    | WorkspacesContainsCondition
    | WorkspacesNotCondition
    | WorkspacesAndCondition
    | WorkspacesOrCondition
    | WorkspacesAnyCondition
)


class WorkspacesSearchQuery(TypedDict, total=False):
    """Search query for workspaces entity."""
    filter: WorkspacesCondition
    sort: list[WorkspacesSortFilter]


# ===== IMAGES SEARCH TYPES =====

class ImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering images search queries."""
    avg_color: str | None
    """Average color of the image"""
    file_name: str | None
    """Name of the image file"""
    has_alpha: bool | None
    """Whether the image has an alpha channel"""
    height: int | None
    """Height of the image in pixels"""
    id: str | None
    """Unique identifier of the image"""
    media_type: str | None
    """MIME type of the image"""
    src: str | None
    """URL to access the image"""
    width: int | None
    """Width of the image in pixels"""


class ImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    avg_color: list[str]
    """Average color of the image"""
    file_name: list[str]
    """Name of the image file"""
    has_alpha: list[bool]
    """Whether the image has an alpha channel"""
    height: list[int]
    """Height of the image in pixels"""
    id: list[str]
    """Unique identifier of the image"""
    media_type: list[str]
    """MIME type of the image"""
    src: list[str]
    """URL to access the image"""
    width: list[int]
    """Width of the image in pixels"""


class ImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    avg_color: Any
    """Average color of the image"""
    file_name: Any
    """Name of the image file"""
    has_alpha: Any
    """Whether the image has an alpha channel"""
    height: Any
    """Height of the image in pixels"""
    id: Any
    """Unique identifier of the image"""
    media_type: Any
    """MIME type of the image"""
    src: Any
    """URL to access the image"""
    width: Any
    """Width of the image in pixels"""


class ImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    avg_color: str
    """Average color of the image"""
    file_name: str
    """Name of the image file"""
    has_alpha: str
    """Whether the image has an alpha channel"""
    height: str
    """Height of the image in pixels"""
    id: str
    """Unique identifier of the image"""
    media_type: str
    """MIME type of the image"""
    src: str
    """URL to access the image"""
    width: str
    """Width of the image in pixels"""


class ImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting images search results."""
    avg_color: AirbyteSortOrder
    """Average color of the image"""
    file_name: AirbyteSortOrder
    """Name of the image file"""
    has_alpha: AirbyteSortOrder
    """Whether the image has an alpha channel"""
    height: AirbyteSortOrder
    """Height of the image in pixels"""
    id: AirbyteSortOrder
    """Unique identifier of the image"""
    media_type: AirbyteSortOrder
    """MIME type of the image"""
    src: AirbyteSortOrder
    """URL to access the image"""
    width: AirbyteSortOrder
    """Width of the image in pixels"""


# Entity-specific condition types for images
class ImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ImagesSearchFilter


class ImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ImagesSearchFilter


class ImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ImagesSearchFilter


class ImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ImagesSearchFilter


class ImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ImagesSearchFilter


class ImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ImagesSearchFilter


class ImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ImagesStringFilter


class ImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ImagesStringFilter


class ImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ImagesStringFilter


class ImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ImagesInCondition = TypedDict("ImagesInCondition", {"in": ImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ImagesNotCondition = TypedDict("ImagesNotCondition", {"not": "ImagesCondition"}, total=False)
"""Negates the nested condition."""

ImagesAndCondition = TypedDict("ImagesAndCondition", {"and": "list[ImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

ImagesOrCondition = TypedDict("ImagesOrCondition", {"or": "list[ImagesCondition]"}, total=False)
"""True if any nested condition is true."""

ImagesAnyCondition = TypedDict("ImagesAnyCondition", {"any": ImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all images condition types
ImagesCondition = (
    ImagesEqCondition
    | ImagesNeqCondition
    | ImagesGtCondition
    | ImagesGteCondition
    | ImagesLtCondition
    | ImagesLteCondition
    | ImagesInCondition
    | ImagesLikeCondition
    | ImagesFuzzyCondition
    | ImagesKeywordCondition
    | ImagesContainsCondition
    | ImagesNotCondition
    | ImagesAndCondition
    | ImagesOrCondition
    | ImagesAnyCondition
)


class ImagesSearchQuery(TypedDict, total=False):
    """Search query for images entity."""
    filter: ImagesCondition
    sort: list[ImagesSortFilter]


# ===== THEMES SEARCH TYPES =====

class ThemesSearchFilter(TypedDict, total=False):
    """Available fields for filtering themes search queries."""
    background: dict[str, Any] | None
    """Background settings for the theme"""
    colors: dict[str, Any] | None
    """Color settings"""
    created_at: str | None
    """Timestamp when the theme was created"""
    fields: dict[str, Any] | None
    """Field display settings"""
    font: str | None
    """Font used in the theme"""
    has_transparent_button: bool | None
    """Whether the theme has a transparent button"""
    id: str | None
    """Unique identifier of the theme"""
    name: str | None
    """Name of the theme"""
    rounded_corners: str | None
    """Rounded corners setting"""
    screens: dict[str, Any] | None
    """Screen display settings"""
    updated_at: str | None
    """Timestamp when the theme was last updated"""
    visibility: str | None
    """Visibility setting of the theme"""


class ThemesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    background: list[dict[str, Any]]
    """Background settings for the theme"""
    colors: list[dict[str, Any]]
    """Color settings"""
    created_at: list[str]
    """Timestamp when the theme was created"""
    fields: list[dict[str, Any]]
    """Field display settings"""
    font: list[str]
    """Font used in the theme"""
    has_transparent_button: list[bool]
    """Whether the theme has a transparent button"""
    id: list[str]
    """Unique identifier of the theme"""
    name: list[str]
    """Name of the theme"""
    rounded_corners: list[str]
    """Rounded corners setting"""
    screens: list[dict[str, Any]]
    """Screen display settings"""
    updated_at: list[str]
    """Timestamp when the theme was last updated"""
    visibility: list[str]
    """Visibility setting of the theme"""


class ThemesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    background: Any
    """Background settings for the theme"""
    colors: Any
    """Color settings"""
    created_at: Any
    """Timestamp when the theme was created"""
    fields: Any
    """Field display settings"""
    font: Any
    """Font used in the theme"""
    has_transparent_button: Any
    """Whether the theme has a transparent button"""
    id: Any
    """Unique identifier of the theme"""
    name: Any
    """Name of the theme"""
    rounded_corners: Any
    """Rounded corners setting"""
    screens: Any
    """Screen display settings"""
    updated_at: Any
    """Timestamp when the theme was last updated"""
    visibility: Any
    """Visibility setting of the theme"""


class ThemesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    background: str
    """Background settings for the theme"""
    colors: str
    """Color settings"""
    created_at: str
    """Timestamp when the theme was created"""
    fields: str
    """Field display settings"""
    font: str
    """Font used in the theme"""
    has_transparent_button: str
    """Whether the theme has a transparent button"""
    id: str
    """Unique identifier of the theme"""
    name: str
    """Name of the theme"""
    rounded_corners: str
    """Rounded corners setting"""
    screens: str
    """Screen display settings"""
    updated_at: str
    """Timestamp when the theme was last updated"""
    visibility: str
    """Visibility setting of the theme"""


class ThemesSortFilter(TypedDict, total=False):
    """Available fields for sorting themes search results."""
    background: AirbyteSortOrder
    """Background settings for the theme"""
    colors: AirbyteSortOrder
    """Color settings"""
    created_at: AirbyteSortOrder
    """Timestamp when the theme was created"""
    fields: AirbyteSortOrder
    """Field display settings"""
    font: AirbyteSortOrder
    """Font used in the theme"""
    has_transparent_button: AirbyteSortOrder
    """Whether the theme has a transparent button"""
    id: AirbyteSortOrder
    """Unique identifier of the theme"""
    name: AirbyteSortOrder
    """Name of the theme"""
    rounded_corners: AirbyteSortOrder
    """Rounded corners setting"""
    screens: AirbyteSortOrder
    """Screen display settings"""
    updated_at: AirbyteSortOrder
    """Timestamp when the theme was last updated"""
    visibility: AirbyteSortOrder
    """Visibility setting of the theme"""


# Entity-specific condition types for themes
class ThemesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ThemesSearchFilter


class ThemesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ThemesSearchFilter


class ThemesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ThemesSearchFilter


class ThemesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ThemesSearchFilter


class ThemesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ThemesSearchFilter


class ThemesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ThemesSearchFilter


class ThemesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ThemesStringFilter


class ThemesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ThemesStringFilter


class ThemesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ThemesStringFilter


class ThemesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ThemesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ThemesInCondition = TypedDict("ThemesInCondition", {"in": ThemesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ThemesNotCondition = TypedDict("ThemesNotCondition", {"not": "ThemesCondition"}, total=False)
"""Negates the nested condition."""

ThemesAndCondition = TypedDict("ThemesAndCondition", {"and": "list[ThemesCondition]"}, total=False)
"""True if all nested conditions are true."""

ThemesOrCondition = TypedDict("ThemesOrCondition", {"or": "list[ThemesCondition]"}, total=False)
"""True if any nested condition is true."""

ThemesAnyCondition = TypedDict("ThemesAnyCondition", {"any": ThemesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all themes condition types
ThemesCondition = (
    ThemesEqCondition
    | ThemesNeqCondition
    | ThemesGtCondition
    | ThemesGteCondition
    | ThemesLtCondition
    | ThemesLteCondition
    | ThemesInCondition
    | ThemesLikeCondition
    | ThemesFuzzyCondition
    | ThemesKeywordCondition
    | ThemesContainsCondition
    | ThemesNotCondition
    | ThemesAndCondition
    | ThemesOrCondition
    | ThemesAnyCondition
)


class ThemesSearchQuery(TypedDict, total=False):
    """Search query for themes entity."""
    filter: ThemesCondition
    sort: list[ThemesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
