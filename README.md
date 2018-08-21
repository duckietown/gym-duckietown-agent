# gym-duckietown-agent

[![Docker Hub](https://img.shields.io/docker/pulls/duckietown/gym-duckietown-agent.svg)](https://hub.docker.com/r/duckietown/gym-duckietown-agent)

Welcome to the `gym-duckietown-agent`, the default template for machine learning [AI-DO](https://www.duckietown.org/research/AI-Driving-Olympics) submissions. It runs [PyTorch](https://pytorch.org/), [numpy](https://pytorch.org/), [scipy](https://www.scipy.org/) and some other useful libraries for machine learning, however you can [customize it](#customizing) to your liking.

There are two versions of the `gym-duckietown-agent`, both built from this repository and available on [Docker Hub](https://hub.docker.com/r/duckietown/gym-duckietown-agent). The default version, [`duckietown/gym-duckietown-agent`](https://github.com/duckietown/gym-duckietown-agent/blob/master/Dockerfile), runs on x86 and ARM devices. The GPU enabled version, [`duckietown/gym-duckietown-agent:gpu`](https://github.com/duckietown/gym-duckietown-agent/blob/master/docker/gpu/Dockerfile), runs on x86 or GPU-powered machines with [`nvidia-docker`](https://github.com/NVIDIA/nvidia-docker). Both of these depend on the [`duckietown/gym-duckietown`](https://github.com/duckietown/gym-duckietown) simulator, or a compatible messaging interface. Below, you will find instructions for installing and running a `gym-duckietown-agent` container.

## Prerequisites

To enable fully reproducible software environments, we use a container tool called [Docker](https://www.docker.com/). For your convenience, we have prepared some [reading material about Docker](http://docs.duckietown.org/software_devel/out/docker_intro.html).

* [git](https://git-scm.com/downloads)
* [Docker CE](https://docs.docker.com/install/) or [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) (for GPU acceleration)
* [docker-compose](https://docs.docker.com/compose/install/) - this allows you to "compose" or "orchestrate" multiple Docker containers into a functional system.

## Setup

To get started, fork or clone this git repository and `cd` into the project directory:

    git clone https://github.com/duckietown/gym-duckietown-agent.git && cd gym-duckietown-agent
    
Now, start the Docker containers (always make sure to have the latest simulator). On first start this will download the ~2GB `duckietown/gym-duckietown-server` container. Due to layer caching, successive starts should be significantly faster.

[Several competition challenges](http://docs.duckietown.org/AIDO/out/ml_primer.html) are available to run.

### To run the Lane Following (LF) task:

    docker-compose -f docker-compose-lf.yml pull && \
    docker-compose -f docker-compose-lf.yml up 

### To run the Lane Following with Vehicles (LFV) task:

    docker-compose -f docker-compose-lfv.yml pull && \
    docker-compose -f docker-compose-lfv.yml up

This will give you a reward output like:
    
    gym-duckietown-agent_1   | starting sub socket on 8902
    gym-duckietown-agent_1   | listening for camera images
    gym-duckietown-agent_1   | [Challenge: LF] The average reward of 10 episodes was -315.7005. Best episode: -283.9803, worst episode: -368.1122
    gym-duckietown-agent_gym-duckietown-agent_1 exited with code 0

(The important bit is the second-to-last line above)

You can terminate the run at any time by pressing <kbd>CTRL</kbd>+<kbd>c</kbd>.

By default, Docker will use the ARM-emulator when running on x86, however you can switch to the GPU version by replacing `duckietown/gym-duckietown-agent` with `duckietown/gym-duckietown-agent:gpu` in your `docker-compose*.yml` file.

## Write your own agent

To write your own agent, first fork this repository, and edit the file [`agent.py`](agent.py). Then run the following command from the root directory of this project on your local machine to evaluate the agent's performance:

    docker build -t duckietown/gym-duckietown-agent . && \
    docker-compose -f docker-compose-lf.yml up`

Check the average reward and try to improve your score. Good luck!

## Running

The `duckietown/gym-duckietown-agent[:gpu]` Docker image is based on [PyTorch](https://hub.docker.com/r/pytorch/pytorch/). You can use this image as a template for implementing your own agent. It runs on both x86 and ARM platforms.

### ARM/x86

`docker run -it duckietown/gym-duckietown-agent python -c "import torch; print(torch.randn(10))"`

### GPU

`docker run -it duckietown/gym-duckietown-agent:gpu python -c "import torch; print(torch.randn(10))"`

## Building

Docker images for x86 and ARM are automatically rebuilt from this GitHub repository, however you should rebuild them locally when you want to test changes to the code.

To do so, first `cd` to the project directory on your local machine. Then, depending on whether you are targeting ARM/x86 or GPU, run one of the following commands:

### ARM/x86

`docker build -t duckietown/gym-duckietown-agent .`

### GPU

`docker build --file=docker/gpu/Dockerfile -t duckietown/gym-duckietown-agent:gpu .`

## Submitting

When the competition opens, you will [submit](https://github.com/duckietown/duckietown-shell#ai-do-submissions) your Docker image `dt`, the [Duckietown Shell](https://github.com/duckietown/duckietown-shell):

    dt aido18 submit <YOUR_DOCKER_HUB_USERNAME>/<YOUR_IMAGE_BASED_ON_GYM_DUCKIETOWN_AGENT>

This Docker image will contain a pretrained model. If you send us a GPU model, we will run it on the simulator only. If you send us an ARM image, we will evaluate the submission and run it on a physical robot, then send you a link to the log.

Subsequently, we will evaluate it on some randomized environments, and rank your submission on a leaderboard. Should you wish to participate in the robotarium challenge, you will need to submit an ARM-based image.

## Customizing

By default, we provide a working PyTorch installation, however you can customize the `duckietown/gym-duckietown-agent` Dockerfile to use your favorite machine learning libraries. The only hard requirement is [`duckietown-slimremote`](https://github.com/duckietown/duckietown-slimremote) to interact with the simulator and this template. Here are some other popular machine learning libraries:

* [TensorFlow](https://www.tensorflow.org/) ([works on RPi](https://www.tensorflow.org/install/install_raspbian))
* [mxnet](https://mxnet.apache.org/) ([also works on RPi](https://mxnet.incubator.apache.org/tutorials/embedded/wine_detector.html))

To customize the default distribution, modify the [`Dockerfile`](Dockerfile) (or [`docker/gpu/Dockerfile`](docker/gpu/Dockerfile) if you are using a GPU) and rebuild the image using the [build instructions](#building).
