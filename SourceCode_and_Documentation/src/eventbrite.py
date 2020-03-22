from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
from json import loads, load
from src.event import Event
import os
import pytz
import requests
import re

'''
This module scrapes all event IDs of events listed on
https://www.eventbrite.co.uk/d/australia--sydney/all-events/
and calls the Eventbrite API to retrieve event details
'''

load_dotenv()

LINK_CLASS_NAME = "eds-media-card-content__action-link"
EVENTBRITE_API = "https://www.eventbriteapi.com/v3/"
EVENTS_PATH = "events/"
EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
EVENTBRITE_URL = "https://www.eventbrite.co.uk/d"
SEARCH_PATH = "/australia--sydney/all-events/"

#TODO - determine if an event is indoors/outdoors
activity_tags = {
    # Music
    "103": ["artsy", "romantic", "indoors", "outdoors"],

    # Business & Professional
    "101": ["geeky", "indoors", "outdoors"],

    # Food & Drink
    "110": ["hungry", "family-friendly", "indoors", "outdoors"],

    # Community & Culture
    "113": ["indoors", "outdoors"],

    # Performing & Visual Arts
    "105": ["artsy", "romantic", "indoors", "outdoors"],

    # Film, Media & Entertainment
    "104": ["artsy", "romantic", "indoors", "outdoors"],

    # Sports & Fitness
    "108": ["sporty", "indoors", "outdoors"],

    # Health & Wellness
    "107": ["artsy", "indoors", "outdoors"],

    # Science & Technology
    "102": ["geeky", "indoors", "outdoors"],

    # Travel & Outdoor
    "109": ["outdoors"],

    # Charity & Causes
    "111": ["indoors", "outdoors"],

    # Religion & Spirituality
    "114": ["indoors", "outdoors"],

    # Family & Education
    "115": ["family-friendly", "indoors", "outdoors"],
    
    # Seasonal & Holiday
    "116": ["indoors", "outdoors"],

    # Government & Politics
    "112": ["geeky", "indoors", "outdoors"],

    # Fasion & Beauty
    "106": ["artsy", "indoors", "outdoors"],

    # Home & Lifestyle
    "117": ["artsy", "indoors", "outdoors"],

    # Auto, Boat & Air
    "118": ["outdoors"],

    # Hobbies & Special Interest
    "119": ["artsy", "geeky", "indoors", "outdoors"],

    # Other
    # Give all tags for now
    "199": ["artsy", "indoors", "outdoors", "sporty", "romantic", "family-friendly", "geeky", "history", "hungry"],

    # School Activities
    "120": ["family-friendly", "indoors", "outdoors"]
}

headers = {
    "Authorization": f"Bearer {EVENTBRITE_API_KEY}"
}

def extract_html(path):
    page = requests.get(EVENTBRITE_URL + path)
    return BeautifulSoup(page.text, "html.parser")

def extract_event_id(event):
    link = event.get('href')
    match = re.match('.*-([0-9]+)\?.*', link)
    return match.group(1)

def scrape_event_ids():
    eventbrite = extract_html(SEARCH_PATH)

    # retrieve html tags containing links to events
    tags = eventbrite.find_all("a", class_=LINK_CLASS_NAME)

    # get event ids from tags
    return set(map(extract_event_id, tags))

def retrieve_event(event_id):
    params = {
        "event_ids": event_id,
        "expand": "venue,organizer"
    }

    response = loads(requests.get(EVENTBRITE_API + EVENTS_PATH, params=params, headers=headers).text)["events"][0]

    return Event(
        event_id = f"EVENTBRITE-{event_id}",
        start_time = datetime.strptime(response["start"]["utc"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        end_time = datetime.strptime(response["end"]["utc"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        latitude = response["venue"]["latitude"],
        longitude = response["venue"]["longitude"],
        name = response["name"]["text"],
        organiser = response["organizer"]["name"],
        is_free = response["is_free"],
        is_online = response["online_event"],
        summary = response["summary"],
        description_html = response["description"]["html"],
        tags = activity_tags.get(response["category_id"])
    )

def get_events():
    event_ids = scrape_event_ids()

    # call Eventbrite API
    return list(map(retrieve_event, event_ids))

if __name__ == '__main__':
    for event in get_events():
        print('----------------------------')
        print("Name: " + event._name)
        print("Time: "
            + str(datetime.fromtimestamp(event._start_time, tz=pytz.timezone('Australia/Sydney')))
            + " to "
            + str(datetime.fromtimestamp(event._end_time,  tz=pytz.timezone('Australia/Sydney'))))
        if event._organiser is not None:
            print("Organiser: " + event._organiser)
        print("Summary: " + event._summary)
        print("Is free? " + str(event._is_free))
        print("Is online? " + str(event._is_online))
        print("Tags: " + str(event._tags))
