# ResInsight Scripting API - rips

## Update procecure on  branch next-major-release
REQUIRED: Compile ResInsight and make sure the content in folder `ResInsight/GrpcInterface/Python/rips` is up to date
- Checkout branch next-major-release
- Delete the copy in `ResInsight-UserDocumentation/docs/rips` 
- Copy all files from `ResInsight/GrpcInterface/Python/rips` into `ResInsight-UserDocumentation/docs/rips` 
- Update the example documentation using `ResInsight-UserDocumentation/docs/source/create_python_examples.py`
- See below for how to create documentation locally
- Publish to branch next-major-release

## Release of master
Create pull request from next-major-release to master branch.

## How to generate documentation locally
- Install Python 3.x
- Install dependencies for rips `pip install grpcio grpcio-tools protobuf`
- Install the documentation system `pip install sphinx`
- Install dependencies for sphinx `pip install m2r sphinx_rtd_theme`
- Open command line in folder **docs**
- Execute `make html`
- Open the generated documentation in a browser `build/html/index.html`
