#!/bin/sh

# Exit on error
set -e

exec >/dev/null 2>&1

# Add development dependencies
uv add --dev ruff
uv add --dev basedpyright
uv add --dev prek

# Initialize git and install prek hooks
git init -b "main"
uv run prek install
uv run prek autoupdate
uv run prek install

# Make initial commit
git add .
uv run prek run --all-files
git add .
git commit -m "Initial commit"

echo "Project {{ cookiecutter.project_name }} is ready!"
