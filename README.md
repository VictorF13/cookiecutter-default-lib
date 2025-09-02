# Cookiecutter Default Library Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Cookiecutter template for bootstrapping a modern Python library project. I
use this template myself whenever starting a new library.

## Features

- Pre-generation hook verifies `uv`, `git`, and Python 3.12+.
- Modern `pyproject.toml` configuration with `uv` and pre-commit defaults.
- Personal scaffold used by [VictorF13](https://github.com/VictorF13).

## Installation

Install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/):

```bash
pip install cookiecutter
```

Ensure `uv`, `git`, and Python **3.12+** are available.

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

