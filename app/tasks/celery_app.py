# celery_app.py
# configures celery

import os

from celery import Celery

celery = Celery(
    'weather_dashboard',
    broker=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    include=['app.tasks.log_tasks'],  # make sure this matches your task module
)

celery.conf.task_default_queue = 'logs'
celery.conf.accept_content = ['json']
celery.conf.task_serializer = 'json'
celery.conf.worker_prefetch_multiplier = 1  # fair dispatch for spiky loads
celery.conf.task_acks_late = True  # don’t lose a log on worker crash
celery.conf.task_time_limit = 10  # hard kill
celery.conf.task_soft_time_limit = 5  # graceful timeout

# explicitly disable result backend (fewer writes, lighter weight)
celery.conf.result_backend = None
celery.conf.task_ignore_result = True

celery.conf.task_routes = {'send_log_to_betterstack': {'queue': 'logs'}}
