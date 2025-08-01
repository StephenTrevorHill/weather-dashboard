import os
import sys

# Add project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_weather_route():
    client = app.test_client()
    response = client.post('/api/weather', data={'city': 'Toronto'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'weather' in data
    assert 'air_quality' in data
    assert 'main' in data['weather']
    assert 'pressure' in data['weather']['main']
    assert 'humidity' in data['weather']['main']
    assert 'wind' in data['weather']
    assert 'speed' in data['weather']['wind']


def test_get_countries():
    client = app.test_client()
    response = client.get('/api/countries')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert 'Canada' in data or any('Canada' in c for c in data)


def test_get_cities_for_country():
    client = app.test_client()
    response = client.get('/api/cities?country=Canada')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any('Toronto' in city for city in data)
