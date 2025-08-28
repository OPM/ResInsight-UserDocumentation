"""
Sphinx extension to automatically clean _internal method references from generated RST files.

This extension hooks into the Sphinx build process to clean RST files after
automodapi generates them but before the final HTML is built.
"""

import os
import re
import glob
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

def clean_rst_file(file_path):
    """Remove _internal method references from a single RST file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        logger.warning(f"Could not read {file_path}: {e}")
        return False
    
    original_content = content
    
    # Remove lines containing _internal in autosummary sections
    # Pattern: "      ~ClassName.method_name_internal"
    content = re.sub(r'^\s*~\w+\.\w*_internal\w*.*$\n', '', content, flags=re.MULTILINE)
    
    # Remove automethod directives for _internal methods
    # Pattern: "   .. automethod:: method_name_internal"
    content = re.sub(r'^\s*\.\.\s+automethod::\s+\w*_internal\w*.*$\n', '', content, flags=re.MULTILINE)
    
    # Clean up any empty lines that might be left behind (max 2 consecutive empty lines)
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # Only write back if content changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Cleaned _internal methods from: {file_path}")
            return True
        except Exception as e:
            logger.warning(f"Could not write {file_path}: {e}")
            return False
    else:
        logger.debug(f"No _internal methods found in: {file_path}")
        return False

def clean_all_rst_files(source_dir):
    """Clean all RST files in the source directory and subdirectories."""
    api_dir = os.path.join(source_dir, "api")
    
    if not os.path.exists(api_dir):
        logger.info("API directory not found, skipping _internal method cleaning")
        return 0
    
    rst_pattern = os.path.join(api_dir, "*.rst")
    rst_files = glob.glob(rst_pattern)
    
    if not rst_files:
        logger.info(f"No RST files found in {api_dir}")
        return 0
    
    cleaned_count = 0
    for rst_file in rst_files:
        if clean_rst_file(rst_file):
            cleaned_count += 1
    
    logger.info(f"Processed {len(rst_files)} RST files, cleaned {cleaned_count} files")
    return cleaned_count

def on_build_finished(app, exception):
    """
    Event handler called when the build is finished.
    This is too late - RST files are already processed into HTML.
    """
    pass

def on_source_read(app, docname, source):
    """
    Event handler called when a source file is read.
    This allows us to modify the RST content before it's processed.
    """
    # Only process files in the api directory that contain _internal
    if docname.startswith('api/') and '_internal' in source[0]:
        logger.info(f"Cleaning _internal methods from docname: {docname}")
        
        content = source[0]
        original_content = content
        
        # Remove lines containing _internal in autosummary sections
        content = re.sub(r'^\s*~\w+\.\w*_internal\w*.*$\n', '', content, flags=re.MULTILINE)
        
        # Remove automethod directives for _internal methods
        content = re.sub(r'^\s*\.\.\s+automethod::\s+\w*_internal\w*.*$\n', '', content, flags=re.MULTILINE)
        
        # Clean up any empty lines that might be left behind
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        if content != original_content:
            source[0] = content
            logger.info(f"Cleaned _internal methods from: {docname}")

def setup(app: Sphinx):
    """Setup the Sphinx extension."""
    # Connect to the source-read event to clean RST content as it's read
    app.connect('source-read', on_source_read)
    
    logger.info("clean_internal_methods extension loaded")
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }