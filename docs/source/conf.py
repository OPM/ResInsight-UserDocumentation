# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import sys

# Add paths for autodoc modules
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../rips/generated'))
# TODO: We need to get access to the generated files in /ApplicationCode/GrpcInterface/Python/rips/generated
# It is not clear how we can organize these files for readthedocs
# sys.path.insert(0, os.path.abspath('../../ApplicationCode/GrpcInterface/Python'))

# -- Project information -----------------------------------------------------

project = 'ResInsight Python API - rips'
copyright = 'Ceetron Solutions AS'
author = 'Ceetron Solutions AS'

# Import version information from RiaVersionInfo
try:
    import RiaVersionInfo
    release = f"{RiaVersionInfo.RESINSIGHT_MAJOR_VERSION}.{RiaVersionInfo.RESINSIGHT_MINOR_VERSION}.{RiaVersionInfo.RESINSIGHT_PATCH_VERSION}"
    version = f"{RiaVersionInfo.RESINSIGHT_MAJOR_VERSION}.{RiaVersionInfo.RESINSIGHT_MINOR_VERSION}"
except ImportError:
    # Fallback version if RiaVersionInfo is not available
    release = '2020.10'
    version = '2020.10'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'm2r2',
    'sphinx_automodapi.automodapi'
]

master_doc = 'index'
napoleon_google_docstring = True
smartquotes = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns to ignore when looking for source files
exclude_patterns = ['build/*']

# -- Read the Docs configuration ---------------------------------------------
# https://about.readthedocs.com/blog/2024/07/addons-by-default/

# Define the canonical URL if using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
    html_context["current_version"] = release

# -- HTML output options -----------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_logo = "images/ResInsightCroppedIconPicture.png"

html_theme_options = {
    'style_nav_header_background': '#505050',
    'display_version': True,  # Show version in sidebar
}

# Add paths that contain custom static files (CSS, etc.)
html_static_path = ['_static']
html_style = 'css/custom.css'
