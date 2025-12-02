"""
Auto-generated cassette tests for Zendesk-Support connector.

These tests are generated from cassette YAML files and test the connector
against recorded API responses.
"""

import pytest
from unittest.mock import AsyncMock, patch

from airbyte_ai_zendesk_support import ZendeskSupportConnector



@pytest.mark.asyncio
async def test_article_attachments_download():
    """Download article attachment file (first 100 bytes)"""
    import base64
    from unittest.mock import Mock

    # Expected binary data from cassette
    expected_base64 = """/9j/4AAQSkZJRgABAQEBLAEsAAD/4QCyRXhpZgAASUkqAAgAAAADAA4BAgBoAAAAMgAAABoBBQABAAAAmgAAABsBBQABAAAAogAAAAAAAABXZWxjb21lLiBSZXRybyBzdHlsZQ=="""
    expected_data = base64.b64decode(expected_base64)

    # Mock metadata response (first request)
    mock_metadata_response = {'article_attachment': {'id': 14328435003535, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/articles/attachments/14328435003535', 'article_id': 7253394935055, 'display_file_name': 'welcome.jpg', 'file_name': 'welcome.jpg', 'locale': None, 'content_url': 'https://d3v-airbyte.zendesk.com/hc/article_attachments/14328435003535', 'relative_path': '/hc/article_attachments/14328435003535', 'content_type': 'image/jpeg', 'size': 21834, 'inline': False, 'created_at': '2025-11-14T00:37:45Z', 'updated_at': '2025-11-14T00:37:49Z'}}

    # Mock file download response (second request)
    mock_file_response = Mock()
    mock_file_response.status_code = 200
    mock_file_response.headers = {}
    mock_file_response.raise_for_status.return_value = None

    # Mock original_response for aiter_bytes
    mock_original_response = Mock()

    async def mock_aiter_bytes(chunk_size=None):
        yield expected_data

    mock_original_response.aiter_bytes = mock_aiter_bytes
    mock_file_response.original_response = mock_original_response

    # Create mock that returns different values for the two requests
    call_count = 0

    async def mock_request_with_stream(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            # First call: metadata request
            return mock_metadata_response
        else:
            # Second call: file download
            return mock_file_response

    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_key"})

    with patch(
        "airbyte_ai_zendesk_support._vendored.connector_sdk.http_client.HTTPClient.request",
        new=mock_request_with_stream
    ):
        result = await connector.article_attachments.download(article_id="7253394935055", attachment_id="14328435003535")

        # Consume the async iterator to get all chunks
        chunks = []
        async for chunk in result:
            chunks.append(chunk)
        downloaded_data = b''.join(chunks)

    assert downloaded_data == expected_data


@pytest.mark.asyncio
async def test_article_attachments_download_no_range():
    """Download article attachment file with text and no range headers"""
    import base64
    from unittest.mock import Mock

    # Expected binary data from cassette
    expected_base64 = """TGluZSAwMTogVGhpcyBpcyB0ZXN0IGNvbnRlbnQgZm9yIFJhbmdlIGhlYWRlciB0ZXN0aW5nLgpMaW5lIDAyOiBUaGlzIGlzIHRlc3QgY29udGVudCBmb3IgUmFuZ2UgaGVhZGVyIHRlc3RpbmcuCkxpbmUgMDM6IFRoaXMgaXMgdGVzdCBjb250ZW50IGZvciBSYW5nZSBoZWFkZXIgdGVzdGluZy4KTGluZSAwNDogVGhlIGVuZC4K"""
    expected_data = base64.b64decode(expected_base64)

    # Mock metadata response (first request)
    mock_metadata_response = {'article_attachment': {'id': 14437559438991, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/articles/attachments/14437559438991', 'article_id': 7253394952591, 'display_file_name': 'test_200bytes.txt', 'file_name': 'test_200bytes.txt', 'locale': None, 'content_url': 'https://d3v-airbyte.zendesk.com/hc/article_attachments/14437559438991', 'relative_path': '/hc/article_attachments/14437559438991', 'content_type': 'text/plain', 'size': 186, 'inline': False, 'created_at': '2025-11-26T00:43:15Z', 'updated_at': '2025-11-26T00:43:18Z'}}

    # Mock file download response (second request)
    mock_file_response = Mock()
    mock_file_response.status_code = 200
    mock_file_response.headers = {}
    mock_file_response.raise_for_status.return_value = None

    # Mock original_response for aiter_bytes
    mock_original_response = Mock()

    async def mock_aiter_bytes(chunk_size=None):
        yield expected_data

    mock_original_response.aiter_bytes = mock_aiter_bytes
    mock_file_response.original_response = mock_original_response

    # Create mock that returns different values for the two requests
    call_count = 0

    async def mock_request_with_stream(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            # First call: metadata request
            return mock_metadata_response
        else:
            # Second call: file download
            return mock_file_response

    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_key"})

    with patch(
        "airbyte_ai_zendesk_support._vendored.connector_sdk.http_client.HTTPClient.request",
        new=mock_request_with_stream
    ):
        result = await connector.article_attachments.download(article_id="7253394952591", attachment_id="14437559438991")

        # Consume the async iterator to get all chunks
        chunks = []
        async for chunk in result:
            chunks.append(chunk)
        downloaded_data = b''.join(chunks)

    assert downloaded_data == expected_data


@pytest.mark.asyncio
async def test_article_attachments_get():
    """Get article attachment metadata"""
    mock_response = {'article_attachment': {'id': 14328435003535, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/articles/attachments/14328435003535', 'article_id': 7253394935055, 'display_file_name': 'welcome.jpg', 'file_name': 'welcome.jpg', 'locale': None, 'content_url': 'https://d3v-airbyte.zendesk.com/hc/article_attachments/14328435003535', 'relative_path': '/hc/article_attachments/14328435003535', 'content_type': 'image/jpeg', 'size': 21834, 'inline': False, 'created_at': '2025-11-14T00:37:45Z', 'updated_at': '2025-11-14T00:37:49Z'}}

    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_key"})

    with patch(
        "airbyte_ai_zendesk_support._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.article_attachments.get(article_id="7253394935055", attachment_id="14328435003535")

    assert result == mock_response


@pytest.mark.asyncio
async def test_article_attachments_list():
    """Captured from real API call on 2025-12-01"""
    mock_response = {'article_attachments': [{'id': 14437559438991, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/articles/attachments/14437559438991', 'article_id': 7253394952591, 'display_file_name': 'test_200bytes.txt', 'file_name': 'test_200bytes.txt', 'locale': None, 'content_url': 'https://d3v-airbyte.zendesk.com/hc/article_attachments/14437559438991', 'relative_path': '/hc/article_attachments/14437559438991', 'content_type': 'text/plain', 'size': 186, 'inline': False, 'created_at': '2025-11-26T00:43:15Z', 'updated_at': '2025-11-26T00:43:18Z'}]}

    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_key"})

    with patch(
        "airbyte_ai_zendesk_support._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.article_attachments.list(article_id="7253394952591")

    assert result == mock_response


@pytest.mark.asyncio
async def test_articles_get():
    """Captured from real API call on 2025-12-01"""
    mock_response = {'article': {'id': 7253394952591, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253394952591.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253394952591-How-do-I-customize-my-Help-Center', 'author_id': 360786799676, 'comments_disabled': False, 'draft': False, 'promoted': False, 'position': 0, 'vote_sum': 0, 'vote_count': 0, 'section_id': 7253394947215, 'created_at': '2023-06-22T00:32:20Z', 'updated_at': '2025-11-26T00:43:18Z', 'name': 'How do I customize my Help Center?', 'title': 'How do I customize my Help Center?', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2025-11-26T00:43:18Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>You can modify the look and feel of your Help Center by changing colors and fonts. See <a href="https://support.zendesk.com/hc/en-us/articles/206177737" target="_blank">Branding your Help Center</a> to learn how.</p>\n\n<p>You can also change the design of your Help Center. If you\'re comfortable working with page code, you can dig in to the site\'s HTML, CSS, and Javascript to customize your theme. To get started, see <a href="https://support.zendesk.com/hc/en-us/articles/203664326" target="_blank">Customizing the Help Center</a>.</p>', 'user_segment_ids': []}}

    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_key"})

    with patch(
        "airbyte_ai_zendesk_support._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.articles.get(id="7253394952591")

    assert result == mock_response


@pytest.mark.asyncio
async def test_articles_list():
    """Captured from real API call on 2025-12-01"""
    mock_response = {'count': 7, 'next_page': None, 'page': 1, 'page_count': 1, 'per_page': 30, 'previous_page': None, 'articles': [{'id': 12138789487375, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/12138789487375.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/12138789487375-This-is-an-article-with-an-attachment', 'author_id': 360786799676, 'comments_disabled': False, 'draft': True, 'promoted': False, 'position': 0, 'vote_sum': 0, 'vote_count': 0, 'section_id': 7253394947215, 'created_at': '2025-03-11T23:33:57Z', 'updated_at': '2025-03-11T23:33:57Z', 'name': 'This is an article with an attachment!', 'title': 'This is an article with an attachment!', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2025-03-11T23:33:57Z', 'user_segment_id': 7253375826191, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>Here be some text<img src="https://d3v-airbyte.zendesk.com/hc/article_attachments/12138758717583" alt="DALL·E 2024-11-19 10.07.37 - A cartoon-style robot with a metallic, retro-futuristic design, holding a smoking cigar in one hand. The robot has a humorous, relaxed expression, wit (1).webp"></p>', 'user_segment_ids': [7253375826191]}, {'id': 7253394952591, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253394952591.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253394952591-How-do-I-customize-my-Help-Center', 'author_id': 360786799676, 'comments_disabled': False, 'draft': False, 'promoted': False, 'position': 0, 'vote_sum': 0, 'vote_count': 0, 'section_id': 7253394947215, 'created_at': '2023-06-22T00:32:20Z', 'updated_at': '2025-11-26T00:43:18Z', 'name': 'How do I customize my Help Center?', 'title': 'How do I customize my Help Center?', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2025-11-26T00:43:18Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>You can modify the look and feel of your Help Center by changing colors and fonts. See <a href="https://support.zendesk.com/hc/en-us/articles/206177737" target="_blank">Branding your Help Center</a> to learn how.</p>\n\n<p>You can also change the design of your Help Center. If you\'re comfortable working with page code, you can dig in to the site\'s HTML, CSS, and Javascript to customize your theme. To get started, see <a href="https://support.zendesk.com/hc/en-us/articles/203664326" target="_blank">Customizing the Help Center</a>.</p>', 'user_segment_ids': []}, {'id': 7253391134863, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253391134863.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253391134863-How-can-agents-leverage-knowledge-to-help-customers', 'author_id': 360786799676, 'comments_disabled': False, 'draft': False, 'promoted': False, 'position': 0, 'vote_sum': 0, 'vote_count': 0, 'section_id': 7253394947215, 'created_at': '2023-06-22T00:32:20Z', 'updated_at': '2023-06-22T00:32:20Z', 'name': 'How can agents leverage knowledge to help customers?', 'title': 'How can agents leverage knowledge to help customers?', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2023-06-22T00:32:20Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>You can use our <a href="https://support.zendesk.com/hc/en-us/articles/115012706488" target="_blank">Knowledge Capture app</a> to leverage your team’s collective knowledge.</p>\n<p>Using the app, agents can:\n</p><ul>\n  <li>Search the Help Center without leaving the ticket</li>\n  <li>Insert links to relevant Help Center articles in ticket comments</li>\n  <li>Add inline feedback to existing articles that need updates</li>\n  <li>Create new articles while answering tickets using a pre-defined template</li>\n</ul>\n\n\n<p>Agents never have to leave the ticket interface to share, flag, or create knowledge, so they can help the customer, while also improving your self-service offerings for other customers.</p>\n\n<p>To get started, see our <a href="https://support.zendesk.com/hc/en-us/articles/360001975088" target="_blank">Knowledge Capture documentation</a>.</p>\n\n<p>And before your agents can start creating new knowledge directly from tickets, you’ll need to <a href="https://support.zendesk.com/hc/en-us/articles/115002374987" target="_blank">create a template</a> for them to use. To help you along, we’ve provided some template ideas below. You can copy and paste any sample template below into a new article, add the <strong>KCTemplate</strong> label to the article, and you’ll be all set.</p>\n\n<h4>Q&amp;A template:</h4>\n\n<blockquote>\n\n<p>\n</p>\n<h3>[Title]</h3>\n\n\n<p>\n</p>\n<h3>Question</h3>\nwrite the question here.\n\n\n<p>\n</p>\n<h3>Answer</h3>\nwrite the answer here.\n\n\n</blockquote>\n\n<h4>Solution template:</h4>\n\n<blockquote>\n\n<p>\n</p>\n<h3>[Title]</h3>\n\n\n<p>\n</p>\n<h3>Symptoms</h3>\nwrite the symptoms here.\n\n\n<p>\n</p>\n<h3>Resolution</h3>\nwrite the resolution here.\n\n\n<p>\n</p>\n<h3>Cause</h3>\nwrite the cause here.\n\n\n</blockquote>\n\n<h4>How-to template:</h4>\n\n<blockquote>\n\n<p>\n</p>\n<h3>[Title]</h3>\n\n\n<p>\n</p>\n<h3>Objective</h3>\nwrite the purpose or task here.\n\n\n<p>\n</p>\n<h3>Procedure</h3>\nwrite the steps here.\n\n\n</blockquote>\n', 'user_segment_ids': []}, {'id': 7253391127951, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253391127951.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253391127951-How-do-I-publish-my-content-in-other-languages', 'author_id': 360786799676, 'comments_disabled': False, 'draft': False, 'promoted': False, 'position': 0, 'vote_sum': 0, 'vote_count': 0, 'section_id': 7253394947215, 'created_at': '2023-06-22T00:32:20Z', 'updated_at': '2023-06-22T00:32:20Z', 'name': 'How do I publish my content in other languages?', 'title': 'How do I publish my content in other languages?', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2023-06-22T00:32:20Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>If you have <a href="https://support.zendesk.com/hc/en-us/articles/224857687" target="_blank">configured your Help Center to support multiple languages</a>, you can publish content in your supported languages. </p>\n\n<p>Here\'s the workflow for localizing your Help Center content into other languages:</p>\n\n<ol>\n<li>Get your content translated in the other languages.</li>\n<li>Configure the Help Center to support all your languages.</li>\n<li>Add the translated content to the Help Center.</li>\n</ol>\n\n\n<p>For complete instructions, see <a href="https://support.zendesk.com/hc/en-us/articles/203664336#topic_inn_3qy_43" target="_blank">Localizing the Help Center</a>.</p>', 'user_segment_ids': []}, {'id': 7253391120527, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253391120527.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253391120527-What-are-these-sections-and-articles-doing-here', 'author_id': 360786799676, 'comments_disabled': False, 'draft': False, 'promoted': False, 'position': 0, 'vote_sum': 1, 'vote_count': 1, 'section_id': 7253394947215, 'created_at': '2023-06-22T00:32:20Z', 'updated_at': '2023-09-04T13:52:58Z', 'name': 'What are these sections and articles doing here?', 'title': 'What are these sections and articles doing here?', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2023-06-22T00:32:20Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>This FAQ is a section in the General category of your help center knowledge base. We created this category and a few common sections to help you get started with your Help Center.</p>\n\n<p>The knowledge base in the Help Center consists of three main page types: category pages, section pages, and articles. Here\'s the structure:</p>\n\n<p><img src="//static.zdassets.com/hc/assets/sample-articles/article0_image.png" alt="Comments are part of the articles. The articles pages are part of Sections page. The Sections pages are part of the Category pages."></p>\n\n<p>You can create your own categories, sections, and articles and modify or completely delete ours. See the <a href="https://support.zendesk.com/hc/en-us/articles/218222877" target="_blank">Organizing knowledge base content</a> and <a href="https://support.zendesk.com/hc/en-us/articles/203664366" target="_blank">Creating articles in the Help Center</a> to learn how.</p>', 'user_segment_ids': []}, {'id': 7253351877519, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253351877519.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253351877519-Sample-article-Stellar-Skyonomy-refund-policies', 'author_id': 360786799676, 'comments_disabled': False, 'draft': True, 'promoted': False, 'position': 0, 'vote_sum': 0, 'vote_count': 0, 'section_id': 7253394933775, 'created_at': '2023-06-22T00:32:20Z', 'updated_at': '2023-06-22T00:32:20Z', 'name': 'Sample article: Stellar Skyonomy refund policies', 'title': 'Sample article: Stellar Skyonomy refund policies', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2023-06-22T00:32:20Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': "<p>All <strong>Stellar Skyonomy</strong> merchandise purchases are backed by our 30-day satisfaction guarantee, no questions asked. We even pay to have it shipped back to us. Additionally, you can cancel your <strong>Stellar Skyonomy</strong> subscription at any time. Before you cancel, review our refund policies in this article.</p><br><p><strong>Refund policy</strong></p><p>We automatically issue a full refund when you <a>initiate a return</a> within 30 days of delivery.<br><br>To <a>cancel an annual website subscription</a> you can do so at any time and your refund will be prorated based on the cancellation date.</p><br><p><strong>Request a refund</strong></p><p>If you believe you’re eligible for a refund but haven’t received one, contact us by completing a <a>refund request form.</a> We review every refund and aim to respond within two business days.<br><br>If you haven't received a refund you're expecting, note that it can take up to 10 business days to appear on your card statement.</p>", 'user_segment_ids': []}, {'id': 7253394935055, 'url': 'https://d3v-airbyte.zendesk.com/api/v2/help_center/en-us/articles/7253394935055.json', 'html_url': 'https://d3v-airbyte.zendesk.com/hc/en-us/articles/7253394935055-Welcome-to-your-Help-Center', 'author_id': 360786799676, 'comments_disabled': False, 'draft': False, 'promoted': False, 'position': 0, 'vote_sum': 1, 'vote_count': 1, 'section_id': 7253394933775, 'created_at': '2023-06-22T00:32:19Z', 'updated_at': '2025-11-14T00:37:49Z', 'name': 'Welcome to your Help Center!', 'title': 'Welcome to your Help Center!', 'source_locale': 'en-us', 'locale': 'en-us', 'outdated': False, 'outdated_locales': [], 'edited_at': '2025-11-14T00:37:49Z', 'user_segment_id': None, 'permission_group_id': 7253379449487, 'content_tag_ids': [], 'label_names': [], 'body': '<p>You\'re looking at your new <a href="https://www.zendesk.com/self-service" target="_blank">Help Center</a>. We populated it with placeholder content to help you get started. Feel free to edit or delete this content.</p>\n\n<p>The Help Center is designed to provide a complete self-service support option for your customers. The Help Center contains: a knowledge base and, on Guide Professional and Enterprise, a Customer Portal for support requests. You can also add a community to your Help Center if you have Zendesk Gather.</p>\n\n<p>Your customers can search for knowledge base articles to learn a task or search the community, if available, to ask fellow users questions. If your customers can\'t find an answer, they can submit a support request.</p>\n\n<p>For more information, see <a href="https://support.zendesk.com/hc/en-us/articles/203664386" target="_blank">Help Center guide for end users</a>.</p><p>Each user has a Help Center profile (Guide Professional and Enterprise), so your Help Center users can get to know one another better. Profiles contain relevant information about the user, along with their activities and contributions.</p>', 'user_segment_ids': []}], 'sort_by': 'position', 'sort_order': 'asc'}

    connector = ZendeskSupportConnector.create(auth_config={"access_token": "test_key"})

    with patch(
        "airbyte_ai_zendesk_support._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.articles.list()

    assert result == mock_response

