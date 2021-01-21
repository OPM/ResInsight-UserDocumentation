from os import listdir

# This script is used to create a RST file for all Python examples
# Content of the file 'PythonExamples.rst' will be overwritten
# The script will create a title from the file name, and add a reference to the source code using literalinclude

path_examples = "../rips/PythonExamples"
file_names = listdir(path_examples)

txt =""
txt += ".. \n   This file was created using the script in docs/source/create_python_examples.py\n\n"
txt +="Python Examples\n"
txt +="---------------\n\n"
txt +="This pages is created based on the content in the **PythonExamples** folder located inside the **rips** module, made available online for convenience.\n\n"

for file_name in file_names:
    reference = file_name.replace(".py", "")
    heading = reference.replace("_", " ").title()
    txt += ".. _" + reference + ":\n\n"
    txt += heading
    txt += "\n"
    txt += "===================================\n"
    txt += ".. literalinclude:: ../rips/PythonExamples/"
    txt += file_name
    txt += "\n\n"

#print (txt)
f = open("PythonExamples.rst", "w")
f.write(txt)
