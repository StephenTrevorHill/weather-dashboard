from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
print("Loaded API key:", API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
                print("Requesting:", weather_url)
                res = requests.get(weather_url)
                res.raise_for_status()
                weather_data = res.json()
            except Exception as e:
                error = f"Error: {e}"

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)