import logging

from app.config import AIR_COMPONENT_LABELS

from .air_quality_data_service import get_aqi_data
from .weather_data_service import get_weather

logger = logging.getLogger(__name__)


def get_all_weather_data(city):
    """
    Retrieve weather and air quality data for a given city.

    Returns a dictionary with the following keys:
    - 'weather': raw weather data from OpenWeather API
    - 'air': raw air quality data from OpenWeather API
    - 'air_components': dictionary of air quality components with friendly labels
    - 'error': error message string if any error occurred, otherwise None
    """
    if not city:
        logger.warning('No city provided.')
        return {
            'weather': None,
            'air': None,
            'air_components': None,
            'error': 'City parameter is missing.',
        }

    logger.debug(f'Fetching all weather data for city: {city}')

    weather_data = None
    air_quality = None
    error = None
    named_components = None

    try:
        # Get weather
        weather_data = get_weather(city)

        # Get Air Quality using lat/long from previous call
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        air_quality = get_aqi_data(lat, lon)

        # Map air quality components to friendly names
        raw_components = air_quality['components']
        named_components = {AIR_COMPONENT_LABELS.get(k, k): v for k, v in raw_components.items()}

    except Exception as e:
        logger.exception(f"Error fetching data for city '{city}': {e}")
        error = f'Error: {e}'

    logger.debug(f'Returning weather data for city: {city}')
    return {
        'weather': weather_data,
        'air': air_quality,
        'air_components': named_components,
        'error': error,
    }
