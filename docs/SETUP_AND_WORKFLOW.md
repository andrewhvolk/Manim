# Setup and workflow guide

This is the main guide for working in this repository.

## First-time Windows setup

From the repository root, run the Windows setup script:

`scripts/setup_windows_safe.ps1`

That script installs system tools, creates `.venv`, installs Python dependencies, and verifies Manim.

## Daily local workflow

1. Open PowerShell in the repository root.
2. Activate `.venv`.
3. Run the preview or final render script.

Use `scripts/render_preview_safe.ps1` for quick renders.
Use `scripts/render_final_safe.ps1` for higher-quality renders.

## Manual render pattern

Preview:

`python -m manim -pql scenes/lesson_001_intro.py Lesson001Intro`

Final:

`python -m manim -pqh scenes/lesson_001_intro.py Lesson001Intro`

## File layout

- `scenes/` holds source scenes.
- `assets/` holds reusable inputs.
- `media/` holds generated output.
- `docs/` holds setup and workflow notes.
- `scripts/` holds helper scripts.

## Good practice

- Keep source in Git.
- Treat `media/` as generated output.
- Commit rendered videos only when you intentionally want a permanent artifact.
- Preview before final render.

## When to rerun setup

Rerun the full setup script only for a new machine, a rebuilt virtual environment, or broken dependencies.
For normal work, activating `.venv` is enough.

## Codex

For Codex container setup, see `docs/CODEX_SETUP.md`.
