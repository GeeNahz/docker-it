FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
