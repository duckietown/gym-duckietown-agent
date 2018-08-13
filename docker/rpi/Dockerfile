FROM duckietown/pytorch

RUN [ "cross-build-start" ]

WORKDIR /workspace

#This file is expected by duckietown-slimremote, but this directory is read-only
#TODO: Instead, we should be setting an environement parameter for RPi and read that from duckietown-slimremote/setup.py
#RUN mkdir -p  /sys/firmware/devicetree/base
#RUN echo "Raspberry" > /sys/firmware/devicetree/base/model

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends git \
    python-dev \
    build-essential \
    libatlas-base-dev && \
    pip install -e git+https://github.com/duckietown/duckietown-slimremote.git#egg=duckietown-slimremote && \
    apt-get remove -y git && \
    rm -rf /var/lib/apt/lists/*

COPY . agent

RUN pip install -e agent

RUN [ "cross-build-end" ]

CMD python agent/agent.py --no-render
