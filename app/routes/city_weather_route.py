import logging

from flask import jsonify, request

from app.services.weather_aggregation_service import get_all_weather_data

logger = logging.getLogger(__name__)


# this is a testable route that closley mimics the main / route that drives the flask template
def setup_routes(app):
    @app.route('/api/city-weather', methods=['GET', 'POST'])
    def city_weather():  # will be flagged unused as it's only called by API route (from JavaScript)
        city = request.args.get('city')
        if not city:
            logger.warning('Missing city parameter in request')
            return jsonify({'error': 'Missing city parameter'}), 400
        logger.debug(f'Fetching weather data for city: {city}')
        return jsonify(get_all_weather_data(city))


# TODO [SMP-21] clean up support for POST
# TODO [SMP-22] add docstring
