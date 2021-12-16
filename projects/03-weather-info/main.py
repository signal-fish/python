import requests
from pprint import pprint

API_Key = '513913dcab31efd0ea1ca17f6944e4d8'
city = input('Enter a city: ')
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()
pprint(weather_data)
