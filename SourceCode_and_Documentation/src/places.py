import json, requests
from event import Event

URL = 'https://api.foursquare.com/v2/venues/search'


# A dictionary containing the category id of all
# the required categories.
CATEGORIES = {
    'artsy': '4d4b7104d754a06370d81259', 
    'athletics': '4f4528bc4b90abdf24c9de85', 
    'bar': '4bf58dd8d48988d116941735', 
    'beach': '4bf58dd8d48988d1e2941735', 
    'cafe': '4bf58dd8d48988d16d941735', 
    'clothes': '4bf58dd8d48988d103951735', 
    'events': '4d4b7105d754a06373d81259', 
    'food': "4d4b7105d754a06374d81259", 
    'gaming cafes': '4bf58dd8d48988d18d941735',
    'uni': '4bf58dd8d48988d1a8941735', 
              }


def get_all_events():

    event_list = []
    
    for category in CATEGORIES.values():

        # params include ll as the latitude and longitude of the city or suburb to search in.
        params = dict(

            client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
            client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
            v='20180604',
            categoryId=category,
            limit='100000',
            radius='100000',
            ll='-33.8671417236,151.2071075439'

        )

        # GET request for the list of places.
        response = requests.get(url=URL, params=params)
        data = json.loads(response.text)
        venues = data['response']['venues']

        for venue in venues:

            y = venue

            time = None
            start_time = None
            end_time = None
            url = None
            description = None
            price = None
            rating = []

            if ('hours' in y):

                time = y['hours']['timeframes']
                line = str(time[0]['open'][0]['renderedTime'])
                line = line.split("–")
                start_time = line[0]
                end_time = line[1]

            if ('url' in y):
                url = y['url']

            if ('rating' in y):
                rating.append(y['rating'])

            if('description' in y):
                description = y['description']

            if ('price'in y):
                price = y['price']['currency']
            
            event_obj = Event(y['id'], start_time, end_time, y['location']['lat'], y['location']
              ['lng'], y['name'], None, price, None, description, url, None, rating)

            event_list.append(event_obj)

    return event_list

def get_event_details(id):
    
    params_prem = dict(
        client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
        client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
        v='20180604'
    )

    PREMIUM_URL = 'https://api.foursquare.com/v2/venues/'
    call_url = PREMIUM_URL + id
            
    premium_response = requests.get(url=call_url, params=PARAMS_PREM)
    premium_data = json.loads(premium_response.text)
            
    return premium_data['response']['venue']
