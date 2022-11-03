
# In local

## Coding your package, or 'deploy' in local
Coding a package should have the following form:
```bash
package_PackageName/

    # The package's name with the code inside (as well as an init file)
    packageName/
        # init file to specify this is a package. You can let it as empty or add some code that will be call each time packageName is imported
        __init__.py  
        # Your package code
        module/      
        file2.py    

    # Contain the setup script, check package_AddOne/setup.py for example  
    setup.py     
    
    # Facultative other files
    README.md
    LICENSE
    tests/
        test_myTest.py
```
Note : you can also replace packageName by src/packageName and put other things in src/

## Install package from local
```bash
cd package_PackageName
pip install [--upgrade] .       
# --upgrade option can be used for install the current version of your package, otherwise it may "install" an older version if it is already installed
pip install -e .               
 # -e for editable mode. This allow you to debug in directly your package.
```


## Use package
```bash
import packageName
from packageName.module import file1
from packageName import file2
```

## In summary
You need to run "pip install -e ." in a folder containing setup.py + the package (addone/ for example)

# With Git

## Coding a package inside a Git repo, or deploy with Git
Create a git repository (say, project_for_package), clone it, go inside and then create the same files as in package_packageNamen and then push.
```
https://github.com/<path?>/project_for_package
    packageName/
    setup.py  
    README.md
    LICENSE
    tests/
```


### Install package from a repo git

```
pip install [--upgrade] git+https://github.com/<path?>/project_for_package

# More specifical install (unsure)
pip install [--upgrade] git+https://github.com/<path?>/project_for_package.git@<branch_name>#egg=<package_name>
```




# With PyPI

## Distribute package
Pre-requisite : create an account on PyPI (with say username Max and password 1234), install build and twine
```
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```

Build the distributions (wheel and source). This will create archives in package_PackageName/dist/
```
cd package_PackageName
python3 -m build
```

Upload all the distributions on PyPI. Use your PyPI username and password.
```
python3 -m twine upload dist/*
```
