from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
from json import loads, load, dumps
import os
import re
import pytz
import requests

'''
This module scrapes all event IDs of events listed on
https://www.eventbrite.co.uk/d/australia--sydney/events--this-week/
and calls the Eventbrite API to retrieve event details
'''

if __name__ == '__main__':
    import sys

    cwd = os.getcwd()
    sys.path.append(cwd)

from src.event import Event

load_dotenv()

BATCH_PATH = "batch/"
EVENTBRITE_API = "https://www.eventbriteapi.com/v3/"
EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
EVENTBRITE_URL = "https://www.eventbrite.co.uk/d"
EVENTS_PATH = "events/"
LINK_CLASS_NAME = "eds-media-card-content__action-link"
NAV_LINK_ATTRS = { "data-spec": "paginator__last-page-link" }
PAGE_LIMIT = 5
PAGE_PATH = "?page="
SEARCH_PATH = "/australia--sydney/events--this-week/"

# Categories
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

# Formats
CONFERENCE = "1"
SEMINAR = "2"
EXPO = "3"
CONVENTION = "4"
FESTIVAL = "5"
PERFORMANCE = "6"
SCREENING = "7"
GALA = "8"
CLASS = "9"
NETWORKING = "10"
PARTY = "11"
RALLY = "12"
TOURNAMENT = "13"
GAME = "14"
RACE = "15"
TOUR = "16"
ATTRACTION = "17"
CAMP = "18"
APPEARANCE = "19"
OTHER = "20"

# All tags: "artsy", "sporty", "romantic", "family-friendly", "geeky", "history", "hungry"
CATEGORIES_TAGS = {
    ALL_TAGS: [],
    BOAT_AIR: [],
    BUSSINESS_PROFESSIONAL: ["geeky"],
    CHARITY: [],
    COMMUNITY_CULTURE: ["family-friendly"],
    FAMILY_EDUCATION: ["family-friendly"],
    FASHION: ["artsy"],
    FILM_MEDIA_ENTERTAINMENT: ["artsy", "romantic"],
    FOOD: ["hungry"],
    GOVERMENT: ["geeky"],
    HEALTH: ["artsy"],
    HOBBY: ["artsy", "geeky"],
    LIFESTYLE: ["artsy"],
    MUSIC: ["artsy"],
    PERFORMING_VISUAL_ARTS: ["artsy"],
    RELIGION: [],
    SCHOOL: ["family-friendly"],
    SCIENCE: ["geeky"],
    SEASONAL_HOLIDAY: [],
    SPORTS: ["sporty"],
    TRAVEL: ["outdoors"]
}

FORMAT_TAGS = {
    CONFERENCE: ["indoors"],
    SEMINAR: ["indoors"],
    EXPO: ["indoors"],
    CONVENTION: ["indoors"],
    FESTIVAL: [],
    PERFORMANCE: ["romantic"],
    SCREENING: ["romantic"],
    GALA: ["hungry", "romantic"],
    CLASS: [],
    NETWORKING: ["geeky"],
    PARTY: ["fun"],
    RALLY: [],
    TOURNAMENT: [],
    GAME: [],
    RACE: [],
    TOUR: ["geeky", "historic"],
    ATTRACTION: ["historic"],
    CAMP: ["outdoors"],
    APPEARANCE: [],
    OTHER: []
}

headers = {
    "Authorization": f"Bearer {EVENTBRITE_API_KEY}"
}

def extract_html(path):
    '''Given a path for the Eventbrite website, scrapes the webpage at that path'''
    page = requests.get(EVENTBRITE_URL + path)
    return BeautifulSoup(page.text, "html.parser")

def extract_event_id(event):
    '''Given a html tag containing a link to an event, extract the event id'''
    link = event.get('href')
    match = re.match('.*-([0-9]+)\?.*', link)
    return match.group(1) if match is not None else ""

def scrape_event_ids():
    '''Scrape all search results for "Events in Sydney, Australia, this week" and return a list of event ids'''
    eventbrite = extract_html(SEARCH_PATH)

    # retrieve number of pages
    nav_text = eventbrite.find(attrs=NAV_LINK_ATTRS).get_text()
    max_pages = int(re.search(r'[^\d]*(\d+)', nav_text).group(1))
    num_pages = max_pages if max_pages <= PAGE_LIMIT else PAGE_LIMIT

    # scrape each page and retrieve html tags containing links to events
    all_tags = []
    for i in range(num_pages):
        page = extract_html(SEARCH_PATH + PAGE_PATH + str(i + 1))
        all_tags.extend(page.find_all("a", class_=LINK_CLASS_NAME))

    # get event ids from tags
    return set(filter(lambda e: e != "", map(extract_event_id, all_tags)))

