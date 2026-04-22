"""Jinja2 extension to provide git user info and uv Python version for defaults."""

from __future__ import annotations

import subprocess
from shutil import which
from typing import TYPE_CHECKING, Any, Literal, cast

from jinja2.ext import Extension

if TYPE_CHECKING:
    from collections.abc import MutableMapping

    from jinja2 import Environment

GitConfigKey = Literal["user.name", "user.email"]

_FALLBACK_PYTHON_VERSION = "3.14"


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


def _uv_python_version() -> str:
    """Return the default Python major.minor version uv would use."""
    uv_executable = which("uv")
    if uv_executable is None:
        return _FALLBACK_PYTHON_VERSION
    result = subprocess.run(  # noqa: S603
        [uv_executable, "python", "find", "--show-version", "--no-project", "--system"],
        capture_output=True,
        text=True,
        check=False,
    )
    version = result.stdout.strip()
    if result.returncode != 0 or not version:
        return _FALLBACK_PYTHON_VERSION
    parts = version.split(".")
    if len(parts) >= 2:  # noqa: PLR2004
        return f"{parts[0]}.{parts[1]}"
    return version


class GitUserConfigExtension(Extension):
    """Expose git user name, email, and uv Python version as Jinja2 globals."""

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
            uv_python_version=_uv_python_version,
        )
