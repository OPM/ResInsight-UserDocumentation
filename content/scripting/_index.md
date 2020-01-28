+++
title = "Scripting"
published = true
weight = 70
+++

![]({{< relref "" >}}images/scripting/ExecuteOctaveScriptOnSelectedCases.png)

ResInsight provides powerful and flexible mechanisms for post-processing of results and automation by its scripting interfaces:

- Command line interface and Command files
- Python interface
- Octave interface

## Command Line Interface and Command files
ResInsight supports several [command line parameters] ({{< ref "CommandLineInterface.md" >}})
for automation via shell scripts. 
By gathering commands into a [Command file]({{< ref "CommandFile.md" >}}),
you may run a sequence of commands by supplying the command file as a 
[command line parameter]({{< ref "CommandLineInterface.md" >}}). 

## Python Interface
ResInsight offers a [Python Interface] ({{< ref "pythonrips.md" >}})
which allows you to interact with a running ResInsight instance from a Python script. 
This allows using the powerful Python language, numerical libraries, and other support modules in conjunction with ResInsight. The Python client package is compatible with **Python 3**.

For examples on how to use Python, see [Examples]({{< ref "pythonexamples.md" >}})

## Octave Interface
By the interface to [Octave](http://www.gnu.org/software/octave/ "Octave") you will find:

- Octave functions that communicates with a running ResInsight session
- Features to simplify management and editing of Octave scripts from ResInsight
- Commands to execute scripts using Octave.  
