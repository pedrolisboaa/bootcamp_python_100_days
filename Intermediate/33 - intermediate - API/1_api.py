import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
data = response.json()['iss_position']

latitude = data['latitude']
longitude = data['longitude']

position = (latitude, longitude)
print(position)

