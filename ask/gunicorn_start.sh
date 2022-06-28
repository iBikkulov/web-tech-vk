#! /bin/bash

APP_DIR="/home/box/web/ask"

# Activate the virtual environment
source $APP_DIR/ask_env/bin/activate

# Start Gunicorn
exec $APP_DIR/ask_env/bin/gunicorn --chdir $APP_DIR ask.wsgi:application --bind 0.0.0.0:8000
