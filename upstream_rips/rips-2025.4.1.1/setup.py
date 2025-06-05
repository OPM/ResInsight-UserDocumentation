from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

RIPS_DIST_VERSION = '1'
	
setup(
    name='rips',
    version='2025.04.1.' + RIPS_DIST_VERSION,
    description='Python Interface for ResInsight',
    long_description=readme,
    author='Ceetron Solutions',
    author_email='info@ceetronsolutions.com',
    url='http://www.resinsight.org',
    license=license,
    packages=['rips'],
    package_data={'rips': ['py.typed', '*.py', 'generated/*.py', 'PythonExamples/*.py', 'tests/*.py']},
    install_requires=['grpcio', 'protobuf', 'wheel', 'typing_extensions'],
    python_requires='>=3.8',
)
