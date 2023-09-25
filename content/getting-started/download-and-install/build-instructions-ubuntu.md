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

    sudo apt install build-essential
    sudo apt install curl zip unzip tar

As gcc 10 is required, it can be useful to set the default compiler.
[Set default compiler](https://linuxconfig.org/how-to-switch-between-multiple-gcc-and-g-compiler-versions-on-ubuntu-20-04-lts-focal-fossa)

Install Qt

    sudo apt install -y qtbase5-dev libqt5svg5-dev qtbase5-private-dev


### Clone and update sub modules

	git clone https://github.com/OPM/ResInsight
    cd ResInsight
    git submodule update --init

### Build and install required dependencies using vcpkg
vcpkg is located in the folder ThirdParty/vcpkg

    ThirdParty/vcpkg/bootstrap-vcpkg.sh
    ThirdParty/vcpkg/vcpkg install grpc boost-filesystem boost-spirit eigen3

### (Windows) Build and install required dependencies using vcpkg 
Open a command prompt for Visual Studio x64

    ThirdParty/vcpkg/bootstrap-vcpkg.bat
    ThirdParty/vcpkg/vcpkg install grpc boost-filesystem boost-spirit eigen3 --triplet x64-windows

    [Developer notes](https://ceetronsolutions.github.io/resinsight-system-doc/editor/vcpkg)

### Python dependencies
Install Python version 3.8 or newer

    python3 -m pip install -r GrpcInterface/Python/requirements.txt

### Installation of custom Qt

Go to a folder to install custom Qt
In this folder, execute
    
    python3 -m pip install aqtinstall
    aqt install-qt linux desktop 5.15.2 -m qtcharts
    

### Build ResInsight
	mkdir cmakebuild
    cd cmakebuild
    cmake \
    -DCMAKE_PREFIX_PATH=/your_qt_path/5.15.2/gcc_64/lib/cmake \
    -DRESINSIGHT_ENABLE_GRPC=true \
    -DVCPKG_TARGET_TRIPLET=x64-linux \
    -DCMAKE_TOOLCHAIN_FILE=../ThirdParty/vcpkg/scripts/buildsystems/vcpkg.cmake \
    -DRESINSIGHT_GRPC_PYTHON_EXECUTABLE=python \
    ..
    
    make -j8


### Notes for CentOS

The dependency on `atomic` can be installed using the following code, adjust the devtoolset version to match your installation:
    
    sudo yum install devtoolset-11-libatomic-devel



[Link to workflow for CentOS 7](https://github.com/OPM/ResInsight/blob/dev/.github/workflows/centos7.yml)
