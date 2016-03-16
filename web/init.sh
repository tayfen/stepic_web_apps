#! /bin/sh
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/gunicorn.d/*.example
sudo ﻿ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
cd ask
sudo gunicorn -D --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application  
