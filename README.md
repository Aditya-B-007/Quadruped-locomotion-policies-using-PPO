```markdown
# Locomotion Policy Robustness Under Sim-to-Real Gap

## Overview

Reinforcement Learning (RL) policies trained in simulation often fail when deployed on real-world hardware due to discrepancies in physical dynamics. This project investigates **how much simulation mismatch a locomotion policy can tolerate** and introduces a measurable **deployability threshold** before real-world transfer.

The focus is on training a quadruped locomotion policy using **Proximal Policy Optimization (PPO)** in a simulated environment, applying **domain randomization**, and systematically evaluating robustness under controlled perturbations.

---

## Problem Statement

Simulation environments cannot perfectly replicate real-world physics. Variations in:

- Gravity  
- Friction  
- Mass distribution  

lead to performance degradation when policies are transferred to real robots.

This project aims to:

- Quantify robustness of trained policies  
- Measure tolerance to physics mismatch  
- Define a threshold for safe deployment  

---

## Key Idea

A policy is considered **deployable** if it maintains at least:

> **50% of its nominal (unperturbed) performance**

The **deployability threshold** is defined as:

> The maximum perturbation level at which reward ≥ 50% of nominal reward

---

## Features

- PPO-based locomotion training
- PyBullet quadruped simulation
- Domain randomization during training
- Systematic robustness evaluation
- Performance degradation analysis
- Visualization of robustness metrics

---

## Project Structure

```

legged-locomotion-rl/
│
├── .vscode/
│   └── settings.json
│
├── env/
│   ├── **init**.py
│   ├── quadruped_env.py        # Base environment
│   └── perturbed_env.py        # Environment with physics perturbations
│
├── results/
│   ├── comparison.gif          # Visual comparison of policies
│   ├── degradation_curve.png   # Reward vs perturbation
│   └── robustness_heatmap.png  # Multi-parameter robustness visualization
│
├── train.py                    # PPO training script
├── evaluate.py                 # Evaluate trained policy
├── robustness_sweep.py         # Run perturbation experiments
├── visualize.py                # Generate plots and GIFs
├── config.py                   # Hyperparameters and configs
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

```

---

## Methodology

### 1. Base Training
- Train a locomotion policy using PPO
- Environment: PyBullet quadruped
- Objective: maximize forward velocity while maintaining stability

### 2. Domain Randomization
During training, randomly vary:

- Gravity (e.g., 8–12 m/s²)
- Friction coefficients
- Link masses

Purpose: expose policy to diverse dynamics

### 3. Robustness Sweep
After training:

- Freeze the policy
- Apply controlled perturbations
- Measure performance degradation

### 4. Deployability Metric
Compute:

```

Deployability Threshold = max perturbation level
where reward ≥ 0.5 × nominal reward

````

---

## Installation

```bash
git clone https://github.com/your-username/legged-locomotion-rl.git
cd legged-locomotion-rl

pip install -r requirements.txt
````

---

## Usage

### Train Policy

```bash
python train.py
```

### Evaluate Policy

```bash
python evaluate.py
```

### Run Robustness Sweep

```bash
python robustness_sweep.py
```

### Generate Visualizations

```bash
python visualize.py
```

---

## Outputs

* **Degradation Curve**
  Shows how reward declines with increasing perturbation

* **Robustness Heatmap**
  Visualizes sensitivity across multiple physics parameters

* **Comparison GIF**
  Side-by-side behavior under nominal vs perturbed conditions

---

## Future Extensions

* Transfer to real quadruped hardware
* Sim-to-real fine-tuning using real trajectories
* Use of adaptive or meta-RL policies
* Integration with MuJoCo / Isaac Gym for scalability

---

## Tech Stack

* Python
* PyBullet
* Stable-Baselines3
* NumPy / Matplotlib
* Gymnasium

---

## Contribution

Contributions are welcome. Open an issue or submit a pull request with improvements or extensions.

```
```
