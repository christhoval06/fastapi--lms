# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEVELOPMENT=1

# install dependencies
RUN pip install --upgrade pip && pip install pip-tools

COPY requirements.in /usr/src/app/requirements.in

RUN pip-compile requirements.in

RUN pip install -r requirements.txt

# copy project
COPY ./ /usr/src/app/

EXPOSE 8000
