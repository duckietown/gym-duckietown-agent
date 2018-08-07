# gym-duckietown-agent

[![Docker Build Status](https://img.shields.io/docker/pulls/duckietown/gym-duckietown-agent.svg)](https://hub.docker.com/r/duckietown/gym-duckietown-agent)

`docker build -t duckietown/duckietown-gym-agent`

Clone this repo:

    git clone https://github.com/duckietown/gym-duckietown-agent.git
    
Change into that directory

    cd gym-duckietown-agent
    
Start containers (make sure to always have the latest simulator). During the first start this will download the ~2GB `duckietown/gym-duckietown-server` container. This might take a while depending on your internet speed. Afterwards this will build the `gym-duckietown-agent` container, which also might take a few minuts the first time. Successive starts should be ignificantly faster.


**to run the LF task**:

    docker-compose -f docker-compose-lf.yml pull && \
    docker-compose -f docker-compose-lf.yml up 

or

**to run the LFV task**:

    docker-compose -f docker-compose-lfv.yml pull && \
    docker-compose -f docker-compose-lfv.yml up

This should give you a reward output like 
    
    gym-duckietown-agent_1   | starting sub socket on 8902
    gym-duckietown-agent_1   | listening for camera images
    gym-duckietown-agent_1   | [Challenge: LF] The average reward of 10 episodes was -315.7005. Best episode: -283.9803, worst episode: -368.1122
    gym-duckietown-agent_gym-duckietown-agent_1 exited with code 0

(The important bit is the second last line here)

You can now end the run by pressing <kbd>CTRL</kbd>+<kbd>c</kbd>.

Now edit the file `agent.py`, run the command `docker-compose pull && docker-compose up` again and try to improve your score.

Good luck :)

## Running

### x86

`docker run duckietown/duckietown-gym-agent`

### Raspberry Pi

`docker run duckietown/duckietown-gym-agent:arm`

## Building

Docker images for x86 and ARM are automatically rebuilt from this GitHub repository, however you can also rebuild them yourself.

To do so, first `cd` to the root directory of this project on your local machine. Then, depending on which platform you are targeting, run one of the following commands:

### x86

`docker build -t duckietown/duckietown-gym-agent .`

### Raspberry Pi

`docker build --file docker/rpi/Dockerfile -t duckietown/duckietown-gym-agent:arm .`
