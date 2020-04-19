import datetime
import json
import os
import pathlib
import pickle

import src.events_collector
import src.event

EVENTS_CACHE_NAME = 'events_cache.pickle'
EVENTS_CACHE_PATH = os.path.join(
    pathlib.Path(__file__).parent.absolute(),
    EVENTS_CACHE_NAME
)
EVENTS_HARDCODE_NAME = 'events_cache.json'
EVENTS_HARDCODE_PATH = os.path.join(
    pathlib.Path(__file__).parent.absolute(),
    EVENTS_HARDCODE_NAME
)

def load_cache():
    with open(EVENTS_CACHE_PATH, 'rb') as f:
        return pickle.load(f)

def load_hardcode():
	with open(EVENTS_HARDCODE_PATH, 'r') as f:
		return json.load(f)

def load_events():
    cache_exists = os.path.exists(EVENTS_CACHE_PATH)

    # first, load from cache
    if cache_exists:
        cache = load_cache()

        cache_is_fresh = datetime.datetime.now() - cache['time'] <= datetime.timedelta(hours=24)

        if cache_is_fresh:
            return cache['events']

    hardcode_exists = os.path.exists(EVENTS_HARDCODE_PATH)

    # otherwise, load from hardcoded data
    if hardcode_exists:
        hardcode = load_hardcode()
        events = list(map(src.event.from_json, hardcode['events']))

    # otherwise, collect from APIs
    else:
        events = src.events_collector.collect_all()

    save_events(events)

    return events


def save_events(events):
    hardcode_exists = os.path.exists(EVENTS_HARDCODE_PATH)

    cache = {
        'events': events,
        'time': datetime.datetime.now()
    }

    if not hardcode_exists:
        hardcode = {
            'events': list(map(lambda e: e.get_serializable_json(), events)),
            'time': datetime.datetime.now().timestamp()
        }
        with open(EVENTS_HARDCODE_PATH, 'w+') as f:
            json.dump(hardcode, f)

    with open(EVENTS_CACHE_PATH, 'wb') as f:
        pickle.dump(cache, f)
