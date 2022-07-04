#! /bin/bash

# A script for running MySQL. Do NOT run manually

APP_DIR=$1

echo -n "Start mysql... "
sudo /etc/init.d/mysql start > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]"
    exit 1
fi

USERS=$(mysql -uroot -e"SELECT User, Host FROM mysql.user;")

mysql -u root -e "CREATE DATABASE IF NOT EXISTS ask;" > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]: Cannot create database."
    exit 1
fi
if [[ ! "$USERS" =~ .*"box"[[:space:]]*"localhost".* ]]; then
        mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '12345'; \
                GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION; \
                FLUSH PRIVILEGES;" > /dev/null 2>&1
        if [ $? != 0 ]; then
        echo -e "[\033[0;31mERROR\033[0m]: Cannot create a user."
        exit 1
        fi
fi
echo -e "[\033[0;32mOK\033[0m]"

source $APP_DIR/ask_env/bin/activate
echo -n "Apply migrations... "
python $APP_DIR/manage.py migrate > /dev/null 2>&1
if [ $? != 0 ]; then
    echo -e "[\033[0;31mERROR\033[0m]"
    exit 1
fi
echo -e "[\033[0;32mOK\033[0m]"
