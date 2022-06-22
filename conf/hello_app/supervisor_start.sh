#! /bin/bash

# A script for installing configuration files and running supervisord. Do NOT run manually

PROJECT_DIR=$(pwd)
CONF_DIR="${PROJECT_DIR}/conf/hello_app"
SUPERVISOR_DIR="/etc/supervisor/conf.d/"

cp -f $CONF_DIR/supervisor.conf $SUPERVISOR_DIR

supervisorctl reread > /dev/null 2>&1
supervisorctl update > /dev/null 2>&1
supervisorctl restart hello > /dev/null 2>&1
