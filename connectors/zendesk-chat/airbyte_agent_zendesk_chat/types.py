"""
Type definitions for zendesk-chat connector.
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

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    pass

class AgentsListParams(TypedDict):
    """Parameters for agents.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]

class AgentsGetParams(TypedDict):
    """Parameters for agents.get operation"""
    agent_id: str

class AgentTimelineListParams(TypedDict):
    """Parameters for agent_timeline.list operation"""
    start_time: NotRequired[int]
    limit: NotRequired[int]
    fields: NotRequired[str]

class BansListParams(TypedDict):
    """Parameters for bans.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]

class BansGetParams(TypedDict):
    """Parameters for bans.get operation"""
    ban_id: str

class ChatsListParams(TypedDict):
    """Parameters for chats.list operation"""
    start_time: NotRequired[int]
    limit: NotRequired[int]
    fields: NotRequired[str]

class ChatsGetParams(TypedDict):
    """Parameters for chats.get operation"""
    chat_id: str

class DepartmentsListParams(TypedDict):
    """Parameters for departments.list operation"""
    pass

class DepartmentsGetParams(TypedDict):
    """Parameters for departments.get operation"""
    department_id: str

class GoalsListParams(TypedDict):
    """Parameters for goals.list operation"""
    pass

class GoalsGetParams(TypedDict):
    """Parameters for goals.get operation"""
    goal_id: str

class RolesListParams(TypedDict):
    """Parameters for roles.list operation"""
    pass

class RolesGetParams(TypedDict):
    """Parameters for roles.get operation"""
    role_id: str

class RoutingSettingsGetParams(TypedDict):
    """Parameters for routing_settings.get operation"""
    pass

class ShortcutsListParams(TypedDict):
    """Parameters for shortcuts.list operation"""
    pass

class ShortcutsGetParams(TypedDict):
    """Parameters for shortcuts.get operation"""
    shortcut_id: str

class SkillsListParams(TypedDict):
    """Parameters for skills.list operation"""
    pass

class SkillsGetParams(TypedDict):
    """Parameters for skills.get operation"""
    skill_id: str

class TriggersListParams(TypedDict):
    """Parameters for triggers.list operation"""
    pass

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== AGENTS SEARCH TYPES =====

class AgentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering agents search queries."""
    id: int
    """Unique agent identifier"""
    email: str | None
    """Agent email address"""
    display_name: str | None
    """Agent display name"""
    first_name: str | None
    """Agent first name"""
    last_name: str | None
    """Agent last name"""
    enabled: bool | None
    """Whether agent is enabled"""
    role_id: int | None
    """Agent role ID"""
    departments: list[Any] | None
    """Department IDs agent belongs to"""
    create_date: str | None
    """When agent was created"""


class AgentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique agent identifier"""
    email: list[str]
    """Agent email address"""
    display_name: list[str]
    """Agent display name"""
    first_name: list[str]
    """Agent first name"""
    last_name: list[str]
    """Agent last name"""
    enabled: list[bool]
    """Whether agent is enabled"""
    role_id: list[int]
    """Agent role ID"""
    departments: list[list[Any]]
    """Department IDs agent belongs to"""
    create_date: list[str]
    """When agent was created"""


class AgentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique agent identifier"""
    email: Any
    """Agent email address"""
    display_name: Any
    """Agent display name"""
    first_name: Any
    """Agent first name"""
    last_name: Any
    """Agent last name"""
    enabled: Any
    """Whether agent is enabled"""
    role_id: Any
    """Agent role ID"""
    departments: Any
    """Department IDs agent belongs to"""
    create_date: Any
    """When agent was created"""


class AgentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique agent identifier"""
    email: str
    """Agent email address"""
    display_name: str
    """Agent display name"""
    first_name: str
    """Agent first name"""
    last_name: str
    """Agent last name"""
    enabled: str
    """Whether agent is enabled"""
    role_id: str
    """Agent role ID"""
    departments: str
    """Department IDs agent belongs to"""
    create_date: str
    """When agent was created"""


class AgentsSortFilter(TypedDict, total=False):
    """Available fields for sorting agents search results."""
    id: AirbyteSortOrder
    """Unique agent identifier"""
    email: AirbyteSortOrder
    """Agent email address"""
    display_name: AirbyteSortOrder
    """Agent display name"""
    first_name: AirbyteSortOrder
    """Agent first name"""
    last_name: AirbyteSortOrder
    """Agent last name"""
    enabled: AirbyteSortOrder
    """Whether agent is enabled"""
    role_id: AirbyteSortOrder
    """Agent role ID"""
    departments: AirbyteSortOrder
    """Department IDs agent belongs to"""
    create_date: AirbyteSortOrder
    """When agent was created"""


# Entity-specific condition types for agents
class AgentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AgentsSearchFilter


class AgentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AgentsSearchFilter


class AgentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AgentsSearchFilter


class AgentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AgentsSearchFilter


class AgentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AgentsSearchFilter


class AgentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AgentsSearchFilter


class AgentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AgentsStringFilter


class AgentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AgentsStringFilter


class AgentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AgentsStringFilter


class AgentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AgentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AgentsInCondition = TypedDict("AgentsInCondition", {"in": AgentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AgentsNotCondition = TypedDict("AgentsNotCondition", {"not": "AgentsCondition"}, total=False)
"""Negates the nested condition."""

AgentsAndCondition = TypedDict("AgentsAndCondition", {"and": "list[AgentsCondition]"}, total=False)
"""True if all nested conditions are true."""

AgentsOrCondition = TypedDict("AgentsOrCondition", {"or": "list[AgentsCondition]"}, total=False)
"""True if any nested condition is true."""

AgentsAnyCondition = TypedDict("AgentsAnyCondition", {"any": AgentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all agents condition types
AgentsCondition = (
    AgentsEqCondition
    | AgentsNeqCondition
    | AgentsGtCondition
    | AgentsGteCondition
    | AgentsLtCondition
    | AgentsLteCondition
    | AgentsInCondition
    | AgentsLikeCondition
    | AgentsFuzzyCondition
    | AgentsKeywordCondition
    | AgentsContainsCondition
    | AgentsNotCondition
    | AgentsAndCondition
    | AgentsOrCondition
    | AgentsAnyCondition
)


class AgentsSearchQuery(TypedDict, total=False):
    """Search query for agents entity."""
    filter: AgentsCondition
    sort: list[AgentsSortFilter]


# ===== CHATS SEARCH TYPES =====

class ChatsSearchFilter(TypedDict, total=False):
    """Available fields for filtering chats search queries."""
    id: str
    """Unique chat identifier"""
    timestamp: str | None
    """Chat start timestamp"""
    update_timestamp: str | None
    """Last update timestamp"""
    department_id: int | None
    """Department ID"""
    department_name: str | None
    """Department name"""
    duration: int | None
    """Chat duration in seconds"""
    rating: str | None
    """Satisfaction rating"""
    missed: bool | None
    """Whether chat was missed"""
    agent_ids: list[Any] | None
    """IDs of agents in chat"""


class ChatsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique chat identifier"""
    timestamp: list[str]
    """Chat start timestamp"""
    update_timestamp: list[str]
    """Last update timestamp"""
    department_id: list[int]
    """Department ID"""
    department_name: list[str]
    """Department name"""
    duration: list[int]
    """Chat duration in seconds"""
    rating: list[str]
    """Satisfaction rating"""
    missed: list[bool]
    """Whether chat was missed"""
    agent_ids: list[list[Any]]
    """IDs of agents in chat"""


class ChatsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique chat identifier"""
    timestamp: Any
    """Chat start timestamp"""
    update_timestamp: Any
    """Last update timestamp"""
    department_id: Any
    """Department ID"""
    department_name: Any
    """Department name"""
    duration: Any
    """Chat duration in seconds"""
    rating: Any
    """Satisfaction rating"""
    missed: Any
    """Whether chat was missed"""
    agent_ids: Any
    """IDs of agents in chat"""


class ChatsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique chat identifier"""
    timestamp: str
    """Chat start timestamp"""
    update_timestamp: str
    """Last update timestamp"""
    department_id: str
    """Department ID"""
    department_name: str
    """Department name"""
    duration: str
    """Chat duration in seconds"""
    rating: str
    """Satisfaction rating"""
    missed: str
    """Whether chat was missed"""
    agent_ids: str
    """IDs of agents in chat"""


