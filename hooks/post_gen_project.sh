#!/bin/bash
set -e

PROJECT_DIR="$(pwd)"

cleanup() {
    cd .. && rm -rf "$PROJECT_DIR"
    printf 'Setup failed. Cleaned up "%s".\n' "{{ cookiecutter.project_slug }}" >&2
}
trap cleanup ERR INT TERM

uv add --dev ruff ty prek

git init -b "main"
uv run prek install
uv run prek autoupdate || true

git add .
uv run prek run --all-files
git rm --cached -r .

printf 'Project %s is ready!\n' "{{ cookiecutter.project_name }}"
