from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
# print("Loaded API key:", API_KEY)

# load detailed names for air quality components
AIR_COMPONENT_LABELS = {
    "co": "Carbon Monoxide (CO)",
    "no": "Nitric Oxide (NO)",
    "no2": "Nitrogen Dioxide (NO₂)",
    "o3": "Ozone (O₃)",
    "so2": "Sulfur Dioxide (SO₂)",
    "pm2_5": "Fine Particulate Matter (PM2.5)",
    "pm10": "Coarse Particulate Matter (PM10)",
    "nh3": "Ammonia (NH₃)"
}

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    air_quality = None
    error = None
    named_components=None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                # Get weather
                weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
                res = requests.get(weather_url)
                res.raise_for_status()
                weather_data = res.json()

                # Get Air Quality using lat/long from previous call
                lat = weather_data["coord"]["lat"]
                lon = weather_data["coord"]["lon"]
                air_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
                aq_res = requests.get(air_url)
                aq_res.raise_for_status()
                # grab first (and only) result
                air_quality = aq_res.json()["list"][0]
                # print(air_quality)

                # create a new dict with the air quality components mapped to the friendly names
                raw_components = air_quality["components"]
                # print(raw_components)
                named_components = {
                    AIR_COMPONENT_LABELS.get(k, k): v
                    for k, v in raw_components.items()
                }
                print(named_components)

            except Exception as e:
                error = f"Error: {e}"

    return render_template("index.html", weather=weather_data, air=air_quality, air_components=named_components, error=error)


@app.route("/api/weather", methods=["POST"])
def weather_api():
    city = request.form.get("city")
    if not city:
        return {"error": "Missing city"}, 400

    try:
        # 1. Get weather data (includes lat/lon)
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        weather_res = requests.get(weather_url)
        weather_res.raise_for_status()
        weather_data = weather_res.json()

        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]

        # 2. Get air quality data using lat/lon
        air_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        air_res = requests.get(air_url)
        air_res.raise_for_status()
        air_data = air_res.json()

        # 3. Combine and return both sets of data
        return {
            "weather": weather_data,
            "air_quality": air_data,
        }

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
