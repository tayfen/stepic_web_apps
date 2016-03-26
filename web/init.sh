https://github.com/skolomiiets/ask

#! /bin/sh
#export STEPIC_WEBAPPS=/home/tayfen/stepic/web_apps/web

#sudo kill -9 $(cat /home/tayfen/develop/stepic/web_apps/web/gunicorn.pid)

sudo kill -9 $(cat /home/box/web/gunicorn.pid) 

# автозаполнение
#pip install django-autofixture
#python manage.py shell < init_db.py


set -e
#ENV=/home/my/env/bin/activate
GUNICORN=gunicorn_django
APP_PATH=/home/tayfen/develop/stepic/web_apps/web/ask
PROJECT_PATH=/home/tayfen/develop/stepic/web_apps/web
CONFROOT=/home/tayfen/develop/stepic/web_apps/web/etc/gunicorn.conf

cd $SETTINGS_PATH
#source $ENV
#export PYTHONPATH=$PROJECT_PATH
#exec $GUNICORN app.settings.staging -c $CONFROOT
exec $GUNICORN -c $CONFROOT

sudo /etc/init.d/mysql restart
mysql -u root -p

python manage.py migrate
# for old dj
mysql -u root -e "create database ask;"
python manage.py syncdb

#curl post
curl --data "title=value1&text=value2" http://127.0.0.1/ask/

sudo rm /etc/nginx/sites-enabled/default
#sudo rm /etc/gunicorn.d/*.example
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ﻿cp /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -D --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application  

#gunicorn_django -c /home/tayfen/develop/stepic/web_apps/web/etc/gunicorn.conf

gunicorn ask.wsgi:application -c /home/tayfen/develop/stepic/web_apps/web/etc/gunicorn.conf


#mysql
#use ask
#show tables;
#show columns from qa_question;
#select id from qa_question limit 5;
#select * from qa_question where id=1;
#mysql -u root -e "create database ask;"
#mysql -u root -p -e 'show databases;'
#mysql -u root -p -e "SHOW TABLE STATUS FROM ask" | awk '{print $1, $2}'|column -t
#sudo restart mysql
