import json, requests
from event import Event

url = 'https://api.foursquare.com/v2/venues/search'


categories_dict = {'food':"4d4b7105d754a06374d81259"
              ,'events':'4d4b7105d754a06373d81259'
              ,'artsy':'4d4b7104d754a06370d81259'
              ,'uni':'4bf58dd8d48988d1a8941735'
              , 'cafe': '4bf58dd8d48988d16d941735'
              , 'bar': '4bf58dd8d48988d116941735'
              , 'athletics': '4f4528bc4b90abdf24c9de85'
              , 'beach': '4bf58dd8d48988d1e2941735'
              , 'clothes': '4bf58dd8d48988d103951735'
              ,'gaming cafes': '4bf58dd8d48988d18d941735'
              }

categories_list = list(categories_dict.values())

locations = {}
return_list = []
count = 0


params_prem = dict(
    client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
    client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
    v='20180604',
  )



for i in categories_list:


  params = dict(
    client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
    client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
    v='20180604',
    categoryId=categories_list[0],
    #near='Sydney,NSW',
    limit=100000,
    radius=100000,
    ll='-33.8671417236,151.2071075439'
  )

  premium_url = 'https://api.foursquare.com/v2/venues/4b09e0e4f964a520151f23e3'
  response = requests.get(url=url1, params=params)
  data = json.loads(response.text)
  data = data['response']['venues']


  for x in data:
    
    '''
    premium_url = 'https://api.foursquare.com/v2/venues/'
    call_url = premium_url + x['id']
    
    premium_response = requests.get(url=call_url, params=params_prem)
    premium_data = json.loads(premium_response.text)
    
    y = premium_data['response']['venue']
    '''

    y = x

    time = None
    start_time = None
    end_time = None
    url = None
    description = None
    price = None
    rating = []

    if ('hours' in y):
      time = y['hours']['timeframes']
      line = (time[0]['open'][0]['renderedTime'])
      line = str(line)
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

    
    print(y['name'] + ' ' + str(y['location']['lat']) + ' ' + str(y['location']['lng']) + ' ' +str(start_time) + ' ' + str(end_time) + ' ' + str(description) + ' ' + str(rating))
    event_obj = Event(y['id'],start_time,end_time,y['location']['lat'],y['location']['lng'],y['name'],None,price,None,description,url,None,rating)
    return_list.append(event_obj)
    
    count+=1
    print('------------------------------------------------------------------------------------')

print (count)

