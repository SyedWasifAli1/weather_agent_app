# from agents import function_tool

# @function_tool
# def get_weather_data(city: str) -> str:
#     """Fetches weather data for a given city (simulated)."""
#     return f"The current weather in {city} is sunny with a temperature of 25°C."


import os
import requests
from agents import function_tool
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

@function_tool
def get_weather_data(city: str) -> str:
    """Fetches real weather data for a given city using OpenWeatherMap API."""
    if not API_KEY:
        return "⚠️ OpenWeatherMap API key not found."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return f"⚠️ Error: {data.get('message', 'Could not fetch weather')}"

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return f"The current weather in {city} is {weather} with a temperature of {temp}°C and humidity {humidity}%."

    except Exception as e:
        return f"⚠️ Failed to fetch weather: {str(e)}"
