"""
Auto-generated cassette tests for Stripe connector.

These tests are generated from cassette YAML files and test the connector
against recorded API responses.
"""

import pytest
from unittest.mock import AsyncMock, patch

from airbyte_ai_stripe import StripeConnector



@pytest.mark.asyncio
async def test_customers_get():
    """Captured from real API call on 2025-11-12"""
    mock_response = {'id': 'cus_TLTWhRfiG8of9k', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762033365, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'UZKYMUN3', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}

    connector = StripeConnector.create(secrets={"token": "test_key"})

    with patch(
        "airbyte_ai_stripe._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.customers.get(id="cus_TLTWhRfiG8of9k")

    assert result == mock_response


@pytest.mark.asyncio
async def test_customers_get_id_cus_TLTWhRfiG8of9k():
    """Captured from real API call on 2025-11-12"""
    mock_response = {'id': 'cus_TLTWhRfiG8of9k', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762033365, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'UZKYMUN3', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}

    connector = StripeConnector.create(secrets={"token": "test_key"})

    with patch(
        "airbyte_ai_stripe._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.customers.get(id="cus_TLTWhRfiG8of9k")

    assert result == mock_response


@pytest.mark.asyncio
async def test_customers_list():
    """Captured from real API call on 2025-11-12"""
    mock_response = {'object': 'list', 'data': [{'id': 'cus_TLTWhRfiG8of9k', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762033365, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'UZKYMUN3', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTVwJvuObOrtK', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762033299, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'ZHUVFJAC', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTT3gfw2YwfyP', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762033201, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': '6CZQDKZY', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTRlx4dVhasN9', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762033078, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'U7GQ7VCD', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTGVKeVif0P18', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762032428, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'I41JFXKO', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTG8CZFAzndUN', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762032399, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': '6FN6WYRE', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTFJEMn4T03Zw', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762032349, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'AYNMADDF', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TLTERaYeIHoBZx', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1762032308, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'P5KTVLL7', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TKjNhE3irtRfAk', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1761861703, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': None, 'discount': None, 'email': 'sdk-test@example.com', 'invoice_prefix': 'FJAKT1Z0', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'SDK Test', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}, {'id': 'cus_TK1WdjUBIHdNfi', 'object': 'customer', 'address': None, 'balance': 0, 'created': 1761698591, 'currency': None, 'default_currency': None, 'default_source': None, 'delinquent': False, 'description': 'Created via manual logging test', 'discount': None, 'email': 'test@example.com', 'invoice_prefix': '4AUSBTGQ', 'invoice_settings': {'custom_fields': None, 'default_payment_method': None, 'footer': None, 'rendering_options': None}, 'livemode': False, 'metadata': {}, 'name': 'Test Customer', 'next_invoice_sequence': 1, 'phone': None, 'preferred_locales': [], 'shipping': None, 'tax_exempt': 'none', 'test_clock': None}], 'has_more': True, 'url': '/v1/customers'}

    connector = StripeConnector.create(secrets={"token": "test_key"})

    with patch(
        "airbyte_ai_stripe._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.customers.list()

    assert result == mock_response

