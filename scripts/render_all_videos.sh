#!/usr/bin/env bash
set -euo pipefail

# Render all manim/v*.py scenes in one command.
# Usage:
#   ./scripts/render_all_videos.sh            # final quality (-qh)
#   ./scripts/render_all_videos.sh l          # preview quality (-ql)
#   ./scripts/render_all_videos.sh h --dry-run

QUALITY="${1:-h}"
DRY_RUN="${2:-}"

if [[ "$QUALITY" != "l" && "$QUALITY" != "m" && "$QUALITY" != "h" && "$QUALITY" != "k" ]]; then
  echo "Usage: $0 [l|m|h|k] [--dry-run]"
  exit 1
fi

if [[ -n "$DRY_RUN" && "$DRY_RUN" != "--dry-run" ]]; then
  echo "Second argument must be --dry-run when provided."
  exit 1
fi

if ! command -v python >/dev/null 2>&1; then
  echo "python not found on PATH. Activate your environment first."
  exit 1
fi

for file in manim/v*.py; do
  class_name="$(rg '^class\s+([A-Za-z_][A-Za-z0-9_]*)\(Scene\):' -or '$1' "$file")"
  if [[ -z "$class_name" ]]; then
    echo "Could not find a Scene class in $file"
    exit 1
  fi

  cmd=(python -m manim "-q${QUALITY}" "$file" "$class_name")
  echo "Rendering ${file} :: ${class_name}"
  echo "+ ${cmd[*]}"

  if [[ "$DRY_RUN" != "--dry-run" ]]; then
    "${cmd[@]}"
  fi
done

echo "Done. Rendered outputs are in media/ (git-ignored)."
