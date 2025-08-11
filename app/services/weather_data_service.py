"""
weather_data_service.py

Service for retrieving current weather data from the OpenWeatherMap API
based on a city name.
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)


def get_weather(city):
    """
    Fetch current weather data for the specified city from OpenWeatherMap.

    Args:
        city (str): The name of the city to fetch weather data for.

    Returns:
        dict: Parsed JSON response containing weather data.

    Raises:
        requests.HTTPError: If the API request fails.
    """

    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    weather_url = (
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    )
    logger.debug(f'Requesting weather data: {weather_url}')

    try:
        res = requests.get(weather_url)
        logger.debug(f'Weather API status: {res.status_code}')
        logger.debug(f'Weather API response: {res.text}')  # or res.json() for parsed data
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        logger.exception(f'Error calling weather API: {e}')
        raise
