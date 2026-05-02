import gymnasium as gym
from stable_baselines3 import PPO
from env.quadruped_env import QuadrupedEnv
from config import Config

def train():
    env = QuadrupedEnv(render=Config.RENDER)
    model = PPO(
        "MlpPolicy", 
        env, 
        verbose=1, 
        learning_rate=Config.LEARNING_RATE,
        batch_size=Config.BATCH_SIZE
    )
    print("Training started... go grab a coffee.")
    model.learn(total_timesteps=Config.TOTAL_TIMESTEPS)
    model.save("results/baseline_ppo_quadruped")
    print("Training complete. Model saved!")

if __name__ == "__main__":
    train()