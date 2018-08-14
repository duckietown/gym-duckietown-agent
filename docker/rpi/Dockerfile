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
    pkg-config \
    libpng-dev \
    build-essential \
    libfreetype6-dev \
    libatlas-base-dev && \
    pip install -e git+https://github.com/duckietown/duckietown-slimremote.git#egg=duckietown-slimremote && \
    apt-get remove -y git && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends libpng12-dev && \
    rm -rf /var/lib/apt/lists/*

#RUN wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb && \
#    dpkg -i /tmp/libpng12.deb && \
#    rm /tmp/libpng12.deb
COPY . agent

RUN pip install -e agent

#RUN pip uninstall -y matplotlib && pip install matplotlib

RUN [ "cross-build-end" ]

CMD python agent/agent.py --no-render
