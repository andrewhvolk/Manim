# Setup Requirements

This project targets Manim Community and should be set up in an isolated Python environment.

## Preferred path

Use `uv` for environment and dependency management.

Codex should generate commands and configuration that support a setup similar to:

```bash
uv venv
uv pip install manim
```

## Compatible fallback

If needed, support the more traditional approach:

```bash
python -m venv .venv
# activate environment
pip install --upgrade pip
pip install manim
```

## Notes

- Keep the setup instructions practical for a local development machine.
- Include Windows PowerShell commands and macOS/Linux commands where they differ.
- Assume LaTeX may be needed for full mathematical rendering quality.
- Explain any machine-level dependencies that still need separate installation.

## Initial test command

Codex should provide an initial preview command for the first sample scene.
