import os
import requests
import datetime
import pytz
from send_email import send_email
from check_conditions import check_conditions
from config import *

def main():
    # Get the current time in the specified timezone
    timezone = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(tz=timezone)

    # Get the weather data
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={LOCATION_LATITUDE}&lon={LOCATION_LONGITUDE}&appid={OWM_API_KEY}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Get the tide data
    tide_url = f'https://www.worldtides.info/api/v2?heights&extremes&lat={LOCATION_LATITUDE}&lon={LOCATION_LONGITUDE}&start={now.year}-{now.month}-{now.day}&length=1&key={WT_API_KEY}'
    tide_response = requests.get(tide_url)
    tide_data = tide_response.json()

    # Get the wind data
    wind_direction = weather_data['wind']['deg']
    if wind_direction > 337.5 or wind_direction <= 22.5:
        wind_direction_text = 'north'
    elif wind_direction > 22.5 and wind_direction <= 67.5:
        wind_direction_text = 'northeast'
    elif wind_direction > 67.5 and wind_direction <= 112.5:
        wind_direction_text = 'east'
    elif wind_direction > 112.5 and wind_direction <= 157.5:
        wind_direction_text = 'southeast'
    elif wind_direction > 157.5 and wind_direction <= 202.5:
        wind_direction_text = 'south'
    elif wind_direction > 202.5 and wind_direction <= 247.5:
        wind_direction_text = 'southwest'
    elif wind_direction > 247.5 and wind_direction <= 292.5:
        wind_direction_text = 'west'
    elif wind_direction > 292.5 and wind_direction <= 337.5:
        wind_direction_text = 'northwest'
    else:
        wind_direction_text = 'unknown'

    # Check the conditions
    conditions = check_conditions(weather_data, tide_data, wind_direction_text)

    # Send an email if the conditions are met
    if conditions:
        subject = f"Conditions met in {LOCATION_NAME}!"
        body = f"Low tide before midday, {wind_direction_text} winds, no rain forecasted."
        send_email(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, subject, body)

if __name__ == '__main__':
    main()
