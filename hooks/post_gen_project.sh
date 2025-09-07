#!/bin/sh
set -e

# portable temp log (fallback)
if command -v mktemp >/dev/null 2>&1; then
  LOG="$(mktemp --suffix=.log 2>/dev/null || mktemp /tmp/project_setup.XXXXXX.log)"
else
  LOG="./project_setup.log"
fi

run_tasks() {
  uv add --dev ruff
  uv add --dev basedpyright
  uv add --dev prek

  git init -b "main"
  uv run prek install
  uv run prek autoupdate
  uv run prek install

  git add .
  uv run prek run --all-files
  git add .
  git commit -m "Initial commit"
}

spinner() {
  pid="$1"
  delay=0.12
  while kill -0 "$pid" 2>/dev/null; do
    for c in '|' '/' '-' '\'; do
      printf '\r%s Running setup...' "$c"
      sleep "$delay"
    done
  done
}

# clear current terminal line in a portable way
clear_line() {
  # move to start then clear to end of line
  printf '\r'
  if command -v tput >/dev/null 2>&1; then
    tput el
  else
    printf '\033[K'
  fi
}

(
  set -e
  run_tasks
) >"$LOG" 2>&1 &
worker=$!

spinner "$worker" &
spin_pid=$!

wait "$worker"
status=$?

# stop spinner
kill "$spin_pid" 2>/dev/null || true
wait "$spin_pid" 2>/dev/null || true

# make sure spinner line is removed before printing anything else
clear_line

if [ "$status" -ne 0 ]; then
  echo "Setup failed (exit code $status). Showing log: $LOG"
  echo "----- BEGIN LOG -----"
  cat "$LOG" >&2
  echo "------ END LOG ------"
  exit "$status"
fi

# visible success printed from main process
printf 'Project %s is ready!\n' "{{ cookiecutter.project_name }}"

rm -f "$LOG" 2>/dev/null || true
exit 0
