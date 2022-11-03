# Gym environment

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