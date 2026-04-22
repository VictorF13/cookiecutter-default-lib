# cookiecutter-default-lib

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A [Cookiecutter](https://cookiecutter.readthedocs.io) template for bootstrapping a modern, strict Python library. Generates a fully configured project with linting, formatting, type checking, and pre-commit hooks, ready to use immediately after generation.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/): used for dependency management and running tools
- `git`: with `user.name` and `user.email` configured
- [`cookiecutter`](https://cookiecutter.readthedocs.io): to run the template

Install `cookiecutter` via `uv`:

```zsh
uv tool install cookiecutter
```

No specific Python version is required. The template detects the default Python version from your `uv` installation and uses it automatically.

## Usage

```zsh
cookiecutter gh:VictorF13/cookiecutter-default-lib
```

You will be prompted for:

| Prompt | Description | Default |
|---|---|---|
| `project_name` | Human-readable name of the library | `New Project` |
| `project_description` | Short description | Auto-filled from name |
| `python_version` | Minimum Python version for the project | Detected from `uv` |
| `username` | Author name | Detected from `git config` |
| `email` | Author email | Detected from `git config` |

`project_slug` (PyPI name) and `package_slug` (import name) are derived automatically from `project_name` and are not prompted.

## What gets generated

```
<project-slug>/
├── src/<package-slug>/
│   ├── __init__.py       # Module entry point
│   └── py.typed          # PEP 561 type marker
├── pyproject.toml        # Project metadata and tool configuration
├── .pre-commit-config.yaml
├── .python-version       # Pinned to detected Python version
├── .gitignore
├── LICENSE               # MIT
└── README.md
```

### Tooling included

| Tool | Purpose |
|---|---|
| [`ruff`](https://docs.astral.sh/ruff/) | Linting (all rules) and formatting |
| [`ty`](https://github.com/astral-sh/ty) | Type checking |
| [`prek`](https://github.com/astral-sh/prek) | Pre-commit hook runner |
| [`hatchling`](https://hatch.pypa.io) | Build backend |

Pre-commit hooks run on every commit: `ruff check --fix`, `ruff format`, `ty check`, and `uv export`/`uv lock` to keep dependency files in sync.

## Post-generation setup

After rendering the template, the post-generation hook automatically:

1. Installs dev dependencies (`ruff`, `ty`, `prek`) via `uv`
2. Initialises a git repository on `main`
3. Installs and updates pre-commit hooks via `prek`
4. Runs all hooks on the initial files to ensure everything is clean

If any step fails, the generated directory is removed automatically so no partial project is left behind.

## Notes

- This template is primarily for personal use. Issues and pull requests are welcome but may not be addressed promptly.
- The ruff ruleset enables all rules with a minimal set of ignores (`PLR0913`, `D203`, `D213`, `COM812`) for a strict, uncompromising setup.

## License

Distributed under the [MIT License](LICENSE).
