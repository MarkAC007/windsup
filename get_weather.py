# get_weather.py
import requests

def get_weather_data(latitude, longitude, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch weather data. ({e})")
        return None

    return response.json()

def display_weather_data(weather_data):
    if weather_data:
        location = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        
        print(f"Weather information for {location}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description.capitalize()}")
    else:
        print("No weather data available.")
