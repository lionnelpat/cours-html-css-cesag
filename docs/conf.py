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
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "light_css_variables": {
        # Couleurs CESAG
        "color-brand-primary": "#1A7A2A",
        "color-brand-content": "#1A7A2A",
        # Sidebar claire
        "color-sidebar-background": "#f4f9f4",
        "color-sidebar-background-border": "#c8dfc8",
        "color-sidebar-caption-text": "#1A7A2A",
        "color-sidebar-link-text": "#2c2c2c",
        "color-sidebar-link-text--top-level": "#111111",
        "color-sidebar-item-background--hover": "#dceede",
        "color-sidebar-item-background--current": "#E8420A",
        "color-sidebar-item-expander-background": "transparent",
        "color-sidebar-item-expander-background--hover": "#dceede",
        # Contenu principal blanc
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f7faf7",
        "color-background-border": "#dde8dd",
        "color-foreground-primary": "#1c1c1c",
        "color-foreground-secondary": "#444444",
        "color-foreground-muted": "#666666",
        # Code
        "color-code-background": "#f4f8f4",
        "color-code-foreground": "#1c2e1c",
        # Liens
        "color-link": "#1A7A2A",
        "color-link--hover": "#E8420A",
        "color-link-underline": "transparent",
        "color-link-underline--hover": "#E8420A",
        # Annonces / highlights
        "color-highlighted-background": "#fff5ef",
        "color-highlighted-text": "#2e1a10",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}

html_title = "Cours HTML & CSS — CESAG L1 MIAGE"
html_short_title = "HTML & CSS CESAG"

# Métadonnées
html_meta = {
    "description": "Support de cours Introduction au Développement Web avec HTML et CSS — Licence 1 MIAGE, CESAG Dakar",
    "keywords": "HTML, CSS, développement web, CESAG, MIAGE, Dakar",
    "author": "PATRICK LIONNEL DOOKO - Model Technologie"
}
