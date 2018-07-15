FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda.sh && \
    sh ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh
ENV PATH /opt/conda/bin:$PATH

RUN conda install numpy scipy matplotlib && \
    conda install -c pytorch magma-cuda91 && \
    conda clean -ya

WORKDIR /workspace

# Manually incremented on a major change to duckietown/gym-duckietown to force
# a rebuild starting from this line
ENV force-docker-rebuild 3

RUN pip install -e git+https://github.com/duckietown/duckietown-slimremote#egg=duckietown-slimremote

COPY . /workspace/agent
RUN pip install -e /workspace/agent

ENTRYPOINT ["python", "/workspace/agent/agent.py"]
