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
sys.path.insert(0, os.path.abspath('_ext'))
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
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'm2r2',
    'hide_grpc_params',
    'clean_internal_methods',
    'searchable_literalinclude'
]

# Generate per-class stub pages for the autosummary tables in
# GeneratedClasses.rst. Stubs use the template in _templates/autosummary/.
autosummary_generate = True

# Enable search functionality
html_search_language = 'en'
html_search_options = {'type': 'default'}

# Include source files in search
html_copy_source = True
html_show_sourcelink = True

master_doc = 'index'
napoleon_google_docstring = True
smartquotes = False

# Keep Python objects (classes, methods) out of the page table of
# contents. Each autosummary stub page is titled after its class, so the
# class object would otherwise show up as a redundant leaf node beneath
# the page in the navigation sidebar.
toc_object_entries = False

# Clean up autosummary generated stub files in source after build to make sure
# we get a full rebuild next time.
def cleanup_autosummary_files(app, exception):
    """Remove autosummary generated stub files from source directory after build."""
    import shutil
    api_dir = os.path.join(app.srcdir, 'api')
    if os.path.exists(api_dir):
        shutil.rmtree(api_dir)

def skip_recursive_type_aliases(app, what, name, obj, skip, options):
    """Exclude rips.PdmObjectBase's mutually-recursive typing aliases.

    PdmObjectBase defines ``Value = Union[..., "ValueArray"]`` and
    ``ValueArray = List[Value]``. autodoc recurses through these aliases
    without terminating, which hangs the build. They are internal
    annotation helpers, not part of the public API.
    """
    if name in ('Value', 'ValueArray'):
        return True
    return skip

def setup(app):
    app.connect('build-finished', cleanup_autosummary_files)
    app.connect('autodoc-skip-member', skip_recursive_type_aliases)

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
