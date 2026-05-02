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

    def reset(self, seed=None, options=None): # type: ignore
        super().reset(seed=seed)
        p.resetSimulation()
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")
        self.robot_id = p.loadURDF("a1/a1.urdf", basePosition=[0, 0, 0.42])
        self.prev_action = np.zeros(12)
        obs = self._get_observation()
        info = {}
        return obs, info
    
    
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
        pos, ori = p.getBasePositionAndOrientation(self.robot_id) #Base position and orientation of the robot in the simulation. The position is returned as a tuple of (x, y, z) coordinates, and the orientation is returned as a quaternion (x, y, z, w).
        rpy=p.getEulerFromQuaternion(ori)
        vel,ang_vel = p.getBaseVelocity(self.robot_id)
        joint_states = p.getJointStates(self.robot_id, range(12))
        joint_pos = [state[0] for state in joint_states]
        joint_vel = [state[1] for state in joint_states]
        joint_forces = [state[3] for state in joint_states]
        obs = np.concatenate([
            joint_pos, 
            joint_vel, 
            self.prev_action, 
            rpy, 
            ang_vel, 
            vel
        ]).astype(np.float32)
        return obs
        
    def _compute_reward(self, obs, action):
        vel_reward = obs[42] # obs[42] is the forward velocity (updated index based on _get_observation)
        energy_penalty = np.sum(np.square(action)) 
        tilt_penalty = np.sum(np.square(obs[36:38])) # obs[36:38] corresponds to the roll and pitch angles (updated index based on _get_observation)
        reward = (1.0 * vel_reward) - (0.01 * energy_penalty) - (0.1 * tilt_penalty)

        return float(reward)
