import json, requests
from event import Event

URL = 'https://api.foursquare.com/v2/venues/search'
PREMIUM_URL = 'https://api.foursquare.com/v2/venues/'

# A dictionary containing the category id of all
# the required categories.
CATEGORIES = { 
    'arcade':'4bf58dd8d48988d1e1931735',
    'general-entertainment':'4bf58dd8d48988d1f1931735',
    'movie':'4bf58dd8d48988d17f941735',
    'water-park':'4bf58dd8d48988d193941735',
    'zoo':'4bf58dd8d48988d17b941735',
    'performing-arts':'4bf58dd8d48988d1f2931735',
    'festival': '5267e4d9e4b0ec79466e48c7',
    'events': '4d4b7105d754a06373d81259', 
    'public-art':'507c8c4091d498d9fc8c67a9',
    'tech-startup':'4bf58dd8d48988d125941735',
    'diner':'4bf58dd8d48988d147941735',
    'cafe': '4bf58dd8d48988d16d941735',
    'bar': '4bf58dd8d48988d116941735', 
    'gaming-cafes':'4bf58dd8d48988d18d941735',
    'beach': '4bf58dd8d48988d1e2941735', 
    'gym': '4bf58dd8d48988d175941735',
    'fishing-spot':'52e81612bcbc57f1066b7a0f',
    'national-park':'52e81612bcbc57f1066b7a21',
    'clothes': '4bf58dd8d48988d103951735', 
    'museum': '4bf58dd8d48988d181941735'
    }   

# A dict containing all the relevant tags to the items in
# CATEGORIES dict.
CATEGORIES_TAGS = {
    'arcade':['indoors','family-friendly','sporty'],
    'general-entertainment':['indoors','family-friendly'],
    'movie':['indoors','family-friendly'],
    'water-park':['outdoors','family-friendly','sporty'],
    'zoo':['outdoors','family-friendly','geeky','historic'],
    'festival':['outdoors','family-friendly'],
    'events':['outdoors','artsy'],
    'diner':['romantic','indoors','hungry','family-friendly'],
    'cafe':['romantic','indoors','hungry'],
    'bar':['romantic','indoors','hungry','artsy'],
    'beach':['family-friendly','outdoors','sporty'],
    'gym':['indoors','sporty'],
    'fishing-spot':['outdoors','family-friendly','sporty'],
    'national-park':['outdoors','family-friendly','sporty','historic'],
    'clothes':['indoors','family-friendly'],
    'museum':['indoors','geeky','artsy','historic','family-friendly'],
    'performing-arts':['indoors','artsy','sporty','family-friendly'],
    'public-art':['outdoors','artsy','family-friendly'],
    'tech-startup':['indoors','geeky'],
    'gaming-cafes':['indoors','sporty','geeky']
    }

def get_all_events():
    event_list = []
    
    for category in CATEGORIES.values():
        # params include ll as the latitude and longitude of the city or suburb to search in.
        client_info = dict(
            client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
            client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
            v='20180604',
            categoryId=category,
            limit=60,
            radius='100000',
            ll='-33.8671417236,151.2071075439'
        )

        response = requests.get(url=URL, params=client_info)
        data = json.loads(response.text)
        venues = data['response']['venues']

        for venue in venues:
            event = parseVenueToEvent(venue,category)
            event_list.append(event)

    return event_list

def get_event_details(id):
    premium_client_info = dict(
        client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
        client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
        v='20180604'
    )
    call_url = PREMIUM_URL + id
            
    premium_response = requests.get(url=call_url, params=premium_client_info)
    premium_data = json.loads(premium_response.text)
            
    return premium_data['response']['venue']

def parseVenueToEvent(venue, category):
    time = ""
    start_time = ""
    end_time = ""
    url = ""
    description = ""
    price = True
    is_online = True
    
    if 'hours' in venue:
        time = venue['hours']['timeframes']
        line = str(time[0]['open'][0]['renderedTime'])
        line = line.split("–")
        start_time = line[0]
        end_time = line[1]
    if 'url' in venue:
        url = venue['url']
    if 'description' in venue:
        description = venue['description']
    if 'price'in venue:
        price = False

    key = (list(CATEGORIES.keys())[list(CATEGORIES.values()).index(category)])
   
    event_obj = Event(venue['id'], url,start_time, end_time, venue['location']['lat'], venue['location']
        ['lng'], venue['name'], "",price, is_online, description, CATEGORIES_TAGS.get(key), [])
    
    return event_obj
