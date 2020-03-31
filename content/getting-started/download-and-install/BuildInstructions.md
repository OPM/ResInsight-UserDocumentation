+++
title = "Build Instructions"
published = true
hidden = false
weight = 30
+++

## Source code
The source code is hosted at [GitHub](https://github.com/opm/resinsight)

In a git enabled shell do: `git clone https://github.com/OPM/ResInsight.git`

## Dependencies and Prerequisites

### Windows Compiler

Visual Studio 2015 and later is supported.

### GCC Compiler

GCC version 4.9 or later is supported. On RedHat Linux 6 you need to install devtoolset-3, and enable it with 
    
    source /opt/rh/devtoolset-3/enable

### Qt5
[Qt](http://download.qt.io/archive/qt/) Qt5 version 5.6.0 or later is supported. 

On some configurations you will be asked to specify the location of Qt5. Example for Windows :
`Qt5_DIR=d:\Qt\5.11.3\msvc2017_64\lib\cmake\Qt5`

#### Qt4 (Deprecated)

{{% notice info %}}
Qt4 is marked as deprecated and support for using Qt4 will soon be removed.
{{% /notice %}}

[Qt](http://download.qt.io/archive/qt/) Qt4 version 4.6.2 or later is supported. On Windows we recommend Qt-4.8.7, while the default installation will do under Linux. 

`RESINSIGHT_BUILD_WITH_QT5=FALSE`

You will need to patch the Qt sources in order to make them build using Visual Studio 2015 using this : 
[Qt-patch](https://github.com/appleseedhq/appleseed/wiki/Making-Qt-4.8.7-compile-with-Visual-Studio-2015) 

### CMake
[CMake](https://cmake.org/download/) version 2.8 or later is supported.

## Build Instructions
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
ResInsight has been verified to build and run on Windows 7/8/10 using Microsoft Visual Studio 2015/2017. 
Typical usage on Windows is to follow the build instructions above, and then open the generated 
solution file in Visual Studio to build the application.

### Linux

Typical usage is to follow the build instructions above to build the makefiles. Then go to the build directory, and run:

- make
- make install

To build from the command line without using the CMake GUI:

- mkdir ResInsight_build
- cd ResInsight_build
- ...
- (set CMake options)
- ...
- cmake < path to ResInsight source folder >
- make
- make install

You will find the ResInsight binary under the Install directory in your build directory.

### CMake Options for ResInsight

| CMake Name                                        | Default | Description                                                           |
|---------------------------------------------------|---------|-----------------------------------------------------------------------|
| `RESINSIGHT_BUILD_DOCUMENTATION`                  | OFF     | Use Doxygen to create the HTML based API documentation. Doxygen must be properly installed. |
| `RESINSIGHT_ENABLE_GRPC`                          | OFF     | Enable gRPC scripting server. Required to be able to use ResInsight from Python |
| `RESINSIGHT_HDF5_DIR`                             | Blank   | Windows Only: Optional path to HDF5 libraries on Windows |
| `RESINSIGHT_ODB_API_DIR`                          | Blank   | Optional path to the ABAQUS ODB API from Simulia. Needed for support of geomechanical models |
| `RESINSIGHT_USE_OPENMP`                           | ON      | Enable OpenMP parallellization in the code |

#### Advanced Options
To be able to modify **Advanced Options** from the CMake User Interface, tick the checkbox **Advanced**

| CMake Name                                        | Default | Description                              |
|---------------------------------------------------|---------|--------------------------------------------------------|
| `RESINSIGHT_BUILD_WITH_QT5`                       | ON      | If ON, use Qt5. If OFF, use Qt4 (Support for Qt4 is deprecated and will be removed) |
| `RESINSIGHT_QT5_BUNDLE_LIBRARIES`                 | OFF     | Linux only: Include Qt5 libraries in the installation package |
| `RESINSIGHT_BUNDLE_OPENSSL`                       | OFF     | Bundle the OpenSSL library DLLs in the Windows installer package |
| `RESINSIGHT_ENABLE_COTIRE`                        | OFF     | Experimental speedup of compilation using cotire |
| `RESINSIGHT_ENABLE_PROTOTYPE_FEATURE_SOURING`     | ON      | Enable Souring features |
| `RESINSIGHT_INCLUDE_APPFWK_TESTS`                 | OFF     | Include unit tests from thirdparty libraries AppFwk and VizFwk |
| `RESINSIGHT_INCLUDE_APPLICATION_UNIT_TESTS`       | OFF     | Include Application Code Unit Tests |
| `RESINSIGHT_PRIVATE_INSTALL`                      | ON      | Linux only: Include libecl libraries in the installation package |
| `RESINSIGHT_HDF5_BUNDLE_LIBRARIES`                | OFF     | Linux only: Include HDF5 libraries in the installation package |

#### Configuration parameters for Python

| CMake Name                                        | Default | Description                              |
|---------------------------------------------------|---------|--------------------------------------------------------|
| `RESINSIGHT_ENABLE_GRPC`                          | OFF     | Enable ResInsight scripting server (required for use of Python) |
| `RESINSIGHT_GRPC_PYTHON_EXECUTABLE`               | Blank   | Location of Python3 executable |
| `RESINSIGHT_GRPC_INSTALL_PREFIX`                  | Blank   | Linux only : Installation prefix for gRPC |

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
`sudo apt-get install git cmake build-essential octave liboctave-dev qtbase5-dev qtscript5-dev`

#### ODB support

ResInsight can be built with support for ABAQUS ODB files. This requires an installation of the ABAQUS ODB API 
from Simulia on the build computer. The path to the ABAQUS ODB API folder containing header files and library 
files must be specified. Leaving this option blank gives a build without ODB support. 
ResInsight has been built and tested with ABAQUS ODB API version 6.14-3 on Windows 7/8/10 and RedHat Linux 6.

#### HDF5

HDF5 is used to read SourSimRL result files. On Windows this is optional, while on Linux the installed HDF5 library will be used if present.

Use an advanced flag RESINSIGHT_HDF5_BUNDLE_LIBRARIES to include HDF5 libraries in the installation package.

Tested with 1.8.18 on windows, and default installation on RedHat 6.

