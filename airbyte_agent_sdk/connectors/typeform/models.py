"""
Pydantic models for typeform connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class TypeformAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Personal access token from your Typeform account settings"""

# Replication configuration

class TypeformReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Typeform"""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDT00:00:00Z from which to start replicating response data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class FormThankyouScreensItemProperties(BaseModel):
    """Nested schema for FormThankyouScreensItem.properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    show_button: bool | None | None = Field(default=None)
    share_icons: bool | None | None = Field(default=None)
    button_mode: str | None | None = Field(default=None)
    button_text: str | None | None = Field(default=None)
    redirect_url: str | None | None = Field(default=None)

class FormThankyouScreensItemAttachment(BaseModel):
    """Nested schema for FormThankyouScreensItem.attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    placement: str | None | None = Field(default=None)

class FormThankyouScreensItemLayoutAttachment(BaseModel):
    """Nested schema for FormThankyouScreensItemLayout.attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    href: str | None | None = Field(default=None)
    scale: float | None | None = Field(default=None)

class FormThankyouScreensItemLayoutPropertiesFocalPoint(BaseModel):
    """Nested schema for FormThankyouScreensItemLayoutProperties.focal_point"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    x: float | None | None = Field(default=None)
    y: float | None | None = Field(default=None)

class FormThankyouScreensItemLayoutProperties(BaseModel):
    """Nested schema for FormThankyouScreensItemLayout.properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    brightness: float | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    focal_point: FormThankyouScreensItemLayoutPropertiesFocalPoint | None | None = Field(default=None)

class FormThankyouScreensItemLayout(BaseModel):
    """Nested schema for FormThankyouScreensItem.layout"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    placement: str | None | None = Field(default=None)
    attachment: FormThankyouScreensItemLayoutAttachment | None | None = Field(default=None)
    properties: FormThankyouScreensItemLayoutProperties | None | None = Field(default=None)

class FormThankyouScreensItem(BaseModel):
    """Nested schema for Form.thankyou_screens_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    ref: str | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    properties: FormThankyouScreensItemProperties | None | None = Field(default=None)
    attachment: FormThankyouScreensItemAttachment | None | None = Field(default=None)
    layout: FormThankyouScreensItemLayout | None | None = Field(default=None)

class FormWorkspace(BaseModel):
    """Workspace details where the form belongs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None | None = Field(default=None, description="URL of the workspace")
    """URL of the workspace"""

class FormFieldsItemValidations(BaseModel):
    """Nested schema for FormFieldsItem.validations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    required: bool | None | None = Field(default=None)

class FormFieldsItemLayoutAttachment(BaseModel):
    """Nested schema for FormFieldsItemLayout.attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    href: str | None | None = Field(default=None)
    scale: float | None | None = Field(default=None)

class FormFieldsItemLayoutPropertiesFocalPoint(BaseModel):
    """Nested schema for FormFieldsItemLayoutProperties.focal_point"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    x: float | None | None = Field(default=None)
    y: float | None | None = Field(default=None)

class FormFieldsItemLayoutProperties(BaseModel):
    """Nested schema for FormFieldsItemLayout.properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    brightness: float | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    focal_point: FormFieldsItemLayoutPropertiesFocalPoint | None | None = Field(default=None)

class FormFieldsItemLayout(BaseModel):
    """Nested schema for FormFieldsItem.layout"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    placement: str | None | None = Field(default=None)
    attachment: FormFieldsItemLayoutAttachment | None | None = Field(default=None)
    properties: FormFieldsItemLayoutProperties | None | None = Field(default=None)

class FormFieldsItemPropertiesChoicesItem(BaseModel):
    """Nested schema for FormFieldsItemProperties.choices_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    ref: str | None | None = Field(default=None)
    label: str | None | None = Field(default=None)

class FormFieldsItemProperties(BaseModel):
    """Nested schema for FormFieldsItem.properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    randomize: bool | None | None = Field(default=None)
    allow_multiple_selection: bool | None | None = Field(default=None)
    allow_other_choice: bool | None | None = Field(default=None)
    vertical_alignment: bool | None | None = Field(default=None)
    choices: list[FormFieldsItemPropertiesChoicesItem | None] | None | None = Field(default=None)

