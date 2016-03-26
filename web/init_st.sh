#! /bin/sh
sudo /etc/init.d/mysql restart
mysql -u root -e "create database ask;"

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
