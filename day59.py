city=input("enter the city name: ")

api="http://api.openweathermap.org/data/2.5/weather?q=ranchi&appid=8e77b1f813676d04e79237519c69abb8"

import requests

response = requests.get(api)
jsondata = response.json()
jsondata['main']['temp']
    



#api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e9185b28e9969fb7a300801eb026de9c"