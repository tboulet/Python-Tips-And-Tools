from gym.envs.registration import register

register(
    id='River-v0',                                            # Name of the environment
    entry_point='package_MyCustomGymEnvs.envs:RiverEnv_v0',    # Path to the environment class
)

register(
    id='River-v1',
    entry_point='package_MyCustomGymEnvs.envs:RiverEnv_v1',
)