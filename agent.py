from __future__ import print_function
import gym
from tqdm import tqdm
import gym_duckietown_agent  # don't remove this line
import numpy as np
import argparse

parser = argparse.ArgumentParser(
    description='This is just here to set some '
                'variables on startup')
parser.add_argument("--no-render", action="store_true",
                    help="add this flag if you are running "
                         "this script inside the docker "
                         "container, so that matplotlib "
                         "doesn't try to load a graphical "
                         "backend in a headless server.")
args = parser.parse_args()

# How many episodes would you like to use for evaluation?
# This is entirely up to you. For the evaluation we will
# dcide upon an arbitrary (high) number.
EPISODES = 10

# Would you like to see the actions, rewards and other
# informations on each step? Warning, this is very verbose.
DEBUG = False

# Would you like to see the robot's camera?
SHOW_CAMERA = True

# if the script runs in a headless docker container
# we _must_ set SHOW_CAMERA to false anyway.
if args.no_render:
    SHOW_CAMERA = False  # We recommend you don't change this

# Create the gym environment
env = gym.make("Duckietown-Lf-Lfv-Navv-Silent-v0")

# Initialize. This is mainly here because it follows the
# gym convention. There are however few cases where the
# simulation is already running and you might wanna call
# this first to make sure the sim is reset.
env.reset()

# For each of the EPISODES we collect the final reward in
# this list and at the very end average it.
rewards = []

# In each episode we gather the rewards by adding it to
# this variable.
reward_buf = 0.0

challenge = None

# we are wrapping the iterator in TQDM because that gives
# us a nice progress bar
for episode in tqdm(range(EPISODES), desc="episode"):

    # 500 is the default max episode length for the LF/LFV task
    for frame in tqdm(range(500), desc="frame"):

        ### THIS IS WHAT YOU HAVE TO REPLACE WITH MACHINE LEARNING MAGIC - START

        # For demo purposes we just randomly sample an action.
        action = env.action_space.sample()

        ### THIS IS WHAT YOU HAVE TO REPLACE WITH MACHINE LEARNING MAGIC - END

        # We run the action in the simulation and see
        # what's the reward the resulting observation
        obs, rew, done, misc = env.step(action)

        # We receive the name of the challenge at every time step - just to
        # make sure we are solving the correct task
        challenge = misc["challenge"]

        if DEBUG:
            print("action {}, reward {}, done {}, misc {}, obs shape {}".format(
                action,
                rew,
                done,
                misc,
                obs.shape
            ))

        if SHOW_CAMERA:
            env.render("human")  # this might fail if run in a container

        # Add reward to buffer
        reward_buf += rew

        if done:
            # If the environment is done (duckie stepped out of bounds or
            # collided) then this episode is over and we reset the environment
            break

    # Reset the simulation
    env.reset()

    # Add cumulative episode reward to buffer and reset the buffer
    rewards.append(reward_buf)
    reward_buf = 0

print("\n."*5, flush=True) # this is due to TQDM - to create space

print("[Challenge: {}] The average reward of {} episodes was {}. "
      "Best episode: {}, worst episode: {}".format(
    challenge,
    EPISODES,
    np.around(np.mean(rewards), 4),
    np.around(np.max(rewards), 4),
    np.around(np.min(rewards), 4)
))

# This also doesn't do anything, but it follows gym convention.
env.close()
