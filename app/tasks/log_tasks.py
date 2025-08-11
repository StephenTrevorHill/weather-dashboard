# app/tasks/log_tasks.py
import os

import requests
from requests.adapters import HTTPAdapter

from app.tasks.celery_app import celery

TOKEN = os.getenv('BETTERSTACK_TOKEN')
HOST = os.getenv('BETTERSTACK_HOST')

# Reuse one session per worker process
_session = requests.Session()

# No transport-level retries; let Celery handle retries
adapter = HTTPAdapter(max_retries=0)
_session.mount('https://', adapter)
_session.mount('http://', adapter)


@celery.task(
    name='send_log_to_betterstack',
    autoretry_for=(requests.Timeout, requests.ConnectionError, requests.HTTPError),
    retry_backoff=2,  # 2s, 4s, 8s, ...
    retry_backoff_max=60,  # cap the backoff
    retry_jitter=True,  # add jitter
    retry_kwargs={'max_retries': 5},
)
def send_log_to_betterstack(message_json: str) -> None:
    if not (TOKEN and HOST):
        return

    resp = _session.post(
        HOST,
        headers={
            'Authorization': f'Bearer {TOKEN}',
            'Content-Type': 'application/json',
        },
        data=message_json,
        timeout=2,
    )

    # Requeue only for overload/rate-limit/server errors
    if resp.status_code == 429 or 500 <= resp.status_code < 600:
        resp.raise_for_status()  # => Celery autoretry

    # For other 4xx (bad auth/payload), do nothing (no retry).
