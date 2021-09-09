FROM python:3.9
RUN apt-get -y update && \
    apt-get -y install python-pkg-resources python-six stress-ng iptables iproute2

RUN pip install mysql-connector-python==8.0.26
ADD . /application
WORKDIR /application
RUN pip install -r requirements.txt
CMD ["gunicorn","--config", "/gunicorn_config.py", "--workers","5","--max-requests","100","--max-requests-jitter","5","--bind","0.0.0.0:8000","--statsd-host=statsd:9125","--statsd-prefix=service2","app:app"]