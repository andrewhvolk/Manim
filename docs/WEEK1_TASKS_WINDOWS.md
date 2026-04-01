# Week 1 tasks (Windows 11, requirements already installed)

Use this checklist after opening the repository root in Windows PowerShell.

## Assumptions

- You already ran setup at least once and `.venv` exists.
- Python dependencies are already installed.
- System dependencies (FFmpeg + MiKTeX) are already installed.

## Day 1: verify your local environment

```powershell
.\.venv\Scripts\Activate.ps1
python -m manim --version
```

Expected result: Manim prints a version and no import error appears.

## Day 2: render the baseline lesson preview

```powershell
.\scripts\render_preview_safe.ps1
```

This should render `Lesson001Intro` from `scenes\lesson_001_intro.py`.

## Day 3: run a baseline final-quality render

```powershell
.\scripts\render_final_safe.ps1
```

Use this as your first "known-good" milestone render.

## Day 4: render the second lesson preview

```powershell
python -m manim -pql scenes/lesson_002_linear_equation_intro.py Lesson002LinearEquationIntro
```

Review readability, pacing, and mathematical clarity.

## Day 5: make one small teaching-focused revision

Possible edits:

- adjust text wording for clarity;
- tweak spacing or timing;
- improve notation consistency.

Then re-run preview:

```powershell
python -m manim -pql scenes/lesson_002_linear_equation_intro.py Lesson002LinearEquationIntro
```

## Day 6: document what you changed

Record in your notes:

- what changed;
- why it improves teaching clarity;
- what still needs revision.

## Day 7: lock week-1 output

Re-render the scene(s) you are keeping as week-1 deliverables:

```powershell
.\scripts\render_preview_safe.ps1
python -m manim -pqh scenes/lesson_002_linear_equation_intro.py Lesson002LinearEquationIntro
```

## Week 1 done checklist

- [ ] I can activate `.venv` and run Manim from the repo root.
- [ ] `Lesson001Intro` renders in preview and final quality.
- [ ] `Lesson002LinearEquationIntro` renders in preview quality.
- [ ] I made and verified at least one clarity-focused revision.
- [ ] I have a short note about next-week priorities.
