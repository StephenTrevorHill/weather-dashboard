from flask import Flask

from .logging_config import configure_logging
from .routes import setup_routes  # import your route setup


def create_app():
    app = Flask(__name__)
    configure_logging()
    setup_routes(app)
    return app
