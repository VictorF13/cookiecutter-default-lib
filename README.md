# Cookiecutter Default Library Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Cookiecutter template for bootstrapping a modern Python library project. This setups a simple library with Python 3.14, `ruff` for linting and formatting, `ty` for type checking, and `prek` for pre-commit hooks, as well as the necessary hooks for those tools.

## Features

- Pre-generation hook verifies `uv`, `git`, and Python 3.14+.
- Modern `pyproject.toml` configuration with `uv` and `prek` defaults using `ty` and `ruff`.

## Installation

Install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/):

```bash
uv tool install cookiecutter
```

Ensure `uv`, `git`, and Python **3.14+** are available.

Configure Git with your `user.name` and `user.email` before running the template
so the initial commit can be created:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Usage

Generate a new project:

```bash
cookiecutter gh:VictorF13/cookiecutter-default-lib
```

Answer the prompts and a skeleton library will be created.

## Documentation

This repository is the documentation for the template. For more on Cookiecutter,
see the [official docs](https://cookiecutter.readthedocs.io/en/latest/).

## Changelog

Pull requests and issues are welcome, but this template is primarily for my
personal use.

## Credits

Created and maintained by [VictorF13](https://github.com/VictorF13). Inspired by
[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) and the broader
Python packaging ecosystem.

## License

Distributed under the [MIT License](LICENSE).
