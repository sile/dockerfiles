FROM centos:7
MAINTAINER Takeru Ohta <phjgt308@gmail.com>

# yum packages
RUN yum -y install curl gcc vim tar ncurses-devel openssl-devel m4 autoconf make git

# Erlang
RUN curl -L https://github.com/erlang/otp/archive/OTP-21.0-rc1.tar.gz -o /tmp/OTP-21.0-rc1.tar.gz
RUN cd /tmp/ && tar zxvf OTP-21.0-rc1.tar.gz
WORKDIR /tmp/otp-OTP-21.0-rc1
RUN ./otp_build autoconf
RUN ./configure
RUN make
RUN make install

# Rebar3
RUN curl -L https://s3.amazonaws.com/rebar3/rebar3 -o /usr/bin/rebar3 && chmod +x /usr/bin/rebar3

WORKDIR /
CMD /bin/bash