class FormFieldsItemAttachment(BaseModel):
    """Nested schema for FormFieldsItem.attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    href: str | None | None = Field(default=None)

class FormFieldsItem(BaseModel):
    """Nested schema for Form.fields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    ref: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    properties: FormFieldsItemProperties | None | None = Field(default=None)
    validations: FormFieldsItemValidations | None | None = Field(default=None)
    attachment: FormFieldsItemAttachment | None | None = Field(default=None)
    layout: FormFieldsItemLayout | None | None = Field(default=None)

class FormLinks(BaseModel):
    """Links to related resources"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display: str | None | None = Field(default=None)

class FormSettingsMetaImage(BaseModel):
    """Nested schema for FormSettingsMeta.image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None | None = Field(default=None)

class FormSettingsMeta(BaseModel):
    """Meta information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_indexing: bool | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    image: FormSettingsMetaImage | None | None = Field(default=None)

class FormSettingsCapabilitiesE2eEncryption(BaseModel):
    """Nested schema for FormSettingsCapabilities.e2e_encryption"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None | None = Field(default=None)
    modifiable: bool | None | None = Field(default=None)

class FormSettingsCapabilities(BaseModel):
    """Nested schema for FormSettings.capabilities"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    e2e_encryption: FormSettingsCapabilitiesE2eEncryption | None | None = Field(default=None)

class FormSettingsCuiSettings(BaseModel):
    """Nested schema for FormSettings.cui_settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar: str | None | None = Field(default=None)
    is_typing_emulation_disabled: bool | None | None = Field(default=None)
    typing_emulation_speed: str | None | None = Field(default=None)

class FormSettingsNotificationsSelf(BaseModel):
    """Nested schema for FormSettingsNotifications.self"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None | None = Field(default=None)
    recipients: list[str | None] | None | None = Field(default=None)
    subject: str | None | None = Field(default=None)
    message: str | None | None = Field(default=None)
    reply_to: str | None | None = Field(default=None)

class FormSettingsNotificationsRespondent(BaseModel):
    """Nested schema for FormSettingsNotifications.respondent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None | None = Field(default=None)
    recipients: list[str | None] | None | None = Field(default=None)
    subject: str | None | None = Field(default=None)
    message: str | None | None = Field(default=None)
    reply_to: str | None | None = Field(default=None)

class FormSettingsNotifications(BaseModel):
    """Nested schema for FormSettings.notifications"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: FormSettingsNotificationsSelf | None | None = Field(default=None)
    respondent: FormSettingsNotificationsRespondent | None | None = Field(default=None)

class FormSettings(BaseModel):
    """Settings and configurations for the form"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    language: str | None | None = Field(default=None, description="Language of the form")
    """Language of the form"""
    progress_bar: str | None | None = Field(default=None, description="Progress bar settings")
    """Progress bar settings"""
    meta: FormSettingsMeta | None | None = Field(default=None, description="Meta information")
    """Meta information"""
    hide_navigation: bool | None | None = Field(default=None)
    is_public: bool | None | None = Field(default=None)
    is_trial: bool | None | None = Field(default=None)
    show_progress_bar: bool | None | None = Field(default=None)
    show_typeform_branding: bool | None | None = Field(default=None)
    are_uploads_public: bool | None | None = Field(default=None)
    show_time_to_complete: bool | None | None = Field(default=None)
    redirect_after_submit_url: str | None | None = Field(default=None)
    google_analytics: str | None | None = Field(default=None)
    facebook_pixel: str | None | None = Field(default=None)
    google_tag_manager: str | None | None = Field(default=None)
    capabilities: FormSettingsCapabilities | None | None = Field(default=None)
    notifications: FormSettingsNotifications | None | None = Field(default=None)
    cui_settings: FormSettingsCuiSettings | None | None = Field(default=None)

