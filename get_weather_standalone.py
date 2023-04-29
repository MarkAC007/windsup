import requests

def get_weather_data(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data. (Status code: {response.status_code})")
        return None

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

def main():
    location = input("Enter a location (e.g., city or city,country): ")
    api_key = "36048a5914df1626d124d4a5a3e5ea67"  # Replace with your OpenWeatherMap API key
    
    weather_data = get_weather_data(location, api_key)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
