#!/usr/bin/env python3
"""
Build script for ResInsight documentation that automatically cleans _internal methods.

This script:
1. Activates the virtual environment
2. Runs sphinx-build to generate RST files (which triggers automodapi)
3. Cleans _internal method references from generated RST files
4. Runs sphinx-build again to generate clean HTML
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description, cwd=None):
    """Run a command and handle errors."""
    print(f"\n=== {description} ===")
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    
    try:
        if isinstance(cmd, str):
            result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                                  capture_output=True, text=True)
        else:
            result = subprocess.run(cmd, cwd=cwd, check=True, 
                                  capture_output=True, text=True)
        
        if result.stdout:
            print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def main():
    # Get script directory
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Paths
    venv_activate = script_dir / "venv" / "Scripts" / "activate"
    source_dir = script_dir / "source"
    build_dir = script_dir / "build"
    clean_script = script_dir / "clean_internal_methods.py"
    
    print(f"Working directory: {script_dir}")
    print(f"Virtual environment: {venv_activate}")
    
    # Check if virtual environment exists
    if not venv_activate.exists():
        print(f"Error: Virtual environment not found at {venv_activate}")
        print("Please create a virtual environment first with: py -m venv venv")
        return False
    
    # Step 1: Clean build directory
    if build_dir.exists():
        print(f"\n=== Cleaning build directory ===")
        run_command(f'rmdir /s /q "{build_dir}"', "Remove build directory")
    
    # Step 2: First build (generates RST files via automodapi)
    # Use a minimal build that just generates the RST files without completing HTML
    sphinx_cmd = f'"{venv_activate}" && sphinx-build -b html "{source_dir}" "{build_dir}" -W --keep-going || echo "First build completed (expected warnings/errors)"'
    
    if not run_command(sphinx_cmd, "Initial build to generate RST files"):
        print("Warning: Initial build had issues, but continuing...")
    
    # Step 3: Clean _internal methods from generated RST files
    clean_cmd = f'"{venv_activate}" && python "{clean_script}"'
    
    if not run_command(clean_cmd, "Clean _internal methods from RST files"):
        print("Error: Failed to clean RST files")
        return False
    
    # Step 4: Final clean build
    final_cmd = f'"{venv_activate}" && sphinx-build -b html "{source_dir}" "{build_dir}"'
    
    if not run_command(final_cmd, "Final documentation build"):
        print("Error: Failed to build final documentation")
        return False
    
    print(f"\n🎉 Documentation build completed successfully!")
    print(f"📁 Output directory: {build_dir}")
    print(f"🌐 Open index.html in your browser: {build_dir / 'index.html'}")
    
    # Verify no _internal methods remain
    print(f"\n=== Verification ===")
    verify_cmd = f'findstr /R "_internal" "{build_dir}\\*.html" | findstr /c:" " > nul && echo "WARNING: _internal methods still found!" || echo "✅ No _internal methods found in HTML files"'
    run_command(verify_cmd, "Verify no _internal methods remain")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)