from setuptools import setup


def get_version(filename):
    import ast
    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in %r.' % filename)
    if version is None:
        raise ValueError(filename)
    return version


version = get_version(filename='gym_duckietown_agent/__init__.py')

setup(
    name='gym_duckietown_agent',
    version=version,
    keywords='duckietown, environment, agent, rl, openaigym, openai-gym, gym',
    install_requires=[
        'gym>=0.9.0',
        'numpy>=1.10.0',
        'duckietown_slimremote>=2018.8.5',
        'matplotlib',
        'tqdm>=4.0.0'
    ]
)
