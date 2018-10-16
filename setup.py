from setuptools import setup

setup(
    name='gym_duckietown_agent',
    version='2018.8.3',
    keywords='duckietown, environment, agent, rl, openaigym, openai-gym, gym',
    install_requires=[
        'gym>=0.9.0',
        'numpy>=1.10.0',
        'duckietown_slimremote>=2018.8.3',
        'matplotlib',
        'tqdm>=4.0.0'
    ]
)
