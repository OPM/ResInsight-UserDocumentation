# ResInsight Scripting API - rips

## Update Procedure for `next-major-release` Branch
The workflow **update-from-latest.yml** is used to update the documentation. This workflow runs the script `docs/source/create_python_examples.py`, downloads the latest rips package from the ResInsight main repository, builds the documentation, and creates a pull request in this repository if needed.

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
	pip install m2r sphinx_rtd_theme
	```
6. Open a command line in the **docs** folder
7. Run:
	```sh
	sphinx-build -b html source build
	```
8. Open the generated documentation in your browser from `build/html/index.html`

## Releasing to Master
Create a pull request from `next-major-release` to the `master` branch.
