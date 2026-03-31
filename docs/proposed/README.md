# Manim Math Video Repo Starter

This repository is a clean starter project for creating teaching-focused mathematics videos with Manim Community.

## Project structure

- `scenes/` contains source scenes.
- `assets/` contains reusable images, audio, and data.
- `media/` contains generated output files and is ignored by Git.
- `docs/` contains setup, workflow, and style guidance.
- `scripts/` contains helper commands for preview and final renders.

## Environment setup

### Preferred: `uv`

#### macOS/Linux

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt
```

#### Windows PowerShell

```powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt
```

### Fallback: `venv` + `pip`

#### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

## Codex container setup

For OpenAI Codex, use the following configuration when rendering Manim scenes in a container:

- **Container image:** `universal`
- **Container caching:** `On`
- **Setup script:** `Manual`
- **Agent internet access:** `On` during setup

Recommended setup commands:

```bash
apt-get update
apt-get install -y ffmpeg pkg-config libcairo2-dev libpango1.0-dev texlive texlive-latex-extra texlive-fonts-recommended texlive-plain-generic dvisvgm
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The same commands are also recorded in `docs/CODEX_SETUP.md` and `scripts/setup_codex.txt`.

## Render the sample scene

### Preview render

```bash
manim -pql scenes/lesson_001_intro.py Lesson001Intro
```

### Final render

```bash
manim -pqh scenes/lesson_001_intro.py Lesson001Intro
```

Helper scripts are also available:

- macOS/Linux: `./scripts/render_preview.sh` and `./scripts/render_final.sh`
- Windows PowerShell: `./scripts/render_preview.ps1` and `./scripts/render_final.ps1`

## Output location

Generated files are written under `media/`, following the paths configured in `manim.cfg`.

## Adding future lessons

- Add one scene file at a time to `scenes/`.
- Prefer filenames such as `lesson_002_limits.py`.
- Keep one primary scene class per file.
- Preview before creating final renders.

## Local machine requirements

Manim requires local system tools beyond Python packages. In particular:

- FFmpeg should be installed for video rendering.
- A LaTeX distribution may be needed for full mathematical text rendering.

## Project metadata

This repository includes a lightweight `pyproject.toml` for project metadata and development tooling. For local workflows, either of the following is reasonable:

- `pip install -r requirements.txt`
- `pip install -r requirements-dev.txt`
- `uv pip install -r requirements.txt`
- `uv pip install -r requirements-dev.txt`
