"""Jinja2 extension to provide git user info for defaults."""

from __future__ import annotations

import subprocess
from jinja2 import Environment
from jinja2.ext import Extension

from typing import Any, cast

from collections.abc import MutableMapping


def _git_config(key: str) -> str:
    """Return the configured git value for ``key``."""
    result = subprocess.run(
        ["git", "config", "--global", key],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


class GitUserConfigExtension(Extension):
    """Expose git user name and email as Jinja2 globals."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        globals_map: MutableMapping[str, Any] = cast(  # pyright: ignore[reportExplicitAny]
            MutableMapping[str, Any],  # pyright: ignore[reportExplicitAny]
            environment.globals,
        )
        globals_map.update(
            git_username=lambda: _git_config("user.name"),
            git_email=lambda: _git_config("user.email"),
        )
