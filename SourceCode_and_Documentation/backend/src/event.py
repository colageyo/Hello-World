class Event:
    def __init__(self, event_id, url, start_time, end_time, latitude, longitude, name, organiser, is_free, is_online,
                 summary, description_html, tags=[], reviews=[]):
        self._event_id = event_id
        self._url = url
        self._start_time = start_time
        self._end_time = end_time
        self._latitude = latitude
        self._longitude = longitude
        self._name = name
        self._organiser = organiser
        self._is_free = is_free
        self._is_online = is_online
        self._summary = summary
        self._description_html = description_html
        self._tags = tags
        self._reviews = reviews

    @property
    def events_id(self):
        return self._event_id

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def organiser(self):
        return self._organiser

    @organiser.setter
    def organiser(self, value):
        self._organiser = value

    @property
    def is_free(self):
        return self._is_free

    @is_free.setter
    def is_free(self, value):
        self._is_free = value

    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @property
    def description_html(self):
        return self._description_html

    @description_html.setter
    def description_html(self, value):
        self._description_html = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value

    def is_of_type(self, t):
        return t in self.tags or t in self.description_html

    def is_only_outdoors(self):
        return self.is_of_type('outdoors')

    def is_only_indoors(self):
        return self.is_of_type('indoors')

    def is_described_by(self, tags):
        return tags.issubset(self.tags) or tags.issubset(self.description_html)

    def get_json(self):
        return {
            "event_id": self._event_id,
            "url": self._url,
            "start_time": self._start_time,
            "end_time": self._end_time,
            "location": {
                "latitude": self._latitude,
                "longitude": self._longitude,
            },
            "name": self._name,
            "organiser": self._organiser,
            "is_free": self._is_free,
            "is_online": self._is_online,
            "summary": self._summary,
            "description_html": self._description_html,
            "tags": self._tags,
            "reviews": self._reviews
        }

    def get_serializable_json(self):
        json = self.get_json()

        for key, value in json.items():
            if isinstance(value, set):
                json[key] = list(value)

        return json
