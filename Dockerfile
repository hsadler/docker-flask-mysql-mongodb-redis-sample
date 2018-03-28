
FROM python:3.4-alpine
ADD requirements.txt /
RUN pip install -r requirements.txt
