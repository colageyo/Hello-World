class Event:
    def __init__(self, event_id, url, start_time, end_time, latitude, longitude, name, organiser, price, is_online,
                 summary, description_html, tags=[], price_tier = 0, rating = 0, image = ""):
        self._event_id = event_id
        self._url = url
        self._start_time = start_time
        self._end_time = end_time
        self._latitude = latitude
        self._longitude = longitude
        self._name = name
        self._organiser = organiser
        self._price = price
        self._is_online = is_online
        self._summary = summary
        self._description_html = description_html
        self._tags = tags
        self._price_tier = price_tier
        self._rating = rating
        self._image = image

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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

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
    def price_tier(self):
        return self._price_tier

    @price_tier.setter
    def price_tier(self, value):
        self._price_tier = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def is_of_type(self, t):
        return t in self.tags or t in self.description_html

    def is_only_outdoors(self):
        return self.is_of_type('outdoors')

    def is_only_indoors(self):
        return self.is_of_type('indoors')

    def is_described_by(self, tags):
        return tags.issubset(self.tags)

    def is_ended(self, time):
        return self._end_time <= time.timestamp() if self._end_time > 0 else False

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
            "price": self._price,
            "is_online": self._is_online,
            "summary": self._summary,
            "description_html": self._description_html,
            "tags": self._tags,
            "price_tier": self._price_tier,
            "rating": self._rating,
            "image": self._image
        }

    def get_serializable_json(self):
        json = self.get_json()

        for key, value in json.items():
            if isinstance(value, set):
                json[key] = list(value)

        return json

def from_json(event):
    return Event(
        event_id=event["event_id"],
        url=event["url"],
        start_time=event["start_time"],
        end_time=event["end_time"],
        latitude=float(event["location"]["latitude"]) if event["location"]["latitude"] != "" else "",
        longitude=float(event["location"]["longitude"]) if event["location"]["longitude"] != "" else "",
        name=event["name"],
        organiser=event["organiser"],
        price=float(event["price"]),
        is_online=event["is_online"],
        summary=event["summary"],
        description_html=event["description_html"],
        tags=event["tags"],
        price_tier=event["price_tier"],
        rating=float(event["rating"]),
        image=event["image"]
    )