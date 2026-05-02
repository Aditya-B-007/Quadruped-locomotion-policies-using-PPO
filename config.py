class Config:
    #Environment variables
    RENDER=True
    MAX_STEPS=200
    GRAVITY_RANGE = [0.85, 1.15] 
    FRICTION_RANGE = [0.6, 1.4]
    MASS_RANGE = [0.75, 1.25]
    LEARNING_RATE = 3e-4
    BATCH_SIZE = 64
    TOTAL_TIMESTEPS = 10000000