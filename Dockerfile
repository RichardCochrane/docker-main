FROM python:2.7-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN pip install -e /app

LABEL maintainer="Richard Cochrane<screamer42@gmail.com>" version="0.1"

CMD pserve development.ini
