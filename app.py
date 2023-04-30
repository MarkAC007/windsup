# app.py
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from get_tide import get_tide_data, display_tide_data
from get_weather import get_weather_data, display_weather_data

# Load environment variables from .env file
load_dotenv()

# Load configuration from config.json file
def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

def is_low_tide_before_10am(tide_data):
    for event in tide_data["extremes"]:
        event_time = datetime.fromtimestamp(event["dt"])
        if event["type"] == "low" and event_time.hour < 10:
            return True
    return False

def is_no_rain(weather_data):
    return weather_data["weather"][0]["main"].lower() != "rain"

def is_wind_from_east_or_west(weather_data):
    wind_deg = weather_data["wind"]["deg"]
    return (wind_deg > 80 and wind_deg < 100) or (wind_deg > 260 and wind_deg < 280)

def main():
    config = load_config()
    latitude = config["latitude"]
    longitude = config["longitude"]

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

    if is_low_tide_before_10am(tide_data) and is_no_rain(weather_data) and is_wind_from_east_or_west(weather_data):
        print("\nConditions met: Low tide before 10 am, no rain, and wind from east or west.")
    else:
        print("\nConditions not met.")

if __name__ == "__main__":
    main()
