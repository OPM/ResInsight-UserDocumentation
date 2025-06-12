import os
from pathlib import Path

# This script is used to create RST files for all Python examples
# It will create individual RST files for each subfolder in PythonExamples
# and a main index file that references all subfolders

path_examples = Path("../rips/PythonExamples")

def create_rst_for_folder(folder_path, relative_to_examples):
    """Create an RST file for a specific folder containing Python examples."""
    
    # Get all Python files in this folder
    python_files = sorted([f for f in folder_path.iterdir() 
                          if f.is_file() and f.suffix == '.py'])
    
    if not python_files:
        return None
    
    folder_name = folder_path.name
    rst_filename = f"PythonExamples_{folder_name}.rst"
    
    # Create heading from folder name
    heading = folder_name.replace("_", " ").title()
    
    txt = ""
    txt += ".. \n   This file was created using the script in docs/source/create_python_examples.py\n\n"
    txt += f"{heading}\n"
    txt += "=" * len(heading) + "\n\n"
    txt += f"This page shows Python examples from the **{folder_name}** folder.\n\n"
    
    for py_file in python_files:
        reference = py_file.stem  # filename without extension
        example_heading = reference.replace("_", " ").title()
        
        txt += f".. _{folder_name}_{reference}:\n\n"
        txt += example_heading + "\n"
        txt += "-" * len(example_heading) + "\n\n"
        
        # Build path relative to the source directory
        relative_path = path_examples / relative_to_examples / py_file.name
        txt += f".. literalinclude:: {relative_path}\n"
        txt += "   :language: python\n"
        txt += "   :linenos:\n"
        txt += "   :caption: " + py_file.name + "\n\n"
    
    # Write the RST file
    with open(rst_filename, "w") as f:
        f.write(txt)
    
    print(f"Created {rst_filename}")
    return rst_filename, heading

def create_general_examples_page():
    """Create a separate page for root-level examples."""
    
    root_files = sorted([f for f in path_examples.iterdir() 
                        if f.is_file() and f.suffix == '.py'])
    
    if not root_files:
        return None
    
    txt = ""
    txt += ".. \n   This file was created using the script in docs/source/create_python_examples.py\n\n"
    txt += "General Examples\n"
    txt += "================\n\n"
    txt += "This page shows Python examples from the root directory.\n\n"
    
    for py_file in root_files:
        reference = py_file.stem
        example_heading = reference.replace("_", " ").title()
        
        txt += f".. _general_{reference}:\n\n"
        txt += example_heading + "\n"
        txt += "-" * len(example_heading) + "\n\n"
       
        relative_path = path_examples / py_file.name
        txt += f".. literalinclude:: {relative_path}\n"
        txt += "   :language: python\n"
        txt += "   :linenos:\n"
        txt += "   :caption: " + py_file.name + "\n\n"
    
    # Write the general examples file
    with open("PythonExamples_General.rst", "w") as f:
        f.write(txt)
    
    print("Created PythonExamples_General.rst")
    return "PythonExamples_General.rst", "General Examples"

def create_main_index():
    """Create the main PythonExamples.rst index file."""
    
    # Get all subdirectories
    subdirs = sorted([d for d in path_examples.iterdir() 
                     if d.is_dir() and not d.name.startswith('.')])
    
    # Also handle files in the root directory
    root_files = sorted([f for f in path_examples.iterdir() 
                        if f.is_file() and f.suffix == '.py'])
    
    txt = ""
    txt += ".. \n   This file was created using the script in docs/source/create_python_examples.py\n\n"
    txt += "Python Examples\n"
    txt += "===============\n\n"
    txt += "This page provides access to all Python examples organized by category.\n\n"
   
   
    # Create toctree for subdirectories and root files
    has_content = bool(subdirs) or bool(root_files)
    
    if has_content:
        txt += ".. toctree::\n"
        txt += "   :maxdepth: 2\n"
        txt += "   :caption: Example Categories:\n\n"
        
        # Add subdirectories to toctree
        for subdir in subdirs:
            rst_file = f"PythonExamples_{subdir.name}"
            txt += f"   {rst_file}\n"
        
        # If there are root files, add general examples page
        if root_files:
            txt += "   PythonExamples_General\n"
        
        txt += "\n"
    
    # Write the main index file
    with open("PythonExamples.rst", "w") as f:
        f.write(txt)
    
    print("Created PythonExamples.rst (main index)")

def main():
    """Main function to process all folders and create RST files."""
    
    if not path_examples.exists():
        print(f"Error: Examples directory not found: {path_examples}")
        return
    
    print(f"Processing examples from: {path_examples}")
    
    # Get all subdirectories
    subdirs = [d for d in path_examples.iterdir() 
               if d.is_dir() and not d.name.startswith('.')]
    
    created_files = []
    
    # Process each subdirectory
    for subdir in subdirs:
        relative_path = subdir.name
        result = create_rst_for_folder(subdir, relative_path)
        if result:
            created_files.append(result)
    
    # Create a separate page for root-level files
    general_result = create_general_examples_page()
    if general_result:
        created_files.append(general_result)
    
    # Create the main index file
    create_main_index()
    
    print(f"\nCompleted! Created {len(created_files)} category files plus main index.")
    print("Created files:")
    print("- PythonExamples.rst (main index)")
    for filename, heading in created_files:
        print(f"- {filename} ({heading})")
    
if __name__ == "__main__":
    main()