def retrieve_event_query(event_id):
    '''Given an event id, construct a JSON object for the batch request'''
    return {
        "method": "GET",
        "relative_url": f"{EVENTS_PATH}?event_ids={event_id}&expand=logo,venue,organizer,format,ticket_availability"
    }

def get_tags(category_id, format_id):
    '''Given a category ID and format ID, generate a list of activity tags'''
    category_tags = CATEGORIES_TAGS.get(category_id) if category_id is not None and category_id in CATEGORIES_TAGS else []
    format_tags = FORMAT_TAGS.get(format_id) if format_id is not None and format_id in FORMAT_TAGS else []
    return list(set(category_tags + format_tags))

def retrieve_event(response):
    '''Given an Event from an Eventbrite API response, create an Event object'''
    format_id = response["format"]["id"] if response["format"] is not None else None
    price = 0
    if "ticket_availability" in response:
        if "minimum_ticket_price" in response["ticket_availability"] and response["ticket_availability"]["minimum_ticket_price"] is not None:
            price = float(response["ticket_availability"]["minimum_ticket_price"]["major_value"])
    return Event(
        event_id=f"EVENTBRITE-{response['url']}",
        url=response["url"],
        start_time=datetime.strptime(response["start"]["utc"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        end_time=datetime.strptime(response["end"]["utc"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        latitude=float(response["venue"]["latitude"]) if response["venue"] is not None else "",
        longitude=float(response["venue"]["longitude"]) if response["venue"] is not None else "",
        name=response["name"]["text"],
        organiser=response["organizer"]["name"],
        price=price,
        is_online=response["online_event"] or is_online(response),
        summary=response["summary"],
        description_html=response["description"]["html"],
        tags=get_tags(response["category_id"], format_id),
        image=response["logo"]["original"]["url"] if response.get("logo") is not None else ""
    )

def get_events():
    '''When called, executes the web scraping and API calls, to generate a list of Event objects'''
    
    print('Eventbrite')
    
    # scrape for event ids
    event_ids = scrape_event_ids()

    # construct batch query
    data = {
        "batch": dumps(list(map(retrieve_event_query, event_ids)))
    }

    # call Eventbrite API using batch request
    response = loads(requests.post(EVENTBRITE_API + BATCH_PATH, data=data, headers=headers).text)
    event_responses = list(map(lambda r : loads(r["body"])["events"][0], response))
    filtered_responses = list(filter(is_appropriate, event_responses))

    # normalize as Event objects
    return list(map(retrieve_event, filtered_responses))

def is_appropriate(event_response):
    '''Given an Event from an Eventbrite API response, determines if appropriate for display'''
    is_dating_event = re.search(r'dating', event_response["name"]["text"].lower()) is not None
    in_summary = re.search(r'(cancelled|canceled|postponed|suspended)', event_response["summary"].lower()) is not None
    in_description = re.search(r'(cancelled|canceled|postponed|suspended)', event_response["description"]["text"].lower()) is not None
    in_name = re.search(r'(cancelled|canceled|postponed)', event_response["name"]["text"].lower()) is not None
    return not any([is_dating_event, in_summary, in_description, in_name])

def is_online(event_response):
    '''Given an Event from an Eventbrite API response, determines if it is online'''
    in_summary = re.search(r'(now online|virtual)', event_response["summary"].lower()) is not None
    in_description = re.search(r'(now online|virtual)', event_response["description"]["text"].lower()) is not None
    in_name = re.search(r'(now online|virtual)', event_response["name"]["text"].lower()) is not None
    return any([in_summary, in_description, in_name])

if __name__ == '__main__':
    for event in get_events():
        print('----------------------------')
        print("Name: " + event._name)
        print("URL: " + event._url)
        print("Time: "
              + str(datetime.fromtimestamp(event._start_time, tz=pytz.timezone('Australia/Sydney')))
              + " to "
              + str(datetime.fromtimestamp(event._end_time, tz=pytz.timezone('Australia/Sydney'))))
        if event._organiser is not None:
            print("Organiser: " + event._organiser)
        print("Summary: " + event._summary)
        print("Price? " + str(event._price))
        print("Is online? " + str(event._is_online))
        print("Tags: " + str(event._tags))
        print("Image: " + str(event._image))
