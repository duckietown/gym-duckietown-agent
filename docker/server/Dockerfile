FROM continuumio/miniconda3

RUN conda install numpy pyyaml scipy pyzmq && conda clean -ya

WORKDIR /workspace
RUN chmod -R a+w /workspace
RUN git clone http://github.com/duckietown/duckietown-slimremote && cd duckietown-slimremote && pip install -e .
RUN git clone http://github.com/duckietown/gym-duckietown && cd gym-duckietown && pip install -e .

EXPOSE 5558 8902
ENTRYPOINT ["duckietown-start-gym"]
