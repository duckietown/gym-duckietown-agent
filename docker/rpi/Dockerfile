FROM resin/raspberrypi3-python:3.4

RUN [ "cross-build-start" ]

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone -b v0.3.1 --recursive https://github.com/pytorch/pytorch

WORKDIR /pytorch

RUN git config user.email foo@foo && git config user.name foo && git cherry-pick af8b64aadca379397ff27c135eccb1cfaee5f524

RUN sed -i 's/jessie/stretch/g' /etc/apt/sources.list && apt-get update && apt-get install --no-install-recommends -y gcc-6 g++-6 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install --no-install-recommends -y \
	libopenblas-dev \
	cython \
	libatlas-dev \
	m4 \
	libblas-dev \
	cmake \
	make \
	wget \
	libffi-dev && \
	rm -rf /var/lib/apt/lists/* 

#https://gist.github.com/fgolemo/e19ef13183f1a4b5b59c24ae2ae31273
RUN pip3 install \
    setuptools \
    matplotlib \
    wheel \
    typing \
    numpy \
    scipy \
    pyyaml \
    cffi \
    --index-url https://www.piwheels.org/simple

ARG CC=/usr/bin/gcc-6
ARG CXX=/usr/bin/g++-6

RUN wget https://cmake.org/files/v3.4/cmake-3.4.1.tar.gz && \
    tar -xvzf cmake-3.4.1.tar.gz && \
    cd cmake-3.4.1 && \
    ./bootstrap && \
    make && \
    make install && \
    rm -rf ../cmake-3.4.1.tar.gz

RUN NO_CUDA=1 NO_DISTRIBUTED=1 python3 setup.py build install

WORKDIR /workspace

#This file is expected by duckietown-slimremote, but this directory is read-only
#TODO: Instead, we should be setting an environement parameter for RPi and read that from duckietown-slimremote/setup.py
#RUN mkdir -p  /sys/firmware/devicetree/base
#RUN echo "Raspberry" > /sys/firmware/devicetree/base/model

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends git && \
    pip install -e git+https://github.com/duckietown/duckietown-slimremote.git#egg=duckietown-slimremote && \
    rm -rf /var/lib/apt/lists/*

COPY . agent

RUN pip install -e agent

RUN [ "cross-build-end" ]

CMD python agent/agent.py --no-render
