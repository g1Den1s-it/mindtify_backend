FROM python:3.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install -r requirements.txt

#create database
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Collect static files
RUN python3 manage.py collectstatic --noinput





