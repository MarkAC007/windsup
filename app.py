# app.py
import os
import sys
import subprocess
from dotenv import load_dotenv
from get_tide import get_tide_data, display_tide_data
from get_weather import get_weather_data, display_weather_data

# Load environment variables from .env file
load_dotenv()


def main():
    try:
        latitude = float(input("Enter the latitude of the location: "))
        longitude = float(input("Enter the longitude of the location: "))
    except ValueError:
        print("Invalid input. Please enter valid latitude and longitude values.")
        return

    weather_api_key = os.environ.get("WEATHER_API_KEY")
    tide_api_key = os.environ.get("TIDE_API_KEY")

    if not (weather_api_key and tide_api_key):
        print("Error: Missing API keys. Please set the WEATHER_API_KEY and TIDE_API_KEY environment variables.")
        return

    weather_data = get_weather_data(latitude, longitude, weather_api_key)
    tide_data = get_tide_data(latitude, longitude, tide_api_key)

    print("\nWeather Information:")
    display_weather_data(weather_data)
    
    print("\nTide Information:")
    display_tide_data(tide_data)

if __name__ == "__main__":
    main()
