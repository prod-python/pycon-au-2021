FROM python:3.9
ADD . /application
WORKDIR /application
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
#RUN apt-get -y update && apt-get -y install stress-ng iptables iproute2
CMD ["gunicorn","--config", "/gunicorn_config.py", "--workers","5","--max-requests","100","--max-requests-jitter","5","--bind","0.0.0.0:8000","--statsd-host=statsd:9125","--statsd-prefix=service1", "app:app"]