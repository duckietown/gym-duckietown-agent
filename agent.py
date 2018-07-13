import gym
import gym_duckietown_agent # don't remove this line
import numpy as np

EPISODES = 10
DEBUG = False

env = gym.make("SimpleSim-Agent-v0")

env.reset()

rewards = []
reward_buf = 0


for episode in range(EPISODES):
    for frame in range(500):


        ### THIS IS WHAT YOU HAVE TO REPLACE WITH MACHINE LEARNING MAGIC - START

        # for demo purposes we just randomly sample an action.
        action = env.action_space.sample()

        ### THIS IS WHAT YOU HAVE TO REPLACE WITH MACHINE LEARNING MAGIC - END


        # we run the action in the simulation and see
        # what's the reward the resulting observation
        obs, rew, done, misc = env.step(action)

        if obs is None:
            continue # need to check for this

        if DEBUG:
            print("action {}, reward {}, done {}, misc {}, obs shape {}".format(
                action,
                rew,
                done,
                misc,
                obs.shape
            ))

        # add reward to buffer
        reward_buf += rew

        if done:
            # if the environment is done (duckie stepped out of bounds or
            # collided) then this episode is over and we reset the environment
            break

    # reset the simulation
    env.reset()

    # add cumulative episode reward to buffer and reset the buffer
    rewards.append(reward_buf)
    reward_buf = 0


print ("The average reward of {} episodes was {}. Best episode: {}, worst episode: {}".format(
    EPISODES,
    np.around(np.mean(rewards),4),
    np.around(np.max(rewards),4),
    np.around(np.min(rewards),4)
))

env.close()