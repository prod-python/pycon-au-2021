
import os

from datadog import initialize, statsd
import time

options = {
    'statsd_host': 'statsd',
    'statsd_port': 9125
}

initialize(**options)


def pre_request(worker, req):
    statsd.increment(
        'worker_request',
        tags=[
            "app:{0}".format(os.getenv("APP_NAME")),
            "worker_id:{0}".format(worker.pid),
        ],
    )


def post_request(worker, req, environ, resp):
    # Decrement busy workers count
    #sc.decr('busy_workers', 1)
    pass
