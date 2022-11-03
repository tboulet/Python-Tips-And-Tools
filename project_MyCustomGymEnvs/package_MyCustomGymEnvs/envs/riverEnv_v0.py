import gym

# Define the environment class
class RiverEnv_v0(gym.Env):
    # Initialize the environment
    def __init__(self):
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Discrete(2)
    # Define the reset function
    def reset(self):
        print("Resetting the environment RiverEnv-v0")
        return 0
    # Define the step function
    def step(self, action):
        return 0, 0, False, {}
    # Define the render function
    def render(self, mode='human'):
        return