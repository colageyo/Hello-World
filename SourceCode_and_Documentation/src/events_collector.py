import src.eventbrite
import src.places


def collect_all():
    eventbrite_events = src.eventbrite.get_events()
    foursquare_events = src.places.get_all_events()

    return eventbrite_events + foursquare_events
