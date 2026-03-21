from scenes._template_lesson import TemplateLesson


class Lesson002LinearEquationIntro(TemplateLesson):
    """Short lesson introducing how to solve equations of the form ax + b = c."""

    lesson_title = "Lesson 002: Solving ax + b = c"
    example_expression = r"\begin{aligned}2x + 3 &= 11\\2x &= 8\\x &= 4\end{aligned}"
    explanation_lines = (
        r"Subtract $b$ from both sides first.",
        r"Then divide both sides by $a$, with $a \neq 0$.",
    )
    summary_lines = (
        r"To solve $ax+b=c$, undo the $+b$ step first.",
        r"Then undo the multiplication by $a$.",
    )
