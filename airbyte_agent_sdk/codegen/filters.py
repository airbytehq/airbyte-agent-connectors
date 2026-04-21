"""
Jinja2 template filters for code generation.

These functions are used as filters in Jinja2 templates and can also be
imported directly for use in Python code.
"""

import re


def to_snake_case(value: str) -> str:
    """Convert string to snake_case."""
    # Insert underscore before uppercase letters that follow lowercase letters
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
    # Insert underscore before uppercase letters that follow numbers or lowercase
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    # Replace hyphens and spaces with underscores
    s3 = s2.replace("-", "_").replace(" ", "_")
    # Convert to lowercase
    return s3.lower()


def to_pascal_case(value: str) -> str:
    """Convert string to PascalCase."""
    # Replace hyphens, underscores, and spaces with spaces
    s1 = value.replace("-", " ").replace("_", " ")
    # Split into words and capitalize each
    words = s1.split()
    # Join capitalized words
    return "".join(word.capitalize() for word in words)


def mdx_escape(value: str) -> str:
    """Escape special characters for MDX compatibility.

    MDX treats curly braces as JavaScript expression delimiters and
    angle brackets as JSX tag delimiters. This filter escapes them
    so they render as literal characters in markdown.

    Note: This function is also imported by scripts/connectors/update-readme.py
    for rendering README templates during connector publishing.
    """
    if not isinstance(value, str):
        return value
    return value.replace("{", "\\{").replace("}", "\\}").replace("<", "\\<").replace(">", "\\>")
