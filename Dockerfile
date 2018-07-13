FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update -y && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         ca-certificates &&\
     rm -rf /var/lib/apt/lists/*

RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install numpy scipy matplotlib && \
     /opt/conda/bin/conda install -c pytorch magma-cuda90 && \
     /opt/conda/bin/conda clean -ya
ENV PATH /opt/conda/bin:$PATH


WORKDIR /workspace
RUN chmod -R a+w /workspace

# this next line is manually incremented every time
# we push major changes to the gym-duckietown repo,
# so that docker forces a rebuild starting at this line
ENV force-docker-rebuild 3

RUN git clone https://github.com/duckietown/duckietown-slimremote && cd duckietown-slimremote && pip install -e . && cd ..

COPY . /workspace/agent
RUN cd /workspace/agent && pip install -e .

ENTRYPOINT ["python","/workspace/agent/agent.py"]
