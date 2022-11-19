from setuptools import setup, find_namespace_packages

setup(
    name="tboulet_test_package880",
    url="https://github.com/tboulet/Python-Tips-And-Tools", 
    author="T. B.",
    author_email="dummy@gmail.com",
    
    packages=find_namespace_packages(),

    version="0.0.4",
    license="MIT",
    description="My first Python package",
    long_description=open('README.md').read(),      # always in md, with a README.md (convention!)
    long_description_content_type="text/markdown",  # always in md !
)
