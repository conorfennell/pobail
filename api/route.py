"""
API module for the application
"""

from flask import Flask
from api.config import Configuration
from api.metrics import Metrics
from api.request_logger import add_request_logging

app = Flask(__name__)
add_request_logging(app)
configuration = Configuration()
metrics = Metrics(app, configuration)

@app.route('/health')
def health():
    """
    Health endpoint which returns the configuration
    """
    return configuration.config
