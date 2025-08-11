# cities.py
# return city list for use in picker on web page

import json
import logging

from flask import jsonify, request

logger = logging.getLogger(__name__)

# pre-load city list from JSON once, on initialization
with open('data/en/cities.json', encoding='utf-8') as f:
    _CITIES_BY_COUNTRY = json.load(f)


def setup_routes(app):
    @app.route('/api/cities')
    def get_cities():  # will be flagged unused as it's only called by API route (from JavaScript)
        """Return the city list for the given country query parameter."""
        country = request.args.get('country')
        logger.debug(f'Fetching city list for country {country}')
        city_list = _CITIES_BY_COUNTRY.get(country, [])
        return jsonify(city_list)


# TODO [SMP-23] add docstring
