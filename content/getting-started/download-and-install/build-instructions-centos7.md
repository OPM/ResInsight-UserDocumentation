+++
title = "Build Instructions CentOS 7"
published = true
hidden = false
weight = 30
+++

## Dependencies and Prerequisites
**vcpkg** can be used to install **grpc** for C++. This method is cross platform, and can be easier to use than directly installing **grpc** and dependencies directly from **grpc** source code. The source code for **vcpkg** is avaialable as a Git sub module in the folder 'vcpkg'. Python3 is required.

vcpkg requires relatively new versions of git and compiler. 
 
[vcpkg](https://github.com/Microsoft/vcpkg)

[grpc quickstart](https://grpc.io/docs/quickstart/cpp/)


### Reference project
A workflow file is used to build using CentOS 7 on GitHub actions. A blank Centos7 Docker image is used, and the required dependencies are installed.

[Link to workflows](https://github.com/OPM/ResInsight/blob/dev/.github/workflows/)

### Configuration and build

| Tool                    | Minimum version  | 
|-------------------------|------------------|
| git                     | 2.7.4            | 
| gcc                     | 7                | 
| python 				  | 3                | 


### gcc
    yum install -y centos-release-scl
    yum-config-manager --enable rhel-server-rhscl-7-rpms
    yum install -y devtoolset-7

### git
	yum install -y https://repo.ius.io/ius-release-el7.rpm
    yum install -y git222

### Clone and update sub modules
Init of submodules is required to get the source code for vcpkg

	git clone git://github.com/OPM/ResInsight.git ResInsight
    cd ResInsight
    git submodule update --init

### Build and install grpc using vcpkg
vcpkg is located in the folder vcpkg

    vcpkg/bootstrap-vcpkg.sh 
    vcpkg/vcpkg install grpc

### Build ResInsight
	mkdir cmakebuild
    cd cmakebuild
    cmake3 \
    -DRESINSIGHT_QT5_BUNDLE_LIBRARIES=ON \
    -DRESINSIGHT_ENABLE_GRPC=true \
    -DVCPKG_TARGET_TRIPLET=x64-linux \
    -DCMAKE_TOOLCHAIN_FILE=../vcpkg/scripts/buildsystems/vcpkg.cmake \
    -DRESINSIGHT_GRPC_PYTHON_EXECUTABLE=python \
    ..
    
    make -j8


### Other build descriptions
[Build description for Windows and Linux](https://github.com/OPM/ResInsight/blob/dev/GRPC_install_instructions.txt)

