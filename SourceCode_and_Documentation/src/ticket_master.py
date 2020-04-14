import json, requests
from event import Event
from datetime import datetime, timedelta

URL = 'https://app.ticketmaster.com/discovery/v2/events'
API_KEY = 's1zvxw6AwOPPr7ej3vaA4EykE2LeO0vU'
CLASSIFICATIONS = {
    'Amusement Park': ['outdoors', 'family-friendly', 'sporty'],
    'Arts & Theatre': ['indoors', 'family-friendly', 'artsy'],
    'Campsite': ['outdoors', 'family-friendly', 'sporty', 'historic'],
    'Casino/Gaming': ['indoors', 'geeky', 'sporty'],
    'Childrens Festival': ['indoors', 'family-friendly', 'sporty', 'artsy'],
    'Fairs & Festivals': ['indoors', 'family-friendly', 'sporty'],
    'Festival': ['outdoors', 'artsy'],
    'Food & Drink': ['indoors', 'family-friendly','romantic', 'hungry'],
    'Health/Wellness': ['outdoors', 'sporty', 'artsy'],
    'Museum': ['indoors', 'family-friendly', 'historic', 'geeky', 'artsy'],
    'Music': ['outdoors', 'artsy'],
    'Sports': ['outdoors', 'family-friendly', 'sporty']
    }


def get_all_events():
    event_list = []

    for classification in CLASSIFICATIONS.keys():
        # Parameters for get request which includes , apikey, classifications and event date times.
        client_info = {
            'classificationName': classification,
            'apikey': API_KEY,
            'source': 'ticketmaster',
            'countryCode': 'AU',
            'stateCode': 'NSW',
            }

        response = requests.get(url=URL, params=client_info)
        data = json.loads(response.text)
        
        if '_embedded' in data:
            events = data['_embedded']['events']
            
            for info in events:
                event_list.append(parseInfoToEvent(info, classification))

    return event_list


def parseInfoToEvent(info, classification):
    start_time = ""
    end_time = ""
    url = ""
    summary = ""
    organiser = ""
    tags = CLASSIFICATIONS.get(classification)
    latitude = ""
    longitude = ""
    is_online = True
    rating = 0
    price = 0 
    image = ""
    if info['dates']['status']['code'] == 'cancelled':
        is_online = False
    if 'dates' in info:
        if 'start' in info['dates']:
            if 'dateTime' in info['dates']['start']:
                start_time = info['dates']['start']['dateTime']
    if 'location' in info['_embedded']['venues'][0]: 
        latitude = info['_embedded']['venues'][0]['location']['latitude']
        longitude = info['_embedded']['venues'][0]['location']['longitude']
    if 'info' in info:
        summary = info['info']
    if 'promoter' in info:
        organiser = info['promoter']['name']
    if 'url' in info:
        url = info['url']
    if 'images' in info:
        if 'url' in info['images'][0]:
            image = info['images'][0]['url']
    if 'priceRanges' in info:
        price = info['priceRanges'][0]['min']
    
    event_info = Event(info['id'], url, start_time, end_time, latitude, longitude, 
        info['name'], organiser, price, is_online, summary, "", rating, image, tags)

    return event_info
