FROM debian:jessie

RUN apt-get update -qq && apt-get install -qqy python python-pip vim nano
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY create_inception_pipeline.py /create_inception_pipeline.py

RUN chmod +x /create_inception_pipeline.py
