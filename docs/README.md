# ResInsight Scripting API - rips

## Update Procedure for `next-major-release` Branch
The workflow **update-from-latest.yml** is used to update the documentation. This workflow:
1. Downloads the latest rips package from the ResInsight main repository
2. Downloads Protocol Buffer (.proto) files from the ResInsight repository
3. Generates Protocol Buffer documentation using `docs/source/generate_protobuf_docs.py`
4. Generates Python examples using `docs/source/create_python_examples.py`
5. Creates a pull request in this repository if needed

## Conventions
We use an internal system to communicate large binary structures between Python and ResInsight. Functions related to this system are postfixed with `_internal` and are removed from the generated documentation using the script `clean_internal_methods.py`.

## How to Generate Documentation Locally
1. Install Python 3.x
2. Create a virtual environment
3. Install dependencies for rips:
	```sh
	pip install grpcio grpcio-tools protobuf
	```
4. Install Sphinx:
	```sh
	pip install sphinx
	```
5. Install Sphinx dependencies:
	```sh
	pip install m2r2 sphinx_rtd_theme sphinx-automodapi
	```
6. **(Optional)** If you have proto files in `docs/proto/`, generate Protocol Buffer documentation:
	```sh
	cd docs/source
	python generate_protobuf_docs.py
	cd ..
	```
7. Open a command line in the **docs** folder
8. Run:
	```sh
	sphinx-build -b html source build
	```
9. Open the generated documentation in your browser from `build/html/index.html`

## Updating Protocol Buffer Documentation
The Protocol Buffer documentation is automatically generated from `.proto` files:

### Automatic Updates (via GitHub Actions)
The workflow automatically:
- Downloads the latest `.proto` files from ResInsight repository
- Generates `ProtobufStructures.rst` documentation
- Includes it in pull requests

### Manual Updates
To manually update Protocol Buffer documentation:

1. Ensure proto files exist in `docs/proto/` directory
2. Run the generator script:
	```sh
	cd docs/source
	python generate_protobuf_docs.py
	```
3. The script will update `docs/source/ProtobufStructures.rst` with current proto definitions

The generator script parses `.proto` files and creates RST documentation including:
- Message definitions with field types and descriptions
- Enum definitions
- Service definitions (gRPC methods)
- Cross-references to Python API methods

## Releasing to Master
Create a pull request from `next-major-release` to the `master` branch.
