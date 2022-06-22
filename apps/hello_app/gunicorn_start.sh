#! /bin/bash

APP_DIR="/home/box/web/apps/hello_app"

# Activate the virtual environment
source $APP_DIR/hello_env/bin/activate

# Start Gunicorn
exec $APP_DIR/hello_env/bin/gunicorn --chdir $APP_DIR hello --bind 0.0.0.0:8080