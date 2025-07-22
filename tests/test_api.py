import sys
import os

# Add project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
def test_weather_route():
    client = app.test_client()
    response = client.post("/api/weather", data={"city": "Toronto"})
    assert response.status_code == 200
    data = response.get_json()
    assert "weather" in data
    assert "air_quality" in data