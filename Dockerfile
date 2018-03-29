
FROM python:3.6-alpine3.7
RUN apk add --no-cache mariadb-dev build-base
ADD requirements.txt /
RUN pip install -r requirements.txt
