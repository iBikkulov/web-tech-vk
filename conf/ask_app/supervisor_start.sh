#! /bin/bash

# A script for installing configuration files and running supervisord. Do NOT run manually

APP_DIR=$1
PROJECT_DIR=$2
CONF_DIR="${PROJECT_DIR}/conf/ask_app"
SUPERVISOR_DIR="/etc/supervisor"

cp -f $CONF_DIR/supervisor_ask.conf $SUPERVISOR_DIR/conf.d/

if [ ! -e $APP_DIR/log/supervisor.log ]; then
    mkdir -p $APP_DIR/log
    touch $APP_DIR/log/supervisor.log
fi

/usr/bin/supervisord -c $SUPERVISOR_DIR/supervisor.conf

supervisorctl reread >/dev/null 2>&1
supervisorctl update >/dev/null 2>&1
supervisorctl restart ask >/dev/null 2>&1
