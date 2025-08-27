"""
Sphinx extension to make literalinclude content searchable.

This extension processes literalinclude directives and adds their content
to the search index so Python examples become searchable.
"""

import os
from docutils import nodes
from sphinx.directives.code import LiteralInclude
from sphinx.util import logging

logger = logging.getLogger(__name__)


class SearchableLiteralInclude(LiteralInclude):
    """
    Enhanced literalinclude directive that adds content to search index.
    """
    
    def run(self):
        # Get the normal literalinclude result
        result = super().run()
        
        # Add searchable content for the included file
        try:
            # Get the environment and config
            env = self.state.document.settings.env
            
            if self.arguments:
                # Resolve the filename
                filename = self.arguments[0]
                if not os.path.isabs(filename):
                    # Make path relative to source directory
                    filename = os.path.join(env.srcdir, filename)
                
                # Read the file content
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Create a text node that will be indexed but not displayed
                    # We'll make this a comment node so it doesn't render
                    search_content = nodes.comment()
                    
                    # Extract meaningful content for search indexing
                    searchable_text = self._extract_searchable_content(content)
                    
                    # Add the content as text that can be indexed
                    if searchable_text:
                        search_content += nodes.Text(searchable_text)
                        result.insert(0, search_content)
                        
                        logger.debug(f"Added searchable content for {filename}")
                    
        except Exception as e:
            # Don't break the build if something goes wrong
            logger.warning(f"Could not add searchable content for literalinclude: {e}")
            
        return result
    
    def _extract_searchable_content(self, content):
        """Extract searchable content from Python code."""
        lines = content.split('\n')
        searchable_parts = []
        
        # Extract header comments (usually the first few lines)
        for line in lines[:10]:
            line = line.strip()
            if line.startswith('#') and len(line) > 1:
                comment = line.lstrip('#').strip()
                if comment and not comment.startswith('!'):  # Skip shebang
                    searchable_parts.append(comment)
        
        # Extract import statements to understand what the script does
        for line in lines:
            line = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                searchable_parts.append(line)
        
        # Extract function definitions
        for line in lines:
            line = line.strip()
            if line.startswith('def '):
                # Extract function name and make it searchable
                func_name = line.split('(')[0].replace('def ', '').replace('_', ' ')
                searchable_parts.append(f"function {func_name}")
        
        # Extract string literals that might contain descriptions
        import re
        string_matches = re.findall(r'["\']([^"\']{10,})["\']', content)
        for match in string_matches[:3]:  # Limit to first 3 long strings
            # Skip paths, URLs, etc.
            if not any(char in match for char in ['/', '\\', '@', 'http']):
                searchable_parts.append(match)
        
        # Add Python API specific terms
        if 'rips' in content:
            searchable_parts.append('ResInsight Python API scripting')
        if 'Instance.find()' in content:
            searchable_parts.append('connect to ResInsight instance')
        if '.cases()' in content:
            searchable_parts.append('get cases from project')
        if '.project' in content:
            searchable_parts.append('ResInsight project access')
        
        return ' '.join(searchable_parts)


def setup(app):
    """Set up the extension."""
    
    # Replace the standard literalinclude directive with our enhanced version
    app.add_directive('literalinclude', SearchableLiteralInclude, override=True)
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }