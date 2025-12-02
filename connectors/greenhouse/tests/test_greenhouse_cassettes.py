"""
Auto-generated cassette tests for Greenhouse connector.

These tests are generated from cassette YAML files and test the connector
against recorded API responses.
"""

import pytest
from unittest.mock import AsyncMock, patch

from airbyte_ai_greenhouse import GreenhouseConnector



@pytest.mark.asyncio
async def test_applications_get_id_169024258003():
    """Captured from real API call on 2025-11-19"""
    mock_response = {'id': 169024258003, 'candidate_id': 160875821003, 'prospect': False, 'applied_at': '2025-11-11T14:40:15.330Z', 'rejected_at': None, 'last_activity_at': '2025-11-11T14:51:30.571Z', 'location': None, 'attachments': [], 'source': {'id': 4000067003, 'public_name': 'HRMARKET'}, 'credited_to': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'recruiter': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'coordinator': {'id': 5442644003, 'first_name': 'Greenhouse', 'last_name': 'Admin', 'name': 'Greenhouse Admin', 'employee_id': None}, 'rejection_reason': None, 'rejection_details': None, 'jobs': [{'id': 5677248003, 'name': 'Manager'}], 'job_post_id': None, 'status': 'active', 'current_stage': {'id': 15772217003, 'name': 'Phone Interview'}, 'answers': [], 'prospective_department': None, 'prospective_office': None, 'prospect_detail': {'prospect_pool': None, 'prospect_stage': None, 'prospect_owner': None}, 'custom_fields': {'test_application_2': None}, 'keyed_custom_fields': {'test_application_2': None}}

    connector = GreenhouseConnector.create(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_greenhouse._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.applications.get(id="169024258003")

    assert result == mock_response


@pytest.mark.asyncio
async def test_applications_list():
    """Captured from real API call on 2025-11-19"""
    mock_response = [{'id': 169024258003, 'candidate_id': 160875821003, 'prospect': False, 'applied_at': '2025-11-11T14:40:15.330Z', 'rejected_at': None, 'last_activity_at': '2025-11-11T14:51:30.571Z', 'location': None, 'attachments': [], 'source': {'id': 4000067003, 'public_name': 'HRMARKET'}, 'credited_to': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'recruiter': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'coordinator': {'id': 5442644003, 'first_name': 'Greenhouse', 'last_name': 'Admin', 'name': 'Greenhouse Admin', 'employee_id': None}, 'rejection_reason': None, 'rejection_details': None, 'jobs': [{'id': 5677248003, 'name': 'Manager'}], 'job_post_id': None, 'status': 'active', 'current_stage': {'id': 15772217003, 'name': 'Phone Interview'}, 'answers': [], 'prospective_department': None, 'prospective_office': None, 'prospect_detail': {'prospect_pool': None, 'prospect_stage': None, 'prospect_owner': None}, 'custom_fields': {'test_application_2': None}, 'keyed_custom_fields': {'test_application_2': None}}, {'id': 169026089003, 'candidate_id': 160877634003, 'prospect': True, 'applied_at': '2025-11-11T14:57:41.860Z', 'rejected_at': None, 'last_activity_at': '2025-11-11T14:57:41.921Z', 'location': None, 'attachments': [], 'source': {'id': 4000067003, 'public_name': 'HRMARKET'}, 'credited_to': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'recruiter': None, 'coordinator': None, 'rejection_reason': None, 'rejection_details': None, 'jobs': [{'id': 5677248003, 'name': 'Manager'}], 'job_post_id': None, 'status': 'active', 'current_stage': None, 'answers': [], 'prospective_department': {'id': 4118362003, 'name': 'Accounting', 'parent_id': None, 'parent_department_external_id': None, 'child_ids': [], 'child_department_external_ids': [], 'external_id': None}, 'prospective_office': {'id': 4091946003, 'name': 'Berlin', 'location': {'name': None}, 'primary_contact_user_id': None, 'parent_id': None, 'parent_office_external_id': None, 'child_ids': [], 'child_office_external_ids': [], 'external_id': None}, 'prospect_detail': {'prospect_pool': {'id': 4034741003, 'name': 'Cold Outreach'}, 'prospect_stage': {'id': 4110893003, 'name': 'In Discussion'}, 'prospect_owner': {'id': 5442645003, 'name': 'Integration Test'}}, 'custom_fields': {'test_application_2': None}, 'keyed_custom_fields': {'test_application_2': None}}]

    connector = GreenhouseConnector.create(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_greenhouse._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.applications.list(per_page=2)

    assert result == mock_response


@pytest.mark.asyncio
async def test_candidates_get_id_160875821003():
    """Captured from real API call on 2025-11-19"""
    mock_response = {'id': 160875821003, 'first_name': 'John', 'last_name': 'Snow', 'company': 'Fivetran', 'title': 'Manager', 'created_at': '2025-11-11T14:40:15.301Z', 'updated_at': '2025-11-11T14:51:30.571Z', 'last_activity': '2025-11-11T14:51:30.571Z', 'is_private': False, 'photo_url': None, 'attachments': [], 'application_ids': [169024258003], 'phone_numbers': [{'value': '23532452345235', 'type': 'home'}], 'addresses': [], 'email_addresses': [{'value': 'test@gmail.io', 'type': 'personal'}], 'website_addresses': [], 'social_media_addresses': [], 'recruiter': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'coordinator': {'id': 5442644003, 'first_name': 'Greenhouse', 'last_name': 'Admin', 'name': 'Greenhouse Admin', 'employee_id': None}, 'can_email': True, 'tags': [], 'applications': [{'id': 169024258003, 'candidate_id': 160875821003, 'prospect': False, 'applied_at': '2025-11-11T14:40:15.330Z', 'rejected_at': None, 'last_activity_at': '2025-11-11T14:51:30.571Z', 'location': None, 'attachments': [], 'source': {'id': 4000067003, 'public_name': 'HRMARKET'}, 'credited_to': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'recruiter': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'coordinator': {'id': 5442644003, 'first_name': 'Greenhouse', 'last_name': 'Admin', 'name': 'Greenhouse Admin', 'employee_id': None}, 'rejection_reason': None, 'rejection_details': None, 'jobs': [{'id': 5677248003, 'name': 'Manager'}], 'job_post_id': None, 'status': 'active', 'current_stage': {'id': 15772217003, 'name': 'Phone Interview'}, 'answers': [], 'prospective_department': None, 'prospective_office': None, 'prospect_detail': {'prospect_pool': None, 'prospect_stage': None, 'prospect_owner': None}, 'custom_fields': {'test_application_2': None}, 'keyed_custom_fields': {'test_application_2': None}}], 'educations': [], 'employments': [], 'linked_user_ids': [], 'custom_fields': {'work_authorization': None}, 'keyed_custom_fields': {'work_authorization': None}}

    connector = GreenhouseConnector.create(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_greenhouse._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.candidates.get(id="160875821003")

    assert result == mock_response


@pytest.mark.asyncio
async def test_candidates_list():
    """Captured from real API call on 2025-11-19"""
    mock_response = [{'id': 160875821003, 'first_name': 'John', 'last_name': 'Snow', 'company': 'Fivetran', 'title': 'Manager', 'created_at': '2025-11-11T14:40:15.301Z', 'updated_at': '2025-11-11T14:51:30.571Z', 'last_activity': '2025-11-11T14:51:30.571Z', 'is_private': False, 'photo_url': None, 'attachments': [], 'application_ids': [169024258003], 'phone_numbers': [{'value': '23532452345235', 'type': 'home'}], 'addresses': [], 'email_addresses': [{'value': 'test@gmail.io', 'type': 'personal'}], 'website_addresses': [], 'social_media_addresses': [], 'recruiter': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'coordinator': {'id': 5442644003, 'first_name': 'Greenhouse', 'last_name': 'Admin', 'name': 'Greenhouse Admin', 'employee_id': None}, 'can_email': True, 'tags': [], 'applications': [{'id': 169024258003, 'candidate_id': 160875821003, 'prospect': False, 'applied_at': '2025-11-11T14:40:15.330Z', 'rejected_at': None, 'last_activity_at': '2025-11-11T14:51:30.571Z', 'location': None, 'attachments': [], 'source': {'id': 4000067003, 'public_name': 'HRMARKET'}, 'credited_to': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'recruiter': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'coordinator': {'id': 5442644003, 'first_name': 'Greenhouse', 'last_name': 'Admin', 'name': 'Greenhouse Admin', 'employee_id': None}, 'rejection_reason': None, 'rejection_details': None, 'jobs': [{'id': 5677248003, 'name': 'Manager'}], 'job_post_id': None, 'status': 'active', 'current_stage': {'id': 15772217003, 'name': 'Phone Interview'}, 'answers': [], 'prospective_department': None, 'prospective_office': None, 'prospect_detail': {'prospect_pool': None, 'prospect_stage': None, 'prospect_owner': None}, 'custom_fields': {'test_application_2': None}, 'keyed_custom_fields': {'test_application_2': None}}], 'educations': [], 'employments': [], 'linked_user_ids': [], 'custom_fields': {'work_authorization': None}, 'keyed_custom_fields': {'work_authorization': None}}, {'id': 160877634003, 'first_name': 'Taras', 'last_name': 'Shevchenko', 'company': None, 'title': 'manager', 'created_at': '2025-11-11T14:57:41.833Z', 'updated_at': '2025-11-11T14:57:41.922Z', 'last_activity': '2025-11-11T14:57:41.921Z', 'is_private': False, 'photo_url': None, 'attachments': [], 'application_ids': [169026089003], 'phone_numbers': [], 'addresses': [], 'email_addresses': [{'value': 'gl_danylo.jablonski@airbyte.io', 'type': 'personal'}], 'website_addresses': [], 'social_media_addresses': [], 'recruiter': None, 'coordinator': None, 'can_email': True, 'tags': [], 'applications': [{'id': 169026089003, 'candidate_id': 160877634003, 'prospect': True, 'applied_at': '2025-11-11T14:57:41.860Z', 'rejected_at': None, 'last_activity_at': '2025-11-11T14:57:41.921Z', 'location': None, 'attachments': [], 'source': {'id': 4000067003, 'public_name': 'HRMARKET'}, 'credited_to': {'id': 5442645003, 'first_name': 'Integration', 'last_name': 'Test', 'name': 'Integration Test', 'employee_id': None}, 'recruiter': None, 'coordinator': None, 'rejection_reason': None, 'rejection_details': None, 'jobs': [{'id': 5677248003, 'name': 'Manager'}], 'job_post_id': None, 'status': 'active', 'current_stage': None, 'answers': [], 'prospective_department': {'id': 4118362003, 'name': 'Accounting', 'parent_id': None, 'parent_department_external_id': None, 'child_ids': [], 'child_department_external_ids': [], 'external_id': None}, 'prospective_office': {'id': 4091946003, 'name': 'Berlin', 'location': {'name': None}, 'primary_contact_user_id': None, 'parent_id': None, 'parent_office_external_id': None, 'child_ids': [], 'child_office_external_ids': [], 'external_id': None}, 'prospect_detail': {'prospect_pool': {'id': 4034741003, 'name': 'Cold Outreach'}, 'prospect_stage': {'id': 4110893003, 'name': 'In Discussion'}, 'prospect_owner': {'id': 5442645003, 'name': 'Integration Test'}}, 'custom_fields': {'test_application_2': None}, 'keyed_custom_fields': {'test_application_2': None}}], 'educations': [], 'employments': [], 'linked_user_ids': [], 'custom_fields': {'work_authorization': None}, 'keyed_custom_fields': {'work_authorization': None}}]

    connector = GreenhouseConnector.create(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_greenhouse._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.candidates.list(per_page=2)

    assert result == mock_response


@pytest.mark.asyncio
async def test_jobs_get_id_5254492003():
    """Captured from real API call on 2025-11-19"""
    mock_response = {'id': 5254492003, 'name': 'Sample Job 1', 'requisition_id': None, 'notes': None, 'confidential': False, 'is_template': None, 'copied_from_id': None, 'status': 'open', 'created_at': '2025-08-15T00:08:02.931Z', 'opened_at': '2025-08-15T00:08:02.936Z', 'closed_at': None, 'updated_at': '2025-08-15T00:08:02.931Z', 'departments': [None], 'offices': [], 'hiring_team': {'hiring_managers': [], 'recruiters': [], 'coordinators': [], 'sourcers': []}, 'openings': [{'id': 6420285003, 'opening_id': '1 - 1', 'status': 'open', 'opened_at': '2025-08-15T00:00:00.000Z', 'closed_at': None, 'application_id': None, 'close_reason': None}], 'custom_fields': {'employment_type': None, 'reason_for_hire': None}, 'keyed_custom_fields': {'employment_type': None, 'reason_for_hire': None}}

    connector = GreenhouseConnector.create(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_greenhouse._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.jobs.get(id="5254492003")

    assert result == mock_response


@pytest.mark.asyncio
async def test_jobs_list():
    """Captured from real API call on 2025-11-19"""
    mock_response = [{'id': 5254492003, 'name': 'Sample Job 1', 'requisition_id': None, 'notes': None, 'confidential': False, 'is_template': None, 'copied_from_id': None, 'status': 'open', 'created_at': '2025-08-15T00:08:02.931Z', 'opened_at': '2025-08-15T00:08:02.936Z', 'closed_at': None, 'updated_at': '2025-08-15T00:08:02.931Z', 'departments': [None], 'offices': [], 'hiring_team': {'hiring_managers': [], 'recruiters': [], 'coordinators': [], 'sourcers': []}, 'openings': [{'id': 6420285003, 'opening_id': '1 - 1', 'status': 'open', 'opened_at': '2025-08-15T00:00:00.000Z', 'closed_at': None, 'application_id': None, 'close_reason': None}], 'custom_fields': {'employment_type': None, 'reason_for_hire': None}, 'keyed_custom_fields': {'employment_type': None, 'reason_for_hire': None}}, {'id': 5677248003, 'name': 'Manager', 'requisition_id': '001', 'notes': None, 'confidential': False, 'is_template': False, 'copied_from_id': None, 'status': 'open', 'created_at': '2025-11-11T14:38:13.438Z', 'opened_at': '2025-11-11T14:38:14.003Z', 'closed_at': None, 'updated_at': '2025-11-11T14:38:14.004Z', 'departments': [{'id': 4118362003, 'name': 'Accounting', 'parent_id': None, 'parent_department_external_id': None, 'child_ids': [], 'child_department_external_ids': [], 'external_id': None}], 'offices': [{'id': 4091946003, 'name': 'Berlin', 'location': {'name': None}, 'primary_contact_user_id': None, 'parent_id': None, 'parent_office_external_id': None, 'child_ids': [], 'child_office_external_ids': [], 'external_id': None}], 'hiring_team': {'hiring_managers': [], 'recruiters': [], 'coordinators': [], 'sourcers': []}, 'openings': [{'id': 6867503003, 'opening_id': None, 'status': 'open', 'opened_at': '2025-11-11T14:38:13.489Z', 'closed_at': None, 'application_id': None, 'close_reason': None}, {'id': 6867504003, 'opening_id': None, 'status': 'open', 'opened_at': '2025-11-11T14:38:13.489Z', 'closed_at': None, 'application_id': None, 'close_reason': None}], 'custom_fields': {'employment_type': 'Full-time', 'reason_for_hire': 'New Headcount'}, 'keyed_custom_fields': {'employment_type': {'name': 'Employment Type', 'type': 'single_select', 'value': 'Full-time'}, 'reason_for_hire': {'name': 'Reason for Hire', 'type': 'single_select', 'value': 'New Headcount'}}}]

    connector = GreenhouseConnector.create(auth_config={"api_key": "test_key"})

    with patch(
        "airbyte_ai_greenhouse._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.jobs.list(per_page=2)

    assert result == mock_response

