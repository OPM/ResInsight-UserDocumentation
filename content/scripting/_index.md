+++
title = "Scripting"

weight = 70
+++

![](/images/scripting/ExecuteOctaveScriptOnSelectedCases.png)

ResInsight provides powerful and flexible mechanisms for post-processing of results and automation by its scripting interfaces:

- Python interface
- Command line interface and Command files
- Octave interface

## Python interface
ResInsight incorporates a powerful Python interface which allows you to interact with ResInsight and load data for further processing and automation.


## Command Line Interface and Command files
ResInsight supports several [command line parameters] ({{< ref "CommandLineInterface.md" >}}) for automation via shell scripts. 
By gathering commands into a [Command file]({{< ref "CommandFile.md" >}}), you may run a sequence of commands by supplying the 
command file as a [command line parameter]({{< ref "CommandLineInterface.md" >}}). 

## Octave Interface
By the interface to [Octave](http://www.gnu.org/software/octave/ "Octave") you will find:

- Octave functions that communicates with a running ResInsight session
- Features to simplify management and editing of Octave scripts from ResInsight
- Commands to execute scripts using Octave.  
