"""Jinja2 extension to provide git user info for defaults."""

from __future__ import annotations

import subprocess
from shutil import which
from typing import TYPE_CHECKING, Any, Literal, cast

from jinja2.ext import Extension

if TYPE_CHECKING:
    from collections.abc import MutableMapping

    from jinja2 import Environment

GitConfigKey = Literal["user.name", "user.email"]


def _git_config(key: GitConfigKey) -> str:
    """Return the configured git value for ``key``."""
    git_executable = which("git")
    if git_executable is None:
        return ""
    result = subprocess.run(  # noqa: S603
        [git_executable, "config", "--global", key],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


class GitUserConfigExtension(Extension):
    """Expose git user name and email as Jinja2 globals."""

    def __init__(self, environment: Environment) -> None:
        """Initialize the GitUserConfigExtension."""
        super().__init__(environment)
        globals_map: MutableMapping[str, Any] = cast(
            "MutableMapping[str, Any]",
            environment.globals,
        )
        globals_map.update(
            git_username=lambda: _git_config("user.name"),
            git_email=lambda: _git_config("user.email"),
        )
