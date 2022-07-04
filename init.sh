#! /bin/bash

# NOTE:
# 1. Use 'sudo' to run this script
# 2. Run this script only from the project directory

PROJECT_NAME="web"
PROJECT_DIR=$(pwd)
APP_DIR="${PROJECT_DIR}/ask"

if [ "$(basename $PROJECT_DIR)" != "$PROJECT_NAME" ]; then
    echo -e "[\033[0;31mERROR\033[0m] Run from outside the project directory '$PROJECT_NAME'"
    exit 1
fi

$PROJECT_DIR/conf/nginx/nginx_start.sh
if [ $? != 0 ]; then exit 1; fi

$PROJECT_DIR/conf/mysql/mysql_start.sh $APP_DIR

$PROJECT_DIR/conf/ask_app/supervisor_start.sh $APP_DIR $PROJECT_DIR
