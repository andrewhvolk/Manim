# Workflow

1. Write a short lesson objective.
2. Draft a scene outline.
3. Implement one scene file.
4. Render a low-quality preview.
5. Review accuracy, pacing, and readability.
6. Revise before making a final render.

## Render commands

### Preview

```bash
manim -pql scenes/lesson_001_intro.py Lesson001Intro
```

### Final

```bash
manim -pqh scenes/lesson_001_intro.py Lesson001Intro
```
