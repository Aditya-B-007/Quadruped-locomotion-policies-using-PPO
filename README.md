# Locomotion Policy Robustness Under Sim-to-Real Gap

## Problem
Policies trained in simulation often fail on real hardware due to 
physics mismatch. But how much mismatch can a policy tolerate — 
and can we measure this before deploying?

## What I will build
- PPO locomotion policy on PyBullet quadruped
- Domain randomized training (gravity, friction, mass)
- Systematic robustness sweep across physics perturbation levels
- Deployability threshold metric: the perturbation level at which 
  reward drops below 50% of nominal performance

##Folder structure:
legged-locomotion-rl/
├── .vscode/
│   └── settings.json
├── env/
│   ├── __init__.py
│   ├── quadruped_env.py
│   └── perturbed_env.py
├── results/
│   ├── comparison.gif
│   ├── degradation_curve.png
│   └── robustness_heatmap.png
├── train.py
├── evaluate.py
├── robustness_sweep.py
├── visualize.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
