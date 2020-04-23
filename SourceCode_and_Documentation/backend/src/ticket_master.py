import json, requests, datetime
from src.event import Event

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
    print('Ticketmaster')

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
    start_time = 0.0
    end_time = 0.0

    url = ""
    summary = ""
    organiser = ""
    tags = CLASSIFICATIONS.get(classification)
    latitude = 0.0
    longitude = 0.0
    is_online = True
    rating = 0
    price = 0 
    # The ticket master API only has a price, so the price_tier will remain an arbitrary value.
    price_tier = 0
    image = ""
    
    if info['dates']['status']['code'] == 'cancelled':
        is_online = False
    if 'dates' in info:
        if 'start' in info['dates']:
            if 'dateTime' in info['dates']['start']:
                dt = datetime.datetime.strptime(info['dates']['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
                start_time = dt.timestamp()
                end_time = (dt + datetime.timedelta(hours=4)).timestamp()

    if 'location' in info['_embedded']['venues'][0]: 
        latitude = float(info['_embedded']['venues'][0]['location']['latitude'])
        longitude = float(info['_embedded']['venues'][0]['location']['longitude'])
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
        info['name'], organiser, price, is_online, summary, "", tags, price_tier, rating, image)

    return event_info
