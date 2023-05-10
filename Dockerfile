FROM python:3.10.11-alpine
ENV PYTHONUNBUFFERED=1

RUN mkdir /dockerTest
COPY . /dockerTest
WORKDIR /dockerTest

EXPOSE $PORT

RUN python -m pip install -r requirements.txt
RUN python manage.py migrate 