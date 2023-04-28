import pytest
from check_conditions import check_conditions

@pytest.mark.parametrize('weather_data, tide_data, wind_direction, expected', [
    ({
        'weather': [{'main': 'Rain'}],
        'wind': {'deg': 90}
    }, {
        'extremes': [{'dt': 1643577600}, {'dt': 1643609400}]
    }, 'east', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 45}
    }, {
        'extremes': [{'dt': 1643585400}, {'dt': 1643617200}]
    }, 'northeast', True),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 315}
    }, {
        'extremes': [{'dt': 1643585400}, {'dt': 1643617200}]
    }, 'northwest', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 135}
    }, {
        'extremes': [{'dt': 1643585400}, {'dt': 1643617200}]
    }, 'southeast', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 225}
    }, {
        'extremes': [{'dt': 1643585400}, {'dt': 1643617200}]
    }, 'southwest', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 180}
    }, {
        'extremes': [{'dt': 1643585400}, {'dt': 1643617200}]
    }, 'south', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 0}
    }, {
        'extremes': [{'dt': 1643585400}, {'dt': 1643617200}]
    }, 'north', True),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 270}
    }, {
        'extremes': [{'dt': 1643577600}, {'dt': 1643609400}]
    }, 'west', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 180}
    }, {
        'extremes': [{'dt': 1643577600}, {'dt': 1643609400}]
    }, 'north', False),
    ({
        'weather': [{'main': 'Clear'}],
        'wind': {'deg': 180}
    }, {
        'extremes': [{'dt': 1643619000}, {'dt': 1643650800}]
    }, 'north', True),
])
def test_check_conditions(weather_data, tide_data, wind_direction, expected):
    assert check_conditions(weather_data, tide_data, wind_direction) == expected
