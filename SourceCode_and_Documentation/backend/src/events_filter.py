import datetime

import src.weather


def filter_events(events, tags):
    events = filter_by_tags(events, tags)
    events = filter_by_location(events)

    return events


def filter_by_tags(events, tags):
    filtered_events = []

    for event in events:
        if event.is_described_by(tags):
            filtered_events.append(event)

    return filtered_events


def suitable(event, location):
    if not location.is_close_to(event.longitude, event.latitude):
    # if event.is_ended(location.time) or not location.is_close_to(event.longitude, event.latitude):
        return False

    # if event.start_time != '' and datetime.datetime.now().timestamp() + location.time_taken_to_reach(event.longitude,
    #                                                                                                  event.latitude) > int(
    #         event.start_time):
    #     return False

    # if event.is_only_outdoors() and (
    #         location.is_too_humid() or
    #         location.is_too_hot() or
    #         location.is_too_early() or
    #         location.is_too_late() or
    #         location.is_too_hazy()
    # ):
    #     return False

    return True


def filter_by_location(events):
    location = src.weather.get_weather_by_city('sydney')

    filtered_events = []

    for event in events:
        if suitable(event, location):
            filtered_events.append(event)

    return filtered_events
