import requests

data_id = {'access_token':'token', 'device_id':"70:ee:50:27:5f:e8"}
data_fav = {'access_token':'token', 'get_favorites':"true"}

r = requests.get('https://api.netatmo.com/api/getstationsdata', params=data_fav)
print(r.url)
print(r.text)