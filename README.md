# Weather Dashboard 🌤️

A simple Flask web app that fetches current weather and air quality data for a city using the OpenWeatherMap API.

## Features

- Fetches weather by city name
- Displays temperature, humidity, and condition
- Retrieves AQI and pollutant breakdown
- Styled interface using custom CSS
- Deployed to [Render](https://weather-dashboard-4nqf.onrender.com)

## Tech Stack

- Python 3.13
- Flask
- Requests
- Gunicorn (for deployment)
- HTML/CSS + Jinja2 templates

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/StephenTrevorHill/weather-dashboard.git
   cd weather-dashboard

   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate

   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Add your API key:
- Create a .env file with:
- OPENWEATHER_API_KEY=your_api_key_here

5. Run locally:
   ```bash
   flask run
