from app import app
from bs4 import BeautifulSoup

def test_homepage_loads_form():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

    soup = BeautifulSoup(res.data, "html.parser")
    form = soup.find("form")
    assert form is not None
    assert "Enter city name" in res.get_data(as_text=True)

def test_homepage_shows_weather_on_post():
    client = app.test_client()
    res = client.post("/", data={"city": "Toronto"})
    assert res.status_code == 200

    soup = BeautifulSoup(res.data, "html.parser")
    assert soup.find("h2")  # Check if a heading is present

    weather_card = soup.find_all("div", class_="card")[0]
    assert "Wind Speed" in weather_card.text
    assert "Pressure" in weather_card.text
    assert "Feels Like" in weather_card.text

    pollutant_heading =soup.find("h3")
    assert pollutant_heading and "Pollutants:" in pollutant_heading.text

    pollutant_table = soup.find( "table")
    assert pollutant_table and "Ozone" in pollutant_table.text

    pollutant_table = soup.find("table")
    rows = pollutant_table.find_all("tr")
    # 1 header row + 8 pollutant rows
    assert len(rows) == 9

