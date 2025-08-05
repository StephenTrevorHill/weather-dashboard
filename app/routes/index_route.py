import logging

from flask import render_template, request

from app.services.weather_aggregation_service import get_all_weather_data

logger = logging.getLogger(__name__)


def setup_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        logger.info('Default route hit')

        if request.method == 'POST':
            city = request.form.get('city')
            if not city:
                logger.debug('POST request received but no city parameter found')
            logger.debug(f'Fetching weather for city: {city}')
            context = get_all_weather_data(city)
            logger.debug('Weather data loaded OK')
        else:
            logger.debug('GET method called - building empty data structure')
            context = {'weather': None, 'air': None, 'air_components': None, 'error': None}

        if context.get('error'):
            logger.warning(f'Error returned in context: {context["error"]}')

        logger.debug('Data collection complete, rendering template and returning')
        return render_template('index.html', **context)
