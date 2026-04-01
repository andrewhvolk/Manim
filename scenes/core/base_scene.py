"""Base scene class shared by all explainer episodes."""

from manim import Scene

# Ensure global configuration is applied before scene execution.
import scenes.core.project_globals as pg


class MathVideoScene(Scene):
    """Universal base scene for the explainer video series."""

    globals = pg

    def setup(self):
        super().setup()
        # Shared overlays/hooks can be added here.

    def tear_down(self):
        super().tear_down()
        # Shared teardown/cleanup hooks can be added here.
