import gym
import gym_duckietown_agent  # don't remove this line
import numpy as np
import argparse
import curses

# Let's set this to one episode because manual control
# takes a lot of time. For evaluating your policy this
# should be higher like 10 or 100 to average out the
# randomness
from gym_duckietown_agent.utils.keyboard import handleKey

EPISODES = 1


# Create the gym environment (in this case the silent one)
# because we don't want any print statements to interfere
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

# Let's initialize the ncurses terminal "window"
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.addstr(0,0,"Hit 'q' to quit. Use arrow keys to drive.")
stdscr.refresh()

for episode in range(EPISODES):

    # 500 is the default max episode length for the LF task
    for frame in range(500):

        key = stdscr.getch()
        stdscr.refresh()
        action = handleKey(key, stdscr)

        if action is None:
            break


        # We run the action in the simulation and see
        # what's the reward the resulting observation
        obs, rew, done, misc = env.step(action)

        # We receive the name of the challenge at every time step - just to
        # make sure we are solving the correct task
        challenge = misc["challenge"]

        stdscr.addstr(2, 0, "action {}, reward {}, done {}, misc {}, obs shape {}".format(
            action,
            np.around(rew,3),
            done,
            misc,
            obs.shape
        ))

        env.render("human") # this might fail if run in a container

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

# This also doesn't do anything, but it follows gym convention.
env.close()

# ...but this we need
curses.endwin()

print("[Challenge: {}] The average reward of {} episodes was {}. Best episode: {}, worst episode: {}".format(
    challenge,
    EPISODES,
    np.around(np.mean(rewards), 4),
    np.around(np.max(rewards), 4),
    np.around(np.min(rewards), 4)
))