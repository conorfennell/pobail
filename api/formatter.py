"""
Module for json formatting logs
"""
from datetime import datetime
from pythonjsonlogger.jsonlogger import JsonFormatter

class CustomJsonFormatter(JsonFormatter):
    """
    Formats the log into the JSON format below.

    {
        "message": "methos=POST path=/health status=2-- duration=0.0028 ip=165.43.2.1 host=localhost",
        "name": "app.api",
        "filename": "request_logger.py",
        "lineno": 24,
        "module": "request_logger",
        "timestamp": "2020-04-12T15:22:22.054Z",
        "level": "INFO"
    }

    """
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record['timestamp'] = formatted_now_time()
        log_record['level'] = record.levelname
        del log_record['levelname']

def formatted_now_time():
    """
    Generates now time in this format 2020-04-12T15:22:22.054Z
    """

    now = datetime.utcnow()
    now_formatted = now.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return f'{now_formatted[:-3]}Z'
