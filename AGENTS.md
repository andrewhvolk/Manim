# AGENTS.md

You are working in a Git repository for generating mathematics videos with Manim Community.

## Primary objective

Create a clean, reproducible, teaching-focused Manim project that can be extended into a library of math videos.

## Instruction priority

1. Follow this file.
2. Follow the files in `docs/`.
3. Preserve user-authored content.
4. Prefer safe, minimal, testable changes.

## Working rules

- Read `README.md` and every file in `docs/` before making changes.
- Build the repository structure described in `docs/REPO_LAYOUT.md`.
- Add only the files necessary to create a clean first working version.
- Do not delete existing user-authored files unless explicitly instructed.
- Do not generate a large content library before the first scene is proven to render.
- Prefer one scene class per file.
- Use descriptive filenames and scene names.
- Keep comments concise and useful.
- Keep mathematical notation explicit and correct.
- Assume the intended audience is undergraduate students unless a file states otherwise.

## Environment rules

- Prefer `uv` for environment and dependency management.
- If `uv` is not appropriate for the machine, use `python -m venv .venv` and `pip`.
- Keep setup cross-platform when practical.
- Document commands clearly for Windows PowerShell and macOS/Linux when they differ.
- Configure the project so a user can preview a scene quickly.

## Manim rules

- Target Manim Community.
- Use LaTeX expressions for mathematical notation where appropriate.
- Separate source scenes from generated media.
- Keep preview rendering fast and final rendering explicit.
- Use a simple consistent visual style unless the style guide says otherwise.

## Repository generation tasks

Create at least the following after reading the docs:
- `.gitignore`
- dependency file(s)
- `scenes/`
- `assets/images/`
- `assets/audio/`
- `assets/data/`
- `media/` or other generated-output path consistent with Manim usage
- `scripts/` with render helper scripts if useful
- `.vscode/` settings only if they add clear value

## Validation rules

Before claiming completion:
- verify that the instructions you wrote are internally consistent;
- verify that the minimal Manim scene is valid Python;
- provide exact commands for preview rendering;
- summarize what still depends on local machine packages or external installs.

## Response style

When reporting work:
- give a short summary;
- list created files;
- list exact commands to run next;
- note any assumptions.
