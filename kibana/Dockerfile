# for kibana

FROM centos:6
MAINTAINER Takeru Ohta <phjgt308@gmail.com>

# yum packages
RUN yum -y install curl libcurl-devel wget unzip which git vim emacs gcc java-1.7.0-openjdk httpd

# Elasticsearch
RUN rpm -ivh https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.3.noarch.rpm
RUN echo 'http.cors.allow-origin: "/.*/"' >> /etc/elasticsearch/elasticsearch.yml
RUN echo 'http.cors.enabled: true' >> /etc/elasticsearch/elasticsearch.yml

# Fluentd
RUN curl -L http://toolbelt.treasuredata.com/sh/install-redhat.sh | sed -E 's/sudo|sudo -k//g' | sh
RUN /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-elasticsearch

# Kibana
RUN wget http://download.elasticsearch.org/kibana/kibana/kibana-latest.zip
RUN unzip kibana-latest.zip
RUN mv kibana-latest /var/www/html/kibana

ADD start.sh /usr/local/bin/start_kibana
ADD td-agent.conf.template /tmp/td-agent.conf.template
RUN cat /tmp/td-agent.conf.template >> /etc/td-agent/td-agent.conf

# 80=httpd, 8080=fluentd
EXPOSE 80
EXPOSE 9880

CMD start_kibana && /bin/bash
