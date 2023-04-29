# get_tide.py
import requests
from datetime import datetime

def get_tide_data(latitude, longitude, api_key):
    try:
        url = f"https://www.worldtides.info/api/v3?heights&extremes&lat={latitude}&lon={longitude}&key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch tide data. ({e})")
        return None

    return response.json()

def display_tide_data(tide_data):
    if tide_data:
        for event in tide_data["extremes"]:
            event_time = datetime.fromtimestamp(event["dt"]).strftime('%Y-%m-%d %H:%M:%S')
            event_type = event["type"].capitalize()
            print(f"{event_type} tide at {event_time}")
    else:
        print("No tide data available.")
