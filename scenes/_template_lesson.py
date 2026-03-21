from manim import DOWN, LEFT, ORIGIN, RIGHT, FadeIn, MathTex, Scene, Tex, Title, VGroup, Write


class TemplateLesson(Scene):
    """Reusable starter scene for future lessons."""

    lesson_title = "Lesson Title"
    example_expression = r"\text{Example: define the main object here.}"
    explanation_lines = (
        r"\text{Explanation point 1}",
        r"\text{Explanation point 2}",
    )
    summary_lines = (
        r"\text{Summary takeaway 1}",
        r"\text{Summary takeaway 2}",
    )

    def construct(self) -> None:
        title = self.build_title()
        example = self.build_example_section()
        explanation = self.build_explanation_section()
        summary = self.build_summary_section()

        self.play(Write(title))
        self.play(FadeIn(example, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(explanation, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(summary, shift=DOWN))
        self.wait(1)

    def build_title(self) -> Title:
        return Title(self.lesson_title)

    def build_example_section(self) -> VGroup:
        heading = Tex("Example", font_size=40)
        content = MathTex(self.example_expression)
        section = VGroup(heading, content).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        section.next_to(ORIGIN, DOWN, buff=0.8)
        return section

    def build_explanation_section(self) -> VGroup:
        heading = Tex("Explanation", font_size=36)
        lines = [Tex(line, font_size=32) for line in self.explanation_lines]
        body = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        section = VGroup(heading, body).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        section.to_edge(LEFT).shift(DOWN * 0.5)
        return section

    def build_summary_section(self) -> VGroup:
        heading = Tex("Summary", font_size=36)
        lines = [Tex(line, font_size=32) for line in self.summary_lines]
        body = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        section = VGroup(heading, body).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        section.to_edge(RIGHT).shift(DOWN * 0.5)
        return section
