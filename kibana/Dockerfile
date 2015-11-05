# for kibana

FROM centos:7
MAINTAINER Takeru Ohta <phjgt308@gmail.com>

# yum packages
RUN yum -y install curl libcurl-devel which git vim emacs gcc java-1.8.0-openjdk initscripts tar

# Elasticsearch
RUN rpm -ivh https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/rpm/elasticsearch/2.0.0/elasticsearch-2.0.0.rpm
RUN echo 'http.cors.allow-origin: "/.*/"' >> /etc/elasticsearch/elasticsearch.yml
RUN echo 'http.cors.enabled: true' >> /etc/elasticsearch/elasticsearch.yml

# Fluentd
RUN curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent2.sh | sed -E 's/sudo//g' | sh
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-elasticsearch --no-ri --no-rdoc -V

# Kibana
RUN curl https://download.elastic.co/kibana/kibana/kibana-4.2.0-linux-x64.tar.gz | tar zxf -
RUN mv kibana*/ /opt/kibana

ADD start.sh /usr/local/bin/start_kibana
ADD td-agent.conf.template /tmp/td-agent.conf.template
RUN cat /tmp/td-agent.conf.template >> /etc/td-agent/td-agent.conf

# 5601=kibana, 9880=fluentd
EXPOSE 5601
EXPOSE 9880

CMD start_kibana && /bin/bash
