"""
air_quality_data_service.py

Service for retrieving air quality data from the OpenWeatherMap API
based on geographic coordinates.
"""

import logging

import requests

from app.config import API_KEY

logger = logging.getLogger(__name__)


def get_aqi_data(lat, lon):
    """
    Fetch air quality data from OpenWeatherMap's Air Pollution API
    using the provided latitude and longitude.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.

    Returns:
        dict: The first item in the API's 'list' response, containing
              air quality data and pollutant concentrations.

    Raises:
        requests.HTTPError: If the API request fails.
    """
    air_url = (
        f'https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}'
    )
    logger.debug(f'Requesting AQI data for lat: {lat}, lon: {lon}')
    aq_res = requests.get(air_url)
    aq_res.raise_for_status()

    air_quality = aq_res.json()['list'][0]
    logger.debug(f'AQI data retrieved for lat: {lat}, lon: {lon}')
    return air_quality
