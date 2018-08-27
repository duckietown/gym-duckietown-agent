import os
import time

import gym
from duckietown_slimremote.pc.robot import RemoteRobot
from gym import spaces
import numpy as np

from gym_duckietown_agent.config import CAMERA_HEIGHT, CAMERA_WIDTH
from matplotlib import pyplot as plt


class SimpleSimAgentEnv(gym.Env):
    """
    Remote client for the simple Duckietown road simulator.
    Draws a road with turns using OpenGL, and simulates
    basic differential-drive dynamics.
    """

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30  # TODO: do we need this on the client?
    }

    def __init__(self, silent=False):
        # Produce the occasional print
        self.silent = silent

        # In the docker container this will be set to point to the
        # hostname of the `gym-duckietown-server` container, but in
        # the local test environment this will just map to localhost
        host = os.getenv("DUCKIETOWN_SERVER", "localhost")

        # Create ZMQ connection
        self.sim = RemoteRobot(host, silent=self.silent)

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

        # Create a black image buffer for the last observation
        self.last_obs = np.zeros((CAMERA_HEIGHT, CAMERA_WIDTH, 3), np.uint8)

        self.reward_range = (-1000, 1000)

        self._windows_exists = False

        # Initialize the state
        self.seed()
        #self.reset()  # FIXME: I'm quite sure this has to be called by the agent by gym convention

    def reset(self):
        """
        Reset the simulation at the start of a new episode
        This also randomizes many environment parameters (domain randomization)
        """

        return self.sim.reset()

    def close(self):
        """
        Doesn't do anything,
        but should be used to end the simulation by gym convention
        """

        pass

    def seed(self, seed=None):
        # TODO: for now this function doesn't do anything.
        # The seed is on the side of the server. Therefore we
        # must transmit the seed to the server. But what if the
        # server is already running and seeded?

        # self.np_random, _ = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        """ Steps the simulation. Run action and get observation and reward.

        :param action: tuple|list|ndarray of exactly 2 floating point values
        each in range [-1,1] indicating the forward/backward speed and the
        steering angle respectively.

        :return: tuple of observation (image as ndarray), reward (float
        scalar), done (bool), misc (empty dict)
        """
        assert len(action) == 2
        action = np.array(action)


        obs, rew, done, misc = self.sim.step(action, with_observation=True)

        return obs, rew, done, misc

    def _create_window(self):
        """ Create a new matplotlib window if none exists to render
        observations.

        :return:
        """


        ## This following bit is important because duckietown_slimremote
        ## uses the Agg backend natively to prevent errors on headless
        ## servers. So if we want to use matplotlib we have to switch
        ## the backend

        import matplotlib
        from matplotlib import pyplot as plt
        gui_env = ['TKAgg', 'GTKAgg', 'Qt4Agg', 'WXAgg']
        for gui in gui_env:
            try:
                plt.switch_backend(gui)
                break
            except:
                continue

        if not self.silent:
            print("Using Matplotlib backend:", matplotlib.get_backend())

        ## actually create the render window
        plt.ion()
        img = np.zeros((CAMERA_HEIGHT, CAMERA_WIDTH, 3))
        self._plt_img = plt.imshow(img, interpolation='none', animated=True, label="Duckiebot Camera")
        self._plt_ax = plt.gca()

    def _draw_window(self, obs):
        """ Update the matplotlib observation window.

        :param obs:
        :return:
        """
        if obs is not None:
            self._plt_img.set_data(obs)
            self._plt_ax.plot([0])
            plt.pause(0.001)  # I found this necessary - otherwise no visible img

    def render(self, mode='human', close=False):
        """ Either create a matplotlib window of the last observation
        or return the last observation as ndarray.

        :param mode: string, possible values are "human" for rendering the
        observations in a matplotlib window and "rgb_array" to return the
        last observation as ndarray.
        :param close:
        :return:
        """
        obs, _, _, _ = self.sim.observe()
        if mode == "rgb_array":
            return obs
        else:
            if not self._windows_exists:
                self._create_window()
                self._windows_exists = True
            self._draw_window(obs)
