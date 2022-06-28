#! /bin/bash

# A script for installing configuration files and running supervisord. Do NOT run manually

PROJECT_DIR=$(pwd)
CONF_DIR="${PROJECT_DIR}/conf/ask_app"
APP_DIR="${PROJECT_DIR}/ask"
SUPERVISOR_DIR="/etc/supervisor/conf.d/"

cp -f $CONF_DIR/supervisor_ask.conf $SUPERVISOR_DIR

if [ ! -e $APP_DIR/log/supervisor.log ]; then
    mkdir -p $APP_DIR/log
    touch $APP_DIR/log/supervisor.log
fi

supervisorctl reread >/dev/null 2>&1
supervisorctl update >/dev/null 2>&1
supervisorctl restart ask >/dev/null 2>&1
