# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
# TODO: We need to get access to the generated files in /ApplicationCode/GrpcInterface/Python/rips/generated
# It is not clear how we can organize these files for readthedocs
# sys.path.insert(0, os.path.abspath('../../ApplicationCode/GrpcInterface/Python'))


# -- Configuration of base URL -----------------------------------------------------
# https://about.readthedocs.com/blog/2024/07/addons-by-default/

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# -- Project information -----------------------------------------------------

project = 'ResInsight Python API - rips'
copyright = 'Ceetron Solutions AS'
author = 'Ceetron Solutions AS'

# The full version, including alpha/beta/rc tags
release = '2020.10'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon', 'm2r2', 'sphinx_automodapi.automodapi'
]

master_doc = 'index'

napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build/*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_logo = "images/ResInsightCroppedIconPicture.png"

html_theme_options = {
    'style_nav_header_background': '#505050',
}
smartquotes = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_style = 'css/custom.css'

# -- Extension configuration -------------------------------------------------
