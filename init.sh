#! /bin/bash

# Run this script only from the project directory

PROJECT_NAME="web"
CUR_DIR=$(pwd)

if [ "$(basename $CUR_DIR)" != "$PROJECT_NAME" ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Run from outside the project directory"
    exit 1
fi

echo -n "Setup nginx configuration files... "
sudo cp -f etc/nginx.conf /etc/nginx/sites-available/
sudo ln -sf /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo rm -f /etc/nginx/sites-enabled/default
echo -e "[\033[0;32mOK\033[0m]"

echo -n "Test nginx configuration files... "
sudo nginx -t > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Check your configuration files."
    sudo rm -f /etc/nginx/sites-available/nginx.conf
    sudo rm -f /etc/nginx/sites-enabled/nginx.conf 
    exit 1
fi
echo -e "[\033[0;32mOK\033[0m]"

echo -n "Setup gunicorn... "
sudo cp -f etc/gunicorn.service /etc/systemd/system/
sudo cp -f etc/gunicorn.socket /etc/systemd/system/
sudo systemctl enable --now gunicorn.socket > /dev/null 2>&1
echo -e "[\033[0;32mOK\033[0m]"

echo -n "Start nginx... "
sudo systemctl enable nginx.service > /dev/null 2>&1
sudo systemctl start nginx > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]"
    exit 1
fi
echo -e "[\033[0;32mOK\033[0m]"
exit 0
