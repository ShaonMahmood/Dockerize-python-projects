FROM python:3

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup
#RUN apk update
#RUN apk upgrade
#RUN apk add build-base python3 python3-dev postgresql-client postgresql-dev gettext
#RUN apk add build-base
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Clean
#RUN apk del -r python3-dev postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p mydjango/static/admin