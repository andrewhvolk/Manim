"""Global project configuration for Manim explainer scenes.

Import this module once (typically from `scenes/core/base_scene.py`) so
configuration is applied consistently across all scenes.
"""

from __future__ import annotations

from pathlib import Path

from manim import TexTemplate, config

# ==========================================
# 1) PROJECT COLOR PALETTE
# ==========================================
C_BACKGROUND = "#1B1F3B"
C_TEXT = "#E8E8E8"
C_DEF = "#5DADE2"
C_EX = "#F5B041"
C_WARN = "#E74C3C"
C_ACCENT = "#58D68D"

# Optional semantic aliases for scene code readability
BRAND_BLUE = C_DEF
BRAND_ACCENT = C_ACCENT

# ==========================================
# 2) LATEX TEMPLATE
# ==========================================
my_template = TexTemplate()
my_template.add_to_preamble(r"\\usepackage{amsmath}")
my_template.add_to_preamble(r"\\usepackage{amssymb}")

# ==========================================
# 3) GLOBAL MANIM CONFIGURATION
# ==========================================
config.background_color = C_BACKGROUND
config.font = "CMU Serif"
config.tex_template = my_template

# Keep generated media in the repository-level media directory.
_REPO_ROOT = Path(__file__).resolve().parents[2]
config.media_dir = str(_REPO_ROOT / "media")
