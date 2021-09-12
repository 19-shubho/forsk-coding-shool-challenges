import requests

cityNm=input('Enter the name of the city: ')

city="http://api.openweathermap.org/geo/1.0/direct?q="+cityNm+"&limit=1&appid=f6a83834813667ac6507638cb6ae37d2"

resp=requests.get(city)

print (resp.json()[0])
#record the latitude and longitude in seperate variables -->
lat=str(resp.json()[0]['lat'])
long=str(resp.json()[0]['lon'])

#air quality api call -->
AirQ="http://api.openweathermap.org/data/2.5/air_pollution?lat="+lat+"&lon="+long+"&appid=f6a83834813667ac6507638cb6ae37d2"

resp1=requests.get(AirQ)

print (resp.json())


