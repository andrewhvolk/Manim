# Repository Layout Specification

Codex should create the following structure unless there is a strong reason to improve it slightly.

```text
.
├─ README.md
├─ AGENTS.md
├─ .gitignore
├─ pyproject.toml            # preferred when using uv
├─ requirements.txt          # acceptable fallback or export
├─ manim.cfg                 # optional if useful
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
├─ media/                    # generated output; should be gitignored
└─ .vscode/
   ├─ settings.json
   └─ tasks.json
```

## Design principles

- `scenes/` contains source animation code.
- `assets/` contains user-supplied inputs.
- `media/` contains generated outputs and should not be committed by default.
- `docs/` contains project guidance for both humans and Codex.
- `scripts/` contains convenience commands for common renders.

## Scene naming conventions

- Use filenames like `lesson_001_intro.py`, `lesson_002_limits.py`, etc.
- Use class names that match the lesson purpose, such as `QuadraticIntro`, `LimitFromTable`, or `ChainRuleExample`.
- Prefer one primary scene class per file.

## Asset naming conventions

- Use lowercase names with underscores.
- Avoid spaces in filenames.
- Keep raw external assets in `assets/` and generated outputs in `media/`.
