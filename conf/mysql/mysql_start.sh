#! /bin/bash

echo -n "Start mysql... "
sudo /etc/init.d/mysql start > /dev/null 2>&1
echo -e "[\033[0;32mOK\033[0m]"

sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS ask;"
sudo mysql -u root -e "CREATE USER IF NOT EXISTS 'box'@'localhost';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"