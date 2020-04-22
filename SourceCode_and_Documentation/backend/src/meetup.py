from datetime import datetime
from dotenv import load_dotenv
from json import loads
import pytz
import os
import requests
import re

if __name__ == '__main__':
    import sys
    cwd = os.getcwd()
    sys.path.append(cwd)

from src.event import Event

load_dotenv()

MEETUP_API = "https://api.meetup.com/2/open_events"
THREE_HOURS_IN_SECONDS = 3 * 60 * 60
SIG_ID = 305125502

# Categories
ARTS_AND_CULTURE = 1
CAREER_AND_BUSINESS = 2
CARS_AND_MOTORCYCLES = 3
COMMUNITY_AND_ENVIRONMENT = 4
DANCING = 5
EDUCATION_AND_LEARNING = 6
FASHION_AND_BEAUTY = 8
FITNESS = 9
FOOD_AND_DRINK = 10
GAMES = 11
LGBT = 12
MOVEMENTS_AND_POLITICS = 13
HEALTH_AND_WELLBEING = 14
HOBBIES_AND_CRAFTS = 15
LANGUAGE_AND_ETHNIC_IDENTITY = 16
BOOK_CLUBS = 18

REQUEST_SIG = {
    "Sydney": {
        1: "954a7e8e1647538aa50b91934a8a2bbca1f532d3",
        2: "960fa5ff1a527ee249c45716bc822088377d1d44",
        3: "9cff013a919899c3c5e0cdf02c5b8ccaf48a1856",
        4: "81de3ea7c704d2cc7405f4aa417aca9658bf2662",
        5: "1b6dfe9a6c0aff69db948786a28f3c9a5b6d407f",
        6: "b0d703b294e3a30fb90f15e768c5da2c47a55d02",
        8: "9f1c2375417e3b1bb04fff593d14bf9cfdaa628d",
        9: "51d1f97f832f12380d70c3553f6544ca44e42cb4",
        10: "998f1c93d45d0c20e7441ca51c8120ac0cdad54e",
        11: "3533b5f5192980304868be43dd94823d4176ab5a",
        12: "ce6bcfd0ecae2dd22db5fb361e2e81fb9e60b8ee",
        13: "f0a3c022182fdb9271e43869ef0ba7c2e1901b88",
        14: "33544345c652c72fd31d9b2b58b3173df9d2e402",
        15: "d7b0ceb875e520cc2ccaa50f362ef5b1a00d91ea",
        16: "8dc3254ea6f9ed7f2924f552c8f055ea2872187e",
        18: "929169193d10c6e925e3233a22d52161456f5202",
    }
}

# TODO - determine if indoors or outdoors
ACTIVITY_TAGS = {
    ARTS_AND_CULTURE: ["artsy"],
    CAREER_AND_BUSINESS: ["geeky"],
    CARS_AND_MOTORCYCLES: ["outdoors"],
    COMMUNITY_AND_ENVIRONMENT: ["outdoors"],
    DANCING: ["sporty", "romantic"],
    EDUCATION_AND_LEARNING: ["geeky"],
    FASHION_AND_BEAUTY: ["artsy"],
    FITNESS: ["sporty"],
    FOOD_AND_DRINK: ["hungry"],
    GAMES: ["geeky"],
    LGBT: [],
    MOVEMENTS_AND_POLITICS: ["geeky", "historic"],
    HEALTH_AND_WELLBEING: ["sporty"],
    HOBBIES_AND_CRAFTS: ["artsy"],
    LANGUAGE_AND_ETHNIC_IDENTITY: ["artsy"],
    BOOK_CLUBS: ["geeky"]
}

def get_params(city, category_id):
    return {
        "and_text": False,
        "offset": 0,
        "city": city,
        "format": "json",
        "limited_events": False,
        "photo-host": "public",
        "page": 20,
        "radius": 25.0,
        "category": category_id,
        "desc": False,
        "status": "upcoming",
        "sig_id": SIG_ID,
        "sig": REQUEST_SIG[city][category_id]
    }

def get_activity_tags(event, category_id):
    tags = set(ACTIVITY_TAGS[category_id])
    if is_event_family_friendly(event):
        tags.add("family-friendly")
    return list(tags)

def is_event_family_friendly(event_response):
    '''Given an Event from the Meetup API response, determines if it is kid-friendly'''
    in_description = re.search(r'(kids|(kid|family)[ -]friendly)', event_response["description"].lower()) is not None if "description" in event_response else False
    in_name = re.search(r'(kids|(kid|family)[ -]friendly)', event_response["name"].lower()) is not None if "name" in event_response else False
    return any([in_description, in_name])

def is_event_online(event_response):
    '''Given an Event from the Meetup API response, determines if it is online'''
    in_venue = re.search(r'(zoom|online|webinar|virtual)', event_response["venue"]["name"].lower()) is not None if "venue" in event_response else False
    in_description = re.search(r'(zoom|now online|virtual|webinar)', event_response["description"].lower()) is not None if "description" in event_response else False
    in_name = re.search(r'(zoom|now online|virtual|webinar)', event_response["name"].lower()) is not None if "name" in event_response else False
    return any([in_venue, in_description, in_name])

def normalise_response(response, category_id):
    start_time = int(response["time"])
    duration = int(response["duration"]) if "duration" in response else THREE_HOURS_IN_SECONDS
    tags = get_activity_tags(response, category_id)
    image = ""
    if "photo_url" in response:
        image = re.sub("global", "highres", response["photo_url"])
    return Event(
        event_id = f"MEETUP-{response['event_url']}",
        url = response['event_url'],
        start_time = start_time / 1000,
        end_time = (start_time + duration) / 1000,
        latitude = float(response["venue"]["lat"]) if "venue" in response else "",
        longitude = float(response["venue"]["lon"]) if "venue" in response else "",
        name = response["name"].strip(),
        organiser = response["group"]["name"],
        price = float(response["fee"]["amount"]) if "fee" in response else 0,
        is_online = is_event_online(response),
        summary = "",
        description_html = response["description"] if "description" in response else "",
        tags = tags,
        image = image
    )

def get_meetups():
    print('Meetup')

    city = "Sydney"

    all_events = []
    for category_id in range(1, 19):
        if category_id not in REQUEST_SIG[city]: continue
        params = get_params(city, category_id)
        events = loads(requests.get(MEETUP_API, params=params).text)
        if "results" in events:
            all_events.extend(list(map(lambda e: normalise_response(e, category_id), events["results"])))
    return all_events

if __name__ == '__main__':
    for meetup in get_meetups():
        print('----------------------------')
        print("Name: " + meetup._name)
        print("URL: " + str(meetup._url))
        print("Time: "
            + str(datetime.fromtimestamp(meetup._start_time, tz=pytz.timezone('Australia/Sydney')))
            + " to "
            + str(datetime.fromtimestamp(meetup._end_time,  tz=pytz.timezone('Australia/Sydney'))))
        if meetup._organiser is not None:
            print("Organiser: " + meetup._organiser)
        print("Summary: " + meetup._summary)
        print("Price? " + str(meetup._price))
        print("Is online? " + str(meetup._is_online))
        print("Tags: " + str(meetup._tags))
        if meetup._image is not "":
            print("Image: " + str(meetup._image))
