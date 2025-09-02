#!/bin/sh

# Exit on error
set -e

# Add development dependencies
uv add --dev ruff
uv add --dev basedpyright
uv add --dev pre-commit

# Initialize git and install pre-commit hooks
git init -b "main"
uv run pre-commit install
uv run pre-commit autoupdate
uv run pre-commit install

# Make initial commit
git add .
uv run pre-commit run --all-files
git add .
git commit -m "Initial commit"

echo "Project {{ cookiecutter.project_name }} is ready!"
