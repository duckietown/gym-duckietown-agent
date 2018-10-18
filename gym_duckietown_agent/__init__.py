from gym.envs.registration import register

register(
    id='Duckietown-Lf-Lfv-Navv-v0',
    entry_point='gym_duckietown_agent.envs:SimpleSimAgentEnv',
    timestep_limit=500,
    reward_threshold=900,
    kwargs={"silent": False, 'camera_width': 160, 'camera_height': 120}
)

# this environment is the same as the one above, but doesn't have any 'print's
register(
    id='Duckietown-Lf-Lfv-Navv-Silent-v0',
    entry_point='gym_duckietown_agent.envs:SimpleSimAgentEnv',
    timestep_limit=500,
    reward_threshold=900,
    kwargs={"silent": True, 'camera_width': 160, 'camera_height': 120}
)

register(
    id='Duckietown-Lf-Lfv-Navv-Silent-v1',
    entry_point='gym_duckietown_agent.envs:SimpleSimAgentEnv',
    timestep_limit=5000000,
    reward_threshold=900,
    kwargs={"silent": True, 'camera_width': 640, 'camera_height': 480}
)
