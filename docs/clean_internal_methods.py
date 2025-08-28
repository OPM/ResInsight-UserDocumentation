#!/usr/bin/env python3
"""
Script to remove _internal method references from generated RST files.
Run this after automodapi generates the RST files but before building HTML.
"""

import os
import re
import glob

def clean_rst_file(file_path):
    """Remove _internal method references from a single RST file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
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
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned: {file_path}")
        return True
    else:
        print(f"No changes needed: {file_path}")
        return False

def clean_all_rst_files(api_dir):
    """Clean all RST files in the API directory."""
    rst_pattern = os.path.join(api_dir, "*.rst")
    rst_files = glob.glob(rst_pattern)
    
    if not rst_files:
        print(f"No RST files found in {api_dir}")
        return 0
    
    cleaned_count = 0
    for rst_file in rst_files:
        if clean_rst_file(rst_file):
            cleaned_count += 1
    
    print(f"\nProcessed {len(rst_files)} files, cleaned {cleaned_count} files")
    return cleaned_count

if __name__ == "__main__":
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    api_dir = os.path.join(script_dir, "source", "api")
    
    print(f"Cleaning _internal method references from RST files in: {api_dir}")
    
    if not os.path.exists(api_dir):
        print(f"Error: API directory not found: {api_dir}")
        exit(1)
    
    cleaned_count = clean_all_rst_files(api_dir)
    
    if cleaned_count > 0:
        print(f"\nSuccessfully cleaned {cleaned_count} RST files.")
        print("You can now build the documentation with: sphinx-build -b html source build")
    else:
        print("\nNo RST files needed cleaning.")