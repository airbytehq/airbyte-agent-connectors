#!/bin/bash
# Run connector evaluations for a specific connector
#
# Usage: ./scripts/connectors/eval.sh <connector_name>
# Example: ./scripts/connectors/eval.sh gong

set -e

CONNECTOR=$1

if [ -z "$CONNECTOR" ]; then
    echo "Usage: $0 <connector_name>"
    echo "Example: $0 gong"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONNECTOR_DIR="$REPO_ROOT/connectors/$CONNECTOR"
EVALS_DIR="$CONNECTOR_DIR/evals"

if [ ! -d "$EVALS_DIR" ]; then
    echo "Error: Evals directory not found at $EVALS_DIR"
    exit 1
fi

echo "Running evaluations for connector: $CONNECTOR"
echo "Evals directory: $EVALS_DIR"
echo ""

cd "$REPO_ROOT/connector_evals"

# Install dependencies if needed
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi

echo "Installing dependencies..."
uv pip install -e ".[dev]"
uv pip install -e "../connectors/$CONNECTOR"

echo ""
echo "Running evaluations..."
uv run pytest "$EVALS_DIR" -m evals -v --tb=short

echo ""
echo "Evaluations complete!"
