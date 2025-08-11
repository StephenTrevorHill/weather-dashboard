import json
import logging
import os
import sys
from datetime import datetime, timezone

from flask import request

from app.config import APP_ENV, APP_VERSION
from app.tasks.log_tasks import send_log_to_betterstack


class JSONFormatter(logging.Formatter):
    def __init__(self, datefmt='%Y-%m-%dT%H:%M:%S%z'):
        super().__init__()
        self.datefmt = datefmt

    def format(self, record):
        # Create timezone-aware datetime from record.created

        log_record = {
            'dt': datetime.now(timezone.utc).isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'logger': record.name,
            'app_env': APP_ENV,
            'version': APP_VERSION,
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


class CeleryBetterstackHandler(logging.Handler):
    def emit(self, record):
        try:
            msg = self.format(record)  # JSON string from your JSONFormatter
            print('DEBUG: queueing BetterStack log via Celery')
            print(f'record contents: {record}')
            send_log_to_betterstack.delay(msg)
        except Exception:
            self.handleError(record)


def configure_logging():
    logger = logging.getLogger()
    if logger.handlers:
        logger.debug("Skipping logger setup as it's already configured")
        return  # Already configured

    if APP_ENV == 'production':
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JSONFormatter())
    console_handler.addFilter(RequestContextFilter())

    logger.addHandler(console_handler)

    LOG_SHIPPING = os.getenv('LOG_SHIPPING', 'none').strip().lower()
    if LOG_SHIPPING == 'betterstack':
        celery_handler = CeleryBetterstackHandler()
        celery_handler.setFormatter(JSONFormatter())
        celery_handler.addFilter(RequestContextFilter())
        logger.addHandler(celery_handler)
        logger.info('Celery-based async log shipping enabled')
        logger.info('Betterstack logging configured.')

    logger.debug(f'Logging configured for {APP_ENV} environment')
