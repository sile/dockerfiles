# for kibana
# http://d.hatena.ne.jp/yk5656/20140516/1401636399

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

# 80=httpd, 8080=fluentd
EXPOSE 80
EXPOSE 8080

CMD start_kibana && /bin/bash
