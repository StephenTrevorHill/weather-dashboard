COMPOSE = docker compose -f docker-compose.dev.yml

.PHONY: up down logs flask-logs worker-logs restart-flask restart-worker build

# Start all services
up:
	$(COMPOSE) up --build

# Stop all services
down:
	$(COMPOSE) down

# Rebuild images without starting
build:
	$(COMPOSE) build

# Tail all logs
logs:
	$(COMPOSE) logs -f

# Tail only Flask logs
flask-logs:
	$(COMPOSE) logs -f flask

# Tail only Worker logs
worker-logs:
	$(COMPOSE) logs -f worker

# Restart Flask service
restart-flask:
	$(COMPOSE) restart flask

# Restart Celery worker service
restart-worker:
	$(COMPOSE) restart worker