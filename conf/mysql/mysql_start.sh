#! /bin/bash

echo -n "Start mysql... "
sudo /etc/init.d/mysql start > /dev/null 2>&1

USERS=$(mysql -uroot -e"SELECT User, Host FROM mysql.user;")

mysql -u root -e "CREATE DATABASE IF NOT EXISTS ask;"
if [[ ! "$USERS" =~ .*"box"[[:space:]]*"localhost".* ]]; then
	mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '12345'; \
        GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION; \
        FLUSH PRIVILEGES;"
fi
echo -e "[\033[0;32mOK\033[0m]"
