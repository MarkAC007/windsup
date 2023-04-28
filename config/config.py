import os

# OpenWeatherMap API key
OWM_API_KEY = os.environ.get('OWM_API_KEY')

# WorldTides API key
WT_API_KEY = os.environ.get('WT_API_KEY')

# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Location settings
LOCATION_LATITUDE = 42.3601
LOCATION_LONGITUDE = -71.0589
LOCATION_NAME = 'Boston, MA'
