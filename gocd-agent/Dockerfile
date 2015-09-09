FROM gocd/gocd-agent

RUN apt-get update -qq && apt-get install -qqy python python-pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
