import requests
from datetime import datetime

def get_tide_data(latitude, longitude, api_key):
    url = f"https://www.worldtides.info/api/v3?heights&extremes&lat={latitude}&lon={longitude}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch tide data. (Status code: {response.status_code})")
        return None

def display_tide_data(tide_data):
    if tide_data:
        for event in tide_data["extremes"]:
            event_time = datetime.fromtimestamp(event["dt"]).strftime('%Y-%m-%d %H:%M:%S')
            event_type = event["type"].capitalize()
            print(f"{event_type} tide at {event_time}")
    else:
        print("No tide data available.")

def main():
    latitude = float(input("Enter the latitude of the location: "))
    longitude = float(input("Enter the longitude of the location: "))
    api_key = "7a6a0fe0-ab84-411a-9189-6b2af196e4ac"  # Replace with your World Tides API key
    
    tide_data = get_tide_data(latitude, longitude, api_key)
    display_tide_data(tide_data)

if __name__ == "__main__":
    main()
