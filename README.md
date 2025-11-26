# AI Connectors

This repository contains auto-generated Python connector packages for Airbyte AI integrations.

## Structure

Each connector is a standalone Python package:

```
connectors/
├── stripe/
│   ├── airbyte_ai_stripe/
│   ├── pyproject.toml
│   ├── CHANGELOG.md
│   └── README.md
├── github/
│   └── ...
└── ...
```

## Publishing

Connectors are automatically published to PyPI when changes are pushed to main.
Each connector has independent versioning and changelog.

## Source

Generated from: https://github.com/airbytehq/airbyte-embedded
