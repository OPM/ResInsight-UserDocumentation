+++
title = "Windows Installation"

hidden = false
weight = 20
+++

## ResInsight Installation

1. Download ZIP binary distribution from [https://github.com/OPM/ResInsight/releases](https://github.com/OPM/ResInsight/releases "release section on GitHub")
2. Extract content from ZIP file
3. Start ResInsight.exe 

{{% notice info %}}
The binary distribution does not support ABAQUS odb files. For building ResInsight with ABAQUS support, see 
[Build Instructions]({{< ref "cmake-configuration.md" >}}).
{{% /notice %}}


## Octave Installation (optional)
1. Download [Octave-4.0.0](ftp://ftp.gnu.org/gnu/octave/windows) and install it. (Newer versions will not work)
2. Launch ResInsight.exe, open **Edit->Preferences**. 
3. On the **Octave** tab, enter the path to the Octave command line interpreter executable.  
   ( Usually _`C:\Your\Path\To\Octave-x.x.x\bin\octave-cli.exe`_ )

{{% notice info %}}
A binary package of ResInsight will normally <b>not</b> work with other Octave versions than the one it is compiled with. 
{{% /notice %}}

{{% notice info %}}
You <b>have</b> to point to the <b>cli</b> binary in the windows octave installation. The <code>octave.exe</code> will not work as it is launching the octave GUI.
{{% /notice %}}

## FAQ

### Windows Firewall notice
ResInsight can communicate with Python and other cloud services. A Windows Firewall message might appear when you launch the application. Choose **Allow** to ensure correct behavior for these features.

### Smartscreen warnings
When launching ResInsight at the first time, a Smartscreen warning might be displayed. This is a security feature by Microsoft, and will warn the user when an unknown program is launched. This warning is displayed once for each installation.


![](/images/getting-started/Smartscreen_01.png)

Press the **More info** link in the upper left section.


![](/images/getting-started/Smartscreen_02.png)

Notice the information and digital signature by **Ceetron Solutions AS**.

Press **Run anyway**, and the application starts. This warning is only displayed once.