class FormTheme(BaseModel):
    """Theme settings for the form"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None | None = Field(default=None, description="URL of the theme")
    """URL of the theme"""

class FormLogicItemActionsItemConditionVarsItem(BaseModel):
    """Nested schema for FormLogicItemActionsItemCondition.vars_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class FormLogicItemActionsItemCondition(BaseModel):
    """Nested schema for FormLogicItemActionsItem.condition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    op: str | None | None = Field(default=None)
    vars: list[FormLogicItemActionsItemConditionVarsItem | None] | None | None = Field(default=None)

class FormLogicItemActionsItemDetailsTo(BaseModel):
    """Nested schema for FormLogicItemActionsItemDetails.to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class FormLogicItemActionsItemDetailsValue(BaseModel):
    """Nested schema for FormLogicItemActionsItemDetails.value"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class FormLogicItemActionsItemDetailsTarget(BaseModel):
    """Nested schema for FormLogicItemActionsItemDetails.target"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class FormLogicItemActionsItemDetails(BaseModel):
    """Nested schema for FormLogicItemActionsItem.details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: FormLogicItemActionsItemDetailsTo | None | None = Field(default=None)
    target: FormLogicItemActionsItemDetailsTarget | None | None = Field(default=None)
    value: FormLogicItemActionsItemDetailsValue | None | None = Field(default=None)

class FormLogicItemActionsItem(BaseModel):
    """Nested schema for FormLogicItem.actions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    action: str | None | None = Field(default=None)
    details: FormLogicItemActionsItemDetails | None | None = Field(default=None)
    condition: FormLogicItemActionsItemCondition | None | None = Field(default=None)

class FormLogicItem(BaseModel):
    """Nested schema for Form.logic_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    ref: str | None | None = Field(default=None)
    actions: list[FormLogicItemActionsItem | None] | None | None = Field(default=None)

class FormSelf(BaseModel):
    """Self-referential link to this form"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None | None = Field(default=None, description="URL of this form resource")
    """URL of this form resource"""

class FormWelcomeScreensItemProperties(BaseModel):
    """Nested schema for FormWelcomeScreensItem.properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    show_button: bool | None | None = Field(default=None)
    share_icons: bool | None | None = Field(default=None)
    button_mode: str | None | None = Field(default=None)
    button_text: str | None | None = Field(default=None)
    redirect_url: str | None | None = Field(default=None)

class FormWelcomeScreensItemAttachment(BaseModel):
    """Nested schema for FormWelcomeScreensItem.attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    placement: str | None | None = Field(default=None)

class FormWelcomeScreensItemLayoutAttachment(BaseModel):
    """Nested schema for FormWelcomeScreensItemLayout.attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    href: str | None | None = Field(default=None)
    scale: float | None | None = Field(default=None)

class FormWelcomeScreensItemLayoutPropertiesFocalPoint(BaseModel):
    """Nested schema for FormWelcomeScreensItemLayoutProperties.focal_point"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    x: float | None | None = Field(default=None)
    y: float | None | None = Field(default=None)

class FormWelcomeScreensItemLayoutProperties(BaseModel):
    """Nested schema for FormWelcomeScreensItemLayout.properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    brightness: float | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    focal_point: FormWelcomeScreensItemLayoutPropertiesFocalPoint | None | None = Field(default=None)

class FormWelcomeScreensItemLayout(BaseModel):
    """Nested schema for FormWelcomeScreensItem.layout"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    placement: str | None | None = Field(default=None)
    attachment: FormWelcomeScreensItemLayoutAttachment | None | None = Field(default=None)
    properties: FormWelcomeScreensItemLayoutProperties | None | None = Field(default=None)

class FormWelcomeScreensItem(BaseModel):
    """Nested schema for Form.welcome_screens_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    ref: str | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    properties: FormWelcomeScreensItemProperties | None | None = Field(default=None)
    attachment: FormWelcomeScreensItemAttachment | None | None = Field(default=None)
    layout: FormWelcomeScreensItemLayout | None | None = Field(default=None)

class Form(BaseModel):
    """A Typeform form with its fields, settings, and logic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    title: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    last_updated_at: str | None = Field(default=None)
    published_at: str | None = Field(default=None)
    workspace: FormWorkspace | None = Field(default=None)
    theme: FormTheme | None = Field(default=None)
    settings: FormSettings | None = Field(default=None)
    welcome_screens: list[FormWelcomeScreensItem | None] | None = Field(default=None)
    thankyou_screens: list[FormThankyouScreensItem | None] | None = Field(default=None)
    logic: list[FormLogicItem | None] | None = Field(default=None)
    fields: list[FormFieldsItem | None] | None = Field(default=None)
    self: FormSelf | None = Field(default=None)
    links: FormLinks | None = Field(default=None, alias="_links")

