import json
import os

from dotenv import load_dotenv

# load detailed names for air quality components
AIR_COMPONENT_LABELS = {
    'co': 'Carbon Monoxide (CO)',
    'no': 'Nitric Oxide (NO)',
    'no2': 'Nitrogen Dioxide (NO₂)',
    'o3': 'Ozone (O₃)',
    'so2': 'Sulfur Dioxide (SO₂)',
    'pm2_5': 'Fine Particulate Matter (PM2.5)',
    'pm10': 'Coarse Particulate Matter (PM10)',
    'nh3': 'Ammonia (NH₃)',
}

# preload city and country tables to global variables
with open('data/en/countries.json', encoding='utf-8') as f:
    COUNTRIES = json.load(f)
with open('data/en/cities.json', encoding='utf-8') as f:
    CITIES_BY_COUNTRY = json.load(f)

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')
# print("Loaded API key:", API_KEY)
