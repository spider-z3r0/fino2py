# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('..'))


project = 'fino2py'
copyright = "2024, Kev O'Malley"
author = "Kev O'Malley"
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.autosummary", "sphinx.ext.mathjax", "sphinx.ext.githubpages"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']



autodoc_mock_imports = ['pandas',]

# Specify the source directory for Python files
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__, __doc__',
    'undoc-members': True,
    'private-members': True,
}