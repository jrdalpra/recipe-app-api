FROM python:3.7-alpine
MAINTENER José Volmei Dal Prá Junior

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduer -D user
USER user
