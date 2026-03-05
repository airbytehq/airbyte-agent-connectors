"""Shared Google Drive auth helpers for the md2gdoc skill.

Provides:
    get_connector() - initialized GoogleDriveConnector from .env credentials
    get_access_token() - fresh OAuth access token for APIs not covered by the connector (e.g. Docs API)
"""

import os
import json
import urllib.request
import urllib.parse
from pathlib import Path

from dotenv import load_dotenv

_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def _load_env() -> None:
    load_dotenv(_ENV_PATH)
    for key in ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"):
        if not os.environ.get(key):
            raise RuntimeError(
                f"{key} not set. Copy .env.example to .env and fill in your credentials."
            )


def get_connector():
    """Return an initialized GoogleDriveConnector using .env credentials."""
    from airbyte_agent_google_drive import GoogleDriveConnector
    from airbyte_agent_google_drive.models import GoogleDriveAuthConfig

    _load_env()
    return GoogleDriveConnector(
        auth_config=GoogleDriveAuthConfig(
            refresh_token=os.environ["GOOGLE_REFRESH_TOKEN"],
            client_id=os.environ["GOOGLE_CLIENT_ID"],
            client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
        )
    )


def get_access_token() -> str:
    """Get a fresh OAuth access token by refreshing via Google's token endpoint.

    Used for APIs not covered by the connector (e.g. Google Docs API).
    """
    _load_env()
    data = urllib.parse.urlencode({
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "client_secret": os.environ["GOOGLE_CLIENT_SECRET"],
        "refresh_token": os.environ["GOOGLE_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        token_data = json.loads(resp.read())

    access_token = token_data.get("access_token")
    if not access_token:
        raise RuntimeError("No access_token in token refresh response")
    return access_token
