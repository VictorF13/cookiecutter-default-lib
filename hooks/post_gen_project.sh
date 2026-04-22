#!/bin/sh
set -e

uv add --dev ruff ty prek

uv sync

git init -b "main"
uv run prek install
uv run prek autoupdate

git add .
uv run prek run --all-files
git restore --staged

printf 'Project %s is ready!\n' "{{ cookiecutter.project_name }}"
