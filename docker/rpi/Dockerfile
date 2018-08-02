FROM resin/armv7hf-debian

RUN [ "cross-build-start" ]

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

RUN git clone -b v0.3.1 --recursive https://github.com/pytorch/pytorch ./pytorch
WORKDIR /usr/src/app/pytorch

RUN git config user.email foo@foo && git config user.name foo && git cherry-pick af8b64aadca379397ff27c135eccb1cfaee5f524

RUN sed -i 's/jessie/stretch/g' /etc/apt/sources.list && apt-get update && apt-get install --no-install-recommends -y gcc-6 g++-6 && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install --no-install-recommends -y libopenblas-dev cython libatlas-dev m4 libblas-dev python3-dev cmake python3-yaml python3-pip python3-setuptools git make wget libffi-dev && rm -rf /var/lib/apt/lists/* 

#https://gist.github.com/fgolemo/e19ef13183f1a4b5b59c24ae2ae31273
RUN pip3 install setuptools wheel typing numpy pyyaml cffi --index-url https://www.piwheels.org/simple
ARG CC=/usr/bin/gcc-6
ARG CXX=/usr/bin/g++-6

RUN wget https://cmake.org/files/v3.4/cmake-3.4.1.tar.gz && tar -xvzf cmake-3.4.1.tar.gz && cd cmake-3.4.1 && ./bootstrap && make && make install && cd .. && rm -rf cmake-3.4.1.tar.gz

RUN NO_CUDA=1 NO_DISTRIBUTED=1 python3 setup.py build

RUN [ "cross-build-end" ]
CMD [ "/bin/bash" ]
