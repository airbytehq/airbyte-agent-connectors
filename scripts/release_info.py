#!/usr/bin/env python3
"""
Script to gather release information for publishing packages to PyPI.

This script:
1. Reads the package version from pyproject.toml
2. Checks if the version already exists on PyPI
3. Extracts changelog notes for the version

Outputs are printed in GITHUB_OUTPUT format for use in GitHub Actions,
but can also be run locally for testing.

Usage:
    python scripts/release_info.py \
        --pyproject connectors/stripe/pyproject.toml \
        --changelog connectors/stripe/CHANGELOG.md \
        --package-name airbyte-agent-stripe

    # For MCP:
    python scripts/release_info.py \
        --pyproject airbyte-agent-mcp/pyproject.toml \
        --changelog airbyte-agent-mcp/CHANGELOG.md \
        --package-name airbyte-agent-mcp
"""

import argparse
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path


def get_version(pyproject_path: Path) -> str:
    """Read the version from pyproject.toml."""
    data = tomllib.loads(pyproject_path.read_text())
    return data["project"]["version"]


def check_pypi_exists(package_name: str, version: str) -> bool:
    """Check if a version already exists on PyPI.

    Returns True if the version exists, False otherwise.
    For network errors or non-404 HTTP errors, returns False (assumes version doesn't exist).
    """
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    req = urllib.request.Request(url, method="HEAD")

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        # For other HTTP errors (5xx, etc.), assume version doesn't exist
        # This means we'll attempt to publish, and twine will fail if it does exist
        print(f"Warning: PyPI check returned HTTP {e.code}", file=sys.stderr)
        return False
    except urllib.error.URLError as e:
        # Network error - assume version doesn't exist
        print(f"Warning: PyPI check failed: {e}", file=sys.stderr)
        return False


def extract_changelog_notes(changelog_path: Path, version: str) -> str:
    """Extract the changelog section for a specific version.

    Returns empty string if changelog file doesn't exist or version section not found.
    """
    if not changelog_path.exists():
        return ""

    lines = changelog_path.read_text().splitlines(keepends=True)

    in_version_section = False
    notes_lines = []
    version_header = f"## [{version}]"

    for line in lines:
        if line.startswith(version_header):
            in_version_section = True
            continue
        elif in_version_section and line.startswith("## ["):
            # Reached the next version section
            break
        elif in_version_section:
            # Skip empty lines at the start
            if not notes_lines and not line.strip():
                continue
            notes_lines.append(line.rstrip())

    # Remove trailing empty lines
    while notes_lines and not notes_lines[-1]:
        notes_lines.pop()

    return "\n".join(notes_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gather release information for PyPI publishing"
    )
    parser.add_argument(
        "--pyproject",
        required=True,
        help="Path to pyproject.toml",
    )
    parser.add_argument(
        "--changelog",
        required=True,
        help="Path to CHANGELOG.md",
    )
    parser.add_argument(
        "--package-name",
        required=True,
        help="PyPI package name (e.g., airbyte-agent-stripe)",
    )
    parser.add_argument(
        "--github-output",
        action="store_true",
        help="Output in GITHUB_OUTPUT format (default: human-readable)",
    )
    args = parser.parse_args()

    pyproject_path = Path(args.pyproject)
    changelog_path = Path(args.changelog)

    # Validate pyproject.toml exists
    if not pyproject_path.exists():
        print(f"Error: pyproject.toml not found at {pyproject_path}", file=sys.stderr)
        sys.exit(1)

    # Get version - let KeyError propagate if project.version is missing
    # as that indicates a malformed pyproject.toml
    version = get_version(pyproject_path)

    # Check PyPI
    exists_on_pypi = check_pypi_exists(args.package_name, version)
    should_publish = not exists_on_pypi

    # Extract changelog
    notes = extract_changelog_notes(changelog_path, version)
    if not notes:
        notes = f"Release of {args.package_name} version {version}"

    # Output results
    if args.github_output:
        print(f"version={version}")
        print(f"should_publish={'true' if should_publish else 'false'}")
        # Use heredoc format for multiline notes
        print("notes<<EOF")
        print(notes)
        print("EOF")
    else:
        print(f"Package: {args.package_name}")
        print(f"Version: {version}")
        print(f"Exists on PyPI: {exists_on_pypi}")
        print(f"Should publish: {should_publish}")
        print(f"\nChangelog notes:\n{notes}")


if __name__ == "__main__":
    main()
