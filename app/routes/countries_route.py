import logging

from app.config import COUNTRIES

logger = logging.getLogger(__name__)


# countries.py
# return country list for use in picker on web page
def setup_routes(app):
    @app.route('/api/countries')
    def get_countries():
        # countries are pre-loaded to a global variable from a json file
        logger.debug('/api/countries API called via {request.method} from {request.remote_addr}')

        logger.debug('Fetching country list')
        return COUNTRIES


# TODO [SMP-24] add docstring
