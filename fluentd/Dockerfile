# for kibana

FROM centos:6
MAINTAINER Takeru Ohta <phjgt308@gmail.com>

# yum packages
RUN yum -y install curl libcurl-devel wget unzip which git vim emacs gcc

# Fluentd
RUN curl -L http://toolbelt.treasuredata.com/sh/install-redhat.sh | sed -E 's/sudo|sudo -k//g' | sh
RUN /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-elasticsearch

# 9880=fluentd
EXPOSE 9880

CMD service td-agent start && /bin/bash