#! /bin/bash

set -e

service elasticsearch start
service td-agent start
/opt/kibana/bin/kibana -q &
