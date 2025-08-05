"""
weather_data_service.py

Service for retrieving current weather data from the OpenWeatherMap API
based on a city name.
"""

import logging

import requests

from app.config import API_KEY

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
    weather_url = (
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    )
    logger.debug(f'Requesting weather data for city: {city}')
    res = requests.get(weather_url)
    res.raise_for_status()
    weather_data = res.json()
    logger.debug(f'Weather data received for city: {city}')
    return weather_data
