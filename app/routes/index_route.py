# index_route.py

import logging
import traceback

from flask import render_template, request

from app.services.weather_aggregation_service import get_all_weather_data

logger = logging.getLogger(__name__)


def setup_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        logger.debug(f'Default route hit for {request.method} from {request.remote_addr}')

        if request.method == 'POST':
            city = request.form.get('city')
            if not city:
                logger.warning('POST request received but no city parameter found')
                # TODO [SMP-26] improve handling if no city passed
            logger.debug(f'Fetching weather for city: {city}')
            context = get_all_weather_data(city)
            logger.debug('Weather data loaded from API')
            # TODO [SMP-27] improve handling if weather API doesn't return data for that city
        else:
            logger.debug('GET method called - building empty data structure')
            context = {'weather': None, 'air': None, 'air_components': None, 'error': None}

        # if context.get('error'):
        #     logger.eroor(f'Error returned in context: {context["error"]}')

        # logger.debug('Data collection complete, rendering template and returning')
        # return render_template('index.html', **context)

        try:
            logger.debug('Data collection complete, rendering template and returning')
            return render_template('index.html', **context)
        except Exception:
            logger.exception('Template rendering failed')
            logger.debug(f'Context passed to template: {context}')
            logger.debug(traceback.format_exc())
            return 'Internal Server Error', 500
