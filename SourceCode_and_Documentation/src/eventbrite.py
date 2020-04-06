from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
from json import loads, load
import os
import pytz
import requests
import re

'''
This module scrapes all event IDs of events listed on
https://www.eventbrite.co.uk/d/australia--sydney/all-events/
and calls the Eventbrite API to retrieve event details
'''

if __name__ == '__main__':
    import sys
    cwd = os.getcwd()
    sys.path.append(cwd)

from src.event import Event

load_dotenv()

EVENTBRITE_API = "https://www.eventbriteapi.com/v3/"
EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
EVENTBRITE_URL = "https://www.eventbrite.co.uk/d"
EVENTS_PATH = "events/"
LINK_CLASS_NAME = "eds-media-card-content__action-link"
SEARCH_PATH = "/australia--sydney/all-events/"

ALL_TAGS = "199"
BOAT_AIR = "118"
BUSSINESS_PROFESSIONAL = "101"
CHARITY = "111"
COMMUNITY_CULTURE = "113"
FAMILY_EDUCATION = "115"
FASHION = "106"
FILM_MEDIA_ENTERTAINMENT = "104"
FOOD = "110"
GOVERMENT = "112"
HEALTH = "107"
HOBBY = "119"
LIFESTYLE = "117"
MUSIC = "103"
PERFORMING_VISUAL_ARTS = "105"
RELIGION = "114"
SCHOOL = "120"
SCIENCE = "102"
SEASONAL_HOLIDAY = "116"
SPORTS = "108"
TRAVEL = "109"

#TODO - determine if an event is indoors/outdoors
ACTIVITIES_TAG = {
    ALL_TAGS: {"artsy", "indoors", "outdoors", "sporty", "romantic", "family-friendly", "geeky", "history", "hungry"},
    BOAT_AIR: {"outdoors"},
    BUSSINESS_PROFESSIONAL: {"geeky", "indoors", "outdoors"},
    CHARITY: {"indoors", "outdoors"},
    COMMUNITY_CULTURE: {"indoors", "outdoors"},
    FAMILY_EDUCATION: {"family-friendly", "indoors", "outdoors"},
    FASHION: {"artsy", "indoors", "outdoors"},
    FILM_MEDIA_ENTERTAINMENT: {"artsy", "romantic", "indoors", "outdoors"},
    FOOD: {"hungry", "family-friendly", "indoors", "outdoors"},
    GOVERMENT: {"geeky", "indoors", "outdoors"},
    HEALTH: {"artsy", "indoors", "outdoors"},
    HOBBY: {"artsy", "geeky", "indoors", "outdoors"},
    LIFESTYLE: {"artsy", "indoors", "outdoors"},
    MUSIC: {"artsy", "romantic", "indoors", "outdoors"},
    PERFORMING_VISUAL_ARTS: {"artsy", "romantic", "indoors", "outdoors"},
    RELIGION: {"indoors", "outdoors"},
    SCHOOL: {"family-friendly", "indoors", "outdoors"},
    SCIENCE: {"geeky", "indoors", "outdoors"},
    SEASONAL_HOLIDAY: {"indoors", "outdoors"},
    SPORTS: {"sporty", "indoors", "outdoors"},
    TRAVEL: {"outdoors"}
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
        url = response["url"],
        start_time = datetime.strptime(response["start"]["utc"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        end_time = datetime.strptime(response["end"]["utc"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        latitude = response["venue"]["latitude"] if response["venue"] is not None else "",
        longitude = response["venue"]["longitude"] if response["venue"] is not None else "",
        name = response["name"]["text"],
        organiser = response["organizer"]["name"],
        is_free = response["is_free"],
        is_online = response["online_event"],
        summary = response["summary"],
        description_html = response["description"]["html"],
        tags = ACTIVITIES_TAG.get(response["category_id"])
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
