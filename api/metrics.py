"""
Module for managing prometheus metrics
"""
import os
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

class Metrics:
    """
    Sets up the flask application to track Prometheus metrics running with multiple processes.
    """
    def __init__(self, app, config):
        self.config = config

        if os.getenv('prometheus_multiproc_dir'):
            self.gunicorn_metrics = GunicornInternalPrometheusMetrics(app, path="/metrics")
