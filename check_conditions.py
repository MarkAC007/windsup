import datetime

def check_conditions(weather_data, tide_data, wind_direction):
    # Check if the tide is low before midday
    timezone = datetime.timezone(datetime.timedelta(hours=-4)) # US/Eastern
    now = datetime.datetime.now(tz=timezone)
    midday = datetime.time(hour=12, minute=0)
    tide_times = [datetime.datetime.fromtimestamp(int(t['dt']), tz=timezone).time() for t in tide_data['extremes']]
    low_tide_before_midday = any([tide_time < midday for tide_time in tide_times if tide_time > now.time()])

    # Check if the wind is easterly
    easterly_wind = wind_direction == 'east'

    # Check if there's no rain forecasted
    no_rain = weather_data['weather'][0]['main'] != 'Rain'

    # Return True if all conditions are met, False otherwise
    return low_tide_before_midday and easterly_wind and no_rain
