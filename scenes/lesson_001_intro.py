from manim import Axes, Create, DOWN, FadeIn, MathTex, Text, Title, VGroup, Write
from manim import BLUE, YELLOW
from manim import Scene


class Lesson001Intro(Scene):
    """Minimal introductory scene for validating the Manim setup."""

    def construct(self) -> None:
        title = Title("Lesson 001: A First Look at a Quadratic")

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=4,
            tips=False,
        )
        graph = axes.plot(lambda x: 0.5 * x**2 + 1, x_range=[-2.6, 2.6], color=BLUE)
        equation = MathTex(r"y = \tfrac{1}{2}x^2 + 1", color=YELLOW)
        equation.scale(0.9)

        caption = Text("A quadratic stays above the x-axis here.", font_size=28)
        caption_group = VGroup(equation, caption).arrange(DOWN, aligned_edge=DOWN)
        caption_group.next_to(axes, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Create(axes), Create(graph))
        self.play(FadeIn(caption_group))
        self.wait(1)
