FROM pytorch/pytorch

RUN conda install numpy scipy matplotlib && conda clean -ya

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends git && \
    pip install -e git+https://github.com/duckietown/duckietown-slimremote.git#egg=duckietown-slimremote && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY . agent

RUN pip install -e agent

CMD python agent/agent.py --no-render
