FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

ADD https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh miniconda.sh

RUN sh miniconda.sh -b -p /opt/conda && rm miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda install numpy scipy matplotlib && \
    conda install -c pytorch magma-cuda91 && \
    conda clean -ya

WORKDIR workspace

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends git && \
    pip install -e git+https://github.com/duckietown/duckietown-slimremote.git#egg=duckietown-slimremote && \
    rm -rf /var/lib/apt/lists/*

COPY . agent

RUN pip install -e agent

CMD python agent/agent.py --no-render
