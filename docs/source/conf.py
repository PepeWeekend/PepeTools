import os
import sys

# ルートディレクトリをパスに追加
# この操作にて、ルートディレクトリ直下にある、〇〇.pyが読み込まれます。
root_path = os.path.abspath('../..')  # ルートディレクトリをsys.pathに追加
sys.path.append(root_path)  # ルートディレクトリ以下のすべてのサブディレクトリをsys.pathに追加
for dirpath, dirnames, filenames in os.walk(root_path):
    sys.path.append(dirpath)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PepeTools'
copyright = '2024, PepeWeekend'
author = 'PepeWeekend'
release = 'TimeS!'


# -- Path setup --------------------------------------------------------------
print(sys.path)  # コメント解除


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]
# extensions = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Appenc User Settings ----------------------------------------------------
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
