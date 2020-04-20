import os
from datetime import datetime
from json import loads

import requests
from dotenv import load_dotenv

import src.conditions

'''
OpenWeather API
Weather conditions: https://openweathermap.org/weather-conditions
'''

load_dotenv()

MINUTES_IN_HOUR = 60
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'

activity_tags = {
    "clear": ["outdoors"],
    "clouds": ["indoors", "outdoors"],
    "drizzle": ["indoors"],
    "rain": ["indoors"],
    "snow": ["cozy", "indoors"],
    "thunderstorm": ["cozy", "indoors"]
}

countries = {
    "AU": "Australia",
    "FR": "France",
    "IT": "Italy",
    "JP": "Japan",
    "US": "United States of America"
}

cities = {
    "sydney": {
        "id": 6619279,
        "name": "City of Sydney",
        "state": "",
        "country": "AU",
        "coord": {
            "lon": 151.208435,
            "lat": -33.867779
        }
    },
    "melbourne": {
        "id": 7839805,
        "name": "Melbourne",
        "state": "",
        "country": "AU",
        "coord": {
            "lon": 144.944214,
            "lat": -37.813061
        }
    },
    "paris": {
        "id": 2968815,
        "name": "Paris",
        "state": "",
        "country": "FR",
        "coord": {
            "lon": 2.3486,
            "lat": 48.853401
        }
    },
    "tokyo": {
        "id": 1850147,
        "name": "Tokyo",
        "state": "",
        "country": "JP",
        "coord": {
            "lon": 139.691711,
            "lat": 35.689499
        }
    },
    "new york": {
        "id": 5128581,
        "name": "New York City",
        "state": "NY",
        "country": "US",
        "coord": {
            "lon": -74.005966,
            "lat": 40.714272
        }
    },
    "rome": {
        "id": 3169070,
        "name": "Rome",
        "state": "",
        "country": "IT",
        "coord": {
            "lon": 12.4839,
            "lat": 41.894741
        }
    }
}


def get_weather_by_city(city):
    country = countries[cities[city]["country"]]

    params = {
        "id": cities[city]["id"],
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    # call OpenWeather API
    response = loads(requests.get(WEATHER_API, params).text)

    # calculate the machine's UTC offset
    local_now = datetime.now()
    utcnow = datetime.utcnow()
    utc_offset = (local_now - utcnow).total_seconds()

    # extract information from response
    weather_icons = list(map(lambda wc: wc["icon"], response["weather"]))
    weather_conditions = list(map(lambda wc: wc["main"], response["weather"]))
    weather_descriptions = list(map(lambda wc: wc["description"], response["weather"]))
    temp = response["main"]["feels_like"]
    humidity = response["main"]["humidity"]
    # visibility = response["visibility"]
    local_sunrise = response["sys"]["sunrise"]
    local_sunset = response["sys"]["sunset"]

    # convert into the city's time
    sunrise = local_sunrise - utc_offset + response["timezone"]
    sunset = local_sunset - utc_offset + response["timezone"]
    now = utcnow.timestamp() + response["timezone"]

    # determine if sunrise/sunset is occurring within the next hour
    is_sunrise_soon = sunrise > now and sunrise - now <= MINUTES_IN_HOUR * MINUTES_IN_HOUR
    is_sunset_soon = sunset > now and sunset - now <= MINUTES_IN_HOUR * MINUTES_IN_HOUR

    # TODO(michelle) - return a json object once data to be used is confirmed
    print(f"Location: {city.capitalize()}, {country.capitalize()}")
    print(f"Time now: {datetime.fromtimestamp(now)}")
    print(f"Weather condition: {weather_conditions[0]} - {weather_descriptions[0]}")
    print(f"Weather icon: http://openweathermap.org/img/wn/{weather_icons[0]}@2x.png")
    print(f"Feels like: {temp} degrees celcius")
    print(f"Humidity: {humidity}%")
    # print(f"Visibility: {visibility}m")
    print(f"Activity tags: {activity_tags[weather_conditions[0].lower()]}")
    print(f"Sunrise: {datetime.fromtimestamp(sunrise)}")
    print(f"Sunset: {datetime.fromtimestamp(sunset)}")
    if is_sunrise_soon:
        print(f"Sunrise is within an hour from now")
    if is_sunset_soon:
        print(f"Sunset is within an hour from now")

    return src.conditions.Conditions(
        f'{weather_conditions[0]} - {weather_descriptions[0]}',
        datetime.fromtimestamp(now),
        temp,
        humidity,
        # visibility,
        activity_tags[weather_conditions[0].lower()],
        datetime.fromtimestamp(sunrise),
        datetime.fromtimestamp(sunset),
        float(cities['sydney']['coord']['lon']),
        float(cities['sydney']['coord']['lat'])
    )
