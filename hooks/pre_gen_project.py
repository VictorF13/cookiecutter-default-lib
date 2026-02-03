"""Pre-generation hook to ensure required commands are available.

This hook runs before the template is rendered. It verifies that ``uv`` and
``git`` commands are available on the path, that git is configured with a user
name and email, and that the running Python interpreter is version 3.14 or
newer. If any of these dependencies are missing, the hook exits with a helpful
error message so that users can install what is needed before continuing.
"""

from __future__ import annotations

import shutil
import subprocess
import sys


REQUIRED_COMMANDS = ("uv", "git")


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
    keys = ("user.name", "user.email")
    missing: list[str] = []
    for key in keys:
        result = subprocess.run(
            ["git", "config", "--global", key],
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


def _check_python_version() -> None:
    """Ensure the running Python interpreter is at least version 3.14."""
    required = (3, 14)
    if sys.version_info < required:
        current = ".".join(str(x) for x in sys.version_info[:3])
        required_str = ".".join(str(x) for x in required)
        msg = (
            f"Python {required_str}+ is required to use this template "
            f"(found {current})."
        )
        sys.exit(msg)


def main() -> None:
    """Run all dependency checks before rendering the template."""
    _check_commands()
    _check_git_user_config()
    _check_python_version()


if __name__ == "__main__":
    main()
