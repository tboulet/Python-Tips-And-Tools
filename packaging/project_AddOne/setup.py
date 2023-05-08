from setuptools import setup, find_namespace_packages

setup(
    name="test_addone",
    url="https://github.com/tboulet/Python-Tips-And-Tools/packaging/project_AddOne", 
    author="tboulet",
    author_email="dummy@gmail.com",
    
    packages=find_namespace_packages(),

    version="0.0.4",
    license="MIT",
    description="My first Python package",
    long_description=open('README.md').read(),     
    long_description_content_type="text/markdown", 
)
