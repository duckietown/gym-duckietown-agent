from gym.envs.registration import register

register(
    id='SimpleSim-Agent-v0',
    entry_point='gym_duckietown_agent.envs:SimpleSimAgentEnv',
    timestep_limit=500,
    reward_threshold=900,
)

register(
    id='SimpleSim-Agent-Debug-v0',
    entry_point='gym_duckietown_agent.envs:SimpleSimAgentEnv',
    timestep_limit=500,
    reward_threshold=900,
    kwargs={'debug': True}
)