class FormsList(BaseModel):
    """Paginated list of forms"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)
    items: list[Form] | None = Field(default=None)

class ResponseAnswersItemPayment(BaseModel):
    """Nested schema for ResponseAnswersItem.payment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    last4: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    success: bool | None | None = Field(default=None)

class ResponseAnswersItemField(BaseModel):
    """Nested schema for ResponseAnswersItem.field"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    ref: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")

class ResponseAnswersItemChoice(BaseModel):
    """Nested schema for ResponseAnswersItem.choice"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    label: str | None | None = Field(default=None)

class ResponseAnswersItemChoices(BaseModel):
    """Nested schema for ResponseAnswersItem.choices"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ids: list[str | None] | None | None = Field(default=None)
    labels: list[str | None] | None | None = Field(default=None)

class ResponseAnswersItem(BaseModel):
    """Nested schema for Response.answers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field: ResponseAnswersItemField | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    text: str | None | None = Field(default=None)
    choice: ResponseAnswersItemChoice | None | None = Field(default=None)
    choices: ResponseAnswersItemChoices | None | None = Field(default=None)
    number: float | None | None = Field(default=None)
    date: str | None | None = Field(default=None)
    email: str | None | None = Field(default=None)
    phone_number: str | None | None = Field(default=None)
    boolean: bool | None | None = Field(default=None)
    file_url: str | None | None = Field(default=None)
    url: str | None | None = Field(default=None)
    payment: ResponseAnswersItemPayment | None | None = Field(default=None)

class ResponseVariablesItem(BaseModel):
    """Nested schema for Response.variables_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    text: str | None | None = Field(default=None)
    number: float | None | None = Field(default=None)

class ResponseCalculated(BaseModel):
    """Calculated data related to the response"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    score: int | None | None = Field(default=None)

class ResponseMetadata(BaseModel):
    """Metadata related to the response"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_agent: str | None | None = Field(default=None)
    platform: str | None | None = Field(default=None)
    referer: str | None | None = Field(default=None)
    network_id: str | None | None = Field(default=None)

class Response(BaseModel):
    """A single form response/submission"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    response_id: str | None = Field(default=None)
    response_type: str | None = Field(default=None)
    landed_at: str | None = Field(default=None)
    landing_id: str | None = Field(default=None)
    submitted_at: str | None = Field(default=None)
    token: str | None = Field(default=None)
    form_id: str | None = Field(default=None)
    metadata: ResponseMetadata | None = Field(default=None)
    variables: list[ResponseVariablesItem | None] | None = Field(default=None)
    hidden: dict[str, Any] | None = Field(default=None)
    calculated: ResponseCalculated | None = Field(default=None)
    answers: list[ResponseAnswersItem | None] | None = Field(default=None)

class ResponsesList(BaseModel):
    """Paginated list of responses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)
    items: list[Response] | None = Field(default=None)

class Webhook(BaseModel):
    """A webhook configured for a form"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    form_id: str | None = Field(default=None)
    tag: str | None = Field(default=None)
    url: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    verify_ssl: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class WebhooksList(BaseModel):
    """List of webhooks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: list[Webhook] | None = Field(default=None)

class WorkspaceForms(BaseModel):
    """Information about forms in the workspace"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    count: float | None | None = Field(default=None, description="Total number of forms in this workspace")
    """Total number of forms in this workspace"""
    href: str | None | None = Field(default=None, description="URL to retrieve the forms")
    """URL to retrieve the forms"""

class WorkspaceSelf(BaseModel):
    """Self-referential link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    href: str | None | None = Field(default=None, description="URL to this workspace")
    """URL to this workspace"""

class Workspace(BaseModel):
    """A workspace containing forms"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    default: bool | None = Field(default=None)
    shared: bool | None = Field(default=None)
    forms: WorkspaceForms | None = Field(default=None)
    self: WorkspaceSelf | None = Field(default=None)

class WorkspacesList(BaseModel):
    """Paginated list of workspaces"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)
    items: list[Workspace] | None = Field(default=None)

class Image(BaseModel):
    """An image in the account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    file_name: str | None = Field(default=None)
    src: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    media_type: str | None = Field(default=None)
    avg_color: str | None = Field(default=None)
    has_alpha: bool | None = Field(default=None)
    upload_source: str | None = Field(default=None)

