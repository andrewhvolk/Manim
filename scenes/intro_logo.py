"""Intro logo scene for Andrew H. Volk branding.

Preview:
    python -m manim -pql scenes/intro_logo.py IntroLogo
Final:
    python -m manim -pqh scenes/intro_logo.py IntroLogo
"""

import numpy as np
from manim import (
    Axes,
    BLUE,
    BLUE_B,
    BLUE_D,
    BOLD,
    Create,
    DOWN,
    Dot,
    FadeIn,
    FadeOut,
    GRAY_A,
    ITALIC,
    LaggedStart,
    Line,
    MoveAlongPath,
    ORIGIN,
    PURPLE,
    RED,
    RIGHT,
    ReplacementTransform,
    Scene,
    TEAL_C,
    Text,
    UP,
    VGroup,
    WHITE,
    Write,
    YELLOW,
    YELLOW_D,
    ValueTracker,
    always_redraw,
    linear,
    smooth,
    there_and_back,
)


class IntroLogo(Scene):
    """Branded intro animation.

    Set ``INTRO_MODE`` to ``"short"`` to reduce motto-cycle runtime.
    """

    INTRO_MODE = "full"
    FONT_FAMILY = "DejaVu Sans"

    BRAND = {
        "name": "Andrew H. Volk",
        "title": "Assistant Professor of Mathematics and Physics",
        "website": "https://andrewhvolk.github.io/",
        "mottos": [
            "Learn Mathematics",
            "Learn Physics",
            "Learn Engineering",
            "Learn Anything",
            "Learn Abundantly",
        ],
    }

    TIMING = {
        "phase_engineering": 1.0,
        "phase_kinematics": 1.2,
        "phase_statistics": 1.2,
        "move_projectile": 1.5,
        "swipe_intro": 0.5,
        "swipe_move": 1.5,
        "logo_transform": 1.2,
        "name_in": 0.8,
        "title_in": 0.8,
        "motto_in": 0.6,
        "motto_step": 0.4,
        "motto_final": 0.8,
        "website_in": 0.8,
        "pulse": 1.5,
        "wait_small": 0.2,
        "wait_medium": 0.5,
        "wait_end": 2.0,
    }

    def construct(self):
        palette = self._palette()
        engineering = self._build_engineering_elements(palette)
        stats_kinematics = self._build_axes_and_curves(palette)
        logo_and_text = self._build_logo_and_text(palette)

        self._animate_phase_engineering(engineering)
        self._animate_phase_kinematics(engineering, stats_kinematics)
        self._animate_phase_statistics(stats_kinematics, logo_and_text)
        self._animate_phase_logo_and_text(logo_and_text)

    def _palette(self):
        return {
            "eng_line": BLUE_D,
            "kin_path": YELLOW_D,
            "stat_curve": TEAL_C,
            "math": BLUE,
            "phys": YELLOW,
            "engineer": RED,
            "any": PURPLE,
            "abundant": TEAL_C,
        }

    def _brand(self):
        return self.BRAND

    def _timing(self):
        return self.TIMING

    def _text(self, value, **kwargs):
        return Text(value, font=self.FONT_FAMILY, **kwargs)

    def _build_engineering_elements(self, palette):
        nodes = [
            [-2, -1, 0],
            [0, -1, 0],
            [2, -1, 0],
            [-1, 0.5, 0],
            [1, 0.5, 0],
        ]
        edges = [(0, 1), (1, 2), (3, 4), (0, 3), (1, 3), (1, 4), (2, 4)]

        dots = VGroup(*[Dot(point, color=WHITE, radius=0.08) for point in nodes])
        lines = VGroup(
            *[Line(nodes[i], nodes[j], color=palette["eng_line"], stroke_width=3) for i, j in edges]
        )
        return {"dots": dots, "lines": lines}

    def _build_axes_and_curves(self, palette):
        ax = Axes(x_range=[-3, 3, 1], y_range=[-1, 2, 1]).set_opacity(0)

        def kinematics_curve(x: float) -> float:
            return -0.4 * x**2 + 1.2

        def gaussian_curve(x: float) -> float:
            return 1.5 * np.exp(-(x**2))

        parabola = ax.plot(kinematics_curve, color=palette["kin_path"], stroke_width=4)
        projectile = Dot(color=WHITE).move_to(ax.c2p(-3, kinematics_curve(-3)))
        bell_curve = ax.plot(gaussian_curve, color=palette["stat_curve"], stroke_width=4)

        z_tracker = ValueTracker(0)

        def build_swiping_line():
            z_val = z_tracker.get_value()
            return ax.get_vertical_line(
                ax.c2p(z_val, gaussian_curve(z_val)),
                color=WHITE,
                stroke_width=2,
            )

        def build_swiping_area():
            return ax.get_area(
                bell_curve,
                x_range=[z_tracker.get_value(), 3],
                color=palette["stat_curve"],
                opacity=0.5,
            )

        swiping_line = always_redraw(build_swiping_line)
        swiping_area = always_redraw(build_swiping_area)

        return {
            "parabola": parabola,
            "projectile": projectile,
            "bell_curve": bell_curve,
            "z_tracker": z_tracker,
            "swiping_line": swiping_line,
            "swiping_area": swiping_area,
        }

    def _build_logo_and_text(self, palette):
        brand = self._brand()

        logo_color = palette["abundant"]
        letter_a = self._text("A", font_size=90, weight=BOLD, color=logo_color)
        letter_h = self._text("H", font_size=90, weight=BOLD, color=logo_color)
        letter_v = self._text("V", font_size=120, weight=BOLD, color=logo_color)

        top_row = VGroup(letter_a, letter_h).arrange(RIGHT, buff=0.4)
        final_logo = VGroup(top_row, letter_v).arrange(DOWN, buff=0.1).scale(0.55)

        name = self._text(brand["name"], font_size=48, weight=BOLD)
        title = self._text(brand["title"], font_size=24, color=GRAY_A)
        website = self._text(brand["website"], font_size=20, color=BLUE_B)

        motto_data = [
            (brand["mottos"][0], palette["math"]),
            (brand["mottos"][1], palette["phys"]),
            (brand["mottos"][2], palette["engineer"]),
            (brand["mottos"][3], palette["any"]),
            (brand["mottos"][4], palette["abundant"]),
        ]

        mottos = [self._text(text, font_size=32, slant=ITALIC, color=color) for text, color in motto_data]
        final_motto = mottos[-1]

        text_group = VGroup(name, title, final_motto, website).arrange(DOWN, buff=0.3)
        full_layout = VGroup(final_logo, text_group).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        final_logo.move_to(full_layout[0])
        text_group.move_to(full_layout[1])
        for motto in mottos[:-1]:
            motto.move_to(final_motto)

        return {
            "final_logo": final_logo,
            "name": name,
            "title": title,
            "website": website,
            "mottos": mottos,
            "final_motto": final_motto,
        }

    def _animate_phase_engineering(self, engineering):
        timing = self._timing()

        dots = engineering["dots"]
        lines = engineering["lines"]

        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.1),
            run_time=timing["phase_engineering"],
        )
        self.play(
            LaggedStart(*[Create(line) for line in lines], lag_ratio=0.1),
            run_time=timing["phase_engineering"],
        )
        self.wait(timing["wait_medium"])

    def _animate_phase_kinematics(self, engineering, stats_kinematics):
        timing = self._timing()

        lines = engineering["lines"]
        dots = engineering["dots"]
        parabola = stats_kinematics["parabola"]
        projectile = stats_kinematics["projectile"]

        self.play(
            ReplacementTransform(lines, parabola),
            ReplacementTransform(dots, VGroup(projectile)),
            run_time=timing["phase_kinematics"],
        )
        self.play(MoveAlongPath(projectile, parabola), run_time=timing["move_projectile"], rate_func=linear)
        self.wait(timing["wait_medium"])

    def _animate_phase_statistics(self, stats_kinematics, logo_and_text):
        timing = self._timing()

        parabola = stats_kinematics["parabola"]
        projectile = stats_kinematics["projectile"]
        bell_curve = stats_kinematics["bell_curve"]
        swiping_line = stats_kinematics["swiping_line"]
        swiping_area = stats_kinematics["swiping_area"]
        z_tracker = stats_kinematics["z_tracker"]
        final_logo = logo_and_text["final_logo"]

        self.play(
            ReplacementTransform(parabola, bell_curve),
            FadeOut(projectile),
            run_time=timing["phase_statistics"],
        )

        self.play(Create(swiping_line), FadeIn(swiping_area), run_time=timing["swipe_intro"])
        self.play(z_tracker.animate.set_value(1.65), run_time=timing["swipe_move"], rate_func=smooth)
        self.wait(timing["wait_medium"])

        self.play(FadeOut(swiping_line), FadeOut(swiping_area), run_time=timing["swipe_intro"])
        self.play(ReplacementTransform(bell_curve, final_logo), run_time=timing["logo_transform"])

    def _animate_phase_logo_and_text(self, logo_and_text):
        timing = self._timing()

        final_logo = logo_and_text["final_logo"]
        name = logo_and_text["name"]
        title = logo_and_text["title"]
        website = logo_and_text["website"]
        mottos = logo_and_text["mottos"]
        final_motto = logo_and_text["final_motto"]

        self.play(FadeIn(name, shift=UP * 0.5), run_time=timing["name_in"])
        self.play(Write(title), run_time=timing["title_in"])

        active_motto = mottos[0]
        self.play(FadeIn(active_motto, scale=0.8), run_time=timing["motto_in"])
        self.wait(timing["wait_small"])

        if self.INTRO_MODE == "full":
            for next_motto in mottos[1:-1]:
                self.play(ReplacementTransform(active_motto, next_motto), run_time=timing["motto_step"])
                active_motto = next_motto
                self.wait(timing["wait_small"])

        self.play(ReplacementTransform(active_motto, final_motto), run_time=timing["motto_final"])
        self.play(Write(website), run_time=timing["website_in"])

        self.play(
            final_logo.animate.scale(1.05).set_color(YELLOW_D),
            final_motto.animate.scale(1.05).set_color(YELLOW_D),
            rate_func=there_and_back,
            run_time=timing["pulse"],
        )
        self.wait(timing["wait_end"])

        self.play(
            FadeOut(final_logo),
            FadeOut(name),
            FadeOut(title),
            FadeOut(website),
            FadeOut(final_motto),
        )
