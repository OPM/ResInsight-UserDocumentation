# ResInsight Scripting API - rips

## Update procecure on branch next-major-release
There is a workflow **update-from-latest.yml** used to update the documentation. This workflow executes the script `ResInsight-UserDocumentation/docs/source/create_python_examples.py`. This workflow will download the rips package from latest build from ResInsight main repo, build the documentation, and create a PR in this repository if required.

## How to generate documentation locally
- Install Python 3.x
- Create a virtual environment
- Install dependencies for rips `pip install grpcio grpcio-tools protobuf`
- Install the documentation system `pip install sphinx`
- Install dependencies for sphinx `pip install m2r sphinx_rtd_theme`
- Open command line in folder **docs**
- Execute `sphinx-build -b html source build`
- Open the generated documentation in a browser from this page `build/html/index.html`

## Release of master
Create pull request from next-major-release to master branch.
