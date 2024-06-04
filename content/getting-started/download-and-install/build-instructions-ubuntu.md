+++
title = "Build Instructions Ubuntu"
published = true
hidden = false
weight = 30
+++

## Dependencies and Prerequisites



### Configuration and build

| Tool                    | Minimum version  | 
|-------------------------|------------------|
| git                     | 2.7.4            | 
| gcc                     | 10               | 
| python 				  | 3                | 


Update apt installer

    sudo apt update

Install GCC and related tools

    sudo apt install build-essential curl zip unzip tar flex bison

As gcc 10 is required, it can be useful to set the default compiler.
[Set default compiler](https://linuxconfig.org/how-to-switch-between-multiple-gcc-and-g-compiler-versions-on-ubuntu-20-04-lts-focal-fossa)

Dependencies for RHEL8

    yum install curl zip unzip tar flex bison perl-IPC-Cmd gcc-toolset-12 freeglut

### Clone and update sub modules

	git clone https://github.com/OPM/ResInsight
    cd ResInsight
    git submodule update --init

### Build and install required dependencies using vcpkg
vcpkg is located in the folder ThirdParty/vcpkg

    ThirdParty/vcpkg/bootstrap-vcpkg.sh

### (Windows) Build and install required dependencies using vcpkg 
Open a command prompt using "Run as Administrator" for Visual Studio x64.

[Detailed Developer notes](https://ceetronsolutions.github.io/resinsight-system-doc/editor/vcpkg)

    ThirdParty/vcpkg/bootstrap-vcpkg.bat

### Python dependencies
Install Python version 3.8 or newer, and use dev-requirements.txt

    python3 -m pip install -r GrpcInterface/Python/dev-requirements.txt

### Qt

System packages Ubuntu

    sudo apt install -y qtbase5-dev libqt5svg5-dev qtbase5-private-dev libqt5networkauth5-dev

System packages RHEL8

    sudo yum install -y qt5-devel qt5-qtnetworkauth-devel qt5-qtcharts-devel qt5-qtbase-private-devel
    gcc-toolset-12-libatomic-devel

Installation of custom Qt

Go to a folder to install custom Qt
In this folder, execute
    
    python3 -m pip install aqtinstall
    aqt install-qt linux desktop 5.15.2 -m qtcharts qtnetworkauth
    

### Build ResInsight
	mkdir cmakebuild
    cd cmakebuild
    cmake \
    -DCMAKE_PREFIX_PATH=/your_qt_path/5.15.2/gcc_64/lib/cmake \
    -DRESINSIGHT_ENABLE_GRPC=true \
    -DRESINSIGHT_GRPC_PYTHON_EXECUTABLE=python \
    ..
    
    make -j8


### Notes for CentOS

The dependency on `atomic` can be installed using the following code, adjust the devtoolset version to match your installation:
    
    sudo yum install devtoolset-11-libatomic-devel



[Link to workflow for CentOS 7](https://github.com/OPM/ResInsight/blob/dev/.github/workflows/centos7.yml)
