import os

import gym
from duckietown_slimremote.pc.robot import RemoteRobot
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

from gym_duckietown_agent.config import CAMERA_HEIGHT, CAMERA_WIDTH


class SimpleSimAgentEnv(gym.Env):
    """
    Simple road simulator to test RL training.
    Draws a road with turns using OpenGL, and simulates
    basic differential-drive dynamics.
    """

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 30 # do we need this on the client?
    }

    def __init__(self, debug=False):

        # Produce graphical output
        self.debug = debug

        # in the docker container this will be set to point to the
        # hostname of the `gym-duckietown-server` container, but in
        # the local test environment this will just map to localhost
        host = os.getenv("DUCKIETOWN_SERVER", "localhost")


        # Create ZMQ connection
        self.sim = RemoteRobot(host)


        # Tuple of velocity and steering angle, each in the range
        # [-1, 1] for full speed ahead, full speed backward, full
        # left turn, and full right turn respectively
        self.action_space = spaces.Box(
            low=-1,
            high=1,
            shape=(2,),
            dtype=np.float32
        )

        # We observe an RGB image with pixels in [0, 255]
        # Note: the pixels are in uint8 format because this is more compact
        # than float32 if sent over the network or stored in a dataset
        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(CAMERA_HEIGHT, CAMERA_WIDTH, 3),
            dtype=np.uint8
        )

        self.reward_range = (-1000, 1000)


        # Initialize the state
        self.seed()
        self.reset() # FIXME: I'm quite sure this has to be called by the agent, like by gym convention

    def reset(self):
        """
        Reset the simulation at the start of a new episode
        This also randomizes many environment parameters (domain randomization)
        """

        raise NotImplementedError

        pass


    def close(self):
        """
        Doesn't do anything,
        but should be used to end the simulation by gym convention
        """


        pass

    def seed(self, seed=None):
        self.np_random, _ = seeding.np_random(seed)
        return [seed]


    def step(self, action):
        raise NotImplementedError

        pass


    def render(self, mode='human', close=False):
        raise NotImplementedError

        pass

