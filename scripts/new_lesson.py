from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "scenes" / "_template_lesson.py"
SCENES_DIR = ROOT / "scenes"


def slugify_lesson_name(lesson_name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", lesson_name.strip().lower()).strip("_")
    if not slug:
        raise ValueError("Lesson name must contain letters or numbers.")
    if not slug.startswith("lesson_"):
        slug = f"lesson_{slug}"
    return slug


def class_name_from_slug(slug: str) -> str:
    parts = [part for part in slug.split("_") if part]
    return "".join(part.capitalize() for part in parts)


def build_scene_text(lesson_name: str) -> str:
    slug = slugify_lesson_name(lesson_name)
    class_name = class_name_from_slug(slug)

    template_text = TEMPLATE_PATH.read_text()
    scene_text = template_text.replace("class TemplateLesson(Scene):", f"class {class_name}(Scene):", 1)
    scene_text = scene_text.replace('lesson_title = "Lesson Title"', f'lesson_title = "{lesson_name}"', 1)
    return scene_text


def create_lesson_file(lesson_name: str) -> Path:
    slug = slugify_lesson_name(lesson_name)
    output_path = SCENES_DIR / f"{slug}.py"
    if output_path.exists():
        raise FileExistsError(f"Scene already exists: {output_path}")

    output_path.write_text(build_scene_text(lesson_name))
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new lesson scene from the template.")
    parser.add_argument("lesson_name", help="Lesson title or lesson slug to use for the new scene.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = create_lesson_file(args.lesson_name)
    print(f"Created {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
