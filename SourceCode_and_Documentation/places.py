import json, requests
import pprint
url1 = 'https://api.foursquare.com/v2/venues/search'
url2 = 'https://api.foursquare.com/v2/venues/explore'

locations = {}

params = dict(
  client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
  client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
  v='20180604',
  categoryID='4d4b7105d754a06374d81259',
  #near='Sydney,NSW',
  limit=100000,
  radius=100000,
  ll='-33.8671417236,151.2071075439'
)

params1 = dict(
  client_id='DEPF4JDYDGBETTC5RDGFWUZTZIB2DDASK4XGU2H0POZSUGO0',
  client_secret='XZP10N5EEDLDVNT04WPSFYUMWPX20LVCFGMC2JMWKXHRG2AI',
  v='20180604',
  near='Sydney,NSW',
  limit=600,
  radius=100000,
)
resp1 = requests.get(url=url1, params=params)
resp2 = requests.get(url=url1, params=params1)

data1 = json.loads(resp1.text)
data2 = json.loads(resp2.text)
data1 = data1['response']['venues']
data2 = data2['response']['venues']
 
count = 0
for i in data1:
  print(i['name'] + ' ' + str(i['location']['lat']) + ' ' + str(i['location']['lng']))
  count+=1

print ('--------------------------------------------------------------------------------------')

for j in data2:
  print(j['name'] + ' ' + str(j['location']['lat']) + ' ' + str(j['location']['lng']))
  count+=1

print(count)