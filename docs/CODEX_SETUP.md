# Codex setup for Manim rendering

This document records the recommended OpenAI Codex container setup for this repository.

## Recommended Codex settings

- **Container image:** `universal`
- **Container caching:** `On`
- **Setup script:** `Manual`
- **Agent internet access:** `On` during setup

## Why these settings

This repository already follows a good Manim project layout:

- `scenes/` for source scenes
- `assets/` for reusable inputs
- `media/` for generated outputs
- `docs/` for workflow guidance
- `scripts/` for helper commands

Manim also depends on system tools that are not covered by Python packages alone. In particular, container setup should install FFmpeg, Cairo/Pango build dependencies, and a LaTeX toolchain for `MathTex`.

## Manual setup script

Use the following script in Codex.

```bash
#!/usr/bin/env bash
set -euxo pipefail

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y \
  ffmpeg \
  pkg-config \
  libcairo2-dev \
  libpango1.0-dev \
  texlive \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-plain-generic \
  dvisvgm

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Source-file format for Manim scenes

Author scenes as plain UTF-8 Python files in `scenes/`.

Recommended conventions:

- one primary scene class per file
- filename pattern such as `lesson_002_limits.py`
- class name pattern such as `Lesson002Limits`

Minimal example:

```python
from manim import *


class Lesson002Limits(Scene):
    def construct(self):
        title = Title("Lesson 002: Limits")
        self.play(Write(title))
        self.wait()
```

## Render commands

Preview render:

```bash
manim -pql scenes/lesson_001_intro.py Lesson001Intro
```

Final render:

```bash
manim -pqh scenes/lesson_001_intro.py Lesson001Intro
```

General pattern for future lessons:

```bash
manim -pql scenes/lesson_002_limits.py Lesson002Limits
manim -pqh scenes/lesson_002_limits.py Lesson002Limits
```

## Output locations

Generated files are written under `media/` according to `manim.cfg`.

- videos in `media/videos/`
- images in `media/images/`
- TeX intermediates in `media/Tex/`
- text intermediates in `media/texts/`

`media/` should remain ignored by Git.

## Recommended workflow

1. Create a new scene file in `scenes/`.
2. Do a quick preview render first.
3. Iterate on content, timing, and layout.
4. Run a final-quality render when the scene is ready.
5. Keep source files in Git and generated outputs out of Git.

## Local development note

This repository now also includes `pyproject.toml` for lightweight project metadata and dependency declaration.
For local installation, either `pip install -r requirements.txt` or `pip install .[dev]` may be used depending on the workflow.
