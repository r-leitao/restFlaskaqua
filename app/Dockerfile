FROM python:slim

MAINTAINER raphael <rleitao@fluksaqua.com>

RUN apt-get update

RUN apt-get install -y python-pip
RUN apt-get install -y mongodb-clients
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN apt-get install -y procps

RUN pip install --no-cache-dir gunicorn Flask eve
RUN pip install pymongo

WORKDIR /app
