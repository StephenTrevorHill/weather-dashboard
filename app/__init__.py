# __init__.py
# top level app factory - returns the app to flask

from flask import Flask

from .logging_config import configure_logging
from .routes import setup_routes  # import your route setup


def create_app():
    # Preload the asyncio module to prevent threaded import races in error logging to Redis
    import asyncio  # noqa: F401

    try:  # noqa: SIM105
        import redis.asyncio  # noqa: F401
    except Exception:
        pass

    app = Flask(__name__)

    # configure logging and attach handlers - site wide
    configure_logging()

    # load the API routes
    setup_routes(app)

    return app
