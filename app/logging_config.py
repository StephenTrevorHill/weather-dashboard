import json
import logging
import os
import sys
from datetime import datetime

from flask import request


class JSONFormatter(logging.Formatter):
    def __init__(self, datefmt='%Y-%m-%dT%H:%M:%S%z'):
        super().__init__()
        self.datefmt = datefmt

    def format(self, record):
        # Create timezone-aware datetime from record.created
        dt = datetime.fromtimestamp(record.created).astimezone()
        timestamp = dt.strftime(self.datefmt)

        log_record = {
            'level': record.levelname,
            'message': record.getMessage(),
            'logger': record.name,
            'time': timestamp,
            'pathname': record.pathname,
            'lineno': record.lineno,
            'funcName': record.funcName,
        }

        # Add custom fields if they exist
        if hasattr(record, 'path'):
            log_record['path'] = record.path
        if hasattr(record, 'remote_addr'):
            log_record['remote_addr'] = record.remote_addr

        return json.dumps(log_record)


class RequestContextFilter(logging.Filter):
    def filter(self, record):
        try:
            record.path = request.path
            record.remote_addr = request.remote_addr
        except RuntimeError:
            # Outside request context
            record.path = None
            record.remote_addr = None
        return True


def configure_logging():
    logger = logging.getLogger()
    if logger.handlers:
        return  # Already configured

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    logger.setLevel(getattr(logging, LOG_LEVEL, logging.DEBUG))

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JSONFormatter())
    console_handler.addFilter(RequestContextFilter())

    logger.addHandler(console_handler)
