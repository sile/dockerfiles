FROM centos:6
MAINTAINER Takeru Ohta <phjgt308@gmail.com>

# yum packages
RUN yum -y install curl gcc vim tar rpm-build ncurses-devel openssl-devel m4

# Erlang
RUN mkdir -p /tmp/rpm/SOURCES
RUN curl http://www.erlang.org/download/otp_src_17.5.tar.gz -o /tmp/rpm/SOURCES/otp_src_17.5.tar.gz

# gcc-4.8
RUN curl http://people.centos.org/tru/devtools-2/devtools-2.repo -o /etc/yum.repos.d/devtools-2.repo
RUN yum install -y devtoolset-2-gcc devtoolset-2-binutils

# RPM
ADD erlang.spec /tmp/erlang.spec
RUN scl enable devtoolset-2 'rpmbuild -bb --define "_topdir /tmp/rpm" /tmp/erlang.spec'

# CMD
CMD rpm -ivh /tmp/rpm/RPMS/x86_64/erlang-OTP17.5-1.native.x86_64.rpm && /bin/bash
