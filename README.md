# Manim Math Video Repo Starter

This repository is a starter project for creating teaching-focused mathematics videos with Manim Community.

## Project structure

- `scenes/` contains source scenes
- `assets/` contains reusable images, audio, and data
- `media/` contains generated output files
- `docs/` contains setup, workflow, and reference documentation
- `scripts/` contains helper scripts for setup and rendering

## Recommended documentation

Use these files as the current source of truth:

- `docs/SETUP_AND_WORKFLOW.md` for the main working guide
- `docs/CODEX_SETUP.md` for Codex container setup
- `scripts/setup_windows_safe.ps1` for first-time Windows setup
- `scripts/render_preview_safe.ps1` for preview renders on Windows PowerShell
- `scripts/render_final_safe.ps1` for final renders on Windows PowerShell

## First-time setup on Windows PowerShell

From the repository root, run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\setup_windows_safe.ps1
```

This script is intended to:

- install Python, FFmpeg, and MiKTeX with winget
- create `.venv` if needed
- activate the virtual environment
- install `requirements.txt`
- install `requirements-dev.txt` when present
- verify that Manim is installed correctly

## Daily local workflow

For normal work, you usually do not need to rerun full setup.

Open PowerShell in the repository root and run:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then use one of the helper scripts:

Preview render:

```powershell
.\scripts\render_preview_safe.ps1
```

Final-quality render:

```powershell
.\scripts\render_final_safe.ps1
```

You can also render a different scene by passing parameters:

```powershell
.\scripts\render_preview_safe.ps1 -SceneFile "scenes\lesson_002_limits.py" -SceneClass "Lesson002Limits"
.\scripts\render_final_safe.ps1 -SceneFile "scenes\lesson_002_limits.py" -SceneClass "Lesson002Limits"
```

## Manual render commands

Preview render:

```bash
python -m manim -pql scenes/lesson_001_intro.py Lesson001Intro
```

Final-quality render:

```bash
python -m manim -pqh scenes/lesson_001_intro.py Lesson001Intro
```

General pattern for future lessons:

```bash
python -m manim -pql scenes/lesson_002_limits.py Lesson002Limits
python -m manim -pqh scenes/lesson_002_limits.py Lesson002Limits
```

## Scene authoring conventions

- store scene source files in `scenes/`
- prefer one primary scene class per file
- use filenames such as `lesson_002_limits.py`
- use matching class names such as `Lesson002Limits`
- preview before final render

## Output location

Generated files are written under `media/`, following the paths configured in `manim.cfg`.

Recommended practice:

- keep source files in Git
- treat `media/` as generated output
- commit rendered videos only when you intentionally want to preserve a milestone artifact

## Refreshing Python packages

If you need to reinstall Python dependencies without rerunning full machine setup:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --no-cache-dir -r requirements.txt
python -m pip install --no-cache-dir -r requirements-dev.txt
```

## When to rerun setup

Rerun `scripts/setup_windows_safe.ps1` only when:

- setting up a new machine
- rebuilding `.venv`
- repairing a broken Python environment
- reinstalling or repairing system dependencies such as FFmpeg or MiKTeX

For ordinary work, activating `.venv` is enough.

## Codex container setup

For OpenAI Codex container usage, see:

- `docs/CODEX_SETUP.md`

That document covers the recommended container image, manual setup script, and render workflow inside Codex.

## Requirements

Python dependencies are managed through:

- `requirements.txt`
- `requirements-dev.txt`

System tools commonly needed for full Manim workflows include:

- FFmpeg
- a LaTeX distribution such as MiKTeX

## Troubleshooting

### No module named manim

Activate `.venv` and reinstall the repository requirements.

### pip cache permission errors

Use `--no-cache-dir` installs. The safe Windows setup script already does this.

### PowerShell cannot find Activate.ps1

The virtual environment has not been created yet. Run `.\scripts\setup_windows_safe.ps1` first.

### MathTex or LaTeX-related problems

Confirm MiKTeX is installed and allow it to install missing packages on first use.
