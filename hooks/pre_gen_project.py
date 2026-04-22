"""Pre-generation hook to ensure required commands are available.

This hook runs before the template is rendered. It verifies that ``uv`` and
``git`` commands are available on the path, that git is configured with a user
name and email, and that the derived project and package slugs are valid.

The target project's Python version is detected at render time from
``uv python find`` and defaults to 3.14 if unavailable.
"""

from __future__ import annotations

import keyword
import re
import shutil
import subprocess
import sys

REQUIRED_COMMANDS = ("uv", "git")

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PACKAGE_SLUG = "{{ cookiecutter.package_slug }}"

# PEP 508 / PyPI: must start and end with alphanumeric; interior may have . - _
_PYPI_NAME_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?$")


def _check_commands() -> None:
    """Ensure all required external commands are available."""
    missing = [cmd for cmd in REQUIRED_COMMANDS if shutil.which(cmd) is None]

    if missing:
        missing_str = ", ".join(missing)
        msg = (
            f"Missing required command(s): {missing_str}. "
            "Please install them and try again."
        )
        sys.exit(msg)


def _check_git_user_config() -> None:
    """Ensure git has the user name and email configured."""
    git_executable = shutil.which("git")
    if git_executable is None:
        return
    keys = ("user.name", "user.email")
    missing: list[str] = []
    for key in keys:
        result = subprocess.run(  # noqa: S603
            [git_executable, "config", "--global", key],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0 or not result.stdout.strip():
            missing.append(key.split(".")[-1])

    if missing:
        missing_str = ", ".join(missing)
        msg = (
            f"Missing required git configuration: {missing_str}. "
            "Please set these with `git config --global user.name 'Your Name'` "
            "and `git config --global user.email 'you@example.com'`."
        )
        sys.exit(msg)


def _check_slugs() -> None:
    """Validate derived project_slug and package_slug."""
    if not _PYPI_NAME_RE.match(PROJECT_SLUG):
        sys.exit(
            f"Invalid project name '{PROJECT_SLUG}': must start and end with a letter "
            "or digit and contain only letters, digits, hyphens, underscores, and dots."
        )
    if not PACKAGE_SLUG.isidentifier():
        sys.exit(
            f"Invalid package name '{PACKAGE_SLUG}': must be a valid Python identifier "
            "(letters, digits, and underscores only; cannot start with a digit)."
        )
    if keyword.iskeyword(PACKAGE_SLUG):
        sys.exit(
            f"Invalid package name '{PACKAGE_SLUG}': '{PACKAGE_SLUG}' is a reserved "
            "Python keyword. Please choose a different project name."
        )


def main() -> None:
    """Run all dependency checks before rendering the template."""
    _check_commands()
    _check_git_user_config()
    _check_slugs()


if __name__ == "__main__":
    main()
