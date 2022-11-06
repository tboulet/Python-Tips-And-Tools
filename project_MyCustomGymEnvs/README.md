# Create a custom gym environment

This contains the files for the gym environment. The environment is based on the [OpenAI Gym](https://gym.openai.com/) framework.

The current folder (project_MyCustomGymEnvs) has to be seen as a package project/repo. It contains the following files:

```
package_MyCustomGymEnvs
    __init__.py  # register envs here
    envs
        __init__.py     # shortcut of env classes here
        riverEnv_v0.py
        riverEnv_v1.py

setup.py    # This is the file that is used to install the package. Name argument is "package_MyCustomGymEnvs"

# Other files 
README.md
```

# File by file

## setup.py
This is the file that is used to install your package. It is used by the command `pip install -e .` (see below). The 'name' argument is the name of the package folder (in this case "package_MyCustomGymEnvs").

## package_MyCustomGymEnvs/\_\_init\_\_.py
This will register the env (or different versions of the env, v0, v1 etc) in gym environments each time the package is imported.

## package_MyCustomGymEnvs/envs/\_\_init\_\_.py
This will just import the env classes so that they are available in the package, and you can use : `from package_MyCustomGymEnvs.envs import riverEnv_v0` for example, instead of `from package_MyCustomGymEnvs.envs.riverEnv_v0 import riverEnv_v0`.

## package_MyCustomGymEnvs/envs/riverEnv_v0.py
Each file inside envs/ will contain a gym.Env class that have to be imported in the init file. 


# Install the package

To install the package, you have to be in the folder that contains the setup.py file. Then, you can install the package with the command `pip install -e .` (the dot is important). This will install the package in editable mode, so that you can modify the files and the changes will be taken into account when you import the package.


# Use the gym env package

Once the package is installed, you can import it in your code. For example, if you want to use the riverEnv_v0 environment, you can do:

```python
# Import riverEnv_v0 (along with other envs)
import package_MyCustomGymEnvs
# Create the environment
env = gym.make('riverEnv-v0')
```

 