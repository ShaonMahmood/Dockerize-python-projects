#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd myproject
# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
su -m myuser -c "celery -A docker_test beat -l info"