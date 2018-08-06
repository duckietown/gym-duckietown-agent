from gym.envs.registration import register

register(
    id='Duckietown-Lf-Lfv-Navv-v0',
    entry_point='gym_duckietown_agent.envs:SimpleSimAgentEnv',
    timestep_limit=500,
    reward_threshold=900,
)
