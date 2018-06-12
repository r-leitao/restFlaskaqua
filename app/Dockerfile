FROM python:slim

MAINTAINER raphael <rleitao@fluksaqua.com>

RUN apt-get update

#RUN apt-get -y install nginx

RUN apt-get install -y python-pip
RUN apt-get install -y mongodb-clients
RUN apt-get install -y curl

RUN pip install --no-cache-dir gunicorn Flask
RUN pip install pymongo

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app

# nginx setup
RUN rm /etc/nginx/sites-enabled/default
COPY conf/flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
