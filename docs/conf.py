# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'package'
copyright = '2023, Full name'
author = 'Full name'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',   # Include documentation from docstrings
    'sphinx.ext.viewcode',  # Add links to the Python source code
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.mathjax',   # Render math
    'sphinx_book_theme',    # Theme (needed here for ReadTheDocs)
]

# LaTeX math
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    'colon_fence',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'Python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'The Package Documentation'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
