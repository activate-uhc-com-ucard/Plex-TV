# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any directories that contain custom modules here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Set Up Plex with plex.tv/link'
copyright = '2025, Plex Inc.'
author = 'Plex Inc.'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Set Up Plex – Activate via plex.tv/link"

# Optional short title (e.g., for navbar)
html_short_title = "Plex Setup Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Uncomment and choose a theme
# html_theme = 'sphinx_rtd_theme'  # Or 'alabaster', 'furo', etc.

# Hide "View page source" link in the HTML output
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files (use with caution)
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you use custom CSS/images

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
