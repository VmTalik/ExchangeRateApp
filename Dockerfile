FROM python:latest

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install cron -y

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#django-crontab logfile
RUN mkdir /cron
RUN touch /cron/django_cron.log

COPY . .
