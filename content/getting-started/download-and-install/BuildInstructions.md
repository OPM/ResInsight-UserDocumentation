+++
title = "Building ResInsight from Source"
published = true
hidden = false
weight = 30
+++

## Source code
The source code is hosted at [GitHub](https://github.com/opm/resinsight)

In a git enabled shell do: `git clone https://github.com/OPM/ResInsight.git`

## Dependencies and Prerequisites

### Windows Compiler

Visual Studio 2019 and later is supported.

### GCC Compiler

On RedHat Linux 7 or CentOS 7 you need to install devtoolset-10, and enable it with 
    
    source /opt/rh/devtoolset-10/enable

### Qt 5
Qt 5.12 or later is supported, Qt 5.15 is recommended.

[Qt download](http://download.qt.io/archive/qt/)  

On some configurations you will be asked to specify the location of Qt. Preferred method is to add Qt path to CMake variable **CMAKE_PREFIX_PATH**

Example for Windows : `CMAKE_PREFIX_PATH=F:/Qt/5.15.2/msvc2019_64`

### CMake
[CMake](https://cmake.org/download/) version 3.15 or later is supported.

## Build Overview
The ResInsight build may be configured in different ways, with optional support for Octave plugins, 
ABAQUS ODB API, HDF5, Pyton, and OpenMP. This is configured using options in CMake.

If you check the button 'Grouped' in the CMake GUI, the CMake variables are grouped by prefix. 
This makes it easier to see all of the options for ResInsight.

- Open the CMake GUI
- Set the path to the source code
- Set the path to the build directory
- Click **Configure** and select your preferred compiler
- Set the build options and click "Configure" again (see ResInsight specific options below)
- Click **Generate** to generate the makefiles or solution file and project files in the build directory
- Run the compiler using the generated makefiles or solution file/project files to build ResInsight

### Windows
ResInsight has been verified to build and run on Windows 10/11 using Microsoft Visual Studio 2019/2022. Typical usage on Windows is to follow the build instructions above, and then open the generated solution file in Visual Studio to build the application.

### Linux

For a reference build instruction for Ubuntu, see [Reference installation description for Ubuntu]({{< ref "build-instructions-ubuntu.md" >}})

### CMake Options for ResInsight

| CMake Name                                        | Default | Description                                                           |
|---------------------------------------------------|---------|-----------------------------------------------------------------------|
| `RESINSIGHT_BUILD_DOCUMENTATION`                  | OFF     | Use Doxygen to create the HTML based API documentation. Doxygen must be properly installed. |
| `RESINSIGHT_ENABLE_GRPC`                          | OFF     | Enable gRPC scripting server. Required to be able to use ResInsight from Python |
| `RESINSIGHT_ENABLE_HDF5`                          | ON      | Windows Only: Download and use HDF5 library |
| `RESINSIGHT_ODB_API_DIR`                          | Blank   | Optional path to the ABAQUS ODB API from Simulia. Needed for support of geomechanical models |
| `RESINSIGHT_USE_OPENMP`                           | ON      | Enable OpenMP parallellization in the code |

#### Advanced Options
To be able to modify **Advanced Options** from the CMake User Interface, tick the checkbox **Advanced**

| CMake Name                                        | Default | Description                              |
|---------------------------------------------------|---------|--------------------------------------------------------|
| `RESINSIGHT_QT5_BUNDLE_LIBRARIES`                 | OFF     | Linux only: Include Qt5 libraries in the installation package |
| `RESINSIGHT_BUILD_LIBS_FROM_SOURCE`               | ON      | If ON: Build some ThirdParty libs locally. If OFF: Download precompiled libraries
| `RESINSIGHT_BUNDLE_OPENSSL`                       | OFF     | Bundle the OpenSSL library binaries |
| `RESINSIGHT_ENABLE_UNITY_BUILD`                   | OFF     | Activate use of CMAKE_UNITY_BUILD on some libraries to improve build speed |
| `RESINSIGHT_INCLUDE_APPFWK_TESTS`                 | OFF     | Include unit tests from thirdparty libraries AppFwk and VizFwk |
| `RESINSIGHT_INCLUDE_APPLICATION_UNIT_TESTS`       | OFF     | Include Application Code Unit Tests |
| `RESINSIGHT_PRIVATE_INSTALL`                      | ON      | Linux only: Include resdata libraries in the installation package |
| `RESINSIGHT_HDF5_BUNDLE_LIBRARIES`                | OFF     | Linux only: Include HDF5 libraries in the installation package |
| `RESINSIGHT_TREAT_WARNINGS_AS_ERRORS`             | OFF     | Enable warnings as errors
| `RESINSIGHT_UPDATE_SUBMODULES`                    | ON      | Automatically issue 'git submodule update --init --recursively' on ThirdParty folder |
| `RESINSIGHT_VCPKG_AUTO_INSTALL`                   | OFF     | Automatically build required dependencies using 'vcpkg' |

#### Configuration parameters for Python

| CMake Name                                        | Default | Description                              |
|---------------------------------------------------|---------|--------------------------------------------------------|
| `RESINSIGHT_ENABLE_GRPC`                          | OFF     | Enable gRPC scripting server. Required to be able to use ResInsight from Python |
| `RESINSIGHT_GRPC_BUNDLE_PYTHON_MODULE`            | OFF     | Bundle GRPC Python module in install folder |
| `RESINSIGHT_GRPC_DOWNLOAD_PYTHON_MODULE`          | ON      | Download GRPC Python module |
| `RESINSIGHT_GRPC_PYTHON_EXECUTABLE`               | Blank   | Location of Python3 executable |


### Optional Libraries and features

#### Python

Please see [ResInsight Python API](https://api.resinsight.org) for installation and configuration.

#### Octave

Octave is now detected searching the file system. If Octave is not detected, the following file path variable must be defined:

`OCTAVE_CONFIG_EXECUTABLE : d:\octave\Octave-4.0.0\bin\octave-config.exe`

It is possible to build ResInsight without compiling the Octave plugins. This can be done by specifying blank for 
the Octave CMake options. The Octave plugin module will not be built, and CMake will show warnings like 'Failed to find mkoctfile'. 
This will not break the build or compilation of ResInsight.

ResInsight has been verified to build and run with Octave versions 3.4.3, 3.8.1, and 4.0.0 on RedHat linux, and 4.0.0 on Windows.

##### Octave Dependencies for Debian Based Distributions

The following command line can be used as a starting point to install required libraries
`sudo apt-get install git cmake build-essential octave liboctave-dev qtbase5-dev qtscript5-dev libqt5svg5-dev qtbase5-private-dev`

#### ODB support

ResInsight can be built with support for ABAQUS ODB files. This requires an installation of the ABAQUS ODB API 
from Simulia on the build computer. The path to the ABAQUS ODB API folder containing header files and library 
files must be specified. Leaving this option blank gives a build without ODB support. 
ResInsight has been built and tested with ABAQUS ODB API version 6.14-3 on Windows 7/8/10 and RedHat Linux 6.

#### HDF5

HDF5 is used to read SourSimRL result files. On Windows this is optional, while on Linux the installed HDF5 library will be used if present.

Use an advanced flag RESINSIGHT_HDF5_BUNDLE_LIBRARIES to include HDF5 libraries in the installation package.

Tested with 1.8.18 on windows, and default installation on RedHat 6.

