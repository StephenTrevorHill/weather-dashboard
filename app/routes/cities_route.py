import logging

from flask import jsonify, request

from app.config import CITIES_BY_COUNTRY

logger = logging.getLogger(__name__)


# cities.py
# return city list for use in picker on web page
def setup_routes(app):
    @app.route('/api/cities')
    def get_cities():
        country = request.args.get('country')
        logger.debug(f'Fetching city list for country {country}')
        city_list = CITIES_BY_COUNTRY.get(country, [])

        return jsonify(city_list)


# TODO [SMP-23] add docstring
