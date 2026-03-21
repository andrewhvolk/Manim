# Repository Layout Specification

This project uses a small, teaching-focused Manim Community layout for building one lesson at a time.

```text
.
├─ README.md
├─ AGENTS.md
├─ .gitignore
├─ pyproject.toml
├─ requirements.txt
├─ manim.cfg
├─ docs/
│  ├─ REPO_LAYOUT.md
│  ├─ INITIAL_FILES.md
│  ├─ SETUP.md
│  ├─ STYLE_GUIDE.md
│  ├─ WORKFLOW.md
│  └─ VIDEO_BRIEF_TEMPLATE.md
├─ scenes/
│  └─ lesson_001_intro.py
├─ assets/
│  ├─ images/
│  ├─ audio/
│  └─ data/
├─ scripts/
│  ├─ render_preview.sh
│  ├─ render_preview.ps1
│  ├─ render_final.sh
│  └─ render_final.ps1
├─ media/
└─ .vscode/
   ├─ settings.json
   └─ tasks.json
```

## Notes

- `scenes/` holds source animations.
- `assets/` stores reusable input files.
- `media/` is generated output and is gitignored.
- `scripts/` provides quick preview and final render helpers.
