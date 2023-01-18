# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '2023_Robot'
copyright = '2023, Me'
author = 'Me'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'javasphinx',
    # 'sphinx.ext.todo',
    'sphinxcontrib.mermaid',
]

mermaid_cmd = './node_modules/.bin/mmdc'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'
html_static_path = ['_static']

# push test, after changing permission
# push test, after changing github pages