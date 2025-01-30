+++
title = "Build Instructions Windows"

hidden = false
weight = 31
+++

## Dependencies and Prerequisites

### Configuration and build

| Tool                    | Minimum version  | Recommended |
|-------------------------|------------------|-------------|
| Visual Studio           | 2019             | 2022        |
| python 				  | 3.8              | 3.10        |
| Qt 	    			  | 6.5              | 6.6         |

It is possible to use Qt 6.4 for to build ResInsight, but some install features introduced in Qt 6.5 are not available. Qt 6.7 has some changes related to theming that is causing some unwanted visual effects. This is currently investigated.

### Clone and update sub modules

	git clone https://github.com/OPM/ResInsight
    cd ResInsight
    git submodule update --init

### Build and install required dependencies using vcpkg 
Open a command prompt using "Run as Administrator" for Visual Studio x64.

[Detailed Developer notes](https://ceetronsolutions.github.io/resinsight-system-doc/editor/vcpkg)

    ThirdParty/vcpkg/bootstrap-vcpkg.bat

### Qt

**Official install tools**

Qt can be installed using the `MaintenanceTool.exe`, and select the following modules:

![](/images/getting-started/qtmaintenancetool.png)

**aqtinstall**

[aqtinstall](https://github.com/miurahr/aqtinstall) is a Python tool used to install Qt directly from Qt distribution sites, and does not require a user account for Qt sites. Other ways to install Qt is described [official Qt documentation](https://www.qt.io/download-qt-installer-oss)

Create a root folder for Qt installations. In this folder, create a virtual environment for **aqtinstall**:

    python3 -m venv myvenv
    myvenv/Scripts/activate
    pip3 install aqtinstall
    aqt install-qt linux desktop 6.6.3 -m qtcharts qt5compat qtnetworkauth
   

### Build ResInsight

The configuration flags for a basic build is given in `CMakePresets.json` in the root of the repository. Configuration flags specific for the system to build on can be specified in `CMakeUserPresets.json`. This file is ignored by git.

- Create a copy of `CMakeUserPresets-example.json` and rename to `CMakeUserPresets.json`
- Update the path to your local installation of Qt6 for the key `CMAKE_PREFIX_PATH` in `CMakeUserPresets.json`

Start Visual Studio, and open the ResInsight source folder. When you open the ResInsight folder for the first time, **vcpkg** may spend a few minutes building the required dependencies specified in `vcpkg.json`.

[CMake Configuration]({{< relref "cmake-configuration" >}})

[Configure and build with CMake Presets in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/cmake-presets-vs?view=msvc-170)