class ChatsSortFilter(TypedDict, total=False):
    """Available fields for sorting chats search results."""
    id: AirbyteSortOrder
    """Unique chat identifier"""
    timestamp: AirbyteSortOrder
    """Chat start timestamp"""
    update_timestamp: AirbyteSortOrder
    """Last update timestamp"""
    department_id: AirbyteSortOrder
    """Department ID"""
    department_name: AirbyteSortOrder
    """Department name"""
    duration: AirbyteSortOrder
    """Chat duration in seconds"""
    rating: AirbyteSortOrder
    """Satisfaction rating"""
    missed: AirbyteSortOrder
    """Whether chat was missed"""
    agent_ids: AirbyteSortOrder
    """IDs of agents in chat"""


# Entity-specific condition types for chats
class ChatsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ChatsSearchFilter


class ChatsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ChatsSearchFilter


class ChatsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ChatsSearchFilter


class ChatsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ChatsSearchFilter


class ChatsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ChatsSearchFilter


class ChatsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ChatsSearchFilter


class ChatsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ChatsStringFilter


class ChatsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ChatsStringFilter


class ChatsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ChatsStringFilter


class ChatsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ChatsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ChatsInCondition = TypedDict("ChatsInCondition", {"in": ChatsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ChatsNotCondition = TypedDict("ChatsNotCondition", {"not": "ChatsCondition"}, total=False)
"""Negates the nested condition."""

ChatsAndCondition = TypedDict("ChatsAndCondition", {"and": "list[ChatsCondition]"}, total=False)
"""True if all nested conditions are true."""

ChatsOrCondition = TypedDict("ChatsOrCondition", {"or": "list[ChatsCondition]"}, total=False)
"""True if any nested condition is true."""

ChatsAnyCondition = TypedDict("ChatsAnyCondition", {"any": ChatsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all chats condition types
ChatsCondition = (
    ChatsEqCondition
    | ChatsNeqCondition
    | ChatsGtCondition
    | ChatsGteCondition
    | ChatsLtCondition
    | ChatsLteCondition
    | ChatsInCondition
    | ChatsLikeCondition
    | ChatsFuzzyCondition
    | ChatsKeywordCondition
    | ChatsContainsCondition
    | ChatsNotCondition
    | ChatsAndCondition
    | ChatsOrCondition
    | ChatsAnyCondition
)


class ChatsSearchQuery(TypedDict, total=False):
    """Search query for chats entity."""
    filter: ChatsCondition
    sort: list[ChatsSortFilter]


# ===== DEPARTMENTS SEARCH TYPES =====

class DepartmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering departments search queries."""
    id: int
    """Department ID"""
    name: str | None
    """Department name"""
    enabled: bool | None
    """Whether department is enabled"""
    members: list[Any] | None
    """Agent IDs in department"""


class DepartmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Department ID"""
    name: list[str]
    """Department name"""
    enabled: list[bool]
    """Whether department is enabled"""
    members: list[list[Any]]
    """Agent IDs in department"""


class DepartmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Department ID"""
    name: Any
    """Department name"""
    enabled: Any
    """Whether department is enabled"""
    members: Any
    """Agent IDs in department"""


class DepartmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Department ID"""
    name: str
    """Department name"""
    enabled: str
    """Whether department is enabled"""
    members: str
    """Agent IDs in department"""


class DepartmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting departments search results."""
    id: AirbyteSortOrder
    """Department ID"""
    name: AirbyteSortOrder
    """Department name"""
    enabled: AirbyteSortOrder
    """Whether department is enabled"""
    members: AirbyteSortOrder
    """Agent IDs in department"""


# Entity-specific condition types for departments
class DepartmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DepartmentsSearchFilter


class DepartmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DepartmentsSearchFilter


class DepartmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DepartmentsSearchFilter


class DepartmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DepartmentsSearchFilter


class DepartmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DepartmentsSearchFilter


class DepartmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DepartmentsSearchFilter


class DepartmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DepartmentsStringFilter


class DepartmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DepartmentsStringFilter


class DepartmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DepartmentsStringFilter


class DepartmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DepartmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DepartmentsInCondition = TypedDict("DepartmentsInCondition", {"in": DepartmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DepartmentsNotCondition = TypedDict("DepartmentsNotCondition", {"not": "DepartmentsCondition"}, total=False)
"""Negates the nested condition."""

DepartmentsAndCondition = TypedDict("DepartmentsAndCondition", {"and": "list[DepartmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

DepartmentsOrCondition = TypedDict("DepartmentsOrCondition", {"or": "list[DepartmentsCondition]"}, total=False)
"""True if any nested condition is true."""

DepartmentsAnyCondition = TypedDict("DepartmentsAnyCondition", {"any": DepartmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all departments condition types
DepartmentsCondition = (
    DepartmentsEqCondition
    | DepartmentsNeqCondition
    | DepartmentsGtCondition
    | DepartmentsGteCondition
    | DepartmentsLtCondition
    | DepartmentsLteCondition
    | DepartmentsInCondition
    | DepartmentsLikeCondition
    | DepartmentsFuzzyCondition
    | DepartmentsKeywordCondition
    | DepartmentsContainsCondition
    | DepartmentsNotCondition
    | DepartmentsAndCondition
    | DepartmentsOrCondition
    | DepartmentsAnyCondition
)


class DepartmentsSearchQuery(TypedDict, total=False):
    """Search query for departments entity."""
    filter: DepartmentsCondition
    sort: list[DepartmentsSortFilter]


# ===== SHORTCUTS SEARCH TYPES =====

class ShortcutsSearchFilter(TypedDict, total=False):
    """Available fields for filtering shortcuts search queries."""
    id: int
    """Shortcut ID"""
    name: str | None
    """Shortcut name/trigger"""
    message: str | None
    """Shortcut message content"""
    tags: list[Any] | None
    """Tags applied when shortcut is used"""


class ShortcutsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Shortcut ID"""
    name: list[str]
    """Shortcut name/trigger"""
    message: list[str]
    """Shortcut message content"""
    tags: list[list[Any]]
    """Tags applied when shortcut is used"""


class ShortcutsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Shortcut ID"""
    name: Any
    """Shortcut name/trigger"""
    message: Any
    """Shortcut message content"""
    tags: Any
    """Tags applied when shortcut is used"""


class ShortcutsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Shortcut ID"""
    name: str
    """Shortcut name/trigger"""
    message: str
    """Shortcut message content"""
    tags: str
    """Tags applied when shortcut is used"""


class ShortcutsSortFilter(TypedDict, total=False):
    """Available fields for sorting shortcuts search results."""
    id: AirbyteSortOrder
    """Shortcut ID"""
    name: AirbyteSortOrder
    """Shortcut name/trigger"""
    message: AirbyteSortOrder
    """Shortcut message content"""
    tags: AirbyteSortOrder
    """Tags applied when shortcut is used"""


# Entity-specific condition types for shortcuts
class ShortcutsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ShortcutsSearchFilter


class ShortcutsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ShortcutsSearchFilter


class ShortcutsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ShortcutsSearchFilter


class ShortcutsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ShortcutsSearchFilter


class ShortcutsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ShortcutsSearchFilter


class ShortcutsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ShortcutsSearchFilter


class ShortcutsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ShortcutsStringFilter


class ShortcutsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ShortcutsStringFilter


class ShortcutsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ShortcutsStringFilter


class ShortcutsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ShortcutsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ShortcutsInCondition = TypedDict("ShortcutsInCondition", {"in": ShortcutsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ShortcutsNotCondition = TypedDict("ShortcutsNotCondition", {"not": "ShortcutsCondition"}, total=False)
"""Negates the nested condition."""

ShortcutsAndCondition = TypedDict("ShortcutsAndCondition", {"and": "list[ShortcutsCondition]"}, total=False)
"""True if all nested conditions are true."""

ShortcutsOrCondition = TypedDict("ShortcutsOrCondition", {"or": "list[ShortcutsCondition]"}, total=False)
"""True if any nested condition is true."""

ShortcutsAnyCondition = TypedDict("ShortcutsAnyCondition", {"any": ShortcutsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all shortcuts condition types
ShortcutsCondition = (
    ShortcutsEqCondition
    | ShortcutsNeqCondition
    | ShortcutsGtCondition
    | ShortcutsGteCondition
    | ShortcutsLtCondition
    | ShortcutsLteCondition
    | ShortcutsInCondition
    | ShortcutsLikeCondition
    | ShortcutsFuzzyCondition
    | ShortcutsKeywordCondition
    | ShortcutsContainsCondition
    | ShortcutsNotCondition
    | ShortcutsAndCondition
    | ShortcutsOrCondition
    | ShortcutsAnyCondition
)


class ShortcutsSearchQuery(TypedDict, total=False):
    """Search query for shortcuts entity."""
    filter: ShortcutsCondition
    sort: list[ShortcutsSortFilter]


# ===== TRIGGERS SEARCH TYPES =====

class TriggersSearchFilter(TypedDict, total=False):
    """Available fields for filtering triggers search queries."""
    id: int
    """Trigger ID"""
    name: str | None
    """Trigger name"""
    enabled: bool | None
    """Whether trigger is enabled"""


class TriggersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Trigger ID"""
    name: list[str]
    """Trigger name"""
    enabled: list[bool]
    """Whether trigger is enabled"""


class TriggersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Trigger ID"""
    name: Any
    """Trigger name"""
    enabled: Any
    """Whether trigger is enabled"""


class TriggersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Trigger ID"""
    name: str
    """Trigger name"""
    enabled: str
    """Whether trigger is enabled"""


class TriggersSortFilter(TypedDict, total=False):
    """Available fields for sorting triggers search results."""
    id: AirbyteSortOrder
    """Trigger ID"""
    name: AirbyteSortOrder
    """Trigger name"""
    enabled: AirbyteSortOrder
    """Whether trigger is enabled"""


# Entity-specific condition types for triggers
class TriggersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TriggersSearchFilter


class TriggersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TriggersSearchFilter


class TriggersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TriggersSearchFilter


class TriggersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TriggersSearchFilter


class TriggersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TriggersSearchFilter


class TriggersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TriggersSearchFilter


class TriggersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TriggersStringFilter


class TriggersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TriggersStringFilter


class TriggersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TriggersStringFilter


class TriggersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TriggersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TriggersInCondition = TypedDict("TriggersInCondition", {"in": TriggersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TriggersNotCondition = TypedDict("TriggersNotCondition", {"not": "TriggersCondition"}, total=False)
"""Negates the nested condition."""

TriggersAndCondition = TypedDict("TriggersAndCondition", {"and": "list[TriggersCondition]"}, total=False)
"""True if all nested conditions are true."""

TriggersOrCondition = TypedDict("TriggersOrCondition", {"or": "list[TriggersCondition]"}, total=False)
"""True if any nested condition is true."""

TriggersAnyCondition = TypedDict("TriggersAnyCondition", {"any": TriggersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all triggers condition types
TriggersCondition = (
    TriggersEqCondition
    | TriggersNeqCondition
    | TriggersGtCondition
    | TriggersGteCondition
    | TriggersLtCondition
    | TriggersLteCondition
    | TriggersInCondition
    | TriggersLikeCondition
    | TriggersFuzzyCondition
    | TriggersKeywordCondition
    | TriggersContainsCondition
    | TriggersNotCondition
    | TriggersAndCondition
    | TriggersOrCondition
    | TriggersAnyCondition
)


class TriggersSearchQuery(TypedDict, total=False):
    """Search query for triggers entity."""
    filter: TriggersCondition
    sort: list[TriggersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
