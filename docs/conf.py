# Configuration Sphinx — Cours HTML & CSS CESAG
# ===============================================

import os
import sys

# -- Infos du projet ----------------------------------------------------------
project = "Introduction au Développement Web — HTML & CSS"
copyright = "2026, CESAG — Dakar"
author = "CESAG — Licence 1 MIAGE"
release = "2025-2026"
language = "fr"

# -- Extensions ---------------------------------------------------------------
extensions = [
    "myst_parser",          # Markdown avec extensions
]

myst_enable_extensions = [
    "colon_fence",          # Blocs :::{admonition} style
    "deflist",              # Listes de définitions
    "tasklist",             # Cases à cocher
    "html_image",           # Images HTML dans Markdown
]

# -- Fichiers sources ---------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Thème HTML ---------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "logo_only": False,
    "navigation_depth": 4,
    "style_nav_header_background": "#1A7A2A",
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

html_title = "Cours HTML & CSS — CESAG L1 MIAGE"
html_short_title = "HTML & CSS CESAG"

# Métadonnées
html_meta = {
    "description": "Support de cours Introduction au Développement Web avec HTML et CSS — Licence 1 MIAGE, CESAG Dakar",
    "keywords": "HTML, CSS, développement web, CESAG, MIAGE, Dakar",
    "authors": "Lionnel Patrick DOOKO - Model Technologie"
}
