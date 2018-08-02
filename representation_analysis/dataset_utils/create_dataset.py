# Please note that this does not work. Because we cannot directly interact with the environment
# And yet to figure out how this works

import gym
import gym_duckietown_agent
from PIL import Image
import numpy as np

env = gym.make("SimpleSim-Agent-v0")
num_samples = 10

for i in range(num_samples):
    obs = env.reset()
    img = Image.fromarray(np.flipud((obs* 255)).astype('uint8'))
    img.save(fp='representation_analysis/trajectories/{}.jpg'.format(i))
    if i+1 % 1000 == 0:
        print('got to sample {}'.format(i))
env.close()


# A better parallelized version of this code is yet to be uploaded