from bs4 import BeautifulSoup
from dotenv import load_dotenv
from json import loads
import os
import requests
import re

'''
This web scraper retrieves all event IDs of events listed on
https://www.eventbrite.co.uk/d/australia--sydney/all-events/
'''

load_dotenv()

LINK_CLASS_NAME = "eds-media-card-content__action-link"
EVENTBRITE_API = "https://www.eventbriteapi.com/v3/events/"
EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
EVENTBRITE_URL = "https://www.eventbrite.co.uk/d"
SEARCH_PATH = "/australia--sydney/all-events/"

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
        "event_ids": event_id
    }

    response = loads(requests.get(EVENTBRITE_API, params=params, headers=headers).text)
    return response["events"][0]

def get_events():
    event_ids = scrape_event_ids()

    # call Eventbrite API
    return list(map(retrieve_event, event_ids))
