FROM resin/raspberrypi3-alpine-python:3.4-slim

RUN [ "cross-build-start" ]

# Clone Pytorch
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    git clone -b v0.3.1 --recursive https://github.com/pytorch/pytorch && \
    cd pytorch && \
    git config user.email foo@foo && \
    git config user.name foo && \
    git cherry-pick af8b64aadca379397ff27c135eccb1cfaee5f524 && \
    apt-get remove git -y && \
    rm -rf /var/lib/apt/lists/*

# Install build deps
RUN sed -i 's/jessie/stretch/g' /etc/apt/sources.list && \
    apt-get update && apt-get install --no-install-recommends -y \
    gcc-6 \
    libopenblas-dev \
    libatlas-dev \
    m4 \
    libblas-dev \
    cmake \
    make \
    wget \
    g++-6 \
    libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Don't trust PiWheels numpy. Something is wrong with it...
RUN pip install cython numpy

# Everything else seems to be okay
RUN pip install --index-url https://www.piwheels.org/simple \
    setuptools \
    matplotlib \
    wheel \
    typing \
    scipy \
    pyyaml \
    cffi
    
ARG CC=/usr/bin/gcc-6
ARG CXX=/usr/bin/g++-6

# Make project
RUN wget https://cmake.org/files/v3.4/cmake-3.4.1.tar.gz && \
    tar -xvzf cmake-3.4.1.tar.gz && \
    cd cmake-3.4.1 && \
    ./bootstrap && \
    make && \
    make install && \
    rm -rf ../cmake-3.4.1.tar.gz

WORKDIR pytorch

# Install Pytorch
RUN NO_CUDA=1 NO_DISTRIBUTED=1 python3 setup.py build install

RUN [ "cross-build-end" ]
