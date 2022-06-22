#! /bin/bash

# A script for installing configuration files and running nginx. Do NOT run manually

PROJECT_DIR=$(pwd)
CONF_DIR="${PROJECT_DIR}/conf/nginx"
NGINX_DIR="/etc/nginx"

echo -n "Setup nginx configuration files... "
cp -f $CONF_DIR/nginx.conf $NGINX_DIR/sites-available/
ln -sf $NGINX_DIR/sites-available/nginx.conf $NGINX_DIR/sites-enabled/nginx.conf
rm -f $NGINX_DIR/sites-enabled/default
echo -e "[\033[0;32mOK\033[0m]"

echo -n "Test nginx configuration files... "
nginx -t > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Check your configuration files."
    rm -f /etc/nginx/sites-available/nginx.conf
    rm -f /etc/nginx/sites-enabled/nginx.conf 
    exit 1
fi
echo -e "[\033[0;32mOK\033[0m]"

echo -n "Start nginx... "
/etc/init.d/nginx restart > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]"
    exit 1
fi
echo -e "[\033[0;32mOK\033[0m]"
exit 0
