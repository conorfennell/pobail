"""
Module for configuring Gunicorn
"""

from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

def child_exit(server, worker): # pylint: disable=unused-argument
    """
    Clean up prometheus metrics when a worker dies
    """
    GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
