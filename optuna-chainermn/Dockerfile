FROM python:3

RUN apt update && apt install -y openmpi-bin libopenmpi-dev emacs
RUN pip install mpi4py pytest optuna chainer==5.4.0
RUN git clone git://github.com/pfnet/optuna.git
