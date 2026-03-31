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

### Scene source format

- Author Manim scenes as plain UTF-8 Python files in `scenes/`
- Prefer one primary scene class per file
- Use filenames such as `lesson_002_limits.py`
- Use matching scene class names such as `Lesson002Limits`

### Render examples

Preview render:

```bash
manim -pql scenes/lesson_001_intro.py Lesson001Intro
```

Final render:

```bash
manim -pqh scenes/lesson_001_intro.py Lesson001Intro
```
