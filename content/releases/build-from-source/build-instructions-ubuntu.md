+++
title = "Build Instructions Ubuntu"

hidden = false
weight = 30
+++

## Dependencies and Prerequisites

This page is mainly build instructions for Ubuntu, but some comments are also added for **RHEL8**.

Basic instructions without Python binding and GRPC.


### Configuration and build

| Tool                    | Minimum version  | 
|-------------------------|------------------|
| gcc                     | 11               | 
| python 				  | 3.8              | 
| Qt 	    			  | 6.4              | 

It is possible to use Qt 6.4 for building ResInsight, but some install features introduced in Qt 6.5 are not supported. Qt 6.7 has some changes related to theming that is causing some unwanted visual effects. This is currently investigated.


Update apt installer

    sudo apt update

Install GCC and related tools

    sudo apt install build-essential curl zip unzip tar flex bison pkg-config libgl1-mesa-dev libglu1-mesa-dev libfreetype6-dev libfontconfig1-dev

[Set default compiler](https://linuxconfig.org/how-to-switch-between-multiple-gcc-and-g-compiler-versions-on-ubuntu-20-04-lts-focal-fossa)

Dependencies for RHEL8

    yum install curl zip unzip tar flex bison perl-IPC-Cmd gcc-toolset-10 freeglut

### Clone and update sub modules

	git clone https://github.com/OPM/ResInsight
    cd ResInsight
    git submodule update --init

### Build and install required dependencies using vcpkg
vcpkg is located in the folder ThirdParty/vcpkg. The packages to be installed is specified in vcpkg.json. The actual install of the selected packages are done in the CMake configure step.

    ThirdParty/vcpkg/bootstrap-vcpkg.sh

### Qt - package manager

Qt6 can be installed using the package manager for Ubuntu

    apt install qt6-base-dev qt6-base-private-dev qt6-charts-dev qt6-networkauth-dev libqt6svg6-dev

    Ubuntu 22.04 : Qt 6.2.4
    Ubuntu 24.04 : Qt 6.4.2

Please note that 6.4 is fully supported for build, but some install features are not supported.

### Qt - aqtinstall
Here is a short description on how to install a custom Qt version.

[aqtinstall](https://github.com/miurahr/aqtinstall) is a Python tool used to install precompiled versions of Qt. Other ways to install Qt is described [official Qt documentation](https://www.qt.io/download-qt-installer-oss)


Create a root folder for Qt installations. In this folder, create a virtual environment for **aqtinstall**:

    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install aqtinstall
    aqt install-qt linux desktop 6.6.3 -m qtcharts qtnetworkauth
   

### Build ResInsight

Install Ninja and CMake
    
    sudo apt-get install ninja-build cmake

The configuration flags for a basic build is given in `CMakePresets.json` in the root of the repository. Configuration flags specific for the system to build on can be specified in `CMakeUserPresets.json`. This file is ignored by git.

- Create a copy of `CMakeUserPresets-example.json` and rename to `CMakeUserPresets.json`
- Update the path to your local installation of Qt6 for the key `CMAKE_PREFIX_PATH` in `CMakeUserPresets.json`

Set current working folder to the root folder of the ResInsight repository. Execute the following commands to build ResInsight:

    cmake . --preset=linux-base
    cd build
    ninja

[CMake Configuration]({{% relref "cmake-configuration" %}})