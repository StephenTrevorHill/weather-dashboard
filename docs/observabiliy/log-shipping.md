# Log Shipping (BetterStack + Celery/Redis)

## Overview
The app emits JSON logs to stdout and (optionally) ships structured logs to BetterStack. Shipping via the app code is really onlu useful in dev. When deployed to Render logs from Stdout can be picked up automatically (once configured).  
- Logs are shipped to Render via an async Celery task. 
- Celery uses Redis (broker) to decouple web requests from network I/O. 
- Celery and Redis can be run in Docker, or for dev they can run on the local machine.

## Architecture
- Flask app → JSON logger → Celery task `send_log_to_betterstack`
- Celery broker: Redis
- Worker: processes tasks and POSTs to BetterStack
- Render ships prod stdout directly to BetterStack as the typical production pattern.

## Config
- `APP_ENV`: development | testing | production
- `LOG_SHIPPING`: none | betterstack
- `BETTERSTACK_HOST`: e.g. `https://<ingest-host>`
- `BETTERSTACK_TOKEN`: bearer token for source
- `REDIS_URL`: e.g. `redis://localhost:6379/0` (local) or `redis://redis:6379/0` (Docker)

## Code Pointers
- `app/logging_config.py`: JSON formatter, RequestContextFilter, BetterStack handler (async via Celery).
- `app/tasks/celery_app.py`: Celery app/broker config.
- `app/tasks/log_tasks.py`: `send_log_to_betterstack` task with HTTP retries.
- `app/__init__.py`: preloads `asyncio` / `redis.asyncio` to avoid import races under multi-threaded logging.

## Local Dev Options
1) **Native**: run Redis (`brew services start redis`), run Celery worker, run Flask.
2) **Docker**: `docker compose -f docker-compose.dev.yml up --build` (services: `flask`, `worker`, `redis`).

## Testing the Path
- Quick probe (inside Flask container):
  ```bash
  docker compose -f docker-compose.dev.yml exec -T flask python - <<'PY'
  import json
  from app.tasks.log_tasks import send_log_to_betterstack
  r = send_log_to_betterstack.delay(json.dumps({"message":"probe from flask"}))
  print("queued task id:", r.id)
  PY