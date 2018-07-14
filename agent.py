import gym
import gym_duckietown_agent  # don't remove this line
import numpy as np

# How many episodes would you like to use for evaluation?
# This is entirely up to you. For the evaluation we will
# dcide upon an arbitrary (high) number.
EPISODES = 10

# Would you like to see the actions, rewards and other
# informations on each step? Warning, this is very verbose.
DEBUG = False

# Create the gym environment
env = gym.make("SimpleSim-Agent-v0")

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

for episode in range(EPISODES):

    # 500 is the default max episode length for the LF task
    for frame in range(500):

        ### THIS IS WHAT YOU HAVE TO REPLACE WITH MACHINE LEARNING MAGIC - START

        # For demo purposes we just randomly sample an action.
        action = env.action_space.sample()

        ### THIS IS WHAT YOU HAVE TO REPLACE WITH MACHINE LEARNING MAGIC - END

        # We run the action in the simulation and see
        # what's the reward the resulting observation
        obs, rew, done, misc = env.step(action)

        # TODO: we need some more testing if this is still necessary
        # During testing every once in a while the first frame was black.
        # I'm not sure what the conditions are for this to happn reliably.
        if obs is None:
            continue

        if DEBUG:
            print("action {}, reward {}, done {}, misc {}, obs shape {}".format(
                action,
                rew,
                done,
                misc,
                obs.shape
            ))

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

print("The average reward of {} episodes was {}. Best episode: {}, worst episode: {}".format(
    EPISODES,
    np.around(np.mean(rewards), 4),
    np.around(np.max(rewards), 4),
    np.around(np.min(rewards), 4)
))

# This also doesn't do anything, but it follows gym convention.
env.close()
