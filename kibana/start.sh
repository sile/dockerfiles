#! /bin/bash

set -e

service elasticsearch start
service httpd start
service td-agent start
