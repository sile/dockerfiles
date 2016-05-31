FROM centos:7

MAINTAINER takeru_ohta <phjgt308@gmail.com>

RUN yum -y install vim git
RUN yum -y install tar
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh -s -- --disable-sudo

CMD /bin/bash
