from dataclasses import dataclass

from manim import *

from style.components import (
    ERROR,
    MUTED,
    PRIMARY,
    SUCCESS,
    TEXT_PRIMARY,
    WARNING,
    make_answer_badge,
    make_formula_box,
    make_step_label,
    make_title,
    make_warning_badge,
    set_gradient_background,
)


@dataclass
class VideoSpec:
    code: str
    topic: str
    objective: str
    formula: str
    examples: list[str]
    mistake: str
    correction: str
    quick_checks: list[str]
    recap: str
    narration: list[str]


FAST = 0.9
STANDARD = 1.2
SLOW = 1.6


def build_standard_scene(scene: Scene, spec: VideoSpec) -> None:
    set_gradient_background(scene)

    title = make_title(f"{spec.code}: {spec.topic}")
    scene.play(Write(title), run_time=SLOW)
    scene.wait(1.8)

    scene.play(title.animate.scale(0.9).to_edge(UP), run_time=STANDARD)
    objective = Text(f"Objective: {spec.objective}", color=TEXT_PRIMARY, font_size=30).next_to(title, DOWN, buff=0.32)
    scene.play(FadeIn(objective, shift=0.15 * DOWN), run_time=STANDARD)

    formula_box = make_formula_box(spec.formula).next_to(objective, DOWN, buff=0.5)
    scene.play(Write(formula_box), run_time=SLOW)
    scene.wait(0.35)

    first_example = spec.examples[0] if spec.examples else "No worked example provided."
    example = Text(f"Example: {first_example}", color=PRIMARY, font_size=30).next_to(formula_box, DOWN, buff=0.42)
    scene.play(FadeIn(example, shift=0.15 * DOWN), run_time=STANDARD)

    mistake = make_warning_badge(spec.mistake).scale(0.9).next_to(example, DOWN, buff=0.45)
    correction = Text(spec.correction, color=SUCCESS, font_size=28).next_to(mistake, DOWN, buff=0.25)
    scene.play(FadeIn(mistake), run_time=STANDARD)
    scene.play(Write(correction), run_time=STANDARD)

    quick_prompt = spec.quick_checks[0] if spec.quick_checks else "State one key check question."
    check = Text(f"Quick check: {quick_prompt}", color=MUTED, font_size=24).to_edge(DOWN, buff=0.8)
    recap_badge = make_answer_badge(spec.recap).next_to(check, UP, buff=0.25)
    scene.play(FadeIn(check, shift=0.1 * UP), run_time=STANDARD)
    scene.play(Flash(recap_badge, color=SUCCESS), FadeIn(recap_badge, shift=0.2 * UP), run_time=SLOW)
    scene.wait(1.0)


def build_step_by_step_scene(scene: Scene, spec: VideoSpec) -> None:
    set_gradient_background(scene)

    title = make_title(f"{spec.code}: {spec.topic}")
    scene.play(Write(title), run_time=SLOW)
    scene.wait(1.2)
    scene.play(title.animate.scale(0.85).to_edge(UP), run_time=STANDARD)

    part = make_step_label("Part 1: Objective and Formula").to_edge(LEFT).shift(UP * 1.9)
    objective = Text(f"Objective: {spec.objective}", color=TEXT_PRIMARY, font_size=30).next_to(part, DOWN, aligned_edge=LEFT, buff=0.28)
    formula_box = make_formula_box(spec.formula).next_to(objective, DOWN, aligned_edge=LEFT, buff=0.35)
    scene.play(FadeIn(part), FadeIn(objective, shift=0.15 * DOWN), run_time=STANDARD)
    scene.play(Write(formula_box), run_time=SLOW)
    scene.wait(0.35)

    examples_header = make_step_label("Part 2: Worked Examples").next_to(formula_box, DOWN, aligned_edge=LEFT, buff=0.45)
    scene.play(FadeIn(examples_header), run_time=STANDARD)

    example_panel = VGroup()
    for i, example_line in enumerate(spec.examples, start=1):
        step_title = Text(f"Example {i}", color=PRIMARY, font_size=30)

        given_text = example_line
        outputs = []
        if "->" in example_line:
            left, right = example_line.split("->", maxsplit=1)
            given_text = left.strip()
            outputs = [item.strip() for item in right.split(",") if item.strip()]

        given = Text(f"Given: {given_text}", color=TEXT_PRIMARY, font_size=26)
        panel_lines = [step_title, given]
        panel_lines.extend(Text(f"Step {k}: {value}", color=PRIMARY, font_size=24) for k, value in enumerate(outputs, start=1))
        current = VGroup(*panel_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        current.next_to(examples_header, DOWN, aligned_edge=LEFT, buff=0.22)

        if len(example_panel) == 0:
            scene.play(FadeIn(current[0]), FadeIn(current[1], shift=0.1 * DOWN), run_time=STANDARD)
        else:
            scene.play(ReplacementTransform(example_panel, current), run_time=STANDARD)

        for step_line in current[2:]:
            scene.play(FadeIn(step_line, shift=0.1 * RIGHT), run_time=FAST)
        scene.wait(0.2)
        example_panel = current

    mistake_header = make_step_label("Part 3: Common Mistake").to_edge(RIGHT).shift(UP * 0.95)
    warning = make_warning_badge(spec.mistake).scale(0.95).next_to(mistake_header, DOWN, buff=0.26)
    correction = Text(spec.correction, color=SUCCESS, font_size=24).next_to(warning, DOWN, buff=0.22)
    scene.play(FadeIn(mistake_header), FadeIn(warning), run_time=SLOW)
    scene.play(Write(correction), run_time=STANDARD)

    checks_header = make_step_label("Part 4: Quick Checks").to_edge(DOWN).shift(UP * 1.05)
    scene.play(FadeIn(checks_header), run_time=STANDARD)
    for q in spec.quick_checks:
        prompt = Text(f"• {q}", color=MUTED, font_size=22).next_to(checks_header, DOWN, buff=0.18)
        scene.play(FadeIn(prompt, shift=0.1 * UP), run_time=FAST)
        scene.wait(0.15)
        scene.play(FadeOut(prompt), run_time=FAST)

    recap_badge = make_answer_badge(spec.recap).to_edge(DOWN)
    scene.play(Flash(recap_badge, color=SUCCESS), FadeIn(recap_badge, shift=0.2 * UP), run_time=SLOW)
    scene.wait(1.0)
