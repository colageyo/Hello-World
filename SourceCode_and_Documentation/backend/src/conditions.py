import datetime
import math

EARTH_RADIUS = 6371
MINUTES_IN_HOUR = 60

# Why is this 72?!
# Assuming the guy is driving 50km/h => 50/60^2 km/sec = 5/6*60 = 1/72 => takes distance * 72 seconds
TIME_TAKEN_MULTIPLICATION_FACTOR = 72


class Conditions:
    def __init__(self, weather, time, temperature, humidity, activity_tags, sunrise, sunset, longitude,
                 latitude):
        self._weather = weather
        self._time = time
        self._temperature = temperature
        self._humidity = humidity
        # self._visibility = visibility
        self._activity_tags = activity_tags
        self._sunrise = sunrise
        self._sunset = sunset
        self._longitude = longitude
        self._latitude = latitude

    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, value):
        self._weather = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    # @property
    # def visibility(self):
    #     return self._visibility

    # @visibility.setter
    # def visibility(self, value):
    #     self._visibility = value

    @property
    def activity_tags(self):
        return self._activity_tags

    @activity_tags.setter
    def activity_tags(self, value):
        self._activity_tags = value

    @property
    def sunrise(self):
        return self._sunrise

    @sunrise.setter
    def sunrise(self, value):
        self._sunrise = value

    @property
    def sunset(self):
        return self._sunset

    @sunset.setter
    def sunset(self, value):
        self._sunset = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    def is_too_hot(self):
        return self.temperature >= 30

    def is_too_cold(self):
        return self.temperature <= 15

    def is_too_humid(self):
        return self.humidity >= 70

    def is_too_late(self):
        ten_pm_tonight = datetime.datetime.now().replace(hour=22, minute=0, second=0, microsecond=0)

        return self.time > ten_pm_tonight

    def is_too_early(self):
        seven_am_today = datetime.datetime.now().replace(hour=22, minute=0, second=0, microsecond=0)

        return self.time < seven_am_today

    # def is_too_hazy(self):
    #     return self.visibility < 10000

    def is_sunrise_soon(self):
        sunrise = self.sunrise.timestamp()
        time = self.time.timestamp()
        return sunrise > time and sunrise - time <= MINUTES_IN_HOUR * MINUTES_IN_HOUR

    def is_sunset_soon(self):
        sunset = self.sunset.timestamp()
        time = self.time.timestamp()
        return sunset > time and sunset - time <= MINUTES_IN_HOUR * MINUTES_IN_HOUR

    def distance_to(self, longitude, latitude):
        if not longitude or not latitude:
            return 0

        # Determine distance difference using Haversine formula
        lon1, lat1, lon2, lat2 = map(math.radians, [float(longitude), float(latitude), self.longitude, self.latitude])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))

        return c * EARTH_RADIUS

    def is_close_to(self, longitude, latitude):
        return self.distance_to(longitude, latitude) < 30

    def time_taken_to_reach(self, longitude, latitude):
        return int(self.distance_to(longitude, latitude) * TIME_TAKEN_MULTIPLICATION_FACTOR)

    def get_json(self):
        return {
            "weather": self._weather,
            "time": self._time.timestamp(),
            "temperature": self._temperature,
            "humidity": self._humidity,
            "location": {
                "latitude": self._latitude,
                "longitude": self._longitude,
            },
            # "visibility": self._visibility,
            "activity_tags": self._activity_tags,
            "sunrise": self._sunrise.timestamp(),
            "sunset": self._sunset.timestamp(),
            "is_sunrise_soon": self.is_sunrise_soon(),
            "is_sunset_soon": self.is_sunset_soon()
        }
