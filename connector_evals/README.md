# Connector Evals

A pydantic-evals based evaluation framework for testing connector quality.

## Overview

This framework evaluates how well an LLM agent can answer business questions using connector tools. It tests both tool selection accuracy and response quality.

## Installation

```bash
pip install -e .
```

## Usage

### Running Evaluations

```python
from connector_evals import run_connector_evals

report = await run_connector_evals(
    connector_name="gong",
    eval_cases_path="evals/eval_cases.yaml",
    cassette_dir="evals/eval_cassettes/",
)

report.print(include_reasons=True)
```

### Creating a Connector Agent

```python
from connector_evals import create_connector_agent
from connector_evals.cassette_loader import load_cassettes_from_files

cassette_loader = load_cassettes_from_files(cassette_dir, cassette_files)
agent = create_connector_agent(connector_yaml_path, cassette_loader)
```

## Components

### Framework (`framework.py`)

- `create_connector_agent()` - Creates a pydantic-ai agent with connector operations as tools
- `run_connector_evals()` - Runs all eval cases for a connector
- `parse_connector_yaml()` - Parses connector.yaml to extract entities/actions

### Evaluators (`evaluators.py`)

- `ConnectorToolsCalledEvaluator` - Validates tool calls using optimal matching algorithm
- `LLMJudgeEvaluator` - Evaluates response quality against expected content

### Cassette Loader (`cassette_loader.py`)

- `CassetteLoader` - Loads and matches cassettes to tool calls by entity+action+params
- `load_cassettes_from_files()` - Loads cassettes from YAML files

## Eval Case Format

```yaml
name: connector_business_questions
description: Evaluate connector for business questions

cases:
  - name: case_name
    question: "Business question to answer"
    cassettes:
      - cassette_file.yaml
    expected_tools:
      - entity: users
        action: list
    expected_answer_contains:
      - expected content
    score_threshold: 0.8
```

## Cassette Format

```yaml
- test_name: entity_action
  entity: entity_name
  action: action_name
  captured_response:
    status_code: 200
    body:
      # Response data
```
