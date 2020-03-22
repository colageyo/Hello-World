class Event():
    def __init__(self, start_time, end_time, latitude, longitude, name, organiser, is_free, summary, description_html, tags = [], reviews = []):
        self._start_time = start_time
        self._end_time = end_time
        self._latitude = latitude
        self._longitude = longitude
        self._name = name
        self._organiser = organiser
        self._is_free = is_free
        self._summary = summary
        self._description_html = description_html
        self._tags = tags
        self._reviews = reviews
    
    def get_json(self):
        return {
            "start_time": self._start_time,
            "end_time": self._end_time,
            "location": {
                "latitude": self._latitude,
                "longitude": self._longitude,
            },
            "name": self._name,
            "organiser": self._organiser,
            "is_free": self._is_free,
            "summary": self._summary,
            "description_html": self._description_html,
            "tags": self._tags,
            "reviews": self._reviews
        }
