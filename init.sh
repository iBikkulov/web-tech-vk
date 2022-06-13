#! /bin/bash

# Run this script only from the project directory

PROJECT_NAME="web"
CUR_DIR=$(pwd)

if [ "$(basename $CUR_DIR)" != "$PROJECT_NAME" ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Run from outside the project directory"
    exit 1
fi

if [ -f /etc/nginx/sites-enabled/test.conf ]; then
    sudo rm -f /etc/nginx/sites-enabled/test.conf
fi
sudo ln -s $CUR_DIR/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo nginx -t
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Conf test failed"
    exit 1
fi

sudo /etc/init.d/nginx restart
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Nginx start failed"
    exit 1
fi

sudo gunicorn -b '0.0.0.0:8080' hello &
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Gunicorn start failed"
    exit 1
fi

echo -e "[\033[0;32mOK\033[0m]"
exit 0
