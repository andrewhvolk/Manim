# Manim Math Video Repo Starter

This repository is the control layer for a Manim Community math-video project.
It is intentionally light at the start: the first goal is to give Codex clear instructions so it can build the project structure safely and consistently.

## Purpose

Use this repository to:
- generate animated math videos with Manim Community;
- keep scenes, assets, and output organized;
- make the environment reproducible;
- support an AI coding agent workflow through Codex.

## What Codex should do first

1. Read `AGENTS.md` and all files in `docs/`.
2. Create the project layout described in `docs/REPO_LAYOUT.md`.
3. Create a working Python environment configuration using either:
   - `uv` as the preferred modern path; or
   - `venv` + `pip` as a compatible fallback.
4. Add the project files described in `docs/INITIAL_FILES.md`.
5. Create one minimal working Manim scene in `scenes/lesson_001_intro.py`.
6. Provide exact commands for local setup, preview rendering, and final rendering.
7. Do not generate many lessons before the first scene renders successfully.

## Tooling expectations

The repository should target Manim Community.
Use a local isolated Python environment.
Assume LaTeX-based math rendering is desired for final videos.
Assume GitHub will be the source of truth.

## Local setup goals

The generated repo should support:
- local development in VS Code;
- rendering from the command line;
- low-quality preview renders for iteration;
- high-quality final renders;
- simple asset management;
- consistent naming and organization.

## Output philosophy

Optimize for clarity, reusability, and small tested changes.
Prefer one scene class per file unless there is a strong reason otherwise.

## Definition of done for initial setup

The initial setup is complete when all of the following are true:
- the repository structure exists;
- dependencies are declared;
- a minimal scene renders successfully;
- README instructions are accurate;
- `.gitignore` excludes generated media and local environments;
- commands for preview and final render are documented.