class ThemeScreens(BaseModel):
    """Screen display settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    alignment: str | None | None = Field(default=None)
    font_size: str | None | None = Field(default=None)

class ThemeFields(BaseModel):
    """Field display settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    alignment: str | None | None = Field(default=None)
    font_size: str | None | None = Field(default=None)

class ThemeColors(BaseModel):
    """Color settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    answer: str | None | None = Field(default=None, description="Color of answer text")
    """Color of answer text"""
    background: str | None | None = Field(default=None, description="Background color")
    """Background color"""
    button: str | None | None = Field(default=None, description="Color of buttons")
    """Color of buttons"""
    question: str | None | None = Field(default=None, description="Color of question text")
    """Color of question text"""

class ThemeBackground(BaseModel):
    """Background settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    brightness: float | None | None = Field(default=None)
    href: str | None | None = Field(default=None)
    layout: str | None | None = Field(default=None)

class Theme(BaseModel):
    """A theme used for styling forms"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    visibility: str | None = Field(default=None)
    font: str | None = Field(default=None)
    has_transparent_button: bool | None = Field(default=None)
    rounded_corners: str | None = Field(default=None)
    colors: ThemeColors | None = Field(default=None)
    background: ThemeBackground | None = Field(default=None)
    fields: ThemeFields | None = Field(default=None)
    screens: ThemeScreens | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class ThemesList(BaseModel):
    """Paginated list of themes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)
    items: list[Theme] | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class FormsListResultMeta(BaseModel):
    """Metadata for forms.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)

class ResponsesListResultMeta(BaseModel):
    """Metadata for responses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)

class WorkspacesListResultMeta(BaseModel):
    """Metadata for workspaces.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)

class ThemesListResultMeta(BaseModel):
    """Metadata for themes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_items: int | None = Field(default=None)
    page_count: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class TypeformCheckResult(BaseModel):
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


class TypeformExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class TypeformExecuteResultWithMeta(TypeformExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class FormsSearchData(BaseModel):
    """Search result data for forms entity."""
    model_config = ConfigDict(extra="allow")

    links: dict[str, Any] | None = None
    """Links to related resources"""
    created_at: str | None = None
    """Date and time when the form was created"""
    fields: list[Any] | None = None
    """List of fields within the form"""
    id: str | None = None
    """Unique identifier of the form"""
    last_updated_at: str | None = None
    """Date and time when the form was last updated"""
    logic: list[Any] | None = None
    """Logic rules or conditions applied to the form fields"""
    published_at: str | None = None
    """Date and time when the form was published"""
    settings: dict[str, Any] | None = None
    """Settings and configurations for the form"""
    thankyou_screens: list[Any] | None = None
    """Thank you screen configurations"""
    theme: dict[str, Any] | None = None
    """Theme settings for the form"""
    title: str | None = None
    """Title of the form"""
    type_: str | None = None
    """Type of the form"""
    welcome_screens: list[Any] | None = None
    """Welcome screen configurations"""
    workspace: dict[str, Any] | None = None
    """Workspace details where the form belongs"""


class ResponsesSearchData(BaseModel):
    """Search result data for responses entity."""
    model_config = ConfigDict(extra="allow")

    answers: list[Any] | None = None
    """Response data for each question in the form"""
    calculated: dict[str, Any] | None = None
    """Calculated data related to the response"""
    form_id: str | None = None
    """ID of the form"""
    hidden: dict[str, Any] | None = None
    """Hidden fields in the response"""
    landed_at: str | None = None
    """Timestamp when the respondent landed on the form"""
    landing_id: str | None = None
    """ID of the landing page"""
    metadata: dict[str, Any] | None = None
    """Metadata related to the response"""
    response_id: str | None = None
    """ID of the response"""
    response_type: str | None = None
    """Type of the response"""
    submitted_at: str | None = None
    """Timestamp when the response was submitted"""
    token: str | None = None
    """Token associated with the response"""
    variables: list[Any] | None = None
    """Variables associated with the response"""


class WebhooksSearchData(BaseModel):
    """Search result data for webhooks entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Timestamp when the webhook was created"""
    enabled: bool | None = None
    """Whether the webhook is currently enabled"""
    form_id: str | None = None
    """ID of the form associated with the webhook"""
    id: str | None = None
    """Unique identifier of the webhook"""
    tag: str | None = None
    """Tag to categorize or label the webhook"""
    updated_at: str | None = None
    """Timestamp when the webhook was last updated"""
    url: str | None = None
    """URL where webhook data is sent"""
    verify_ssl: bool | None = None
    """Whether SSL verification is enforced"""


class WorkspacesSearchData(BaseModel):
    """Search result data for workspaces entity."""
    model_config = ConfigDict(extra="allow")

    account_id: str | None = None
    """Account ID associated with the workspace"""
    default: bool | None = None
    """Whether this is the default workspace"""
    forms: dict[str, Any] | None = None
    """Information about forms in the workspace"""
    id: str | None = None
    """Unique identifier of the workspace"""
    name: str | None = None
    """Name of the workspace"""
    self: dict[str, Any] | None = None
    """Self-referential link"""
    shared: bool | None = None
    """Whether this workspace is shared"""


class ImagesSearchData(BaseModel):
    """Search result data for images entity."""
    model_config = ConfigDict(extra="allow")

    avg_color: str | None = None
    """Average color of the image"""
    file_name: str | None = None
    """Name of the image file"""
    has_alpha: bool | None = None
    """Whether the image has an alpha channel"""
    height: int | None = None
    """Height of the image in pixels"""
    id: str | None = None
    """Unique identifier of the image"""
    media_type: str | None = None
    """MIME type of the image"""
    src: str | None = None
    """URL to access the image"""
    width: int | None = None
    """Width of the image in pixels"""


class ThemesSearchData(BaseModel):
    """Search result data for themes entity."""
    model_config = ConfigDict(extra="allow")

    background: dict[str, Any] | None = None
    """Background settings for the theme"""
    colors: dict[str, Any] | None = None
    """Color settings"""
    created_at: str | None = None
    """Timestamp when the theme was created"""
    fields: dict[str, Any] | None = None
    """Field display settings"""
    font: str | None = None
    """Font used in the theme"""
    has_transparent_button: bool | None = None
    """Whether the theme has a transparent button"""
    id: str | None = None
    """Unique identifier of the theme"""
    name: str | None = None
    """Name of the theme"""
    rounded_corners: str | None = None
    """Rounded corners setting"""
    screens: dict[str, Any] | None = None
    """Screen display settings"""
    updated_at: str | None = None
    """Timestamp when the theme was last updated"""
    visibility: str | None = None
    """Visibility setting of the theme"""


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

FormsSearchResult = AirbyteSearchResult[FormsSearchData]
"""Search result type for forms entity."""

ResponsesSearchResult = AirbyteSearchResult[ResponsesSearchData]
"""Search result type for responses entity."""

WebhooksSearchResult = AirbyteSearchResult[WebhooksSearchData]
"""Search result type for webhooks entity."""

WorkspacesSearchResult = AirbyteSearchResult[WorkspacesSearchData]
"""Search result type for workspaces entity."""

ImagesSearchResult = AirbyteSearchResult[ImagesSearchData]
"""Search result type for images entity."""

ThemesSearchResult = AirbyteSearchResult[ThemesSearchData]
"""Search result type for themes entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

FormsListResult = TypeformExecuteResultWithMeta[list[Form], FormsListResultMeta]
"""Result type for forms.list operation with data and metadata."""

ResponsesListResult = TypeformExecuteResultWithMeta[list[Response], ResponsesListResultMeta]
"""Result type for responses.list operation with data and metadata."""

WebhooksListResult = TypeformExecuteResult[list[Webhook]]
"""Result type for webhooks.list operation."""

WorkspacesListResult = TypeformExecuteResultWithMeta[list[Workspace], WorkspacesListResultMeta]
"""Result type for workspaces.list operation with data and metadata."""

ImagesListResult = TypeformExecuteResult[list[Image]]
"""Result type for images.list operation."""

ThemesListResult = TypeformExecuteResultWithMeta[list[Theme], ThemesListResultMeta]
"""Result type for themes.list operation with data and metadata."""

