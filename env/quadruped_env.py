import gymnasium as gym
import numpy as np
import pybullet as p
import pybullet_data #---> We import the pybullet_data module to access the data files provided by PyBullet, such as URDF files for robots and environments.
class QuadrupedEnv(gym.Env):
    def __init__(self,render=False):
        super(QuadrupedEnv, self).__init__()
        self.robot_id = None
        self.client = p.connect(p.GUI if render else p.DIRECT) #---> We establish a connection to the PyBullet physics server. If render is True, we use the GUI mode; otherwise, we use DIRECT mode for headless operation.
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) #---> We set the additional search path for PyBullet to find the data files, such as URDF files for robots and environments.
        #We design how the robot will look
        self.prev_action= np.zeros(12) #---> We initialize a variable to store the previous action taken by the robot, which can be useful for certain algorithms that require information about past actions.
        self.action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(12,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(45,), dtype=np.float32) #What the robot can see
    def step(self, action):
        for i in range(12):
            p.setJointMotorControl2(bodyUniqueId=self.robot_id,
                                    jointIndex=i,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=action[i],
                                    force=5.0)
        p.stepSimulation()
        obs=self._get_observation()
        self.prev_action = action
        reward=self._compute_reward(obs,action)
        done=False
        truncated=False # Used if the episode runs out of time
        info={}         # Used for debugging
        
        return obs, reward, done, truncated, info

    def _get_observation(self):
        # TODO: Extract real IMU, joint states, and commands from PyBullet
        # For now, returning a dummy 45-dimensional array so it doesn't crash
        obs = np.zeros(45, dtype=np.float32)
        return obs
        
    def _compute_reward(self, obs, action):
        total_reward = 0.0 
        
        return float(total_reward)
