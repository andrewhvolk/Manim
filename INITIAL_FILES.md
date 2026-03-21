# Initial Files to Generate

Codex should generate a minimal first working version of the repository.

## Required files

1. `.gitignore`
2. `pyproject.toml` if using `uv`
3. `requirements.txt` if useful as an export or fallback
4. `docs/SETUP.md`
5. `docs/WORKFLOW.md`
6. `docs/STYLE_GUIDE.md`
7. `docs/VIDEO_BRIEF_TEMPLATE.md`
8. `scenes/lesson_001_intro.py`
9. optional helper render scripts in `scripts/`

## Minimal scene requirement

The first scene should:
- import from `manim`;
- render a simple title and at least one mathematical object or graph;
- be short and stable;
- be suitable for testing whether the environment works.

## README requirements after generation

The repository README should then include:
- what the project is;
- how to create the environment;
- how to install dependencies;
- how to render the sample scene;
- where output files are written;
- how future lessons should be added.
