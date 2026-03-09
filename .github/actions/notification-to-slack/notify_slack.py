#!/usr/bin/env python3
"""
Send a notification to a Slack channel.

Usage:
    export SLACK_BOT_TOKEN=xoxb-...
    python notify_slack.py --channel C07PPP45S78 --message-body '[{"type": "section", "text": {"type": "mrkdwn", "text": "Hello!"}}]'

Or with --token:
    python notify_slack.py --channel C07PPP45S78 --message-body '...' --token xoxb-...
"""

import argparse
import json
import os
import sys

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from termcolor import cprint


def parse_args():
    parser = argparse.ArgumentParser(
        description="Send a notification to a Slack channel"
    )
    parser.add_argument(
        "--channel",
        required=True,
        help="Slack channel ID (e.g., C07PPP45S78)",
    )
    parser.add_argument(
        "--message-body",
        required=True,
        help="JSON array of Slack blocks",
    )
    parser.add_argument(
        "--message-text",
        default="",
        help="Optional plain text message (fallback for notifications)",
    )
    parser.add_argument(
        "--token",
        help="Slack bot token; or set SLACK_BOT_TOKEN environment variable",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    token = args.token or os.getenv("SLACK_BOT_TOKEN")
    if not token:
        cprint(
            "Missing Slack bot token (set SLACK_BOT_TOKEN or pass --token)",
            "red",
        )
        sys.exit(1)

    try:
        message_body = json.loads(args.message_body, strict=False)
    except json.JSONDecodeError as e:
        cprint(f"Invalid JSON in message-body: {e}", "red")
        sys.exit(1)

    raw_text = (args.message_text or "").strip()
    if raw_text:
        text = raw_text
    elif message_body:
        text = message_body[0].get("text", {}).get("text", "")
    else:
        text = ""

    print(json.dumps(message_body, indent=4))

    client = WebClient(token=token)
    try:
        client.chat_postMessage(channel=args.channel, text=text, blocks=message_body)
        cprint("Message sent successfully!", "green")
    except SlackApiError as error:
        print()
        cprint("Error on calling the Slack API!", "red")
        cprint("-" * 78, "red")
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
