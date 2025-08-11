import json
import logging

logger = logging.getLogger(__name__)

# load the country list from JSON on iniiitalization
with open('data/en/countries.json', encoding='utf-8') as f:
    _COUNTRIES = json.load(f)


# countries.py
# return country list for use in picker on web page
def setup_routes(app):
    @app.route('/api/countries')
    def get_countries():  # noqa: F401
        # countries are pre-loaded to a global variable from a json file
        logger.debug('/api/countries API called via {request.method} from {request.remote_addr}')

        logger.debug('Fetching country list')
        return _COUNTRIES


# TODO [SMP-24] add docstring
