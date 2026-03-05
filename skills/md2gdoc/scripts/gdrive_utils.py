"""Google Drive utility commands for the md2gdoc skill.

Uses the airbyte-agent-google-drive connector for all Drive operations
and urllib for the Docs API (set-pageless).

Subcommands:
    upload-docx <docx_path> [folder_path]
        Upload a .docx file to Google Drive, converting to native Google Doc.
        Prints the Google Docs edit URL to stdout.
        folder_path is a slash-separated path like "Tech Specs/Q1 2026".
        Defaults to root if omitted.

    get-doc-url <folder_path> <basename>
        Find an uploaded file in Google Drive and print its Google Docs URL.

    get-access-token
        Get a fresh OAuth access token from .env credentials.

    set-pageless <file_id>
        Set a Google Doc to pageless mode via the Docs API.

Usage:
    python3 gdrive_utils.py upload-docx /tmp/spec.docx "Tech Specs"
    python3 gdrive_utils.py get-doc-url "Tech Specs" "my-spec"
    python3 gdrive_utils.py get-access-token
    python3 gdrive_utils.py set-pageless "1aBcDeFgHiJkLmNoPqRsTuVwXyZ"
"""

import asyncio
import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from gdrive_auth import get_access_token as _get_access_token, get_connector


async def _resolve_folder_id(connector, folder_path: str) -> str:
    """Resolve a slash-separated folder path to a Google Drive folder ID.

    E.g. "Tech Specs/Q1 2026" -> resolves "Tech Specs" under root, then "Q1 2026" inside it.
    Returns the final folder's ID.
    """
    parent_id = "root"
    parts = [p.strip() for p in folder_path.split("/") if p.strip()]

    for part in parts:
        escaped_part = part.replace("'", "\\'")
        q = (
            f"name = '{escaped_part}' and '{parent_id}' in parents "
            f"and mimeType = 'application/vnd.google-apps.folder' "
            f"and trashed = false"
        )
        result = await connector.files.list(q=q, page_size=1, fields="files(id,name)")
        files = result.data
        if not files:
            print(f"Error: folder '{part}' not found under parent '{parent_id}'", file=sys.stderr)
            sys.exit(1)
        parent_id = files[0].id

    return parent_id


async def _upload_docx(docx_path: str, folder_path: str | None) -> str:
    """Upload a .docx file as a native Google Doc, return the edit URL."""
    connector = get_connector()

    file_bytes = Path(docx_path).read_bytes()
    b64_content = base64.b64encode(file_bytes).decode("utf-8")
    file_name = Path(docx_path).stem

    kwargs = {}
    if folder_path:
        folder_id = await _resolve_folder_id(connector, folder_path)
        kwargs["parents"] = [folder_id]

    result = await connector.files_upload.create(
        upload_type="multipart",
        name=file_name,
        mime_type="application/vnd.google-apps.document",
        file_content=b64_content,
        file_mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        **kwargs,
    )
    file_id = result["id"]
    return f"https://docs.google.com/document/d/{file_id}/edit"


def cmd_upload_docx(docx_path: str, folder_path: str | None = None) -> None:
    """Upload a .docx to Drive as a native Google Doc. Prints edit URL."""
    if not Path(docx_path).exists():
        print(f"Error: file not found: {docx_path}", file=sys.stderr)
        sys.exit(1)

    url = asyncio.run(_upload_docx(docx_path, folder_path))
    print(url)


async def _get_doc_url(folder_path: str, basename: str) -> str:
    """Find an uploaded file in a Drive folder and return its edit URL."""
    connector = get_connector()

    folder_id = await _resolve_folder_id(connector, folder_path)

    escaped_basename = basename.replace("'", "\\'")
    q = (
        f"name contains '{escaped_basename}' and '{folder_id}' in parents "
        f"and trashed = false"
    )
    result = await connector.files.list(q=q, page_size=10, fields="files(id,name,mimeType)")
    files = result.data

    gdoc = next(
        (f for f in files if f.mime_type == "application/vnd.google-apps.document"),
        None,
    )
    docx = next(
        (f for f in files if f.mime_type and "wordprocessingml" in f.mime_type),
        None,
    )
    found = gdoc or docx

    if not found:
        print(f"Error: no file matching '{basename}' found in '{folder_path}'", file=sys.stderr)
        sys.exit(1)

    return f"https://docs.google.com/document/d/{found.id}/edit"


def cmd_get_doc_url(folder_path: str, basename: str) -> None:
    """Find the uploaded file and print its Google Docs edit URL."""
    url = asyncio.run(_get_doc_url(folder_path, basename))
    print(url)


def cmd_get_access_token() -> None:
    """Print a fresh OAuth access token to stdout."""
    print(_get_access_token())


def cmd_set_pageless(file_id: str) -> None:
    """Set a Google Doc to pageless mode via the Docs batchUpdate API."""
    access_token = _get_access_token()

    url = f"https://docs.googleapis.com/v1/documents/{file_id}:batchUpdate"
    payload = json.dumps({
        "requests": [{
            "updateDocumentStyle": {
                "documentStyle": {
                    "documentFormat": {
                        "documentMode": "PAGELESS"
                    }
                },
                "fields": "documentFormat"
            }
        }]
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp.read()
            print(f"Pageless mode set for document {file_id}")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        if e.code == 403:
            print(
                f"Warning: Docs API returned 403. The OAuth project may not have "
                f"the Google Docs API enabled. Use Option B (Chrome MCP) or Option C "
                f"(manual) instead.\nDetails: {error_body}",
                file=sys.stderr,
            )
            sys.exit(2)
        else:
            print(f"Error: Docs API returned HTTP {e.code}: {error_body}", file=sys.stderr)
            sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error connecting to Docs API: {e.reason}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 gdrive_utils.py <subcommand> [args...]", file=sys.stderr)
        print("Subcommands: upload-docx, get-doc-url, get-access-token, set-pageless", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "upload-docx":
        if len(sys.argv) < 3 or len(sys.argv) > 4:
            print("Usage: python3 gdrive_utils.py upload-docx <docx_path> [folder_path]", file=sys.stderr)
            sys.exit(1)
        folder = sys.argv[3] if len(sys.argv) == 4 else None
        cmd_upload_docx(sys.argv[2], folder)

    elif cmd == "get-doc-url":
        if len(sys.argv) != 4:
            print("Usage: python3 gdrive_utils.py get-doc-url <folder_path> <basename>", file=sys.stderr)
            sys.exit(1)
        cmd_get_doc_url(sys.argv[2], sys.argv[3])

    elif cmd == "get-access-token":
        cmd_get_access_token()

    elif cmd == "set-pageless":
        if len(sys.argv) != 3:
            print("Usage: python3 gdrive_utils.py set-pageless <file_id>", file=sys.stderr)
            sys.exit(1)
        cmd_set_pageless(sys.argv[2])

    else:
        print(f"Unknown subcommand: {cmd}", file=sys.stderr)
        print("Subcommands: upload-docx, get-doc-url, get-access-token, set-pageless", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
