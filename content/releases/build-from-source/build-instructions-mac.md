+++
title = "Build Instructions Mac"

hidden = false
weight = 32
+++

## Dependencies and Prerequisites

The build targets **macOS 15** and uses the Apple Clang compiler shipped with Xcode / the Command Line Tools.

### Configuration and build

| Tool                    | Minimum version  |
|-------------------------|------------------|
| macOS                   | 15               |
| Apple Clang (Xcode)     | Command Line Tools |
| python 				  | 3.12             |
| Qt 	    			  | 6.7.0            |

gRPC and HDF5® are currently disabled for the Mac build.

### Clone and update sub modules

	git clone https://github.com/OPM/ResInsight
    cd ResInsight
    git submodule update --init

### Homebrew build tools

macOS ships an old `bison` (2.3) in `/usr/bin`. The `thrift` package built by vcpkg — a transitive dependency of Apache Arrow — requires bison newer than 2.5. Install the Homebrew version and put it ahead on your `PATH`:

    brew install bison
    export PATH="$(brew --prefix bison)/bin:$PATH"

### Build and install required dependencies using vcpkg

vcpkg is located in the folder `ThirdParty/vcpkg`. The packages to be installed are specified in `vcpkg.json`. The actual install of the selected packages is done in the CMake configure step.

    ThirdParty/vcpkg/bootstrap-vcpkg.sh

### Qt - aqtinstall

[aqtinstall](https://github.com/miurahr/aqtinstall) is a Python tool used to install precompiled versions of Qt. Other ways to install Qt are described in the [official Qt documentation](https://www.qt.io/download-qt-installer-oss).

Create a root folder for Qt installations. In this folder, create a virtual environment for **aqtinstall**:

    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install aqtinstall
    aqt install-qt mac desktop 6.7.0 -m qtnetworkauth

### Build ResInsight

Install Ninja and CMake (for example with Homebrew):

    brew install ninja cmake

There is no Mac CMake preset yet, so the Mac build is configured with explicit CMake flags. Set the current working folder to the root of the ResInsight repository and update `CMAKE_PREFIX_PATH` to point at your local Qt installation:

    cmake -S . -B build -G Ninja \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
      -DCMAKE_PREFIX_PATH=<path-to-your-Qt>/6.7.0/macos/lib/cmake \
      -DCMAKE_TOOLCHAIN_FILE=ThirdParty/vcpkg/scripts/buildsystems/vcpkg.cmake \
      -DRESINSIGHT_ENABLE_GRPC=false \
      -DRESINSIGHT_ENABLE_HDF5=false

When you run the configure step for the first time, **vcpkg** may spend a few minutes building the required dependencies specified in `vcpkg.json`.

Then build:

    cmake --build build

### Running an unsigned build

The Mac build is currently unsigned and unnotarised. macOS Gatekeeper will quarantine `ResInsight.app` when it is downloaded and refuse to launch it, reporting that the app is damaged or cannot be opened. Remove the quarantine attribute before the first launch:

    sudo xattr -r -d com.apple.quarantine ResInsight.app

Then start it normally — double-click the app or run:

    open ResInsight.app

[CMake Configuration]({{% relref "cmake-configuration" %}})

The exact, always up-to-date build steps are defined in the [ResInsight Mac build workflow](https://github.com/OPM/ResInsight/blob/dev/.github/workflows/ResInsightMac.yml) on GitHub.
