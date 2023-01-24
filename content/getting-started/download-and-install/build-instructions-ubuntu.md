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
| gcc                     | 7                | 
| python 				  | 3                | 


Update apt installer

    sudo apt update

Install GCC and related tools

    sudo apt install build-essential
    sudo apt install curl zip unzip tar

Install Qt

    sudo apt install -y qtbase5-dev libqt5svg5-dev qtbase5-private-dev


### Clone and update sub modules

	git clone git://github.com/OPM/ResInsight.git ResInsight
    cd ResInsight
    git submodule update --init

### Build and install required dependencies using vcpkg
vcpkg is located in the folder ThirdParty/vcpkg

    ThirdParty/vcpkg/bootstrap-vcpkg.sh 
    ThirdParty/vcpkg/vcpkg install grpc boost-filesystem boost-spirit eigen3

### Build ResInsight
	mkdir cmakebuild
    cd cmakebuild
    cmake \
    -DRESINSIGHT_ENABLE_GRPC=true \
    -DVCPKG_TARGET_TRIPLET=x64-linux \
    -DCMAKE_TOOLCHAIN_FILE=..ThirdParty/vcpkg/scripts/buildsystems/vcpkg.cmake \
    -DRESINSIGHT_GRPC_PYTHON_EXECUTABLE=python \
    ..
    
    make -j8


### Other build descriptions

[Link to workflow for CentOS 7](https://github.com/OPM/ResInsight/blob/dev/.github/workflows/centos7.yml)
