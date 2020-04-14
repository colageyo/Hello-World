import datetime
import os
import pathlib
import pickle

import src.events_collector

EVENTS_CACHE_NAME = 'events_cache.pickle'
EVENTS_CACHE_PATH = os.path.join(
    pathlib.Path(__file__).parent.absolute(),
    EVENTS_CACHE_NAME
)


def load_cache():
    with open(EVENTS_CACHE_PATH, 'rb') as f:
        return pickle.load(f)


def load_events():
    cache_exists = os.path.exists(EVENTS_CACHE_PATH)

    if cache_exists:
        cache = load_cache()

        cache_is_fresh = datetime.datetime.now() - cache['time'] <= datetime.timedelta(hours=24)

        if cache_is_fresh:
            return cache['events']

    events = src.events_collector.collect_all()

    save_events(events)

    return events


def save_events(events):
    cache = {
        'events': events,
        'time': datetime.datetime.now()
    }
    with open(EVENTS_CACHE_PATH, 'wb') as f:
        pickle.dump(cache, f)
