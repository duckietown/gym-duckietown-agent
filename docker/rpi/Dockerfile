FROM duckietown/pytorch

RUN [ "cross-build-start" ]

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

RUN apt-get update && apt-get install --no-install-recommends -y \
        libatlas-base-dev && \
    rm -rf /var/lib/apt/lists/* 

RUN [ "cross-build-end" ]

CMD python agent/agent.py --no-render
