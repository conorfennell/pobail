"""
Module for managing configuration
"""
import os
from datetime import datetime
from configparser import ConfigParser

class Configuration:
    """
    Centralises and converts all configuration into a dictionary
    """

    def __init__(self):
        config = ConfigParser()
        config_path = os.getenv('CONFIG_PATH', default='config.ini')
        config.read(config_path)

        self.config = {
            'name': 'pobail',
            'startTime': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        }
