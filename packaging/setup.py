import setuptools

setuptools.setup(
    name="package1",
    version="0.0.1",
    description="My package 1",
    packages=setuptools.find_packages(),
    # python_requires='>=3.7',
)

setuptools.setup(
    name="package2",
    version="0.0.2",
    description="My package 2",
    packages=setuptools.find_packages(),
)

# Setup package this way :
#     cd packaging
#     pip install .

# Setup package in editable mode this way :
#     cd packaging
#     pip install -e .

# This will run setup.py with pip and install package1 and package2 in the current environment.
