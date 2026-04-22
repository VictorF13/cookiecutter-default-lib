#!/bin/bash
set -e

PROJECT_DIR="$(pwd)"

cleanup() {
    cd .. && rm -rf "$PROJECT_DIR"
    printf 'Setup failed. Cleaned up "%s".\n' "{{ cookiecutter.project_slug }}" >/dev/tty
}
trap cleanup ERR INT TERM

exec >/dev/null 2>&1

uv add --dev ruff ty prek

git init -b "main"
uv run prek install
uv run prek autoupdate || true

git add .
uv run prek run --all-files
git rm --cached -rq .

exec >/dev/tty 2>&1
printf 'Project %s is ready!\n' "{{ cookiecutter.project_name }}"
